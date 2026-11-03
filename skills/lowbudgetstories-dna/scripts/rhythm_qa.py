#!/usr/bin/env python3
"""rhythm_qa.py - edit-rhythm + sound QA gate for Low-Budget-Stories-style videos.

Measures a finished video and compares it with the norms measured on the 10 most-viewed
@LowBudgetStories videos (see deep-research/L4-audio-edit-rhythm.md for how they were derived).

Needs: ffmpeg + ffprobe on PATH, Python 3.9+, numpy, Pillow (Pillow only for --montage).  No OpenCV, no librosa.
Usage:
  python rhythm_qa.py VIDEO.mp4 [--transcript words.json] [--mode voiced|wordless|auto] [--out qa_out]
                                [--hold 8] [--montage] [--quiet]
  --transcript  faster-whisper style JSON ({"segments":[{"start","end","text","words":[{"w","s","e"}]}]}) or a
                plain list of [start,end] speech intervals. Enables speech-vs-bed loudness, WPM and pause checks.
  --mode        voiced = dialogue story (default when a transcript with >=50 words is given),
                wordless = music + pantomime story (default otherwise).
Outputs (in --out): report.json, shots.csv (every shot), seconds.csv (per-second map: cut flag, loudness,
                    silence, music/side level, speech), montage_cuts.jpg (with --montage: before/after of every cut
                    so a human can confirm cuts vs. camera moves).
Exit code: 0 = no FAIL, 1 = at least one FAIL (WARNs never fail the gate).

Shot-boundary model (calibrated by eye on before/after montages of every boundary in v07, v08 and v10):
  cut       one-frame change: 1-corr(grey) or colour-histogram distance > 0.30 AND >= 2.5x the 3 neighbouring steps
            (histogram-only jumps while the picture keeps its structure = fade, ignored)
  reframe   4-12 frame burst between two stable framings of one composite (quick zoom / whip) or a cut into moving
            footage -- the channel's main way to "cut" without new art; counted as a boundary
  pan       13-35 frame eased slide between two speakers on one wide plate (shot/reverse-shot without a cut)
  dissolve  frame t ~ blend of t-0.48 s and t+0.48 s (residual < 35 % of the scene difference), scenes differ
  black     mean luma < 6/255 for >= 0.2 s (black hold / fade); its own shot; the opening fade-in (< 1 s) is ignored
Slow push-ins, parallax walkers, characters crossing the frame and pose swaps are NOT boundaries; they are reported
as in-shot motion (camera class per shot, pose-swap events/min).
The story ends where the end card starts (last static shot >= 2 s inside the final 25 s); shot statistics and
cuts/min are computed on the story only.
"""
import argparse, json, math, os, re, subprocess, sys
import numpy as np

FPS = 25                     # analysis frame rate (videos at 50 fps are resampled)
SW, SH = 96, 54              # analysis frame size for boundaries
ZW, ZH, ZFPS = 192, 108, 5   # grey frames for zoom/pan estimation

# ----------------------------------------------------------------------------------------------------------------
# Corpus norms: measured with this script on the 10 most-viewed videos (v01-v10, 2.4M-6.3M views), see
# deep-research/L4-audio-edit-rhythm.md.  PASS band = corpus range (lightly rounded); outside -> WARN;
# FAIL = clearly outside anything the corpus does.  Bands marked * are tightened to the top-6 (>= 3.4M views)
# where the lower-ranked videos drift (long talky holds in v05/v06/v09/v10).
NORMS = {
    'common': {
        'cuts_per_min_total':   dict(lo=14.0, hi=23.5, fail_lo=11.0, fail_hi=28.0),   # corpus 14.2-23.5
        'median_shot_s':        dict(lo=2.2, hi=3.7, fail_lo=1.6, fail_hi=5.0),       # 2.28-3.60
        'mean_shot_s':          dict(lo=2.5, hi=4.3, fail_lo=2.0, fail_hi=6.0),       # 2.53-4.23
        'p90_shot_s':           dict(lo=3.6, hi=7.7, fail_lo=3.0, fail_hi=10.0),      # 3.66-7.63
        'cuts_per_min_0_15':    dict(lo=14.0, hi=28.0, fail_lo=6.0, fail_hi=40.0),    # 8-28 (v10 = chapter card)
        'cuts_per_min_15_60':   dict(lo=16.0, hi=27.0, fail_lo=10.0, fail_hi=36.0),   # 16.0-26.7
        'cuts_per_min_body':    dict(lo=12.5, hi=25.5, fail_lo=9.0, fail_hi=32.0),    # 12.9-25.3
        'cuts_per_min_last30':  dict(lo=10.0, hi=24.0, fail_lo=3.0, fail_hi=32.0),    # 4-24
        'max_shot_s':           dict(lo=4.0, hi=10.0, fail_lo=0.0, fail_hi=36.0),     # * top-6 <= 10; v10 35
        'holds_over_hold_per_10min': dict(lo=0.0, hi=9.0, fail_lo=0.0, fail_hi=20.0), # 0-12; top-6 0-8.8
        'first_cut_s':          dict(lo=1.3, hi=5.7, fail_lo=0.0, fail_hi=10.0),      # 1.36-5.64
        'end_card_s':           dict(lo=4.8, hi=15.0, fail_lo=3.0, fail_hi=25.0),     # 4.9-14.6
        'black_hold_total_s':   dict(lo=0.0, hi=8.5, fail_lo=0.0, fail_hi=25.0),      # 0-20.2
        'loudness_range_lu':    dict(lo=9.5, hi=13.0, fail_lo=6.0, fail_hi=18.0),     # 9.6-15.7
        'dramatic_silences':    dict(lo=0.0, hi=6.0, fail_lo=0.0, fail_hi=12.0),      # >= 1 s, 0-6
    },
    'voiced': {
        'integrated_lufs':      dict(lo=-22.5, hi=-16.5, fail_lo=-26.0, fail_hi=-13.0),  # -22.5..-16.6
        'speech_share_pct':     dict(lo=31.0, hi=58.0, fail_lo=20.0, fail_hi=75.0),      # 31.7-57.3
        'first_word_s':         dict(lo=3.0, hi=33.0, fail_lo=0.0, fail_hi=60.0),        # 3.1-32.6
        'wpm_in_turns':         dict(lo=150.0, hi=205.0, fail_lo=120.0, fail_hi=235.0),  # 151-204
        'bed_below_voice_lu':   dict(lo=2.5, hi=12.0, fail_lo=1.0, fail_hi=18.0),        # 2.8-11.9
        'music_change_at_speech_onset_db': dict(lo=-3.0, hi=2.5, fail_lo=-12.0, fail_hi=8.0),  # -2.7..+2.0 = no ducking
        'longest_wordless_s':   dict(lo=16.0, hi=60.0, fail_lo=5.0, fail_hi=90.0),       # 22.4-60.0
    },
    'wordless': {
        'integrated_lufs':      dict(lo=-15.0, hi=-10.0, fail_lo=-20.0, fail_hi=-8.0),   # -14.6, -10.5
    },
}

# ----------------------------------------------------------------------------------------------------------------
def run(cmd, text=False):
    return subprocess.run(cmd, capture_output=True, text=text, errors='ignore' if text else None)

def probe(video):
    r = run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,r_frame_rate',
             '-of', 'json', video], text=True)
    j = json.loads(r.stdout or '{}')
    return float(j.get('format', {}).get('duration', 0) or 0)

def decode_rgb(video):
    raw = run(['ffmpeg', '-v', 'error', '-i', video, '-an', '-vf', f'fps={FPS},scale={SW}:{SH}:flags=area',
               '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, SH, SW, 3)

def decode_grey(video, w, h, fps):
    raw = run(['ffmpeg', '-v', 'error', '-i', video, '-an', '-vf', f'fps={fps},scale={w}:{h}:flags=area,format=gray',
               '-f', 'rawvideo', '-']).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w)

def ncorr(a, b):
    sa, sb = a.std(), b.std()
    if sa < 2 and sb < 2:
        return 1.0 if abs(a.mean() - b.mean()) < 6 else 0.0
    if sa < 2 or sb < 2:
        return 0.0
    a = a - a.mean(); b = b - b.mean()
    return float((a * b).sum() / math.sqrt((a * a).sum() * (b * b).sum()))

def hists(rgb):
    q = (rgb // 32).astype(np.int32)
    idx = (q[..., 0] * 64 + q[..., 1] * 8 + q[..., 2]).reshape(len(rgb), -1)
    H = np.zeros((len(rgb), 512), np.float32)
    for i in range(len(rgb)):
        H[i] = np.bincount(idx[i], minlength=512)
    return H / H.sum(1, keepdims=True)

# ----------------------------------------------------------------------------------------------------------------
def boundaries(rgb):
    n = len(rgb)
    small = rgb[:, ::3, ::3, :].astype(np.float32)          # 18x32 for structure
    g = small.mean(-1)
    lum = rgb.reshape(n, -1).mean(1)
    H = hists(rgb)
    D = np.array([1 - ncorr(g[i], g[i + 1]) for i in range(n - 1)])
    hd = np.abs(H[1:] - H[:-1]).sum(1) / 2
    a16 = rgb.astype(np.int16)
    frac = np.array([(np.abs(a16[i + 1] - a16[i]).max(-1) > 25).mean() for i in range(n - 1)])
    black = lum < 6
    cuts = []
    for i in range(n - 1):
        if black[i] and black[i + 1]:
            continue
        nb = np.r_[D[max(0, i - 3):i], D[i + 1:i + 4]]; nh = np.r_[hd[max(0, i - 3):i], hd[i + 1:i + 4]]
        m = nb.max() if len(nb) else 0; mh = nh.max() if len(nh) else 0
        fading = D[i] < 0.10 and abs(float(lum[i + 1] - lum[i])) > 1.0   # same picture, brightness ramp = fade
        if (D[i] > 0.30 and D[i] > 2.5 * m + 0.05) or (hd[i] > 0.30 and hd[i] > 2.5 * mh + 0.05 and not fading):
            cuts.append(i + 1)
    # dissolves (blend test)
    W = 12; diss = []; i = W
    cutset = np.zeros(n, bool); cutset[cuts] = True
    while i < n - W:
        A, B, M = g[i - W], g[i + W], g[i]
        if cutset[i - W:i + W + 1].any() or black[i - W] or black[i + W] or ncorr(A, B) > 0.5:
            i += 1; continue
        dAB = B - A
        den = (dAB * dAB).sum()
        if den < 1e-3:
            i += 1; continue
        alpha = float(((M - A) * dAB).sum() / den)
        res = np.sqrt(((M - (A + alpha * dAB)) ** 2).mean()) / (np.sqrt((dAB ** 2).mean()) + 1e-6)
        stepmax = D[i - W:i + W].max()
        if 0.25 < alpha < 0.75 and res < 0.35 and stepmax < 0.30:
            diss.append(i); i += 2 * W
        else:
            i += 1
    # black runs >= 0.2 s
    blacks = []; i = 0
    while i < n:
        if black[i]:
            j = i
            while j + 1 < n and black[j + 1]:
                j += 1
            if j - i + 1 >= 5:
                blacks.append((i, j + 1))
            i = j + 1
        else:
            i += 1
    # virtual-camera transitions between two stable framings of one composite:
    #   reframe = 4-12 frame burst (quick zoom / whip) or a cut straight into a moving shot,
    #   pan     = 13-35 frame eased slide between speakers on one wide plate (shot/reverse-shot without a cut).
    reframes = []; pans = []; act = 0.03; i = 4
    while i < n - 6:
        if D[i] > act and (D[i - 4:i] <= act).all() and not black[i]:
            j = i
            while j + 1 < n - 1 and D[j + 1] > act and j - i < 60:
                j += 1
            Lb = j - i + 1; peak = float(D[i:j + 1].max())
            post_stable = j + 5 < n - 1 and (D[j + 1:j + 5] <= act).all()
            nd = 1 - ncorr(g[i], g[min(n - 1, j + 1)])
            near = cutset[max(0, i - 2):min(n, j + 4)].any()
            if not near and post_stable and Lb <= 12 and peak > 0.12 and nd >= 0.45:
                reframes.append(i + 1)
            elif not near and post_stable and 12 < Lb <= 35 and peak > 0.10 and nd >= 0.55:
                pans.append(i + 1)
            elif not near and D[i] >= 0.30 and nd >= 0.60:
                reframes.append(i + 1)               # cut into a moving shot
            i = j + 1
        else:
            i += 1
    # cut into moving footage: one big spike inside motion (neighbours too busy for the plain cut test)
    taken = np.zeros(n, bool)
    for x in reframes + pans:
        taken[max(0, x - 10):x + 10] = True
    for i in range(3, n - 5):
        if (D[i] >= 0.40 and D[i] >= 1.8 * D[i - 3:i].max() and not cutset[max(0, i - 10):i + 11].any()
                and not taken[i] and not black[i] and 1 - ncorr(g[i - 3], g[i + 4]) >= 0.60):
            reframes.append(i + 1); taken[max(0, i - 10):i + 10] = True
    reframes.sort()
    # local in-shot events ("pose swaps", props, text pops): spiky but sub-cut change
    local = []
    for i in range(1, n - 2):
        if cutset[max(0, i - 2):i + 3].any():
            continue
        if 0.012 <= frac[i] and D[i] < 0.30 and frac[i] > 3 * max(frac[i - 1], frac[i + 1], 0.004):
            local.append(i + 1)
    return dict(cuts=cuts, diss=diss, reframes=reframes, pans=pans, blacks=blacks, local=local, lum=lum, frac=frac, D=D, hd=hd)

# ----------------------------------------------------------------------------------------------------------------
SCALES = [0.80, 0.86, 0.91, 0.95, 1.0, 1.05, 1.10, 1.16, 1.24, 1.33]

def _rs(img, w, h):
    from PIL import Image
    return np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).resize((w, h), Image.BILINEAR), np.float32)

def _ncc_match(big, small):
    Hb, Wb = big.shape; Hs, Ws = small.shape
    if Hs > Hb or Ws > Wb or small.std() < 4:
        return -1.0, 0, 0
    T = small - small.mean(); tn = np.sqrt((T ** 2).sum())
    num = np.fft.irfft2(np.fft.rfft2(big) * np.fft.rfft2(T[::-1, ::-1], s=big.shape), s=big.shape)[Hs - 1:Hb, Ws - 1:Wb]
    def wsum(x):
        ii = np.pad(x.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
        return ii[Hs:, Ws:] - ii[:-Hs, Ws:] - ii[Hs:, :-Ws] + ii[:-Hs, :-Ws]
    N = Hs * Ws; s1 = wsum(big); var = np.maximum(wsum(big ** 2) - s1 ** 2 / N, 1e-6)
    ncc = num / (np.sqrt(var) * tn)
    k = int(np.argmax(ncc)); y, x = divmod(k, ncc.shape[1])
    return float(ncc[y, x]), y, x

def camera(A, B):
    """scale (>1 = push-in) and shift of B relative to A, from a 70 % centre crop of B searched in A."""
    A = A.astype(np.float32); B = B.astype(np.float32)
    h, w = A.shape; cw, ch = int(w * 0.7), int(h * 0.7); x0, y0 = (w - cw) // 2, (h - ch) // 2
    best = (-2, 1.0, 0, 0)
    for s in SCALES:
        sm = B[y0:y0 + ch, x0:x0 + cw] if s == 1.0 else _rs(B[y0:y0 + ch, x0:x0 + cw], round(cw / s), round(ch / s))
        c, y, x = _ncc_match(A, sm)
        if c > best[0]:
            best = (c, s, y - (h - sm.shape[0]) // 2, x - (w - sm.shape[1]) // 2)
    return dict(ncc=round(best[0], 2), scale=best[1], dy=int(best[2]), dx=int(best[3]))

# ----------------------------------------------------------------------------------------------------------------
def audio(video, dur, speech):
    r = run(['ffmpeg', '-hide_banner', '-nostats', '-v', 'verbose', '-i', video, '-vn', '-af',
             'ebur128=framelog=verbose', '-f', 'null', '-'], text=True).stderr
    rows = re.findall(r't:\s*([\d.]+)\s+TARGET:\S+ LUFS\s+M:\s*(-?[\d.]+)\s+S:\s*(-?[\d.]+)', r)
    summ = r.split('Summary:')[-1]
    I = re.search(r'I:\s+(-?[\d.]+) LUFS', summ); LRA = re.search(r'LRA:\s+([\d.]+) LU', summ)
    n10 = int(dur * 10) + 1
    M = np.full(n10, -120.0); S = np.full(n10, -120.0)
    for t, m, s in rows:
        k = min(n10 - 1, max(0, int(float(t) * 10) - 1)); M[k] = float(m); S[k] = float(s)
    raw = run(['ffmpeg', '-v', 'error', '-i', video, '-vn', '-ac', '2', '-ar', '22050', '-f', 's16le', '-']).stdout
    raw = raw[:len(raw) // 4 * 4]
    x = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32) / 32768
    hop = 2205; n = min(len(x) // hop, n10)
    if n < 10:
        return None                                  # no (usable) audio stream
    mid = (x[:n * hop, 0] + x[:n * hop, 1]) / 2; side = (x[:n * hop, 0] - x[:n * hop, 1]) / 2
    db = lambda v: 20 * np.log10(np.sqrt((v.reshape(n, hop) ** 2).mean(1)) + 1e-9)
    mid_db, side_db = db(mid), db(side)
    M = M[:n]; S = S[:n]
    silent = M < -45
    def runs(mask, minlen):
        out = []; i = 0
        while i < len(mask):
            if mask[i]:
                j = i
                while j + 1 < len(mask) and mask[j + 1]:
                    j += 1
                if j - i + 1 >= minlen:
                    out.append((round(i / 10, 1), round((j - i + 1) / 10, 1)))
                i = j + 1
            else:
                i += 1
        return out
    sil = runs(silent, 4)
    res = dict(integrated_lufs=float(I.group(1)) if I else None, loudness_range_lu=float(LRA.group(1)) if LRA else None,
               silence_runs=sil, silence_total_s=round(sum(d for _, d in sil), 1),
               digital_silence_runs=runs(mid_db < -70, 4),
               music_off_runs=runs((side_db < -60) & ~silent, 20),
               momentary_p10_50_90=[round(float(v), 1) for v in np.percentile(M[M > -70], [10, 50, 90])] if (M > -70).any() else None)
    # transients ("SFX candidates"): >= 12 dB rise over the previous 0.5 s, short, not on a word onset
    e = mid_db; onsets = []
    wstarts = np.array([a for a, _ in speech]) if speech else np.array([-99.0])
    last = -9
    for i in range(5, n - 2):
        base = np.median(e[i - 5:i])
        if e[i] - base >= 12 and e[i] > np.percentile(e, 55) and i / 10 - last > 0.4:
            if np.min(np.abs(wstarts - i / 10)) > 0.15:
                onsets.append(round(i / 10, 1)); last = i / 10
    res['sfx_candidates'] = onsets
    sp = np.zeros(n, bool)
    for a, b in speech:
        sp[int(a * 10):int(math.ceil(b * 10))] = True
    if speech:
        nonsp = ~sp & ~silent
        vs = M[sp & ~silent]; bd = M[nonsp]
        res['voice_momentary_med'] = round(float(np.median(vs)), 1) if len(vs) else None
        res['bed_momentary_med'] = round(float(np.median(bd)), 1) if len(bd) else None
        if len(vs) and len(bd):
            res['bed_below_voice_lu'] = round(float(np.median(vs) - np.median(bd)), 1)
        # ducking test: music (stereo side) level 0.2-1.0 s before a speech turn vs 0.3-1.1 s after it starts
        turns_ = []
        for a_, b_ in sorted(speech):
            if turns_ and a_ - turns_[-1][1] < 1.2:
                turns_[-1][1] = max(turns_[-1][1], b_)
            else:
                turns_.append([a_, b_])
        dd = []
        for i_, (a_, b_) in enumerate(turns_):
            if i_ and a_ - turns_[i_ - 1][1] < 1.2:
                continue
            pre = side_db[max(0, int((a_ - 1.0) * 10)):int((a_ - 0.2) * 10)]; post = side_db[int((a_ + 0.3) * 10):int((a_ + 1.1) * 10)]
            if len(pre) and len(post) and pre.mean() > -70 and post.mean() > -70:
                dd.append(float(post.mean() - pre.mean()))
        if dd:
            res['music_change_at_speech_onset_db'] = round(float(np.median(dd)), 1)   # corpus: -2.9..+2.0 = no ducking
    res['_per100ms'] = dict(M=M, S=S, mid=mid_db, side=side_db, silent=silent, speech=sp)
    return res

def load_speech(path):
    if not path:
        return [], 0, []
    j = json.load(open(path, encoding='utf-8'))
    ivals, words, turns = [], 0, []
    if isinstance(j, list):
        return [(float(a), float(b)) for a, b in j], 0, []
    for s in j.get('segments', []):
        if re.search(r'thanks? (you )?for watching', s.get('text', ''), re.I):
            continue                               # whisper hallucination on music
        ws = s.get('words') or []
        for w in ws:
            ivals.append((w['s'], w['e'])); words += 1
        if ws:
            turns.append((s['start'], s['end'], len(ws)))
        elif s.get('text'):
            ivals.append((s['start'], s['end']))
    return ivals, words, turns

# ----------------------------------------------------------------------------------------------------------------
def seg_stats(bounds_s, dur, a, b):
    """cuts per minute inside [a,b) and shot lengths of shots that start inside it."""
    inside = [t for t in bounds_s if a <= t < b]
    mins = max((b - a) / 60, 1e-6)
    return round(len(inside) / mins, 1)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('video'); ap.add_argument('--transcript'); ap.add_argument('--mode', default='auto',
                                                                            choices=['auto', 'voiced', 'wordless'])
    ap.add_argument('--out', default='qa_out'); ap.add_argument('--hold', type=float, default=8.0)
    ap.add_argument('--montage', action='store_true'); ap.add_argument('--quiet', action='store_true')
    ap.add_argument('--no-audio', action='store_true')
    ap.add_argument('--target-lufs', type=float, default=None,
                    help='our own loudness target (e.g. -14). Replaces the corpus integrated-LUFS band (the corpus is '
                         'mixed quiet, -16.6..-22.5 for voiced videos) with target +-1.5 (PASS) / +-4 (FAIL).')
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    if a.target_lufs is not None:
        for grp in ('voiced', 'wordless'):
            NORMS[grp]['integrated_lufs'] = dict(lo=a.target_lufs - 1.5, hi=a.target_lufs + 1.5,
                                                 fail_lo=a.target_lufs - 4.0, fail_hi=a.target_lufs + 4.0)
    dur = probe(a.video)
    rgb = decode_rgb(a.video); n = len(rgb); dur = dur or n / FPS
    B = boundaries(rgb)
    # boundary list (seconds) with type
    bl = [(c / FPS, 'cut') for c in B['cuts']] + [(d / FPS, 'dissolve') for d in B['diss']] + \
         [(r / FPS, 'reframe') for r in B['reframes']] + [(p / FPS, 'pan') for p in B['pans']]
    for s0, s1 in B['blacks']:
        if s0 == 0 and s1 / FPS < 2.0:
            continue                               # opening fade-in from black is not an edit
        if s0 > 0 and s1 < n: bl.append((s0 / FPS, 'to_black'))
        if s1 < n and s0 > 0: bl.append((s1 / FPS, 'from_black'))
        if s1 >= n - 1 and s0 > 0: bl.append((s0 / FPS, 'to_black'))
    bl.sort()
    merged = []
    for t, k in bl:                                  # merge boundaries closer than 0.2 s
        if t < 1.0:
            continue                                 # opening fade-in / slide-in is not an edit
        if merged and t - merged[-1][0] < 0.2:
            continue
        merged.append((t, k))
    edges = [0.0] + [t for t, _ in merged] + [dur]
    kinds = ['start'] + [k for _, k in merged]
    # camera estimate per shot
    zg = decode_grey(a.video, ZW, ZH, ZFPS)
    shots = []
    for i in range(len(edges) - 1):
        t0, t1 = edges[i], edges[i + 1]; L = t1 - t0
        f0, f1 = int(t0 * FPS), max(int(t0 * FPS) + 1, int(t1 * FPS) - 1)
        isblack = float(B['lum'][f0:f1].mean()) < 6 if f1 > f0 else False
        mov = float((B['frac'][f0:f1 - 1] > 0.03).mean()) if f1 - 1 > f0 else 0.0
        nloc = int(sum(1 for x in B['local'] if f0 < x < f1))
        cam = dict(ncc=None, scale=1.0, dx=0, dy=0); camclass = 'black' if isblack else 'static'
        if L >= 1.2 and not isblack:
            z0 = min(len(zg) - 1, int((t0 + 0.25) * ZFPS)); z1 = min(len(zg) - 1, int((t1 - 0.25) * ZFPS))
            if z1 > z0:
                cam = camera(zg[z0], zg[z1])
                if cam['ncc'] >= 0.6:
                    if cam['scale'] >= 1.05: camclass = 'push_in'
                    elif cam['scale'] <= 0.95: camclass = 'pull_out'
                    elif abs(cam['dx']) + abs(cam['dy']) >= 6: camclass = 'pan/slide'
                    elif mov > 0.5: camclass = 'animated_bg'
                else:
                    camclass = 'animated/changing' if mov > 0.3 else 'static'
        shots.append(dict(i=i, t0=round(t0, 2), t1=round(t1, 2), dur=round(L, 2), enter=kinds[i],
                          moving_share=round(mov, 2), pose_swaps=nloc, camera=camclass,
                          scale=cam['scale'], ncc=cam['ncc']))
    # end card = last shot >= 2 s before the trailing black/fade; the story ends where it starts
    endcard, story_end = 0.0, dur
    k = len(shots) - 1
    while k >= 0 and (shots[k]['camera'] == 'black' or shots[k]['dur'] < 2.0) and shots[k]['t0'] >= dur - 25:
        k -= 1                                       # skip trailing black and fade-out remnants
    if (k > 0 and shots[k]['dur'] >= 2.0 and shots[k]['t0'] >= max(dur - 25, 0.5 * dur)
            and shots[k]['camera'] == 'static'):
        endcard = shots[-1]['t1'] - shots[k]['t0'] - sum(s['dur'] for s in shots[k + 1:] if s['camera'] == 'black')
        story_end = shots[k]['t0']
    story = [s for s in shots if s['t0'] < story_end - 0.05 and s['camera'] != 'black']
    L = np.array([s['dur'] for s in story] or [0.0])
    bsec = [t for t, _ in merged if t < story_end - 0.05]
    body_a, body_b = 60.0, max(60.0, story_end - 30)
    holds = [s for s in story if s['dur'] > a.hold]
    body_shots = [s for s in story if s['t0'] >= body_a and s['t1'] <= body_b]
    blacks = [s for s in shots if s['camera'] == 'black']
    R = dict(video=a.video, duration_s=round(dur, 2), story_end_s=round(story_end, 2), shots=len(story),
             boundaries=len(bsec),
             boundary_types={k: sum(1 for t, x in merged if x == k and t < story_end - 0.05)
                             for k in ['cut', 'reframe', 'pan', 'dissolve', 'to_black', 'from_black']},
             cuts_per_min_total=round(len(bsec) / (story_end / 60), 1),
             cuts_per_min_0_15=seg_stats(bsec, dur, 0, 15), cuts_per_min_15_60=seg_stats(bsec, dur, 15, 60),
             cuts_per_min_body=seg_stats(bsec, dur, body_a, body_b),
             cuts_per_min_last30=seg_stats(bsec, dur, story_end - 30, story_end),
             mean_shot_s=round(float(L.mean()), 2), median_shot_s=round(float(np.median(L)), 2),
             p10_shot_s=round(float(np.percentile(L, 10)), 2), p90_shot_s=round(float(np.percentile(L, 90)), 2),
             max_shot_s=round(float(L.max()), 2),
             longest_hold_body_s=round(max([s['dur'] for s in body_shots] or [0]), 2),
             holds_over_hold=[(s['t0'], s['dur'], s['camera'], s['pose_swaps']) for s in holds],
             holds_over_hold_per_10min=round(len(holds) / (story_end / 600), 1),
             first_cut_s=round(bsec[0], 2) if bsec else None,
             end_card_s=round(endcard, 2),
             black_hold_total_s=round(sum(s['dur'] for s in blacks if 0 < s['t0'] and s['t1'] < dur - 0.5), 1),
             pose_swaps_per_min=round(len(B['local']) / (dur / 60), 1),
             camera_mix={k: round(sum(s['dur'] for s in shots if s['camera'] == k) / dur * 100, 1)
                         for k in sorted(set(s['camera'] for s in shots))},
             per_minute_cuts=[sum(1 for t in bsec if m * 60 <= t < m * 60 + 60) for m in range(int(math.ceil(dur / 60)))],
             boundary_list=[(round(t, 2), k) for t, k in merged])
    speech, nwords, turns = load_speech(a.transcript)
    mode = a.mode if a.mode != 'auto' else ('voiced' if nwords >= 50 else 'wordless')
    R['mode'] = mode
    if speech:
        sp_s = sum(e - s for s, e in speech)
        R['speech_share_pct'] = round(100 * sp_s / dur, 1)
        R['first_word_s'] = round(min(s for s, _ in speech), 1)
        st = sorted(speech); gaps = [st[i + 1][0] - st[i][1] for i in range(len(st) - 1)]
        R['longest_wordless_s'] = round(max(gaps + [st[0][0], dur - st[-1][1]]), 1)
        if turns:
            tw = sum(w for _, _, w in turns); td = sum(e - s for s, e, _ in turns)
            R['wpm_in_turns'] = round(tw / (td / 60), 0) if td > 0 else None
        pz = [g for g in gaps if 0.3 <= g <= 2.0]
        R['pauses_0.3_2s_median'] = round(float(np.median(pz)), 2) if pz else None
    if not a.no_audio:
        au = audio(a.video, dur, speech)
        if au is None:
            print('WARNING: no audio stream found - audio checks skipped'); a.no_audio = True
    if not a.no_audio:
        per = au.pop('_per100ms'); R.update(au)
        R['silence_runs_per_10min'] = round(len(au['silence_runs']) / (dur / 600), 1)
        R['dramatic_silences'] = sum(1 for t0, d in au['silence_runs'] if d >= 1.0 and t0 >= 2.0 and t0 < R['story_end_s'])
        # seconds.csv
        cutsec = np.zeros(int(dur) + 1, int)
        for t in bsec:
            cutsec[min(len(cutsec) - 1, int(t))] += 1
        with open(os.path.join(a.out, 'seconds.csv'), 'w') as f:
            f.write('sec,boundaries,momentary_max_lufs,shortterm_lufs,mid_db,side_db,silent_share,speech_share\n')
            for s in range(min(len(cutsec), len(per['M']) // 10)):
                sl = slice(s * 10, s * 10 + 10)
                f.write(f"{s},{cutsec[s]},{per['M'][sl].max():.1f},{per['S'][sl].mean():.1f},{per['mid'][sl].mean():.1f},"
                        f"{per['side'][sl].mean():.1f},{per['silent'][sl].mean():.1f},{per['speech'][sl].mean():.1f}\n")
    with open(os.path.join(a.out, 'shots.csv'), 'w') as f:
        f.write('i,t0,t1,dur,enter,camera,scale,ncc,moving_share,pose_swaps\n')
        for s in shots:
            f.write('{i},{t0},{t1},{dur},{enter},{camera},{scale},{ncc},{moving_share},{pose_swaps}\n'.format(**s))
    # ---- checks
    checks = []
    for grp in ('common', mode):
        for k, b in NORMS[grp].items():
            v = R.get(k)
            if v is None:
                continue
            st = 'PASS' if b['lo'] <= v <= b['hi'] else ('FAIL' if (v < b['fail_lo'] or v > b['fail_hi']) else 'WARN')
            checks.append((k, v, f"{b['lo']}..{b['hi']}", st))
    R['checks'] = checks
    json.dump(R, open(os.path.join(a.out, 'report.json'), 'w'), indent=1, default=str)
    if a.montage:
        montage(a.video, merged, os.path.join(a.out, 'montage_cuts.jpg'))
    if not a.quiet:
        print(f"\n== LBS rhythm QA  {os.path.basename(a.video)}  {dur:.0f}s  mode={mode}")
        print(f"shots {R['shots']}  boundaries {R['boundary_types']}  pose-swaps/min {R['pose_swaps_per_min']}")
        print(f"cuts/min  total {R['cuts_per_min_total']} | 0-15s {R['cuts_per_min_0_15']} | 15-60s {R['cuts_per_min_15_60']}"
              f" | body {R['cuts_per_min_body']} | last30 {R['cuts_per_min_last30']}")
        print(f"shot s    p10 {R['p10_shot_s']}  median {R['median_shot_s']}  mean {R['mean_shot_s']}  p90 {R['p90_shot_s']}"
              f"  max {R['max_shot_s']}  (story ends {R['story_end_s']}s, end card {R['end_card_s']}s)")
        print('cuts per minute of runtime:', R['per_minute_cuts'])
        print('holds >%gs:' % a.hold, ', '.join(f"{t0}s {d}s {c}" for t0, d, c, _ in R['holds_over_hold'][:12]))
        print('camera mix % of runtime:', R['camera_mix'])
        if not a.no_audio:
            print(f"loudness  I {R['integrated_lufs']} LUFS  LRA {R['loudness_range_lu']} LU  momentary p10/50/90 "
                  f"{R['momentary_p10_50_90']}")
            if 'bed_below_voice_lu' in R:
                print(f"voice vs bed: bed {R['bed_below_voice_lu']} LU below voice; music change at speech onsets "
                      f"{R.get('music_change_at_speech_onset_db')} dB (corpus -3..+2 = static bed, no ducking)")
            print('silence runs (>=0.4 s, M<-45):', R['silence_runs'][:12], ' music-off runs (>=2 s):', R['music_off_runs'][:8])
            print('dramatic silences (>= 1 s, inside the story):', R['dramatic_silences'])
            print('SFX candidates/min %.1f' % (len(R['sfx_candidates']) / (dur / 60)))
        if speech:
            print(f"speech {R['speech_share_pct']}%  first word {R['first_word_s']}s  longest wordless {R['longest_wordless_s']}s"
                  f"  WPM(in turns) {R.get('wpm_in_turns')}  pause median {R.get('pauses_0.3_2s_median')}s")
        print('-- checks vs corpus norms')
        for k, v, band, st in checks:
            print(f"  {st:<5} {k:<28} {v!s:>8}   norm {band}")
    sys.exit(1 if any(c[3] == 'FAIL' for c in checks) else 0)

def montage(video, bounds, out, per_row=4):
    """before/after frame pair for every boundary, labelled with its type, for a human calibration pass."""
    from PIL import Image, ImageDraw
    W, H = 192, 108
    tiles = []
    for t, kind in bounds:
        pair = []
        pre = 0.12 if kind == 'cut' else 0.30          # reframes/dissolves take 0.2-0.5 s
        post = 0.08 if kind == 'cut' else 0.50
        for tt in (max(0, t - pre), t + post):
            raw = run(['ffmpeg', '-v', 'error', '-ss', f'{tt:.3f}', '-i', video, '-frames:v', '1', '-vf', f'scale={W}:{H}',
                       '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']).stdout
            pair.append(np.frombuffer(raw, np.uint8).reshape(H, W, 3) if len(raw) == W * H * 3 else np.zeros((H, W, 3), np.uint8))
        tiles.append(((t, kind), pair))
    rows = max(1, math.ceil(len(tiles) / per_row))
    img = Image.new('RGB', (per_row * (2 * W + 8), rows * (H + 14)), (25, 25, 25)); d = ImageDraw.Draw(img)
    for k, ((t, kind), (p, q)) in enumerate(tiles):
        r, c = divmod(k, per_row); x0, y0 = c * (2 * W + 8), r * (H + 14)
        img.paste(Image.fromarray(p), (x0, y0 + 14)); img.paste(Image.fromarray(q), (x0 + W, y0 + 14))
        d.text((x0 + 2, y0 + 1), f'{k} {kind} @ {t:.2f}s', fill=(255, 255, 0))
    img.save(out, quality=80)

if __name__ == '__main__':
    main()
