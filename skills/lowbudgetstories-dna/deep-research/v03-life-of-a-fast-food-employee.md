# v03 — "Life of a Fast Food employee" (nZvW71zWNwc) — per-second teardown
Analyst 1 · evidence: 51 sheets_1fps (0–452 s, all opened in order), 15 isheets (0–60 s @4 fps), single frames s0022/s0123/s0393/s0402/s0415/s0429, cuts.csv (150 cuts), metrics.json, silences.csv, transcript json (761 words with timestamps), audio16k.wav (own RMS/centroid/low-band/pitch analysis), heatmap.json, 400 comments, v.info.json.
Channel meme characters (Wojak, NPC, Karen, Zoomer, Chad-wannabe) are described for analysis only; every rule says "original character that fills this role".

---

## 1. Card

| Field | Value |
|---|---|
| Title | `Life of a Fast Food employee` — 6 words, 28 chars, inconsistent caps (lower-case "employee") |
| Upload | 2023-10-19 (Thu), 12 days after "Life of a retail employee" (3.46 M) |
| Views / likes / comments | 4,932,336 / 132,717 / ~7,000 (meta; info.json sample capped at 400) |
| Like/view · comment/view | **2.69 %** (lowest of the top 10, tied with v06) · **0.142 %** |
| Rank | #3 of 148 · 9.5× channel median · 4.2× median of its 10 nearest uploads |
| Duration | 452.4 s (7:32), 1080p25 |
| Category / tags | Comedy · fixed 21-tag channel block (not topic-specific) |
| Chapters (5) | 0:00 The drive-thru ordering · 1:57 Conflict at the window · 2:53 Service complaints · 4:28 Second customer interaction · 5:36 Final confrontation and review — generic, summary-style titles [inferred: YouTube auto-chapters, med] |
| Description essentials | L1: "This Wojak meme video is about the life of a fast food chain employee, whether you are working at McDonalds, Burger King, Wendys or another Food chain." Then the parody brand "McWages", the customer types ("drunk zoomers", "boomers who don't understand technology"), and a respect message. Donations, feedback paragraph, socials, music: Audionautix – Sneaky Snooper; Wayne Jones – Brain Trust; Noughts – Throwdown. |
| Metrics | cuts/min @≥8 = **19.9** (150) · median shot **2.28 s** · mean 3.0 s · max 11.5 s · shots <1 s: 4 · 1–2 s: 48 · 2–4 s: 63 · 4–8 s: 32 · ≥8 s: 4 · cuts per 30 s: 9/16/11/12/7/8/9/9/9/14/9/10/9/10/8 |
| Loudness | **−21.9 LUFS**, LRA 12.8 LU (7.3 dB quieter than v01) |
| Pauses ≥0.35 s | 22 (20.2 s total); dense cluster 327.9–333.5 (scene change into the counter chapter) |
| Speech | 761 words, speech segments 277 s (61 % of runtime) → **165 wpm** mean; segment range 48–342 wpm |
| Wordless blocks | 0–32.6 s (32.6 s) · 237.6–258.0 (20.4) · 277.7–290.3 (12.6) · 323.3–339.3 (16.0) · 406.6–430.5 (23.9) = **105 s (23 %)** |

**Thumbnail (1280×720, viewed):** group-photo lineup of 3 waist-up figures, no text. CENTRE (hero, head x≈505–775 = 21 % of width, head + cap y≈30–350 = 44 % of height, body ≈ x 280–1000): exhausted white face, purple eye bags, flat mouth, **red** cap and red/black polo with yellow "W". LEFT (≈30 % width): blonde woman with bun, dark-teal visor + uniform with "W", neutral face. RIGHT (≈32 %): curly-blond zoomer, round glasses, smug smile, green/red/brown striped polo. Background: real photo of blue sky + a **real** golden-arches pole sign "McDonald's — Billions and billions served" (x≈770–975, top 34 %), trees left. Foreground bottom 25 %: real food cut-outs (nuggets, burger, purple milkshake with whipped cream, fries in a branded red box). Measured: luminance 0.48, saturation 0.59, cyan 48 % + pink 22 % + orange 12 % of saturated pixels (warm 28 % / cool 37 %).
Mismatch with the video: the video uses grey uniforms, the parody brand "McWages", and at least one thumbnail figure (bun-haired woman in teal) does not appear as such [frame check, med]. The purple shake matches a mid-2023 viral fast-food drink trend [inferred, med].

**Heatmap (100 bins of 4.52 s) — top peaks mapped:**

| Rank | Window | Value | On screen |
|---|---|---|---|
| 1 | 0–5 s | 1.000 | sofa → phone lock screen "McWages — Your shift starts in 30 minutes wagie!" (start peak, partly re-start artefact [inferred]) |
| 2 | 5–9 s | 0.721 | sigh with closed eyes; TV game → TV off, black screen reflecting him |
| 3 | 417–421 s | 0.555 | phone feed: a news-meme account posts the counter fight; hero's shocked CU; tweet opens |
| 4 | 426–430 s | 0.535 | hero's crying-rage CU, then first replies scroll (reading time) |
| 5 | 421–426 s | 0.502 | tweet detail push-in (date "19/10/23" = upload day, 7,461 likes) |
| hills | 109–127 s | 0.20–0.22 | coupon-after-payment → rage colour ramp → forced grin → CLOSED sign |
|  | 222–245 s | 0.16–0.21 | the customer's mother arrives |
|  | 366–394 s | 0.27–0.38 | hero steps in for coworker, insult duel, cup in hand |
| trough | 190–208 s | 0.00–0.03 | 98-fries complaint set-up (counting, phone held up) |

---

## 2. Premise · the turn · emotional arc

**Premise:** one shift of a worn-out fast-food worker: four escalating customers and a contradictory boss — until he finally stands up for a bullied coworker and the internet takes his side.

**The turn:** 6:12 (372 s, 82 % of runtime) — the protagonist, until now only reacting, steps beside the harassed coworker at the register and orders the filming customer to pay or leave. Everything before is passive endurance; everything after is consequence and vindication.

| # | t | Label | Evidence |
|---|---|---|---|
| A | 0:00–0:16 | Dread | shift notification (3.5–5.0), sigh (6.75–7.75), game switched off (9.25–10), rehearsed forced grin in mirror (14.25–15.5) |
| B | 0:16–0:31 | Resigned entry | train commute, restaurant, title card (21–23.5), first CU at drive-thru (28.75) |
| C | 0:32–1:46 | Frustration | drive-thru ordering loop; faces go neutral → squint → rage (75–86, 6-s hold) → wet eyes (95–96) |
| D | 1:46–2:08 | Boiling point | coupon after payment; face white→pink→red with bloodshot eyes 120–124, snaps to forced grin 125–126; "CLOSED" sign 127 |
| E | 2:08–4:30 | Powerless absurdity | boss contradicts himself (130–169); straw, 98-fries, the Karen mother (171–244); night, break room, sent back (245–268) |
| F | 4:30–5:28 | Small win | stoned zoomers buy only a water, pay $20 for $2; he pockets the change with a sly grin (327) |
| G | 5:28–6:47 | Courage | filming influencer + gym bro refuse to pay and mock the coworker; hero intervenes (372), insult duel, gets a drink thrown on him (394), says the moral line soaked (401–406) |
| H | 6:48–7:24 | Vindication | viral post → fear (425–426) → five supportive replies (427–439) → soft smile (440–444) |

---

## 3. Beat sheet / visual script

### 3a. First 32 s (4 fps evidence; cut list from cuts.csv)
| t (s) | What happens | Scale / framing | Background | Motion / transition | On-screen text | Audio |
|---|---|---|---|---|---|---|
| 0.00–1.00 | fade in: plain white character on sofa with game controller, dark-grey tee, track pants | WS | real living-room photo | fade-in 1.0 s | — | game/phone SFX, centroid 3.0–3.8 kHz, −25…−29 dBFS |
| 1.00–2.20 | holds | WS | same | static | — | same |
| 2.20 cut → 2.25–3.50 | phone on cushion, screen wakes "5:00" | insert | real sofa photo | static | clock | notification SFX |
| 3.56 cut → 3.50–5.00 | **push-in on lock screen** | ECU insert | phone UI | push-in | **"McWages — Your shift starts in 30 minutes wagie!"** 5:00 PM, green "W" app icon | 4.3–6.0 hard mute (digital −∞) |
| 5.36 cut → 5.25–6.50 | eyes drift to phone | CU | living room | — | — | mute → small SFX |
| 6.75–7.75 | eyes closed (sigh) | CU | same | — | — | SFX |
| 8.48 cut → 8.50–9.00 | real TV with a block-building game | insert | real TV photo | — | game HUD | game SFX |
| 9.25–10.00 | TV off — black screen reflects him on the sofa | insert | same | — | — | click |
| 10.36 cut → 10.25–12.00 | looks aside, slides out frame R, camera pans to the painting | CU → pan | living room | pan R | — | **10.5–16.0 hard mute (5.5 s)** |
| 12.24 cut → 12.25–15.50 | mirror reflection (semi-transparent layer in a wooden frame): now in grey "W" visor, rubs eye; rehearses a toothy service grin 14.25–15.50 | MCU | bathroom/door frame | — | "W" logo | silence |
| 15.80 cut → 15.75–18.50 | illustrated train: hero on bench with phone; office woman + obese long-haired man in a pony-print T-shirt (**customer #2 foreshadowed**); shopfront slides past window | WS | illustrated train, real street through window | window parallax | shop sign | music in at 16.0 (−35 dBFS, ≈80 BPM) |
| 18.75 | whip blur | — | — | whip | — | music |
| 19.00–20.75 | from behind, facing the "McWages" restaurant (red roof, yellow "W" pole sign) | WS | real restaurant photo with parody sign | tilt up, character sinks out | "McWages" | music |
| 21.00–23.50 | **title card** scrolls down onto sky | — | real sky photo | scroll-in, 2.25-s hold | **"LIFE OF A FAST FOOD EMPLOYEE"** — heavy rounded black all-caps, ≈67 % of width (x 158–802/960), cap height ≈6.5 % (35/540 px), no box/stroke | music |
| 23.92 cut → 24.0–28.5 | through the pick-up window: grey NPC workers; hero walks into the kitchen | WS | real pick-up window photo, posters "What we're made of… 100% pure Bugs", "freshly brewed" | slow push | poster gags | music |
| 28.76 cut → 28.75–30.25 | hero CU with headset at drive-thru station | CU 3/4 | real kitchen photo (brick, fryers, window), darkened + vignette | — | "W" | music fades (−40 dBFS) |
| 30.60 cut → 30.5–31.75 | drive-thru monitor (real photo) shows a red 3D pickup at the order post | insert | real monitor photo | — | — | **drive-thru timer beeps** (centroid 2.4–2.9 kHz) |

### 3b. Rest of the film, per beat
| # | t | Beat | Who / scale | Background | Motion / transition | On-screen text | Audio |
|---|---|---|---|---|---|---|---|
| 1 | 0:32–1:37 | **Customer 1 (drive-thru):** greeting repeated 3×, sizes confusion (asks "medium", menu says "regular"), happy-meal confusion, total $12 | employee CU ↔ monitor insert, alternating every **0.5–2.0 s**; customer CU first revealed at 51.75 (red cap printed with the channel name mirrored, aviators, floral shirt, 3D red pickup); WS drive-thru exterior 97–99 | real kitchen; real drive-thru lane photo with "McWages" sign | hard cuts; slight push on monitor | menu post "Confirm…" | voices 97–245 wpm; beeps; low music bed |
| 2 | 1:37–2:08 | **Window + coupon:** hands over cash; customer produces coupon after paying, asks to cancel; employee's face colour ramps white → pink → saturated red with bloodshot eyes and gritted teeth (120–124), snaps to forced grin (125–126); "CLOSED — Sorry, we are closed" sign on window (127–128) | CU / WS window | real pick-up window photo | colour animation on the face layer | **"CLOSED"** | rage beat dialogue, f0 rises to 144 Hz |
| 3 | 2:08–2:50 | **Boss interlude:** asks to move inside — "No"; balding grey-haired manager then orders him to swap with coworker Josh ("I said you only do what I say"); 3-shot with grinning bald coworker (165–169) | MS 6-s hold (137–142), manager CU (143–147), 2-shot (159–163), 3-shot (165–169) | brighter real kitchen photo, brick wall, closed shutter | motion-blur whips at 164, 170 | name tag | segment f0 120–131 Hz |
| 4 | 2:50–3:10 | **Customer 2 at counter:** obese long-haired man in pony-print T-shirt; straw complaint → hero returns with pink straw (188) | tray OTS, CU | real dining-room photos (NPC extras incl. mobility scooter) | walk-ins | real cup/fries packaging visible | 92–115 wpm |
| 5 | 3:10–3:47 | **98 fries:** customer counted 98, "looked up on Google" there must be 100 (phone held up, 205–209) | OTS / CU alternation 2–5 s | same | whip-blur on customer at 204 | blank phone screen | 191–212 wpm |
| 6 | 3:47–4:05 | **Karen mother:** enters as blurred foreground (229–231), arms crossed; hero scared with sweat drop (240–244) | FG/BG two-shot | same | rack focus | — | f0 139–158 Hz on her lines |
| 7 | 4:05–4:11 | **Time skip:** same exterior photo day (245–247) → night (248–250, blue grade, lit sign, birds) | WS | real restaurant + pole sign | grade change, no cut | "McWages" | 20-s wordless block starts |
| 8 | 4:11–4:30 | break room without cap, eye bags, phone; manager appears in red fire-exit door (257–262), sends him back; exhausted CU | MS / WS | real break-room photo (microwave, kids-meal box) | — | EXIT sign | f0 88–125 Hz |
| 9 | 4:30–5:28 | **Customer 3 (night drive-thru):** sedan with four stoned zoomers orders only a water ("extremely beautiful bottle of water"), pays $20 for $2, "thanks bro, you too"; hero pockets change with sly grin (327) | monitor (blue night) ↔ CU; 3D sedan CU under glowing "W" sign (295–297); OTS hand-over 9.6-s hold (304.6–314.2) | real drive-thru, night | hard cuts | poster now "100% pure Bugs" | one zoomer line reads f0 ≈260 Hz (pitched-up voice) |
| 10 | 5:28–5:34 | empty counter WS (328–329), dining room at night from behind (330–333) | WS | real counter photo | — | menus | silence cluster 327.9–333.5 |
| 11 | 5:34–6:12 | **Customer 4 (counter):** man in brown monogram bucket cap + purple-tinted glasses holding a red party cup, and a bald goatee gym bro in a black tank top; refuse to pay, film the coworker ("say hi to the internet"), mock his uniform | 3-shot, OTS, CU; filming phone raised (356–368) | real counter with Scandinavian menu boards ("kr" prices) | hard cuts 1.4–3.7 s | menu text | 230–319 wpm, f0 78–94 Hz (customers) |
| 12 | 6:12–6:30 | **TURN:** hero appears beside coworker (372–373): "Pay or leave"; insult duel; coworker grins with relief (389) | 2-shot CU hero (angry brows) + coworker, **8-s hold** (376–383) | menu-screen bokeh | — | — | 241–342 wpm (fastest of film) |
| 13 | 6:30–6:47 | ECU red cup in hand (392–393); cup thrown, real cola-splash photo with motion blur (394); **black 2 s** (395–396); hero's face + shirt splattered brown (397–398); moral line delivered deadpan, coworker beside, **9.1-s hold** (399–408) | ECU / insert / black / 2-shot | brighter counter photo (white tiles) | impact cut to black | — | low rumble stinger 390–393 & 396–398 (energy <250 Hz 81–88 %), splash burst at 394 (−20.5 dBFS) |
| 14 | 6:48–7:24 | **Epilogue:** night exterior WS, hero alone on a bench with phone (408–409); CU tired (410–412); X/Twitter feed POV — a post by the channel itself announcing this video, parody posts by real public accounts, then a news-meme account posting the incident (413–417); shocked CU (418–419); tweet detail "0:57AM · 19/10/23", 7,461 likes (420–424); crying-rage CU (425–426); replies scroll 13 s (427–439) — five fictional users side with the employees, one using a Spanish-meme phrase; hero face: rage → surprise (431) → **soft smile 440–444** | WS / POV / CU | real night exterior; phone UI | push-in on phone | readable reply text ≈3 % of height | replies are voiced (430–440: 211–278 wpm) |
| 15 | 7:25–7:32 | end card: orange #ED720B, mascot, "LOW BUDGET STORIES", 4 handles, 2 end-screen slots, darkens at 451 | — | flat | — | handles | music up, −20 dBFS |

---

## 4. Script / communication mechanics

- **Structure = "one shift, four customers".** Customer bits run 96 s (C1: drive-thru 32–97 + window/coupon 97–128), 73 s (C2 + mother 171–244), 57 s (C3 zoomers 270–327), 72 s (C4 influencers 336–408); two boss interludes (130–169, 251–268) separate them. A cold-open (0–32 s) and an epilogue (408–444) bracket the shift. Every bit ends on a visual punchline: CLOSED sign, pink straw, the Karen's arrival, the pocketed change, the soaked uniform.
- **Escalation of hostility:** confusion (C1) → pedantry + family pressure (C2) → harmless absurdity that pays (C3, the breather) → humiliation + violence + publicity (C4). The breather (C3) sits right before the climax, a classic relief-then-hit spacing.
- **Dialogue gags are cognitive-friction jokes** that every service worker recognises: answering "yes" to an either/or question, the medium-vs-regular naming (comment 48 likes), the coupon after payment, the boss's contradictory order, counting fries. Background text gags reward pausing: "100% pure Bugs" poster, "wagie" in the notification, parody "McWages" name.
- **Silent acting carries the subtext:** the forced customer-service grin (rehearsed in the mirror at 0:14, reused at 2:05 and 3:16–3:20) is the film's central visual motif; comment "the clenched smile hiding … internal dying" (325 likes).
- **Callbacks:** obese customer seen on the train at 0:16 returns at 2:53; the mirror grin returns in front of each customer; the coworker swapped in at 2:45 is the one the hero defends at 6:12; the phone (opening notification) returns as the epilogue feed — the day starts and ends on a phone screen.
- **The moral is said once, plainly, by the soaked hero** (≈20 words, 401–406) and then multiplied by five voiced "public" replies — the message is delivered as social proof rather than preaching.
- **Withheld:** the customer's face is held back for 20 s (only a monitor image 32–51.5); the drink thrower's hit is cut to black (no impact frame); the hero never wins materially — the reward is reputation.
- **Self-promotion inside the fiction:** the first post in the epilogue feed is the channel announcing this exact video (413), and the viral tweet is dated the real upload day.

## 5. Visual grammar

- **Rhythm:** 19.9 cuts/min, median 2.28 s. Dialogue scenes use speaker/listener alternation at 0.5–2.0 s (drive-thru 32–60 s: 18 cuts in 28 s); holds of 6–11 s are reserved for (a) listening to the boss (137–142), (b) transactions (304–314), (c) the turn and the moral (376–383, 399–408). Densest bins: 30–60 s (16 cuts) and 270–300 s (14 cuts) — both drive-thru exchanges.
- **Framing:** CU 3/4 on the employee (head ≈45–55 % of frame height) for ≈50 % of shots; OTS for counter confrontations; WS photos of exteriors as scene-setters (97–99, 103, 127, 245–250, 302–304, 328, 408).
- **Compositing:** vector characters with thick black outlines on darkened/vignetted real photos; 3D-render vehicles; real product cut-outs (burger box, fries, PET bottle, banknotes, red party cup, cola splash). Background photos come from different real restaurants (Scandinavian "kr" menus at 344 and 399) — continuity is sacrificed for texture [observed].
- **Expression library for the hero (12 states):** neutral, annoyed (lowered brows), skeptical squint, rage (gritted-teeth grid), wet-eyed rage, pink rage ramp, forced grin, tired eye-bags, scared (sweat drop), sly grin, deadpan soaked, soft smile. The same pink rage ramp appears in v07 (222–223) — a channel device.
- **Transitions:** hard cuts; motion-blur whips (18.75, 164, 170, 204); grade-only time skip day→night on the same photo (245–250); impact cut to 2 s of black (395–396).
- **Colour:** daylight neutral (R−B ≈0.00…+0.05); night sections cool (R−B −0.02…−0.09 at 270–285 and 360–375); the rage ramp is the only saturated colour event on a character; end card jumps to saturated orange.
- **Watermark:** bottom-left YouTube glyph + "Low Budget Stories", white ≈70 % opacity, on all frames except black/end card.
- **Title card:** 21.0–23.5 s, exact title text, heavy rounded black caps on a sky photo, scroll-in (v06 uses the same device at 16–17 s with a "Low Budget Stories" subtitle).

## 6. Audio grammar

- **Voices:** 761 words. Pitch per word (autocorrelation, 40-ms frames): overall median f0 **110 Hz** (p10 86, p90 178). Most segment medians sit at 78–131 Hz (male register); the mother's lines read 139–158 Hz (low for a female voice); a few shouted or young-character segments read 178–400 Hz (octave errors possible) → most likely one or two male performers, pitch-shifted for female/teen roles [inferred, low–med]. Performance: deadpan employee vs exaggerated customers; the 362–389 s confrontation is the fastest delivery (230–342 wpm). Accent not verified (no listening test); a commenter singles out the first customer's voice as memorable.
- **Music:** low bed under dialogue; opening cue at −33…−35 dBFS from 16.0 s, ≈80 BPM; credited library tracks include a comedic pizzicato "sneaky" cue that the channel reuses across ≥7 videos (v03, v05, v06, v07, v10, 2025–26 uploads). End card music at ≈−20 dBFS.
- **SFX:** phone/game SFX in the cold open (centroid 3.0–4.7 kHz); **drive-thru timer beeps** under the window scenes (centroid 2.4–2.9 kHz; comments 1,600 + 290 + 156 likes single them out as authentic); cola splash at 394; low rumble stingers 390–393, 396–398.
- **Silence:** two hard digital mutes in the cold open (4.3–6.0, 10.5–16.0) make the dread beat feel airless; 2 s of black+silence after the throw; 22 pauses ≥0.35 s; 5 wordless blocks totalling 105 s.
- **Loudness map:** speech scenes −21…−27 dBFS RMS (2-s windows), night/break scenes down to −40 dBFS, integrated −21.9 LUFS / LRA 12.8 — under-levelled vs v01 (−14.6).

## 7. Retention devices & why viewers stayed / replayed / commented

| Device | Where | Evidence |
|---|---|---|
| 4-s relatable dread hook (shift notification calling the viewer a "wagie") | 0:03–0:05 | heatmap 1.00 / 0.72 in 0–9 s |
| Title card confirms the click promise after a wordless cold open | 0:21 | — |
| Episode variety: new customer archetype every 55–115 s | 0:32–6:47 | chapter list mirrors this structure |
| Occupational authenticity (beeps, sizes, coupons, Google fries) | throughout | relatable "I worked/I work…" comments: **104 of 400 top comments, 63,044 likes = 57 % of all likes in the sample**; top comment 23,000 likes (empathy), 12,000, 10,000, 9,900, 7,700 |
| Running facial motif (forced grin) | 0:14, 2:05, 3:16 | 325-like comment |
| Hero turn + moral | 6:12–6:47 | "Brought a tear to my eye when he defended his co-worker" 1,900; "6:44 … just because we wear this outfit…" 423; respect-workers comments 43 (18,514 likes) |
| Social-proof epilogue (readable replies) | 6:52–7:20 | heatmap 0.42–0.56 (people pause/rewind to read) |

Why it got **commented**: it invites testimony. Former and current workers prove membership by telling their own story; "respect fast food workers" is a low-cost moral stance that people sign under. This differs from v01 (grief/identity) and drives the highest comment/view in the top 3 (0.142 %).

## 8. Weaknesses / risks

1. **Real brand use:** real golden-arches sign in the thumbnail, real logos on cups/fries in the film (171–178), while the story uses a parody brand. Trademark risk; the thumbnail also mis-sells the uniform/cast. [ETİK]
2. **Real public figures in the fake feed** (celebrity and media accounts shown posting) — impersonation risk; the bald gym bro is read by viewers as a real influencer lookalike (comment 69 likes). [ETİK]
3. **Under-levelled audio** (−21.9 LUFS): YouTube does not turn quiet videos up; it plays ~7 dB below v01.
4. **Slow middle of act 1:** 0:32–1:46 ordering scene (74 s) and the 3:10–3:30 fries set-up have heatmap 0.00–0.10; the gags are good but each runs 1.5–2× longer than needed.
5. **Continuity breaks:** different restaurant photos between shots (menus change language/prices), uniform colours change between thumbnail and film; the viral-tweet caption contradicts what we saw (it says the drink was thrown on the customer) [observed; intent unknown].
6. Profanity and a crude insult in the climax — ad-suitability risk for a copy aimed at broad audiences.

## Why it works
- **Mass-identity topic:** an entry-level job that a very large share of viewers has done; the video turns their private grievances into public validation — the comment section is 57 % testimony by likes.
- **Simple, binge-safe structure:** dread cold open → title → 4 customers of rising hostility → one act of courage → public vindication; no lore needed.
- **Visual comedy carries voiced comedy:** CU face states (12) and the forced-grin motif land the joke even when the line is weak; cut alternation every 0.5–2 s keeps a 7.5-min dialogue piece moving at ≈20 cuts/min.
- **The ending is a reward the viewer can share:** "workers deserve respect" is the line people repeat in comments and reposts.

## Rules to copy
1. [KOPYA] Runtime 420–460 s for a "Life of a <job>" episode (v03 452 s, v06 453 s, v08 211 s is the short exception).
2. [KOPYA] Open with a 15–30-s wordless cold open at home: phone notification text that names the job and insults the worker in ≤10 words (readable 1.5–2.0 s at ≥4 % of frame height) → sigh → leisure switched off → mirror rehearsal of a forced grin. Use 1–2 hard mutes (1.5–5.5 s) inside it.
3. [KOPYA] Foreshadow one later customer in the commute shot (seen ≥2 min before their scene).
4. [KOPYA] Title card at 15–25 s: the exact video title in heavy rounded all-caps black, ≈60–70 % of frame width, on a sky photo, held 2–2.5 s, scroll-in.
5. [KOPYA] Structure: 4 customers (55–115 s each) + 2 boss interludes (20–45 s) + 30–40-s epilogue; order customers by rising hostility and place one harmless/paying customer directly before the climax.
6. [KOPYA] Each customer is a distinct original archetype (indecisive older driver, pedantic customer + over-protective parent, stoned young group, filming show-off + muscle sidekick) — original characters that fill these roles, each with one signature prop.
7. [KOPYA] End every customer bit on a visual punchline shot (sign, prop, pocketed tip, soaked uniform) held ≥2 s.
8. [KOPYA] In dialogue, alternate speaker CU and listener/insert every 0.5–2.0 s; keep overall cut rate 18–21 cuts/min and median shot 2.2–2.6 s; reserve 6–11-s holds for the boss, the transaction and the moral.
9. [KOPYA] Give the protagonist ≥10 expression states; reuse the forced service grin ≥3 times as the visual motif; use the white→pink→red rage ramp (4–5 s, bloodshot eyes, gritted teeth) once, snapping into the forced grin.
10. [KOPYA] Turn at 80–84 % of runtime: the protagonist defends a weaker coworker; the moral is one sentence of ≤20 words, said deadpan in a 7–10-s two-shot after he has paid a price (soaked, humiliated).
11. [KOPYA] Epilogue: in-world social feed shows the incident went viral; 4–5 fictional replies, each voiced and shown on screen for ≈2.5 s, all supportive; end on a soft smile held 4–5 s.
12. [KOPYA] Voice: 1–2 performers for all roles (pitch-shift for others), mean ≈165 wpm, confrontations at 230–340 wpm; keep ≥20 % of runtime wordless (5 blocks of 12–32 s).
13. [KOPYA] Lay authentic workplace SFX (timers, beeps, machines) under every workplace scene; they are the recognition trigger for insiders.
14. [KOPYA] Hide 2–3 background text gags (posters, app names) per episode for pausers.
15. [KOPYA] Put the channel's own "new video out now" post inside the in-world feed, dated on the real upload day.
16. [İYİLEŞTİRME] Master to −14 LUFS integrated (v03 −21.9) with dialogue at −18…−20 dBFS RMS.
17. [İYİLEŞTİRME] Cap any single gag loop (ordering confusion, counting) at ≤45 s; v03's 74-s ordering scene and 20-s fries set-up are the replay troughs.
18. [İYİLEŞTİRME] Keep one background set per location (or match menus/props) so continuity holds between shots.
19. [ETİK] Parody brand only — invented name, invented logo, no real logos on packaging, signs or thumbnails.
20. [ETİK] Fictional accounts only in any social-media mock; no real celebrities, media outlets or recognisable lookalikes.
21. [ETİK] Keep insults non-sexual and non-profane if the target is broad/ad-friendly distribution.

## Open questions
- Who voices the roles, and in what accent? Needs a listening pass; pitch data only suggests 1–2 male performers.
- Are the chapters auto-generated by YouTube or written by the creator (wording suggests auto)?
- Traffic split search vs suggested for "life of a fast food worker"-type queries — no analytics available.
- Whether the mid-2023 purple-shake trend in the thumbnail was deliberate topical bait.
