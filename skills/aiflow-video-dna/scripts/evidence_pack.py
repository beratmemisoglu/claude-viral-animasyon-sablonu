"""Build the evidence pack used to reverse-engineer (or QA) a YouTube video.

Usage:
  python evidence_pack.py <youtube-url-or-local.mp4> <out_dir> [--whisper medium|small|none] [--lang hi|en|tr|...] [--device cpu|cuda]

Produces in <out_dir>:
  raw/        video.mp4, v.info.json, thumbnail (URL input only)
  data/       frames_1fps/sNNNN.jpg, frames_intro_4fps/iNNNN.jpg, scdet_scores.csv, cuts.csv,
              silences.csv, loudness.txt, audio16k.wav, heatmap.json, comments.json,
              transcript_transcribe|translate.{txt,json}, metrics.json
Requires ffmpeg/ffprobe on PATH, yt-dlp for URLs, faster-whisper (optional) for transcripts.
Run it from a folder that is not inside the download target, and keep out_dir empty/new.
"""
import argparse
import json
import os
import re
import statistics as st
import subprocess
import sys
import wave

sys.stdout.reconfigure(encoding="utf-8")


def run(cmd, cwd=None, check=True):
    print("+", " ".join(cmd[:6]), "…" if len(cmd) > 6 else "")
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True, encoding="utf-8", errors="ignore")


def download(url, raw):
    # metadata + top comments + thumbnail first (captions are often rate-limited; we transcribe locally instead)
    run(["yt-dlp", "--skip-download", "--write-info-json", "--write-thumbnail", "--get-comments",
         "--extractor-args", "youtube:max_comments=400,all,100,0;comment_sort=top", "-o", "v.%(ext)s", url], cwd=raw)
    run(["yt-dlp", "-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/bv*[height<=1080]+ba/b",
         "--merge-output-format", "mp4", "-o", "video.%(ext)s", url], cwd=raw)
    info = json.load(open(os.path.join(raw, "v.info.json"), encoding="utf-8"))
    return os.path.join(raw, "video.mp4"), info


def cuts_from(rows, th, gap=0.25):
    out, last = [], -9.0
    for t, s in rows:
        if s >= th and t - last >= gap:
            out.append((t, s))
            last = t
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--whisper", default="medium")
    ap.add_argument("--lang", default=None)
    ap.add_argument("--device", default="cpu", choices=["cpu", "cuda"],
                    help="cuda needs the nvidia-cublas-cu12 and nvidia-cudnn-cu12 (9.x) wheels in the same venv")
    a = ap.parse_args()

    raw, data = os.path.join(a.out, "raw"), os.path.join(a.out, "data")
    for d in (raw, data, os.path.join(data, "frames_1fps"), os.path.join(data, "frames_intro_4fps")):
        os.makedirs(d, exist_ok=True)

    info = {}
    if re.match(r"https?://", a.src):
        video, info = download(a.src, raw)
        json.dump(info.get("heatmap"), open(os.path.join(data, "heatmap.json"), "w"), indent=0)
        comments = [{"author": c.get("author"), "text": c.get("text"), "likes": c.get("like_count"),
                     "is_pinned": c.get("is_pinned"), "by_uploader": c.get("author_is_uploader"),
                     "parent": c.get("parent")} for c in info.get("comments") or []]
        json.dump(comments, open(os.path.join(data, "comments.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    else:
        video = os.path.abspath(a.src)

    dur = float(json.loads(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", video]).stdout)["format"]["duration"])

    # frames: 1 fps over the whole video, 4 fps over the first 60 s (the hook)
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vf", "fps=1,scale=960:-2", "-q:v", "4", "-start_number", "0",
         os.path.join(data, "frames_1fps", "s%04d.jpg")])
    run(["ffmpeg", "-v", "error", "-y", "-t", "60", "-i", video, "-vf", "fps=4,scale=960:-2", "-q:v", "4", "-start_number", "0",
         os.path.join(data, "frames_intro_4fps", "i%04d.jpg")])

    # scene-change score for every frame; filter paths must be relative (Windows drive colons break filter args)
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-an", "-vf",
         "scale=320:-2,scdet=threshold=10:sc_pass=0,metadata=mode=print:file=scdet_raw.txt", "-f", "null", "-"], cwd=data)
    rows, t = [], None
    for line in open(os.path.join(data, "scdet_raw.txt")):
        if line.startswith("frame:"):
            t = float(line.split("pts_time:")[1])
        elif line.startswith("lavfi.scd.score="):
            rows.append((t, float(line.split("=")[1])))
    with open(os.path.join(data, "scdet_scores.csv"), "w") as f:
        f.write("time_s,score\n")
        f.writelines(f"{t:.3f},{s:.3f}\n" for t, s in rows)
    with open(os.path.join(data, "cuts.csv"), "w") as f:
        f.write("time_s,score\n")
        f.writelines(f"{t:.3f},{s:.2f}\n" for t, s in cuts_from(rows, 8))

    # narration pauses + loudness
    sil_log = run(["ffmpeg", "-v", "info", "-y", "-i", video, "-vn", "-af", "silencedetect=noise=-35dB:d=0.35", "-f", "null", "-"]).stderr
    sil, s0 = [], None
    for line in sil_log.splitlines():
        m = re.search(r"silence_start: ([\d.]+)", line)
        if m:
            s0 = float(m.group(1))
        m = re.search(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", line)
        if m and s0 is not None:
            sil.append((s0, float(m.group(1)), float(m.group(2))))
    with open(os.path.join(data, "silences.csv"), "w") as f:
        f.write("start,end,duration\n")
        f.writelines(f"{x:.2f},{y:.2f},{d:.2f}\n" for x, y, d in sil)
    loud = run(["ffmpeg", "-v", "info", "-y", "-i", video, "-vn", "-af", "ebur128=framelog=quiet", "-f", "null", "-"]).stderr
    lufs = re.search(r"I:\s+(-?[\d.]+) LUFS", loud.split("Summary:")[-1])
    lra = re.search(r"LRA:\s+([\d.]+) LU", loud.split("Summary:")[-1])
    open(os.path.join(data, "loudness.txt"), "w").write(loud.split("Summary:")[-1])

    # cut-rate metrics at several thresholds (calibrate by looking at frames: screen recordings score low)
    metrics = {"duration_s": round(dur, 2), "title": info.get("title"), "views": info.get("view_count"),
               "likes": info.get("like_count"), "comments": info.get("comment_count"),
               "integrated_lufs": float(lufs.group(1)) if lufs else None, "lra_lu": float(lra.group(1)) if lra else None,
               "pauses_ge_0_35s": len(sil), "pause_total_s": round(sum(d for *_, d in sil), 1), "cuts": {}}
    for th in (4, 6, 8, 10, 15, 25):
        c = cuts_from(rows, th)
        ts = [0.0] + [t for t, _ in c] + [dur]
        shots = [b - x for x, b in zip(ts, ts[1:])]
        metrics["cuts"][f"score>={th}"] = {"count": len(c), "per_min": round(len(c) / dur * 60, 2),
                                           "mean_shot_s": round(st.mean(shots), 2), "median_shot_s": round(st.median(shots), 2),
                                           "max_shot_s": round(max(shots), 1)}
    json.dump(metrics, open(os.path.join(data, "metrics.json"), "w"), indent=1)
    print(json.dumps(metrics, indent=1))

    # mono 16 kHz audio + transcript (original language and English translation)
    wav = os.path.join(data, "audio16k.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000", wav])
    if a.whisper != "none":
        if a.device == "cuda":
            # register the CUDA runtime DLLs shipped by the nvidia-* wheels before ctranslate2 loads
            import site
            for sp in site.getsitepackages():
                for sub in ("cublas", "cudnn", "cuda_nvrtc"):
                    d = os.path.join(sp, "nvidia", sub, "bin")
                    if os.path.isdir(d):
                        os.add_dll_directory(d)
                        os.environ["PATH"] = d + os.pathsep + os.environ["PATH"]
        try:
            import numpy as np
            from faster_whisper import WhisperModel
        except ImportError:
            print("faster-whisper not installed: pip install faster-whisper (in a venv) — transcript skipped")
            return
        with wave.open(wav, "rb") as w:
            audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
        if a.device == "cuda":
            model = WhisperModel(a.whisper, device="cuda", compute_type="float16")
        else:
            model = WhisperModel(a.whisper, device="cpu", compute_type="int8", cpu_threads=os.cpu_count())
        tasks = ["transcribe"] if (a.lang or "en") == "en" else ["transcribe", "translate"]
        for task in tasks:
            segs_iter, inf = model.transcribe(audio, task=task, language=a.lang, word_timestamps=True, beam_size=5,
                                              vad_filter=True, condition_on_previous_text=False)
            segs = []
            with open(os.path.join(data, f"transcript_{task}.txt"), "w", encoding="utf-8") as txt:
                for s in segs_iter:
                    segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
                                 "words": [{"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2)} for w in (s.words or [])]})
                    m, sec = divmod(int(s.start), 60)
                    txt.write(f"[{m:02d}:{sec:02d}] {s.text.strip()}\n")
            json.dump({"language": inf.language, "task": task, "segments": segs},
                      open(os.path.join(data, f"transcript_{task}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(task, "segments:", len(segs))


if __name__ == "__main__":
    main()
