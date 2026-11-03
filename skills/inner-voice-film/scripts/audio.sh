#!/usr/bin/env bash
# Voice + soundtrack for a film:  ./scripts/audio.sh <slug>
#   1) shadow lines with the ElevenLabs voice (needs ELEVENLABS_API_KEY; cached mp3s are reused)
#   2) procedural score + SFX from scripts/<slug>-cues.mjs
#   3) compressor + loudnorm -15 LUFS → public/audio/<slug>-mix.wav
set -euo pipefail
SLUG="${1:?usage: audio.sh <slug>}"
cd "$(dirname "$0")/.."
if [ -f "src/films/$SLUG/voice-lines.json" ]; then python3 scripts/eleven_say.py "src/films/$SLUG/voice-lines.json"; fi
python3 scripts/build-film-audio.py "$SLUG"
node "scripts/$SLUG-audio.mjs" "public/audio/$SLUG-mix-raw.wav"
ffmpeg -hide_banner -loglevel error -y -i "public/audio/$SLUG-mix-raw.wav" \
  -af "acompressor=threshold=-22dB:ratio=3:attack=8:release=250:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=11" -ar 48000 -ac 2 "public/audio/$SLUG-mix.wav"
ffmpeg -hide_banner -i "public/audio/$SLUG-mix.wav" -af ebur128 -f null - 2>&1 | grep -E '^\s+I:' | tail -1
