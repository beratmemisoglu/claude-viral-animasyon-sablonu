"""Render thumbnail presets/requests to PNG with headless Edge, then save 320x180 mobile previews + a contact sheet.

usage:  python render.py                      # the 3 built-in presets
        python render.py requests.json        # a list of thumbnail requests (JSON schema in README)
        python render.py --debug              # also render safe-zone overlays
        python render.py requests.json --out=C:\\path\\to\\film\\thumbs   # write PNGs somewhere else
"""
import json, os, shutil, subprocess, sys, urllib.parse
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
_out = [a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--out=")]
OUT = Path(_out[0]).resolve() if _out else HERE / "out"
# Windows: Edge. Linux (VPS): $THUMB_BROWSER, or Chrome / Chromium on PATH, or Remotion's chrome-headless-shell.
EDGE = os.environ.get("THUMB_BROWSER") or (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" if os.name == "nt"
    else shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser") or "chrome")

DEFAULT = [
    {"id": "bedClock", "preset": "bedClock"},
    {"id": "doorLight", "preset": "doorLight"},
    {"id": "phoneBed", "preset": "phoneBed"},
]


def shot(cfg: dict, png: Path):
    url = (HERE / "thumb.html").as_uri() + "?config=" + urllib.parse.quote(json.dumps(cfg))
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1280,720", "--virtual-time-budget=8000", "--allow-file-access-from-files",
                    f"--screenshot={png}", url], check=True, capture_output=True, timeout=120)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    debug = "--debug" in sys.argv
    reqs = json.loads(Path(args[0]).read_text(encoding="utf-8-sig")) if args else DEFAULT
    OUT.mkdir(parents=True, exist_ok=True)
    smalls = []
    for r in reqs:
        rid = r.get("id", r.get("preset", "thumb"))
        cfg = {k: v for k, v in r.items() if k != "id"}
        png = OUT / f"{rid}.png"
        shot(cfg, png)
        im = Image.open(png).convert("RGB")
        assert im.size == (1280, 720), im.size
        small = im.resize((320, 180), Image.LANCZOS)
        small.save(OUT / f"{rid}_320.png")
        smalls.append(small)
        if debug:
            shot(dict(cfg, debug=True), OUT / f"{rid}_debug.png")
        print("ok", png)
    # contact sheet: how they sit next to each other at mobile size
    sheet = Image.new("RGB", (len(smalls) * 330 + 10, 200), (15, 15, 15))
    for i, s in enumerate(smalls):
        sheet.paste(s, (10 + i * 330, 10))
    sheet.save(OUT / "contact_320.png")


if __name__ == "__main__":
    main()
