# L1 — Packaging, CTR & channel strategy (cross-corpus lens)
Analyst 1 · sources: `channel_all_meta.txt` (148 public videos, snapshot 2026-10-23; one age-restricted video "Your first gym experience be like", 382 K, is missing from it), `videos_sorted.txt`, all 10 corpus `v.info.json` (description, tags, chapters, heatmap), 10 corpus thumbnails + **14 extra thumbnails fetched** to `lbs\_thumbs\` (best, mid and worst performers), pixel metrics on all 24 thumbnails (own script), 4,000 top comments (400 × 10, theme-coded by regex), descriptions of 3 recent uploads (2025-12, 2026-06, 2026-10) via yt-dlp, and contact sheets of all 10 videos (first 2 + mid + last for v02, v04–v10; every sheet for v01/v03).
No YouTube Analytics exist for this channel in our evidence → CTR, impressions and traffic sources are **not measured**; every statement about them is marked [inferred] with a confidence.
Channel characters (Wojak, Doomer, Chad, NPC…) are named only to describe the pattern; every rule says "original character that fills this role".

---

## 1. Channel numbers

### 1.1 View distribution (148 videos, 128.9 M views)
| Stat | Value |
|---|---|
| Median / mean | **518,729** / 871,133 |
| p25 / p75 / p90 | 310 K / 1.07 M / 1.83 M |
| Top-10 share of all views | **30.0 %** |
| Videos ≥2× / ≥3× / ≥5× median | 39 / 20 / 9 |
| Top 10 (the corpus) | 4.7×–12.3× median; all 10 ≥2.46 M |
| Worst | 83 K ("What if Anakin…", 2021) — 0.16× |

Era-controlled outlier score (views ÷ median of the 10 nearest uploads): top 5 = Life of a food delivery driver ×7.5 (2022), Social Credit ×6.8 (2022), Metaverse ×5.9 (2021), Doomer's path to Happiness ×5.8 (2024), Origin of a Doomer ×4.8 (2023). Fast Food ×4.2, From Doomer to Bloomer ×3.4, Gyms in 2050 ×2.3. Bottom = memes/specials under 2 min (×0.16–0.25) and "be like" skits.

### 1.2 Views by upload year (age effect + era effect)
| Year | Uploads | Median views | Mean | Median dur (s) | Median gap between uploads (d) | Best video |
|---|---|---|---|---|---|---|
| 2021 | 31 | 482 K | 675 K | 190 | 8 | Living in a Metaverse 2.66 M |
| 2022 | 23 | 520 K | 860 K | 211 | 14 | Social Credit 3.16 M |
| **2023** | 22 | **1.60 M** | **2.00 M** | 315 | 13 | **Origin of a Doomer 6.39 M** |
| 2024 | 16 | 864 K | 1.18 M | 389 | 21 | Doomer's path to Happiness 4.43 M |
| 2025 | 25 | 475 K | 611 K | 447 | 10 | From Game Addict to Successful 1.51 M |
| 2026 (to Oct) | 31 | 283 K | 322 K | 512 | 7 | Being Lonely in your 30's 0.64 M |

- 7 of the top 10 were uploaded in one 18-month window (Jan 2023 – Jul 2024).
- Lifetime views/day: Doomer's path to Happiness 5,420/d, Origin 4,867/d, Fast Food 4,484/d, From Doomer to Bloomer 4,115/d, Retail 3,112/d — the 2023–24 winners still earn more per day than most 2026 uploads did in their first 3 months.
- New uploads still get an opening push (Life of a Casino Employee: 242 K in 4 days = 60,581/d; Living in a Ghetto: 625 K in 11 days), but 2026 uploads mostly plateau at 0.14–0.64 M.
- Durations rose every year (190 → 512 s median) while cadence doubled in 2025–26 (gap 7–10 d) and median views fell to 283 K. Causality not provable here (topic fatigue, audience aging, more competitors are equally plausible) [inferred, low].

### 1.3 Upload cadence timeline
2021: 2–5 uploads/month (crypto-meme skits, 1.5–3.5 min). 2022: 1–3/month, first "Living in…" dystopias and the first "Life of a…" (May 2022). **2023: 1–3/month, median gap 13 d, 3 theme sprints** — "in 2050" ×3 in 7 weeks (Apr 9, May 7, May 28), Doomer saga ×2 (Mar 20, Jul 7), "Life of a…" ×5 in 10 weeks (Oct 7 → Dec 15). 2024: slowdown (gap 21 d, max 46 d). 2025: gap 10 d, longer episodes, new "in your 30's" family (Oct 2025 →). 2026: weekly-ish (gap 7 d), 8–10-min episodes.

### 1.4 Format families — who won
Raw and era-controlled (median of views ÷ neighbour median):
| Family | n | Median views | Max | Share of all channel views | Median rel. | Videos ≥2× neighbours | Median dur (s) | Median like % |
|---|---|---|---|---|---|---|---|---|
| "Life of a [job]" | 37 | 580 K | 4.93 M | **29.2 %** | 1.13 | 8 | 453 | 3.06 |
| Doomer saga / transformation | 10 | 671 K | 6.39 M | 15.1 % | 1.07 (mean 2.09) | 4 | 251 | 3.88 |
| Dystopia (2050 / Metaverse / Social Credit / AI) | 15 | 625 K | 3.41 M | 13.3 % | 0.87 (mean 1.80) | 4 | 372 | 4.20 |
| Crypto/finance memes (2021–22 base) | 29 | 517 K | 1.36 M | 14.8 % | 0.88 | 5 | 190 | 3.71 |
| Relatable skits ("be like", "when you", POV, vs) | 26 | 388 K | 2.08 M | 12.1 % | 0.71 | 6 | 327 | 3.64 |
| "Life of a [social archetype]" | 7 | 804 K | 1.45 M | 5.1 % | 0.87 | 2 | 393 | 3.29 |
| "[state] in your 30's" (2025–26) | 9 | 635 K | 1.37 M | 4.6 % | **1.86** | 3 | 534 | 2.96 |
| Addiction cycle | 3 | 1.16 M | 2.46 M | 3.0 % | 1.53 | 1 | 421 | 3.80 |
| Other memes/specials | 12 | 241 K | 0.84 M | 2.8 % | 0.46 | 0 | 154 | 5.32 |

Reading: the saga and dystopia families are **hit-driven** (mean ≫ median: each has 3 mega-hits and many flops); the job series is the **reliable volume engine** (37 episodes, 29 % of all views); "in your 30's" is currently the strongest family relative to the channel's declining baseline.

### 1.5 Duration sweet spot
| Duration | n | Median views | Median rel. (era-controlled) |
|---|---|---|---|
| <2 min | 8 | 139 K | 0.22 |
| 2–3.5 min | 35 | 423 K | 0.66 |
| 3.5–5 min | 21 | 643 K | 0.88 |
| **5–6.5 min** | 22 | **1.28 M** | 1.36 |
| **6.5–8 min** | 20 | 987 K | **1.62** |
| 8–9.5 min | 38 | 353 K | 0.95 |
| ≥9.5 min | 4 | 295 K | 0.96 |

Two sweet spots: **voiced episodes 300–480 s** (v03 452, v05 441, v06 453, v07 427, v10 421, v09 359), and **wordless emotional saga films 170–281 s** (v04 170, v01 221, v02 281 — 3 of the top 4). Top-10 durations: 170, 211, 221, 281, 359, 421, 427, 441, 452, 453 s.

---

## 2. Comparison table — the 10 corpus videos (packaging)

| # | Title (words/chars) | Template | Family | Upload (weekday) | Dur | Views | ×ch. median | Like % | Comment % | Thumbnail layout | Figures | Text in thumbnail | Real brand / IP in thumbnail | Description L1 | Series link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v01 | Origin of a Doomer (4/18) | Origin of a [archetype] | saga | 2023-03-20 Mon | 221 | 6.39 M | 12.3 | 3.55 | 0.103 | diagonal split, same character before/after in profile, facing each other | 2 | none | none | "This Doomer video is about how Wojak turns into a doomer…" | → sequel URL |
| v02 | From Doomer to Bloomer (4/22) | From [A] to [B] | saga | 2023-07-07 Fri | 281 | 4.96 M | 9.6 | 4.36 | 0.109 | before → red curved arrow → after; mentor ghost behind centre | 3 | none | photoreal meme man | "This video is de sequel to 'Origin of a doomer'. Watch it here…" (link starts at t=10 s) | ← prequel URL |
| v03 | Life of a Fast Food employee (6/28) | Life of a [job] | job | 2023-10-19 Thu | 452 | 4.93 M | 9.5 | 2.69 | 0.142 | lineup of 3 workers waist-up + food foreground | 3 | none | real fast-food pole sign + packaging | "This Wojak meme video is about the life of a fast food chain employee…" + 3 real chain names | — |
| v04 | Doomer's path to Happiness (4/26) | [A]'s path to [state] | saga | 2024-07-28 Sun | 170 | 4.43 M | 8.5 | 4.36 | 0.108 | 50/50 vertical split, night vs sunrise, red arrow | 2 | none | beer-brand-like green bottles | "…short montage of doomers guide to happiness, with [song] as background music." | — |
| v05 | Gyms in 2050 (3/12) | [domain] in 2050 | dystopia | 2023-05-07 Sun | 441 | 3.41 M | 6.6 | 3.36 | 0.079 | duo; giant outline "2050" behind | 2 | "2050" (outline numerals) | — | "This wojak gym meme video is about gyms in 2050." | — |
| v06 | Life of a retail employee (5/25) | Life of a [job] | job | 2023-10-07 Sat | 453 | 3.46 M | 6.7 | 2.69 | 0.168 | lineup of 3 | 3 | name tags only | real retailer spark logo | "…Wojak works at Walmart (Wagemart)…" + 4 real retailer names | — |
| v07 | Living in a Social Credit System (6/32) | Living in a [system] | dystopia | 2022-06-15 Wed | 427 | 3.16 M | 6.1 | 3.78 | 0.231 | centre face in recognition bracket, score boxes, CCTV, NPC crowd | 5 | numbers 548 / 539 / 712 / 391 | — | "The Social Credit System is a national credit rating…" | — |
| v08 | Life of a food delivery driver (6/30) | Life of a [job] | job | 2022-05-04 Wed | 211 | 2.82 M | 5.4 | 3.52 | 0.089 | duo on bikes; map left / sky right; earnings | 2 | "+$18 +$5,3 +$12" | parody courier brand | "Deliveroo, Uber Eats, Takeaway and other…" | — |
| v09 | Living in a Metaverse (4/21) | Living in a [system] | dystopia | 2021-11-24 Wed | 359 | 2.66 M | 5.1 | 5.49 | 0.270 | one face split down the middle: happy virtual world / sad real city | 1 (+2 avatars) | none | real tech-company logo | "Facebook Metaverse is on its way…" | — |
| v10 | Gaming Addiction Cycle (3/22) | [activity] Addiction Cycle | addiction | 2023-01-29 Sun | 421 | 2.46 M | 4.7 | 3.40 | 0.166 | single centred hollow face, controller, game world blurred | 1 | none | real block-game imagery | "This Wojak meme video is about gaming addiction…" | — |

Measured thumbnail pixels (320×180 downsample): see §4.2.

---

## 3. Title anatomy

- **Length:** all 148: median 5 words / 25 chars (range 10–57 chars). Top 25: 3–6 words, **12–32 chars** (max 32). Word-count distribution (all): 3 w = 24, 4 w = 41, 5 w = 33, 6 w = 31, ≥7 w = 18.
- **First word:** "Life" 43×, "When" 15×, "Living" 10×, "Doomer" 5×. The title ends on the job / archetype / system / end-state noun in 8/10 corpus titles (exceptions end on "2050" and "Cycle").
- **Absent from all top-25 titles:** question marks, ALL CAPS, emoji, numbers other than a year ("2050"), brackets, clickbait adjectives ("insane", "shocking"). Casing is sloppy (only 17/148 titles are consistent Title Case) — not a factor.
- **What under-performs:** question titles n=5 median 517 K; parentheses n=10 median 420 K; "be like" n=13 median 356 K; titles led by the character's name n=17 median 423 K (only the saga escapes this, because "Doomer" there is the topic, not the actor).
- Sequels are **never** titled "Part 2" (one exception: "POV: You Live In An Apartment (Part 2)", 0.40 M vs 0.69 M for part 1). Sequels get a new self-standing promise ("From Doomer to Bloomer").

### 3.1 Reusable title templates (pattern → channel evidence; never reuse an exact title)
| # | Template | n | Median | Best | Note |
|---|---|---|---|---|---|
| T1 | Life of a [mass-market job] | 37 | 580 K | 4.93 M | pillar; strongest for entry-level jobs most viewers have held |
| T2 | Life of a [social archetype] | 7 | 804 K | 1.45 M | "Karen", "NPC", "introvert Gym Bro" |
| T3 | Origin of a [archetype] | 2 | 3.28 M | 6.39 M | once per archetype; 2026 reuse flopped (0.18 M) |
| T4 | From [negative archetype] to [positive archetype] | 3 | 1.51 M | 4.96 M | sequel slot |
| T5 | [Archetype]'s path to [positive state] | 1 | 4.43 M | 4.43 M | montage version of T4 |
| T6 | [Everyday domain] in 2050 | 5 | 1.31 M | 3.41 M | dating / gyms / food worked in 2023; gaming/AI in 2024–26 flopped |
| T7 | Living in a [system / place] | 4 | 1.64 M | 3.16 M | social credit, virtual world |
| T8 | Growing up in a [system] | 1 | 1.46 M | — | follow-up to T7 |
| T9 | [Activity] Addiction Cycle | 1 | 2.46 M | — | "Phase 1…" chapter cards inside |
| T10 | Living with a [addiction / difficult person] | 6 | 705 K | 1.16 M | phone addiction best |
| T11 | [state] in your 30's | 9 | 635 K | 1.37 M | era-adjusted best family now (1.86×) |
| T12 | The (dark) life of a [glamorous role] | 2 | 1.42 M | 2.08 M | "influencer" |
| T13 | [Attractive] vs [unattractive] [group] | 1 | 1.73 M | — | |
| T14 | [Archetype A] VS [Archetype B] at a family dinner | 2 | 1.20 M | 1.36 M | "…addict at a family dinner" |
| T15 | When you get addicted to [X] | 1 | 1.34 M | — | |
| T16 | When being [identity] isn't enough | 1 | 1.24 M | — | |
| T17 | [Group] nowadays | 1 | 1.09 M | — | |
| T18 | How not to [action] | 1 | 1.33 M | — | |
| T19 | [App / situation] be like | 13 | 356 K | 1.57 M | weak except dating apps |
| T20 | POV: You [situation] | 2 | 546 K | 695 K | weak |
| T21 | Why it sucks to be a [job] | 1 | 476 K | — | weaker than T1 in the same era (0.8×) |
| T22 | [Topic] Then VS Now | 1 | 195 K | — | anti-pattern |

---

## 4. Thumbnails

### 4.1 What was compared
Winners = the 10 corpus thumbnails (2.46–6.39 M). Mid = 6 fetched (warehouse 2.17 M, influencer 2.08 M, Uber 1.93 M, attractive-vs-unattractive 1.73 M, unemployed-30's 1.37 M, ghetto 0.62 M at 11 days). Losers = 8 fetched (janitor 0.14 M, alcoholic→bloomer 0.15 M, AI girlfriend 0.17 M, origin of an unemployed 0.18 M, retail manager 0.22 M, AI in 2050 0.31 M, doomer lifestyle 0.34 M, gaming in 2050 0.35 M). All viewed; pixel metrics computed on all 24.

### 4.2 Measured
| Group | Mean luminance | Mean saturation | Warm ≥15 % AND cool ≥15 % of saturated pixels | Dark (lum ≤0.30) + one cool hue ≥59 % | Title words in image |
|---|---|---|---|---|---|
| Winners (10) | **0.46** | 0.47 | **6/10** (top 4: **4/4**) | **0/10** | 0/10 |
| Mid (6) | 0.60 | 0.23 | 0/6 | 0/6 | 0/6 (one "HI….." speech text, one UI screenshot, one "Uber" wordmark) |
| Losers (8) | **0.38** | 0.54 | 1/8 | **4/8** (AI girlfriend 0.21, doomer lifestyle 0.20, AI 2050 0.26, gaming 2050 0.30) | 0/8 ("2050" numerals ×1) |

Per-thumbnail notes:
- **v01** L/R luminance difference +0.48 (largest of 24): warm daylight field left, dark rainy city right; heads ≈90 % of frame height; eye lines aligned.
- **v04** 50/50 split, sat 0.67, azure 43 % + red 31 %; red curved arrow across the top.
- **v02** clone layout of v04's logic (before → arrow → after) + mentor behind; the 2026 clone "From Alcoholic to Bloomer" uses the identical layout (arrow, mentor, dark city → green field) and got **0.15 M** (×0.4).
- **Origin of an Unemployed (0.18 M)** reuses v01's split, but heads are only 35–38 % of frame height, both faces neutral and both look right (no face-off, no expression contrast).
- **Job lineups** are identical across winners and losers: fast food 4.93 M, retail 3.46 M, warehouse 2.17 M vs janitor 0.14 M, retail manager 0.22 M — same 3-figure lineup, same exhausted centre face, same blurred workplace photo.
- Numbers as the only text: v07 score boxes (pixel font, white on black), v08 green "+$18", v05 outline "2050"; the same "2050" device on the 2024/2026 sequels flopped.

### 4.3 Conclusion on thumbnails
Inside this channel the thumbnail **grammar is constant** (cartoon figures on a real photo, no title words, exhausted face, parody uniform), so it cannot explain the 30× spread between winners and losers; **topic + timing + novelty of the template** do (clones of a past winner's layout lost 5–30×). The thumbnail's job is to be instantly legible: one idea, one contrast. Measurable avoidances: dark monochrome neon (0/16 winners+mid, 4/8 losers), small heads without expression contrast in split layouts.

### 4.4 Thumbnail rebuild spec (for original characters)
Canvas 1280×720, sRGB. Keep the bottom-right 230×110 px free (timestamp overlay). Characters: original designs, black outline 6–8 px, flat fills, one dominant white/pale face.
**Layout A — Transformation split (saga/origin titles)**
- Divider 8–12° off vertical, crossing the top edge at x 500–560 and the bottom at x 640–700.
- Same original character both sides, profile, facing each other; head height ≥60 % of frame (v01 ≈90 %); eyes on one horizontal line (±20 px).
- Left: real daylight photo (sky + field), warm skin tint, open-mouth laugh. Right: real night city photo, cold purple/blue rim light, flat mouth, purple eye bags, stubble, dark hood/beanie.
- Optional: red curved arrow (#E01B22-range, 6-px white outline) from left chest to right chest (v02, v04).
- Target metrics: |left − right luminance| ≥0.30; warm ≥15 % and cool ≥15 % of saturated pixels.
**Layout B — Workplace lineup (job titles)**
- 3 waist-up figures: centre protagonist head 20–25 % of width and 40–50 % of height, purple eye bags, flat mouth, parody uniform/logo; flankers 28–32 % of width each with contrasting expressions (smug, angry, mocking).
- Background: real photo of the workplace (exterior with sky preferred), Gaussian blur 8–15 px; foreground props of the job across the bottom 20–25 % (products, tools).
- Mean luminance 0.45–0.65; at least one warm prop/uniform colour against a cool sky.
**Layout C — System overlay (dystopia titles)**
- One central face 45–60 % of frame height + one diegetic device: score boxes, a recognition bracket, or outline year numerals (≤4 numeric tokens, white-on-black or neon outline, ≤25 % of height).
- Never dark-monochrome: mean luminance ≥0.35 and include a second hue ≥15 %.
**All layouts:** 0 title words; ≤4 numeric tokens; parody brands only; no real people's photos; small channel wordmark optional (≤3 % of height).

---

## 5. Description, tags, SEO, monetisation (data, not instructions)

**Skeleton used on 10/10 corpus videos and still in Oct 2026 (unchanged ≈5 years):**
1. 1–5-sentence keyword paragraph, usually opening "This Wojak meme video is about…" (7/10 + 3/3 recent). 5/10 name real brands or entities for search (fast-food chains; retailers; delivery apps; a tech company; a country).
2. Series line (only the saga): v01 links forward to the sequel ("Watch the sequel … here"), v02 links back in its first sentence (URL with `&t=10s`).
3. Channel membership link (from 2024: v04 and all 2025–26 checked) and, in 2026, a merch plush link.
4. Crypto donation block (BTC/ETH/ADA addresses) with an in-joke sign-off — on 10/10.
5. "New kid on the block… would be epic if one day I can become as great as [3 peer meme channels]" — names peer channels on 9/10 [inferred: keyword piggy-back on adjacent channels, med]. v07 adds a disclaimer of non-affiliation with a look-alike channel.
6. "Also being reposted online by others under the name 'Life of a guy'" (v01 only).
7. Socials (Instagram, Twitter, Reddit, TikTok) and "Music used" credits (10/10).
- **Tags:** one fixed 21-tag block (wojak, doomer, zoomer, boomer, chad, meme, crypto, cryptomeme, bitcoin, cardano, ethereum, btc, eth, ada, tradgirl, jimmy, low, budget, stories, story, zero) on 9/10 and on 2026 uploads; v09 has an 8-tag subset. Tags are not topic-specific → no evidence they matter.
- **Category:** Comedy on 10/10. **Chapters:** v02, v03, v10 and recent uploads have 5–6 summary-style chapters ("The drive-thru ordering", "Dealing with rejection") [inferred: auto-generated, med].
- **In-video packaging:** title card repeating the title at 16–23 s (v03, v06); "Phase 1 – …" chapter cards (v10); orange #ED720B end card 5–7 s with 2 end-screen slots on **10/10**; bottom-left watermark on 10/10; in-story self-plug (v03 feed post announcing the video).

### 5.1 Engagement ratios
| | Like/view | Comment/view |
|---|---|---|
| All 148 (median) | 3.52 % | 0.225 % |
| Top 10 (median) | 3.53 % | **0.125 %** |
| v01 / v02 / v03 / v04 / v05 | 3.55 / 4.36 / 2.69 / 4.36 / 3.36 | 0.103 / 0.109 / 0.142 / 0.108 / 0.079 |
| v06 / v07 / v08 / v09 / v10 | 2.69 / 3.78 / 3.52 / 5.49 / 3.40 | 0.168 / 0.231 / 0.089 / 0.270 / 0.166 |
| Family medians | saga 3.88 · dystopia 4.20 · job 3.06 · 30's 2.96 | job 0.198 · 30's 0.474 · saga 0.241 |

Like rate does not separate winners from the rest; **winners have about half the channel's comment rate** → their extra views came from people outside the commenting core [inferred: broad suggested/browse or off-platform reach, med].

### 5.2 What the comments say about clicking and sharing (400 top comments per video, regex-coded, likes summed)
| Theme | Strongest in | Count (likes) |
|---|---|---|
| Occupational testimony ("I worked at…", "accurate") | v03 | 104 (63,044 = 57 % of sampled likes) · v06 136 (32,101) · v08 61 (15,775) |
| "Respect the workers" stance | v03 | 43 (18,514) |
| Emotion / crying | v01 | 66 (14,864) |
| Wordless praise | v01 | 20 (15,837) — 0 in every voiced video |
| Meme-lore (mentor/Chad/Wojak) | v02 | 94 (54,264); v01 77 (27,843) |
| Dystopia fear / tech discourse | v07, v09 | top comments 17,000–19,000 likes each |
| Arrived from a short / repost | v01, v04 | v01: "who came here after that short video" 3,600 likes; a viewer spent an hour finding it from a short; v04: 10 comments (4,667) |
| Rewatch / "2026 is on" | v04 | 17 (934) |

---

## 6. Series & sequel chains
| Chain | Videos (date, views) | Linking |
|---|---|---|
| Doomer saga | Origin (2023-03, 6.39 M) → From Doomer to Bloomer (2023-07, 4.96 M, 109 days later, 0.78× parent) → Doomer's path to Happiness (2024-07, 4.43 M, standalone montage) → From Game Addict to Successful (2025-03, 1.51 M) → From Alcoholic to Bloomer (2026-01, 0.15 M) → Origin of an Unemployed (2026-06, 0.18 M) | bidirectional description links only between the first two |
| "in 2050" sprint | Dating (2023-04-09, 1.80 M) → Gyms (2023-05-07, 3.41 M, 1.89× parent) → Food (2023-05-28, 1.31 M) → Gaming (2024-03, 0.35 M) → AI (2026-01, 0.31 M) | title template only |
| Virtual-world chain | Living in a Metaverse (2021-11, 2.66 M) → Explaining it to a boomer (2021-12, 0.35 M) → Growing up in a Metaverse (2022-02, 1.46 M, 0.55× parent) → When you lose access (2022-10, 0.52 M) | none |
| Job series | food delivery (2022-05) … retail (2023-10-07) + fast food (2023-10-19, 12 days apart, 1.43× sibling) … fast-food **manager** (2025-07, 0.61 M), retail **manager** (2026-07, 0.22 M) | same template, same thumbnail lineup |
| "in your 30's" | parents (2025-10, 1.00 M) → unemployed (2025-12, 1.37 M) → dating, broke, lonely, renting, stuck, obese (0.26–0.81 M) | template only |

Pattern: a sequel/sibling released **within 1–4 months** of a hit kept 0.55–1.89× of the parent; the same template revived **after 12+ months** delivered 0.03–0.3× (Origin of an Unemployed 0.18 M vs 6.39 M).

---

## 7. Why did this channel get distributed (2023) vs why did people watch?

### 7.1 Distribution (reach) — mostly [inferred]
1. **Meme-currency timing [inferred, med]:** the characters (sad beanie doomer, NPC, Chad/Gigachad, Karen, zoomer) were the shared visual vocabulary of 2020–23 meme culture; the two biggest wordless films run on instrumental versions of songs that were popular "sad edit" sounds on short-video platforms at the time (credited in the descriptions). The packaging looked like content people already circulated.
2. **Off-platform reposts as a funnel [observed + inferred, med]:** the creator states v01 is reposted by others as "Life of a guy"; comments with 3,600 likes and the "spent an hour finding this from a short" testimony show short clips sending viewers to the long video.
3. **Language-free = global suggested traffic [inferred, med]:** v01/v04 contain zero words; v01's top comments include Spanish-language comments and viewers self-identifying as non-English-speaking; wordless praise appears only on the wordless films (20 comments, 15,837 likes on v01).
4. **Reach beyond the core [measured proxy]:** winners' comment rate 0.125 % vs channel 0.225 % — a typical signature of large non-subscriber audiences.
5. **Search-shaped titles for the job series [inferred, low–med]:** "Life of a [job]" literally matches how people search their own job; description paragraphs add real chain names (5/10). No search-traffic data to confirm.
6. **Session chains [inferred, med]:** theme sprints (3 dystopias in 7 weeks, 5 job episodes in 10 weeks) with identical thumbnail grammar make the next video the obvious "up next".
7. **2023 production step-up [observed]:** median duration 211 → 315 s, "serious" emotional storytelling (pinned creator comments on v09 2021 and v01 2023 call these deliberately more serious/cinematic; v04's pinned comment is a direct motivational message), cadence 13 days.

### 7.2 Why people watched (retention) — mostly [observed]
- One premise per video, legible from the thumbnail in <1 s (before/after; uniform lineup; score overlay).
- Universal loss/humiliation ladders (v01: one loss every ~20 s) and occupational recognition (v03: 57 % of comment likes are testimonies).
- Steady 19–20 cuts/min with holds only on loss/moral beats; music (saga) or comedic face states (job) doing the emotional work.
- Endings that pay off identity: rescue (saga), vindication (job), dread confirmed (dystopia).

---

## 8. Invariant packaging formula (present in ≥8/10)
1. Title 3–6 words, 12–32 chars, no question mark / caps / emoji / numbers except a year — **10/10**; ends on the job/archetype/system/end-state noun — **8/10**.
2. Thumbnail with zero title words (numbers allowed, ≤4 tokens) — **10/10**.
3. Thumbnail = thick-outline cartoon figures composited on a real photo or game screenshot — **10/10**.
4. At least one face in a negative state (exhausted, empty, grimacing, creepy grin, ruined half) — **9/10** (v08 neutral-focused).
5. Description: keyword paragraph naming the meme character/topic + donation block + music credits + socials — **10/10**.
6. Category Comedy, fixed tag block — **10/10**.
7. Duration 170–453 s — **10/10**.
8. Orange end card 5–7 s with 2 end-screen slots; bottom-left watermark on every frame — **10/10**.

## 9. Variations by format family
| Family | Title | Thumbnail | Duration | Voice | Engagement signature |
|---|---|---|---|---|---|
| Doomer saga (v01, v02, v04) | Origin of / From A to B / A's path to B | transformation split or arrow, 2–3 figures | 170–281 s | v01, v04 wordless; v02 voiced | like 3.55–4.36 %, comment ≈0.10 %, emotion + mentor-lore comments |
| Job series (v03, v06, v08) | Life of a [job] | 2–3 uniformed workers, workplace photo, parody/real logo | 211–453 s | voiced dialogue, 165 wpm (v03) | lowest like % (2.69–3.52), testimony-heavy comments |
| Dystopia (v05, v07, v09) | [X] in 2050 / Living in a [system] | overlay device (year, scores) or virtual/real split | 359–441 s | voiced (phone/system voices) | like 3.36–5.49 %, fear/discourse comments |
| Addiction (v10) | [Activity] Addiction Cycle | single hollow face + activity world | 421 s | voiced, phase title cards | like 3.40 %, "too realistic" comments |

## 10. Anti-patterns (measured on this channel)
- Cloning a past winner's thumbnail layout and title template after ≥12 months: From Alcoholic to Bloomer 0.15 M, Origin of an Unemployed 0.18 M, Retail Manager 0.22 M, AI in 2050 0.31 M.
- Dark monochrome neon thumbnails (mean luminance ≤0.30, one blue/cyan hue ≥59 %): 4/8 losers, 0/16 winners+mid.
- Under-2-minute memes/specials (median 139 K, 0.22× neighbours); "be like" skits (356 K); question titles (517 K); character-name-led titles outside the saga.
- Episodes stretched to 8–10.5 min (2025–26 median 447–512 s) while uploading every 7–10 days — coincides with the decline (confounded).
- Generic, untargeted tag block and peer-channel name-dropping in descriptions — no evidence of benefit; potential misleading-metadata exposure.

---

## Why it works
- **A title is a category, not a teaser:** "Life of a [job]", "Origin of a [archetype]", "[domain] in 2050" tell the viewer exactly which identity or fear the video is about; 25 of the top 25 titles are 3–6 words with the subject noun last.
- **The thumbnail is one contrast, readable in <1 s:** before vs after, worker vs workplace, face vs score. Grammar stays constant, so the topic does the differentiating.
- **Families + sprints + sequels** create session chains: 3 "2050" videos in 7 weeks, 5 job episodes in 10 weeks, a sequel 109 days after the #1 hit.
- **Shareable identity payoff:** testimony (job series), grief (saga), fear (dystopia) — the comment section becomes social proof, and short clips of the films travel off-platform.

## Rules to copy
1. [KOPYA] Titles: 3–6 words, 12–32 characters, ending on the job/archetype/system/end-state noun (or a year), no "?", no ALL CAPS, no emoji, no numbers except a year.
2. [KOPYA] Choose every title from a family template (T1–T18 in §3.1); avoid T19–T22 ("be like", "POV", "why it sucks", "then vs now").
3. [KOPYA] Never write "Part 2": a sequel gets its own promise ("From [A] to [B]", "[A]'s path to [B]").
4. [KOPYA] Thumbnails: 0 title words, ≤4 numeric tokens, original cartoon characters with 6–8-px outlines on a real (licensed/own) photo; pick Layout A/B/C from §4.4.
5. [KOPYA] For transformation thumbnails: head height ≥60 % of frame, eyes aligned, left/right luminance difference ≥0.30, opposite expressions.
6. [İYİLEŞTİRME] Reject a thumbnail if mean luminance <0.30 and one blue/cyan hue covers ≥59 % of saturated pixels (4/8 losers).
7. [İYİLEŞTİRME] Do not reuse a winner's exact layout for a different topic after >6 months; change at least the layout family or the central contrast.
8. [KOPYA] Runtime: wordless emotional films 170–280 s; voiced episodes 300–480 s; nothing under 120 s on the main channel.
9. [KOPYA] Put the exact title on screen as a title card between 15 and 25 s (after a wordless cold open).
10. [KOPYA] Use an end card of 5–7 s with exactly 2 end-screen slots (next video + subscribe) and one brand colour; keep a small watermark (≤5 % of height) bottom-left.
11. [KOPYA] Description: first 2 lines = premise + the real-world phrases a viewer would search (job name, situation); then prequel/sequel links in both directions; then chapters (5–6, story-beat names); then credits and socials.
12. [İYİLEŞTİRME] Tags: 8–12 topic-specific tags per video (job/archetype/situation + format) instead of one fixed block.
13. [ETİK] Do not name other creators/channels or real brands for keyword reach; use parody brand names in title, thumbnail, description and video.
14. [KOPYA] Sprint a family: release 3–5 videos of one family within 6–10 weeks, same thumbnail grammar, different topic.
15. [KOPYA] Publish a sequel or sibling within 30–120 days of any video that reaches ≥3× the channel median; link it from the parent's description and pinned comment.
16. [KOPYA] On every "serious"/emotional film, pin a 1–3-sentence creator comment about the intent or a direct message to the viewer (pinned on v01 9,300 likes, v09 8,700, v04 6,700 — exactly the three most "serious" corpus films).
17. [İYİLEŞTİRME] Cut and publish 2–3 vertical clips (the turn, the reveal, the moral) per film on your own short-form accounts with the long title in the caption — own the "repost" funnel instead of leaving it to re-uploaders.
18. [ETİK] Music: original or properly licensed; never instrumental covers of chart songs, even though they helped the original channel.

## Open questions
- Real CTR, impressions and traffic-source split per video (search vs suggested vs external) — not available without channel analytics.
- Whether thumbnails/titles were changed after upload (no history available); several old thumbnails look re-made in a 2024–26 style [inferred, low].
- Size of the off-platform repost ecosystem ("Life of a guy") — needs a TikTok/Shorts search.
- Whether the 2025–26 decline is driven by duration, cadence, topic fatigue or platform changes — needs analytics or controlled tests on a new channel.

---

## Packaging recipe (for a new channel with original characters)

**A. Title (pick one template, fill with an original subject)**
- Job pillar: `Life of a [job most viewers have done]` (3–6 words).
- Saga pillar: `Origin of a [archetype]` → sequel `From [archetype] to [opposite]` → montage `[Archetype]'s path to [state]`.
- Future/system pillar: `[Everyday domain] in 2050` / `Living in a [system]` / `Growing up in a [system]`.
- Life-stage pillar: `[Hard state] in your 30's`.
- Check: 12–32 characters, subject last, no punctuation except apostrophe.

**B. Thumbnail (1280×720)** — Layout A/B/C from §4.4; QA gates: 0 title words · ≤4 numeric tokens · main face ≥40 % of frame height · mean luminance 0.38–0.65 · warm ≥15 % and cool ≥15 % of saturated pixels (or explicit two-world split) · bottom-right 230×110 px clear · parody logos only.

**C. Description skeleton**
```
[1–2 sentences: original character + premise + 2–4 searchable real-world phrases, ≤300 characters]
Prequel: [title] – [URL]      Sequel: [title] – [URL]
Chapters: 00:00 [beat] / … (5–6)
Support / membership: [link]
Music & sound: [track – license]
Follow: [own socials]
```
Tags: 8–12 specific. Pinned comment: 1–2 sentences on the idea/effort + the sequel link when it exists.

**D. In-video packaging** — wordless cold open 15–30 s → title card at 15–25 s (exact title, heavy rounded caps, ≈60–70 % of width, 2–2.5 s) → story → 5–7-s end card in one brand colour with 2 end-screen slots.

**E. Series plan (first 6 months, 13–15 uploads)**
- Month 1–2: 4 job episodes (mass-market jobs), 1 saga origin film (wordless, ≈220 s).
- Month 3: 3 "in 2050" or "Living in a [system]" episodes in one sprint.
- Month 3–4: saga sequel (`From A to B`) 90–120 days after the origin, linked both ways.
- Month 5–6: double down on whichever family produced a ≥3× video (2–3 more in 6 weeks); drop templates that stay <0.7× for 3 tries.

**F. Cadence & length** — 1 upload every 10–14 days (2023 breakout cadence: median gap 13 d); voiced episodes 300–480 s, wordless films 170–280 s; master to −14 LUFS; 2–3 vertical clips per film on own short-form accounts within 48 h of upload.
