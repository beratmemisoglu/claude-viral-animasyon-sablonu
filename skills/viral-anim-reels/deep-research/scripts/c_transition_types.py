"""Classify each detected transition (from out/c_measure.json) as hard cut / dissolve / whip-morph
by decoding +-0.4 s at 30 fps. Usage: python -I c_transition_types.py <research_root>"""
import sys, os, json, subprocess, numpy as np
R = sys.argv[1]; OUT = os.path.join(R, 'analysis', 'scripts', 'out')
D = json.load(open(os.path.join(OUT, 'c_measure.json')))['videos']
W, H = 72, 128
res = {}
for vid, r in D.items():
    ch = 'ricksclips' if r['ch'] == 'Ricks Clips' else 'competitors'
    p = os.path.join(R, 'videos', ch, vid, 'video.mp4')
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'fps=30,scale={W}:{H}', '-pix_fmt', 'gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
    F = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
    F[:, int(H*.52):int(H*.80)] = 0
    cnt = {'hard': 0, 'dissolve': 0, 'whip_morph': 0}
    for t in r['cut_times']:
        i = int(t * 30); a, b = max(i - 12, 1), min(i + 12, len(F) - 1)
        d = np.array([np.abs(F[j] - F[j - 1]).mean() for j in range(a, b)])
        if d.sum() == 0: continue
        if d.max() / d.sum() > 0.45: cnt['hard'] += 1; continue
        A, B = F[a - 1], F[b]; mid = F[(a + b) // 2]
        al = np.clip(((mid - B) * (A - B)).sum() / (((A - B) ** 2).sum() + 1e-6), 0, 1)
        resid = np.abs(mid - (al * A + (1 - al) * B)).mean() / (np.abs(A - B).mean() + 1e-6)
        cnt['dissolve' if resid < 0.35 else 'whip_morph'] += 1
    res[vid] = dict(ch=r['ch'], views=r['views'], dur=r['dur'], **cnt)
    print(vid, r['ch'][:12], round(r['views'] / 1e6, 2), cnt, flush=True)
json.dump(res, open(os.path.join(OUT, 'c_transitions.json'), 'w'), indent=1)
