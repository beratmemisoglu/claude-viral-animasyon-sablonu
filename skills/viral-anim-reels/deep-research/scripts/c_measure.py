"""Analyst C - visual edit-rhythm measurement.
Usage: python -I c_measure.py <research_root>
Decodes every video at 10 fps / 90x160 via ffmpeg pipe, computes:
 - hard cuts (big frame diff + histogram change)
 - "visual state changes" (anchor-based: composition drifted far from the last anchor;
   counts morphs / camera-move transitions that scene>0.15 misses)
 - camera motion classes on 0.5 s steps (static / pan / zoom / other-motion)
 - holds (>=1 s nearly static)
 - HSV brightness / saturation, k-means palette
 - alignment of state changes to word onsets (subs.en-orig.json3)
Caption band (rows 52%-80%) is masked out for motion metrics because burned-in
word captions change every ~0.3 s.
"""
import sys, os, json, subprocess, glob
import numpy as np
from PIL import Image

ROOT = sys.argv[1]
W, H, FPS = 90, 160, 10
OUT = os.path.join(ROOT, 'analysis', 'scripts', 'out')
os.makedirs(OUT, exist_ok=True)
MASK = np.ones((H, W), bool)
MASK[int(H * .52):int(H * .80), :] = False
STOP = set("the a an and or but of to in on at for with by from is was were be been are it its it's this that these those he she they them his her their you your we our i me my as so if then than there here what who why how when where which not no just only also very all any one into out up down over after before about".split())


def decode(path):
    cmd = ['ffmpeg', '-v', 'error', '-i', path, '-vf', f'fps={FPS},scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (W * H * 3)
    return np.frombuffer(raw[:n * W * H * 3], np.uint8).reshape(n, H, W, 3)


def gray(f):
    return f.astype(np.float32) @ np.array([.299, .587, .114], np.float32)


def hist(f):
    q = (f[MASK] // 64).astype(np.int32)
    h = np.bincount(q[:, 0] * 16 + q[:, 1] * 4 + q[:, 2], minlength=64).astype(np.float32)
    return h / h.sum()


def phase_shift(a, b):
    A = np.fft.fft2(a - a.mean()); B = np.fft.fft2(b - b.mean())
    R = A * np.conj(B); R /= np.abs(R) + 1e-6
    r = np.real(np.fft.ifft2(R))
    i = np.unravel_index(np.argmax(r), r.shape)
    peak = r[i] / (r.std() + 1e-6)
    dy, dx = i
    if dy > a.shape[0] // 2: dy -= a.shape[0]
    if dx > a.shape[1] // 2: dx -= a.shape[1]
    return dx, dy, peak


def zoom_err(a, b, s):
    # scale frame a by s about centre, compare to b on masked centre region
    if s == 1.0:
        return np.abs(a - b)[MASK].mean()
    im = Image.fromarray(a)
    nw, nh = int(round(W * s)), int(round(H * s))
    im2 = np.asarray(im.resize((nw, nh), Image.BILINEAR), np.float32)
    if s > 1:
        ox, oy = (nw - W) // 2, (nh - H) // 2
        a2 = im2[oy:oy + H, ox:ox + W]
        return np.abs(a2 - b)[MASK].mean()
    ox, oy = (W - nw) // 2, (H - nh) // 2
    sub = b[oy:oy + nh, ox:ox + nw]
    m = MASK[oy:oy + nh, ox:ox + nw]
    return np.abs(im2 - sub)[m].mean()


def words(d):
    p = os.path.join(d, 'subs.en-orig.json3')
    out = []
    if not os.path.exists(p):
        return out
    js = json.load(open(p, encoding='utf8'))
    for ev in js.get('events', []):
        t0 = ev.get('tStartMs', 0)
        for s in ev.get('segs', []) or []:
            w = s.get('utf8', '').strip()
            if w and w != '\n':
                out.append(((t0 + s.get('tOffsetMs', 0)) / 1000, w))
    return out


def kmeans(X, k=8, it=25, seed=0):
    rng = np.random.default_rng(seed)
    C = X[rng.choice(len(X), k, replace=False)].astype(np.float32)
    for _ in range(it):
        d = ((X[:, None, :] - C[None]) ** 2).sum(-1)
        l = d.argmin(1)
        for j in range(k):
            if (l == j).any():
                C[j] = X[l == j].mean(0)
    cnt = np.bincount(l, minlength=k)
    o = np.argsort(-cnt)
    return C[o], cnt[o] / cnt.sum()


def analyse(d):
    fr = decode(os.path.join(d, 'video.mp4'))
    n = len(fr); dur = n / FPS
    G = np.stack([gray(f) for f in fr])
    # 1) consecutive diffs (masked)
    dif = np.array([np.abs(G[i] - G[i - 1])[MASK].mean() for i in range(1, n)])
    hs = np.stack([hist(f) for f in fr])
    hd = np.array([0.5 * np.abs(hs[i] - hs[i - 1]).sum() for i in range(1, n)])
    raw_cuts = [i / FPS for i in range(1, n) if dif[i - 1] > 22 and hd[i - 1] > .25]
    cuts = []
    for c in raw_cuts:  # merge multi-frame dissolves (<0.4 s apart) into one transition
        if not cuts or c - cuts[-1] > 0.4:
            cuts.append(c)
    # coarse "new composition" count at a stricter threshold (40) for robustness
    def count_states(T):
        anc = None; k = 0; lst = -9
        for i in range(n):
            if anc is None: anc = th[i]; continue
            if np.abs(th[i] - anc)[tm].mean() > T:
                anc = th[i]
                if i - lst >= 3: k += 1; lst = i
        return k
    # 2) anchor-based state changes on 16x28 blurred thumbnails
    th = np.stack([np.asarray(Image.fromarray(g.astype(np.uint8)).resize((16, 28), Image.BOX), np.float32) for g in G])
    tm = np.asarray(Image.fromarray(MASK.astype(np.uint8) * 255).resize((16, 28), Image.NEAREST)) > 0
    anchor = th[0]; last = 0; changes = []
    for i in range(1, n):
        dd = np.abs(th[i] - anchor)[tm].mean()
        if dd > 28 and (i - last) >= 3:  # >=0.3 s apart
            changes.append(i / FPS); anchor = th[i]; last = i
        elif dd > 28:
            anchor = th[i]
    changes40 = count_states(40)
    # 3) camera classes on 0.5 s steps
    step = 5; cls = []
    for i in range(0, n - step, step):
        a, b = G[i], G[i + step]
        base = np.abs(a - b)[MASK].mean()
        if base < 2.0:
            cls.append('static'); continue
        if any(i < c * FPS <= i + step for c in cuts):
            cls.append('cut'); continue
        dx, dy, pk = phase_shift(a, b)
        errs = {s: zoom_err(a, b, s) for s in (0.94, 0.965, 0.985, 1.0, 1.015, 1.035, 1.06)}
        bs = min(errs, key=errs.get)
        if bs != 1.0 and errs[bs] < 0.8 * base:
            cls.append('zoom_in' if bs > 1 else 'zoom_out')
        elif (abs(dx) + abs(dy)) >= 1 and pk > 8:
            cls.append('pan_h' if abs(dx) >= abs(dy) else 'pan_v')
        else:
            cls.append('other_motion')
    # holds: runs of static >=1 s (2 steps)
    holds = []; run = 0
    for c in cls + ['x']:
        if c == 'static': run += 1
        else:
            if run >= 2: holds.append(run * step / FPS)
            run = 0
    # 4) colour
    hsv = np.stack([np.asarray(Image.fromarray(f).convert('HSV'), np.float32) for f in fr[::FPS]])
    bri = hsv[..., 2].mean() / 255 * 100; sat = hsv[..., 1].mean() / 255 * 100
    px = fr[::FPS][:, MASK].reshape(-1, 3)
    # 5) per 10 s window
    nw = int(np.ceil(dur / 10))
    win = [sum(1 for c in changes if k * 10 <= c < (k + 1) * 10) for k in range(nw)]
    # 6) word alignment
    ws = words(d)
    onsets = np.array([t for t, w in ws]) if ws else np.array([])
    content = np.array([t for t, w in ws if w.lower().strip('.,!?"\'') not in STOP and len(w) >= 4]) if ws else np.array([])
    def near(ts, ref, tol=0.3):
        if len(ref) == 0 or len(ts) == 0: return None
        return float(np.mean([np.min(np.abs(ref - t)) <= tol for t in ts]))
    rng = np.random.default_rng(1)
    rand = rng.uniform(0.5, max(dur - 0.5, 1), 400)
    gaps = np.diff([0] + changes + [dur])
    return dict(dur=round(dur, 1), cuts=len(cuts), cut_times=[round(c, 1) for c in cuts], changes=len(changes), changes40=changes40, shot_len=round(dur / (len(cuts) + 1), 2),
                change_times=[round(c, 1) for c in changes], changes_per10=round(len(changes) / dur * 10, 2),
                median_gap=round(float(np.median(gaps)), 2), mean_gap=round(float(np.mean(gaps)), 2),
                win=win, cls={k: round(cls.count(k) / len(cls) * 100, 1) for k in set(cls)},
                moving_pct=round(100 * (1 - cls.count('static') / len(cls)), 1),
                holds=holds, hold_total=round(sum(holds), 1), longest_hold=max(holds) if holds else 0,
                mean_diff=round(float(dif.mean()), 2), bri=round(float(bri), 1), sat=round(float(sat), 1),
                align_content=near(changes, content), align_any=near(changes, onsets),
                align_content_chance=near(rand, content), px=px[::7].tolist())


def main():
    res = {}
    for ch in ('ricksclips', 'competitors'):
        for d in sorted(glob.glob(os.path.join(ROOT, 'videos', ch, '*'))):
            vid = os.path.basename(d)
            if not os.path.exists(os.path.join(d, 'video.mp4')):
                continue
            m = json.load(open(os.path.join(d, 'meta.json'), encoding='utf8'))
            r = analyse(d)
            r.update(ch=m.get('channel'), title=m.get('title'), views=m.get('view_count'), date=m.get('upload_date'))
            res[vid] = r
            print(vid, r['ch'], r['dur'], 'cuts', r['cuts'], 'chg', r['changes'], 'per10', r['changes_per10'], 'mov', r['moving_pct'], flush=True)
    # palettes per channel
    pal = {}
    for chn in sorted(set(r['ch'] for r in res.values())):
        X = np.array([p for r in res.values() if r['ch'] == chn for p in r['px']], np.float32)
        if len(X) > 60000:
            X = X[np.random.default_rng(0).choice(len(X), 60000, replace=False)]
        C, w = kmeans(X, 10)
        pal[chn] = [('#%02x%02x%02x' % tuple(int(v) for v in c), round(float(x) * 100, 1)) for c, x in zip(C, w)]
    for r in res.values():
        r.pop('px')
    json.dump(dict(videos=res, palettes=pal), open(os.path.join(OUT, 'c_measure.json'), 'w'), indent=1)
    print(json.dumps(pal, indent=1))


if __name__ == '__main__':
    main()
