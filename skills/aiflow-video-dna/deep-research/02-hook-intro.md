# 02 — The hook and the intro (00:00 → 03:12, chapter "Important")

Analyst #2 of 8 · Video: AI Flow, "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)", 22:52, 144,518 views.

**Evidence I used:**
- I read all 240 frames in `frames_intro_4fps` (0–60 s) and every 1 fps frame from 60 to 192 s, mostly as labelled contact sheets.
- I extracted extra 10 fps frames for the moments where motion matters (0–13 s, 17.5–21 s, 134.5–140 s, 183–192.5 s). They are in `ROOT\tmp\a2\f10_*`, with contact sheets in `ROOT\tmp\a2\sheets10`.
- Transcripts: `transcript_transcribe.json` (Hindi/Urdu, word timestamps) and `transcript_translate.json` (English translation).
- Edit and audio data: `cuts.csv`, `scdet_scores.csv`, `silences.csv`, and `audio16k.wav` (my own RMS and sub-bass measurements).
- Other data: `heatmap.json`, the thumbnail `v.webp`, `comments.json` and `channel_videos.tsv`.

Timestamps are mm:ss.s. Spoken times come from the Hindi word timestamps unless I mark them EN.
The narration is paraphrased. Short quotes appear only where the wording itself is the pattern.

---

## 0. One-paragraph summary

The intro is a **3-minute "proof dossier"**, not a 15-second hook.

**The hook (0–9 s):**
- It opens with a 1.5 s reaction clip and asks "which YouTube niche always has high RPM?".
- At 0:05 it pretends to read your mind ("yes, you guessed right").
- At **0:08.1** it slams the answer on screen as a full-screen spinning title card, "Finance Niche". This is the thumbnail's own headline.
- At **0:09.2** it cuts to the competitor's channel grid, which contains the very thumbnails shown in the video's thumbnail.

**What follows the hook:**
- It runs **two proof channels**, a small new one first and then the title's channel, Nick Invests.
- It states **17 distinct numbers in 192 s (8 in the first 60 s)**. Each spoken number is matched by a punch-in or a blue text-selection highlight within about 0.5 s.
- It does **money math** with a deliberately conservative RPM: 668K views × $5 RPM = **$3,340**, spoken at 0:58.2.
- It kills the **"fake views" objection** using likes and comments.
- It **deconstructs one competitor title** as a curiosity and FOMO device.
- It gives a **money motive**: a 3.5 s WWE "Here Comes the Money" meme, then "52 min, 44 min, so more ads".
- The **explicit promise** comes only at **2:34.2**. After it come an open loop (a future video about the first channel), reassurance, 9 s of the competitor's actual video with its own audio, and a subscribe CTA framed as a public goal ("100K before 2027").

**Delivery and edit rhythm:**
- The narration never stops: about 200 Hindi-ASR words per minute (EN translation ≈ 185 wpm), and only one pause ≥ 0.35 s in the first 60 s.
- The picture never freezes for more than 3.7 s.

---

## 1A. Second-by-second HOOK TABLE (0–30 s)

The columns give the narration beat (paraphrased, with spoken word times), what is on screen, the edit event, and the psychological function.

| t (s) | Narration beat (paraphrased) | On screen | Edit event | Function |
|---|---|---|---|---|
| 0 | "Let me ask you a question" (0.00–1.42) | Kung Fu Panda's Po close-up, inset (~60 % width) on a black pillarbox. The first frame is motion-blurred, so the clip enters with a zoom/whip | Clip opens on a blur-in. No title, no logo, no face | **Pattern interrupt** + question frame |
| 1 | End of frame line. The real question starts at 1.62 | Po turns or shakes (blur at 1.2). **HARD CUT 1.57** to an AI-generated red room: walls tiled with hundreds of video screens, one red-yellow screen with a small woman's silhouette | Cut #1 (scdet 13.7) | Curiosity: "the YouTube world" metaphor |
| 2 | "On YouTube, which niche…" (1.62–2.84) | Red room, slow push-in | Push-in | **Question** |
| 3 | "…whose RPM always stays high?" (3.10–4.78) | **HARD CUT 3.34** to a white radial-vignette background (#fbfbfb center) | Cut #2 (scdet 62) | Question / stakes |
| 4 | Same sentence. RPM 3.48, "always" 3.90, HIGH 4.34 | Kinetic text appears **word by word, karaoke-synced**: "RPM", then "Hamesha", "HIGH", "rehta", "hai". Each word fades grey→black in ~0.2 s at 3.5 / 3.7 / 3.9 / 4.1 / 4.3. Bold sans, dark grey, left-center | Kinetic caption (5 pops in 0.9 s). Cleared at 4.9 | **Keyword emphasis** (benefit = high RPM) |
| 5 | "Yes, you thought exactly right" (5.12–6.88) | 5.0–5.3: a framed image card fades in (washed-out → full colour) with a drop shadow on white. Two translucent blue heads with glowing brains linked by lightning ("mind reading") | Fade-in card | **Rapport / validation**: the viewer feels clever |
| 6 | (continues) | Card holds | — | Validation |
| 7 | "The name of that niche is…" (7.12–7.88) | **HARD CUT 7.0** to a screen recording of the Nick Invests channel Videos tab. The cursor clicks *Popular* (7.5) and the page dims and reloads at 7.9 | Cut #3 (24.4) + click | 1-second **withheld answer** (suspense) |
| 8 | "**Finance Niche**" (8.32–8.82) | **HARD CUT 8.07** to black. White heavy sans "Finance Niche" **spins in from ≈ −35° and levels by 8.4 s** | Cut #4 (71.2), kinetic title. **Sub-bass hit** at 8.75–9.5 s (30–90 Hz band +10–15 dB vs. neighbours; RMS −18 dBFS) | **Instant answer**. It is the exact headline of the thumbnail ("FINANCE NICHE") |
| 9 | "It's the only niche…" (9.20) | **HARD CUT 9.2** to the Nick Invests *Popular* grid. Thumbnails include "THE $20,000 RULE", "$900 A MONTH?!" and "WHAT PEOPLE REALLY HAVE", the same ones as in the video's thumbnail. View counts are visible: 954K, 617K, 609K, 491K | Cut #5 (68.5) | **Thumbnail promise confirmed**. First on-screen numbers |
| 10 | "…whose RPM never goes down" (10.68–12.10) | Hover-autoplay preview on the top thumbnail. vidIQ "Views per hour" tooltip | Hover / tooltip | **Authority claim** (absolute) |
| 11 | (continues) | **11.5:** blue browser text-selection (#1c73f8) over the top title + "954K views". vidIQ outlier tooltip | Highlight | First **highlighted number** |
| 12 | "First of all, look at this channel" (12.64–13.72) | **HARD CUT 12.45** to the *Legend Investor Mindset* channel page (Buffett-portrait thumbnails) | Cut #6 (15.4). This is the **last edit cut of the hook**; from here on it is continuous screen recording | **Proof channel #1** introduced |
| 13 | "look" (13.72) | Static channel header | — | Pointer ("look at this") |
| 14 | "Legend Investor Mindset" (14.24–15.30) | Cursor moves to the stats line | — | Naming |
| 15 | "brother (bhai sahab)…" (15.78) | Red click-ring around the cursor on the stats line | Cursor ring | **Peer tone** |
| 16 | "…it has only…" (16.82) | **PUNCH-IN 16.5–17.0** (~1.3–1.5×, estimated) on the channel header | Zoom-in, 0.6 s **before** the number is spoken | Sets up the contrast |
| 17 | "**24 videos**" (17.12) | "24 videos" blue-selected 17.1–17.9 | Highlight synced to the word | **Proof number #1**: small input |
| 18 | "**46,000**" (18.56–19.06) | Selection jumps to "46.1K subscribers" (18.8) | Highlight synced | **Proof number #2**: big output |
| 19 | "…subscribers achieved" (19.40–20.62) | Hold (frame frozen 17.08–20.19 except the selection) | — | Proof lands |
| 20 | — | **ZOOM-OUT 20.0–20.6** | Zoom-out | Reset |
| 21 | "And guess: which niche is the content in?" (20.90–22.76) | Static page, idle cursor | — | **Rhetorical question** / micro-loop |
| 22 | (continues) | Static | — | Open loop |
| 23 | "I'll tell you myself" (23.24–24.04) | Static (frozen 22.3–24.2 s) | — | Loop closed in **≈ 2.3 s** |
| 24 | "This channel makes finance content" (24.26–26.28) | Scroll down (24.0) | Scroll | Confirmation |
| 25 | (continues) | Hover-autoplay preview of the first thumbnail, with its burned-in captions playing (25.5–28.5) | Hover preview | Evidence that it is a real, live video |
| 26 | "But still, look how fast it has grown" (26.50–28.84) | Preview plays | — | **Speed / FOMO** |
| 27 | "look" (27.00) | Preview | — | Pointer |
| 28 | (continues) | Scroll back up (28.0) | Scroll | — |
| 29 | "Every one of its videos gets very good views" (29.12–31.48) | Cursor rests on the vidIQ **"Monetized"** badge (29–30) | Cursor | **Proof** (monetized = earning) |

**Count for 0–30 s:**
- 6 hard edit cuts, all in the first 12.45 s, so the average shot length there is **2.1 s**.
- About **20 distinct visual events** in 30 s, roughly one every 1.5 s. These are cuts, kinetic pops, fades, clicks, hovers, highlights, zooms and scrolls.
- From 12.45 s on, change comes from **cursor, selection, zoom and scroll** inside one continuous screen recording, not from cuts.

---

## 1B. Beat table 30 s → 3:12

| Time | Narration beat (paraphrased) | On screen | Edit event | Function |
|---|---|---|---|---|
| 0:30.7–0:35.2 | Its first video went up only two months ago (31.8–35.2) | Click *Oldest* (page dims 30.7) → oldest list, "2 months ago" dates. Slow push-in toward the dates 31.3–34 | Click + slow zoom | **Recency proof**: the door is still open (FOMO) |
| 0:35.2–0:38.4 | Its popular video went viral just two weeks ago | Popular sort, zoomed. "How to Escape Low Income… 668K · 2 weeks ago", vidIQ outlier badge ">100×" | Zoomed view | Virality + recency |
| 0:38.5–0:44.2 | That video now has **668,000** views (spoken 39.26–40.62), huge for finance | Title + "668K views" blue-selected **39.0–40.0**. VPH tooltip. Smooth zoom-out 42.0–43.75 | Highlight synced, zoom-out | **Proof number** |
| 0:44.5–0:49.8 | Do the math yourself: finance RPM runs **$5–$15** (5 at 47.66, 15 at 49.18) | Scroll down/up the grid. Click *Latest* (48.3) | Scroll / click | **Money math set-up** (anchor range) |
| 0:50.9–0:59.9 | Take only the *minimum* $5 → this one video = **$3,340** (58.16) | Hover preview. Click *Popular* (52.0). Click into the video, which gives a **1.3 s glimpse of the real video** (53.1–54.5: Buffett portrait + green/white kinetic captions). Back. 668K re-selected 57.5–59.5 while "$3,340" is spoken. **No calculator overlay** | Two cuts (page changes) + highlight | **Money math** (conservative = credible) |
| 0:59.9–1:03.9 | And many more videos have lakhs of views | Scroll the grid | Scroll | Abundance |
| 1:03.9–1:17.7 | Don't think these are fake views. Open any video, look at the likes and the comments: real people watch this | Click *Latest*. Open the "Poverty Loop" video (68.7). Player shows a kinetic caption "over 10 years". Description panel, **25K likes**, "**1,533 Comments**", scroll through comments 72–76 | Page cut + scroll | **Objection handling** + social proof |
| 1:17.7–1:26.0 | Besides this one, look at **Nick Invests**: only **184** videos (82.04), **155,000** subscribers (84.6) | Hover *Similar Channels* (78) → Nick Invests channel (79), banner with a cartoon man. Name selected (81). **PUNCH-IN 81.5–82.0 (~2×)**: "184 videos" selected (82), then "155K subscribers" (84–85). Zoom-out 86 | Zoom + highlight synced | **Proof channel #2** (the title's channel) |
| 1:26.6–1:28.8 | Its videos are really interesting | Popular grid. Click *Oldest* (88) | Click | Bridge |
| 1:29.5–1:38.8 | Look how many views. The popular one, from only 5 months ago, has nearly **1 million** | Oldest list ("6 months ago") → back to popular (92) → zoom-in (95). "954K" + title selected, outlier tooltip (97). **Whip/zoom-blur transition** (98) | Zoom, highlight, blur transition | **Proof number** |
| 1:39.3–1:44.7 | These are evergreen: even now it gets views **every hour** | vidIQ "Views per hour" tooltip | Tooltip | **Passive-income** proof |
| 1:45.1–1:48.4 | They're not as simple as they look | Hover-autoplay preview | — | Curiosity: "I'll decode it" |
| 1:48.9–1:56.2 | Look at the titles. Reads "Why Everything Changed Even More After $20,000"; "reading it, I want to click" | Scroll (108.5–110.5) → **PUNCH-IN + red rectangle (#f6272b)** around the $20,000 card (title + 954K). **Fully frozen 111.9–115.7 s (3.7 s, the longest freeze in the intro)** while the title is read | Zoom + red box | **Title deconstruction** (curiosity gap modelled) |
| 1:57.2–2:07.2 | Everyone wants to know what changes after $20k. Relatable + FOMO → viral | Zoom-out, long scroll of the grid, *Latest* list (newest "12 hours ago") | Scroll | Names the psychology (teaches the "why") |
| 2:07.6–2:15.4 | Stop and think: why do all these channels make content? Don't overthink it, the reason is money | **3-D tilt/perspective zoom** of the grid (2:08–2:11). Cut to the Legend page (2:13) | Tilt-zoom, cut | Rhetorical question → motive |
| 2:15.4–2:18.9 | (the meme's own song line plays: "Here comes the money") | **Full-screen WWE meme**: an executive with cash and an arena crowd. Heavy motion blur, whip-blur out at 2:18.0–2:18.8. Narration gap of 1.24 s (137.76–139.0), the only real VO gap before the sample clip | Meme insert + its audio | **Pattern interrupt** + humour |
| 2:18.9–2:31.3 | Look at the lengths: **52** min (140.70), **44** min (141.52). Longer video = more ads = more earnings | Nick *Latest* grid. **Punch-in + red rectangles** on the "FOLLOW THE MONEY 52:40" card (2:21) and the "LIVE WITHOUT WORRIES 44:05" card (2:22), each within ~0.5 s of the spoken number. Scroll | Zoom + red box ×2 | **Money logic #2** (format = revenue) |
| 2:31.5–2:33.9 | Now you know why the finance niche matters | Grid | — | Recap |
| **2:34.2–2:38.8** | **That's why in this video I'll teach you to make videos like Nick Invests** | Continuous scroll through ~40 Nick thumbnails (abundance visual) | Scroll | **EXPLICIT PROMISE** |
| 2:39.5–2:43.0 | The channel you saw at the start will get its own video too | Cut to the Legend Investor Mindset page | Cut | **Open loop** (future video / series) |
| 2:43.4–2:49.4 | No stress; this video will be very interesting, so sit back and watch carefully | Legend page → click *Latest* → cut (2:47) to the Nick watch page playing "Why Everything Changes EVEN MORE After $20,000" with burned-in captions | Cut | **Reassurance** + attention instruction |
| 2:49.7–2:58.4 | (no host VO; the competitor video's own English narration plays) | Competitor video cropped **inset on black** (~44 % width). Cartoon man with phone "BALANCE", green coffee, red "RAMEN" pack; yellow-outline word captions | Inset; host voice muted for 8.7 s | **Taste of the output** (what you will make) |
| 2:58.4–3:03.0 | Before we go on, one thing… | Back to the Nick watch page (captions continue) | — | CTA set-up |
| 3:03.2–3:06.0 | Yes, *that* thing: if you haven't subscribed to AI Flow, do it now | AI Flow channel page; banner "**TARGET: 100K SUBS BEFORE 2027**" with a progress bar 30,333 / −69,667. 3:03.9 page dims, a white card scales in (3:04.0–3:04.5) with a YouTube logo + red SUBSCRIBE; the cursor clicks; **"SUBSCRIBED" (grey) at 3:06** | Dim + animated card | **Subscribe CTA** |
| 3:06.9–3:11.6 | …because we have to reach 1 lakh (100K) subscribers before 2027 (2027 at 187.08) | AI Flow video grid → **3:09.7–3:11.6 full-screen bright-green (#3efd02) "100K Subscribers"** over the dimmed page | Full-screen text card | **Goal-gradient / community** CTA |
| 3:11.7 → | As always, step one for any niche: channel creation and branding | Cut to the Nick Invests channel. **Chapter 2 starts 3:12** | Cut | Transition |

---

## 2. HOOK ANATOMY

### Structure name

> **Question → Mind-read ("you guessed right") → Instant answer as title card → Authority claim on the competitor grid → Proof channel #1 (small input / big output) → Micro-question → Recency & virality proof → Money math with the minimum RPM → Anti-objection ("not fake views") → Proof channel #2 (the title's channel) → Evergreen proof → Title deconstruction (curiosity + FOMO) → Money motive (+ meme interrupt) → "Length = more ads = more money" → Explicit promise → Open loop (future video) → Reassurance → Taste of output → Public-goal subscribe CTA → Chapter 2**

In short, a **"Proof Dossier" intro**: hook (9 s) + 2-channel case file (2 min) + motive (40 s) + promise and bridge (60 s).

### Measurements

| Metric | Value | Source |
|---|---|---|
| First spoken question | 0:00.0 frame line; the real question at **0:01.6** | Hindi words |
| Answer to the question | Card on screen **0:08.07**; spoken 0:08.32 (6.7 s after the question) | Frames, words |
| First number visible on screen | **0:09.2** (954K, 617K… on the grid) | i0037 |
| First highlighted number | **0:11.5** (954K, blue selection) | 10 fps sheet |
| First spoken proof number | **0:17.12** ("24 videos"), then 0:18.56 "46,000" | Words |
| Money math | Range at 0:45.9 → result **$3,340 at 0:58.16** (668,000 × $5 / 1000 is correct) | Words |
| Anti-objection | 1:03.9–1:17.7 | EN segments |
| Second proof channel | 1:17.7 (named 1:20.4) | EN |
| Title deconstruction | 1:48.9–2:07.2 | EN |
| **Explicit promise** of what the video teaches | **2:34.2** (154.2 s = 80 % of the way through the 192 s chapter) | Words |
| Open loop for a future video | 2:39.5 | Words |
| Distinct numbers stated | **8 in the first 60 s** (24; 46,000; 2 months; 2 weeks; 668,000; $5; $15; $3,340). **17 in 192 s** (+ 184; 155,000; 5 months; ~1 million; $20,000; 52 min; 44 min; 1 lakh/100K; 2027), plus vague "lakhs of views" | Transcript |
| Numbers highlighted on screen | **11** (blue selection ×8: 954K, 24, 46.1K, 668K ×2, 184, 155K, 954K; red box ×3: $20,000 card, 52:40, 44:05) + 100K card + progress bar | Frames |
| "Look at this" pointers (imperative *dekho*) | **9 in 192 s** (13.7, 27.0, 69.9, 71.9, 90.2, 101.4, 110.3, 140.2, 169.4) + "you can see" at 79.7. **2 in the first 30 s**. About **one every 19 s** | Hindi words |
| Screen-proof "show" moments | ≈ 14 (each grid, sort, date, view count, likes/comments, durations and title shown while being talked about) | Frames |
| Speech rate | Hindi ASR: **210 wpm** (0–30 s), **201 wpm** (0–60 s), 202 wpm (0–169 s). EN translation: 192 / 183 / 188 wpm | Word timestamps |
| Pauses | silencedetect (−35 dB, ≥0.35 s): **1 in the first 60 s** (21.42 s, 0.37 s), 4 in 192 s. Word gaps ≥0.25 s: only 2, both where other audio plays (meme 137.8, sample 169.7) | silences.csv, words |
| Address | Hindi "aap" (you) **14** vs "main/mujhe" (I) 4 + "hum" (we) 4. EN: you/your 14 vs I/me/we 6, so **~2.3 : 1 second person**. "Bhai" (brother) ×2 (15.8 s, 135 s) | Words |
| Rhetorical questions | **3 explicit** (1.6 s niche?; 20.9 s guess the niche?; 127.6 s why do they all make content?) + 1 implicit (the read-out title). Answered after **6.7 s / 2.3 s / ≈ 4 s** | Words |
| Hard edit cuts | 6 in 0–12.45 s (ASL 2.1 s). After that, cuts only for page changes, inserts and the meme | cuts.csv + frames |
| Longest fully frozen frame | **3.74 s** (111.9–115.7, red box on the title). Other long holds: 3.3 s (72.7–76.0 comments), 3.1 s (17.1–20.2 header). The 6 s low-motion run at 170.5–176.5 is the inset sample (limited animation) | scdet_scores (thr 0.05 / 0.5) |
| Zoom / punch-in events | ≈ 8 in 192 s (16.5, 31–34 slow push, 35, 81.5, 95, 109–111, 128–131 tilt, 140). **Each one lands on a number or a title** | scdet + frames |

### Tone markers

- Constant second-person imperatives ("look", "calculate it yourself", "open any video").
- Peer address ("brother").
- Mind-reading flattery at 0:05.
- Absolutes, e.g. the niche whose RPM never drops at 0:09–0:12.
- Reassurance close ("no tension, sit comfortably").

---

## 3. VISUAL HOOK

### Opening frames and the thumbnail

- **First frame (0:00.0):** a motion-blurred close-up of Po (Kung Fu Panda). It is inset at ~60 % width with black side bars, used as a reaction GIF for "let me ask you a question".
  - It does **not** match the thumbnail.
  - Its only job is pattern interrupt plus humour.
  - It is copyrighted footage: a production system should replace it (see rules).
- **First visual change:** 1.57 s (hard cut). Then cuts at 3.34, 7.0, 8.07, 9.2 and 12.45 s.
- **Thumbnail match:** the thumbnail (1280×720) contains:
  - giant "FINANCE NICHE" in yellow-orange + white;
  - a red "FULL COURSE" tag;
  - four Nick-Invests-style cartoon thumbnails: "THE FIRST $1K HURTS", "WHAT PEOPLE REALLY HAVE", "$900 A MONTH?!" and "THE $20,000 RULE";
  - ChatGPT + CapCut logos with a "189K VIEWS ↑" card;
  - a pile of cash on a teal background.
- **The video pays the thumbnail off by 0:09.2:**
  - The headline words appear as the full-screen card at **0:08.07**.
  - Three of the four thumbnails are visible on the real Nick Invests grid at **0:09.2–0:12.4**.
  - "THE FIRST $1K HURTS" appears in the grid at ~2:00.
  - "FULL COURSE" is paid off by the chapter list and the 2:34 promise.
  - The "189K VIEWS" card is never literally shown; the intro shows 954K and 668K instead.

### Kinetic text and title cards

- **3.5–4.4 s:** grey→black word-by-word fade on white, karaoke-synced to the narration.
- **8.07–9.2 s:** "Finance Niche" white on black, rotating in from ≈ −35° in 0.3 s, plus a probable sub-bass impact SFX.
- **3:09.7–3:11.6:** "100K Subscribers" in heavy rounded sans, bright green **#3efd02**, centered over a darkened screen recording.

### Highlighting language

There is no custom overlay graphic for numbers. The editor uses the **browser's native blue text selection (#1c73f8)** as a highlighter, synchronised with the spoken number (17.1, 18.8, 39.0, 57.5, 82, 84.6, 97 s). For the "look at this specific item" moments he uses a **red rectangle (#f6272b, ~3 px)** around a card (1:51–1:55, 2:21, 2:22). A **red click-ring** shows on the cursor.

- vidIQ overlays (VPH, outlier score, "Monetized") are left on screen as **third-party authority badges**.
- No on-screen calculator is used for $3,340. The money result is carried by voice alone, with 668K selected.

### Zooms

- **Punch-ins happen ~0.5 s before the number is spoken.** For example, the zoom starts at 16.5 and "24" is spoken at 17.12; the zoom starts at 81.5 and "184" is spoken at 82.04.
- Zooms are held while the number(s) are spoken and released within ~1 s after.
- Variants: slow push-ins (31–34 s), 3-D tilt (2:08–2:11), whip/zoom-blur transitions (1:38, 2:15 in, 2:18 out).

### Inserted clips

| Time | Insert |
|---|---|
| 0:00–0:01.6 | Po reaction clip |
| 0:01.6–0:03.3 | AI-generated "room of screens" |
| 0:05–0:07 | Stock "telepathy" image card |
| 0:53.1–0:54.5 | 1.3 s in-browser glimpse of the competitor video |
| 1:09–1:10 | Buffett video playing |
| 2:15.4–2:18.9 | WWE "money" meme with its audio |
| 2:47–3:03 | Competitor video playing with its English narration, including an 8.7 s inset on black |
| 3:04–3:06 | Animated subscribe-button card |
| 3:09.7–3:11.6 | "100K Subscribers" card |

### Music and SFX hints

These are measurement-based; I did not listen to the audio.

- The narration is continuous, with a median speech level of −23 dBFS. Whole-file integrated loudness is −19.4 LUFS with LRA 2.8 LU, i.e. heavily compressed and flat.
- Between words the 50 ms floor drops to −54 to −65 dBFS (1st percentile). That suggests **no continuous music bed** under the VO, or a very quiet one.
- The 0–13 s floor is slightly higher (p1 −53.6 vs −61…−65 later), so a faint bed or whooshes in the opening 13 s are possible (low confidence).
- A sub-bass burst (30–90 Hz, +10–15 dB) at 8.75–9.5 s coincides with the "Finance Niche" card and is probably an impact SFX.
- The meme (2:16) and the sample clip (2:50) bring their **own audio** while the host stops talking.

---

## 4. RETENTION READ (heatmap 0–192 s)

`heatmap.json` is YouTube's **"most replayed"** curve: relative replay/seek density, normalised to the video's maximum (686–700 s = 1.0). **It is not an audience-retention curve.** Absolute drop-off in the intro cannot be measured from this pack.

| Bucket (s) | Value | What is on screen |
|---|---|---|
| 0–13.7 | 0.051 | Hook |
| 13.7–27.4 | 0.034 | Proof channel #1 numbers |
| 27.4–41.2 | **0.024** (3rd-lowest of all 100 buckets) | Recency, 668K |
| 41.2–54.9 | 0.043 | Money-math set-up |
| 54.9–68.6 | 0.083 | $3,340, "not fake" |
| 68.6–82.3 | 0.107 | Likes/comments, Nick Invests |
| 82.3–96.0 | 0.117 | 184 videos / 155K / ~1M |
| 96.0–109.8 | 0.042 | Evergreen, "not that simple" |
| 109.8–123.5 | 0.037 | Title deconstruction |
| **123.5–137.2** | **0.248** | Why channels exist → **money** → meme starts |
| **137.2–150.9** | **0.243** | Meme → 52/44 min → more ads = more money |
| 150.9–164.6 | 0.038 | Promise + open loop |
| 164.6–178.4 | 0.047 | Reassurance + sample clip |
| **178.4–192.1** | **0.255** | Subscribe CTA + **3:12 chapter landing point** (192.0 falls in this bucket) |

Video median = 0.206 and mean = 0.239. The intro averages 0.10.

### Reading

1. **The hook and proof stretch (0–55 s) is watched once and never revisited** (0.024–0.051, among the lowest buckets of the whole video). That is expected: a hook's job is to be consumed once, and replays concentrate on the copy-the-prompt steps (Script→Voice peak = 1.0).
2. **The money-motive stretch is the only part of the intro that is replayed above the video median** (0.24–0.25, about 5–10× the hook buckets). This covers 2:03–2:31: "why do they make content? money", the meme, then "52/44 minutes, so more ads, so more money". For this audience the **money logic is the most re-watched idea in the intro**. Possible explanations: people re-watching to show others, people re-checking the ad logic, or scrubbing viewers stopping on the full-screen meme, which is the most visually distinct frame in the intro.
3. **The 178–192 s spike (0.255) contains the chapter-2 landing time (192.0 s).** It is very likely **chapter-skippers** jumping to "Channel Setup" plus returners re-entering at the step-by-step part. The chapter list is what makes a 3-minute intro survivable: impatient viewers have an exit that keeps them in the video.
4. Moderate rise at 55–96 s (0.08–0.12), where the numbers are densest ($3,340, likes/comments, 184/155K/~1M). Viewers go back to re-check figures.

### What the intro does to hold people through 3:12

- **It answers in 8 s.** The niche (the thumbnail headline) is named, so nobody is left wondering whether this is the right video.
- **Proof density:** a new number about every 11 s on average (17 in 192 s), each visually marked.
- **Escalation by contrast:**
  - small channel (24 videos → 46K) before big channel (184 → 155K);
  - views (668K) before dollars ($3,340);
  - "2 months old" before "viral 2 weeks ago".
- **It kills the doubt that would make viewers leave** ("fake views") at 1:04, before it can form.
- **It teaches a mini-insight before the tutorial:** the title deconstruction gives intro-watchers a reward even before the steps start.
- **Pattern interrupts** at 0:00, 0:08 (title card + SFX), 2:15 (meme) and 3:09 (green full-screen card).
- **Open loops:**
  - "not as simple as they look" (1:45) → decoded later;
  - "a video on the first channel is coming" (2:39). Two comments explicitly ask for that Legend Investor Mindset video, so the loop was remembered.
- **Reassurance + an instruction to watch carefully** right before the long build, then **9 s of the target output** so viewers know exactly what they will be able to make.
- **Continuous narration:** effectively zero dead air, at ~200 wpm.

---

## 5. REUSABLE HOOK TEMPLATE

All numbers in brackets must be pulled live from the real channels (YouTube Data API / vidIQ / Social Blade). **Never invent stats.**

### 5A. "How to make videos like {SUCCESS_CHANNEL}": faithful version (≈ 3:10, as AI Flow did it)

| Beat | Time (s) | Script slot | Visual |
|---|---|---|---|
| B0 Question frame | 0.0–1.6 | "Let me ask you something." | 1–1.6 s reaction clip (own or licensed / AI-generated), inset or full, blur-in |
| B1 The question | 1.6–5.0 | "Which kind of YouTube channel always {BENEFIT: earns high RPM / gets watched to the end / …}?" | Metaphor image (AI-generated) 1.5–2 s → kinetic keyword text, word-by-word, synced to the words |
| B2 Mind-read | 5.0–7.0 | "Yep, you guessed it." | Image card fade-in (0.3 s) |
| B3 Answer card | 7.0–9.2 | "It's the **{NICHE}** niche." | 1 s screen flash of {SUCCESS_CHANNEL} grid → **full-screen title card = the thumbnail's headline words**, spin/scale-in 0.3 s + impact SFX |
| B4 Authority claim | 9.2–12.5 | "{ABSOLUTE CLAIM about the niche}" | {SUCCESS_CHANNEL} *Popular* grid (thumbnails visible in your own thumbnail). Highlight the top view count at ~11.5 s |
| B5 Proof channel #1 (small / new) | 12.5–20.5 | "First, look at {SMALL_CHANNEL}: only [N] videos, [X] subscribers." | Punch-in 0.5 s before the first number; select/highlight each number on its word; zoom out after |
| B6 Micro-question | 20.5–24.5 | "Guess what it's about? I'll tell you: {NICHE}." | Static or slow push (≤ 3.5 s) |
| B7 Recency + virality | 24.5–44 | "Its first video is only [2 months] old… its top video blew up [2 weeks] ago… [668K] views." | Sort Oldest → dates. Sort Popular → highlight views + date |
| B8 Money math | 44–60 | "Do the math: {NICHE} RPM is [$a–$b]. Take just the minimum [$a] → this one video ≈ **[$Y]**." | Grid scroll. Re-highlight the view count on the result line. Optional: a 1–2 s glimpse of the video |
| B9 Anti-objection | 60–78 | "And no, these aren't fake views. Open any video: [likes], [comments], real people." | Open the video; likes; scroll the comment list (≥ 3 s) |
| B10 Proof channel #2 = {SUCCESS_CHANNEL} | 78–105 | "Now {SUCCESS_CHANNEL}: [N] videos, [X] subs; its top video, [5 months] old, has ~[1M] views, and it still gets views every hour." | Punch-in + highlight N and X; VPH/outlier badges |
| B11 Format deconstruction | 105–128 | "Look at this title: '{TITLE}'. I want to click just reading it, because {curiosity gap}. Relatable + FOMO = viral." | Punch-in + red box around one card; freeze ≤ 4 s while reading it |
| B12 Money motive + interrupt | 128–151 | "Why do all these channels exist? Money." [meme 2–4 s with its sound] "Look at the lengths: [52] min, [44] min. Longer = more ads = more money." | Tilt-zoom on the grid → full-screen meme (licensed/own) → red boxes on the durations |
| B13 Explicit promise | 151–160 | "So in this video I'll show you how to make videos exactly like {SUCCESS_CHANNEL}." | Long abundance scroll of the success grid |
| B14 Open loop + reassurance | 160–169 | "{SMALL_CHANNEL} gets its own video soon. No stress, this is easy to follow; get comfortable." | Back to channel #1 → open a {SUCCESS_CHANNEL} video |
| B15 Taste of output | 169–178 | (silence; the target-style clip plays with its own audio, 8–10 s) | Inset on black or full screen |
| B16 Goal CTA | 178–192 | "Quick thing: subscribe, we're racing to [100K] by [year]." | Channel page with a progress banner → animated subscribe click → full-screen goal card → **chapter 2 timestamp at the end of this beat** |

### 5B. Compressed version (recommended default for an automated system, ≈ 75–90 s)

The faithful order is kept, but each beat is shortened:

| Beat | Time (s) |
|---|---|
| B0 Question frame | 0–1.5 |
| B1 The question | 1.5–4.5 |
| B2 Mind-read | 4.5–6 |
| B3 Answer card | 6–8.5 |
| B4 Authority claim | 8.5–11 |
| B5 Proof channel #1 | 11–18 |
| B7 Recency + virality | 18–28 |
| B8 Money math | 28–40 |
| B9 Anti-objection | 40–48 |
| B10 Proof channel #2 | 48–60 |
| B11 Format deconstruction | 60–70 |
| B12 Money motive | 70–78 (meme ≤ 2.5 s) |
| B13 Explicit promise | **78–83** |
| B14 + B15 Open loop, reassurance, taste of output | 83–92 (sample 6 s) |
| B16 Goal CTA | 92–100 → chapter 2 |

B6 (micro-question) is dropped. Use this when the topic is not money-motivated, or when your own retention data shows drop-off before the promise.

### 5C. Generic variant (any tutorial / explainer)

| Slot | Time | Content |
|---|---|---|
| Q | 0–2 s | Ask the viewer a question whose answer is the topic |
| Q + keyword | 2–5 s | Kinetic keyword text |
| "You guessed it" | 5–7 s | Validation beat |
| Answer card = thumbnail words | 7–9 s | Full-screen card |
| Proof #1 (ordinary person/case, small input → big result) | 9–20 s | Highlight 2 numbers on their words |
| Proof #2 (the famous example) | 20–35 s | Two numbers |
| Value math (time / money / grades / followers saved or gained) | 35–45 s | Use the minimum case |
| Objection kill ("isn't this fake / too hard / too expensive?") | 45–55 s | Show the evidence |
| Mechanism teaser (why the famous example works, named in 1–2 psychology words) | 55–65 s | — |
| Explicit promise ("In this video you'll learn to…") | 65–72 s | — |
| Reassurance | 72–76 s | — |
| 5–8 s preview of the end result | 76–84 s | — |
| CTA | ≤ 10 s | Then chapter 1 |

### 5D. Six example hooks for other niches (original wording; bracketed values are placeholders to fill with live data)

**1. Stickman explainer channel ("How to make videos like {StickmanChannel}")**

- 0.0: *"Quick question."* (reaction clip)
- 1.5: *"What kind of video can a stick figure with no face turn into a million views?"* (kinetic: "STICK FIGURE · MILLION VIEWS")
- 5.0: *"Yeah, you already know."*
- 7.0: Card **"STICKMAN EXPLAINERS"** + hit.
- 9.0: *"They're the cheapest animation on YouTube and still some of the most-watched."* (grid; highlight [2.3M])
- 12.5: *"Look at this channel: only [19] uploads, [240K] subscribers."* (punch-in, highlight 19 → 240K)
- 20.0: *"And its first upload? Just [3] months ago."*

**2. History documentary channel**

- 0.0: *"Let me ask you something."*
- 1.5: *"What do millions of people happily watch for a full hour before bed?"* (kinetic: "1 HOUR · EVERY NIGHT")
- 5.0: *"Exactly."*
- 7.0: Card **"HISTORY DOCUMENTARIES"** + hit.
- 9.0: *"Long runtime means more ad breaks, and history never goes out of date."* (grid; highlight a [58:12] duration)
- 12.5: *"This channel posted just [11] videos and sits at [96K] subscribers."*
- 20.0: *"Its biggest one, [3] months old, still pulls views every hour."*

**3. Psychology / human-behaviour channel**

- 0.0: *"One question."*
- 1.5: *"Why does a ten-minute video about one tiny mental bias beat most celebrity interviews?"* (kinetic: "ONE BIAS · MILLIONS")
- 5.0: *"You're thinking the same thing I am."*
- 7.0: Card **"PSYCHOLOGY NICHE"** + hit.
- 9.0: *"Everyone wants to understand themselves; the audience never runs out."*
- 12.5: *"Look: [27] videos, [310K] subscribers, all faceless."*
- 20.0: *"And this video right here: [890K] views in [6] weeks."*

**4. Sleep-story / relaxation long-form channel**

- 0.0: *"Quick question for you."*
- 1.5: *"Which videos keep earning ads while the viewer is fast asleep?"* (kinetic: "ASLEEP · STILL EARNING")
- 5.0: *"Yep, those ones."*
- 7.0: Card **"SLEEP STORIES"** + hit.
- 9.0: *"Three-hour runtimes, and people replay them every single night."*
- 12.5: *"This channel: [14] uploads, [130K] subscribers."*
- 20.0: *"Watch-time math: at a minimum of [$3] RPM, this one video ≈ [$X]."*

**5. Mystery / unsolved-case documentary channel**

- 0.0: *"Let me ask you."*
- 1.5: *"What makes someone click a 40-minute video at 2 a.m. and stay to the last second?"* (kinetic: "2 A.M. · LAST SECOND")
- 5.0: *"You guessed it."*
- 7.0: Card **"UNSOLVED MYSTERIES"** + hit.
- 9.0: *"An open question is the strongest hook there is."*
- 12.5: *"This channel has only [22] videos and [175K] subscribers."*
- 20.0: *"Some will say these views are bought. Open any video and read the comments."*

**6. Generic software tutorial (non-YouTube niche)**

- 0.0: *"Quick question."*
- 1.5: *"Why do some freelancers charge [5×] more for the same dashboard?"* (kinetic: "SAME DASHBOARD · 5× PRICE")
- 5.0: *"Right, it's how it looks."*
- 7.0: Card **"PRO-LEVEL EXCEL DASHBOARDS"** + hit.
- 9.0: *"This one dashboard got [1,200] saves on LinkedIn."*
- 12.5: *"Its creator posted only [9] of them and now books clients [2] months out."*
- ~70: *"By the end of this video you'll build this exact dashboard, step by step."*

---

## 6. Why it works (hypotheses tied to evidence)

1. **The intro matches buyer intent, not curiosity intent.**
   - The searcher wants to start a faceless finance channel. Before spending 20 minutes, they need to know the niche pays and the model is real.
   - So the intro is a due-diligence package: two channels, 17 numbers, money math, an anti-fake check, and the revenue mechanism (length → ads).
   - Heatmap: the money-logic stretch (2:03–2:31) is the only intro segment replayed above the video median (0.24–0.25 vs 0.21).
2. **The thumbnail promise is redeemed within 9 s.** The thumbnail's headline "FINANCE NICHE" and three of its four cartoon thumbnails appear on screen at 0:08–0:12, which lowers bounce anxiety. The first frame is a meme, so the first 8 s run purely on the question → answer loop.
3. **Every claim is shown, not told.** Numbers are spoken and simultaneously selected or boxed (11 highlights). Third-party badges (vidIQ "Monetized", VPH, outlier ×) do the authority work, so the host never needs to show his face.
4. **Small → big sequencing makes the dream feel reachable.**
   - The first case is a 2-month-old, 24-video channel with 46K subs. "Someone like me could do this."
   - Only then comes the aspirational title channel (184 videos, 155K, ~1M-view video).
   - Recency ("2 weeks ago", "every hour") adds FOMO: the opportunity is happening now.
5. **Objections are pre-empted:**
   - fake views (1:04);
   - "it looks too simple / I can't do it" (1:45, the "not as simple as it looks" line becomes the reason to watch);
   - "too long / boring" (2:43 reassurance).
6. **Peer register plus speed.** Second person ~2.3:1 over first person, "brother", continuous ~200 wpm Hinglish/Urdu narration, almost no dead air. It feels like a friend explaining fast.
7. **Escape hatch.** Chapters let impatient viewers skip to 3:12. The 178–192 s heatmap bump (0.255) sits on that landing point, so the long intro does not cost those viewers.
8. **Proven format on this channel.**
   - Channel median ≈ 7,250 views over 84 uploads with public counts; this video is ≈ 20× that.
   - The channel's other top videos are the same pattern: "How To Make Videos Like {channel}" (196K) and "High RPM Finance" (146K).
   - Comments ask for the second-channel video (2 comments) and praise the visual decoding ("I've watched ~10 videos and none could make Nick-Invests-like visuals"). Both are signs the intro's framing was absorbed.

---

## 7. Rules to copy

1. **Speak a direct question to the viewer within the first 2.0 s.** Preface it with "Let me ask you…" and make its answer the video's niche or topic.
2. **Name the answer on a full-screen title card by 0:09 at the latest** (measured 8.07 s). The card text must be identical to the biggest words in the thumbnail; animate it in ≤ 0.3 s with an impact SFX.
3. **Show at least 2 of the thumbnail's visual elements on screen by 0:12** (measured 9.2 s: the exact competitor thumbnails).
4. **Make 5–6 hard cuts in the first 12.5 s (average shot ≤ 2.2 s).** Then switch to continuous screen recording, where change comes from cursor, selection, zoom and scroll.
5. **Never let the frame stay fully frozen > 4.0 s in the intro** (max measured 3.7 s). Produce a visible event (cursor move, hover preview, selection, scroll, zoom) every 1.5–4 s; target ≥ 18 visual events in the first 30 s.
6. **Show the first number on screen by 0:10 and highlight it by 0:12. Speak the first proof number by 0:18.**
7. **Punch in (1.3–2×) 0.3–0.6 s before a number is spoken.** Highlight the number within ±0.5 s of its spoken word; zoom out ≤ 1 s after the last number of the sentence.
8. **State ≥ 8 distinct numbers in the first 60 s and ≥ 15 in the whole intro.** Visually mark ≥ 10 of them (selection highlight or red box).
9. **Use two proof cases in this order:** a small/new example ("only N videos → X subs, first upload N months ago"), then the famous example named in the title.
10. **Do the money (value) math with the minimum of the range.** Say the result as its own sentence of ≤ 2 s, and re-highlight the source number while saying it.
11. **Answer every rhetorical question within 2–7 s.** Use ≥ 3 rhetorical questions in a 3-minute intro (≥ 2 in the first 30 s).
12. **Handle the #1 doubt (fake / too hard / too expensive) before 1:20** with on-screen evidence: likes, comment count, a ≥ 3 s comment scroll.
13. **Deconstruct one title from the success channel:** read it aloud, box it in red, and name the psychology in ≤ 3 words ("curiosity", "relatable", "FOMO").
14. **Insert exactly one full-screen meme / pattern interrupt of 2–4 s in the second half of the intro, with its own sound.** It must be licensed, original or AI-generated: **never copyrighted film/TV/WWE footage**.
15. **Give the explicit promise ("in this video I'll teach you to make videos like {SUCCESS_CHANNEL}") by 2:35 in the faithful format, by 1:25 in the compressed format.** Repeat the success channel's name in it.
16. **Open one loop for a future video** (e.g. "the first channel gets its own video") within 10 s after the promise.
17. **Play 6–10 s of the target output with its own audio before chapter 2,** with the host silent.
18. **Keep the narration continuous:** ≤ 1 pause ≥ 0.35 s per minute, and no word gap ≥ 0.25 s except under inserted audio. Target 180–200 English wpm (≈ 200 Hindi-ASR wpm).
19. **Address the viewer as "you" at least 2× as often as "I/we".** Use one "look at this" pointer every 15–20 s, each tied to a specific on-screen element the cursor is touching.
20. **Close the intro with a ≤ 15 s subscribe CTA framed as a public goal** (progress banner + animated subscribe click + one full-screen goal card). Set chapter 2's timestamp exactly at the end of the CTA so skippers land on the first step.
21. **Name the intro chapter something that discourages skipping** ("Important") and keep the intro ≤ 14 % of the runtime (measured 192 / 1372 s = 14 %).

---

## 8. Open questions / low-confidence

- **True retention is unknown.** `heatmap.json` is "most replayed" (relative replays), not audience retention. Low intro values mean "not re-watched", not "abandoned". The 178–192 s spike is *inferred* to be chapter-skip landings, because 192.0 s falls inside that bucket.
- **SFX/music:** the 8.75–9.5 s sub-bass burst is inferred from spectrum, not heard. A faint bed in 0–13 s is possible (slightly higher noise floor), and the whooshes on the blur transitions (1:38, 2:15, 2:18) could not be confirmed. Nobody listened to the audio.
- **Zoom factors (1.3–2×)** are visual estimates from frame comparison, not pixel-measured.
- **Speech rate:** the Hindi/Urdu ASR word count depends on Whisper tokenisation. The English-translation wpm (183–192) is the safer comparison number for English scripts.
- **The 2:34 promise is late by general YouTube norms.** Whether a compressed (≈ 80 s) intro would retain better for this audience cannot be tested from this data. A/B it.
- **Copyright exposure:** the intro uses Kung Fu Panda and WWE clips plus a long stretch of a competitor's video and audio (2:47–3:03). This apparently did not hurt this upload, but a production system must not replicate it.
- **The lead magnet (PDF prompts) is not mentioned in the intro** (first mention is after 3:12). Yet "pdf" appears in 26 of 133 comments and "prompt" in 21. Whether teasing the PDF in the intro would raise retention or comments is untested.
- **Thumbnail "189K VIEWS" card:** it does not match any number shown in the intro; its source is unverified.
