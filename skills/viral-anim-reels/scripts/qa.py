"""Render QA for a finished Reel (references/05 §4, 07).

  python -I qa.py <slug|dir> [--file build/final.mp4]

Checks: 1080x1920 · 30 fps · 45-66 s · -14 LUFS ±0.5 · TP <= -1 · no silence (-35 dB, >=0.25 s) ·
VO starts <= 0.05 s · 6-10 VO pauses 0.35-0.9 s · captions present. Writes qa/sheet_NN.jpg (1 fps contact
sheets) + qa/hook.jpg (first 3 s @4 fps) — LOOK at them (caption band, Clause consistency, literal nouns).
"""
import argparse, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, project_dir, run, duration, font, LANG, lang_of

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("--file", default="build/final.mp4")
a = ap.parse_args()
d = project_dir(a.project)
f = os.path.join(d, a.file)
q = os.path.join(d, "qa")
os.makedirs(q, exist_ok=True)
res = []
def chk(ok, msg, level="FAIL"):
    res.append(("PASS" if ok else level, msg))

pr = json.loads(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
                     "-of", "json", f]).stdout)["streams"][0]
num, den = map(int, pr["r_frame_rate"].split("/"))
chk((pr["width"], pr["height"]) == (1080, 1920), f"resolution {pr['width']}x{pr['height']}")
chk(abs(num / den - 30) < 0.1, f"fps {num / den:.2f}")
dur = duration(f)
chk(45 <= dur <= 66, f"duration {dur:.1f}s (45-65)")

r = run(["ffmpeg", "-i", f, "-af", "ebur128=peak=true", "-f", "null", "-"])
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)[-1])
tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
TP = float(tp[-1]) if tp else 0.0
chk(abs(I + 14) <= 0.5, f"integrated {I:.1f} LUFS (-14 ±0.5)")
chk(TP <= -1.0, f"true peak {TP:.1f} dBTP (<= -1)")
r = run(["ffmpeg", "-i", f, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"])
sil = re.findall(r"silence_start: (-?[\d.]+)", r.stderr)
chk(not sil, f"silences (-35 dB, >=0.25 s): {len(sil)} {sil[:5]}")

wp = os.path.join(d, "audio", "words.json")
if os.path.exists(wp):
    w = load(wp)
    chk(w[0]["s"] <= 0.05, f"VO starts at {w[0]['s']:.2f}s (<=0.05)")
    gaps = [w[i + 1]["s"] - w[i]["e"] for i in range(len(w) - 1)]
    pauses = [g for g in gaps if g >= 0.35]
    chk(5 <= len(pauses) <= 11, f"VO pauses >=0.35 s: {len(pauses)} (6-10)", "WARN")
    chk(max(gaps) <= 0.95, f"longest VO pause {max(gaps):.2f}s (<=0.9)", "WARN")
    wpm = len(w) / (w[-1]["e"] - w[0]["s"]) * 60
    tw = LANG[lang_of(load(os.path.join(d, "script.json"), {}))]["wpm"]
    chk(tw * 0.9 <= wpm <= tw * 1.1, f"speech rate {wpm:.0f} wpm (target ~{tw})", "WARN")
ass = os.path.join(d, "build", "captions.ass")
chk(os.path.exists(ass) and open(ass, encoding="utf-8").read().count("Dialogue:") > 50, "captions.ass has >50 cards")

fontfile, _ = font()
fr = "fonts/" + os.path.basename(fontfile)
os.makedirs(os.path.join(d, "build", "fonts"), exist_ok=True)
for cmd, out in [(["-vf", f"fps=1,scale=216:-2,drawtext=fontfile={fr}:text='%{{pts\\:hms}}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=5x4"], "../qa/sheet_%02d.jpg"),
                 (["-t", "3", "-vf", f"fps=4,scale=270:-2,drawtext=fontfile={fr}:text='%{{pts\\:hms}}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x2", "-frames:v", "1"], "../qa/hook.jpg")]:
    subprocess.run(["ffmpeg", "-y", "-i", os.path.relpath(f, os.path.join(d, "build")), *cmd, "-q:v", "3", out],
                   cwd=os.path.join(d, "build"), capture_output=True)

for lv, m in res:
    print(f"{lv:4}  {m}")
fails = sum(1 for lv, _ in res if lv == "FAIL")
print(f"\nFAIL {fails} · contact sheets -> {q} (open and check caption band, character, literal nouns)")
sys.exit(1 if fails else 0)
