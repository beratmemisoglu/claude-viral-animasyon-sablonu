# 01 — Packaging, CTR and why it won

Video: "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)" (SRjm9tvMHhs). AI Flow (@AIFlowOfficial). Uploaded 2026-03-09. Runtime 22:52. 144,518 views, 4,498 likes and 133 comments as of 2026-10-22, 227 days after upload.

Analyst #1 of 8 (packaging, CTR, outlier analysis). Evidence used: the info.json, the thumbnail (raw\v.webp, measured with PIL), comments.json, heatmap.json, channel_videos.tsv, the full English translation of the transcript, 1 fps frames plus ffmpeg full-resolution crops, one yt-dlp channel-metadata call, and one read-only load of the public channel "Videos" page in a browser (cookies rejected) to fill the view counts that the TSV had as NA.

---

## Summary (10 bullets)

1. **This is a 10.3× outlier for the channel.** The channel median is 14,000 views over 107 other uploads, and the video ranks 8th of 108. Against tougher baselines the multiple is 6.6× (median of the last 12 months, 22K) and 4.8× (the ±10 neighbouring uploads, 30K). It is not the channel's #1: that is "AI Survival ASMR" at 278K.
2. **The subscriber count of 509 in the metadata is a parsing error.** A yt-dlp channel call returned `channel_follower_count = 50900`, and the live channel header reads "50.9k subscribers • 108 videos". The yt-dlp watch-page parse dropped the decimal in "50.9K". In the video itself (03:04 and 21:35) the channel had about 30–31K subscribers, with a banner reading "TARGET: 100K SUBS BEFORE 2027".
3. **The biggest structural factor is distribution, not packaging.** The video is a **YouTube Collaboration post with 4 creators**: `creators = AI Flow, Oriva AI, AI Man, Ai Dadaji`. Every one of the 24 "NA" rows in channel_videos.tsv is a collab post. Over the last ~10 months, collab posts have a median of 47K views against 8K for solo posts (5.9×). 7 of the channel's top 10 videos are collabs.
4. **The second factor is a proven topic franchise.** Finance is the channel's best topic (median 45K across n=11, versus 14K for the channel). This video is the third large finance tutorial, after "How I Create High RPM Finance Videos Using ONLY AI" (146K) and the finance "Part 2" (230K). Its thumbnail reuses the exact "FINANCE NICHE / FULL COURSE" label of the 230K hit.
5. **Title formula: `How To Make Videos Like {Named Channel} With AI ({Money qualifier} {Niche} Niche)`.** The channel's two biggest "Like X" titles share this skeleton: Yellow Dude (196K) and this one (144.5K). Both use a plain name (no @), no pipe tail, and a parenthetical niche or money qualifier. "Like X" titles with a "| YouTube Automation…" tail have a median of 17K, against 52.5K without the tail.
6. **The thumbnail is the channel's house template.** It has a giant two-word label (yellow topic word plus white "NICHE"), a red "FULL COURSE" pill, a white analytics-style proof panel (ChatGPT and CapCut logos plus "189K VIEWS ↑"), a pile of banknotes, a dark teal radial background, and 4 example thumbnails behind everything. The "189K VIEWS" figure is recycled: the same number appears on at least two other AI Flow thumbnails (seen at 21:47), so it is decoration, not a real stat.
7. **The money promise is front-loaded and repeated.** The parenthetical "High RPM" appears in the title, the thumbnail has a money pile, and the intro does RPM arithmetic ($5–15 RPM, about $3,340 from one 668K-view video, 00:45–00:57) and argues that longer videos carry more ads (02:18–02:28).
8. **The replay peaks sit on readable artefacts.** The global peak (11:26–11:39) is the finished, structured script being pasted and scrolled in Google Docs. Further peaks: the Grok image-to-talking-video moment (15:19–15:46, up to 0.85), the topic-pattern prompt (07:05–07:19, 0.45), and CapCut animation and captions (18:03–18:17, 0.53). The prompts were gated behind a PDF that many viewers never received, so the screen was the only way to copy them.
9. **About a third of comments ask for the prompts.** 44 of 132 viewer comments (33%) ask for the PDF, prompts or file. A "200 Likes" target was shown at 21:44 and the PDF was promised on Telegram and WhatsApp. Likes reached 4,498 (3.1% of views), yet viewers still complain the link never came. The audience is South-Asian aspiring creators: about 52% romanised Hindi/Urdu, about 42% English (many one-word asks), and 3% Devanagari. At least 12 commenters already run finance-named channels.
10. **Hidden reach multipliers.** The video has an **auto-dubbed English (US) audio track** alongside the Hindi original (confirmed in the formats). It is a long "full course" (median views rise steadily with duration on this channel). The description is SEO-heavy: 564 words, 19 URLs, and a 20-line "Queries People Ask" keyword block naming competitor channels. The pinned comment is still being re-edited months later to route traffic to newer videos.

---

## 1. Title

### 1.1 Anatomy

| Element | Text | Chars | Job | Evidence |
|---|---|---|---|---|
| Search stem | `How To Make Videos Like` | 23 | Matches the dominant query shape for aspiring creators ("how to make videos like X"). Five of the 15 tags are variants of it. | Tags: `how to create videos like nick invest`, `how to make a channel like nick invests`, … |
| Borrowed authority / entity | `Nick Invests` | 12 | Names a real, fast-growing finance-animation channel. On screen at 01:20–01:35 it has 155K subscribers, 184 videos, and a ~1M-view video 5 months old. This gives search capture for the channel name, adjacency in suggested and browse for that channel's audience, and "this is already proven" credibility. | Video 01:20–01:41; description repeats the name 3× in prose and 7× in total |
| Ease / means promise | `With AI` | 7 | Signals low skill and low cost. The video backs it with free tools (Claude free plan 10:18, Google AI Studio "totally free" 11:45, Whisk, Grok). | Transcript 10:18, 11:45 |
| Parenthetical money and niche qualifier | `(High RPM Finance Niche)` | 24 | "High RPM" is creator-economy jargon for "pays more per view". "Finance Niche" is the category label and is repeated as the thumbnail headline. The parenthetical can be cut off on mobile without losing the core promise, because the thumbnail repeats it. | Thumbnail headline "FINANCE NICHE"; intro RPM math 00:45–00:57 |

- **Length:** 69 characters and 13 words. The median for the channel's top 15 is 69 characters; for the rest it is 74.
- **Case:** Title Case; only "RPM" is in caps. No numbers, emoji, pipe or year.
- **Front-loading:** the named entity ends at character 35, so it survives every truncation.
- **No direct hype words** ("viral", "insane", "secret"). The money hook sits in the qualifier.
- **Title and thumbnail split the work.** The title carries the entity ("Nick Invests") and the method ("With AI"). The thumbnail carries category, completeness, proof and an outcome preview. They overlap only on "Finance Niche", and the thumbnail never writes the channel name: it shows the channel's visual style instead (section 2).

### 1.2 Sister titles that share the skeleton (strongest evidence)

| Title | Views | Collab | Duration |
|---|---|---|---|
| How To Make Videos Like Yellow Dude (USA Fitness Faceless Channel Reveal) | 196K | solo | 12:34 |
| **How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)** | **144.5K** | 4 creators | 22:52 |
| How to Make Viral AI Movies Like @MYTHRA | 117K | 3 creators | 17:56 |
| How to Make Videos Like @time4growth Using Only FREE AI Tools \| Youtube Automation Tutorial | 73K | solo | 14:40 |
| How to Make 3d Videos like Zack D Films with AI (Full Guide) | 60K | solo | 11:48 |

The winning variant uses a **plain channel name (no "@")**, **no "| keyword tail"**, and **one parenthetical** that names the niche and its money or geography angle ("USA Fitness Faceless", "High RPM Finance").

### 1.3 The channel's winning title patterns (derived from its top 15)

1. **Named model channel:** "How To Make Videos Like {X}" with a money or niche parenthetical (196K, 144.5K, 117K, 73K, 60K).
2. **Named channel plus an insider sacrifice:** "I Bought {X}'s Paid Course So You Don't Have To" (168K).
3. **First-person build with a format noun:** "How I Create Viral AI {Format} Videos from Scratch (Free Tools)" (264K), "How I Create High RPM Finance Videos Using ONLY AI" (146K), "…VIRAL Roblox Videos Using Only AI (Full Step-by-Step Guide)" (75K).
4. **New-niche urgency:** "How to Make AI {Format} Videos in {Year} – New Viral Niche Exploding Right Now (Full Tutorial)" (278K).
5. **Big-outcome tutorial or series:** "How To Create Viral {Niche} Videos With AI That Get Millions of Views (Step-by-Step) | Part 2" (230K).
6. **Clone-any:** "Clone Any YouTube Channel with Claude AI (No Coding, 100% Free)" (159K).
7. **Tool trick (era-dependent):** "How to Make Long YouTube Videos Using Grok AI | Secret Trick…" (95K), "Stop Using Sora 2 & Veo 3! Grok Now Makes Long Videos…" (77K).

Common DNA across these: a concrete **entity** (channel, format or tool), **"AI"**, a **low-effort qualifier** ("Only AI", "Free Tools", "No Coding", "Zero Experience?"), and an implied **money or virality outcome**. Weak patterns are niche lists (median 3.2K), news about tools or policy (6.1K), and "this channel got N views" case studies (5.2K).

### 1.4 25 title templates (proven formula, ready to fill)

Slots:
- `{SUCCESS_CHANNEL}`: a real channel that is growing now, written without "@".
- `{NICHE}`: Finance, Health, History, Psychology, Fitness…
- `{MONEY_QUALIFIER}`: High RPM, High CPM, USA Audience, Evergreen, Monetizable…
- `{FORMAT}`: 2D Animated, Stickman, Whiteboard, Documentary…
- `{TOOL}`, `{GEO}`, `{N}`, `{YEAR}`.

Keep each title at ≤ 75 characters. Keep the entity within the first 40 characters. Use exactly one parenthetical.

1. How To Make Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER} {NICHE} Niche)
2. How To Make Videos Like {SUCCESS_CHANNEL} ({GEO} {NICHE} Faceless Channel Reveal)
3. How To Make {NICHE} Videos Like {SUCCESS_CHANNEL} With AI (Full Course)
4. How I Make Videos Like {SUCCESS_CHANNEL} Using Only AI ({MONEY_QUALIFIER} Niche)
5. How To Make {FORMAT} Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER})
6. I Bought {SUCCESS_CHANNEL}'s Paid Course So You Don't Have To
7. How I Create {MONEY_QUALIFIER} {NICHE} Videos Using ONLY AI
8. How To Make Videos Like {SUCCESS_CHANNEL} With FREE AI Tools ({NICHE} Niche)
9. Zero Experience? How To Make Videos Like {SUCCESS_CHANNEL} With AI
10. How To Make Videos Like {SUCCESS_CHANNEL} With AI (Evergreen {NICHE} Niche)
11. How To Make Videos Like {SUCCESS_CHANNEL} With AI (Part 2: {STEP})
12. How To Make Videos Like {SUCCESS_CHANNEL} With {TOOL} ({MONEY_QUALIFIER} {NICHE} Niche)
13. How To Start a {NICHE} Channel Like {SUCCESS_CHANNEL} With AI (Full Course)
14. How I Built a {NICHE} Channel Like {SUCCESS_CHANNEL} Using Only AI
15. How To Make {NICHE} Videos Like {SUCCESS_CHANNEL} in {YEAR} ({MONEY_QUALIFIER})
16. {NICHE} Videos Like {SUCCESS_CHANNEL} Are Blowing Up – Here's How To Make Them With AI
17. How To Make Videos Like {SUCCESS_CHANNEL} With AI (New {MONEY_QUALIFIER} Niche)
18. How To Make Long {NICHE} Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER})
19. How To Make Videos Like {SUCCESS_CHANNEL} and {SUCCESS_CHANNEL_2} With AI ({NICHE} Niche)
20. How To Make Videos Like {SUCCESS_CHANNEL} With AI ({GEO} Audience, {MONEY_QUALIFIER})
21. How To Make Videos Like {SUCCESS_CHANNEL} With AI (No Editing Skills Needed)
22. How I Recreate the {SUCCESS_CHANNEL} Style With AI ({NICHE} Niche Full Course)
23. How To Make {FORMAT} {NICHE} Videos Like {SUCCESS_CHANNEL} (100% FREE AI)
24. How To Make Videos Like {SUCCESS_CHANNEL} With AI ({N} Videos, {MONEY_QUALIFIER} Niche)
25. How To Make Faceless {NICHE} Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER})

**Selection rule for `{SUCCESS_CHANNEL}`.** Pick a channel with ≤ 200 uploads and ≥ 50K subscribers that has at least one video ≥ 500K views from the last 6 months. Nick Invests had 184 videos, 155K subscribers and a ~1M-view video 5 months old. Also prefer channels your own commenters already ask about. Here commenters asked for "hoodie guy" (2 comments, 15 likes in total), "Legend Investor Mindset" (2), "Reborn Mindset" and "Bob Invests".

---

## 2. Thumbnail

All measurements below were taken on raw\v.webp at 1280×720: PIL colour medians, pixel bounding boxes and WCAG ratios.

### 2.1 Layout grid (percent of W=1280, H=720)

```
 x: 0%      3%                 41%   59%                 97% 100%
 y: 0%  ┌──────────────────────────────────────────────────────┐  navy corners #091841
    3%  │  [CARD TL: mascot + "THE FIRST $1K HURTS"]  ░teal░  [CARD TR: "WHAT PEOPLE REALLY HAVE"]
   35%  │ ███ FINANCE (yellow) ███████  NICHE (white/silver) ███ │  headline band 35–49%
   49%  │                                                        │
   53%  │  [CARD BL "$900 A MONTH?!"] [■ FULL COURSE ■] [CARD BR "THE $20,000 RULE"]  pill 35–65% × 53–64%
   75%  │            ┌─[ChatGPT logo] [CapCut logo] │ VIEWS / 189K VIEWS (↑)─┐  panel 24–75% × 75–96%
   83%  │ $$$$$$$$$$$$ green banknote pile across full width $$$$$$$$$$$$  │  money band 83–100%
  100%  └──────────────────────────────────────────────────────┘
```

- **Symmetry.** Three columns: example cards on the left (3–41%), a glowing teal gutter (41–59%), and example cards on the right (59–97%). Three horizontal layers sit over them: the headline band through the middle, the pill under it, and the proof panel on the bottom centre over the money band.
- **Focal point.** The headline centre, at about (49%, 41%). Reading path: headline, then pill, then proof panel, then the card headlines.

### 2.2 Every element, measured

| # | Element | Measured position / size | Colour (sampled) | Type and effect | Click psychology |
|---|---|---|---|---|---|
| 1 | **"FINANCE"** | x 91–709 px (7–55%), glyph height ≈ 100 px (**13.9% H**) | Vertical gradient: **#F7C41E** (top) → **#F7BD09** (mid) → **#F7B409** (bottom) | Geometric ultra-heavy wide sans with square-ish counters (Montserrat Black or Gilroy Heavy class). **No hard stroke.** A large soft dark halo/drop shadow (dark green-black ~**#112F25**) separates it from both the background and the pale cards. | Category label: "this is the money niche". Gold reads as wealth. |
| 2 | **"NICHE"** | x ≈ 735–1195 px (57–93%), same height | Silver gradient: **#C6C8CA** (top) → **#F6F7F8** (middle) → **#CBCDD1** (bottom), a metallic sheen | Same font and halo | The two-colour split puts weight on the topic word. "NICHE" is the channel's recurring series word (TRENDING NICHE, FRESH NICHE, GOLDEN NICHE…). |
| 3 | **"FULL COURSE" pill** | Red shape x 444–833 (34.7–65.1%), y 380–460 (52.8–63.9%), about 389×80 px; text cap height ≈ 37 px (**5.1% H**) | Pill **#F7090A**, text **#FFFDFC** (contrast 4.1:1) | Same heavy sans, rounded rectangle, near-horizontal | Completeness and value ("everything in one video"). Justifies 22:52. Red supplies urgency and the one warm accent. |
| 4 | **Proof panel** | ≈ x 24–75%, y 75–96%; dark border **#282B2D** about 6–8 px; corner radius about 14 px | Fill **#FEFEFE** | Left: OpenAI knot logo (≈117 px, 16% H) and CapCut logo, both black line art. Right: "VIEWS" header (condensed bold, ≈35 px, 4.9% H) over "189K VIEWS" (condensed regular, ≈35 px), then a green circle with an up-arrow, **#13C813**, Ø ≈ 66 px (9% H), with a green glow. | Mimics an analytics card. Says "only ChatGPT + CapCut needed" (ease) and "it gets views" (social proof). **The 189K number is recycled template decoration**: the same "189K VIEWS" sits on the FINANCE NICHE Part 2 and FRESH NICHE car-restoration thumbnails (frame 21:47). |
| 5 | **4 example thumbnails** ("this is what you'll make") | Each ≈ 38% W × 40% H. TL 3–41% × 3–46%, TR 59–97% × 4–46%, BL 3–41% × 52–89%, BR 59–97% × 53–86% (partly covered by the panel) | Paper **#D9D8DB / #C2CCD0**; headline ink **#040506** (14:1) | Headlines "THE FIRST $1K HURTS", "WHAT PEOPLE REALLY HAVE", "$900 A MONTH?!", "THE $20,000 RULE" in a heavy condensed sans, line heights 6–13% H ("$20,000" ≈ 13%). Hand-drawn black curved arrows, a cartoon man with a money prop, and slight float shadows. | An outcome preview and pattern match for Nick Invests fans. Each mini-card is itself a proven money-curiosity hook, so the thumbnail borrows the click power of 4 proven thumbnails. **These are copies of the named channel's real thumbnails, and the character resembles a famous TV cartoon. Do not copy this (see the spec).** |
| 6 | **Money pile** | Bottom band y ≥ 83%. Green pixel share per row rises from 7% (y=600) to 33% (y=680). | **#096E09 → #0A760A**, bright highlights | Photo-real banknote cut-outs overlapping the bottom edges of cards and panel | Reward and the RPM promise, readable even at thumbnail-dot size |
| 7 | **Background** | Full frame | Radial: centre gutter **#086F77 / #086364** → sides **#082D60 / #082843** → corners **#091841 / #0B1834** | Smooth gradient with a vertical light glow in the centre gutter | Dark and cool, so yellow, red, white and green pop. Distinct from both the light (#FFFFFF) and dark (#0F0F0F) YouTube UI. |

**Contrast (WCAG ratio).**

| Pair | Ratio |
|---|---|
| Yellow on centre teal | 3.4 |
| Yellow on navy | 7.9 |
| White on teal | 5.3 |
| **Yellow on pale card** | **1.2 (would vanish)** |
| Yellow on dark halo | 8.4 |
| White on halo | 12.9 |
| Green arrow on white | 2.2 |

The **dark halo is load-bearing**: without it the headline disappears wherever it crosses the cards. In greyscale (checked at 320×180) both headline words stay the brightest objects on screen.

### 2.3 Mobile read (downscaled to 168×94 and inspected)

| Element | Rendered height at 168×94 | Read |
|---|---|---|
| FINANCE NICHE | ≈ 13 px | **Readable**: the single message that survives |
| Card headlines | 6–12 px | "$20,000 RULE" and "$1K HURTS" readable as money cues; the rest is texture |
| FULL COURSE | ≈ 4.8 px | Reads as a red tag; the words are marginal |
| VIEWS / 189K VIEWS | ≈ 4.6 px | **Not readable.** The panel still reads as a stats card because of the green ↑ dot. |
| Logos | 10–15 px | Recognisable by shape (OpenAI knot) |
| Money band | — | Reads as "green money" |

At feed size the thumbnail resolves to three messages: **FINANCE NICHE**, then **cartoon money examples**, then **money**. Weakness: clutter. The proof number is illegible, and 4 cards plus a panel compete with each other. This works because the audience already knows the template and the named channel's style.

### 2.4 It is a house template, not a one-off

Frames 03:04 and 21:41–21:50 show the AI Flow videos grid. The same system appears on WHITEBOARD ANIMATION, TRENDING NICHE (×3), FRESH NICHE (×2), FINANCE NICHE (Part 2, 230K) and BULK IMAGES: a collage of example frames, a two-word yellow-and-white label, a red FULL COURSE pill, and a white proof panel with tool logos and a views figure. For this video, only the label (reused from the 230K finance hit) and the 4 background examples (Nick Invests-style) changed. The **template builds recognition** for returning viewers; the **variables (topic word plus example style)** carry the novelty.

### 2.5 Rebuild spec (any niche): Photoshop / Canva / SVG

Canvas 1280×720 px. All coordinates are % of W/H, origin at the top left. Layer order runs bottom to top.

| Layer | Spec |
|---|---|
| L0 Background | Radial gradient centred at (50%, 45%), radius 75%: stop 0% `#086F77`, 45% `#08445E`, 100% `#091841`. Add a vertical soft light streak: a 14%-wide rectangle at x 43–57%, `#0FA3A8` at 25% opacity, Gaussian blur 60 px. |
| L1 Example cards ×4 | Rectangles 38% W × 41% H at TL (3%, 3%), TR (59%, 4%), BL (3%, 52%), BR (59%, 53%). Fill `#E4E4E6` with a faint paper noise of 3%. Rotate each card ±1–3° (TL −2°, TR +2°, BL +1°, BR −1°). Shadow 0 10 px 28 px `rgba(0,0,0,.45)`. **Content per card:** **your original mascot** occupies the left 40% of the card. On the right goes a 2–3-line headline in **Anton** (or Oswald 700), `#050505`, line height 0.95, sized so the biggest word is 9–13% H. Add one hand-drawn black curved arrow (8 px stroke) from the text to the mascot and one niche prop (coin jar, payslip, skull, dumbbell…). Card headlines must be real or planned video titles of the "example channel" style written for **your** mascot, never screenshots of another channel. |
| L2 Money / reward band | Full width, y 83–100%: a cut-out pile of green banknotes `#0A760A` with highlights `#2FBF3A`. Let it overlap the card bottoms by 3–5% H. For non-money niches keep the money (the promise is creator income) or swap in a niche reward pile (gold coins and gems), at ≥ 20% saturated colour coverage in that band. |
| L3 Headline halo | Duplicate the headline text in `#0B1F1A`, Gaussian blur 22 px at 85% opacity, offset (0, +6 px). An extra 8 px outer glow in `#000000` at 40% is optional. |
| L4 Headline | One line, centred at x 50%, cap height **13–14% H** (≈ 96–100 px), spanning **82–88% W**. Word 1 = `{NICHE_WORD}` in **Montserrat Black 900** (or Poppins Black), tracking +1%, vertical gradient `#F7C41E → #F7B409` (topic colour; see the swaps below). Word 2 = `NICHE` (or `COURSE`, `METHOD`, `CHANNEL`) with silver gradient `#C6C8CA → #F6F7F8 (50%) → #CBCDD1`. Gap between the words ≈ 2% W. Baseline at y ≈ 48%. **No hard stroke.** |
| L5 Pill | Rounded rectangle centred at x 50%, y 53–64%, width ≈ 30% W, radius 12 px, fill `#F7090A`, rotated 0 to −2°. Text `FULL COURSE` (or `STEP BY STEP`, `FREE TOOLS`) in Montserrat Black, `#FFFFFF`, cap height 5–6% H, with a shadow of 0 3 px 6 px `rgba(0,0,0,.35)`. |
| L6 Proof panel | Rounded rectangle x 24–75%, y 75–96%, fill `#FEFEFE`, stroke 7 px `#282B2D`, radius 14 px, shadow 0 8 px 20 px `rgba(0,0,0,.5)`. Left 45%: two tool logos in black line style at 14–16% H each, separated by 4% W (use only logos you are allowed to show; generic glyphs are fine). Right: `VIEWS` in Oswald 700 at 5% H, then `{REAL_NUMBER} VIEWS` in Oswald 500 at 5% H, then a green circle Ø 9% H `#13C813` with a white ↑ arrow and a 12 px `#13C813` glow at 60%. **Use a verifiable number** (for example the real view count of the example channel's top video, or your own result), never a recycled figure. |
| L7 (optional) Gutter glow | A soft white radial at (50%, 30%), 15% opacity, behind the headline. |

**Topic-word colour swaps** (keep "NICHE" silver every time, and keep the background family):

| Niche | Topic-word gradient |
|---|---|
| Finance | `#F7C41E → #F7B409` |
| Health / fitness | `#B6F23A → #7ED321` |
| History | `#F5A623 → #D9822B` |
| Psychology | `#FF7AD9 → #E040A0` |
| Horror / survival | `#FF4D4D → #D41C1C`, with the pill switched to `#FFC400` and black text |
| Tech | `#4FD1FF → #1FA2FF` |

**Original mascot (mandatory).** Never draw or prompt a character that resembles a known TV or film cartoon; the reference mini-thumbnails here do. Define the mascot once and reuse it:
- **Silhouette:** e.g. a pear-shaped body, a large oval head and a single distinctive feature such as a tuft, scarf or beanie.
- **Palette:** 3 flat colours plus outline. Outline `#1A1A1A` at 6 px.
- **Expression set:** smug, worried, shocked, thinking.
- **Prop slot:** in the right hand.

Run a similarity check against famous characters before publishing, as a reverse-image or visual review.

**QA before export.**
1. Downscale to 168×94: the headline must read; one card headline must read; the money band must read.
2. Greyscale: the headline is the brightest element.
3. The headline halo contrast is ≥ 7:1 against everything it crosses.
4. Total text blocks ≤ 7. This thumbnail has 7: headline, pill, panel and 4 card headlines. Do not add more.
5. The proof number is true.

---

## 3. Description, tags, chapters, links (SEO structure)

### 3.1 What is there (measured)

- **Size:** 3,985 characters, 564 words, 109 lines, **19 URLs**, 5 hashtags.
- **Line 1 is the exact title**, so the keyword sits in the first 150 characters (the search snippet).
- **Prose block:** 4 paragraphs, 187 words, second person ("you will learn…"). Keyword repetitions in the prose: "finance" 8×, "Nick Invests" 3×, "high RPM" 2×, "faceless" 2×. Across the whole description: finance 21×, niche 14×, channel 15×, YouTube 17×, AI 12×. The prose names every pipeline step (topics → script → voiceover → visuals → titles and thumbnails → editing), which mirrors the chapters semantically.
- **Lead magnet:** a "PDF Link" pointing to a Google Drive file, placed right after the prose. It is also in the pinned comment.
- **Tools block:** the **affiliate link first**, with a heart emoji ("Buy Aged or Monetized Accounts", monetizedprofiles.com with an `affid` parameter). Then Google Whisk, Cleanup.pictures, Pixelcut and Grok. Claude, Google AI Studio and CapCut are used in the video but not linked.
- **Community funnel:** Instagram, then Telegram labelled "(Must Join)", then WhatsApp channel labelled "(Active)". The video promises the PDF on Telegram and WhatsApp once a like target is met (21:41–21:50).
- **Chapters:** 11 one-word step labels: Important, Channel Setup, Video topics, Script, Voice, Visuals, Videos, Editing, Thumbnail, SEO, Final Video. The intro (0:00–3:12, the proof section) is labelled **"Important"** to discourage skipping. The heatmap shows it is still the least replayed part (mean 0.10).
- **"Watch My Previous Videos":** 10 internal links with short labels. Mostly named-channel and finance siblings: "Make Finance Videos Like Crayon Capital", "Primate Economics (Part 1)", "your.nextcore", Grok trick, JSON ads. Labels can differ from the current titles. QohbJR-c1T8 is labelled "…Like Crayon Capital" but is now titled "How I Create High RPM Finance Videos Using ONLY AI", which suggests titles get renamed.
- **"Queries People Ask":** 20 lines, 176 words of raw keyword variants, plus a comma-stuffed line that repeats all the tags and adds "sketch videos with ai" and "videos like bob invest". This is where **competitor channel names (Crayon Capital, Bob Invests)** are planted.
- **Hashtags:** #makemoneyonline #ai #aitools #youtubeautomation #newniche. The first three render above the title.
- **Tags (15, 454 characters):** generic (`make money online`, `ai`, `ai tools`, `ai flow`), then the "how to create videos like nick invest" family (5 variants, including a typo "nick invest"), finance how-tos, `high rpm finance niche`, `how to make videos like crayon capital`, `how to find high rpm niches 2026`.
- **Pinned comment (uploader, edited):** 3 "Watch Next" links (finance Part 2, a 100K-new-niche video, a "Claude Code $4,200/Month" video), a "Full Course on Finance Niche" link, and the PDF link. It links videos uploaded **after** this one (1–2 months ago), so it is **being re-edited to route this evergreen video's traffic to new uploads**.

### 3.2 Reusable description template

```
{TITLE}

In this video, you will learn how to create {NICHE} videos like {SUCCESS_CHANNEL} using AI tools. The {NICHE} niche is one of the {MONEY_QUALIFIER} niches on YouTube, and many faceless channels {VERIFIABLE_RESULT_CLAIM}.

I will show you the complete process step by step: how to find viral {NICHE} video topics, how to write a high-quality script with AI, how to generate an AI voiceover, and how to create visuals and images for your videos. Even if you have no experience, you can start a {NICHE} channel with this method.

This tutorial also explains how channels like {SUCCESS_CHANNEL} grow so fast with evergreen {NICHE} content: curiosity-driven titles, simple thumbnails, and simple editing that keeps viewers watching.

If you want to start a faceless YouTube channel in the {MONEY_QUALIFIER} {NICHE} niche, this video takes you from channel creation to publishing.

📄 Free Prompt Pack (all prompts used in this video): {DIRECT_LINK}   ← deliver immediately, never gate
__________________
🛠️ Tools used
{TOOL_1}: {URL}
{TOOL_2}: {URL}
{TOOL_3}: {URL}
{OPTIONAL_DISCLOSED_AFFILIATE}: {URL}  (affiliate link)
__________________
🌍 Community
{COMMUNITY_CHANNEL_1}: {URL}
{COMMUNITY_CHANNEL_2}: {URL}
__________________
⏰ Chapters
00:00 {Proof / why this niche}
mm:ss Channel Setup
mm:ss Video Topics
mm:ss Script
mm:ss Voice
mm:ss Visuals
mm:ss Animation
mm:ss Editing
mm:ss Thumbnail
mm:ss SEO
mm:ss Final Video
__________________
🎬 Watch next
▶ {SERIES_VIDEO_1 short label}  {URL}
▶ {SERIES_VIDEO_2 short label}  {URL}
… (6–10 items, same niche or named-channel series first)
__________________
📌 Questions people ask
{12–20 short natural-language variants: "how to make videos like {SUCCESS_CHANNEL}", "{NICHE} faceless channel", "{MONEY_QUALIFIER} youtube niche", "{SIMILAR_CHANNEL_2} style videos with ai", "how to start a {NICHE} youtube channel {YEAR}"}

#{HASHTAG_1} #{HASHTAG_2} #{HASHTAG_3} #{HASHTAG_4} #{HASHTAG_5}
```

**Tag template (12–16 tags, ≤ 480 characters).**
- Generic: `make money online`, `ai tools`, `{CHANNEL_BRAND}`.
- 4–5 variants of `how to make videos like {SUCCESS_CHANNEL}` (with and without the trailing "s", "create" / "make", "channel like").
- 3 niche how-tos: `how to make {NICHE} videos with ai`, `faceless {NICHE} videos`, `{MONEY_QUALIFIER} {NICHE} niche`.
- 1–2 adjacent channels: `how to make videos like {SIMILAR_CHANNEL}`.
- 1 dated query: `how to find {MONEY_QUALIFIER} niches {YEAR}`.

**Pinned comment template.** Line 1: the lead-magnet link. Lines 2–4: "Watch next" links to the newest videos in the same series. Re-edit it monthly.

---

## 4. Comments and audience (data\comments.json, n=133)

- **Coverage:** 132 viewer comments plus 1 pinned uploader comment. The uploader posted no replies. Sum of comment likes: 235. Timing is front-loaded: 65 comments (49%) are "7 months ago", 87 (66%) fall within the first ~2 months, and posts still arrive 7 days ago, so the video is evergreen.
- **Language mix (heuristic):**
  - Romanised Hindi/Urdu (Hinglish): 69 (52%).
  - English: 56 (42%). Many are one-word asks such as "Pdf" or "Prompt".
  - Devanagari Hindi: 4 (3%).
  - Romanised Bengali: 1.
  - Emoji only: 2.
  - "Bhai / bro / bhaiya" appears in 49 comments, a peer-mentor register.
  - YouTube shows "PK" next to the logo in the screen recordings, suggesting a Pakistan-based creator. One viewer remarks that he does not seem Indian; another writes from Bangladesh.
- **What viewers ask for:**
  - **The prompts PDF:** 44 comments (33%) mention pdf, prompt or file ("where is the pdf", "prompt kahan hai"). One Devanagari comment (5 likes) says the like target was passed (200+) and still no PDF link appeared on the WhatsApp channel.
  - **Voice:** which voice it is, how to make long voiceovers, and that Google AI's limit is about 1 minute (7 comments).
  - **CapCut:** how to download or run it from India, captions not free (8).
  - **Next named channels:** "hoodie guy" (2 comments with 9 and 6 likes), "Legend Investor Mindset" (2), "Reborn Mindset", "Iron Football" shorts, own-character creation, an editing deep-dive.
  - **Ops questions:** upload time for a US audience, turning on the AI-content label, monetisation odds.
- **Objections:**
  - **Effort and cost (top comment, 39 likes):** 100–120 images per 10 minutes and 10–15 hours per video.
  - **Inauthentic-content and policy risk:** 15 likes, plus 3 Hinglish variants.
  - **Saturation:** a commenter says channels doing this (Warren-Buffett style) "died", 3 comments.
  - **Getting views is hard:** 2.
  - **Visuals harder than they look:** 6 likes. The commenter has watched ~10 tutorials and none matched the Nick Invests or Bob Invests look.
  - **Tool paywalls:** Grok became paid (2 comments); a Grok watermark.
  - **The voice sounds odd:** almost certainly the auto-dubbed English track.
- **Practitioner signal:** at least 12 commenters' handles are finance-channel names (…Invests, …Wealth, Dollar…, Money…). Two commenters say they made a channel after this video, and one says views are starting to come. The video converts viewers into practitioners, who then come back for the next "like X" tutorial.
- **What drove engagement:**
  1. The like-gated lead magnet. The "200 Likes" target appears at 21:44 and is said at 21:41–21:50; likes reached 4,498, which is 22× the target and a 3.1% like rate.
  2. Delivery friction itself, which produced dozens of PDF comments. This is negative sentiment, but it still counts as comment activity.
  3. A concrete, copyable pipeline that invites follow-up questions.
  4. Named-channel requests that feed the next video.

  The comment rate is modest: 0.92 per 1,000 views.

---

## 5. Heatmap reading (data\heatmap.json, 100 buckets of ~13.7 s)

**What the graph measures.** The "most replayed" graph is normalised so that max = 1. It shows replay concentration, not audience retention.

**The full curve.**

| Time | Value | What is happening |
|---|---|---|
| 00:00–01:49 | 0.02–0.12 | Low. A small bump at 01:08–01:36 (0.11–0.12) is the Nick Invests reveal plus the "~1M views, evergreen" claim. |
| 02:03–02:30 | 0.25 | Nick Invests video grid; "the reason is money"; video lengths 52 and 44 min, so more ads |
| 02:30–02:58 | 0.04 | Example clip playing |
| 02:58–03:12 | 0.26 | Example clip ends, the "100K Subscribers" subscribe overlay appears, and the Channel Setup chapter lands |
| Channel Setup (03:12–06:41, mean 0.24) | — | Local peaks at **03:39–03:53 = 0.32** (the channel-name prompt, zoomed full screen at 03:52), **05:29–05:43 = 0.34** (5 logo prompts, then Whisk), **06:24–06:37 = 0.35** (refined logo prompt) |
| Video topics (06:41–09:25, mean 0.23) | — | **07:05–07:19 = 0.45**: the topic-generator prompt with the title-pattern list is readable on screen (07:02–07:12). Then a decay to 0.11–0.23 while lists scroll, rising to 0.30 at the chapter boundary. |
| Script (09:25–11:38, mean 0.36) | — | A 0.21–0.37 plateau: the script prompt is visible at 09:40, plus the Claude free plan and the 1,800–2,200-word length control. Then **11:26–11:39 = 1.00 (global peak)**: the finished script is pasted into Google Docs and the headings are deleted (11:23–11:35). The document outline (HOOK / PROBLEM SETUP / CORE EXPLANATION / INSIGHT / PRACTICAL TAKEAWAY / ENDING) is visible at 11:30, and the text scrolls by about a page per second (11:36–11:44). The Voice chapter also begins at 11:38, so chapter-jump landings fall in this bucket. |
| Voice (11:38–13:00, mean 0.49, the highest-mean long chapter) | — | 0.70 / 0.58 / 0.60 / 0.45: Google AI Studio's free TTS steps, a one-line style-instruction prompt (12:08–12:25), the "Charon" voice choice. A dip to 0.20 at 12:34–12:48 while the sample voice plays. |
| Visuals (13:00–15:10, mean 0.36) | — | 13:15–13:43 = 0.47–0.50 (the image-prompt prompt in ChatGPT, then scene prompts); 14:10–14:24 = 0.40 (the Whisk "subject" trick that keeps the character consistent, 14:31–14:44) |
| **Videos (15:10–15:55, mean 0.60, the highest of any chapter)** | — | 15:19–15:32 = 0.70 and **15:32–15:46 = 0.85**: the image-to-video prompt, then **Grok turns the cartoon image into a talking clip with audio** (15:26–15:45) |
| Editing (15:55–19:30, mean 0.17) | — | Falls to **0.03–0.06 at 16:55–17:50**, a talk-only explanation of image timing with nothing to copy. **18:03–18:17 = 0.53**: where to click in CapCut for zoom in/out animation and auto captions. |
| Thumbnail (mean 0.18), SEO (mean 0.13), Final Video (mean 0.06) | — | Taper; 22:24–22:52 ≈ 0. Viewers do not watch the sample output. |

**Pattern.** Every local maximum coincides with a **copyable artefact on screen** (a prompt, a finished script, a setting, a click path) or a **"wow" output reveal** (the Grok talking character). Every trough coincides with **talk-only explanation** or a **sample playing**. Because the PDF was gated or undelivered, pausing on the screen was the only way to get the prompts, and that amplifies these replay peaks.

**Chapter-landing effect.** Buckets at chapter starts lift moderately (0.24–0.37). Voice (11:38) is the strongest landing, consistent with the voice questions in the comments.

---

## 6. Channel formula benchmarks

Sources: the live channel page on 2026-10-22, which filled all 24 "NA" rows (all of them collab posts), and the TSV durations. The target counts as 144,518.

**Baselines.** Channel median **14,000** (n=108, mean 35,237, p75 45K, p90 89K). Target rank: **8 of 108**.

| Baseline | Median | Target multiple |
|---|---|---|
| Whole channel (excl. target) | 14,000 | **10.3×** |
| Uploads in the last 12 months | 22,000 | 6.6× |
| ±10 neighbouring uploads | 30,000 | 4.8× |
| Solo posts, collab era (≤ 10 months) | 8,000 | 18.1× |
| Collab posts, collab era | 47,000 | 3.1× |
| "Like {Named channel}" formula | 26,000 (excl.) | 5.6× |
| Finance topic | 44,000 (excl.) | 3.3× |

| Primary title formula | n | Median views | Max | Best example |
|---|---|---|---|---|
| **Named model channel ("…Videos Like {X}")** | 17 | **27,000** | 196K | Yellow Dude (196K); **this video (144.5K)**; @MYTHRA (117K) |
| Named channel, other angle ("I Bought X's Paid Course…") | 1 | 168,000 | 168K | Anidoc paid course |
| Niche / format how-to (no named channel) | 35 | 19,000 | 278K | AI Survival ASMR "New Viral Niche…" (278K) |
| Clone-any-channel | 4 | 15,000 | 159K | Clone Any YouTube Channel with Claude AI |
| First-person build ("How I Create / I Built") | 9 | 14,000 | 264K | AI Car Restoration (264K); High RPM Finance (146K) |
| Tool trick / review / tool news | 29 | 6,100 | 95K | Grok long-video trick |
| "This channel got N views" case study | 4 | 5,150 | 41K | This New Channel Got 100K+ Views… |
| Niche lists / opportunity / policy news | 9 | 3,200 | 64K | Why Psychology + Self Improvement… |

| Modifier | n | Median |
|---|---|---|
| **Collab post (≥ 2 creators)** | 24 | **51,500** |
| Solo post | 84 | 7,250 |
| Collab, 4+ creators | 7 | 69,000 |
| Finance / economics / RPM topic | 11 | 45,000 |
| Finance and solo | 8 | 28,500 |
| Finance and collab | 3 | 144,518 (56K / 144.5K / 230K) |
| "Like X", no "\|" tail | 8 | 52,500 |
| "Like X", with "\|" keyword tail | 9 | 17,000 |
| "Like X", plain name / with @ | 6 / 11 | 43,500 / 25,000 |
| "Full/Complete Course" **in the title** | 5 | 8,700 (it belongs in the thumbnail) |
| "FREE" in title | 30 | 9,100 |
| "Viral" in title | 21 | 22,000 |
| Duration < 8 min | 24 | 2,950 |
| 8–12 min | 36 | 6,650 |
| 12–18 min | 29 | 25,000 |
| 18–25 min | 12 | 35,500 |
| > 25 min | 7 | 38,000 |

Reading: on this channel, **length, collab distribution, a finance or money topic and a named-entity title all stack**. The target sits where all four overlap: 22:52, 4 creators, finance, and a named channel.

---

## 7. Why it works (ranked hypotheses, with evidence)

1. **Multi-channel Collaboration distribution (largest effect, but confounded).** The post went out under 4 creators. Over the same ~10-month era, collab posts have a median of 47K against 8K for solo posts, and 7 of the top 10 channel videos are collabs. The partner channels' subscribers see it in their feeds and subscription lists, which seeds early velocity before search and suggested take over. **Confound:** collab posts are also longer and are probably the creator's "big topic" picks.
2. **A proven money topic and franchise momentum.** Finance is the channel's best topic (45K median). This video follows 146K and 230K finance tutorials. The thumbnail label is identical to the 230K hit's, and the pinned comment and description cross-link the finance series. Returning viewers recognise both the series and the template.
3. **The named-entity title rides a channel at peak curiosity.** On screen at 01:20–01:41, Nick Invests has 155K subscribers, 184 videos, and a ~1M-view video 5 months old. Aspiring creators who see that channel search for "videos like nick invests" or get this video suggested next to it. The tags and the "Queries" block cover the variants and adjacent channels (Crayon Capital, Bob Invests). The same skeleton produced the channel's 196K Yellow Dude hit.
4. **An explicit money promise.** "High RPM" in the title, a money pile in the thumbnail, RPM math in the first minute ($5–15 RPM, ~$3,340 from one video), and the "longer means more ads" argument. The audience's core motive is income. Comments ask about monetisation and USA-audience strategy.
5. **The thumbnail sells the output, not the presenter.** Four example thumbnails in the target style let viewers preview "what I will make". "FULL COURSE" signals completeness. Two familiar tool logos signal ease, and the ↑ views card signals results. At mobile size it still reads as "FINANCE NICHE + cartoon money".
6. **A complete, free-tool pipeline that rewards rewatching.** 22:52 with 11 step chapters. Free tools at every step (Claude free, AI Studio TTS, Whisk, Grok). Prompts appear readable on screen (zoomed at 03:52), so replay peaks form at every copyable artefact, which tells YouTube the video is useful. Viewers come back to it while they build.
7. **The lead magnet plus a public like target.** The "200 Likes" target turns the like button into a transaction (3.1% like rate). Delivery friction pushed comment volume up (33% of comments ask for the PDF) at a sentiment cost.
8. **An auto-dubbed English track.** The formats contain "English (US)" alongside "Hindi original (default)". 42% of comments are in English, and one English viewer asks where to get "this English voice", which means they heard the auto-dub. This widens the addressable audience beyond Hindi/Urdu speakers.
9. **Timing (March 2026).** The finance-animation "…Invests" wave was peaking (Nick Invests, Bob Invests, Crayon Capital, Legend Investor Mindset; the last had 46.1K subscribers from 24 videos at 00:14–00:31). Free AI tools could replicate the look. The channel was growing from ~31K to 50.9K subscribers.
10. **Evergreen query.** The video still draws comments 7 days ago, and lifetime views average ≈ 637 per day. A "how to make videos like {growing channel}" query stays alive as long as the model channel keeps growing.

---

## 8. Rules to copy

1. Title every flagship tutorial with the skeleton `How To Make Videos Like {SUCCESS_CHANNEL} With AI ({MONEY_QUALIFIER} {NICHE} Niche)`. Write the channel name without "@", use exactly one parenthetical, no "|" keyword tail, ≤ 75 characters, with the entity ending before character 40.
2. Pick `{SUCCESS_CHANNEL}` only if it has ≤ 200 uploads, ≥ 50K subscribers, and at least one video ≥ 500K views from the last 6 months. Show those three numbers on screen within the first 90 s.
3. Prefer niches with a money qualifier (finance, high-RPM, USA audience) for flagship videos. On the reference channel, finance titles have a median of 3.2× the channel median.
4. Do not write "Full Course" in the title. Put it in the thumbnail pill. Titles containing "Full/Complete Course" have a median of 8.7K (n=5), below the 14K channel median, while the top finance tutorials carry "FULL COURSE" only in the thumbnail.
5. Make flagship tutorials 18–28 min with 9–12 one-word step chapters (Setup, Topics, Script, Voice, Visuals, Animation, Editing, Thumbnail, SEO, Final). Never publish a "how to build a channel" tutorial under 12 min (the < 8 min median is 2.95K).
6. Publish flagship tutorials as a YouTube Collaboration with 2–4 partner channels in the same audience whenever possible (collab median 47K versus solo 8K in the same era).
7. Build every thumbnail on the fixed house template in section 2.5. Change only the topic word, the topic colour, the 4 example cards and the proof number.
8. Make the headline one line, 13–14% of height, 82–88% of width, two words: a coloured topic word plus a silver "NICHE". Always put a dark blurred halo behind it (≥ 7:1 contrast against everything it crosses). Never use a hard stroke.
9. Fill the 4 example cards with **your own original mascot** in the target channel's genre: curiosity-money headlines, a black hand-drawn arrow, one prop. Never paste another channel's real thumbnails or a character resembling a known cartoon.
10. Use a real, verifiable figure in the proof panel. Never recycle a number across thumbnails.
11. Run thumbnail QA at 168×94 before export: the headline must read, at least one card headline must read, and there are ≤ 7 text blocks in total.
12. Spend the first 3:00 on proof (example channel stats, RPM arithmetic, the "longer videos = more ads" argument), then promise the full method. Label that chapter so viewers do not skip it.
13. Show every prompt **full screen and zoomed, for ≥ 3 s**, at the moment it is used. Expect a replay spike there and treat it as a feature.
14. Deliver the prompt pack immediately: a direct link in the description, the pinned comment and on screen. If you use a like goal, say the number once (e.g. 200), and post the link anyway within 24 h. Undelivered gates cost sentiment (33% of comments here are complaints about it).
15. Show one "wow" output reveal (image → animated or talking clip) in the middle third (55–70% of runtime). It produced the strongest chapter-level replay (mean 0.60).
16. Cut any talk-only stretch longer than 20 s where nothing copyable is on screen (17:00–17:50 dropped to 0.03).
17. Write the description in this order: title on line 1 → 150–200 words of second-person prose repeating the niche word ≥ 6× and the named channel ≥ 3× → the lead-magnet link → tools (disclosed affiliates) → community links → chapters → 6–10 "watch next" series links → a 12–20-line "questions people ask" block that includes 1–2 adjacent channel names → 5 hashtags.
18. Use 12–16 tags, 4–5 of them variants of "how to make videos like {SUCCESS_CHANNEL}" (including common misspellings) and 1–2 adjacent channels.
19. Re-edit the pinned comment every month so it points to the newest videos in the same series.
20. Mine comments for the next `{SUCCESS_CHANNEL}`. Any channel requested in ≥ 2 comments, or with ≥ 10 total likes, goes on the topic shortlist.
21. Keep the creator's original-language audio and enable auto-dubbing (or upload a reviewed English dub) so English-speaking aspiring creators are reached.

---

## 9. Open questions / low-confidence

- **No YouTube Studio data.** Impressions, CTR, traffic-source split (search, suggested, browse, collab feeds) and average view duration are unknown. The CTR-related conclusions are inferred from packaging and outcomes, not measured.
- **Collab confound.** Collab posts are recent, longer, and probably reserved for the strongest topics. The 5.9× collab effect is a correlation. The sizes of the partner channels (Oriva AI, AI Man, Ai Dadaji) were not checked, to keep requests minimal.
- **Survivorship bias.** A video titled "How To Make Professional AI Ads With Magic Hour Step by Step" (918 views, shown on the channel page at 03:04) is missing from today's list. One viewer also remarks that underperforming videos seem to be removed. The channel medians may be inflated by deletions.
- **Renamed titles.** Labels in the description and pinned comment differ from the current titles of QohbJR-c1T8 ("…Like Crayon Capital") and 0bUfNxSCsGs ("Claude Code (Free Plan) + YouTube = $4,200/Month"). The creator may A/B test or rename titles, and in the SEO step (21:00) he recommends generating 5 titles for A/B testing. Whether this video's title or thumbnail changed after upload is unknown.
- **PDF timing.** It is unclear whether the Drive link was in the description at upload or added later (the pinned comment is marked "edited"). It is also unclear why viewers kept asking: they may not open descriptions on mobile, or the link was added late.
- **Auto-dub share.** The share of views that came through the English auto-dub is unknown. The English comments could also come from South-Asian viewers who write in English.
- **The heatmap is "most replayed".** It is not a retention curve. The low intro values do not prove people skipped the intro.
- **Thumbnail measurements.** Font identification is by visual class (geometric black sans for the headline and pill, condensed grotesk for cards and panel), not by font file. Exact pill rotation (≤ 3°) and panel border width are estimated from the image.
- **Comment language split.** It comes from a keyword heuristic (±5%).
- **IP risk.** The reference thumbnail reproduces another channel's real thumbnails and a character resembling a well-known cartoon. Its CTR may partly come from that recognisability, which our template intentionally forgoes.
