# L4 — Quantitative edit rhythm and sound design (all 10 corpus videos)

Analyst 4. Every number below was measured on the local files with `scripts/rhythm_qa.py` (final run, all 10 videos),
ffmpeg EBU R128 (100 ms momentary / 3 s short-term log, true peak), mid/side decomposition (music is mostly stereo, TTS dialogue
is mono centre, so the stereo **side** channel isolates the music bed), spectral-flux transient detection, pYIN pitch on dialogue
lines, spectral cross-correlation between end cards, the "most replayed" heatmap and the whisper word timestamps.
Frame evidence: full per-second pass of v07 and v08 (see their teardowns); for the other 8 videos sheets 1, 2, mid and last,
plus frame montages of every long hold and every top replay peak (`v07…/data/extra/a4_rhythm/corpus_long_holds.jpg`,
`corpus_top_replay.jpg`). Per-video outputs of the final run are in every `vNN_…/data/extra/a4_rhythm/`
(`rhythm_report.json`, `shots.csv`, `seconds.csv`; boundary montages for v07, v08, v10). Family labels: **Doomer saga** v01 v02 v04 · **Job ("Life of a …")** v03 v06 v08 ·
**Dystopia** v05 v07 v09 · **Addiction cycle** v10.

---

## 0. Calibration — what counts as a "cut" on this channel

The channel's pictures are still composites (2D cut-out characters on photos/3D renders) animated by a virtual camera, so a
raw scene-change score both over- and under-counts. I checked before/after frame pairs for every boundary in v07, v08 and
v10 and every candidate class below.

| Event | What it looks like | scdet ≥ 8 | Counted as a boundary? |
|---|---|---|---|
| Hard cut | 1-frame change of framing/location | yes (857 of 864 scdet cuts matched) | **yes** |
| Quick reframe | 4–12 frame (0.16–0.5 s) zoom/whip from a 2-shot to a single on the same composite, or a cut into moving stock footage | **missed** (scores 3–9 spread over frames) | **yes** — it is how the channel cuts without drawing a second shot (79 found, 15 in v07) |
| Slide-pan | 13–35 frame eased slide between two speakers on one wide plate | missed | **yes** (25 found; v09 warehouse, v10 angel/devil) |
| Dissolve / triple exposure | blend of two shots over ~1 s | partly | yes (26) |
| Black hold / fade | luma < 6/255 ≥ 0.2 s; opening fade-in < 1.2 s ignored | counts black + next shot as one long shot | black is its own "shot"; excluded from shot statistics |
| Slow push-in, parallax walker, character crossing frame, pose swap (face/arm drawing replaced) | in-shot motion | sometimes fires (score 3–6) | **no** (pose swaps reported separately, 1.5–13.8 /min) |
| Fade/brightness ramp on the same picture (end-card fade) | histogram moves, structure constant | fires | no (rule: histogram-only jump with structure change < 0.10 = fade) |

Net effect: calibrated boundaries = scdet ≥ 8 cuts **+17 %** (1,012 vs 864 in the 10 stories; scdet-only false positives: 7).
The difference matters most in the talky videos (v05 +32 boundaries, v10 +32, v06 +21) where dialogue is staged on one
plate with reframes/pans. All numbers below are calibrated and computed on the **story only** (0 → start of end card).

---

## 1. Comparison table (calibrated)

| | v01 | v02 | v03 | v04 | v05 | v06 | v07 | v08 | v09 | v10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Views (M) | 6.39 | 4.96 | 4.93 | 4.43 | 3.41 | 3.46 | 3.16 | 2.82 | 2.66 | 2.46 |
| Family | Doomer | Doomer | Job | Doomer | Dystopia | Job | Dystopia | Job | Dystopia | Addiction |
| Voice | none | TTS | TTS | none | TTS | TTS | TTS | TTS | TTS | TTS |
| Story length s | 215 | 274 | 445 | 161 | 433 | 446 | 412 | 205 | 351 | 407 |
| Boundaries (cut/reframe/pan/diss/black) | 68/2/1/2/1 | 71/5/0/4/3 | 146/13/1/0/0 | 56/1/5/0/1 | 81/26/5/4/0 | 95/24/1/3/0 | 122/15/5/3/0 | 56/8/0/1/1 | 70/3/5/3/2 | 69/14/5/7/4 |
| **Boundaries/min (story)** | 20.6 | 18.2 | 21.6 | **23.5** | 16.1 | 16.5 | 21.1 | 19.3 | **14.2** | 14.6 |
| 0–15 s /min | 20 | 16 | 24 | 20 | 16 | 28 | 20 | 16 | 20 | **8** |
| 15–60 s /min | 18.7 | 17.3 | 26.7 | 21.3 | 16.0 | 16.0 | 22.7 | 22.7 | 22.7 | 17.3 |
| body (60 s → −30 s) /min | 22.6 | 19.3 | 21.1 | 25.3 | 16.6 | 16.5 | 21.0 | 19.7 | 12.9 | 15.5 |
| last 30 s of story /min | 16 | 14 | 18 | 24 | 10 | 12 | 20 | 14 | 10 | **4** |
| Shot p10 / median / mean / p90 s | 1.54/2.64/2.88/4.43 | 1.28/2.96/3.30/5.64 | 1.28/2.28/2.77/5.00 | 1.49/2.44/2.53/3.66 | 1.52/3.12/3.70/6.18 | 1.48/3.00/3.60/6.08 | 1.40/2.34/2.82/5.10 | 1.14/2.44/3.03/6.17 | 1.69/3.60/4.23/7.63 | 1.27/3.08/4.07/7.28 |
| Max story shot s | 6.5 | 10.0 | 9.6 | 6.1 | **17.3** | 14.0 | 8.7 | 9.5 | 14.6 | **35.1** |
| Shots > 8 s / > 10 s | 0/0 | 4/0 | 1/0 | 0/0 | 4/1 | 5/2 | 1/0 | 3/0 | 7/6 | 8/6 |
| First boundary s | 1.9 | 3.9 | 2.2 | 2.7 | 2.9 | 1.4 | 3.1 | 3.7 | 5.6 | 4.5 |
| Black inside story s | 1.9 | 6.1 | 1.7 | 1.9 | 4.1 | 0 | 0 | 8.4 | 4.4 | **20.2** (chapter cards) |
| End card s | 4.9 | 7.3 | 7.3 | 8.8 | 7.3 | 7.3 | 14.6 | 5.0 | 8.0 | 13.8 |
| Push-in share of runtime % | 47 | 40 | 30 | 43 | 27 | 23 | 14 | 26 | 13 | 33 |
| Pose swaps /min | 2.7 | 1.5 | 9.0 | 13.8 | 6.8 | 2.2 | 5.8 | 2.9 | 2.5 | 2.7 |
| Integrated LUFS / LRA LU | −14.6/11.3 | −20.6/10.1 | −21.9/12.8 | **−10.5**/10.8 | −21.4/12.3 | −22.5/**15.7** | −19.9/11.9 | −16.6/**9.6** | −18.1/12.5 | −20.1/12.7 |
| True peak dBTP | −3.0 | −2.6 | −0.5 | +0.7 | +0.3 | −4.2 | −0.7 | +0.7 | +0.4 | +0.4 |
| Momentary p10/p50/p90 LUFS | −26/−15/−13 | −39/−22/−19 | −39/−25/−19 | −23/−10/−9 | −37/−24/−19 | −39/−26/−20 | −34/−21/−18 | −36/−19/−14 | −29/−19/−15 | −44/−24/−18 |
| Short-term LUFS first 15 s vs body | −24 vs −14 | −38 vs −21 | silent vs −23 | −25 vs −10 | −24 vs −23 | −27 vs −24 | −31 vs −21 | −19 vs −18 | −27 vs −19 | −33 vs −23 |
| Music under story % | 100 | 99 | 95 | 98 | 97 | 85 | 93 | 87 | 97 | 77 |
| Speech share % (words) | 0 | 55 | 48 | 0 | 51 | 51 | 55 | 32 | 57 | 42 |
| First word s | — | 14.1 | 32.6 | — | 7.2 | 26.6 | 21.7 | 3.5 | 12.9 | 3.1 |
| WPM inside turns | — | 199 | 165 | — | 189 | 172 | 204 | 162 | 185 | 151 |
| Word-gap median s (0.3–2 s gaps) | — | 0.44 | 0.56 | — | 0.46 | 0.46 | 0.44 | 0.58 | 0.48 | 0.49 |
| Longest wordless stretch s | 215 | 22 | 33 | 161 | **60** | 49 | 31 | 26 | 23 | 58 |
| Bed below voice LU (median momentary) | — | 6.4 | 8.7 | — | 7.4 | 11.9 | 9.3 | 2.8 | 9.1 | 5.1 |
| Music change at speech onset dB (ducking test) | — | +0.1 | −0.8 | — | −2.7 | +0.2 | +2.0 | −1.6 | +0.9 | −1.1 |
| Silences ≥ 1 s inside story | 1 | 1 | 4 | 1 | 2 | 1 | 4 | 0 | 1 | 6 |
| Non-voice transients /min | 0.5 | 2.1 | 7.8 | **0.0** | 4.8 | 7.7 | 3.2 | 5.4 | 3.3 | 5.7 |
| Credited music | "After Dark" piano/orchestral edit | Whitesand – Melody of my dreams | Sneaky Snooper; Brain Trust; Throwdown | MGMT – Little Dark Age (instr.) | Sneaky Snooper; Legend (Zyzz theme); Investigations | Sneaky Snooper; Fight Scene; Brain Trust | Brain Trust; Sneaky Snooper; Milk Coffee | I like Peanuts; "Villain music" | Milk Coffee; Broken Piano; Mysterious | Legionnaire; Game Over (metal); cinematic tense |
| Top replay peak (position in story) → screen | 0.87 betrayal reveal (girlfriend, roses) | 0.87 mirror: transformed body | 0.94 phone: viral post of his own fight | 0.41 whiteboard "Goals" list swap | 0.39 gym screen playing a meme fitness video | 0.99 last gag before end card | 0.89 hidden recorder in car | 0.88 news headline after elided crash | 0.85 VR-catfish reveal | 0.80 "monthly payment complete" → wrecked face |

Ranking signal (descriptive, n = 10, confounded with upload era and topic): Spearman ρ(views, boundaries/min) = **+0.56**;
every video with a story shot > 13 s (v05, v06, v09, v10) ranks 5th–10th, and every top-4 video keeps its longest story
shot ≤ 10 s.

---

## 2. Shot-length distribution (1,006 story shots pooled)

| p10 | p25 | median | p75 | p90 | mean | shots < 1.5 s | shots > 8 s |
|---|---|---|---|---|---|---|---|
| 1.36 s | 1.88 s | **2.66 s** | 4.03 s | 5.70 s | 3.28 s | 13.4 % | 3.3 % |

Per family: Doomer saga median 2.44–2.96 s and **max ≤ 10 s** (music-driven, montage-like); Job median 2.28–3.00;
Dystopia 2.34–3.60 with the longest talky holds; Addiction 3.08 with a 35 s hold.

**Longest holds and what they do (frame-verified):**

| Video | Hold | What is on screen | Function |
|---|---|---|---|
| v10 | 6:01.5, 35.1 s | lonely CU at an office party, colleagues blurred behind | isolation beat (static, almost no picture change) |
| v10 | 2:31.7, 21.5 s | lunch-table 2-shot with a colleague, slow push from WS to CU | pressure conversation |
| v05 | 5:01.7, 17.3 s | WS of three characters in the gym, group dialogue | exposition |
| v09 | 1:37.4, 14.6 s | warehouse conveyor with slide-pans following a parcel between two workers | dialogue on one plate |
| v06 | 5:58.0, 14.0 s / 6:56.3, 13.3 s | break-room door 3-shot; aisle 2-shot | dialogue |
| v02 | 3:02.2, 10.0 s | mentor and protagonist over a night city, slide | mentor speech |
| v08 | 1:51.3, 9.5 s | bench CU, "I love this job…" | dramatic-irony monologue |
| v07 | 5:26.7, 8.7 s | car 2-shot | debate |
| v01 / v04 | 6.5 s / 6.1 s | push-ins on emotional CUs | music beat |

Rule extracted: **every hold > 8 s in the corpus is a dialogue or monologue shot; no action, montage or reaction shot
exceeds 6.5 s.** The wordless videos never hold > 6.5 s.

---

## 3. Rhythm vs. story beats

1. **Speech density drives the cut rate** (294 ten-second windows of the 8 voiced videos, Spearman ρ = −0.25; per video
   −0.11 to −0.57). Windows with ≥ 70 % speech: median **12 boundaries/min**; windows with < 70 % speech: median **18**.
   Per beat in v07: wordless plot beats 25–32/min, dialogue beats 10.7–18/min; in v08:
   montage 23–44/min, monologues 6–12.5/min.
2. **Flat body, slower ending.** Runtime-decile means (all 10): 19.4 · 19.9 · 20.4 · 18.4 · 21.0 · 18.2 · 17.9 · 18.3 · 18.3 ·
   **13.9**. The last decile is slower in 7/10 (exceptions v04, v05, v07) — endings settle into a reveal hold
   (v08 drone pull-back 8.2 s, v10 35 s CU, v02 mirror) before the end card.
3. **Acceleration spikes = turning points without words**: v08 applying/hired 39/min, sabotage ladder 32/min, hospital
   reveal 44/min; v07 street→bus 32/min, bus complaint 31/min. Deceleration = argument (v07 car 14/min, confession 10.7/min) or irony.
4. **Act breaks are marked by black or a cue change, not by a cut-rate change**: v08 5.6 s black + sub hit at 57 % of
   the story; v02 black at 2:15 (49 %); v10 chapter cards "Phase N – …" in white bold sans, centred, on black or superimposed (0:00, 2:16, 2:19, 3:18).
5. **Replay ≠ rhythm.** Heatmap vs. local cut density: ρ = −0.06…+0.18 in all 10 (no relationship); heatmap vs. speech share
   −0.30…+0.18 (replays sit slightly more on wordless moments). What replay peaks share is **content**: the top peak lies at
   **80–99 % of the story in 8/10** and is always a reveal/payoff frame; in 6/10 it contains readable text or UI (news
   headline, whiteboard list, phone payment notice, viral post, recorder label). Exceptions v04/v05 (top peak at 39–41 %)
   are also text/meme inserts (goal list, meme fitness clip).

---

## 4. Audio — measured grammar

**Loudness.** Voiced stories −16.6…−22.5 LUFS integrated (median −20.4); wordless music films −10.5 and −14.6 (louder by
6–10 LU, music mastered as a song). LRA 9.6–15.7 LU (median 12.1). True peak −4.2…+0.7 dBTP — **5/10 exceed 0 dBTP after
encoding** (no limiter discipline). Openings are soft: the first 15 s run **≥ 2.8 LU quieter than the body in 8/10, ≥ 8.9 LU in
7/10** (fade-in, ambient bed, pantomime), then the level settles.

**Music presence and roles.** A bed sits under 77–100 % of every story (≥ 85 % in 9/10). Cue changes happen on location cuts
and act breaks; 2–4 credited tracks per voiced video. Roles found by spectral character + placement:
- *Mischief/comedy cue* (pizzicato/plucked library cue; "Sneaky Snooper" credited in 4/10: v03 v05 v06 v07) under setups, schemes, everyday humiliation.
- *Dark/villain cue* (low, minor; "Brain Trust" credited 3/10, "Villain music" v08) from the act break to the end.
- *Cool/idyll cue* (jazz/boom-bap loop; "Milk Coffee" credited 2/10; v08 montage) for rides with a "Chad", montages.
- *Hype cue* for a hero entrance (v05 meme hardstyle anthem for the gym), *epic/metal* for addiction peaks (v10).
- *Emotional anthem* for the wordless Doomer films: one meme-famous song as instrumental/cover for the whole film (v01 synth-pop piano/orchestral edit, estimator ≈ 129 BPM; v04 indie-synth instrumental ≈ 99 BPM); v02 a soft ambient piano track (≈ 89 BPM, A major after the mentor arrives).
- Licensing: voiced videos use royalty-free / CC-BY library cues (Audionautix, Kevin MacLeod, Scott Buckley, YouTube-library style) [inferred from credits]; the two wordless top-5 films use commercial songs (an MGMT instrumental and a cover edit) [inferred → likely Content-ID claimed; do not copy].
- Tempo/key estimates on mixed material are unstable (the estimator returns 66–172 BPM within one video); only the tracks that run alone are reliable (v01 ≈ 129, v04 ≈ 99, v02 ≈ 89 BPM, outro loop 1.81 s bar ≈ 66/133 BPM).

**Ducking: none.** Music level 0.2–1.0 s before vs. 0.3–1.1 s after each speech-turn onset changes by −2.7…+2.0 dB
(median per video) — no dip in 8/8 voiced videos. Separation is a **static mix**: bed 2.8–11.9 LU (median ≈ 8) under the
voice; long dialogue scenes get a quieter or low-passed cue (v07 tunnel: bed energy only < 1 kHz) instead of a duck.

**Music-off and silence rules.** True silence (≤ −45 LUFS) ≥ 1 s inside a story occurs 0–6 times (median 1); every
instance is on a decision, verdict or reveal: v07 1:08 (choosing, 4.0 s), 6:47 (after the verdict, 4.1 s); v08 has no
silence but removes the music for the overlord's last line (3:06.9–3:11.4); v03 opens with 2.6 s + 5.4 s silences under the
"your shift starts in 30 minutes" phone notification and the forced-grin mirror beat (0:04–0:16); v10 uses 4.6–5.6 s silences on its chapter cards. v02 ends the story into **11.2 s of silence** across the
end card (commenters single out "the silence at the end").

**End-card audio is a fixed asset.** Spectral cross-correlation of the first 5.5 s of every end card: v03, v04, v05, v06,
v07, v10 are **identical (r = 0.93–1.00)** — a mono drum-led loop with a 1.81 s bar; v08 (May 2022) uses the same loop as its
delivery-montage bed (r = 0.80–0.92); v01/v09 let the story music run into the card; v02 is silent. End-card length 7.28 s
in 4/10 (v02 v03 v05 v06) → a fixed template clip; overall 4.9–14.6 s; always the same orange card.

**SFX.** Wordless films: 0–0.5 non-voice transients/min (the music does everything). Voiced: 2.1–7.8/min, each tied to a state
change on screen. Inventory with measured shape:
| SFX | Shape | Where |
|---|---|---|
| UI click / notification tick | 6.7–7.3 kHz centroid, 50–120 ms | every phone/Governbot card (v07 ×8), "Apply" tap (v08) |
| Notification whoosh | 4.3 kHz noise, 0.4 s | "NEW ORDER" insert (v08 1:27.96) |
| Idea / reward chime | tonal 1.6–2.7 kHz, 0.3–0.65 s | grin of an idea (v08 0:26.9, v07 1:42.3), score gain |
| Object / costume thud | centroid 280–430 Hz, ≥ 60 % energy < 300 Hz, 0.1–0.5 s | one per garment (v08 dress-up), cap throw, door |
| Sub boom | centroid 60–110 Hz, 0.7–4 s | act-break black, overlord reveal, "absolute hell", drone reveal, final verdict |
| Musical hit / riser | sustained 1.1–2.2 s | entering a new location (v07 tunnel 1:51) |
| Typing clicks | 1.2–1.7 kHz, 20–70 ms, bursts | someone writing a complaint (v07 3:16–3:19) |
| (absent) impact/crash, footsteps, room tone, ambience beds | — | violence is elided silently (v08 2:57) |

**Voices (8 voiced videos).** Synthetic (TTS), high confidence: 1 filler in 5,343 transcribed words (a scripted "Um... me." in
v02 1:19) and no other disfluency; identical
inter-line gap medians 0.44–0.58 s across 8 videos made over 2 years; flat prosody (male lines 3.5–10 semitone range,
f0 ≈ 86–103 Hz for the protagonist and the "Chad"); accents chosen as presets (overlord with a French-sounding accent,
servant German-sounding, Sydney/Brooklyn accents swapped in v09 — 1,400- and 759-like comments mock it); explicit comments:
"obvious AI voices" (v09), "voice bot could be upgraded to the Elevenlabs level", "robovoices even more robotic for
government bots" (v05), "Radio TTS voice" (v07). Rates: 151–204 WPM inside turns; single short lines 225–320 WPM. System
characters (Governbot, gym AI) = female assistant voice; enforcement/government = pitched-down monotone. Processing: dry,
level-constant (momentary −15…−20 LUFS per line), no reverb, no room tone. Antagonist lines with accents get burned-in
white subtitles.

---

## 5. Invariant formula (holds in ≥ 8/10)

1. Story cut rate **14–24 boundaries/min** (10/10), median shot **2.3–3.6 s** (10/10), p90 ≤ 7.7 s (10/10).
2. First boundary ≤ 5.7 s (10/10); 15–60 s segment ≥ 16 boundaries/min (10/10).
3. No action/reaction shot > 6.5 s; holds > 8 s are dialogue/monologue only (10/10).
4. Opening fade-in from black ≤ 1.2 s and a soft first 15 s (≥ 2.8 LU under the body) (8/10).
5. Music under ≥ 85 % of the story (9/10); cue changes at location/act cuts; **no sidechain ducking** (8/8 voiced).
6. TTS voices, dry, 150–205 WPM, 0.44–0.58 s gaps (8/8 voiced).
7. Silence ≥ 1 s used ≤ 6 times and only on decisions/verdicts/reveals (10/10).
8. Slow push-ins on 13–47 % of runtime + reframes instead of new shots (10/10).
9. Orange end card 4.9–14.6 s; fixed outro audio in 6/10 (all post-2023 voiced videos + v04).
10. Top replay peak on a reveal/payoff frame, at 80–99 % of the story (8/10); replay is unrelated to cut density (10/10).

## 6. Variations by format family

| Family | Rhythm | Sound |
|---|---|---|
| Doomer saga (v01, v04 wordless; v02 voiced) | fastest and most even: 18–24/min, max shot ≤ 10 s, last 30 s 14–24/min; pose swaps up to 13.8/min carry "acting" | one emotional song for the whole film, −10.5/−14.6 LUFS, 0–0.5 SFX/min; v02: soft ambient + mentor voice, silent end card |
| Job "Life of a …" (v03, v06, v08) | 16.5–21.6/min; cold-open morning/home routine montage (v06 0–15 s at 28/min, title card at 0:16); dialogue holds up to 14 s in v06 | comedy library cue + villain/fight cue; most SFX (5.4–7.8/min: UI, chimes, thuds); v08 loudest (−16.6) |
| Dystopia (v05, v07, v09) | 14.2–21.1/min; system UI inserts every 20–60 s; dialogue on one plate with reframes/pans; v05/v09 hold 14–17 s | female system TTS + typewriter text, dark cue for the twist act, silences on verdicts |
| Addiction cycle (v10) | slowest open (8/min in 0–15 s, chapter card on black), 20 s of black chapter cards, 35 s isolation hold, last 30 s at 4/min | most silence (6 runs ≥ 1 s, 15 % of runtime without music), epic → metal → tense cues |

---

## 7. RHYTHM SPEC (reusable; for a 3:30–7:30 story)

| Segment | Target | Notes |
|---|---|---|
| 0:00–0:01.2 | fade from black (luma 0 → full in ≤ 1.2 s), optional lateral slide of a blurred foreground layer | not counted as a cut |
| 0:00–0:15 | **16–24 boundaries/min** (4–6), first cut 1.5–4.0 s; WS establish → MS → CU/insert | no dialogue before 0:03; voiced videos may stay wordless to 0:14–0:33 |
| 0:15–1:00 | **17–27/min**, median shot ≤ 2.6 s | premise delivered with pictures + ≤ 3 lines |
| Body, wordless plot / pantomime beats | 22–32/min, shots 1.8–2.7 s | |
| Body, montage (job loop, transformation) | 25–45/min, shots 1.1–2.5 s, ≥ 3 laps | music up to voice level |
| Body, dialogue beats (≥ 70 % speech) | 10–14/min, median shot 4–5 s; one plate, switch speakers with a reframe/slide every ≤ 10 s; **cap single-location dialogue at 60 s** or intercut | |
| Monologue / irony line | 1 shot 8–10 s, slow push-in to ≤ 1.15× | the only legal > 8 s holds |
| Act break | 4–6 s black (or chapter card ≤ 4 s) at 45–60 % of the story | with a sub hit + new cue |
| Last 30 s of the story | 10–20/min; end on one 6–10 s reveal/pull-back | |
| End card | 7.3 s static (range 5–15) | fixed template + fixed outro audio |
| Distribution checks | p10 1.3–1.6 s · median 2.3–3.0 · mean 2.8–3.5 · p90 5–6.5 · max ≤ 10 · ≤ 3 % of shots > 8 s · 10–15 % < 1.5 s | |
| Camera | slow push-in on ≥ 25 % of runtime; ≥ 1 reframe per 30 s; pose swaps 2–9/min for acting | |

## 8. SOUND DESIGN SPEC

| Item | Target |
|---|---|
| Loudness, voiced | **−20 ± 2 LUFS** integrated (corpus −16.6…−22.5), LRA 10–13 LU, true peak ≤ −1.0 dBTP [İYİLEŞTİRME: corpus overs up to +0.7] |
| Loudness, wordless music film | −11…−15 LUFS integrated, LRA ≈ 11 LU, ≤ −1.0 dBTP |
| Opening | first 15 s 3–10 LU below the body (short-term); bed or ambience only, then the first line |
| Dialogue level | each TTS line −15…−20 LUFS momentary, dry, no reverb, constant |
| Bed under dialogue | **8 ± 2 LU below voice** (static; corpus 2.8–11.9); no sidechain ducking; for dialogue > 60 s low-pass the bed at ≈ 1 kHz or drop it 3 dB at the scene cut |
| Bed in music-only beats | rise to voice level (−13…−17 LUFS momentary) |
| Music roles | 2–4 cues per voiced video: comedy/mischief (setup) → idyll/cool loop (rides, montages) → dark/villain (from the act break to the end); wordless: one emotional instrumental 90–130 BPM for the whole film. Original or properly licensed tracks only. |
| Cue changes | on hard cuts at location changes and act breaks; enter a dark cue on black with a sub hit (60–110 Hz, 1–1.5 s) |
| Music-off | 1–3 windows of 2–5 s per video, on decision / verdict / overlord punchline; resume with voice or a boom |
| Silence | ≤ 6 runs ≥ 1 s per video; none > 5 s inside the story except chapter cards |
| SFX | voiced 3–8 per minute, wordless 0–1; one per on-screen state change: UI click (6–7 kHz, ≤ 120 ms) per phone card, notification whoosh (≈ 4 kHz noise, 0.4 s), idea/reward chime (1.6–2.7 kHz, 0.3–0.6 s), object/costume thud (< 300 Hz, 0.1–0.5 s), sub boom for reveals; no ambience beds, no footsteps; violence elided without impact sound |
| Voices | TTS, one distinct preset per character (≥ 4 semitones apart or different accent for characters who debate); 150–205 WPM inside turns; 0.4–0.6 s gaps; system/AI = female assistant voice + typewriter text; enforcement = pitched-down monotone; accented antagonist = burned-in subtitles |
| End card | the same 7–8 s signature outro loop every video (build your own), same card |

---

## 9. QA script — `~\.claude\skills\lowbudgetstories-dna\scripts\rhythm_qa.py`

`python rhythm_qa.py VIDEO.mp4 [--transcript words.json] [--mode voiced|wordless|auto] [--out qa_out] [--hold 8] [--montage] [--no-audio] [--quiet]`

Needs ffmpeg/ffprobe, numpy, Pillow (only for `--montage`). Decodes 96×54 @ 25 fps, detects cuts / reframes / slide-pans /
dissolves / black holds (model in §0), finds the end card and computes story-only statistics: boundaries/min for 0–15 s,
15–60 s, body, last 30 s and per runtime minute, shot p10/median/mean/p90/max, holds > `--hold`, camera class per shot
(push-in/pull-out/pan/static via NCC scale search), pose swaps/min; audio: integrated LUFS, LRA, momentary percentiles,
silence map (≥ 0.4 s, M < −45 LUFS), music-off runs (stereo side < −60 dB), dramatic silences ≥ 1 s, SFX candidates,
and with a transcript: speech share, first word, longest wordless stretch, WPM inside turns, bed-below-voice LU and the
ducking test. Writes `report.json`, `shots.csv`, `seconds.csv` (per-second cut flag, momentary/short-term LUFS, mid/side
dB, silence and speech share) and `montage_cuts.jpg` (before/after frame pair for every boundary, for the human
calibration pass). Compares 22 metrics with the corpus norms above (PASS = corpus range, WARN outside it, FAIL far
outside); exit code 1 on any FAIL. Runtime ≈ 40–70 s per 3–7 min video.

Test results (final version):
- **v08** (voiced, 211 s): 66 boundaries (56 cut, 8 reframe, 1 dissolve, 1 from-black), 19.3/min (0–15 s 16 · 15–60 s 22.7 · body 19.7 · last 30 s 14), shots p10 1.14 / median 2.44 / mean 3.03 / p90 6.17 / max 9.48 s, story ends 205.5 s, I −16.6 LUFS, LRA 9.6, bed 2.8 LU, onset change −1.6 dB, speech 31.7 %, 162 WPM → **22/22 PASS, exit 0**.
- **v03** (voiced, 452 s): 160 boundaries, 21.6/min (24 · 26.7 · 21.1 · 18), median 2.28 s, max 9.6 s, I −21.9, bed 8.7 LU, 4 dramatic silences → **22/22 PASS, exit 0**.
- **v04** (wordless, 170 s): all 15 wordless checks PASS, exit 0.
- **v10** (voiced, 421 s): 5 WARN — 0–15 s at 8/min (chapter card), last 30 s at 4/min, max shot 35.1 s, 11.8 holds > 8 s per 10 min, 20.2 s of black — exactly the deviations listed in §6; exit 0.
- Synthetic negative test (90 s single still + soundtrack): 11 FAIL (0 cuts/min, 90 s shot, no end card), exit 1; a 20 s clip without audio runs with audio checks skipped.

---

## 10. Anti-patterns (measured in the weaker half of the corpus or flagged by the data)

1. Single-location dialogue > 60 s without reframes (v07 car 97.7 s at 14/min → lowest replay plateau; v05/v06/v09/v10 holds 13–35 s).
2. Opening on a black chapter card (v10: 8 boundaries/min in 0–15 s; 20 s of black overall).
3. Ending at 4 boundaries/min for 30 s before the card (v10).
4. A bed louder than 4 LU under the voice without subtitles (v08 is 2.8 LU and needs subtitles for its accented villain).
5. Overs after encoding (> 0 dBTP in 5/10).
6. Commercial songs as the score (v01/v04) — works for reach, unsafe for monetisation/claims; replace with original.
7. Look-alike TTS voices for two debaters (v07 protagonist and driver both ≈ 95 Hz).
8. Sidechain-style pumping or ambient room tone — the corpus never uses them; they would break the flat "meme comic" sound.

---

## Why it works

- The edit is a **comic-strip cadence**: a new panel every 2.3–3.6 s, with drawings reused through reframes and push-ins,
  so pictures change fast while the art budget stays low.
- Rhythm follows the ear: when TTS dialogue carries meaning the cut rate halves (12 vs 18/min), when pictures carry it the
  rate doubles — attention is never split.
- Sound is architectural, not decorative: a near-constant bed sets the mood per act, cues switch on act cuts, and the rare
  subtractions (music-off, 1.5–5 s silences) mark decisions and verdicts.
- Synthetic voices are an accepted channel convention (even a running joke) and keep production cheap and consistent.
- Replays come from reveal frames and readable text near the end, not from fast cutting — the rhythm keeps people
  watching, the reveal makes them rewind.

## Rules to copy

1. [KOPYA] Edit every story to 16–22 boundaries/min (corpus 14–24), median shot 2.3–3.0 s, p90 ≤ 6.5 s, max story shot ≤ 10 s; count reframes/slide-pans as boundaries and verify with `rhythm_qa.py --montage`.
2. [KOPYA] 0:00–0:15 at 16–24/min with the first cut by 4 s; 0:15–1:00 at ≥ 17/min; open with a ≤ 1.2 s fade from black and a soft first 15 s (3–10 LU under the body).
3. [KOPYA] Set beat cut rates by speech density: wordless plot 22–32/min, montage 25–45/min, dialogue (≥ 70 % speech) 10–14/min with a reframe every ≤ 10 s.
4. [KOPYA] Allow holds > 8 s only for monologues/irony lines (8–10 s, slow push-in); never hold an action or reaction shot > 6.5 s.
5. [KOPYA] Put the act break at 45–60 % of the story as 4–6 s of black (or a ≤ 4 s chapter card) with a sub hit and a new, darker cue.
6. [KOPYA] Place the strongest reveal — ideally with readable on-screen text — at 80–95 % of the story and follow it with one 6–10 s hold before the end card.
7. [KOPYA] Music under ≥ 85 % of the story, 2–4 cues per voiced video mapped comedy → idyll → dark; static bed 8 ± 2 LU under dialogue, no ducking; low-pass or −3 dB for dialogue scenes > 60 s.
8. [KOPYA] Remove music for 2–5 s on 1–3 decision/verdict/punchline moments; ≤ 6 true silences ≥ 1 s per video.
9. [KOPYA] SFX only for state changes (UI click, notification whoosh, idea chime, object thud, sub boom), 3–8 per minute in voiced videos, none in wordless music films; no ambience beds.
10. [KOPYA] TTS cast with one distinct preset per role, 150–205 WPM, 0.4–0.6 s gaps, dry; subtitles for accented antagonists; female assistant voice + typewriter text for any "system".
11. [KOPYA] Same orange-family end card and the same 7–8 s signature outro loop on every upload [İYİLEŞTİRME: build your own loop and card design].
12. [İYİLEŞTİRME] Master voiced videos to −20 ± 1 LUFS, LRA 10–13 LU, true peak ≤ −1.0 dBTP (corpus has overs to +0.7).
13. [İYİLEŞTİRME] Cap single-location dialogue at 60 s; avoid black chapter cards in the first 15 s.
14. [ETİK] Score with original or properly licensed music only — never the commercial songs or covers used in v01/v04, never the channel's outro loop; use original characters that fill the same roles, no real persons, brands or news mastheads in inserts.

## Open questions

- Which credited title is which cue (e.g. "Sneaky Snooper" vs "Brain Trust" in v07) needs a human listening pass; spectral mapping only gives character and placement.
- Is the fixed outro loop the credited "Milk Coffee" jazz loop or an uncredited signature?
- The views–cut-rate correlation (ρ = +0.56, n = 10) is confounded with upload year and topic; it needs the full 148-video channel to test.
- TTS vendor/voice IDs cannot be recovered from the audio; only "synthetic, preset accents" is established.
