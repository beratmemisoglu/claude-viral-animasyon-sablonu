"""Caption pop/scale check: per-frame (30 fps) bbox of caption fill in a band. python -I d_pop.py video.mp4 t0 dur y0 y1"""
import sys, subprocess, numpy as np
from scipy import ndimage as ndi
v, t0, dur, y0, y1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
H = y1 - y0
p = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t0), "-t", str(dur), "-i", v, "-vf", f"crop=720:{H}:0:{y0}",
                    "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
a = np.frombuffer(p.stdout, np.uint8).reshape(-1, H, 720, 3).astype(int)
for i, fr in enumerate(a):
    fill = (fr.min(2) > 200) | ((fr[..., 0] > 190) & (fr[..., 1] > 160) & (fr[..., 2] < 120))
    dark = fr.max(2) < 80
    m = fill & ndi.binary_dilation(dark, iterations=4)
    ys, xs = np.where(m)
    if len(xs) < 80:
        print(f"{t0+i/30:.3f} -"); continue
    print(f"{t0+i/30:.3f} w={xs.max()-xs.min():3d} h={ys.max()-ys.min():3d} yc={y0+(ys.max()+ys.min())//2} n={len(xs)}")
