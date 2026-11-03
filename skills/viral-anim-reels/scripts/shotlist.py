"""Turn script lines + VO timings into a timed shot list and Higgsfield prompts.

  python -I shotlist.py <slug|dir>

Needs audio/lines.json + audio/words.json (run tts.py first; --dry is fine for planning).
Writes build/shots.json and shots/PROMPTS.md (keyframe + motion prompt per shot, target file names).
A line's "shot" may be a dict or a list of dicts (split evenly at word boundaries).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, save, project_dir

d = project_dir(sys.argv[1])
s = load(os.path.join(d, "script.json"))
lines = {m["n"]: m for m in load(os.path.join(d, "audio", "lines.json"))}
words = load(os.path.join(d, "audio", "words.json"))
total = words[-1]["e"] + 0.5

STYLE = ("Style: 2D cel-shaded cartoon characters with thick dark-navy outlines inside a richly painted 2.5D "
         "storybook environment, painterly textures, warm practical lights against cool blue ambient shadows "
         "(orange-teal contrast), soft depth of field with a blurred foreground prop, moderate saturation, "
         "no watermark, no realistic human faces, main subject in the upper 60% of the frame, keep the band "
         "between 46% and 60% of the height free of important detail (caption zone), keep the right edge clear.")
SIZE = {"push_in": "medium shot", "truck": "wide shot", "whip": "medium shot", "pull_out": "close-up",
        "overhead": "top-down overhead map view", "cutaway": "cutaway cross-section diorama",
        "iris": "circular magnifying-glass vignette revealing a macro detail", "rack": "close-up", "morph": "medium shot"}
MOVE = {"push_in": "slow dolly push-in toward the {noun}", "truck": "smooth lateral truck right revealing the {noun}",
        "whip": "steady drift toward the {noun}, then a fast whip pan to the right in the last half second",
        "pull_out": "quick pull-back from a close-up of the {noun} to a wide shot",
        "overhead": "slow overhead crane down toward the {noun}", "cutaway": "slow push-in on the cross-section of the {noun}",
        "iris": "slow zoom into the magnified circle showing the {noun}", "rack": "rack focus from the foreground prop to the {noun}",
        "morph": "smooth transformation into the next scene"}
CLAUSE = ("Clause the raccoon inspector (use the CLAUSE reference element: grey raccoon, brass round glasses, green "
          "visor, teal trench coat, mustard scarf, thick navy outline)")

ids = sorted(lines)
shots = []
for i, ln in enumerate(s["lines"]):
    n = ln["n"]
    start = 0.0 if i == 0 else lines[n]["start"]
    end = lines[ids[i + 1]]["start"] if i + 1 < len(ids) else total
    specs = ln.get("shot") or {}
    specs = specs if isinstance(specs, list) else [specs]
    lw = [w for w in words if w["line"] == n]
    cuts = [start]
    for k in range(1, len(specs)):  # split at word boundaries
        idx = round(len(lw) * k / len(specs))
        cuts.append(lw[idx]["s"] if idx < len(lw) else end)
    cuts.append(end)
    for k, sp in enumerate(specs):
        sid = f"s{n:02d}" + ("" if len(specs) == 1 else "abcdef"[k])
        cam = sp.get("camera", "push_in")
        noun = sp.get("noun", "")
        subj = sp.get("action") or (f"{CLAUSE} examines" if sp.get("clause") else "the scene centred on")
        if sp.get("clause") and "Clause" not in subj:
            subj = f"{CLAUSE}; {subj}"
        sign = f'a readable in-world sign that says "{sp["sign"]}", ' if sp.get("sign") else ""
        kp = (f"Vertical 9:16 frame. {subj} — the key object \"{noun}\" clearly visible and large — in "
              f"{sp.get('setting', '')}, {sp.get('time', '')}. Cinematic {sp.get('size') or SIZE.get(cam, 'medium shot')}, {sign}{STYLE}")
        mp = ("Keep the exact art style, outlines and character design of the start image. Camera: "
              + MOVE.get(cam, MOVE["push_in"]).format(noun=noun)
              + f". Subtle character motion only: {sp.get('micro', 'blink and small head turn')}. Gentle parallax, light dust "
              "particles, no scene cut, no new characters, no text changes, no face morphing, continuous motion.")
        shots.append({"id": sid, "line": n, "beat": ln.get("beat"), "start": round(cuts[k], 3), "end": round(cuts[k + 1], 3),
                      "dur": round(cuts[k + 1] - cuts[k], 3), "noun": noun, "camera": cam,
                      "transition": sp.get("transition", "dissolve"), "clause": bool(sp.get("clause")),
                      "keyframe_prompt": kp, "motion_prompt": mp, "vo": ln["text"]})

save(os.path.join(d, "build", "shots.json"), shots)
md = [f"# Shot prompts — {s.get('title', '')} (Case #{s.get('case_no', 0):03d})\n",
      f"{len(shots)} shots · {total:.1f}s · save keyframes as shots/<id>.png and motion clips as shots/<id>.mp4\n"]
for sh in shots:
    flag = "  ⚠ >5 s: consider splitting" if sh["dur"] > 5.2 else ("  ⚠ <2 s" if sh["dur"] < 2.0 else "")
    md += [f"## {sh['id']} · {sh['start']:.2f}–{sh['end']:.2f}s ({sh['dur']:.2f}s) · {sh['beat']} · {sh['camera']} → {sh['transition']}{flag}",
           f"VO: {sh['vo']}", "", "**Keyframe:**", "```", sh["keyframe_prompt"], "```", "**Motion (I2V, 5 s, no audio):**", "```", sh["motion_prompt"], "```", ""]
open(os.path.join(d, "shots", "PROMPTS.md"), "w", encoding="utf-8").write("\n".join(md))
long_ = [x["id"] for x in shots if x["dur"] > 5.2]
print(f"{len(shots)} shots, median {sorted(x['dur'] for x in shots)[len(shots) // 2]:.2f}s, >5.2s: {long_ or 'none'}")
print(os.path.join(d, "shots", "PROMPTS.md"))
