"""D — burned-in caption measurement.
Usage: python -I d_captions.py <video_dir> [<video_dir> ...]  -> prints one JSON line per video
Heuristic: caption pixels = bright fill (white or yellow) lying next to dark stroke/shadow pixels,
inside a horizontal band found from the temporal row profile. Measures at 10 fps on the native 720x1280
frame (all videos are 720x1280); px values are reported scaled to a 1080x1920 canvas (x1.5).
Caption change events are matched to json3 word onsets to estimate sync offset.
"""
import sys, os, json, subprocess, glob
import numpy as np
from scipy import ndimage as ndi
sys.stdout.reconfigure(encoding="utf-8")

FPS = 10
Y0, Y1 = 560, 1200          # search band on 720x1280 frame
W = 720
H = Y1 - Y0
SC = 1.5                    # 720 -> 1080


def words_from_json3(d):
    f = [x for x in glob.glob(os.path.join(d, "*.json3")) if "en-orig" in x] or glob.glob(os.path.join(d, "*.json3"))
    j = json.load(open(f[0], encoding="utf-8"))
    out = []
    for ev in j.get("events", []):
        t0 = ev.get("tStartMs", 0)
        for s in ev.get("segs", []) or []:
            w = s.get("utf8", "").strip()
            if not w or w.startswith("[") or w == "\n":
                continue
            out.append(((t0 + s.get("tOffsetMs", 0)) / 1000.0, w))
    out.sort()
    return out


def frames(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={FPS},crop={W}:{H}:0:{Y0}",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    n = W * H * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n:
            break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)


def cand_mask(fr):
    r, g, b = fr[..., 0].astype(int), fr[..., 1].astype(int), fr[..., 2].astype(int)
    mn = np.minimum(np.minimum(r, g), b); mx = np.maximum(np.maximum(r, g), b)
    white = mn > 205
    yellow = (r > 190) & (g > 160) & (b < 120)
    fill = white | yellow
    dark = mx < 80
    near = ndi.binary_dilation(dark, iterations=4)
    c = fill & near
    c[:, :40] = False; c[:, -40:] = False
    return c, white, yellow, dark


def analyse(d):
    vid = os.path.join(d, "video.mp4")
    masks, metas = [], []
    for fr in frames(vid):
        c, white, yellow, dark = cand_mask(fr)
        masks.append(np.packbits(c, axis=1))
        metas.append((int(white[c].sum()), int(yellow[c].sum())))
    if not masks:
        return None
    M = [np.unpackbits(m, axis=1)[:, :W].astype(bool) for m in masks]
    prof = np.mean([m.sum(1) for m in M], axis=0)
    pk = int(np.argmax(prof))
    thr = prof[pk] * 0.25
    a = pk
    while a > 0 and prof[a - 1] > thr: a -= 1
    b = pk
    while b < H - 1 and prof[b + 1] > thr: b += 1
    a = max(0, a - 12); b = min(H - 1, b + 12)
    # per frame stats inside band
    present, heights, ycent, widths, sigs = [], [], [], [], []
    for m in M:
        band = m[a:b + 1]
        lab, n = ndi.label(band)
        if n:
            sizes = ndi.sum(band, lab, range(1, n + 1))
            keep = np.isin(lab, 1 + np.where(sizes >= 12)[0])
        else:
            keep = band
        cnt = int(keep.sum())
        ok = cnt > 150
        present.append(ok)
        if ok:
            ys, xs = np.where(keep)
            # robust bbox (2..98 pct)
            y_lo, y_hi = np.percentile(ys, [1, 99]); x_lo, x_hi = np.percentile(xs, [1, 99])
            heights.append(y_hi - y_lo); ycent.append(a + Y0 + (y_lo + y_hi) / 2); widths.append(x_hi - x_lo)
            sigs.append(keep[::2, ::2])
        else:
            sigs.append(None)
    # change events
    ev = []
    prev = None
    for i, s in enumerate(sigs):
        if s is None:
            prev = None; continue
        if prev is None:
            ev.append(i / FPS)
        else:
            inter = (s & prev).sum(); uni = (s | prev).sum()
            if uni and inter / uni < 0.35:
                ev.append(i / FPS)
        prev = s
    words = words_from_json3(d)
    wt = np.array([w[0] for w in words]) if words else np.array([0.0])
    offs = []
    for t in ev:
        k = np.argmin(np.abs(wt - t))
        dt = t - wt[k]
        if abs(dt) <= 0.4:
            offs.append(dt)
    dur = len(M) / FPS
    # spans between events while text present
    cards = []
    for i, t in enumerate(ev):
        t_end = ev[i + 1] if i + 1 < len(ev) else dur
        cards.append(t_end - t)
    wsum = sum(metas[i][0] for i in range(len(metas))); ysum = sum(metas[i][1] for i in range(len(metas)))
    res = dict(
        id=os.path.basename(d), dur=round(dur, 1),
        band_y_1080=[round((a + Y0) * SC), round((b + Y0) * SC)],
        pct_frames_with_caption=round(100 * np.mean(present), 1),
        text_h_med_1080=round(float(np.median(heights)) * SC, 1) if heights else None,
        y_center_med_1080=round(float(np.median(ycent)) * SC) if ycent else None,
        y_center_pct=round(float(np.median(ycent)) / 1280 * 100, 1) if ycent else None,
        width_med_1080=round(float(np.median(widths)) * SC) if widths else None,
        width_p90_1080=round(float(np.percentile(widths, 90)) * SC) if widths else None,
        n_events=len(ev), n_words=len(words),
        words_per_card=round(len(words) / max(1, len(ev)), 2),
        card_dur_med=round(float(np.median(cards)), 2) if cards else None,
        events_matched_pct=round(100 * len(offs) / max(1, len(ev)), 1),
        sync_offset_med_ms=round(1000 * float(np.median(offs))) if offs else None,
        sync_offset_iqr_ms=[round(1000 * float(x)) for x in np.percentile(offs, [25, 75])] if offs else None,
        yellow_share=round(ysum / max(1, wsum + ysum), 3),
    )
    return res


if __name__ == "__main__":
    for d in sys.argv[1:]:
        try:
            r = analyse(d)
        except Exception as e:
            r = dict(id=os.path.basename(d), error=str(e))
        print(json.dumps(r, ensure_ascii=False), flush=True)
