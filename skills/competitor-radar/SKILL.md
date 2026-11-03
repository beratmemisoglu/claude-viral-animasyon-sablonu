---
name: competitor-radar
description: Daily competitor intelligence for the faceless animated YouTube channel "The Other Self". Scans the competitor channels with the YouTube Data API (what is being watched fast right now, outliers vs each channel's median, durations, title/thumbnail patterns, upload cadence), stores daily snapshots to measure 24h view velocity, then turns the evidence into ORIGINAL film ideas for the inner-voice-film skill (one pain word title + hook + fresh visual metaphor) — never copies a competitor's title, story, character or thumbnail. Use it every day before choosing the next film, and whenever the owner asks "rakipler ne yapıyor", "rakip analizi", "trend", "içerik fikri", "ne izleniyor", "hangi konu tutar".
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    category: youtube
    tags: [youtube, competitors, research, ideas, faceless, animation]
---

# Competitor Radar — The Other Self

Goal: every day, learn **what the audience of faceless "inner struggle" animation is consuming fastest** and convert it
into **one original film decision** (+ a short ranked backlog) for `inner-voice-film`.

## Competitors (edit `competitors.json`)
Day One Films (main), IfverseTales, Last Soul Origin, cheslimpico, Little Wars Films, Inner War Films, Madness Paint,
Pointless Fiction, If Humans.

## Daily procedure (do every step, in order)

1. **Scan** (≈100 API quota units, free):
   `~/the-other-self/.venv-yt/bin/python ~/.claude/skills/competitor-radar/scripts/competitor_scan.py`
   → `~/the-other-self/project/competitors/data/YYYY-MM-DD.json` (raw snapshot) and
   `~/the-other-self/project/competitors/YYYY-MM-DD.md` (metrics report: 24h velocity leaders, outliers, newest uploads,
   title patterns, durations, cadence, Shorts vs long). Read the report fully.
2. **Look at the winners' thumbnails** (vision): `scripts/competitor_scan.py` downloads the top thumbnails to
   `project/competitors/thumbs/YYYY-MM-DD/`. Open the top 6 with the vision tool and note the *craft* only: emotion,
   colour, text (words + punctuation), composition, what is impossible/surprising. **Never** pass these images to
   Higgsfield or any generator (rule: competitor thumbnails are analysis-only).
3. **Diagnose** with `references/method.md` §1: for each top performer write the *underlying pain* (one word), the
   *format signal* (length, title form, hook type), and *why it travels* (identity, universality, curiosity). Separate
   signal from noise: velocity and outlier score beat raw views; one viral video ≠ a trend (need ≥2 channels or
   ≥2 videos).
4. **Generate ideas** with §2: at least 6 idea cards, each = TITLE (one ALL-CAPS pain word people say about themselves)
   · hook line · ritual · the twin's lie · fresh visual metaphor · evidence (which competitor data) · originality check.
5. **Originality gate** (§3, mandatory): reject any idea whose title word, story spine, metaphor or set already exists
   in `project/films/PUBLISHED.md`, `project/TOPICS.md` [x] items, or a competitor title from the last 60 days. Different
   angle on the same pain is allowed only with a new metaphor and a new ritual.
6. **Score & pick** (§4 rubric, 0–5 each: demand, velocity trend, originality, metaphor strength, universality,
   production fit). Pick **one** film for today; keep the rest in `project/TOPICS.md` "Next" (newest evidence first).
7. **Write outputs**:
   - append a dated section to `project/competitors/IDEAS.md` (all cards + scores),
   - update `project/TOPICS.md`,
   - write `project/films/<slug>/BRIEF.md` for today's pick (title, hook, ritual, voice lie ladder seed, metaphor,
     evidence) — this is the input for `inner-voice-film`,
   - one-paragraph Turkish summary for the owner (what is hot, today's pick, why).
8. **Learn**: if our own videos have analytics (`studio/scripts/youtube/yt_stats.py`), compare them with the
   competitors' winners and add 1–3 concrete lessons to `project/LEARNINGS.md`.

## Hard rules
- Copy the *logic*, never the surface: no competitor titles, lines, characters, plots, thumbnails, colours (Day One
  Films' red, their bean character).
- Our universe only: Moon head + his blue shadow twin, black letterboxed stage, ~2:45, ElevenLabs twin voice.
- Evidence or it didn't happen: every idea cites numbers from the snapshot. Never invent metrics; if the scan fails,
  say so and fall back to `project/TOPICS.md`.
- Quota: one scan per day is enough (≈100 units of 10,000).

## Files
| File | Use |
|---|---|
| `competitors.json` | handles to scan (add/remove here) |
| `scripts/competitor_scan.py` | API scan → snapshot JSON + metrics report + top thumbnails |
| `references/method.md` | diagnosis → idea cards → originality gate → scoring rubric, with examples |
