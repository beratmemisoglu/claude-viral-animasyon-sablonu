"""Build labelled contact sheets from the evidence-pack frames so a reviewer can scan every second.

Usage: python contact_sheets.py <video_dir>
  data/sheets_1fps/sheet_NNN_<start>s.jpg   3x3 grid, 640x360 cells, 1 frame per second (9 s per sheet)
  data/sheets_intro_4fps/isheet_NNN_<start>s.jpg  4x4 grid, 480x270 cells, 4 fps (4 s per sheet), first 60 s
Each cell carries its timestamp (seconds) in the top-left corner.
"""
import glob
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
vd = sys.argv[1]
data = os.path.join(vd, "data")
try:
    font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
except OSError:
    font = ImageFont.load_default()


def build(files, t_of, cols, rows, cw, ch, outdir, prefix, per_label):
    os.makedirs(outdir, exist_ok=True)
    n = cols * rows
    for si in range(0, len(files), n):
        chunk = files[si:si + n]
        sheet = Image.new("RGB", (cols * cw, rows * ch), (16, 16, 16))
        for k, f in enumerate(chunk):
            im = Image.open(f).convert("RGB").resize((cw, ch), Image.LANCZOS)
            dr = ImageDraw.Draw(im)
            lab = per_label(t_of(si + k))
            dr.rectangle([0, 0, 8 + 13 * len(lab), 28], fill=(0, 0, 0))
            dr.text((4, 2), lab, fill=(255, 235, 59), font=font)
            sheet.paste(im, ((k % cols) * cw, (k // cols) * ch))
        start = t_of(si)
        sheet.save(os.path.join(outdir, f"{prefix}_{si // n:03d}_{int(start):04d}s.jpg"), quality=82)


f1 = sorted(glob.glob(os.path.join(data, "frames_1fps", "s*.jpg")))
build(f1, lambda i: float(i), 3, 3, 640, 360, os.path.join(data, "sheets_1fps"), "sheet", lambda t: f"{int(t)}s")
f4 = sorted(glob.glob(os.path.join(data, "frames_intro_4fps", "i*.jpg")))
build(f4, lambda i: i / 4.0, 4, 4, 480, 270, os.path.join(data, "sheets_intro_4fps"), "isheet", lambda t: f"{t:.2f}s")
print(vd, "1fps frames", len(f1), "sheets", len(glob.glob(os.path.join(data, "sheets_1fps", "*.jpg"))),
      "| intro frames", len(f4), "sheets", len(glob.glob(os.path.join(data, "sheets_intro_4fps", "*.jpg"))))
