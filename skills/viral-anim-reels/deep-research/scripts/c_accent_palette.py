"""Accent + key-light palette of core Ricks videos from 2fps frames (every 4th frame).
Usage: python -I c_accent_palette.py <research_root>"""
import sys, os, glob, json, numpy as np
from PIL import Image
R = sys.argv[1]
def km(X, k, it=30):
    rng = np.random.default_rng(0); C = X[rng.choice(len(X), k, replace=False)]
    for _ in range(it):
        l = ((X[:, None] - C[None]) ** 2).sum(-1).argmin(1)
        C = np.array([X[l == j].mean(0) if (l == j).any() else C[j] for j in range(k)])
    c = np.bincount(l, minlength=k); o = np.argsort(-c); return C[o], c[o] / c.sum()
P = []; H = []
for d in glob.glob(os.path.join(R, 'videos', 'ricksclips', '*')):
    if json.load(open(os.path.join(d, 'meta.json'), encoding='utf8'))['upload_date'] < '20261007': continue
    for f in sorted(glob.glob(os.path.join(d, 'frames', '*.jpg')))[::4]:
        im = Image.open(f).convert('RGB').resize((45, 80))
        a = np.asarray(im, np.float32).reshape(-1, 3); h = np.asarray(im.convert('HSV'), np.float32).reshape(-1, 3)
        P.append(a); H.append(h)
P = np.concatenate(P); H = np.concatenate(H)
hx = lambda c: '#%02x%02x%02x' % tuple(int(v) for v in c)
for name, m in [('accent S>55% V>45%', (H[:, 1] > 140) & (H[:, 2] > 115)), ('shadows V<30%', H[:, 2] < 77), ('highlights V>80% S<25%', (H[:, 2] > 204) & (H[:, 1] < 64))]:
    X = P[m]; X = X[np.random.default_rng(1).choice(len(X), min(30000, len(X)), replace=False)]
    C, w = km(X, 8)
    print(name, f'{m.mean()*100:.1f}% of px:', ' '.join(f'{hx(c)}:{x*100:.0f}' for c, x in zip(C, w)))
# hue histogram of saturated px
hh = H[(H[:, 1] > 90) & (H[:, 2] > 60), 0] / 255 * 360
b = np.histogram(hh, bins=12, range=(0, 360))[0]; print('hue bins 30deg:', (b / b.sum() * 100).round(1).tolist())
