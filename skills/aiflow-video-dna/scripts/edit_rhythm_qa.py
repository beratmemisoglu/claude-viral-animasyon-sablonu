#!/usr/bin/env python3
"""edit_rhythm_qa.py - measure the edit rhythm of a finished video (QA gate).

Needs: ffmpeg/ffprobe on PATH, Python 3.9+, numpy, Pillow.  No OpenCV.
Usage:
  python edit_rhythm_qa.py VIDEO.mp4 [--start 0] [--dur 0] [--out qa_out] [--hold 8] [--profile tutorial|animated]
Outputs: qa_out/events.csv, qa_out/minutes.csv, qa_out/report.json and a pass/fail table on stdout.

Event classes (10 fps, 256x144 grey):
  cut          instant (<=0.3 s) full-frame content change (editor cut, tab switch, overlay in/out)
  page_change  gradual full-frame change (fade, page load, animated transition)
  zoom_in/out  camera scale change (NCC scale search 1.06-2.3x), returns factor + move duration
  scroll/pan   camera/page translation
  local        region-limited change >=4 % of pixels (UI update, caption, sticker, typing burst)
  micro        <4 % of pixels (cursor, caret) - ignored for rhythm
"""
import argparse, json, math, os, subprocess, sys
import numpy as np
from PIL import Image

W, H, FPS = 256, 144, 10

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def decode_gray(video, start, dur):
    cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(start)]
    if dur: cmd += ['-t', str(dur)]
    cmd += ['-i', video, '-vf', f'fps={FPS},scale={W}:{H}:flags=area,format=gray', '-f', 'rawvideo', '-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W)

def rs(img, w, h):
    return np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).resize((w, h), Image.BILINEAR), np.float32)

def ncc_match(big, small, minstd=6.0):
    Hb, Wb = big.shape; Hs, Ws = small.shape
    if Hs > Hb or Ws > Wb or Hs < 6 or Ws < 6 or small.std() < minstd: return (-1.0, 0, 0)
    T = small - small.mean(); tn = np.sqrt((T ** 2).sum())
    num = np.fft.irfft2(np.fft.rfft2(big) * np.fft.rfft2(T[::-1, ::-1], s=big.shape), s=big.shape)[Hs-1:Hb, Ws-1:Wb]
    def wsum(x):
        ii = np.pad(x.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
        return ii[Hs:, Ws:] - ii[:-Hs, Ws:] - ii[Hs:, :-Ws] + ii[:-Hs, :-Ws]
    N = Hs * Ws; s1 = wsum(big); var = np.maximum(wsum(big ** 2) - s1 ** 2 / N, 1e-6)
    ncc = num / (np.sqrt(var) * tn); ncc[var / N < minstd ** 2] = -1
    k = int(np.argmax(ncc)); y, x = divmod(k, ncc.shape[1])
    return (float(ncc[y, x]), y, x)

SCALES = [1.0, 1.06, 1.12, 1.2, 1.28, 1.36, 1.45, 1.55, 1.67, 1.8, 1.95, 2.1, 2.3]
STEP_SCALES = [1.0, 1.03, 1.06, 1.1, 1.15, 1.22, 1.3]

def estimate(A, B, crop=0.7, scales=SCALES):
    """How is B related to A? best scale (>1 zoom-in), NCC of best fit, identity NCC, shift at scale 1."""
    A = A.astype(np.float32); B = B.astype(np.float32)
    a0, b0 = A - A.mean(), B - B.mean()
    ncc_id = float((a0 * b0).sum() / np.sqrt((a0 ** 2).sum() * (b0 ** 2).sum() + 1e-6))
    cw, ch = int(W * crop), int(H * crop); x0, y0 = (W - cw) // 2, (H - ch) // 2
    Bc, Ac = B[y0:y0+ch, x0:x0+cw], A[y0:y0+ch, x0:x0+cw]
    res = []
    for s in scales:
        sm = Bc if s == 1.0 else rs(Bc, round(cw / s), round(ch / s))
        c, y, x = ncc_match(A, sm); res.append((c, s, y, x))
        if s > 1.0:
            c, y, x = ncc_match(B, rs(Ac, round(cw / s), round(ch / s))); res.append((c, 1 / s, y, x))
    r1 = [r for r in res if r[1] == 1.0][0]
    best = max(res, key=lambda r: r[0])
    return dict(scale=best[1], ncc=best[0], ncc_id=ncc_id, ncc_s1=r1[0], dy=r1[2] - y0, dx=r1[3] - x0)

def detect_events(a):
    a16 = a.astype(np.int16)
    d = np.abs(a16[1:] - a16[:-1]); mad = d.mean((1, 2)); frac = (d > 24).mean((1, 2))
    act = (frac > 0.02) | (mad > 2.0); n = len(mad); segs = []; i = 0
    while i < n:                                  # group active pairs, bridge 1-frame gaps
        if act[i]:
            j = i
            while j + 1 < n and (act[j+1] or (j + 2 < n and act[j+2])): j += 1
            segs.append((i, j)); i = j + 1
        else: i += 1
    events = []
    for i0, i1 in segs:
        A = a[i0].astype(np.float32); B = a[min(i1 + 1, len(a) - 1)].astype(np.float32)
        r = estimate(A, B); m = np.abs(A - B) > 24; chg = float(m.mean())
        if m.any():
            ys, xs = np.where(m); bbarea = (np.ptp(xs) + 1) * (np.ptp(ys) + 1) / (W * H)
        else: bbarea = 0.0
        ntr = nzm = 0; sdy = sdx = 0; zp = 1.0; nst = 0
        for k in range(i0, i1 + 1):               # per-step motion model
            if frac[k] < 0.01 and mad[k] < 1: continue
            nst += 1; s = estimate(a[k], a[k+1], crop=0.6, scales=STEP_SCALES)
            if s['ncc'] > 0.85:
                if s['scale'] == 1.0 and (s['dy'] or s['dx']): ntr += 1; sdy += s['dy']; sdx += s['dx']
                elif s['scale'] != 1.0 and s['ncc'] - s['ncc_s1'] > 0.03: nzm += 1; zp *= s['scale']
        dur = (i1 - i0 + 1) / FPS; peak = float(frac[i0:i1+1].max())
        conc = float(frac[i0:i1+1].max() / max(frac[i0:i1+1].sum(), 1e-6))   # single-step concentration
        dl = abs(A.mean() - B.mean()); gain = r['ncc'] - max(r['ncc_id'], r['ncc_s1'])
        zf = 1.0
        if chg < 0.04 and ntr < 2: cls = 'micro'
        elif dl < 15 and ((r['ncc'] >= 0.75 and r['scale'] != 1 and gain >= 0.15 and abs(math.log(r['scale'])) > 0.05)
                          or (nzm >= 2 and nzm >= 0.4 * nst and abs(math.log(zp)) > 0.08)):
            zf = r['scale'] if (r['ncc'] >= 0.75 and gain >= 0.15) else zp
            cls = 'zoom_in' if zf > 1 else 'zoom_out'
        elif dl < 12 and chg < 0.6 and nst and ntr >= 0.5 * nst and abs(sdy) + abs(sdx) >= 4:
            cls = 'scroll' if abs(sdy) >= abs(sdx) else 'pan'
        elif (chg >= 0.2 and bbarea >= 0.35) or (bbarea >= 0.6 and chg >= 0.1 and r['ncc_id'] < 0.85):
            cls = 'cut' if (dur <= 0.3 and conc >= 0.6) or (conc > 0.6 and peak > 0.25) else 'page_change'
        elif chg < 0.04: cls = 'micro'
        else: cls = 'local'
        events.append(dict(t0=i0 / FPS, t1=(i1 + 1) / FPS, dur=dur, cls=cls, chg=round(chg, 3), bbarea=round(bbarea, 2),
                           zoom_factor=round(zf, 2), lum_jump=round(dl, 1)))
    return events, mad, frac

def audio_stats(video, start, dur):
    cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(start)] + (['-t', str(dur)] if dur else []) + \
          ['-i', video, '-vn', '-ac', '2', '-ar', '22050', '-f', 's16le', '-']
    x = np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.int16).reshape(-1, 2).astype(np.float32) / 32768
    if not len(x): return {}
    mid, side = (x[:, 0] + x[:, 1]) / 2, (x[:, 0] - x[:, 1]) / 2; hop = 2205; n = len(mid) // hop
    db = lambda v: 20 * np.log10(np.sqrt((v[:n*hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)
    m, s = db(mid), db(side); speech = float(np.median(m))
    loud = m > speech + 12                                     # stings / SFX / music hits >= 12 dB over speech
    stings, i = [], 0
    while i < n:
        if loud[i]:
            j = i
            while j + 1 < n and (loud[j+1] or (j + 3 < n and loud[j+2:j+4].any())): j += 1
            if j - i + 1 >= 3: stings.append(round(i / 10 + start, 1))
            i = j + 1
        else: i += 1
    quiet = m < -35; pauses, i = 0, 0
    while i < n:
        if quiet[i]:
            j = i
            while j + 1 < n and quiet[j+1]: j += 1
            pauses += (j - i + 1) >= 4; i = j + 1
        else: i += 1
    lo = run(['ffmpeg', '-hide_banner', '-nostats', '-ss', str(start)] + (['-t', str(dur)] if dur else []) +
             ['-i', video, '-vn', '-af', 'ebur128', '-f', 'null', '-']).stderr
    I = [l for l in lo.splitlines() if l.strip().startswith('I:')]; L = [l for l in lo.splitlines() if l.strip().startswith('LRA:')]
    return dict(speech_rms_median_db=round(speech, 1), pauses_ge_0_4s_below_m35db=int(pauses), loud_stings=stings,
                stereo_bed_share=round(float((s > -75).mean()), 2),
                integrated_lufs=I[-1].split()[1] if I else None, lra=L[-1].split()[1] if L else None)

def summarize(events, t0, t1, hold):
    nm = [e for e in events if e['cls'] != 'micro' and t0 <= e['t0'] < t1]
    shots = [e for e in nm if e['cls'] in ('cut', 'page_change')]
    mins = max((t1 - t0) / 60, 1e-6)
    bt = np.diff([t0] + [e['t0'] for e in shots] + [t1]); bt = bt[bt > 0.05]
    at = [t0] + [e['t0'] for e in nm] + [t1]
    holds = [(round(at[i], 1), round(at[i+1] - at[i], 1)) for i in range(len(at) - 1) if at[i+1] - at[i] > hold]
    c = {k: sum(1 for e in nm if e['cls'] == k) for k in ['cut', 'page_change', 'zoom_in', 'zoom_out', 'scroll', 'pan', 'local']}
    return dict(changes=len(nm), changes_per_min=round(len(nm) / mins, 1), cuts_per_min=round(c['cut'] / mins, 1),
                shot_changes_per_min=round(len(shots) / mins, 1), median_shot_s=round(float(np.median(bt)), 1) if len(bt) else None,
                mean_shot_s=round(float(bt.mean()), 1) if len(bt) else None,
                median_gap_between_changes_s=round(float(np.median(np.diff(at))), 1), longest_hold_s=round(max(np.diff(at)), 1),
                holds_over_limit=holds, zooms=c['zoom_in'] + c['zoom_out'], **c)

# Targets distilled from the reference video (AI Flow, SRjm9tvMHhs) - see 04-edit-rhythm-metrics.md
TARGETS = {'tutorial': dict(changes_per_min=(20, 45), shot_changes_per_min=(6, 18), median_shot_s=(1.5, 5.0), max_hold_s=15, holds_per_10min=6),
           'animated': dict(changes_per_min=(15, 40), shot_changes_per_min=(5, 12), median_shot_s=(3.0, 9.0), max_hold_s=10, holds_per_10min=3)}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('video'); ap.add_argument('--start', type=float, default=0)
    ap.add_argument('--dur', type=float, default=0); ap.add_argument('--out', default='qa_out'); ap.add_argument('--hold', type=float, default=8)
    ap.add_argument('--profile', default='tutorial', choices=list(TARGETS)); ap.add_argument('--no-audio', action='store_true')
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    frames = decode_gray(a.video, a.start, a.dur)
    events, mad, frac = detect_events(frames)
    for e in events: e['t0'] = round(e['t0'] + a.start, 2); e['t1'] = round(e['t1'] + a.start, 2)
    T0, T1 = a.start, a.start + len(frames) / FPS
    total = summarize(events, T0, T1, a.hold)
    minutes = [dict(minute=int(m // 60), **summarize(events, m, min(m + 60, T1), a.hold)) for m in np.arange(T0 - T0 % 60, T1, 60)]
    zooms = [e for e in events if e['cls'].startswith('zoom')]
    total['zoom_factors'] = [e['zoom_factor'] for e in zooms]; total['zoom_move_s'] = [e['dur'] for e in zooms]
    aud = {} if a.no_audio else audio_stats(a.video, a.start, a.dur)
    with open(os.path.join(a.out, 'events.csv'), 'w') as f:
        f.write('t0,t1,dur,class,changed_frac,bbox_area,zoom_factor,lum_jump\n')
        for e in events: f.write('{t0},{t1},{dur},{cls},{chg},{bbarea},{zoom_factor},{lum_jump}\n'.format(**e))
    with open(os.path.join(a.out, 'minutes.csv'), 'w') as f:
        keys = ['minute', 'changes', 'cut', 'page_change', 'zoom_in', 'zoom_out', 'scroll', 'local', 'shot_changes_per_min', 'median_shot_s', 'longest_hold_s']
        f.write(','.join(keys) + '\n')
        for m in minutes: f.write(','.join(str(m[k]) for k in keys) + '\n')
    json.dump(dict(total=total, minutes=minutes, audio=aud), open(os.path.join(a.out, 'report.json'), 'w'), indent=1, default=str)
    t = TARGETS[a.profile]; mins = (T1 - T0) / 60
    checks = [('changes/min', total['changes_per_min'], t['changes_per_min']),
              ('shot changes/min', total['shot_changes_per_min'], t['shot_changes_per_min']),
              ('median shot s', total['median_shot_s'], t['median_shot_s'])]
    print(f"\n== Edit-rhythm QA  {a.video}  [{T0:.0f}-{T1:.0f}s, profile={a.profile}]")
    for name, v, (lo, hi) in checks:
        print(f"{name:<22}{v!s:>8}   target {lo}-{hi}   {'PASS' if v is not None and lo <= v <= hi else 'FAIL'}")
    nh = len(total['holds_over_limit']); lim = t['holds_per_10min'] * mins / 10
    print(f"{'longest hold s':<22}{total['longest_hold_s']:>8}   max {t['max_hold_s']}   {'PASS' if total['longest_hold_s'] <= t['max_hold_s'] else 'FAIL'}")
    print(f"{'holds > %gs' % a.hold:<22}{nh:>8}   max {lim:.0f}   {'PASS' if nh <= lim else 'FAIL'}")
    print(f"{'zoom moves':<22}{total['zooms']:>8}   factors {total['zoom_factors'][:12]}")
    if aud: print('audio:', {k: v for k, v in aud.items() if k != 'loud_stings'}, '| stings at', aud['loud_stings'][:20])

if __name__ == '__main__':
    main()
