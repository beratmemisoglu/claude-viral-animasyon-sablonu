"""Transcribe data/audio16k.wav of every vNN_* folder with faster-whisper (GPU), word timestamps.

Usage: venv python transcribe_gpu.py <lbs_dir> [model]
Writes data/transcript_transcribe.{txt,json} next to each audio file. Skips folders already done.
"""
import json
import os
import site
import sys
import wave

sys.stdout.reconfigure(encoding="utf-8")
for sp in site.getsitepackages():
    for sub in ("cublas", "cudnn", "cuda_nvrtc"):
        d = os.path.join(sp, "nvidia", sub, "bin")
        if os.path.isdir(d):
            os.add_dll_directory(d)
            os.environ["PATH"] = d + os.pathsep + os.environ["PATH"]

import numpy as np
from faster_whisper import WhisperModel

root = sys.argv[1]
name = sys.argv[2] if len(sys.argv) > 2 else "medium"
model = WhisperModel(name, device="cuda", compute_type="float16")

for d in sorted(os.listdir(root)):
    data = os.path.join(root, d, "data")
    wav = os.path.join(data, "audio16k.wav")
    out_json = os.path.join(data, "transcript_transcribe.json")
    if not os.path.isfile(wav) or os.path.isfile(out_json):
        continue
    with wave.open(wav, "rb") as w:
        audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    segs_iter, inf = model.transcribe(audio, task="transcribe", language="en", word_timestamps=True, beam_size=5,
                                      vad_filter=True, condition_on_previous_text=False)
    segs = []
    with open(os.path.join(data, "transcript_transcribe.txt"), "w", encoding="utf-8") as txt:
        for s in segs_iter:
            segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
                         "words": [{"w": x.word, "s": round(x.start, 2), "e": round(x.end, 2)} for x in (s.words or [])]})
            m, sec = divmod(int(s.start), 60)
            txt.write(f"[{m:02d}:{sec:02d}] {s.text.strip()}\n")
    json.dump({"language": inf.language, "segments": segs}, open(out_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    words = sum(len(s["text"].split()) for s in segs)
    print(d, "segments", len(segs), "words", words, flush=True)
