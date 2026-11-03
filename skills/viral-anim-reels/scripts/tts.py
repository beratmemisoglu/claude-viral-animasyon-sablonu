"""Narration with word timestamps (ElevenLabs /with-timestamps), one request per script line.

  python -I tts.py <slug|dir>                 # real TTS (needs ELEVENLABS_API_KEY + voice_id in voice-narrator.json)
  python -I tts.py <slug|dir> --dry           # no API: silent VO with estimated timings (animatic / pipeline test)
  python -I tts.py --list-voices "energetic american male storyteller"

Writes audio/vo.wav (mono 48 kHz), audio/words.json [{w,s,e,line}], audio/lines.json [{n,start,end}].
Line keys used: text, spoken (optional TTS override), style (narrator|dialogue|verdict), pause_after (s).
"""
import argparse, base64, json, os, re, sys, urllib.parse, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SKILL, load, save, project_dir, run, duration, words_of, LANG, lang_of

ap = argparse.ArgumentParser()
ap.add_argument("project", nargs="?")
ap.add_argument("--dry", action="store_true")
ap.add_argument("--force", action="store_true")
ap.add_argument("--wpm", type=float, default=None, help="target words/min after optional speed-up (default: language profile)")
ap.add_argument("--list-voices", metavar="QUERY")
ap.add_argument("--lang", default="en", help="language for --list-voices (en|tr)")
a = ap.parse_args()
KEY = os.environ.get("ELEVENLABS_API_KEY")


def api(path, body=None):
    req = urllib.request.Request("https://api.elevenlabs.io" + path, method="POST" if body else "GET",
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"xi-api-key": KEY or "", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read()[:400].decode(errors='replace')}")


if a.list_voices is not None:
    if not KEY:
        sys.exit("ELEVENLABS_API_KEY not set")
    print("== your voices ==")
    for v in api("/v2/voices?page_size=50").get("voices", []):
        print(f"{v['voice_id']}  {v['name']}  {v.get('labels', {})}")
    q = urllib.parse.urlencode({"search": a.list_voices, "gender": "male", "language": a.lang, "page_size": 15})
    print("\n== shared library ==")
    for v in api(f"/v1/shared-voices?{q}").get("voices", []):
        print(f"{v['voice_id']}  {v['name']}  accent={v.get('accent')} age={v.get('age')}  {v.get('preview_url')}")
    sys.exit(0)

d = project_dir(a.project)
s = load(os.path.join(d, "script.json"))
lg = lang_of(s)
a.wpm = a.wpm or LANG[lg]["wpm"] - 3
cfg_path = os.path.join(SKILL, "voice-narrator.json" if lg == "en" else f"voice-narrator-{lg}.json")
CFG = load(cfg_path)
aud = os.path.join(d, "audio")
raw = os.path.join(aud, "raw")
os.makedirs(raw, exist_ok=True)
if not a.dry:
    if not KEY:
        sys.exit("ELEVENLABS_API_KEY not set (use --dry for a timing-only run)")
    if CFG.get("voice_id", "CHOOSE_ME") == "CHOOSE_ME":
        sys.exit(f"{os.path.basename(cfg_path)} voice_id is CHOOSE_ME — the narrator voice is the user's choice. "
                 "Run --list-voices (--lang {lg}), let the user pick, then set voice_id.")


def tts_line(n, text, style):
    """Return (wav_path, words[{w,s,e}]) relative to the trimmed clip start."""
    wav = os.path.join(raw, f"l{n:02d}.wav")
    meta = os.path.join(raw, f"l{n:02d}.json")
    if a.dry:
        ws = words_of(text)
        weights = [0.6 + 0.4 * min(len(w), 12) / 6 for w in ws]  # longer words take longer...
        scale = len(ws) * 60 / a.wpm / max(sum(weights), 1e-6)   # ...but the line still averages the target wpm
        t, out = 0.0, []
        for w, wt in zip(ws, weights):
            dur = wt * scale
            out.append({"w": w, "s": round(t, 3), "e": round(t + dur * 0.92, 3)})
            t += dur
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{t:.3f}", wav])
        return wav, out
    if os.path.exists(meta) and os.path.exists(wav) and not a.force:
        return wav, load(meta)
    st = CFG["styles"].get(style, CFG["styles"]["narrator"])
    r = api(f"/v1/text-to-speech/{CFG['voice_id']}/with-timestamps?output_format=mp3_44100_192",
            {"text": text, "model_id": CFG["model_id"], "voice_settings": st})
    mp3 = os.path.join(raw, f"l{n:02d}.mp3")
    open(mp3, "wb").write(base64.b64decode(r["audio_base64"]))
    al = r.get("normalized_alignment") or r["alignment"]
    chars, cs, ce = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    words, cur, ws_ = [], "", None
    for ch, s0, e0 in zip(chars, cs, ce):
        if ch.isspace():
            if cur.strip():
                words.append({"w": cur.strip(), "s": ws_, "e": pe})
            cur, ws_ = "", None
            continue
        if ws_ is None:
            ws_ = s0
        cur += ch
        pe = e0
    if cur.strip():
        words.append({"w": cur.strip(), "s": ws_, "e": pe})
    t0 = max(0.0, words[0]["s"] - 0.02)
    t1 = words[-1]["e"] + 0.06
    run(["ffmpeg", "-y", "-i", mp3, "-af", f"atrim={t0:.3f}:{t1:.3f},asetpts=PTS-STARTPTS,highpass=f=70",
         "-ac", "1", "-ar", "48000", wav])
    words = [{"w": w["w"], "s": round(w["s"] - t0, 3), "e": round(w["e"] - t0, 3)} for w in words]
    save(meta, words)
    return wav, words


parts, allw, linemap, t = [], [], [], 0.0
for i, ln in enumerate(s["lines"]):
    n = ln["n"]
    style = ln.get("style") or ("verdict" if ln.get("beat") == "verdict" else "dialogue" if re.match(r'\s*["“]', ln["text"]) else "narrator")
    wav, ws = tts_line(n, ln.get("spoken") or ln["text"], style)
    dur = duration(wav)
    parts.append(wav)
    for w in ws:
        allw.append({"w": w["w"], "s": round(t + w["s"], 3), "e": round(t + w["e"], 3), "line": n})
    gap = float(ln.get("pause_after", 0.12) or 0.12) if i < len(s["lines"]) - 1 else 0.5
    linemap.append({"n": n, "start": round(t, 3), "end": round(t + dur, 3)})
    t += dur
    sil = os.path.join(raw, f"gap{n:02d}.wav")
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{gap:.3f}", sil])
    parts.append(sil)
    t += gap

lst = os.path.join(raw, "concat.txt")
open(lst, "w").write("".join(f"file '{p.replace(os.sep, '/')}'\n" for p in parts))
vo_raw = os.path.join(raw, "vo_concat.wav")
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:a", "pcm_s16le", vo_raw])

# optional speed-up toward target wpm (max 1.12x)
speech = allw[-1]["e"] - allw[0]["s"]
wpm = len(allw) / speech * 60
f = 1.0 if a.dry else min(max(a.wpm / wpm, 1.0), 1.12)
vo = os.path.join(aud, "vo.wav")
run(["ffmpeg", "-y", "-i", vo_raw, "-af", f"atempo={f:.4f}" if f > 1.0 else "anull", "-ac", "1", "-ar", "48000", vo])
if f > 1.0:
    for w in allw:
        w["s"], w["e"] = round(w["s"] / f, 3), round(w["e"] / f, 3)
    for m in linemap:
        m["start"], m["end"] = round(m["start"] / f, 3), round(m["end"] / f, 3)
save(os.path.join(aud, "words.json"), allw)
save(os.path.join(aud, "lines.json"), linemap)
print(f"{'DRY ' if a.dry else ''}VO {duration(vo):.2f}s · {len(allw)} words · {wpm * f:.0f} wpm (speed x{f:.2f}) -> {vo}")
