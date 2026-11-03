#!/usr/bin/env python3
"""thumbnail_qa.py - QA gate for a 1280x720 thumbnail against the measured rules of the Low-Budget-Stories DNA
(references/05-packaging.md section 3) and the Humdrum Hours palette (brand/MARKA-RENK-PALETI.md).

Usage:  python thumbnail_qa.py thumb.png [--layout A|B|C] [--palette brand-palette.json] [--quiet]
Needs:  Python 3.9+, numpy, Pillow.   Exit code 1 = at least one FAIL (WARNs never fail).

Checks (pixel-measured on a 320x180 downsample, so a photo plate or a vector draft are treated the same):
  size          16:9, 1280x720 recommended
  mean_luma     0.38..0.65 (winners 0.46 mean); FAIL <0.30 or >0.78
  warm / cool   share of SATURATED pixels (HSV S>=0.25, V>=0.2): warm (hue <70 or >=330) and cool (160..280) each >=15%
  dark_mono     FAIL when mean luma <0.30 AND one cool hue >=59% of saturated pixels (4/8 losers, 0/16 winners)
  amber_share   pixels near the brand amber <=15% (WARN >15, FAIL >25)      [needs palette]
  coral_share   pixels near the brand coral <=10% (WARN >10, FAIL >18)      [needs palette]
  corner_clear  bottom-right 230x110 px (YouTube timestamp) is quiet: luma std <=0.04
  luma_gap      layout A only: |left40% - right40%| mean luma >=0.30
  palette_fit   info only: share of pixels within dE76<=14 of a palette colour
"""
import argparse
import json
import math
import os
import sys

import numpy as np
from PIL import Image

DEFAULT = {"Slate night": "#1E2733", "Overtime amber": "#F2A71B", "Chalk": "#F4F2ED", "Break-room blue": "#5F7F91",
           "Paper": "#D8D5CE", "Ink": "#15181E", "Blank gray": "#8E959C", "Alert coral": "#EE6249", "Okay mint": "#86D0A4",
           "Inner voice cyan": "#6FE3FF", "System violet": "#7B61FF", "Dusk mauve": "#8F6F9E"}


def load_palette(path):
    if path and os.path.isfile(path):
        d = json.load(open(path, encoding="utf-8"))["colors"]
        return {v["name"]: v["hex"] for v in d.values()}
    return DEFAULT


def hex_rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float64)


def to_lab(rgb):  # rgb float 0..255, shape (...,3)
    c = rgb / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def hsv(rgb):
    c = rgb / 255.0
    mx, mn = c.max(-1), c.min(-1)
    d = mx - mn
    h = np.zeros_like(mx)
    r, g, b = c[..., 0], c[..., 1], c[..., 2]
    m = d > 1e-9
    rm = m & (mx == r); gm = m & (mx == g) & ~rm; bm = m & ~rm & ~gm
    h[rm] = ((g - b)[rm] / d[rm]) % 6
    h[gm] = (b - r)[gm] / d[gm] + 2
    h[bm] = (r - g)[bm] / d[bm] + 4
    s = np.where(mx > 0, d / np.maximum(mx, 1e-9), 0)
    return h * 60.0, s, mx


def verdict(v, lo, hi, flo, fhi):
    if v < flo or v > fhi:
        return "FAIL"
    return "PASS" if lo <= v <= hi else "WARN"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image"); ap.add_argument("--layout", choices=["A", "B", "C"]); ap.add_argument("--palette")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    im = Image.open(a.image).convert("RGB")
    W, H = im.size
    small = np.asarray(im.resize((320, 180), Image.LANCZOS), dtype=np.float64)
    luma = (0.299 * small[..., 0] + 0.587 * small[..., 1] + 0.114 * small[..., 2]) / 255.0
    hh, ss, vv = hsv(small)
    sat = (ss >= 0.25) & (vv >= 0.2)
    nsat = max(int(sat.sum()), 1)
    warm = sat & ((hh < 70) | (hh >= 330)); cool = sat & (hh >= 160) & (hh <= 280)
    pal = load_palette(a.palette)
    lab_img = to_lab(small)
    near = lambda name, th=20: float((np.linalg.norm(lab_img - to_lab(hex_rgb(pal[name])), axis=-1) <= th).mean())
    pal_labs = np.stack([to_lab(hex_rgb(h)) for h in pal.values()])
    dmin = np.min(np.linalg.norm(lab_img[..., None, :] - pal_labs[None, None, :, :], axis=-1), axis=-1)

    rows = []
    aspect_ok = abs(W / H - 16 / 9) < 0.01
    rows.append(("size", f"{W}x{H}", "1280x720 (16:9)", "PASS" if (W, H) == (1280, 720) else ("WARN" if aspect_ok else "FAIL")))
    ml = float(luma.mean())
    rows.append(("mean_luma", f"{ml:.2f}", "0.38..0.65", verdict(ml, 0.38, 0.65, 0.30, 0.78)))
    wp, cp = float(warm.sum()) / nsat * 100, float(cool.sum()) / nsat * 100
    rows.append(("warm_share_%", f"{wp:.0f}", ">=15", "PASS" if wp >= 15 else ("FAIL" if wp < 8 else "WARN")))
    rows.append(("cool_share_%", f"{cp:.0f}", ">=15", "PASS" if cp >= 15 else ("FAIL" if cp < 8 else "WARN")))
    # dominant cool hue share (dark monochrome neon check)
    cool_hue_share = cp
    rows.append(("dark_mono", f"luma {ml:.2f}, cool {cool_hue_share:.0f}%", "not (<0.30 and >=59%)",
                 "FAIL" if (ml < 0.30 and cool_hue_share >= 59) else "PASS"))
    am, co = near("Overtime amber") * 100, near("Alert coral") * 100
    rows.append(("amber_share_%", f"{am:.1f}", "<=15", "PASS" if am <= 15 else ("FAIL" if am > 25 else "WARN")))
    rows.append(("coral_share_%", f"{co:.1f}", "<=10", "PASS" if co <= 10 else ("FAIL" if co > 18 else "WARN")))
    big = np.asarray(im, dtype=np.float64)
    y0, x0 = max(H - 110, 0), max(W - 230, 0)
    reg = big[y0:, x0:]
    rstd = float(((0.299 * reg[..., 0] + 0.587 * reg[..., 1] + 0.114 * reg[..., 2]) / 255.0).std())
    rows.append(("corner_clear", f"luma std {rstd:.3f}", "<=0.040", "PASS" if rstd <= 0.04 else "WARN"))
    if a.layout == "A":
        gap = abs(float(luma[:, :72].mean()) - float(luma[:, -72:].mean()))
        rows.append(("luma_gap", f"{gap:.2f}", ">=0.30", "PASS" if gap >= 0.30 else "FAIL"))
    fit = float((dmin <= 14).mean()) * 100
    rows.append(("palette_fit_%", f"{fit:.0f}", "info", "INFO"))
    fails = [r for r in rows if r[3] == "FAIL"]
    if not a.quiet:
        print(f"== thumbnail QA  {os.path.basename(a.image)}  layout={a.layout or '-'}")
        for k, v, n, s in rows:
            print(f"  {s:5s} {k:15s} {v:28s} norm {n}")
        print("RESULT:", "FAIL" if fails else "PASS (WARNs need a reason)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
