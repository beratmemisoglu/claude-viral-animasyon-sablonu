"""Validate script.json + package.json against the measured rules (references/02, 03, 06).

  python -I validate.py <slug|project_dir> [--wpm N]   (wpm default from the script language profile)

Exit 0 = no FAIL (WARNs allowed), 1 = at least one FAIL.
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, project_dir, words_of, lower, LANG, lang_of

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("--wpm", type=float, default=None)
a = ap.parse_args()
d = project_dir(a.project)
s = load(os.path.join(d, "script.json"))
p = load(os.path.join(d, "package.json"), {})
lg = lang_of(s)
L = LANG[lg]
a.wpm = a.wpm or L["wpm"]

res = []
def chk(ok, level, msg):
    res.append(("PASS" if ok else level, msg))

BEATS = ["hook", "reaction", "rule", "objection", "false_alarm", "ladder", "counter_clue", "twist", "mechanism", "payoff", "verdict"]
SCHOOL, STAKE, PIVOTS, ANOMALY = L["school"], L["stake"], L["pivots"], L["anomaly"]

lines = s.get("lines", [])
text_all = " ".join(l.get("text", "") for l in lines)
nwords = len(words_of(text_all))
pauses = sum(float(l.get("pause_after", 0) or 0) for l in lines)
est = nwords / a.wpm * 60 + pauses

# --- structure
chk(len(lines) >= 10, "FAIL", f"{len(lines)} lines (need >=10, ~1 per shot; target 14-16)")
chk(L["words"][0] <= nwords <= L["words"][1], "FAIL", f"{nwords} words (target {L['words'][0]}-{L['words'][1]}, lang {lg})")
chk(45 <= est <= 66, "FAIL", f"estimated duration {est:.1f}s at {a.wpm:.0f} wpm + {pauses:.1f}s pauses (target 45-65)")
present = [l.get("beat") for l in lines]
# closing.mode "punchline" = Ricks-style ending (moral line that echoes the hook, no stamp/CTA in the VO;
# the comment question and send CTA live in the caption). Measured on Japan Job (14.7M, top comment rate).
punchline = s.get("closing", {}).get("mode") == "punchline"
for b in ["hook", "rule", "objection", "twist", "mechanism", "payoff"] + ([] if punchline else ["verdict"]):
    chk(b in present, "FAIL", f"beat '{b}' present")
bad = [b for b in present if b not in BEATS]
chk(not bad, "FAIL", f"unknown beat names: {bad}" if bad else "beat names valid")

# --- positions by cumulative words (end-card CTA lines are not part of the story arc)
story = [l for l in lines if not l.get("end_card")]
story_words = len(words_of(" ".join(l.get("text", "") for l in story)))
cum, pos = 0, {}
for l in story:
    w = len(words_of(l.get("text", "")))
    pos.setdefault(l.get("beat"), cum / max(story_words, 1))
    cum += w
if "twist" in pos:
    t = pos["twist"] * 100
    chk(55 <= t <= 75, "FAIL", f"twist starts at {t:.0f}% (target 60-72, max 75)")
if "mechanism" in pos and "twist" in pos:
    chk(pos["mechanism"] >= pos["twist"], "WARN", "mechanism comes after twist")
if "objection" in pos:
    sec = pos["objection"] * nwords / a.wpm * 60
    chk(sec <= 17, "WARN", f"second hook/objection at ~{sec:.1f}s (target 10-13s)")

# --- hook
hook = lines[0].get("text", "") if lines else ""
hw = len(words_of(hook))
chk(L["hook_words"][0] <= hw <= L["hook_words"][1], "FAIL", f"hook {hw} words (target {L['hook_words'][0]}-{L['hook_words'][1]})")
chk(not hook.strip().endswith("?"), "FAIL", "hook is a statement, not a question")
chk(re.search(STAKE, lower(hook, lg)) is not None, "WARN", "hook contains a stake word (million/illegal/alive/fired/...)")
chk(not re.match(L["hook_ban"], lower(hook, lg)), "FAIL", "hook does not open with a banned opener (Look/Imagine/Did you know/How/Why)")
chk(s.get("hook_type") in {"H1", "H2", "H3", "H4", "H6"}, "FAIL", f"hook_type {s.get('hook_type')} allowed (H7/H8/H9 banned)")

# --- rhythm
low = lower(text_all, lg)
yousee = len(re.findall(L["hinge"], low))
chk(yousee >= 1, "WARN", f"hinge '{L['hinge_name']}' used {yousee}x (target 2)")
piv = len(re.findall(PIVOTS, low))
pm = piv / max(est / 60, 0.1)
chk(pm >= 6, "WARN", f"pivots {pm:.1f}/min (target >=6)")
chk('"' in text_all or "“" in text_all, "WARN", "at least one line of dialogue")
chk(re.search(L["proxy"], low) is not None, "WARN", f"audience-proxy '{L['proxy_name']}' present")
longs = [l["n"] for l in lines if len(words_of(l.get("text", ""))) > 34]
chk(not longs, "WARN", f"lines over 34 words: {longs}" if longs else "no overlong lines")

# --- devices / closing
dv = s.get("devices", {})
chk(len(dv.get("comment", [])) >= 2, "FAIL", "devices.comment has >=2 comment devices")
chk(bool(dv.get("send")), "FAIL", "devices.send set")
mw = lower(dv.get("meme_word") or "", lg)
chk(bool(mw) and low.count(mw) >= 2, "WARN", f"meme word '{mw}' repeated >=2x in VO")
if punchline:
    first = set(words_of(lower(hook, lg)))
    last = set(words_of(lower(lines[-1].get("text", ""), lg))) if lines else set()
    chk(len(first & last) >= 2, "WARN", "punchline echoes the hook (shared words) for a loop-like ending")
else:
    chk(bool(s.get("closing", {}).get("verdict")), "FAIL", "closing.verdict (Clause stamp) set")

# --- facts
flag = s.get("fact_flag")
chk(flag in {"G", "G*", "K"}, "FAIL", f"fact_flag {flag} valid")
srcs = [x for x in s.get("sources", []) if x.get("url")]
if flag in {"G", "G*"}:
    chk(len(srcs) >= 1, "FAIL", f"{len(srcs)} sourced claims (need >=1, each with 2 URLs)")
    chk(all(x.get("url2") for x in srcs), "FAIL", "every claim has a second independent source (url2)")
if flag == "K":
    chk(re.search(L["legend"], lower(" ".join(l["text"] for l in lines[:2]), lg)) is not None,
        "FAIL", "fiction/legend is flagged in the first 5 s")
if flag == "G*":
    chk(re.search(L["gstar"], low) is not None, "WARN", "G* claim framed ('most historians say' / 'some call it a myth')")

# --- shots
miss = [l["n"] for l in lines if not (l.get("shot") or {}) or not (l["shot"] if isinstance(l["shot"], dict) else l["shot"][0]).get("noun")]
chk(not miss, "FAIL", f"lines without shot.noun: {miss}" if miss else "every line has a shot with a concrete noun")
allshots = [sp for l in lines if l.get("shot") for sp in (l["shot"] if isinstance(l["shot"], list) else [l["shot"]])]
cams = [sp.get("camera") for sp in allshots]
for need in ["cutaway", "overhead", "iris"]:
    chk(need in cams, "WARN", f"shot type '{need}' used")
chk(any(sp.get("clause") for sp in allshots), "WARN", "Clause appears in >=1 shot")
chk(abs(len(allshots) - est / 3.8) <= 4, "WARN", f"{len(allshots)} shots (target ~{est / 3.8:.0f} = duration / 3.8 s)")

# --- title
t = s.get("title", "")
tw = t.split()
chk(L["title_words"][0] <= len(tw) <= L["title_words"][1], "FAIL", f"title '{t}' has {len(tw)} words (target {L['title_words'][0]}-{L['title_words'][1]})")
chk(not (set(lower(w, lg).strip("?,.'") for w in tw) & SCHOOL), "FAIL", "title has no school words (Science/Behind/Actually/Explained/Facts/Works)")
chk(not lower(t, lg).startswith(L["title_ban_start"]), "FAIL", f"title does not start with '{L['title_ban_start'].strip()}'")
chk(re.search(ANOMALY, lower(t, lg)) is not None, "WARN", "title has an anomaly verb/constraint")
chk(not re.search(r"[#\U0001F300-\U0001FAFF]", t), "FAIL", "title has no emoji/hashtag")
chk(t.endswith("?") == bool(re.search(L["title_q"], lower(t, lg))), "WARN", "question mark only for What If/Would You/Legal-or-not titles")

# --- package
if p:
    ct = p.get("cover_text", "")
    chk(2 <= len(ct.split()) <= 4, "FAIL", f"cover_text '{ct}' 2-4 words")
    chk(lower(ct, lg).strip("?! ") != lower(t, lg), "FAIL", "cover_text is not the title")
    fl = p.get("caption_first_line", "")
    chk(0 < len(fl) <= 80, "FAIL", f"caption_first_line {len(fl)} chars (<=80)")
    chk(lower(fl.strip(), lg) != lower(hook.strip(), lg), "FAIL", "caption first line is not a copy of the VO hook")
    hs = p.get("hashtags", [])
    chk(3 <= len(hs) <= 5, "FAIL", f"{len(hs)} hashtags (3-5)")
    chk(bool(p.get("comment_question")), "FAIL", "comment_question set")
    chk(bool(p.get("pinned_comment")), "WARN", "pinned_comment (sources + answer) set")
    chk(0.3 <= float(p.get("cover_frame_sec", 0)) <= 4, "WARN", "cover_frame_sec in 0.3-4 s (impossible moment)")

fails = [m for lv, m in res if lv == "FAIL"]
for lv, m in res:
    print(f"{lv:4}  {m}")
print(f"\n{nwords} words · ~{est:.1f}s · {len(lines)} lines · FAIL {len(fails)} · WARN {sum(1 for lv, _ in res if lv == 'WARN')}")
sys.exit(1 if fails else 0)
