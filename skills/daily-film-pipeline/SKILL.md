---
name: daily-film-pipeline
description: The once-a-day autonomous production run of the YouTube channel "The Other Self" — preflight checks, competitor-radar → today's original idea, inner-voice-film → screenplay + Remotion animation + ElevenLabs twin voice + calm score + QA + YouTube render, other-self-thumbnail → 3 concepts on paper, the agent picks the CTR winner and generates only that ONE thumbnail (Higgsfield), metadata, YouTube Data API upload + thumbnail + publish, logs and a Turkish Discord report. Use it for the daily cron job and whenever the owner says "bugünün filmini yap", "günlük üretim", "daily run", "otomatik film".
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    category: youtube
    tags: [youtube, automation, animation, remotion, pipeline]
---

# Daily Film Pipeline — The Other Self

One run = one finished, uploaded film. Work in `~/the-other-self`. Follow `.hermes.md` rules. The owner decided
(2026-10-15) that this runs **every day without a screenplay approval gate**; quality gates below replace it.

## 0. Preflight (stop and report if anything fails)
`bash ~/.claude/skills/daily-film-pipeline/scripts/preflight.sh` — checks: already published today? (one film per day),
ELEVENLABS_API_KEY set, YouTube token valid, disk ≥ 5 GB, studio typecheck. Then call `mcp__higgsfield__balance`
(need ≥ 15 credits). On failure: do NOT continue; report the exact problem in Turkish.

## 1. Idea (skill `competitor-radar`)
Run the full competitor-radar procedure → `project/films/<slug>/BRIEF.md` (slug = lowercase title word).

## 2. Screenplay (skill `inner-voice-film`, FILM mode steps 1–3)
Write `project/films/<slug>/SCREENPLAY.md` from BRIEF.md: 13 beats, frame ranges summing to 4950 (2:45), voice ledger,
couplets, slogan, PACKAGE. Run the skill's QA checklist (stamp < 0:15, rock bottom 31–40 %, every voice line paid off,
no competitor lines, no red). Fix before building. No approval wait.

## 3. Build (inner-voice-film steps 4–6)
- `cp -r studio/src/films/procrastination studio/src/films/<slug>` as the template (newest, most complete); rewrite
  `timeline.json`, scenes, `Film.tsx` names, and register the film + per-scene compositions in `studio/src/Root.tsx`
  (copy the procrastination Folder block). Reuse `src/lib/` (rig, stage, text, props, TitleCard, Twin, Bedroom-like
  sets). New props go into the film folder.
- `cd studio && npx tsc --noEmit` must pass.
- **Visual QA (mandatory):** `./scripts/stills.sh <slug> "<scene:frames;…>" out/qa/<slug>-N.jpg` for every scene
  (2–3 frames each), open every sheet with the vision tool, fix: text overlapping text/heads/windows/DAY counter,
  off-model character (round head + sprout, oval eyes), limbs detached, empty frames, text outside letterbox. Repeat
  until clean (max 4 rounds).

## 4. Voice + music
- `src/films/<slug>/voice-lines.json` = every blue line (`n`, `text`, `style` whisper|taunt|boss, `spoken` for numbers).
- Copy `studio/scripts/procrastination-cues.mjs` → `<slug>-cues.mjs`, change the scene ids, voice placements
  (`[S.<scene> + <frame of the blue text>, n, gain]`) and SFX for the new sets. Keep the calm music rules.
- `./scripts/audio.sh <slug>` → loudness must print about −15 LUFS.

## 5. Render
`./scripts/render-youtube.sh <slug>` → `project/films/<slug>/<SLUG>-youtube.mp4`. Verify with ffprobe: 1920×1080,
duration ≈ 165 s, audio present. Pull 6 frames with ffmpeg at the milestones (0:08, 0:45, 0:55, 1:05, 2:00, 2:35) and
look at them.

## 6. Thumbnail — ONE final image (owner decision 2026-10-15; no A/B test on the channel)
1. Hook Engine (skill `other-self-thumbnail` §6b): write **3 concepts on paper** (H1 absurd · H2 twin sabotage ·
   H4 extreme emotion), each with text (1–3 words, "." or "?"), scene, emotion, light, title pairing.
2. **Pick the CTR winner yourself**: score each with the 6-question stop-scroll score (0–2 each) + 2 extra points:
   (a) differs from the competitor thumbnails you saw today, (b) text and title do different jobs. Use
   `project/LEARNINGS.md` (what got clicks before) to break ties. Write the 3 scores + the reason into YOUTUBE.md.
3. Generate **only the winner** in Higgsfield (nano_banana_pro, reference `project/brand/profile/ref-hero-standing.png`,
   **2 candidates in one call**, ≈4 credits). Pick the on-model candidate (round bald sand head, ONE leaf sprout, no
   red, no gibberish text). If both drift, regenerate once (max ≈8 credits per film); if still bad, use the runner-up
   concept once. Never exceed ≈8 credits.
4. Overlay the text with `generator/render.py` (baseImage `file:///home/ubuntu/...`) → `project/films/<slug>/thumbs/<SLUG>-thumb.png`
   + `_320` preview; open the 320 px preview with vision and confirm the word, the face and the glow read at phone size.
5. This single image is the one uploaded with the video.

## 7. Metadata + upload
- `project/films/<slug>/YOUTUBE.md` (title, 2 alts, description with REAL chapter timestamps from timeline.json,
  3 hashtags, tags, pinned comment, Shorts ideas).
- `project/films/<slug>/description.txt` and `upload.json`:
  `{"file": "project/films/<slug>/<SLUG>-youtube.mp4", "thumbnail": "project/films/<slug>/thumbs/<SLUG>-thumb.png",
    "title": "<SLUG> | An Animated Short Film", "description_file": "project/films/<slug>/description.txt",
    "tags": [...], "privacy": "private", "publish_at": "<output of: python3 ~/.claude/skills/daily-film-pipeline/scripts/publish_time.py>",
    "category": "1", "synthetic": true}`
- `.venv-yt/bin/python studio/scripts/youtube/youtube_upload.py --meta project/films/<slug>/upload.json`
  (run from `~/the-other-self`). It prints VIDEO id + privacy. NOTE: while the Google API project is unaudited, YouTube
  forces uploads to stay private and ignores publish_at → then tell the owner to press "Publish" in YouTube Studio
  at **17:00 UK time**.
- **Publish time = every day 17:00 Europe/London** (owner decision 2026-10-15; DST-safe via publish_time.py). The cron
  job starts at 07:00 UTC so the film is ready hours before. If production runs late, publish_time.py falls back to
  "now + 20 min" and the report must say so.

## 8. Log + report
- Append to `project/films/PUBLISHED.md` (date, film, id, URL, privacy, notes); mark the topic `[x]` in TOPICS.md.
- Discord report (Turkish, short): film + link, what was verified (stills rounds, loudness, duration), thumbnails
  used (the winner + why it beat the other 2 concepts), Higgsfield credits spent, today's competitor insight, anything the owner must do (e.g. press Publish).

## Failure policy
Any step that still fails after 2 honest fix attempts → stop, do not upload, keep the files, report the error and the
step. Never upload a film that was not visually checked. Never skip the voice (if ElevenLabs fails, stop).
