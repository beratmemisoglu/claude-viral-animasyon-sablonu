# 04 — Edit rhythm, measured: how often the picture changes and how

Reference: AI Flow, "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)" (SRjm9tvMHhs, 22:52, 1920×1080, 29.97 fps).
Analyst #4 of 8. Everything below was measured on `raw/video.mp4`: 10 fps 256×144 grey decode (13,715 frames), the 41,103-frame scdet series, 1 fps stills, ~60 full-resolution frame grabs, stereo audio at 22.05 kHz, and the Whisper transcripts (Hindi/Urdu original plus English translation). Timestamps are mm:ss.
Working files are in `ROOT\tmp\a4\` (events_final4.json, metrics.json, timeline_1s.json, tables.md, edit_rhythm_qa.py).

---

## Summary

1. **582 visual-change events in 22:52, or 25.5 per minute.** The median gap between any two changes is **1.4 s** (mean 2.4 s). They break down as 106 instant cuts, 92 gradual full-frame changes (fades, page loads, animated UI), 105 scrolls/pans, **14 animated zoom moves** and 265 local UI changes (≥4 % of pixels). Cursor and caret movements are ignored.
2. **Shot changes (cut + gradual full-frame change): 198, or 8.7/min. Median shot 2.6 s, mean 6.9 s.** Instant cuts alone come to 4.6/min. 49 of the 106 cuts are white→white tab or page switches, with a median scdet score of only **8.9** (10th–90th percentile 5.2–14.2). The other 57 cuts have a median of 24.4.
3. **No single scdet threshold counts cuts correctly.** At ≥15 every event is a real cut or overlay, but only 36 % of cuts are found. At ≥8, 82 % are found, but half of the 190 events are not cuts (CapCut preview swaps, scrolls, UI changes). At ≥4, 97 % are found inside 362 events, of which only about 25 % are cuts. The classifier I used (scdet/frame diff to find candidates, then bbox area, NCC scale/translation search and single-step concentration) agreed with my visual check on 42 of 47 events (89 %).
4. **What is on screen (share of runtime):** full-frame screen recording 71 %, zoomed screen recording 5 % (70 s), CapCut 13 %, finished-video playback 5 %, competitor example clips 3 %, full-screen text/graphics 1.5 %, movie/meme B-roll 0.6 %, demo of a generated clip 0.4 %.
5. **The editing effort is front-loaded.** The "Important" chapter (0:00–3:12) runs 31.6 changes/min and 12.8 shot changes/min. It contains 12 of the 14 zooms and 11 of the 18 inserts. The hook shows **6 different visual sources in its first 9.2 s**: movie meme, cinematic B-roll, kinetic text, image card, screen recording, black title card. After that, 3:12–10:48 runs **7.6 minutes with no insert or graphic**. Its only camera moves are one prompt zoom (3:48–4:14), and there are no zooms at all after 4:14.
6. **Zoom language.** The 14 zooms are all between 0:16 and 4:14. All are animated with easing; none is a cut. Punch-ins go to **1.45–1.67×** (typically **1.55×**) with 0.3–0.7 s of motion. Slow pushes go to 1.12–1.32× over 1–2.7 s. Zooms are held **1.6–4.2 s** (once 20.8 s, on a ChatGPT prompt). **Every zoom is triggered by the narrator naming an on-screen number or title** ("24 videos / 46,000 subscribers", "184 videos", a title, "52 minutes").
7. **Static holds:** there are **28 holds > 8 s, totalling 376 s (27 % of runtime)**. The longest is **31.9 s** (12:34–13:06, a generated-voice sample playing over a static AI Studio page). The Voice chapter has **0 cuts in 82 s**.
8. **Audio rhythm.**
   - Narration runs at **~200 words/min** (original language) and covers 94 % of runtime. There are only 26 pauses ≥0.35 s, and the mix is −19.4 LUFS with LRA 2.8 LU.
   - The mix is essentially **mono voice**. A near-inaudible stereo music loop (period **21.8 s**, side channel about −60 dBFS) runs under it.
   - **11 loud music stings** (1–1.5 s cues, some chained to 5.6 s, momentary loudness 12–14 LU *above* the voice) sit in narration gaps exactly at "result reveal" moments.
   - No whoosh, pop or click SFX were found at cuts or overlays.
9. **Edit density is weakly negatively correlated with the most-replayed curve.** Spearman ρ is −0.11 for all changes and −0.18 for shot changes. Top-quartile replay buckets have *fewer* changes than bottom-quartile ones (5.7 vs 6.9 per 13.7 s) and more static time (41 % vs 27 %). The 1.00 peak (11:26–11:40) contains **0 shot changes**. Buckets that contain a music sting average 0.46 replay vs 0.21 for the rest.
10. **The intro recycles B-roll.** The same channel-browsing takes are reused 2–3 times under the narration. For example, 2:04.6, 2:28.6 and 3:24.6 are pixel-identical (cursor included), and 1:04 matches 2:43. That is about 20–25 s of repeats in the first 3.5 min, plus 1:28–1:40 reused at 21:18–21:31.

---

## Method & thresholds

### Pipeline
1. **Decode:** `ffmpeg -i video.mp4 -vf "fps=10,scale=256:144:flags=area,format=gray" -f rawvideo` produced 13,715 frames.
2. **Activity:** for each 0.1 s step I computed the mean absolute difference (MAD) and the fraction of pixels changing by more than 24 grey levels (`frac`). A step is *active* if frac > 2 % or MAD > 2. Consecutive active steps, bridging 1-frame gaps, form one **event**. There were 726 raw events.
3. **Motion model per event**, comparing the frame before the event with the frame after it:
   - *zero-mean NCC* template search of the 70 % centre crop at scales 1.0–2.3× in both directions, giving the zoom factor;
   - the scale-1 shift, giving scroll or pan;
   - a per-step model (scales 1.0–1.3, crop 60 %) to catch smooth zooms and long scrolls;
   - the changed-pixel bounding-box area;
   - the luminance jump;
   - single-step concentration, i.e. the share of the event's change that happens inside one 0.1 s step. I also cross-checked the per-frame scdet peak.
4. **Rules:**
   - **micro:** <4 % of pixels changed (cursor, caret).
   - **zoom:** best NCC ≥0.75 at scale ≠1, at least 0.15 better than identity and than a pure shift, and luminance jump <15. Alternatively, ≥2 per-step zoom steps.
   - **scroll/pan:** ≥50 % of steps are pure translations.
   - **full-frame change:** changed area ≥20 % with bbox ≥35 %, or bbox ≥60 % with NCC to the previous frame <0.85. It counts as a **cut** if it happens within ≤0.3 s with concentration ≥0.6; otherwise it is a **gradual change**.
   - **local:** everything else.
5. **Manual layer:** non-screen inserts (B-roll, text/graphic cards, subscribe animation, example clips, demo, CapCut, finished video) were labelled from contact sheets and frame grabs. Each boundary was snapped to its detected event.
6. **Absolute zoom state per second:** a template of Chrome's bookmarks bar, taken from the 0:15 frame, was matched in each 1 fps frame. NCC ≥0.9 at scale 1.0 and y = 22 px means the frame is full-frame. In screen-recording seconds anything else means zoomed. 1,011 of 1,371 s matched as full-frame.

### Calibration: 47 events checked by eye (frame triplets before, mid and after at 400–960 px)

| Time | scdet peak | Auto class | Visual verdict |
|---|---|---|---|
| 00:01.0 | 62 | gradual | hook: Panda clip → screen wall → "RPM" text (compound) ✔ |
| 00:04.8 | 2.5 | gradual | image card (brain illustration) fades/scales in on grey ✔ |
| 00:06.9 / 00:07.8 / 00:09.1 | 24 / 71 / 69 | cut | card → YouTube → black "Finance Niche" card → YouTube ✔ |
| 00:12.3 | 15 | cut | tab switch Nick Invests → Legend Investor Mindset ✔ |
| 00:16.5 / 00:20.2 | 4.1 / 3.8 | zoom in / out | eased punch-in 1.55× on channel header, back out ✔ |
| 00:24.1 | 4.0 | scroll | page scroll ✔ |
| 00:30.6 | 8.9 | local | thumbnail grid fades after a "Popular" click ✔ |
| 00:33.1 | 0.4 | zoom in | slow 1.12× push ✔ |
| 00:41.6 | 4.2 | gradual | sort click with re-layout ✔ |
| 00:44.8 | 9.9 | scroll | ✔ |
| 00:53.0 / 01:17.7 | 51 / 26 | cut | to Buffett video playing / back to channel page ✔ |
| 01:11.6 | 5.8 | gradual | jump-scroll to comments (borderline) ~ |
| 01:50.8 | 7.0 | zoom in | 1.55× punch-in + pan, red box appears ✔ |
| 03:03.6 / 03:06.8 | 44 / 39 | gradual / cut | subscribe animation in / out ✔ |
| 03:09.6 / 03:11.5 | 47 / 52 | cut | "100K Subscribers" card in / out ✔ |
| 03:48.7 / 04:11.4 | 0.6 / 0.3 | zoom in / out | slow 1.67× zoom into ChatGPT prompt and back ✔ |
| 04:36.6 / 04:42.1 | 5.6 / 8.4 | cut | ChatGPT ↔ YouTube tab switches (white→white) ✔ |
| 05:37.4 / 05:38.3 | 16 / 10 | cut | ChatGPT → Whisk landing → Whisk app ✔ |
| 06:04.9 / 06:06.1 / 06:17.0 / 06:33.4 | 15 / 14 / 11 / 11 | cut | ChatGPT ↔ Whisk tab switches ✔ |
| 06:39.8 | 14 | cut | Whisk lightbox opens (0.2 s fade, UI) ~ |
| 06:49.6 | 12 | cut | Whisk → YouTube (Nick Invests) ✔ |
| 07:16.7 / 08:51.0 | 0.9 / 1.2 | local | ChatGPT answer grows / list scroll in the answer pane (scroll mislabelled local) ✔/✗ |
| 08:10.7 / 13:53.0 / 15:58.9 | 2.1 / 1.3 / 4.0 | scroll | ✔ |
| 09:12.2 | 6.8 | zoom in → **corrected to scroll** | ✗ (auto) |
| 14:33.8 / 14:53.8 | 29 / 8.2 | cut | lightbox close / Whisk → ChatGPT ✔ |
| 14:35.0 | 4.3 | zoom out → **corrected to local** | Whisk side panel slides open ✗ (auto) |
| 14:56.0 / 20:02.9 | 4.2 / 2.5 | gradual | Whisk generating → placeholders → results ✔ |
| 19:50.5 | 3.8 | local | Docs → ChatGPT tab switch, a missed cut ✗ |
| 20:13.5 | 3.4 | gradual | Whisk results scrolled (scroll mislabelled) ~ |
| 20:37.1 | 6.2 | cut | jump-scroll in Whisk ✔ |

The two zoom false positives were corrected in all tables below. Expect cuts to be **under-counted by about 5–10 %**: white-on-white tab switches with similar layouts can fall below the full-frame test.

### Why the given `cuts.csv` (scdet ≥8) is not a cut list for this video

| scdet threshold (gap 0.25 s) | Events | Real cuts or overlay in/out | Gradual full-frame | Scroll | Local UI | Inside CapCut preview | Recall of my 106 cuts |
|---|---|---|---|---|---|---|---|
| ≥4 | 362 | 106 | 118 | 57 | 59 | 62 | 97 % |
| ≥8 | 190 | 89 | 44 | 15 | 35 | 56 | 82 % |
| ≥10 | 129 | 63 | 29 | 3 | 27 | 55 | 58 % |
| ≥15 | 46 | 40 | 6 | 0 | 0 | 5 | 36 % |

Why the scores mislead:
- A white page replaced by another white page scores only 5–15.
- Dark↔light swaps (CapCut, black cards, dimmed overlays) score 25–73.
- Images being swapped inside CapCut's small preview window score about 11 every 0.3–2 s (16:42–17:56) without any editor cut.
- Zoom moves never exceed 10.4 because the change is spread over 3–20 frames.

**Recommended rule:** use scdet ≥4 (or 10 fps frac >2 %) only to generate candidates, then classify them. Use ≥15 only as a high-precision "big visual jump" counter.

---

## Per-chapter table

"Grad." means a gradual full-frame change. "Inserts" counts non-screen inserts (B-roll, graphics, examples, demo, finished video). When a chapter has no shot change, its "shot length" is the chapter length. WPM is words/min of the original-language transcript. "Heat" is the mean most-replayed value.

| Chapter | Span | Changes | Cut | Grad. | Zoom | Scroll | Local | Inserts | Changes/min | Cuts/min | Shot chg/min | Mean / med shot (s) | Mean / med gap any change (s) | Holds >8 s (n / s) | Shot-type share | WPM | Heat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Important | 0:00-3:12 | 101 | 18 | 23 | 12 | 25 | 23 | 11 | 31.6 | 5.6 | 12.8 | 4.7 / 2.6 | 1.9 / 1.3 | 2 / 17 | SR-full 58%, SR-zoom 21%, Example 10%, B-roll 4%, Text/GFX 6% | 194 | 0.10 |
| Channel Setup | 3:12-6:41 | 92 | 14 | 11 | 2 | 30 | 35 | 0 | 26.4 | 4.0 | 7.2 | 8.0 / 2.8 | 2.2 / 1.3 | 5 / 70 | SR-full 88%, SR-zoom 12% | 212 | 0.23 |
| Video topics | 6:41-9:25 | 43 | 5 | 3 | 0 | 15 | 20 | 0 | 15.7 | 1.8 | 2.9 | 18.2 / 4.9 | 3.7 / 2.5 | 5 / 60 | SR-full 100% | 205 | 0.23 |
| Script | 9:25-11:38 | 37 | 2 | 0 | 0 | 2 | 33 | 2 | 16.7 | 0.9 | 0.9 | 44.3 / 46.4 | 3.5 / 1.7 | 5 / 69 | SR-full 95%, SR-zoom 2%, Text/GFX 3% | 216 | 0.37 |
| Voice | 11:38-13:00 | 11 | 0 | 0 | 0 | 0 | 11 | 0 | 8.0 | 0.0 | 0.0 | 82.0 / 82.0 | 6.8 / 4.2 | 5 / 67 | SR-full 100% | 221 | 0.47 |
| Visuals | 13:00-15:10 | 65 | 22 | 9 | 0 | 17 | 17 | 1 | 30.0 | 10.2 | 14.3 | 4.1 / 1.5 | 2.0 / 1.1 | 2 / 24 | SR-full 87%, Example 13% | 172 | 0.37 |
| Videos | 15:10-15:55 | 25 | 9 | 5 | 0 | 2 | 9 | 1 | 33.3 | 12.0 | 18.7 | 3.2 / 2.2 | 1.8 / 1.2 | 0 / 0 | SR-full 82%, SR-zoom 4%, Demo 13% | 179 | 0.55 |
| Editing | 15:55-19:30 | 100 | 23 | 16 | 0 | 7 | 54 | 1 | 27.9 | 6.4 | 10.9 | 5.4 / 2.3 | 2.1 / 1.3 | 3 / 53 | SR-full 13%, CapCut 86%, Final vid 1% | 211 | 0.16 |
| Thumbnail | 19:30-20:38 | 43 | 7 | 13 | 0 | 2 | 21 | 0 | 37.9 | 6.2 | 17.6 | 3.2 / 1.9 | 1.5 / 1.0 | 0 / 0 | SR-full 90%, Final vid 10% | 197 | 0.18 |
| SEO | 20:38-21:50 | 39 | 5 | 7 | 0 | 4 | 23 | 1 | 32.5 | 4.2 | 10.0 | 5.5 / 2.8 | 1.8 / 1.0 | 0 / 0 | SR-full 93%, Text/GFX 7% | 212 | 0.12 |
| Final Video | 21:50-22:51 | 26 | 1 | 5 | 0 | 1 | 19 | 1 | 25.4 | 1.0 | 5.9 | 8.8 / 8.3 | 2.3 / 1.9 | 1 / 10 | SR-full 5%, Final vid 95% | 125 | 0.07 |
| **Total** | 0:00-22:52 | 582 | 106 | 92 | 14 | 105 | 265 | 18 | 25.5 | 4.6 | 8.7 | 6.9 / 2.6 | 2.4 / 1.4 | 28 / 376 | SR-full 71%, SR-zoom 5%, Example 3%, B-roll 1%, Text/GFX 2%, Demo 0.4%, CapCut 13%, Final vid 5% | 200 | 0.24 |

Reading it:
- **Two dense zones:** the opening proof (0:00–4:15) and the image/video/thumbnail workflow (13:00–15:55 and 19:30–20:38). There, frequent tab switches (ChatGPT ↔ Whisk ↔ Grok) produce 10–12 cuts/min.
- **Two near-static zones:** Video topics → Script → Voice (6:41–13:00, 0–3 shot changes/min). There the screen is a ChatGPT, Claude, Google Docs or AI Studio page being read aloud.

---

## Per-minute table (minutes 0–22)

Hold durations are clipped at the minute boundary; true durations are in the list that follows.

| Min | Chapter(s) | Changes | Cut | Grad. | Zoom | Scroll | Local | Shot chg/min | Mean / med shot (s) | Holds >8 s (start, s) | Shot-type share | WPM | Heat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Important | 24 | 6 | 5 | 3 | 3 | 7 | 11 | 5.5 / 3.2 | - | SR-full 60%, SR-zoom 25%, Example 2%, B-roll 5%, Text/GFX 8% | 201 | 0.04 |
| 1 | Important | 33 | 3 | 8 | 6 | 3 | 13 | 11 | 5.0 / 2.5 | 1:40 (9) | SR-full 73%, SR-zoom 23%, Example 3% | 207 | 0.08 |
| 2 | Important | 36 | 4 | 9 | 3 | 17 | 3 | 13 | 4.3 / 2.5 | - | SR-full 50%, SR-zoom 18%, Example 23%, B-roll 8% | 168 | 0.14 |
| 3 | Important / Channel Setup | 31 | 5 | 6 | 1 | 13 | 6 | 11 | 5.0 / 2.9 | 3:48 (11) | SR-full 65%, SR-zoom 18%, Example 5%, Text/GFX 12% | 221 | 0.24 |
| 4 | Channel Setup | 29 | 6 | 4 | 1 | 9 | 9 | 10 | 5.5 / 2.4 | 4:22 (14) | SR-full 77%, SR-zoom 23% | 173 | 0.19 |
| 5 | Channel Setup | 17 | 2 | 0 | 0 | 5 | 10 | 2 | 20.0 / 21.7 | 5:17 (10), 5:38 (20) | SR-full 100% | 240 | 0.28 |
| 6 | Channel Setup / Video topics | 29 | 8 | 3 | 0 | 8 | 10 | 11 | 5.0 / 4.4 | 6:17 (10) | SR-full 100% | 207 | 0.29 |
| 7 | Video topics | 16 | 1 | 0 | 0 | 3 | 12 | 1 | 30.0 / 30.0 | 7:03 (9), 7:23 (8), 7:51 (9) | SR-full 100% | 207 | 0.28 |
| 8 | Video topics | 10 | 0 | 0 | 0 | 4 | 6 | 0 | 60.0 / 60.0 | 8:00 (11), 8:37 (11) | SR-full 100% | 200 | 0.17 |
| 9 | Video topics / Script | 22 | 2 | 2 | 0 | 6 | 12 | 4 | 12.0 / 4.9 | 9:45 (9) | SR-full 98%, SR-zoom 2% | 213 | 0.26 |
| 10 | Script | 12 | 2 | 0 | 0 | 0 | 10 | 2 | 20.0 / 8.4 | 10:00 (14), 10:25 (17) | SR-full 90%, SR-zoom 3%, Text/GFX 7% | 230 | 0.30 |
| 11 | Script / Voice | 20 | 0 | 0 | 0 | 1 | 19 | 0 | 60.0 / 60.0 | 11:00 (17), 11:16 (8), 11:48 (8) | SR-full 100% | 212 | 0.55 |
| 12 | Voice | 5 | 0 | 0 | 0 | 0 | 5 | 0 | 60.0 / 60.0 | 12:00 (10), 12:10 (8), 12:23 (10), 12:34 (26→32) | SR-full 100% | 217 | 0.43 |
| 13 | Visuals | 27 | 6 | 4 | 0 | 7 | 10 | 10 | 5.5 / 1.5 | 13:31 (16) | SR-full 72%, Example 28% | 214 | 0.43 |
| 14 | Visuals | 30 | 10 | 4 | 0 | 10 | 6 | 14 | 4.0 / 2.2 | 14:40 (8) | SR-full 100% | 140 | 0.31 |
| 15 | Visuals / Videos / Editing | 39 | 18 | 7 | 0 | 4 | 10 | 25 | 2.4 / 1.5 | - | SR-full 87%, SR-zoom 3%, Demo 10% | 171 | 0.55 |
| 16 | Editing | 23 | 7 | 6 | 0 | 1 | 9 | 13 | 4.3 / 1.3 | 16:13 (26) | SR-full 10%, CapCut 90% | 218 | 0.14 |
| 17 | Editing | 44 | 9 | 6 | 0 | 0 | 29 | 15 | 3.8 / 2.3 | - | CapCut 100% | 219 | 0.06 |
| 18 | Editing | 17 | 2 | 1 | 0 | 1 | 13 | 3 | 15.0 / 13.3 | 18:27 (14) | CapCut 100% | 187 | 0.28 |
| 19 | Editing / Thumbnail | 26 | 3 | 3 | 0 | 4 | 16 | 6 | 8.6 / 6.0 | 19:00 (10) | SR-full 68%, CapCut 17%, Final vid 15% | 218 | 0.21 |
| 20 | Thumbnail / SEO | 44 | 6 | 17 | 0 | 1 | 20 | 23 | 2.5 / 1.7 | - | SR-full 100% | 193 | 0.15 |
| 21 | SEO / Final Video | 29 | 5 | 4 | 0 | 5 | 15 | 9 | 6.0 / 4.9 | - | SR-full 80%, Text/GFX 8%, Final vid 12% | 186 | 0.13 |
| 22 | Final Video | 19 | 1 | 3 | 0 | 0 | 15 | 5 | 10.3 / 9.8 | 22:14 (10) | Final vid 100% | 142 | 0.04 |

### Longest static holds (> 8 s with no change ≥4 % of pixels), true durations

| Hold | Dur | On screen | What the narration does |
|---|---|---|---|
| 12:34–13:06 | 31.9 s | Google AI Studio TTS page, full frame | plays the generated voice sample, then announces the Visuals step |
| 16:13–16:39 | 25.6 s | CapCut with an empty, black preview | explains trimming long silences out of the voice track |
| 05:38–05:59 | 20.4 s | Whisk prompt page (cursor only) | explains pasting the logo prompt and choosing a square size |
| 07:51–08:11 | 19.4 s | ChatGPT topic list | explains picking a video category first ("financial trap") |
| 10:59–11:17 | 17.7 s | Claude artifact with the finished script | asks the viewer to read the script and notes its question hook |
| 10:25–10:42 | 16.9 s | Claude prompt | explains the script-length settings |
| 09:58–10:14 | 16.6 s | ChatGPT prompt | prompt rules, then switches to Claude |
| 03:49–04:05 | 15.8 s | ChatGPT prompt, **zoomed 1.67×** | how many names to request |
| 13:31–13:47 | 15.7 s | ChatGPT image-prompt request | where to paste the script |
| 18:28–18:42 | 14.3 s | CapCut timeline | "keep the editing slow-paced" advice |
| 04:22–04:37 | 14.1 s | ChatGPT name list | names are grouped in three categories |
| 11:56–12:10 | 13.9 s | AI Studio, empty box | paste the script, split long scripts |
| 18:56–19:10 | 13.5 s | CapCut export dialog | reassurance about the finance niche |
| 8 more holds of 8–12.6 s | | prompts and lists | |

**Pattern:** **every long hold is a text-heavy instruction screen** (a prompt, list, script, settings page or empty preview) while the narrator explains what to type or select. **None** happens on a "proof", example or result screen; those always change within 1–4 s.

---

## Zoom language

### Measured zoom moves (all confirmed on 10 fps strips)

| # | Time | Direction / factor | Active motion | Ease profile (cumulative share of the move per 0.1 s) | Hold until next move | Trigger in narration (paraphrased) |
|---|---|---|---|---|---|---|
| 1 | 00:16.5 | in **1.55×** (header, top-left anchor) | 0.4 s | 0 → .15 → .67 → .92 → 1 (S-curve, ease-in-out) | 3.1 s | quotes "24 videos" and "46K subscribers" |
| 2 | 00:20.2 | out to 100 % | 0.3 s | 0 → .27 → .84 → 1 | – | next sentence ("and guess what?") |
| 3 | 00:33.1 | slow push **1.12×** | ~1.6 s | linear drift | ~8 s (until page change at 0:41.6) | "first video only two months ago" |
| 4 | 01:21.6 | in **1.55×** (Nick Invests header) | 0.4 s | 0 → .15 → .85 → 1 | 3.9 s | quotes "184 videos", then the subscriber count |
| 5 | 01:26.1 | out | 0.5 s | 0 → .32 → .84 → 1 | – | new sentence |
| 6 | 01:34.8 | slow **1.28×** | ~0.7 s inside a 1.8 s event | .13/.37/.62/.75/.87/1 (ease-out) | 1.6 s | "popular video, 5 months old" |
| 7 | 01:38.2 | out (0.78) | 0.4 s | .33/.66/.83/1 | – | "almost 1 million views" |
| 8 | 01:50.8 | in **1.55×** + pan, then **red box** 1:52–1:55 | 0.7 s | .14 steps (ease-in-out) | 4.2 s | "look at the title of these videos" |
| 9 | 01:55.8 | out | 0.4 s | .14/.37/.59/.93/1 | – | reaction to the title |
| 10 | 02:07.5 | slow **1.16×** | 0.5 s | .2 steps | ~7 s (cut to WWE meme) | "that's why these go viral" |
| 11 | 02:19.9 | in **1.32×** + **red box** 2:21–2:22 | 0.3 s | .21/.55/.89/1 | 3.0 s | "look at the length: 52 min, 44 min" |
| 12 | 02:22.9 | out (0.72) | ~1.2 s | linear | – | "longer video = more ads" |
| 13 | 03:48.7 | in **1.67×** on ChatGPT prompt box | ~1.4 s (3:49.0–3:50.4) | slow ease-in-out | **20.8 s** | "choose how many channel names you want" |
| 14 | 04:11.4 | slow out (0.60) | ~1.6 s | linear (.08 steps) | – | "nothing else to change in the prompt" |

### Rules distilled
- **Factor:** punch-ins land on **1.5–1.67×** (5 of 8 zoom-ins). "Gentle push" zooms are 1.12–1.32×. Every zoom-out returns to exactly 100 %; there is no zoom-out below full frame.
- **Motion:** always animated, never a hard cut to a cropped frame. Punch moves take **0.3–0.7 s with an S-curve.** About 15 % of the move happens in the first 0.1 s, about 70 % by the midpoint, and the last 0.2 s settles. Slow pushes take 1–2.7 s with linear or ease-out curves. Zoom and pan happen together, so the camera glides to the target. This looks like CapCut keyframe zooms, or Screen-Studio-style auto-zoom, on the recording.
- **Hold:** typically **3–4 s**, i.e. exactly one spoken sentence. The longest is 20.8 s, while a prompt field is explained.
- **Frequency:** 14 moves in total, **3.7 per minute during 0:00–4:15** and **0 per minute after 4:15**. That is about 70 s zoomed in total (5 % of runtime). The tutorial body is shown at native full-frame scale; Chrome's tab and bookmark bars stay visible 74 % of the time.
- **Trigger:** the zoom-in starts 0–1 s after the narrator *names* a number, title or field that is on screen. The zoom-out starts with the next sentence.
- **Callouts:** there are only **2 red rectangle boxes**, and both are combined with a zoom: around a video card at 1:52–1:55 and around a 44-min video card at 2:21–2:22. They are thin (about 2 px at 960 w) and pure red (≈#FF0000).
- **Cursor and highlighting:** the cursor is the plain system cursor; it is not enlarged and has no click ripple. The narrator highlights by selecting text natively, e.g. selecting "Legend Investor Mindset" at 0:15 and "24 videos" at 0:18. No arrows, underlines or spotlight masks were found (low confidence for non-red colours).

---

## Overlay / graphic inserts

| # | Time | Dur | Type | Look (measured) | Trigger / narration | Audio |
|---|---|---|---|---|---|---|
| 1 | 00:00.0–00:01.9 | 1.9 s | movie meme (animated panda close-up, letterboxed) | full frame | opening question line starts at frame 0 | voice only (clip muted) |
| 2 | 00:01.9–00:03.3 | 1.4 s | cinematic B-roll (red wall of screens, figure) | full frame | "which niche always has high RPM" | voice |
| 3 | 00:03.3–00:04.8 | 1.5 s | **kinetic text** "RPM … HIGH rehta hai" with words revealed one by one | dark sans on light grey gradient (#E0E0E0–#F8F8F8) | same sentence | voice |
| 4 | 00:04.8–00:07.0 | 2.2 s | **image card** (brain illustration in a drop-shadow card) that fades and scales in | card on grey | "you're right" beat | voice |
| 5 | 00:08.0–00:09.2 | 1.2 s | **title card** "Finance Niche" | white bold, slight tilt, pure black background | names the niche | voice |
| 6 | 00:53.0–00:54.4, 01:08.5–01:09.7 | 1.4 / 1.2 s | competitor video playing (Buffett-style) | screen recording of the YouTube player | earnings maths / "open any video" | muted, voice over |
| 7 | 01:52–01:55, 02:21–02:22 | 3 / 1.5 s | red box callouts with zoom | see zoom table | title / video length | voice |
| 8 | 02:15.0–02:19.6 | 4.6 s | **WWE "money" meme clip** | full frame | the narrator says the reason is money; the clip's own famous theme line plays | **clip audio on** (stereo, side −16 dB) |
| 9 | 02:46.4–03:03.1 | 16.7 s | **competitor example clip** (cartoon finance video): YouTube player, then framed on black, then player | captions burned in | narrator stops; ~10 s of the clip's own narration plays | **clip audio on** |
| 10 | 03:03.6–03:07.4 | 3.8 s | **subscribe animation**: page dims to ~20 % luminance with vignette, a white card expands into a red (#FF0000) SUBSCRIBE button, the cursor clicks, it becomes grey SUBSCRIBED | animated overlay | own channel shown, then the CTA | voice |
| 11 | 03:09.6–03:11.9 | 2.3 s | **"100K Subscribers"** neon-green (#3AFC00) bold text with dark outline over dimmed page (mean luminance 40/255) | instant in/out | subscriber-target talk | voice |
| 12 | 10:48.5–10:52.1 | 3.6 s | subscribe animation (same template) | – | "press subscribe while the script is being written", i.e. placed in *waiting time* | voice |
| 13 | 10:53.2–10:55.1 | 1.9 s | **meme sticker**: a hand with a pistol pops in over the Claude page | cut-out PNG, center-right | joke line "nobody is forcing you" | voice |
| 14 | 13:08.2–13:25.1 | 16.9 s | competitor example clip in the YouTube player | – | narrator explains the competitor's images and animation | muted, voice over |
| 15 | 15:39.2–15:44.9 | 5.7 s | **demo of own generated clip** (Grok output, framed on black) | – | payoff of the image-to-video step | **own audio on** (−17 dB side) |
| 16 | 19:27.9–19:36.6 | 8.7 s | **finished-video teaser** (vignette, burned captions) | – | "our video is ready" | its own voice |
| 17 | 21:42.4–21:47.3 | 4.9 s | **"200 Likes"** neon-green text over dimmed page | – | like-target CTA | voice |
| 18 | 21:52.7–22:51 | 58.9 s | **finished video** playback | image swap about every 8.3 s (7 swaps), word-by-word captions, vignette, 2 hard wipes/cuts at 22:25.9 and 22:35.7 | – | its own voice |

**Cadence:**
- 0:00–3:12 has 11 inserts, about 1 every 17 s.
- 3:12–21:50 has 7 inserts, about 1 every 2.7 min.
- The longest stretch without an insert is **3:12 → 10:48 (7.6 min)**.
- The tutorial body's visual variety comes from **switching apps** (YouTube → ChatGPT → Docs → Whisk → Claude → AI Studio → Grok → CapCut), which changes the dominant colour scheme roughly every 1–3 min: white, yellow Whisk sidebar, dark CapCut.

**Recycled B-roll in the intro:** 2:04.6 = 2:28.6 = 3:24.6, 2:25.0 = 3:21.0, and 1:04 = 2:43 are pixel-identical frames with the cursor in the same place. The editor loops a handful of 2–7 s channel-scroll takes under 3 minutes of continuous talking. In the SEO chapter, 1:28–1:40 is reused at 21:18–21:31.

---

## Audio rhythm

| Measure | Value | Confidence |
|---|---|---|
| Integrated loudness / LRA | −19.4 LUFS / 2.8 LU (heavily compressed voice) | high (given) |
| Narration density | 4,564 words (original Hindi/Urdu ASR) = **200 wpm**; speech segments cover 1,293 of 1,372 s (94 %); only 13 inter-word gaps > 1 s | high |
| Pauses ≥0.35 s below −35 dB | 26: 12 inside the final-video playback and 3 inside inserted clips (2:54, 15:41, 15:44), which leaves **only 11 narrator pauses in 21:50 of tutorial (≈1 every 2 min)** | high |
| Pause floor | −47 to −66 dBFS RMS (not digital silence), so there is room tone or a faint bed | high |
| Stereo image | L−R is digitally zero in ~75–85 % of 100 ms windows, so **the voice is mono** | high |
| Background music | a faint **stereo tonal element recurs every 21.815 s (±0.16 s, 52 occurrences, 0:28–19:45)**: harmonic partials at ~450 Hz and 1.2–1.5 kHz in the side channel at about −60 dBFS. The phase-locked period across cuts implies a continuous **looped music bed on its own track**, mixed so low (I estimate ≤ −45 dBFS, ≥25 dB under the voice) that it is effectively inaudible. A continuous stereo bed (−55…−67 dBFS side) runs 20:00–21:43. | medium (period: high; audibility: low) |
| **Music stings** | **11 short loud music cues**, all in narration gaps right before or after a result is revealed: 4:16, 6:08, 6:35, 11:33, 12:19, 14:28, 15:05–15:11, 15:33–15:39, 18:07–18:10, 18:22, 20:04–20:07. Each is a 1–1.5 s harmonic music cue with a loud onset; several chain into 3–5.6 s runs (15:05–15:11, 15:33–15:39, 18:07–18:10). All 11 show stacked horizontal partials in the spectrogram, so they are not speech. Momentary loudness **−5.8 to −8.7 LUFS vs speech −19…−23 LUFS, i.e. +12–14 LU**. The narrator then typically says "now look…". Quieter cues below the +12 dB detection threshold may exist and are not counted. | high (detection), medium (that it is a stock sting rather than a meme sound) |
| SFX at cuts/overlays | none detected. Around the subscribe animations, the 100K/200 Likes cards, the sticker and every hard cut, the 0.5 s level changes by ≤ ±2.5 dB and the side channel shows no transient. **No whoosh, pop or click.** | medium |
| Clip audio | the WWE meme (2:15), the competitor example (2:49–3:03), the own Grok demo (15:39) and the finished video (19:28, 21:53) play **their own audio**; the other examples are muted under the voice | high |

**Reading:** the audio pace is set by **one dense, compressed, nearly gapless voice** (the editor removes or never leaves pauses; the narrator himself advises cutting long silences at 16:13). There is no music-driven rhythm. The only musical punctuation is the reveal sting: a loud 1–5 s cue that fills the silent moment while a tool finishes generating.

---

## Retention correlation (most-replayed heatmap, 100 buckets × 13.72 s)

| Test | Result |
|---|---|
| Spearman ρ, replay vs all visual changes per bucket | **−0.11** (−0.13 without the first 3 buckets) |
| ρ, replay vs shot changes (cut + gradual) | **−0.18** (−0.23) |
| ρ, replay vs static share (time in gaps > 5 s) | +0.13 (+0.09) |
| Top-quartile vs bottom-quartile replay buckets | 5.7 vs 6.9 changes, 1.7 vs 2.4 shot changes, 41 % vs 27 % static |
| Buckets with a music sting (n = 11) | mean replay **0.46** vs 0.21 for buckets without (2.2×) |
| Buckets with inserts (graphics, memes, examples) | 0.19, *below* average |

What sits under the peaks:
- **11:26–11:40 (1.00)** shows a Google Doc of the full, cleaned example script being scrolled, with **0 shot changes and 13 local changes**. A **music sting (11:33)** fills the gap after the cleanup, and the narrator says the clean script is ready. **11:40–12:35 (0.45–0.70)** is the static AI Studio set-up: single-speaker mode, paste script, style instructions, speaker "Charon", with **four holds of 8–14 s and zero cuts**. A sting sits at 12:19. Viewers are seeking back to **copy settings and read the script**. Comments agree: 26 of 133 mention the PDF and 21 the prompts; nobody mentions music or editing pace.
- **15:19–15:47 (0.70–0.85)** shows Grok: upload image → paste the same prompt → generate. A **5.5 s sting at 15:33–15:39** is followed by the **5.7 s payoff demo**, in which the static character becomes a talking clip with its own voice. This is the densest stretch of the tutorial body (25 shot changes/min in minute 15).
- **13:16–13:57 (0.42–0.50)** is the end of the competitor example clip, then the image-prompt request.
- **18:04–18:18 (0.53)** is CapCut, where the narrator recommends simple zoom-in/zoom-out animations and auto captions; stings at 18:07–18:10.
- **7:05–7:19 (0.45)** shows the topic-generation prompt in Docs (static).

**Conclusion:** replays are driven by **information you need to copy or verify** (prompts, settings, finished script, payoff demo), not by cutting speed. Faster cutting does not raise replays; if anything the rewatched sections are the *static* ones. Edit density matters where the replay curve cannot see it: the 0:00–3:12 proof section, which has very low replay (0.10) but is where first-time viewers decide to stay. That is the only place the editor spent real effort (zooms, inserts, memes, text cards). Low-confidence point: the "most replayed" curve is not the retention curve, so I cannot measure drop-off here.

---

## Edit tempo spec (for a CapCut/Premiere editor or a Remotion/ffmpeg pipeline)

"Reference" is what the AI Flow video measured. "Target" is what we should ship. Where the reference was sloppy (32 s holds, 7.6 min with no insert) the target is tightened, but only in ways that do not fight the "real-time tutorial" feel that drove the replays.

| Segment | Reference (measured) | Target for our videos | Implementation hint |
|---|---|---|---|
| **Hook 0:00–0:10** | 6 visual sources in 9.2 s; changes at 1.9 / 3.3 / 4.8 / 7.0 / 8.0 / 9.2 s; first real screen proof at 0:07 | 5–7 changes in the first 10 s (one every 1.2–2 s); ≥3 source types (meme/B-roll, kinetic text, black title card, screen proof); show proof by ≤0:08 | Remotion `<Sequence>`s of 30–60 frames; kinetic text reveals word by word at 6–8 frames/word |
| **Proof section (≈0:10–3:00)** | 31.6 changes/min, 12.8 shot chg/min, median shot 2.6 s; 3.7 zooms/min; 1 insert / 17 s | 25–35 changes/min; 1 animated zoom per quoted number (2–4/min); 1 insert (meme, example clip, graphic card) every 15–30 s; one 10–17 s example clip *with its own audio* before 3:00 | zoom keyframes: 100→155 %, 12–20 frames, ease-in-out; hold 90–120 frames; out 9–15 frames |
| **Tutorial step (screen recording)** | 16–38 changes/min, 0–12 cuts/min, median gap between any change 1.0–4.2 s; zero zooms after 4:15; holds up to 32 s | **20–30 changes/min; never a static hold > 15 s** (break it with a zoom/scroll/highlight); a punch-in (1.4–1.7×) on every field the viewer must type into or copy; full frame otherwise (≥70 % of time) | auto-zoom on click coordinates (Screen-Studio style) or CapCut keyframes; detect holds > 12 s with the QA script and insert a 1.3× push |
| **Instruction screens to copy (prompt, settings, script)** | static 8–20 s holds; highest replay of the whole video | **allowed** to hold 8–15 s, but zoom so the text is readable on mobile (≥1.5× if body text < 14 px at 1080p) and say the exact field name | hold = narration sentence length; do not cut away mid-sentence |
| **Waiting / generation time** | subscribe animation dropped in (10:48); loud music sting in pauses (11×) | place a CTA or a 1–2 s sting in every wait > 3 s; speed-ramp the wait (×4–×8) instead of holding it | sting ≤ +6 LU over voice (the reference's +12–14 LU is harsh); fade 50 ms in, 200 ms out |
| **Result reveal** | sting, then "now look…", result on screen 2–5 s, often lightbox | always: 0.3–0.5 s silence or sting → punch-in 1.3–1.6× on the result → hold 2–4 s | |
| **CTA overlays** | 2 subscribe animations (3:03, 10:48; 3.6–3.9 s; background dimmed to ~20 % luminance); 2 neon-green target cards (#3AFC00, 2.3–4.9 s) at 3:09 and 21:43 | 1 animated CTA every 6–8 min, always over a waiting or low-information moment; never over a prompt the viewer is copying | dim layer: black at 75–80 % opacity + vignette |
| **Full-screen text / title cards** | 3 in the first 9 s, then only CTA cards | 1 big text card per new section header (chapter start) plus the hook ones; 0.8–1.5 s | white on black, or black on #EEE, bold sans |
| **Meme / B-roll inserts** | 3 (0:00, 0:02, 2:15) + 1 sticker (10:53), each on a literal keyword ("money", "no force") | 1 per 2–3 min in long tutorials, always on a literal keyword, ≤ 2–5 s, own audio only if iconic | |
| **Example / demo clips** | 3 competitor clips (1.2–17 s), 1 own demo 5.7 s, finished-video teaser 8.7 s at 19:28, full final video 59 s at the end | show the finished product within the first 3 min (≤15 s) **and** before the final section; a 4–8 s demo after every generation step | |
| **Finished cartoon video (the product itself)** | image swap every ~8.3 s (7 swaps in 58 s), word-by-word captions (a caption change every 1–2 s), vignette, 2 hard wipes/cuts | image every 3–8 s; 2–4-word captions; ≤1 transition style; slow 1.05–1.15× push per image | |
| **Audio** | 200 wpm, 94 % speech coverage, 26 pauses ≥0.35 s in 22:52, −19.4 LUFS, LRA 2.8; no SFX; bed inaudible | 170–200 wpm; remove pauses > 0.5 s except before reveals; bed −30 to −35 dB under the voice (audible but subliminal) or none; −14 to −16 LUFS for YouTube; optional soft whoosh on title cards only | ffmpeg `silenceremove` / `loudnorm=I=-15:LRA=4` |
| **Recycled footage** | intro loops 2–7 s browsing takes 2–3× (≈20–25 s) | acceptable for "talking over proof", but vary zoom or crop on the repeat so it is not pixel-identical | |

---

## QA script

Save it as `edit_rhythm_qa.py`. It is self-contained: ffmpeg + numpy + Pillow, no OpenCV. I ran it on the whole reference video (3 min 14 s on a laptop CPU), and it reproduces this report's numbers:
- 25.5 changes/min, 8.7 shot changes/min, median shot 2.6 s;
- longest hold 31.9 s and 28 holds > 8 s. Both FAIL our stricter target by design;
- 16 zoom candidates (14 real + the 2 false positives listed in the calibration);
- −19.4 LUFS / LRA 2.8;
- 17 loud windows ≥12 dB over speech, clustered into the stings listed below.

```python
#!/usr/bin/env python3
"""edit_rhythm_qa.py - measure the edit rhythm of a finished video (QA gate).

Needs: ffmpeg/ffprobe on PATH, Python 3.9+, numpy, Pillow.  No OpenCV.
Usage:
  python edit_rhythm_qa.py VIDEO.mp4 [--start 0] [--dur 0] [--out qa_out] [--hold 8] [--profile tutorial|animated]
Outputs: qa_out/events.csv, qa_out/minutes.csv, qa_out/report.json and a pass/fail table on stdout.

Event classes (10 fps, 256x144 grey):
  cut          instant (<=0.3 s) full-frame content change (editor cut, tab switch, overlay in/out)
  page_change  gradual full-frame change (fade, page load, animated transition)
  zoom_in/out  camera scale change (NCC scale search 1.06-2.3x), returns factor + move duration
  scroll/pan   camera/page translation
  local        region-limited change >=4 % of pixels (UI update, caption, sticker, typing burst)
  micro        <4 % of pixels (cursor, caret) - ignored for rhythm
"""
import argparse, json, math, os, subprocess, sys
import numpy as np
from PIL import Image

W, H, FPS = 256, 144, 10

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def decode_gray(video, start, dur):
    cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(start)]
    if dur: cmd += ['-t', str(dur)]
    cmd += ['-i', video, '-vf', f'fps={FPS},scale={W}:{H}:flags=area,format=gray', '-f', 'rawvideo', '-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W)

def rs(img, w, h):
    return np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).resize((w, h), Image.BILINEAR), np.float32)

def ncc_match(big, small, minstd=6.0):
    Hb, Wb = big.shape; Hs, Ws = small.shape
    if Hs > Hb or Ws > Wb or Hs < 6 or Ws < 6 or small.std() < minstd: return (-1.0, 0, 0)
    T = small - small.mean(); tn = np.sqrt((T ** 2).sum())
    num = np.fft.irfft2(np.fft.rfft2(big) * np.fft.rfft2(T[::-1, ::-1], s=big.shape), s=big.shape)[Hs-1:Hb, Ws-1:Wb]
    def wsum(x):
        ii = np.pad(x.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
        return ii[Hs:, Ws:] - ii[:-Hs, Ws:] - ii[Hs:, :-Ws] + ii[:-Hs, :-Ws]
    N = Hs * Ws; s1 = wsum(big); var = np.maximum(wsum(big ** 2) - s1 ** 2 / N, 1e-6)
    ncc = num / (np.sqrt(var) * tn); ncc[var / N < minstd ** 2] = -1
    k = int(np.argmax(ncc)); y, x = divmod(k, ncc.shape[1])
    return (float(ncc[y, x]), y, x)

SCALES = [1.0, 1.06, 1.12, 1.2, 1.28, 1.36, 1.45, 1.55, 1.67, 1.8, 1.95, 2.1, 2.3]
STEP_SCALES = [1.0, 1.03, 1.06, 1.1, 1.15, 1.22, 1.3]

def estimate(A, B, crop=0.7, scales=SCALES):
    """How is B related to A? best scale (>1 zoom-in), NCC of best fit, identity NCC, shift at scale 1."""
    A = A.astype(np.float32); B = B.astype(np.float32)
    a0, b0 = A - A.mean(), B - B.mean()
    ncc_id = float((a0 * b0).sum() / np.sqrt((a0 ** 2).sum() * (b0 ** 2).sum() + 1e-6))
    cw, ch = int(W * crop), int(H * crop); x0, y0 = (W - cw) // 2, (H - ch) // 2
    Bc, Ac = B[y0:y0+ch, x0:x0+cw], A[y0:y0+ch, x0:x0+cw]
    res = []
    for s in scales:
        sm = Bc if s == 1.0 else rs(Bc, round(cw / s), round(ch / s))
        c, y, x = ncc_match(A, sm); res.append((c, s, y, x))
        if s > 1.0:
            c, y, x = ncc_match(B, rs(Ac, round(cw / s), round(ch / s))); res.append((c, 1 / s, y, x))
    r1 = [r for r in res if r[1] == 1.0][0]
    best = max(res, key=lambda r: r[0])
    return dict(scale=best[1], ncc=best[0], ncc_id=ncc_id, ncc_s1=r1[0], dy=r1[2] - y0, dx=r1[3] - x0)

def detect_events(a):
    a16 = a.astype(np.int16)
    d = np.abs(a16[1:] - a16[:-1]); mad = d.mean((1, 2)); frac = (d > 24).mean((1, 2))
    act = (frac > 0.02) | (mad > 2.0); n = len(mad); segs = []; i = 0
    while i < n:                                  # group active pairs, bridge 1-frame gaps
        if act[i]:
            j = i
            while j + 1 < n and (act[j+1] or (j + 2 < n and act[j+2])): j += 1
            segs.append((i, j)); i = j + 1
        else: i += 1
    events = []
    for i0, i1 in segs:
        A = a[i0].astype(np.float32); B = a[min(i1 + 1, len(a) - 1)].astype(np.float32)
        r = estimate(A, B); m = np.abs(A - B) > 24; chg = float(m.mean())
        if m.any():
            ys, xs = np.where(m); bbarea = (np.ptp(xs) + 1) * (np.ptp(ys) + 1) / (W * H)
        else: bbarea = 0.0
        ntr = nzm = 0; sdy = sdx = 0; zp = 1.0; nst = 0
        for k in range(i0, i1 + 1):               # per-step motion model
            if frac[k] < 0.01 and mad[k] < 1: continue
            nst += 1; s = estimate(a[k], a[k+1], crop=0.6, scales=STEP_SCALES)
            if s['ncc'] > 0.85:
                if s['scale'] == 1.0 and (s['dy'] or s['dx']): ntr += 1; sdy += s['dy']; sdx += s['dx']
                elif s['scale'] != 1.0 and s['ncc'] - s['ncc_s1'] > 0.03: nzm += 1; zp *= s['scale']
        dur = (i1 - i0 + 1) / FPS; peak = float(frac[i0:i1+1].max())
        conc = float(frac[i0:i1+1].max() / max(frac[i0:i1+1].sum(), 1e-6))   # single-step concentration
        dl = abs(A.mean() - B.mean()); gain = r['ncc'] - max(r['ncc_id'], r['ncc_s1'])
        zf = 1.0
        if chg < 0.04 and ntr < 2: cls = 'micro'
        elif dl < 15 and ((r['ncc'] >= 0.75 and r['scale'] != 1 and gain >= 0.15 and abs(math.log(r['scale'])) > 0.05)
                          or (nzm >= 2 and nzm >= 0.4 * nst and abs(math.log(zp)) > 0.08)):
            zf = r['scale'] if (r['ncc'] >= 0.75 and gain >= 0.15) else zp
            cls = 'zoom_in' if zf > 1 else 'zoom_out'
        elif dl < 12 and chg < 0.6 and nst and ntr >= 0.5 * nst and abs(sdy) + abs(sdx) >= 4:
            cls = 'scroll' if abs(sdy) >= abs(sdx) else 'pan'
        elif (chg >= 0.2 and bbarea >= 0.35) or (bbarea >= 0.6 and chg >= 0.1 and r['ncc_id'] < 0.85):
            cls = 'cut' if (dur <= 0.3 and conc >= 0.6) or (conc > 0.6 and peak > 0.25) else 'page_change'
        elif chg < 0.04: cls = 'micro'
        else: cls = 'local'
        events.append(dict(t0=i0 / FPS, t1=(i1 + 1) / FPS, dur=dur, cls=cls, chg=round(chg, 3), bbarea=round(bbarea, 2),
                           zoom_factor=round(zf, 2), lum_jump=round(dl, 1)))
    return events, mad, frac

def audio_stats(video, start, dur):
    cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(start)] + (['-t', str(dur)] if dur else []) + \
          ['-i', video, '-vn', '-ac', '2', '-ar', '22050', '-f', 's16le', '-']
    x = np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.int16).reshape(-1, 2).astype(np.float32) / 32768
    if not len(x): return {}
    mid, side = (x[:, 0] + x[:, 1]) / 2, (x[:, 0] - x[:, 1]) / 2; hop = 2205; n = len(mid) // hop
    db = lambda v: 20 * np.log10(np.sqrt((v[:n*hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)
    m, s = db(mid), db(side); speech = float(np.median(m))
    loud = m > speech + 12                                     # stings / SFX / music hits >= 12 dB over speech
    stings, i = [], 0
    while i < n:
        if loud[i]:
            j = i
            while j + 1 < n and (loud[j+1] or (j + 3 < n and loud[j+2:j+4].any())): j += 1
            if j - i + 1 >= 3: stings.append(round(i / 10 + start, 1))
            i = j + 1
        else: i += 1
    quiet = m < -35; pauses, i = 0, 0
    while i < n:
        if quiet[i]:
            j = i
            while j + 1 < n and quiet[j+1]: j += 1
            pauses += (j - i + 1) >= 4; i = j + 1
        else: i += 1
    lo = run(['ffmpeg', '-hide_banner', '-nostats', '-ss', str(start)] + (['-t', str(dur)] if dur else []) +
             ['-i', video, '-vn', '-af', 'ebur128', '-f', 'null', '-']).stderr
    I = [l for l in lo.splitlines() if l.strip().startswith('I:')]; L = [l for l in lo.splitlines() if l.strip().startswith('LRA:')]
    return dict(speech_rms_median_db=round(speech, 1), pauses_ge_0_4s_below_m35db=int(pauses), loud_stings=stings,
                stereo_bed_share=round(float((s > -75).mean()), 2),
                integrated_lufs=I[-1].split()[1] if I else None, lra=L[-1].split()[1] if L else None)

def summarize(events, t0, t1, hold):
    nm = [e for e in events if e['cls'] != 'micro' and t0 <= e['t0'] < t1]
    shots = [e for e in nm if e['cls'] in ('cut', 'page_change')]
    mins = max((t1 - t0) / 60, 1e-6)
    bt = np.diff([t0] + [e['t0'] for e in shots] + [t1]); bt = bt[bt > 0.05]
    at = [t0] + [e['t0'] for e in nm] + [t1]
    holds = [(round(at[i], 1), round(at[i+1] - at[i], 1)) for i in range(len(at) - 1) if at[i+1] - at[i] > hold]
    c = {k: sum(1 for e in nm if e['cls'] == k) for k in ['cut', 'page_change', 'zoom_in', 'zoom_out', 'scroll', 'pan', 'local']}
    return dict(changes=len(nm), changes_per_min=round(len(nm) / mins, 1), cuts_per_min=round(c['cut'] / mins, 1),
                shot_changes_per_min=round(len(shots) / mins, 1), median_shot_s=round(float(np.median(bt)), 1) if len(bt) else None,
                mean_shot_s=round(float(bt.mean()), 1) if len(bt) else None,
                median_gap_between_changes_s=round(float(np.median(np.diff(at))), 1), longest_hold_s=round(max(np.diff(at)), 1),
                holds_over_limit=holds, zooms=c['zoom_in'] + c['zoom_out'], **c)

# Targets distilled from the reference video (AI Flow, SRjm9tvMHhs) - see 04-edit-rhythm-metrics.md
TARGETS = {'tutorial': dict(changes_per_min=(20, 45), shot_changes_per_min=(6, 18), median_shot_s=(1.5, 5.0), max_hold_s=15, holds_per_10min=6),
           'animated': dict(changes_per_min=(15, 40), shot_changes_per_min=(5, 12), median_shot_s=(3.0, 9.0), max_hold_s=10, holds_per_10min=3)}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('video'); ap.add_argument('--start', type=float, default=0)
    ap.add_argument('--dur', type=float, default=0); ap.add_argument('--out', default='qa_out'); ap.add_argument('--hold', type=float, default=8)
    ap.add_argument('--profile', default='tutorial', choices=list(TARGETS)); ap.add_argument('--no-audio', action='store_true')
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    frames = decode_gray(a.video, a.start, a.dur)
    events, mad, frac = detect_events(frames)
    for e in events: e['t0'] = round(e['t0'] + a.start, 2); e['t1'] = round(e['t1'] + a.start, 2)
    T0, T1 = a.start, a.start + len(frames) / FPS
    total = summarize(events, T0, T1, a.hold)
    minutes = [dict(minute=int(m // 60), **summarize(events, m, min(m + 60, T1), a.hold)) for m in np.arange(T0 - T0 % 60, T1, 60)]
    zooms = [e for e in events if e['cls'].startswith('zoom')]
    total['zoom_factors'] = [e['zoom_factor'] for e in zooms]; total['zoom_move_s'] = [e['dur'] for e in zooms]
    aud = {} if a.no_audio else audio_stats(a.video, a.start, a.dur)
    with open(os.path.join(a.out, 'events.csv'), 'w') as f:
        f.write('t0,t1,dur,class,changed_frac,bbox_area,zoom_factor,lum_jump\n')
        for e in events: f.write('{t0},{t1},{dur},{cls},{chg},{bbarea},{zoom_factor},{lum_jump}\n'.format(**e))
    with open(os.path.join(a.out, 'minutes.csv'), 'w') as f:
        keys = ['minute', 'changes', 'cut', 'page_change', 'zoom_in', 'zoom_out', 'scroll', 'local', 'shot_changes_per_min', 'median_shot_s', 'longest_hold_s']
        f.write(','.join(keys) + '\n')
        for m in minutes: f.write(','.join(str(m[k]) for k in keys) + '\n')
    json.dump(dict(total=total, minutes=minutes, audio=aud), open(os.path.join(a.out, 'report.json'), 'w'), indent=1, default=str)
    t = TARGETS[a.profile]; mins = (T1 - T0) / 60
    checks = [('changes/min', total['changes_per_min'], t['changes_per_min']),
              ('shot changes/min', total['shot_changes_per_min'], t['shot_changes_per_min']),
              ('median shot s', total['median_shot_s'], t['median_shot_s'])]
    print(f"\n== Edit-rhythm QA  {a.video}  [{T0:.0f}-{T1:.0f}s, profile={a.profile}]")
    for name, v, (lo, hi) in checks:
        print(f"{name:<22}{v!s:>8}   target {lo}-{hi}   {'PASS' if v is not None and lo <= v <= hi else 'FAIL'}")
    nh = len(total['holds_over_limit']); lim = t['holds_per_10min'] * mins / 10
    print(f"{'longest hold s':<22}{total['longest_hold_s']:>8}   max {t['max_hold_s']}   {'PASS' if total['longest_hold_s'] <= t['max_hold_s'] else 'FAIL'}")
    print(f"{'holds > %gs' % a.hold:<22}{nh:>8}   max {lim:.0f}   {'PASS' if nh <= lim else 'FAIL'}")
    print(f"{'zoom moves':<22}{total['zooms']:>8}   factors {total['zoom_factors'][:12]}")
    if aud: print('audio:', {k: v for k, v in aud.items() if k != 'loud_stings'}, '| stings at', aud['loud_stings'][:20])

if __name__ == '__main__':
    main()
```

Notes for use:
- `--profile tutorial` is for screen-recording videos. `--profile animated` is for finished cartoon videos like the 21:53 product (image every 3–8 s, captions as local changes).
- For a Remotion pipeline, run it on every render. Fail the build when `longest_hold_s > 15` (tutorial) or `> 10` (animated), and print `holds_over_limit` so the generator can insert a push or zoom there.
- Thresholds were calibrated on 1080p screen recordings with mostly white UI. For dark UIs, lower `frac > 0.02` to 0.015.

---

## Why it works (hypotheses tied to evidence)

1. **Fast proof first, then slow and real.** In 0:00–3:12, 11 inserts, 12 zooms and 12.8 shot changes/min sell the opportunity: real channels, zoomed numbers, money meme, competitor clip. After 4:15 the editor stops decorating; the tutorial is real-time screen recording at native scale. This makes it feel authentic and easy to follow ("I can do this with free tools"). The replay curve shows viewers come back to the *instruction screens* (11:26–12:35, 15:19–15:47), not to the dense intro (replay 0.10).
2. **The voice is the metronome.** 200 wpm, 94 % speech coverage and only 11 pauses in 21:50 of tutorial mean there is always something being *said*, even when the picture holds for 15–30 s. The median 1.4 s between visual changes comes mostly from the narrator's own clicks, scrolls and tab switches, so it is motivated movement rather than decorative cutting.
3. **Every zoom points at a claim.** Zooms only happen when a number or title is spoken (24 videos, 46K subs, 184 videos, ~1M views, 52-min videos). The camera "underlines" the proof, so a few zooms carry a lot of persuasion.
4. **Reveals are punctuated.** The 11 loud stings land exactly on "result appears" moments, and those buckets have 2.2× the average replay. The sting marks "this is the payoff", and viewers seek to it. Causation is uncertain: stings sit on the result screens people revisit anyway.
5. **Strategic static.** Holds on prompts and settings are not dead air for this audience. 26 of 133 comments ask for the PDF or prompts; people pause and copy. Tightening those parts with fast cuts would likely *hurt* (ρ between shot changes and replay is −0.18 to −0.23).
6. **App switching is free visual variety.** Moving through YouTube → ChatGPT → Docs → Whisk (yellow) → Claude → AI Studio → Grok → CapCut (dark) changes the screen's colour and layout every 1–3 min without editing effort.

---

## Rules to copy

1. **Hook:** make 5–7 visual changes in the first 10 s (one every 1.2–2.0 s) using ≥3 source types (meme/B-roll, kinetic text, black title card, screen proof). Show screen proof by 0:08.
2. **Proof section (first ~3 min):** reach ≥25 visual changes/min and ≥10 shot changes/min. Insert a meme, example clip or text card every 15–30 s.
3. **Zoom only on a spoken claim.** Start a punch-in to **1.5–1.67×** within 0–1 s of naming an on-screen number, title or field.
4. **Zoom motion:** animate 0.3–0.7 s with an ease-in-out S-curve, combined with a pan to the target. Hold 3–4 s (one sentence). Zoom back out to 100 % on the next sentence. Never hard-cut to a crop.
5. **Gentle push:** use **1.12–1.3× over 1–2.7 s** for "look at this page" moments with no specific element.
6. **Tutorial body:** keep the recording at full frame ≥70 % of the time. Aim for 20–30 visual changes/min, with motivated UI actions counting as changes.
7. **Hold limits:** never hold a frame > 15 s. Allow 8–15 s holds only on instruction screens (prompt, settings, script), at most 6 per 10 min, and only when the text is mobile-readable (zoom ≥1.5× if needed).
8. **Field punch-in:** punch in on every field the viewer must type into or copy, and say the exact field name while zoomed.
9. **Example clip:** show one competitor or finished-product clip of 10–17 s with its **own audio**, inside the first 3 min.
10. **Payoff demo:** show a 4–8 s demo of every generated asset (image → video, voice sample) right after the generation step.
11. **Reveal sting:** play a 1–3 s music sting in the gap before a result reveal, mixed at most +6 LU above the voice (the reference's +12–14 LU is too loud to copy). Follow it with "now look" and a punch-in on the result.
12. **CTA animation:** place an animated CTA (dim background to ~20 % luminance, card pops, button changes state; 3–4 s) every 6–8 min, only during waiting or low-information moments, never over a prompt being copied.
13. **Target cards:** show subscriber/like targets as 2–5 s neon-green (#3AFC00) bold text with a dark outline over the dimmed screen, with at most 2 per video.
14. **Literal memes:** use meme inserts only on a literal keyword ("money" → money meme), ≤5 s each, about 1 per 2–3 min in long tutorials.
15. **Narration density:** keep narration at 170–200 wpm with ≥90 % speech coverage. Cut pauses > 0.5 s except the deliberate pre-reveal beat.
16. **Mix:** −14 to −16 LUFS integrated, LRA ≤ 4 LU, voice mono-centred. Put a music bed 30–35 dB under the voice or omit it. Use no SFX on cuts; SFX are optional on title cards only.
17. **Finished product:** in the final cartoon video, swap the image every 3–8 s, show captions of 2–4 words that change every 1–2 s, use one transition style, and add a 1.05–1.15× push per image.
18. **Recycled B-roll:** if you reuse B-roll under long talking stretches, change crop or zoom on each repeat so frames are never pixel-identical.
19. **QA gate:** run `edit_rhythm_qa.py` on every render. Fail when longest hold > 15 s (tutorial) / > 10 s (animated), changes/min < 20, or median shot > 5 s (tutorial) / > 9 s (animated).

---

## Open questions / low-confidence

- **Cut count accuracy:** about 89 % of 47 checked events were classified correctly. White→white tab switches with similar layouts can be missed (one found at 19:50.5), so the true cut count is probably 110–118, not 106. I could not separate an *editor* cut from an *in-recording* tab switch; both look identical in the export.
- **Music bed audibility:** the 21.815 s periodic stereo element proves a continuous looped track, but its level in the centre channel could not be isolated. My estimate is ≤ −45 dBFS, and I could not listen to it. Treat "bed present but inaudible" as medium confidence.
- **Nature of the stings:** they are harmonic and chord-like, so music rather than speech, but they could be meme audio (an iconic jingle) rather than a stock sting. I also did not verify whether they cover sped-up footage. Motion during stings is close to average (MAD 0.3–3.4 vs 2.7), which argues against a fast time-lapse.
- **Zoom tooling:** whether the zooms are CapCut keyframes or a Screen-Studio-type recorder cannot be told from pixels. The S-curve easing with simultaneous pan fits both.
- **Arrows and highlights in non-red colours** were not systematically searched; only red boxes were scanned. Blue text selections are native browser highlights.
- **Replay curve ≠ retention.** "Most replayed" shows seek-back density, not drop-off. The value of the dense intro for first-time retention is inferred, not measured.
- **Per-minute holds** are clipped at minute boundaries in the table. True hold durations are in the separate hold list.
- **WPM** comes from Whisper word timestamps of Hindi/Urdu ASR; word segmentation for this language may inflate counts by ±10 %.
