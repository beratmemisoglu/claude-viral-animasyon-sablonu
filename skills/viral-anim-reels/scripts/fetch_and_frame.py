"""Download YouTube Shorts + auto subs, extract frames, scene cuts and contact sheets.
Usage: python -I fetch_and_frame.py <out_root> <video_id> [<video_id> ...]
Per video: <out_root>/<id>/video.mp4, info.json, subs (*.vtt/json3), frames/ (2 fps), cuts.txt, sheet_*.jpg
"""
import json, os, re, subprocess, sys

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

def process(root, vid):
    d = os.path.join(root, vid)
    os.makedirs(os.path.join(d, "frames"), exist_ok=True)
    mp4 = os.path.join(d, "video.mp4")
    if not os.path.exists(mp4):
        r = run(["yt-dlp", "-f", "bv*[height<=1280][ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
                 "--merge-output-format", "mp4", "-o", os.path.join(d, "video.%(ext)s"),
                 "--write-info-json", "--no-playlist", "--no-warnings",
                 f"https://www.youtube.com/shorts/{vid}"])
        if not os.path.exists(mp4):
            print(vid, "DOWNLOAD FAIL", r.stderr[-400:]); return
    if not any(f.endswith(".json3") for f in os.listdir(d)):
        # best effort: original-language auto captions (word timings); 429 is tolerated
        run(["yt-dlp", "--skip-download", "--write-auto-subs", "--sub-langs", "en-orig,en", "--sub-format", "json3",
             "--sleep-subtitles", "2", "-o", os.path.join(d, "subs.%(ext)s"), "--no-warnings",
             f"https://www.youtube.com/shorts/{vid}"])
    for f in os.listdir(d):
        if f.endswith(".info.json"):
            os.replace(os.path.join(d, f), os.path.join(d, "info.json"))
    # frames at 2 fps
    if not os.listdir(os.path.join(d, "frames")):
        run(["ffmpeg", "-y", "-i", mp4, "-vf", "fps=2,scale=360:-2", "-q:v", "4",
             os.path.join(d, "frames", "f_%04d.jpg")])
    # scene cuts
    r = run(["ffmpeg", "-i", mp4, "-vf", "select='gt(scene,0.15)',showinfo", "-f", "null", "-"])
    cuts = [float(m) for m in re.findall(r"pts_time:([0-9.]+)", r.stderr)]
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp4]).stdout.strip() or 0)
    with open(os.path.join(d, "cuts.txt"), "w") as fh:
        fh.write(f"duration={dur:.2f}\ncuts={len(cuts)}\navg_shot={dur/(len(cuts)+1):.2f}s\n")
        fh.write("\n".join(f"{c:.2f}" for c in cuts))
    # contact sheets: 1 fps, 5x4 tiles with timestamp
    run(["ffmpeg", "-y", "-i", mp4, "-vf",
         r"fps=1,scale=216:-2,drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=5x4",
         "-q:v", "3", os.path.join(d, "sheet_%02d.jpg")])
    # hook sheet: first 3 s at 4 fps
    run(["ffmpeg", "-y", "-t", "3", "-i", mp4, "-vf",
         r"fps=4,scale=270:-2,drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x2",
         "-frames:v", "1", "-q:v", "3", os.path.join(d, "hook_sheet.jpg")])
    # transcript from json3 (word-level)
    for f in os.listdir(d):
        if f.endswith(".json3"):
            j = json.load(open(os.path.join(d, f), encoding="utf-8"))
            lines = []
            for ev in j.get("events", []):
                t = ev.get("tStartMs", 0) / 1000
                txt = "".join(s.get("utf8", "") for s in ev.get("segs", []) or []).strip()
                if txt:
                    lines.append(f"[{t:6.2f}] {txt}")
            open(os.path.join(d, "transcript.txt"), "w", encoding="utf-8").write("\n".join(lines))
            break
    info = json.load(open(os.path.join(d, "info.json"), encoding="utf-8")) if os.path.exists(os.path.join(d, "info.json")) else {}
    meta = {k: info.get(k) for k in ["id", "title", "description", "view_count", "like_count", "comment_count",
                                    "duration", "upload_date", "channel", "tags", "width", "height", "fps"]}
    json.dump(meta, open(os.path.join(d, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(vid, "OK", meta.get("duration"), meta.get("view_count"), len(cuts), "cuts")

if __name__ == "__main__":
    root = sys.argv[1]
    for v in sys.argv[2:]:
        try:
            process(root, v)
        except Exception as e:
            print(v, "ERR", e)
