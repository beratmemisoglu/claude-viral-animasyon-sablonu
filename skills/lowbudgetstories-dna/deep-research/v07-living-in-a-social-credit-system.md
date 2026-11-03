# v07 — "Living in a Social Credit System" (SZ2YJCg8Ess) — per-second teardown

Analyst 4 (lens: edit rhythm + sound). Evidence: all 48 `sheets_1fps`, all 15 `sheets_intro_4fps`, single frames, `scdet_scores.csv`,
`rhythm_qa.py` (final run `qa4_v07`, montage of every boundary checked by eye), EBU R128 100 ms log, mid/side spectrograms
(`data/extra/a4_rhythm/spec_mid.png`, `spec_side.png`), transient detector, pYIN pitch per dialogue line, heatmap, top ~400 comments.
Timestamps `mm:ss`; `[inferred]` = interpretation with confidence.

---

## 1. Card

| Field | Value |
|---|---|
| Title | Living in a Social Credit System (dystopia format "Living in a …", names a real-world system = search + fear hook) |
| Views / channel median | 3,155,438 / 518,729 → **6.1×** channel median |
| Likes | 119,140 → **3.78 %** |
| Comments | 7,300 → **0.23 %** of views (2.6× the comment rate of v08; political-fear topic) |
| Upload | 2022-06-15 |
| Duration | 426.8 s (story 0:00–6:52.2, end card 6:52.2–7:06.8 = 14.6 s) · 1080p25 |
| Thumbnail | 1280×720. Background: European street photo graded saturated red (≈ #B00000–#E00000) with dark vignette. Centre: original-meme protagonist in black beanie/hoodie with orange ribbed collar, x 23–73 %, y 15–100 %, **forced toothy grin**, orange outer glow; an orange face-scan bracket (corners + 25 % translucent orange fill) around the head (x 33–70 %, y 15–82 %); above it a black rounded label with white pixel-font score **"548"** (x 43–61 %, y 0–14 %). Two grey NPC heads left and two right (lower half), each with a black score label (539, 712, x12, 39x) at y 30–45 %. CCTV cameras in both top corners (≈ 18 % of width each). No title text. Note: thumbnail says 548, the video's protagonist starts at 648. |
| Description | 1st sentence defines the real system (SEO), then a beat-teaser in questions ("Will he get a deal with a boomer? Will he get punished for seeking contact with …? Will he get a ride home by Chad in his audi?"), donations, socials, disclaimer of affiliation with a copycat channel, **music credits: Wayne Jones – Brain Trust; Audionautix – Sneaky Snooper; Ryan/Jazz loop music – Milk Coffee**. |
| Tags | identical 21-tag channel block (wojak, doomer, …) |
| scdet metrics (score ≥ 8) | 133 cuts, 18.69 /min, mean 3.19 s, median 2.58 s, max 14.7 s (= end card) |
| Calibrated edit metrics | 145 story boundaries (122 hard cuts, 15 reframes, 5 slide-pans, 3 dissolves) → **21.1 boundaries/min**; 146 story shots: p10 1.4 s · median 2.3 s · mean 2.8 s · p90 5.1 s · **max 8.7 s** (no story shot > 9 s) |
| Loudness | **−19.9 LUFS** integrated, LRA 11.9 LU, momentary p10/50/90 −33.7 / −20.9 / −17.5 LUFS |
| Pauses (−35 dB ≥ 0.35 s) | 13 pauses, 18.8 s total; dramatic silences 1:08.0–1:12.0 (4.0 s), 1:12.4–1:13.9 (1.5 s), 1:24.4–1:27.3 (2.9 s), 6:47.2–6:51.3 (4.1 s) |
| Speech | 835 words, 54.7 % of runtime voiced, first word 0:21.7, longest wordless stretch 31.2 s (1:24.2–1:55.4), 204 WPM inside turns (fastest in corpus) |

**Heatmap top peaks → screen**

| Rank | Window | Value | Screen |
|---|---|---|---|
| 1 | 6:07.2–6:11.5 | **1.000** | **The twist**: shot through the steering wheel → rack focus to a seat-back device with a social-network-style "f" logo, "CONTROL", Record/Play and a red recording light (6:02–6:09) → photoreal villain in a space jet, subtitle "What a shame." (6:10) |
| 2 | 0:00.0–0:04.3 | 0.887 | Opening: dark 3D-rendered living room, gamer on couch, HODL poster (start spike) |
| 3 | 6:45.6–6:49.9 | 0.716 | Wheel ECU with a red padlock (6:44–6:46) → rich driver's face turns **pink with bloodshot eyes**, black screaming mouth (6:49–6:51) |
| 4 | 3:16.4–3:20.7 | 0.629 | Bus: protagonist smirks at a woman, she frowns and types on her phone (filing the complaint) |
| 5 | 3:25.0–3:29.2 | 0.623 | Phone: "We have received a tip about the fact that you are harassing…" → shocked CU |
| 6 | 1:33.9–1:38.2 | 0.552 | Bus sign "REQUIRED CREDIT: 650", CU looking up, lock screen "CREDIT SCORE: 648" |
| 7 | 5:33.1–5:37.3 | 0.487 | "Because now the government can't hear us talking" → "Listen kid. This social credit system is an absolute hell." |
| 8 | 6:32.8–6:37.1 | 0.458 | ECU "…lowering your score by 500 points" → 499 |

Replay clusters on **score changes and the twist**; the 97-s car debate (3:56–5:34) is the low plateau (0.11–0.17).

---

## 2. Premise, turn, arc

**Premise:** a gamer living under a social credit score (648/1000) needs 650 to board a bus, earns +2 by staging a donation in front of a CCTV camera, loses 5 to a false harassment complaint, hitches a ride with a near-perfect 999 citizen who privately admits the system is hell — but the car itself was recording, so the 999 citizen falls to 499 and loses his car.

**The turn:** 6:02–6:09 — after "luckily this conversation cannot be monitored" (5:59–6:04), the camera finds the recording device in the car. The story flips from *the protagonist's* problem to *nobody is safe*, and the most-replayed second of the video sits on it.

| # | Time | Emotion | Evidence |
|---|---|---|---|
| 1 | 0:00–0:21 | Comfort → irritation | gaming, "1 URGENT MESSAGE" on TV 0:16.75, rage face 0:19 |
| 2 | 0:22–0:48 | Patronised | Governbot lecture, frown 0:30, clench 0:37 |
| 3 | 0:48–1:13 | Defiance → humiliation | taps "no, I deny" 0:52–0:54, threat, sweat 1:04, blue tears 1:05, 4 s silence 1:08 |
| 4 | 1:14–1:27 | Defeat | "blocked from playing video games for 7 days", TV goes black 1:20, slumped 1:25 |
| 5 | 1:33–1:43 | Blocked → scheming | bus requires 650, grin 1:42 |
| 6 | 2:27–3:05 | Smug success | staged donation under the camera, "650 points" 3:01 |
| 7 | 3:06–3:44 | Injustice → rage | complaint −5 → 645, "not possible to submit a counter notification" 3:34–3:41, pink face 3:43 |
| 8 | 3:53–6:04 | Envy → doubt → kinship | 999 driver's life, "fake life" jab 4:40, confession 5:35–6:04 |
| 9 | 6:02–6:52 | Dread → punishment | device, −500, padlock, pink rage, 4 s silence |

---

## 3. Beat sheet / visual script

### 3a. First 22 s at 4 fps (cold open is pure pantomime — no dialogue until 0:21.7)

| Time | Picture | Audio |
|---|---|---|
| 0:00.00–0:00.75 | Fade in from black. | — |
| 0:00.75–0:02.75 | WS 3D-rendered dark living room (black couch, red Persian rug, coffee table, window light, "HODL" poster); protagonist (grey ringer T-shirt, white face) seated with game controller. Static. | low thuds every ~0.7–3.5 s from 0:01.8 (game/music hits, centroid 115–160 Hz) |
| 0:03.12 | Cut MS on couch, slack face. | |
| 0:04.52 | Cut OTS: black silhouette head with rim light (right 35 % of frame) facing a TV that plays live block-game footage; TV blurred; 0:06.75 rack focus to TV. | |
| 0:09.52 | Cut MS; 0:10.0 slight push; 0:11.48 CU, eyes glance sideways. | hit 0:10.1 |
| 0:13.16 | Cut OTS TV (inventory screen 0:14, crafting 0:15.5); 0:16.12 cut tighter on TV. 0:16.75 TV overlay "1 URGENT MESSAGE / PLEASE OPEN YOUR PHONE" (white bold condensed caps on a black translucent band). | notification hit 0:16.9 (0.44 s) |
| 0:18.80 | Cut MS; 0:19.25 face → rage clench. | |
| 0:20.56 | Reframe: phone face-down on the rug (top view), cartoon hand grabs 0:20.75–0:21.25. | |
| 0:21.56 | Low-angle POV lifting phone; 0:21.75 phone in white hand: app header "WOJAK / CITIZEN-ID / CREDIT: 648/1000", blonde avatar, "MESSAGE FROM GOVERNBOT". | Governbot TTS starts 0:21.7 |

### 3b. Full beat sheet (cuts/min measured per beat)

| Beat | Time | Cuts/min | Picture | Audio |
|---|---|---|---|---|
| B1 Cold open | 0:00–0:21.6 | 25 | 3a. Locations: room, TV, phone only. | cue A (plucked, "sneaky" C-major-ish, ≈123 BPM estimate) low under game; no voice |
| B2 Governbot lecture | 0:21.6–0:48 | 18 | Phone in hand over blurred couch; message types on **word-by-word in sync with the TTS** (white card, black sans text); 0:26.04 cut to tilted ECU card; CU reactions 0:30–0:31, 0:36–0:39; text scrolls up as it fills. | female TTS f0 ≈ 140–150 Hz, 160–186 WPM (slowest voice = bureaucratic); 91 % voiced |
| B3 The choice | 0:48–1:14 | 25 | 0:48.25 options fade in: "▶ yes, I'll agree not to play video games for a week" / "no, I deny"; 0:51 rage CU; 0:52.25–0:54 thumb moves arrow to "no, I deny" (bold); threat text 0:55–1:02; worried CU 1:00; sweat drops 1:04; **blue tears + clenched teeth 1:05**; ECU card "…lower your social credit by 3 points. please choose again." 1:06–1:08; options again 1:08; crying 1:09–1:10; thumb on "yes" 1:11–1:12; crying 1:13–1:15. | UI tick hits 0:48.3, 0:52.9; **music fades out 1:05.5; 4.0 s silence 1:08.0–1:12.0** while he chooses; 1.5 s silence 1:12.4–1:13.9 |
| B4 Consequence | 1:14–1:27 | 28 | phone "excellent choice. You will now be blocked from playin…" 1:16; crying 1:18; 1:19 TV with overlay again, OTS silhouette; **1:20 TV black** (game killed); phone "…score remains the same by 648 points." 1:21–1:24; 1:25–1:26 MS slumped on dark couch. | voice only, no music (side channel = digital silence 1:06.5–1:26.5); clicks 1:15.1, 1:19.3, 1:24.0 (6.7–7.3 kHz UI ticks); silence 1:24.4–1:27.3 |
| B5 Street → bus | 1:27–1:46 | **32** | 1:27 stock NYC street, protagonist now in **black beanie + black hoodie** walks among a crowd, blurred woman foreground (depth layer); 1:29 dissolve to crosswalk WS with many original side characters and an in-joke storefront; 1:32–1:33 yellow bus, black sign with yellow border "REQUIRED CREDIT: 650"; 1:34–1:35 CU looking up; 1:36–1:37 rage, phone enters; 1:38 lock-screen ECU "13:09 / JUNE 11 – 2025 / CREDIT SCORE: 648" on pink-red wallpaper; 1:39 rage; 1:40 tired; 1:41 MS by bus; 1:42.08 reframe → grin (idea); 1:43–1:45 bus alone. | music returns 1:27 (cue B, dark/low); 0 % voiced; tonal "idea" chime 1:42.3–1:42.6 (2.6–2.7 kHz, 0.5 s) |
| B6 Tunnel deal | 1:46–2:26 | 25.5 | 1:46 storms through crowd; 1:47–1:49 graffiti tunnel (stock photo), angry walk; 1:50.9 reframe to tunnel WS, bearded homeless man sitting far; 1:51–1:55 approach; 1:55–2:18 dialogue in OTS / reverse-OTS, sliding between the two on one wide plate (slide-pans 1:58.4, 2:07.6, 2:16.0); 2:19–2:21 he stands, walks; 2:22–2:25.6 graffiti wall WS with a CCTV camera top-right, he sits under it. | music low-passed (side energy only < 1 kHz) under the dialogue = muffled bed; 50 % voiced; homeless voice f0 125–138 Hz, 219–265 WPM |
| B7 Staged donation | 2:26–2:43 | 25 | 2:26 protagonist enters left; 2:27–2:33 2-shot with CCTV top-right, hands a $10 bill, smug grin; 2:34 CU grin with banknote; 2:35.3 whip-blur reframe; **2:35.6 ECU CCTV camera**; 2:37.1 reframe back to grin; 2:39 2-shot; 2:40–2:42 homeless leaves. | brighter cue from 2:23 (full band); "Make sure to spend it on something good like a product from…" product-placement joke 2:31–2:38 |
| B8 Reward | 2:43–3:06 | 21 | CU; phone (13:14) "congratulations. We have noticed you donating money…" 2:44–2:48; smiling with phone 2:49–2:50; **"CREDIT 649" in green 2:51**; open-mouth laugh 2:52–2:53; "…our partner [store] noticed you promoting their company…" 2:54–2:58; laugh 2:59–3:00; **"650" green 3:01–3:03**; smug 3:04–3:05. | Governbot TTS; ding 2:43.4 (1.9 kHz) |
| B9 Bus complaint | 3:06–3:44.5 | **31** | 3:06 3D-render bus interior; 3:07–3:09 WS passengers (red-haired woman arms crossed, older man, glasses man); 3:10–3:11 CU; 3:12 young woman seated (brown hair, choker, tank top); 3:13 CU annoyed; 3:14 smirk; 3:15–3:16 she frowns, phone; 3:17–3:18 sad; 3:19 she types, disgusted; 3:20–3:21 smug; 3:22–3:23 tired + phone; 3:24–3:27 phone (13:25) "We have received a tip…"; 3:28–3:29 shocked CU; 3:30–3:31 she smirks; 3:32–3:33 **"645" red**; 3:34–3:35 sweating; 3:36–3:39 "…below a score of 700 points, it is not possible to submit a counter notification"; 3:40–3:41 sweat; 3:42 crying rage; **3:43 face turns PINK (≈ #F578B7) with bloodshot eyes** (max-rage colour); 3:44 blurred bus exterior (thrown off). | taps on her phone 3:16.4–3:19.4 (1.2–1.7 kHz clicks); full-band loud burst 3:43–3:53 (rage + ejection) |
| B10 Wall, car arrives | 3:44.5–3:56.3 | 20 | 3:45–3:47 WS alone against a red brick wall with an in-joke cursive graffiti; 3:48 CU sad; 3:49 a car door wipes the frame; 3:50–3:51 silver sports coupé, driver = square-jawed blond "Chad"-type (white shirt, gold watch); 3:52–3:54 driver side CU. | tonal hit 3:49.1 (car arrival); **0.5 s silence 3:54.9** before "Need a ride?" |
| B11 Car debate | 3:56–5:34 | **14** (dialogue) | Dark car interior, windows show moving graffiti video. **~8 camera set-ups cycled** for 97.7 s with no new location: frontal 2-shot, rear ¾, side, two singles, tight OTS, profile CU, doomer CU with blurred driver foreground; set-up changes are mostly quick reframes/slides (4:24.6, 4:26.3, 4:35.4, 4:53.0, 5:06.2, 5:09.6). 5:24–5:26 driver profile "Can you turn on flight mode"; 5:27–5:28 phone shows airplane icon. | cue C (stereo, harmonic 0.7–2.4 kHz pattern; jazz-loop character [inferred med: the credited "Milk Coffee"]); 82 % voiced; both male voices f0 86–103 Hz, 200–320 WPM within lines (rapid-fire debate) |
| B12 Confession | 5:34–6:02 | 10.7 | side angle 5:35–5:39; tight OTS 5:40–5:46; side 5:47–5:51; 2-shot 5:52–5:58; side 5:59–6:01. | **cue D enters 5:35 under "Listen kid"** (dark minor, louder: side −31…−33 dB vs −37…−41 before); sub boom 5:38.3 on "absolute hell"; 89 % voiced |
| B13 TWIST | 6:02–6:10 | 22.5 | 6:02 through the steering wheel; seat-back device "f CONTROL", Record ▶ / ■, **red recording light**; rack focus driver → device; ECU device 6:08–6:09. | music continues, no voice 6:04–6:10 |
| B14 Villain | 6:10–6:18 | 15 (2 boundaries) | photoreal suited man in a jet, purple-galaxy windows; white subtitles: "What a shame." / "The man had so much potential." / "Dump the social credit." — only subtitled voice in the video; 6:15.5 reframe to CU. | villain voice f0 ≈ 87 Hz, then a pitched-down monotone "operator" voice (pYIN floor ≈ 66–69 Hz, 0.7–3.5 st range) |
| B15 Punishment | 6:18–6:52.2 | 23 | 6:18–6:19 coupé front in tunnel, plate "999 CLUB"; 6:20 2-shot; 6:21–6:22 driver eye glance; 6:23–6:26 phone (tan hand) "CHAD / CITIZEN-ID … / CREDIT: 999/1000", airplane icon; "bad thinking and negative speaking" 6:21–6:26; 6:27–6:28 driver; 6:29–6:32 phone; **6:33 ECU "…lowering your score by 500"**; 6:34–6:35 driver; 6:36–6:38 ECU "…social credit score of 499."; 6:39–6:41 car in tunnel; 6:42–6:43 wheel CU; 6:43.8 reframe → ECU hub with **red padlock**; 6:45–6:46 wheel+lock; 6:47–6:48 2-shot; 6:49–6:50 driver face turns **pink**; 6:51 protagonist sweating + pink driver screaming. | robotic government voice; **4.1 s silence 6:47.2–6:51.3** after "Please step outside of the vehicle", ended by a 4 s low boom 6:51.5 |
| B16 End card | 6:52.2–7:06.8 | — | orange #ED710A card, original mascot (beanie) left, "LOW BUDGET STORIES" heavy black brush caps, social handles, end-screen slots (dark rectangle, light circle); fade to black 7:06. | **mono drum-led loop** (kick every 1.81 s ≈ 66 / 133 BPM). Spectral cross-correlation of the first 5.5 s of every corpus end card: **v03, v04, v05, v06, v07, v10 carry the identical outro audio (r = 0.93–1.00)**, and v08 uses the same loop as its delivery-montage bed (r = 0.80–0.92) → a fixed channel outro asset [measured; which credited title it is: unknown] |

---

## 4. Script / communication mechanics

- **Score as the plot engine.** Every turn is a number on a phone: 648 → (−3 threat) → 648 → required 650 → 649 → 650 → 645 → (≥ 700 needed to appeal) → 999 → 499. Seven numeric state changes in 6:52; viewers can follow the stakes with the sound off. Green numbers for gains (2:51, 3:01), red for losses (3:32), pink skin for maximum outrage (3:43, 6:49).
- **Device-voice as narrator.** The system speaks only through a typed phone card read by a female TTS ("Governbot") in polite customer-service register; the contrast between polite wording and punitive content is the satire ("You don't add any value to your society" became a 12,000-like comment quote).
- **Pantomime first, dialogue second.** 0:00–0:21 and 1:27–1:55 (31 s) are wordless; the protagonist says only 6 short lines in the first 3:50. The talking is done by the system, the homeless man and the driver.
- **Escalation by rule-reveal:** each scene reveals one more rule (games cost points → buses need 650 → cameras pay for charity → complaints need no proof → < 700 cannot appeal → private talk is recorded → the car is locked). Rules are delivered as UI text at the moment they bite.
- **Callbacks:** CCTV camera (2:22, 2:35.6) pays off as the in-car recorder (6:02); "flight mode" set-up at 5:24 → paid at 6:23 (airplane icon visible on the punished phone); the opening "urgent message" overlay repeats at 1:19; pink-face rage used for the protagonist (3:43) and mirrored on the driver (6:49).
- **Withheld:** what the government actually is; the woman's motive (never explained, makes the injustice sharper — 310-like comment calls it "the most infuriating part"). The villain who enjoys the result is the same overlord device as in v08 (a running channel antagonist).
- **Ending:** the "good citizen" falls 500 points; the protagonist only watches (sweating). No resolution, no moral voice-over; last sound is a 4.1 s silence and a boom.

---

## 5. Visual grammar

**Rhythm (measured).** Boundaries verified by eye on the full before/after montage (`data/extra/a4_rhythm/montage_boundaries.jpg`; per-shot table `shots.csv`, per-second map `seconds.csv`) and reframe/pan crops (`data/extra/a4_rhythm/reframe.jpg`, `reframe2.jpg`): of 20 non-hard-cut boundaries, 19 are real framing changes, 1 (2:25.6) is a marginal drift.

| Segment | Boundaries/min |
|---|---|
| 0:00–0:15 | 20 (first cut 0:03.12) |
| 0:15–1:00 | 22.7 |
| body 1:00–6:22 | 21.0 |
| last 30 s of story 6:22–6:52 | 20 |
| per minute of runtime | 22 · 29 · 23 · 27 · 14 · 13 · 17 · 0 (end card) |

The video is flat-fast for 4 minutes (22–29/min), **halves to 13–14/min for the car debate + confession (minutes 5–6)**, and re-accelerates to 17–22/min for the twist and punishment. Per beat: wordless/plot beats 25–32/min (B1, B3, B4, B5, B9, B6 with its slide-pans), dialogue beats 10.7–18/min (B2, B11, B12). Shot length: p10 1.4 s, median 2.3 s, mean 2.8 s, p90 5.1 s; only one story shot > 8 s (5:26.7, 8.7 s, two-shot in the car).

**Camera.** 71.3 % of runtime static composites, push-in 14.0 %, slide/pan 4.6 %, moving/animated backgrounds (car windows, crowd) 8.1 %. 15 quick reframes + 5 slide-pans replace extra shots: the tunnel dialogue and the car debate are staged on **one wide composite** and the virtual camera slides or zooms between the two speakers (shot/reverse-shot without a cut). Rack-focus is faked with blur layers (0:06.75 TV, 6:02 device).

**Backgrounds.** 3D-rendered interiors (living room, bus, car interior), stock photos (NYC street, graffiti tunnel, brick wall), stock video (block-game TV footage, moving windows). Characters are flat 2D cut-outs with 3–5 px black outlines, composited with drop shadow-free edges; depth from blurred foreground people.

**Colour as state.** Green numbers = gain, red = loss, pink face (≈ #F578B7) + red bloodshot eyes = injustice rage; blue tears = humiliation; sweat drops = fear. Grading shifts by location (warm living room, grey street, dark car) rather than by emotion.

**Text/UI.** Phone UI cards (white card, black sans, header "MESSAGE FROM GOVERNBOT", ID line, credit line) are the channel's "dialogue box"; lock screen with huge credit number; TV overlay band for alerts; subtitles only for the overlord (white sans, bottom centre). Watermark bottom-left on every frame incl. phone inserts. No title card, no chapter cards.

---

## 6. Audio grammar

**Music map (mid/side spectrogram + level; credited tracks: "Brain Trust", "Sneaky Snooper", "Milk Coffee" — all royalty-free library / free-loop sources; mapping by character [inferred, medium–low]).**

| Time | Cue | Character | Side level |
|---|---|---|---|
| 0:00–1:05.5 | A | plucked/pizzicato "sneaky" comedy pattern, bright partials 0.7–2.4 kHz, key estimate C major (conf. 0.56–0.71), tempo estimate ≈ 123 BPM | −37…−41 dB |
| **1:05.5–1:27** | **none** | music removed for the choice/consequence; 4.0 s + 1.5 s + 2.9 s true silences | digital silence |
| 1:27–1:53 | B | dark, low, sparse (street, bus) | −42…−45 |
| 1:54–2:23 | B low-passed | energy only < 1 kHz under the tunnel dialogue (muffled) | −44…−45 |
| 2:23–3:08 | A' | brighter full-band (staged donation, reward) | −37…−40 |
| 3:08–3:43 | B' | low bed in the bus | −38…−42 |
| 3:43–3:53 | hit | loud full-band burst on the pink-rage/ejection | — |
| 3:57–5:34 | C | harmonic jazz-loop pattern (car) | −35…−41 |
| **5:35–6:47** | D | dark minor (C minor estimate, conf. 0.46), **4–8 dB louder** than C — tension for confession, twist, punishment | −31…−33 |
| 6:47.2–6:51.3 | none | silence after the final verdict | — |
| 6:52–7:06 | outro | mono drum loop = the channel's standard end-card audio (identical in 6/10 corpus end cards, see B16) | mono |

**Ducking:** none. Music level 0.2–1.0 s before vs. after each speech-turn onset changes by a median +2.0 dB (no dip); voice sits a median **9.3 LU above the bed** by static mix level. Dialogue-heavy scenes simply get a quieter or filtered cue (tunnel low-pass, car jazz at −38 dB).

**SFX inventory (transients, spectral class, picture):** low game/music thuds 0:01.8–0:20 (centroid 115–160 Hz, every 0.7–3.5 s) under the gaming; alert hit 0:16.9 (TV overlay); UI selection ticks 0:48.3, 0:52.9, 1:07.6 (≈ 1 kHz, 50 ms); phone notification clicks 1:15.1, 1:19.3, 1:24.0, 3:03.9, 3:34.1, 3:37.6 (6.7–7.3 kHz, 70–120 ms) on every Governbot card; "idea" chime 1:42.3 (2.6 kHz, 0.5–0.65 s); sustained musical hit 1:51.0 (2.2 s) entering the tunnel; camera/notification chimes 2:15.8 (4.2 kHz), 2:43.4 (1.9 kHz); typing clicks 3:16.4–3:19.4 (woman filing the complaint); chime 3:22.4; car-arrival tonal hit 3:49.1; sub boom 3:56.7 (82 Hz, 0.7 s) as he gets in; sub boom 5:38.3 (1.35 s) on "absolute hell"; impact 6:15.9 on "Dump the social credit"; lock clicks 6:44.8–6:45.2; 4 s boom 6:51.5 after the final silence. ≈ 3.2 detectable non-voice hits per minute; **every Governbot card gets a high click, every reveal a low boom**.

**Voice.** TTS ensemble, high confidence: 0 fillers in 835 words; uniform inter-line gaps (pause median 0.44 s, same as v02/v05/v06/v09); per-line pitch range 3.5–10 st for the male voices (flat read-out prosody); commenters across the channel call the voices "AI voices", "TTS", "voice bot", and one notes the government bots are made "even more robotic". Casting by voice preset: female assistant for the state (f0 ≈ 140–150 Hz [pitch under music, medium]), two similar young-male voices (f0 86–103 Hz) for protagonist and driver, a higher, rougher male for the homeless man (125–138 Hz), pitched-down monotone male for the government enforcement lines (≈ 66–69 Hz floor, 0.7–3.5 st). Rate: Governbot 140–186 WPM; car debate 200–320 WPM inside lines (lines overlap with < 0.4 s gaps) → the debate is dense and fast even though the picture slows down. Processing: dry, constant level (momentary −17…−20 LUFS per line), no room tone.

**Loudness map.** cold open −28 LUFS momentary median (quiet, game-bed only), dialogue scenes −17…−19, wordless street −31 (music only, low), confession/punishment −17…−18 with louder music, end card −15.

**Silence usage.** Silence is reserved for **decisions and verdicts**: the 4.0 s choice pause (1:08), the post-punishment slump (1:24.4), the beat before "Need a ride?" (3:54.9) and the final 4.1 s after the car is locked (6:47.2). Each is followed by a hard re-entry (voice or boom).

---

## 7. Retention devices and why viewers stayed / replayed / commented

| Device | Time | Evidence |
|---|---|---|
| Numeric stakes on screen (7 score changes) | 1:38, 2:51, 3:01, 3:32, 6:33, 6:36 | 4 of the 8 heat peaks are on score/verdict screens |
| Rule-reveal injustice | 3:34–3:41 | "Since you are below 700 points you are not allowed to submit a counter notification — that's scary" (851 likes); "the most infuriating part is when the girl got the guy's score reduced for just looking at her" (310) |
| Quotable system line | 0:55–1:02 | "'You don't add any value to your society' — said the government bureaucrat" (12,000) |
| Sympathetic underdog | 1:51–2:42 | "the homeless boomer was the most happy character" (9,100) |
| Twist (surveillance everywhere) | 6:02–6:11 | heatmap max 1.000 |
| Debate monologue as thesis | 5:35–5:56 | quoted verbatim in a 1,400-like comment; "5:38 Chad is right" (360) |
| Real-world fear framing | whole | top comment "legit scarier than any horror movie" (17,000); big-tech capability (13,000); "1984-tier dystopia using only memes" (7,500); Black Mirror comparison (806) |
| Series demand | — | "More of Wojak in the social credit hell please" (828), "Can we get more of these?" (1,100) |

---

## 8. Weaknesses / risks

1. **97.7 s car debate at 14 cuts/min with 82 % speech** (3:56–5:34) — the lowest-replay plateau of the video (heat 0.11–0.17); the talk is fast (200–320 WPM) but the picture cycles the same 8 set-ups.
2. Real brands and likenesses: a named online retailer as "partner", a car maker's model, a social-network logo on the recorder, a photoreal real person as the overlord. [ETİK] — never copy.
3. Real-country political topic (named state in the description) — demonetisation/ban risk in some markets; comments turn political (cancel-culture debate).
4. Thumbnail score (548) contradicts the story (648) — minor continuity slip.
5. 14.6 s end card is long relative to v08 (6.4 s) and adds nothing; the outro loop is generic.
6. Pitch-similar TTS voices for protagonist and driver (both ≈ 95 Hz) make the 97-s debate harder to follow by ear.

---

## Why it works

- The abstract system is made concrete as **one number on a phone** that changes 7 times; stakes are legible in 1 s.
- The cut rate is high (21/min) where the story moves by pictures and drops (10.7–14/min) where the argument is spoken — the eye rests when the ear works.
- Silence is spent only on decisions and verdicts (4 windows, 1.5–4.1 s), so each one reads as a punch.
- The twist recontextualises the safest character (999 citizen) and lands on the most replayed second.
- Polite machine voice + punitive content = satire that produces quotable lines and fear-comments (0.23 % comment rate).

## Rules to copy

1. [KOPYA] Externalise the dystopia as one on-screen number (score/credits/rank) with ≥ 6 changes in a 6–7 min story; show every change as a phone/UI insert of 1.5–3 s, green for gains, red for losses.
2. [KOPYA] Open with 15–25 s of pure pantomime in ≤ 3 locations at 20–25 cuts/min; the first spoken line is the system's message, arriving by an alert overlay (white bold caps on a black translucent band).
3. [KOPYA] Make the system speak through a typed UI card read by a polite female assistant-style TTS at 150–185 WPM, text revealed word-by-word in sync with the voice; one high UI click (6–7 kHz, ≤ 120 ms) per card.
4. [KOPYA] Rhythm: 20–25 boundaries/min for wordless/plot beats; 10–14/min for dialogue beats > 60 s; never hold a story shot > 9 s; stage dialogue on one wide composite and switch speakers with quick reframes/slides (≥ 1 per 10 s of dialogue).
5. [KOPYA] Reserve silence (music and SFX out, ≤ −45 LUFS) for decisions and verdicts only: 3–4 windows of 1.5–4.5 s, each ended by a voice line or a low boom.
6. [KOPYA] Remove music for the protagonist's punishment scene (choice → consequence) and bring a darker cue back on the next location cut.
7. [KOPYA] Switch to the darkest, loudest cue (4–8 dB above the previous bed) at the start of the confession/twist act (last 20 % of the story) and keep it to the final verdict.
8. [KOPYA] No sidechain ducking: set dialogue beds 8–10 LU below voice; for long dialogue scenes low-pass the bed (< 1 kHz) instead of turning it off.
9. [KOPYA] Plant the twist device twice before it pays off (camera on the wall, privacy request) and reveal it with a rack-focus from the speaker to the device (≥ 3 s) followed by the overlord's 3-line reaction.
10. [KOPYA] Integrated loudness −20 ± 1 LUFS, LRA 11–12 LU for dialogue-led dystopias.
11. [İYİLEŞTİRME] Cap any single-location dialogue at 60 s or intercut it (cutaways to the score, the city, the overlord) to avoid the 3:56–5:34 plateau; keep ≥ 15 boundaries/min there.
12. [İYİLEŞTİRME] Cast clearly different voices (≥ 4 semitones apart in median pitch, or different accents) for any two characters who debate.
13. [ETİK] Use an invented country/system name, invented companies (no real retailer, car maker or social-network marks), and an original character that fills the "bored all-powerful overlord" role — never a real person's photo.
14. [ETİK] Replace the channel's meme cast with original characters that fill the same roles (tired everyman, rich perfect citizen, cheerful outcast, accuser).

## Open questions

- Which credited track is cue A vs. D ("Sneaky Snooper" vs. "Brain Trust")? Needs listening; spectral mapping only gives character.
- Is the mono outro drum loop (identical end-card audio in v03–v07 and v10, montage bed in v08) the credited "Milk Coffee" jazz loop or an uncredited channel signature?
- Exact TTS vendor/voices cannot be determined from the audio; accents and flat prosody only establish "synthetic".
