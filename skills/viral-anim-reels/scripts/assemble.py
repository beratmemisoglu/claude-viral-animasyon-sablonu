"""Assemble the final Reel: shots + transitions + VO + music bed + SFX + captions -> build/final.mp4

  python -I assemble.py <slug|dir> [--draft]

Inputs (project folder):
  build/shots.json (shotlist.py), audio/vo.wav + words.json (tts.py), build/captions.ass (captions.py)
  shots/<id>.mp4 (I2V clip)  or  shots/<id>.png|jpg|webp (keyframe -> Ken Burns)  or nothing (placeholder card = animatic)
  music/*.mp3|wav|m4a (optional bed; otherwise a quiet procedural pad placeholder)
Outputs: build/final.mp4, build/cover.jpg, build/ig_caption.txt, build/yt.txt
--draft renders at 540x960 for a fast preview.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, project_dir, run, duration, font, lower, upper, lang_of, W, H, FPS

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("--draft", action="store_true")
a = ap.parse_args()
d = project_dir(a.project)
b = os.path.join(d, "build")
seg_dir = os.path.join(b, "seg")
sfx_dir = os.path.join(b, "sfx")
for x in (seg_dir, sfx_dir, os.path.join(b, "fonts")):
    os.makedirs(x, exist_ok=True)
s = load(os.path.join(d, "script.json"))
p = load(os.path.join(d, "package.json"), {})
shots = load(os.path.join(b, "shots.json"))
lg = lang_of(s)
words = load(os.path.join(d, "audio", "words.json"))
vo = os.path.join(d, "audio", "vo.wav")
ass = os.path.join(b, "captions.ass")
if not os.path.exists(ass):
    sys.exit("build/captions.ass missing — run captions.py first")
ow, oh = (540, 960) if a.draft else (W, H)
fontfile, fam = font()
shutil.copy(fontfile, os.path.join(b, "fonts", os.path.basename(fontfile)))
FONT_REL = "fonts/" + os.path.basename(fontfile)
X = {"dissolve": ("fade", 0.2), "whip": ("smoothleft", 0.15), "morph": ("dissolve", 0.35)}
ENC = ["-c:v", "libx264", "-preset", "veryfast" if a.draft else "medium", "-crf", "20" if a.draft else "17", "-pix_fmt", "yuv420p"]
total = shots[-1]["end"]

# ---------- 1. one normalized segment per shot (length = shot + outgoing transition overlap)
kinds = {"clip": 0, "still": 0, "placeholder": 0}
segs = []
for i, sh in enumerate(shots):
    T = X.get(sh["transition"], X["dissolve"])[1] if i + 1 < len(shots) else 0.0
    L = (shots[i + 1]["start"] - sh["start"] if i + 1 < len(shots) else total - sh["start"]) + T
    out = os.path.join(seg_dir, f"{sh['id']}.mp4")
    cover = f"scale={ow}:{oh}:force_original_aspect_ratio=increase,crop={ow}:{oh},setsar=1,fps={FPS}"
    clip = os.path.join(d, "shots", sh["id"] + ".mp4")
    still = next((f for f in glob.glob(os.path.join(d, "shots", sh["id"] + ".*")) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))), None)
    if os.path.exists(clip):
        avail = max(duration(clip) - 0.25, 0.5)
        slow = min(L / avail, 1.25) if L > avail else 1.0
        vf = f"setpts={slow:.4f}*PTS,{cover},tpad=stop_mode=clone:stop_duration={L:.3f},trim=duration={L:.3f}"
        run(["ffmpeg", "-y", "-ss", "0.25", "-i", clip, "-vf", vf, "-an", *ENC, out]); kinds["clip"] += 1
    elif still:
        n = int(L * FPS) + 1
        zin = sh["camera"] != "pull_out"
        z = f"min(1+0.08*on/{n},1.08)" if zin else f"max(1.08-0.08*on/{n},1.0)"
        vf = (f"scale={ow * 2}:{oh * 2}:force_original_aspect_ratio=increase,crop={ow * 2}:{oh * 2},"
              f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={ow}x{oh}:fps={FPS},setsar=1")
        run(["ffmpeg", "-y", "-loop", "1", "-i", still, "-vf", vf, "-t", f"{L:.3f}", "-an", *ENC, out]); kinds["still"] += 1
    else:
        tf = os.path.join(seg_dir, f"{sh['id']}.txt")
        noun = textwrap.fill(sh["noun"].upper(), 16)  # shot nouns are English (image-prompt language)
        open(tf, "w", encoding="utf-8", newline="\n").write(f"{sh['id']} · {sh['camera']}\n\n{noun}")
        fs = 34 if a.draft else 68
        vf = (f"drawtext=fontfile={FONT_REL}:textfile=seg/{sh['id']}.txt:fontcolor=0xF2B134:fontsize={fs}:"
              f"x=(w-text_w)/2:y=h*0.16:line_spacing=16,fps={FPS}")
        # cwd=build so the drawtext font/text paths have no drive colon
        r = subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=0x101635:s={ow}x{oh}:r={FPS}:d={L:.3f}",
                            "-vf", vf, "-an", *ENC, os.path.relpath(out, b)], cwd=b, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr[-1200:])
        kinds["placeholder"] += 1
    segs.append((out, sh, T))

# ---------- 2. xfade chain (cut points = line starts)
inputs, fc, last = [], [], "[0:v]"
for i, (f, sh, T) in enumerate(segs):
    inputs += ["-i", f]
for i in range(1, len(segs)):
    kind, T = X.get(segs[i - 1][1]["transition"], X["dissolve"])
    off = shots[i]["start"] - T / 2 if i > 0 else 0
    lab = f"[x{i}]"
    fc.append(f"{last}[{i}:v]xfade=transition={kind}:duration={T}:offset={max(off, 0.05):.3f}{lab}")
    last = lab
vid = os.path.join(b, "video_noaudio.mp4")
if len(segs) == 1:
    shutil.copy(segs[0][0], vid)
else:
    run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", last, "-t", f"{total:.3f}", *ENC, vid])

# ---------- 3. SFX + music + VO mix
def sfx(name, expr):
    f = os.path.join(sfx_dir, name + ".wav")
    if not os.path.exists(f):
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", expr, "-ac", "1", "-ar", "48000", f])
    return f

whoosh = sfx("whoosh", "anoisesrc=d=0.45:c=pink:a=0.7,highpass=f=500,lowpass=f=7000,afade=t=in:st=0:d=0.3:curve=exp,afade=t=out:st=0.3:d=0.15")
impact = sfx("impact", "aevalsrc='0.9*sin(2*PI*(70-40*t)*t)*exp(-5*t)':d=0.7")
stamp = sfx("stamp", "aevalsrc='0.9*sin(2*PI*150*t)*exp(-30*t)+0.4*(random(0)-0.5)*exp(-45*t)':d=0.35,lowpass=f=2500")
events = []
for i in range(1, len(shots)):
    tr = shots[i - 1]["transition"]
    if tr == "whip" or (tr == "dissolve" and i % 2 == 0):
        events.append((whoosh, shots[i]["start"] - 0.3, -10 if tr == "whip" else -16))
tw = next((x for x in shots if x["beat"] == "twist"), None)
if tw:
    events.append((impact, tw["start"], -8))
verdict = lower(s.get("closing", {}).get("verdict") or "", lg)
vw = next((w for w in reversed(words) if verdict and lower(w["w"], lg).strip(".,!?") == verdict), None)
vs = next((x for x in shots if x["beat"] == "verdict"), None)
if vw or vs:
    events.append((stamp, (vw["s"] if vw else vs["start"] + 0.3), -6))

mus = sorted(glob.glob(os.path.join(d, "music", "*.*")))
mus = [m for m in mus if m.lower().endswith((".mp3", ".wav", ".m4a", ".flac", ".ogg"))]
music = os.path.join(b, "music_bed.wav")
if mus:
    run(["ffmpeg", "-y", "-stream_loop", "-1", "-i", mus[0], "-t", f"{total:.3f}", "-af",
         f"afade=t=out:st={total - 0.6:.3f}:d=0.6,loudnorm=I=-25:TP=-3", "-ar", "48000", "-ac", "2", music])
else:  # placeholder pad (quiet, continuous) — replace with a real licensed/own bed for publishing
    run(["ffmpeg", "-y", "-f", "lavfi", "-i",
         f"aevalsrc='(0.10*sin(2*PI*110*t)+0.07*sin(2*PI*164.81*t)+0.05*sin(2*PI*220*t)+0.03*sin(2*PI*329.63*t))*(0.7+0.3*sin(2*PI*0.2*t))':d={total:.3f}",
         "-af", "lowpass=f=1500,loudnorm=I=-27:TP=-3", "-ar", "48000", "-ac", "2", music])

ins = ["-i", vo, "-i", music]
fc = ["[0:a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,loudnorm=I=-16:TP=-2,aresample=48000,pan=stereo|c0=c0|c1=c0,asplit=2[vo][vosc]",
      "[1:a][vosc]sidechaincompress=threshold=0.04:ratio=5:attack=20:release=350[mus]"]
mix_in = "[vo][mus]"
for k, (f, t, db) in enumerate(events):
    ins += ["-i", f]
    ms = int(max(t, 0) * 1000)
    fc.append(f"[{k + 2}:a]volume={db}dB,adelay={ms}|{ms},pan=stereo|c0=c0|c1=c0[e{k}]")
    mix_in += f"[e{k}]"
fc.append(f"{mix_in}amix=inputs={2 + len(events)}:normalize=0:duration=first,apad,atrim=0:{total:.3f},alimiter=limit=0.9[mx]")
pre = os.path.join(b, "mix_pre.wav")
run(["ffmpeg", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[mx]", "-ar", "48000", pre])
# two-pass loudnorm -> -14 LUFS / -1 dBTP
r = run(["ffmpeg", "-i", pre, "-af", "loudnorm=I=-14:TP=-1.5:LRA=4:print_format=json", "-f", "null", "-"])
m = json.loads(re.findall(r"\{[^{}]+\}", r.stderr)[-1])
mix = os.path.join(b, "mix.wav")
run(["ffmpeg", "-y", "-i", pre, "-af",
     f"loudnorm=I=-14:TP=-1.5:LRA=4:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
     f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true", "-ar", "48000", mix])

# ---------- 4. burn captions + mux (cwd=build so libass paths have no drive colon)
final = "final_draft.mp4" if a.draft else "final.mp4"
vf = f"subtitles=captions.ass:fontsdir=fonts" + (",scale=540:960" if a.draft else "")
if a.draft:  # captions are authored at 1080x1920: upscale, burn, downscale
    vf = "scale=1080:1920," + vf
r = subprocess.run(["ffmpeg", "-y", "-i", "video_noaudio.mp4", "-i", "mix.wav", "-vf", vf, "-map", "0:v", "-map", "1:a",
                    *ENC, "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-movflags", "+faststart", "-shortest", final],
                   cwd=b, capture_output=True, text=True, encoding="utf-8", errors="replace")
if r.returncode:
    sys.exit(r.stderr[-1500:])

# ---------- 5. cover (impossible-moment frame + 2-4 word text in the 3:4 safe band) + captions text
ct = textwrap.fill(upper(p.get("cover_text") or s.get("title", ""), lg), 14)  # 2-4 words -> 1-3 lines
open(os.path.join(b, "cover_text.txt"), "w", encoding="utf-8", newline="\n").write(ct)
open(os.path.join(b, "cover_case.txt"), "w", encoding="utf-8").write(f"{'DOSYA' if lg == 'tr' else 'CASE'} #{int(s.get('case_no', 0)):03d} · {upper(s.get('series', ''), lg)}")
longest = max(len(x) for x in ct.splitlines())
fs = int(min(150, (ow - 130) / (0.78 * max(longest, 1))))  # ~0.75 em per glyph for Arial Black / Montserrat
vf = (f"drawtext=fontfile={FONT_REL}:textfile=cover_text.txt:fontcolor=white:fontsize={fs}:borderw={fs // 12}:bordercolor=black:"
      f"shadowx=6:shadowy=8:shadowcolor=black:line_spacing={fs // 6}:x=(w-text_w)/2:y=h*0.36,"
      f"drawtext=fontfile={FONT_REL}:textfile=cover_case.txt:fontcolor=0xF2B134:fontsize={max(fs // 3, 14 if a.draft else 28)}:borderw=3:bordercolor=black:"
      f"x=(w-text_w)/2:y=h*0.30")
r = subprocess.run(["ffmpeg", "-y", "-ss", f"{float(p.get('cover_frame_sec', 1.0)):.2f}", "-i", "video_noaudio.mp4", "-frames:v", "1",
                    "-vf", vf, "-q:v", "2", "cover.jpg"], cwd=b, capture_output=True, text=True, encoding="utf-8", errors="replace")
if r.returncode:
    print("cover failed:", r.stderr[-400:])
cap = (f"{p.get('caption_first_line', '')}\n\n{p.get('caption_body', '')}\n{p.get('keywords_line', '')}\n\n{p.get('comment_question', '')}\n\n"
       f"Case #{int(s.get('case_no', 0)):03d} · {s.get('series', '')} · Sources in the pinned comment.\n" + " ".join(p.get("hashtags", [])))
open(os.path.join(b, "ig_caption.txt"), "w", encoding="utf-8").write(cap.strip() + "\n")
open(os.path.join(b, "pinned_comment.txt"), "w", encoding="utf-8").write(p.get("pinned_comment", ""))
open(os.path.join(b, "yt.txt"), "w", encoding="utf-8").write(f"{p.get('yt_title') or s.get('title', '')}\n\n{p.get('yt_description', '')}\n")
print(f"{final}: {duration(os.path.join(b, final)):.2f}s · shots {kinds} · sfx events {len(events)} · music {'file' if mus else 'placeholder pad'}")
print(os.path.join(b, final))
