"""Word-card captions (references/05 §1) from audio/words.json -> build/captions.ass

  python -I captions.py <slug|dir> [--upper] [--hook-band]

Cards: max 2 words / 14 chars, function words glue to the next word, punctuation ends a card,
card appears 33 ms before the word and stays until the next card; last card +0.4 s.
Numbers / money / words listed in script.json "highlight" get yellow (max 1 per 10 cards, 1 in first 3 s).
--hook-band adds package.json cover_text as a top band for 0-2 s (IG test variant).
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, project_dir, font, lower, upper, LANG, lang_of

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("--upper", action="store_true")
ap.add_argument("--hook-band", action="store_true")
a = ap.parse_args()
d = project_dir(a.project)
s = load(os.path.join(d, "script.json"))
p = load(os.path.join(d, "package.json"), {})
words = load(os.path.join(d, "audio", "words.json"))
_, fam = font()
lg = lang_of(s)

FUNC = LANG[lg]["func"]
hi_words = {lower(w, lg) for w in s.get("highlight", [])}

def isfunc(w):
    return lower(w, lg).strip(",.?!;:\"“”") in FUNC


# content words close a card; function words glue forward to the next word (Ricks: ~70 % single-word cards)
cards, cur = [], []
for w in words:
    txt = " ".join(x["w"] for x in cur + [w])
    if cur and (len(cur) >= 2 or len(txt) > 14 or (isfunc(w["w"]) and not all(isfunc(x["w"]) for x in cur))):
        cards.append(cur); cur = []
    cur.append(w)
    if not isfunc(w["w"]) or re.search(r"[,.?!:;]$", w["w"]):
        cards.append(cur); cur = []
if cur:
    cards.append(cur)
# split any card over 14 chars
out = []
for c in cards:
    if len(c) > 1 and len(" ".join(x["w"] for x in c)) > 14:
        out += [[x] for x in c]
    else:
        out.append(c)
cards = out


def ts(t):
    t = max(t, 0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


ev, last_hi = [], -99
for i, c in enumerate(cards):
    st = c[0]["s"] - 0.033
    en = cards[i + 1][0]["s"] - 0.033 if i + 1 < len(cards) else c[-1]["e"] + 0.4
    txt = " ".join(x["w"] for x in c)
    txt = upper(txt, lg) if a.upper else txt
    plain = re.sub(r"[^\w$%₺]", "", lower(txt, lg))
    hi = (re.search(r"[\d$£€%₺]", txt) or plain in hi_words) and i - last_hi >= 10 and not (st < 3 and last_hi >= 0)
    if hi:
        last_hi = i
    size = "" if len(txt) <= 12 else r"{\fs72}"
    ev.append(f"Dialogue: 0,{ts(st)},{ts(en)},{'WordHi' if hi else 'Word'},,0,0,0,,{{\\xshad4\\yshad6}}{size}{txt}")

head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Word,{fam},80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,5,2,65,65,820,1
Style: WordHi,{fam},80,&H000AD6FF,&H000AD6FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,5,2,65,65,820,1
Style: Band,{fam},96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,6,8,65,65,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
if a.hook_band and p.get("cover_text"):
    ev.insert(0, f"Dialogue: 1,{ts(0)},{ts(2.0)},Band,,0,0,0,,{upper(p['cover_text'], lg)}")
path = os.path.join(d, "build", "captions.ass")
os.makedirs(os.path.dirname(path), exist_ok=True)
open(path, "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")
n = len(words) / max(len(cards), 1)
durs = sorted(cards[i + 1][0]["s"] - cards[i][0]["s"] for i in range(len(cards) - 1))
print(f"{len(cards)} cards · {n:.2f} words/card · median {durs[len(durs) // 2]:.2f}s · font {fam} -> {path}")
