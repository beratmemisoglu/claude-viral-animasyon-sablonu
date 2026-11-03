# v08 — "Life of a food delivery driver" (zj9H9bOmP14) — per-second teardown

Analyst 4 (lens: edit rhythm + sound). Evidence: all 24 `sheets_1fps`, all 15 `sheets_intro_4fps`, single frames, `scdet_scores.csv`,
`rhythm_qa.py` run (`qa2_v08`), EBU R128 momentary/short-term log (100 ms), mid/side spectrograms
(`data/extra/a4_rhythm/spec_mid.png`, `spec_side.png`), transient detector, pYIN pitch on every dialogue line, heatmap, top ~400 comments.
Timestamps `mm:ss`. `[inferred]` = interpretation, with confidence.

---

## 1. Card

| Field | Value |
|---|---|
| Title | Life of a food delivery driver (series format "Life of a …", 5 words, no hook word, no number) |
| Views / channel median | 2,823,273 / 518,729 → **5.4×** channel median (148 uploads) |
| Likes | 99,460 → **3.52 %** of views |
| Comments | 2,500 → 0.089 % of views |
| Upload | 2022-05-04 (one of the earliest corpus videos; v09 2021-11 and v07 2022-06 are the same era) |
| Duration | 210.5 s (story 0:00–3:22.4, black 1.7 s, end card 6.4 s) — **shortest voiced video in the corpus** |
| Technical | 1920×1080 **50 fps** (only 50 fps file in the corpus; all others 25 fps) · AAC 128 kb/s stereo 44.1 kHz |
| Thumbnail | 1280×720. Two original-meme couriers on bikes fill the left ~75 % of width, faces at ~25–45 % height: front rider orange cap/jacket/backpack with parody logo "TAKEAWAGE" (orange ≈ #EB7E14), second rider cyan jacket + white/cyan helmet. Background split: left half a light street-map, right half motion-blurred sky/greenery. Right third: three green (≈ #10EA3F) money ticks with 6–8 px black outline stacked and shrinking: "+$18" (~17 % of frame height), "+$5,3", "+$12". No title text, no red/negative cue — the thumbnail sells the *promise* (money + freedom); the video sells its destruction. |
| Description | 1st sentence = SEO (names Deliveroo, Uber Eats, Takeaway, "fast food delivery"), 2nd–4th = logline ("Wojak tries it out. He quits his job at McDonalds and becomes a … driver"), then crypto-donation block, socials, **music credits: "Audionautix – I like Peanuts", "Villain Music No Copyright"**. |
| Tags | 21 generic channel tags (wojak, doomer, zoomer, boomer, chad, meme, crypto…, low, budget, stories) — identical block to v07; no topic tags. |
| scdet metrics (score ≥ 8) | 61 cuts, 17.39 /min, mean shot 3.40 s, median 2.65 s, max 14.8 s (the max includes black frames) |
| Calibrated edit metrics (`rhythm_qa.py`, see §5) | 66 boundaries in the story 0:00–3:25.5 (56 hard cuts, 8 "reframes" = 0.16–0.4 s virtual-camera jumps, 1 dissolve, 1 from-black) → **19.3 boundaries/min**; 65 story shots: p10 1.1 s · median 2.4 s · mean 3.0 s · p90 6.2 s · max 9.5 s |
| Loudness | **−16.6 LUFS integrated**, LRA **9.6 LU** (lowest LRA of the corpus), momentary p10/50/90 −36.2 / −19.0 / −14.0 LUFS; true digital silence only at 0:00–0:00.6 |
| Pauses (silencedetect −35 dB ≥ 0.35 s) | 16 pauses, 9.2 s total — none ≥ 1 s; the music never stops except 3:06.9–3:11.4 (§6) |
| Speech | 221 words, 31.7 % of runtime voiced (lowest voiced share in corpus; v01/v04 have 0 %), first word 0:03.5, longest wordless stretch 26.2 s (1:24.8–1:51.0) |

**Heatmap ("most replayed") top peaks → screen**

| Rank | Window | Value | What is on screen |
|---|---|---|---|
| 1 | 3:01.5–3:03.6 | **1.000** | Hospital: phone ECU push-in on a news article "Share meal deliverers not insured for liability: 'Risks are enormous'" (3:01–3:02), then rage-crying CU with red eyes in the defeated black-beanie costume (3:03). Payoff of the accident that was **never shown** (2:57–2:58 = empty road). The 2:57–3:05 window averages 0.58. |
| 2 | 0:00.0–0:02.1 | 0.497 | Fade-in + lateral slide reveal of the fast-food counter (start spike, present in every corpus video). |
| 3 | 0:50.6–0:52.8 | 0.355 | Phone UI "TAKEAWAGE – Welcome to Takeawage / Become a driver now! / - Decent money / - Cool bike / - No annoying boss / - Better than McWages" + orange "Apply for job" → text that needs a pause to read (joke list). |
| 4 | 2:25.6–2:27.7 | 0.266 | "NEW ORDER! 32min away, you got this!" route map → cut to crying courier on a London-style street. |
| 5 | 2:12.9–2:15.0 | 0.218 | Villain CU, subtitle "Turn on rainfall." (first sabotage command). |
| 6 | 2:06.6–2:08.7 | 0.195 | Villain reveal after 5.6 s of black: subtitle "What?" |

Replay is concentrated after the turn: mean heat 0:00–2:00 = 0.10, 2:00–3:10 = 0.30.

---

## 2. Premise, turn, arc

**Premise (one line):** a fast-food cashier quits to become a bike courier and is briefly happy — until an all-powerful puppet-master watching from a jet in space notices the happiness and sabotages him command by command, ending in hospital and finally replacing every courier with drones.

**The turn:** 1:58.7 the courier says the dramatic-irony line *"How can this go wrong?"* → hard cut to **5.6 s of pure black** (2:00.8–2:06.4) with a sub-bass hit at 2:00.9 → fade-in on the villain: *"What? He is enjoying his new job?"* (2:07.8). Everything before is setup (2:00 of the 3:30), everything after is escalation.

| # | Time | Emotion (protagonist) | Evidence |
|---|---|---|---|
| 1 | 0:00–0:21 | Humiliated / fed up | forced teeth-grin at 0:04, threat line 0:08–0:12, tired CU 0:16 |
| 2 | 0:23–0:35 | Hope (idea) | sees a courier through the window 0:23–0:26, grin 0:26.5, "That's it." 0:26.7 |
| 3 | 0:40–0:47 | Defiance | pouting CU 0:40, throws cap off 0:42.8–0:43.5, walks out 0:44.4 |
| 4 | 0:50–1:03 | Euphoria | "You are hired!" 0:53.5, sunburst dress-up 0:59–1:03 |
| 5 | 1:09–1:58 | Contentment | friendly customer + tip 1:13–1:17, montage 1:28–1:47, bench "I love this job" 1:51 |
| 6 | 2:00–2:06 | Dread (viewer) | black screen + drone |
| 7 | 2:16–2:47 | Escalating misery | rain + tears 2:17–2:20, 30–32 min orders 2:24–2:30, ECU crying 2:32–2:33, "I didn't order this" 2:43–2:47 |
| 8 | 2:51–3:03 | Catastrophe | blind-NPC car 2:52–2:54, empty road 2:57, hospital 2:59–3:03 |
| 9 | 3:04–3:22 | Cosmic irony | "prepare for plan technological automatization" 3:07–3:11, drone army 3:12–3:22 |

---

## 3. Beat sheet / visual script

Legend: CU close-up, MS medium, WS wide, ECU extreme close-up, OTS over-the-shoulder. "Photo" = static stock photograph used as background with 2D cut-out characters composited on top; "video" = moving stock footage background. Cut rate per beat measured by `rhythm_qa.py`; loudness = median momentary LUFS.

### 3a. First 20 s at 4 fps

| Time | Picture | Audio |
|---|---|---|
| 0:00.00–0:01.00 | Fade from black (luma 1→76/255 in 1.2 s) **combined with a lateral slide**: two blurred foreground customers (blonde in blue top; man in green "69" jersey) slide out right→left revealing the counter. WS. Background: stock photo of an Asian fast-food counter, menu boards, promo stands. Cashier (original cap with yellow "W", red polo "I'm wagin' it" parody) centre, glasses co-worker left, customer in blue floral shirt holding an energy-drink can right. | Playful music bed from 0:00.4, side −38 dB |
| 0:01.00–0:03.70 | Same WS, static. | music only |
| 0:03.72 | **Cut** MS cashier forced teeth-grin, customer blurred at right edge (OTS). | TTS male: "We are really sorry for the long waiting time." (0:03.5–0:05.9) |
| 0:06.16 | Cut WS 2-shot. | "Your order will be here soon." |
| 0:07.96 | Cut CU customer (reverse angle: restaurant seating + self-order kiosk photo); bespectacled man in suspenders walks behind him 0:09–0:13 (moving cut-out = life in background). | Customer threat line 0:08.2–0:12.6 (f0 122 Hz, 8.7 st range — most animated voice of act 1) |
| 0:13.36 | Cut WS; dark blurred silhouette crosses foreground left 0:13.25–0:14.0 (foreground wipe); customer walks out right 0:14–0:15.75. | music only, 3 s |
| 0:16.04 | Cut MS cashier, tired eyes. Red-shirt figure crosses blurred foreground 0:19.25–0:20.75. | "I hate this job and these people so much." 0:16.2 · "I have to find something better…" 0:18.5–0:21.1 |

### 3b. Full beat sheet

| Beat | Time | Cuts/min | Picture (who, scale, background, motion, text) | Audio |
|---|---|---|---|---|
| B1 Cold open at the counter | 0:00–0:16 | 15 (4 cuts) | see 3a | cue A (light, playful), voice 52 % |
| B2 "I hate this job" | 0:16–0:26.3 | 17.5 | MS cashier; 0:23.40 cut to WS reverse: blurred queue foreground, courier in teal jacket/backpack ("DELIVER CONSOOM" parody) picking up an order through the restaurant; 0:24.96 quick reframe closer on courier (push). | −17 LUFS, voice 45 % |
| B3 The idea | 0:26.3–0:35.9 | 12.5 | 0:26.32 CU cashier, smile grows to open-mouth grin by 0:26.5 with slow push-in; 0:30.76 reframe to MS smiling; 0:33.3 pout of resolve; customer re-enters right 0:35.5. | chime-like tonal hit 0:26.9 (1.6 kHz centroid) on the grin; monologue 0:26.7–0:35.0 (88 % voiced) |
| B4 Quitting | 0:35.9–0:47.7 | 20.3 | 0:36.76 WS 2-shot; 0:38.76 MS cashier OTS customer; 0:40.08 reframe to CU pout; 0:42.8–0:43.5 hand rips cap off → bald head, angry brow; 0:44.44 WS cashier exits left, **customer left alone at the counter 0:45–0:47.7 (3 s comic hold, no dialogue)**. | customer: "Do you have my happy meal" / cashier: "I don't work here anymore…" (0:36.0–0:44.1); hit at 0:42.9 on the cap throw |
| B5 Applying | 0:47.7–0:56.9 | **39** (fastest of act 1) | 0:47.72 exterior: red brick wall, "McWages" sign + golden arches, green exit sign; MS ex-cashier contemplative; 0:49.32 reframe, phone enters hand. 0:50.12 phone-in-white-cartoon-hand over grey cobblestone photo (insert): orange app "TAKEAWAGE" (house + $ logo), list "- Decent money / - Cool bike / - No annoying boss / - Better than McWages", orange button "Apply for job". 0:51.84 back to face (sly). 0:52.80 ECU thumb presses button → 0:53.5 button turns green (#10EA3F) "You are hired!", 0:55.25 "*Shift starts tomorrow 8am". 0:55.68 CU big grin; motion-blur whip at 0:56.75. | **music dips: momentary −38 LUFS for 8 s** (quietest stretch of the video), tap transient 0:53; no voice |
| B6 Handshake + dress-up | 0:56.9–1:04.3 | 16 | 0:56.92 depot photo (orange bags on shelves, courier with orange bike); boss (navy suit, tie, tired eyes, energy can) shakes hands. 0:59.00 cut to **sunburst background** (rays #FFC12B / #FF243B): T-pose; jacket flies in from right 0:59.25–0:59.75, jacket on 1:00, cap 1:02, backpack 1:03 (one item ≈ every 1.1 s). | **music jumps to loudest act-1 level** (side −24 dB); 4 low thuds at 0:57.98, 1:00.14, 1:01.25, 1:02.35 = one per garment |
| B7 First delivery | 1:04.3–1:27.7 | 18 | 1:04.32 **speed-line background** (red/black horizontal streaks, base #880009, yellow-orange lines) — bike rides in L→R (travel transition, 2.9 s). 1:07.20 front door "14", brick, wisteria; bike stops 1:08; door opens 1:09 on a jaw-heavy blond "Chad"-type customer. 1:09.56 CU courier holding kraft bag, terraced street photo blurred. 1:12.80 OTS customer profile in dark doorway; 1:15.0 reframe to 2-shot (smiles). 1:17.00 WS: hand with watch reaches out (tip), door shuts 1:18. **1:18.84 CU courier smug smile on the street — 8.9 s hold with slow push-in** while he talks (1:18.3–1:24.8 "That was a very nice customer…"). 1:26 phone enters. | voice 56 %; door/click transients 1:07.4, 1:15.7, 1:16.3; music almost leaves the stereo field (side −54 dB) under the dialogue |
| B8 Delivery montage | 1:27.7–1:51.3 | **23** | 1:27.72 phone insert "NEW ORDER! Go get that bag" + map + GO. 1:30.24 CU smile + phone. 1:33.00 speed lines (red) bike L→R. 1:35.88 hand-off insert: orange sleeve hands bag to a white hand over a blurred red-brick building. 1:38.32 **yellow-green** speed lines, side CU riding. 1:41.20 hand-off insert at "BERGAMOT" restaurant (green sleeve with red bracelet). 1:43.64 **cyan/pink** speed lines. 1:45.24 hand-off to red sleeve (shopfront). 1:47.12 WS park bench, courier on phone, bike + bag, two passers-by. Pattern: **ride → hand-off → ride → hand-off**, each 2.4–2.9 s, speed-line colour changes each lap. | 4 % voiced; mono drum-led music, momentary median −13.8 LUFS (**loudest beat before the turn**); kick-like low thuds every ~0.9 s (1:32–1:49) |
| B9 The irony monologue | 1:51.3–2:00.8 | **6** (1 shot) | 1:51.32 CU on the bench smiling at phone, green park photo with blurred legs — **9.5 s static hold, the longest story shot**. | "Man, I love this job. No annoying boss yelling at me… nice salary" 1:51.0–1:58.7, "How can this go wrong?" 1:58.7–2:00.0 |
| B10 Act break | 2:00.8–2:06.4 | — | **Hard cut to black, 5.6 s** (only the watermark visible), then 0.7 s fade-in. | villain cue enters on the cut: sub-bass hit 2:00.9 (centroid 70 Hz, 1.5 s), drone continues; booms 2:05.6 |
| B11 Villain intro + rain | 2:06.4–2:20.6 | 17 | Photoreal man in black suit, hand on chin, private-jet interior, windows show a **purple galaxy**; slow push. Subtitles (white sans, ≈3 % of frame height, bottom 86 % y): "What?" 2:07, "He is enjoying his new job?" 2:09–2:10; off-screen servant answers 2:10.9–2:12.8; 2:13.52 reframe to CU, "Turn on rainfall." 2:14–2:15. 2:15.64 courier riding past a fence (moving video background) smiling 2:16 → 2:17 white rain streak overlay + desaturated sky → 2:18 annoyed → 2:19–2:20 crying (light-blue tear streaks, clenched teeth). | villain cue, side −24…−31 dB (music now 6–10 dB louder relative to voice than in act 1) |
| B12 Sabotage 2–3 | 2:20.6–2:39.1 | **32** | 2:20.64 villain "Order a pizza from the other side of the city." 2:24.16 phone "NEW ORDER! 32min away, you got this!" 2:25.76 crying CU (street). 2:28.36 villain WS "Now do it again." 2:29.64 phone at night (dark cobblestone) "NEW ORDER! 30min away, let's exercise!" 2:31.28 crying CU at night (cherry blossom, neon). 2:32.28 ECU crying, hand on face. 2:33.56 villain ECU "Raise the workpressure." 2:35.72 riding, crying; **2:36.4–2:38.4 triple ghost dissolve** of three crying faces (exhaustion montage). | voice 32 %; momentary −15 LUFS |
| B13 Mood switch | 2:39.1–2:47.6 | 21 | villain "Switch the mood of customers." 2:42.28 same doorway, same customer now cold: "I didn't order this." 2:44–2:45; courier cries 2:45; door shuts 2:46. | |
| B14 Blind-NPC car | 2:47.6–2:59 | 16 | villain "Spawn a blind NPC driving a car." 2:50.76 hand-held roadside video (pole whips through foreground), 2:52.8 reframe: red compact car (moving footage) driven by a grey NPC with **X eyes** (= blind) in a suit, CU 2:53–2:54. 2:55.00 courier rides country road smiling (unaware). **2:57–2:59 empty road + fence: the impact is elided.** | car-pass transient 2:52.3; no crash sound measured |
| B15 Hospital | 2:59–3:04.5 | **44** | 2:59 wall TV in a hospital shows the same empty road; courier now in **the black beanie + black hoodie (defeat costume)**, red eyes. 3:00 WS hospital bed, IV. 3:01.28 phone: news article (real-looking outlet, "Entrepreneur in a pinch", dated July 25, 2021); 3:01.88 reframe = ECU push on the headline. 3:03.40 CU rage-crying. | 0 % voice; **most replayed seconds** |
| B16 Villain's last line | 3:04.5–3:12.2 | 0 (7.7 s) | villain WS, slow push. Subtitles "Not yet," 3:07 / "but prepare for plan technological automatization." 3:08–3:10. | **music removed entirely 3:06.9–3:11.4** (stereo side = digital silence); clicks 3:05.8, thuds 3:07.0/3:08.1 under the line |
| B17 Drone reveal | 3:12.2–3:22.4 | 12 | 3:12.24 CU orange "TAKEAWAGE" quadcopter carrying a kraft box, dark vignette lifts 3:12–3:15; 3:14.60 **pull-back reveal, 8.2 s**: hundreds of identical drones in a hangar. | villain cue returns with a 4 s sub boom at 3:14.7 |
| B18 Out | 3:22.4–3:30.5 | — | black 3:22.4–3:24.1, end card fades in 3:24.1–3:25.5 and holds to 3:30.5 (6.4 s by eye; detector 5.0 s): orange #ED710A, original channel mascot (beanie) left, "LOW BUDGET STORIES" heavy black brush caps top, three social handles, dark translucent rectangle + light circle = YouTube end-screen slots. | cue continues to the end |

---

## 4. Script / communication mechanics

- **Sparse, functional dialogue: 221 words in 210 s (63 words per minute of runtime).** Speech carries only (a) the premise (0:16–0:35), (b) the irony line (1:58.7), (c) the villain's commands. Everything else is pantomime with props: cap-throw = "I quit" (0:42.8), app list = the job's promise (0:50), garment-by-garment dress-up = transformation, hand-off inserts = the work loop, rain overlay = sabotage taking effect, beanie costume in hospital = "back to doomer".
- **Command → consequence couplets.** Each villain line is followed within 1.1–2.5 s by its visual effect: "Turn on rainfall" 2:14 → rain 2:17; "Order a pizza from the other side of the city" 2:21 → "32min away" 2:24; "Now do it again" 2:28 → "30min away" 2:29; "Switch the mood of customers" 2:40 → cold customer 2:42; "Spawn a blind NPC driving a car" 2:48 → car 2:51. Five couplets in 51 s — an escalation ladder the viewer can predict, which is the joke.
- **Callbacks / repetition:** the same doorway "14" and the same customer used twice (friendly 1:09, hostile 2:42) — the change of mood is the gag; the same phone-in-hand insert template 4× (0:50, 1:27, 2:24, 2:29) with only the text changed ("Go get that bag" → "you got this!" → "let's exercise!" = escalating sarcasm); speed-line ride shot 4×; the counter customer from 0:08 never returns (commenter at 492 likes asked for exactly that callback).
- **Contrast device:** act 1 (0:00–2:00) bright photos, sunburst, playful music, 0 tears; act 2 (2:06–3:22) dark jet, rain, night, villain music, tears in 9 of 23 courier shots.
- **What is withheld:** the villain's identity/motive is never explained; the accident is **not shown** (2:57 empty road → 2:59 hospital). The heatmap maximum sits right after the elision (3:01.5–3:03.6), i.e. viewers scrub back to work out what happened.
- **On-screen text** is diegetic only (phone UI, news headline, subtitles for the villain); no captions for the protagonist, no title card, no chapter cards.
- **Ending:** the cosmic villain wins and scales up (drones) — no resolution for the protagonist; last story image is the drone hangar, not the hero.

---

## 5. Visual grammar

**Rhythm (measured, calibrated).** `rhythm_qa.py` boundary model (single-frame cut + 4–10-frame "reframe" + blend-test dissolve + black runs) was checked against before/after frame pairs for every boundary (`data/extra/a4_rhythm/montage_boundaries.jpg`, `reframe.jpg`; per-shot table `shots.csv`, per-second map `seconds.csv`): all 66 story boundaries are real changes of framing. scdet ≥ 8 misses the 8 quick reframes (scdet scores 3–9 spread over 4–8 frames), the triple-exposure dissolve and the from-black, adds 2 false positives on an exposure change inside the drone pull-back (3:15.9–3:16.0), and counts the 5.6 s black + villain shot as one 14.8 s "shot". The opening fade-in + slide (0:00–0:01) is not an edit.

| Segment | Boundaries/min |
|---|---|
| 0:00–0:15 | 16 (4 cuts; first cut 0:03.72) |
| 0:15–1:00 | 22.7 |
| body 1:00–2:55.5 | 19.7 |
| last 30 s of story 2:55.5–3:25.5 | 14 |
| per minute of runtime | 21 · 17 · 21 · 7 (minute 4 = drone hold + end card) |

Shot length (65 story shots): p10 1.1 s, median 2.4 s, mean 3.0 s, p90 6.2 s; holds > 8 s: 1:18.8 (8.9 s, monologue, push-in), 1:51.3 (9.5 s, irony monologue), 3:14.6 (8.2 s, drone pull-back). **Every hold > 8 s is either a monologue or the final reveal; no hold > 10 s.** Rhythm follows speech inversely: beats with ≥ 85 % voice run at 6–12.5 cuts/min, voiceless montage beats at 23–44 cuts/min (B5 39, B12 32, B15 44).

**Camera.** Push-in on 25.6 % of runtime (slow digital zoom on a still composite), static 47.7 %, animated/changing content (montage overlays, moving footage) 19 %. 8 quick reframes (0:24.96, 0:30.76, 0:40.08, 0:49.32, 1:15.0, 2:13.52, 2:52.8, 3:01.88) = a zoom/slide between two framings of the same composite, 0.16–0.4 s — the channel's way to "cut" without a second shot. Parallax: foreground blurred passers-by crossing the frame (0:00, 0:13, 0:19) act as wipes [inferred: separate blurred layer animated across, high confidence].

**Compositing.** Flat 2D cut-out characters (pure white faces, 3–5 px black outline, flat colour clothing, no shading except blue tears) on **blurred** stock photographs (fake depth-of-field) or stock video (fence/road, red car, rain). Phone screens are rendered UI mock-ups held by a cartoon hand over a cobblestone photo — a reusable template.

**Colour as emotion.** Euphoria = sunburst #FFC12B/#FF243B; travel = speed-line plates (red #880009, yellow-green, cyan-pink); villain = dark desaturated plate with violet galaxy; misery = rain overlay + night photos; defeat = black-beanie costume. Brand thread orange ≈ #EB7E14 (jacket, app, drones) ≈ end-card #ED710A.

**Watermark.** Bottom-left, YouTube play icon + "Low Budget Stories" in a comic hand-lettered font, ~50 % white, ≈ 2.5 % of frame height, on 100 % of frames including black frames; not on the end card.

**Title card:** none (series title only in the YouTube title).

---

## 6. Audio grammar

**Mix architecture (measured).** Music lives mostly in the stereo side channel, dialogue is mono centre, so mid/side separation gives a clean music map.

| Time | Music cue (side level) | Role |
|---|---|---|
| 0:00.4–0:47.7 | Cue A, light/playful, energy 150–2,400 Hz, side ≈ −39 dB | job-misery comedy under dialogue |
| 0:47.7–0:56.5 | same cue nearly gone (momentary −38 LUFS) | "thinking" pocket before the decision |
| 0:56.5–1:09 | loudest act-1 music, bright (side −24 dB) | hired / dress-up / first ride celebration |
| 1:09–2:00 | music collapses to mono and very low under dialogue (side −54…−59 dB); mono drum-led loop rises for the 1:28–1:49 montage (momentary −12…−14 LUFS). **This loop is the same audio the channel later uses as its fixed end-card outro** (spectral cross-correlation with the v07 end card r = 0.80–0.92; identical outro in v03–v07, v10) | idyll |
| 2:00.9 | sub-bass hit on the black, then a low drone | act break |
| 2:01–3:06.9 | **villain cue** (dark, minor; key estimator: C minor, conf. 0.54–0.63) at side −24…−31 dB, i.e. **6–15 dB louder than the act-1 bed** | sabotage |
| **3:06.9–3:11.4** | **music OFF** (stereo side = digital silence) | the villain's final line lands dry |
| 3:12–3:30 | villain cue returns with a 4 s sub boom at 3:14.7, plays through the end card | drone reveal + outro |

Credited tracks: Audionautix "I like Peanuts" (royalty-free, CC-BY library) and an unnamed "Villain Music No Copyright" [inferred mapping: playful cue = acts 1 (0:00–2:00), villain cue = 2:01–3:30; high confidence for the split because it coincides with the black act break, medium for which credited title is which]. Tempo estimates are unreliable on this material (estimator returns 66–152 BPM for different windows); the montage loop shows a periodic low thud every ≈ 0.9 s.

**SFX inventory (transient detector + spectral shape; tied to picture):** tonal "idea" hit 0:26.9 (1.6 kHz centroid, 0.35 s) on the grin; cap-throw hit 0:42.9; UI tap 0:53 (button); 4 garment thuds 0:57.98–1:02.35 (centroid 310–430 Hz, 75 % energy < 300 Hz) on the dress-up; door/knock 1:07.4; click 1:15.7 (5.6 kHz, 0.12 s); door thud 1:16.3; notification whoosh 1:27.96 (4.3 kHz noise, 0.44 s) + tap 1:28.3 on the "NEW ORDER" insert; phone ping 2:24.3 (1.4 kHz tonal); sub-bass hits 2:00.9 (1.5 s), 2:05.6, 2:08.5 (villain reveal); car pass 2:52.3; clicks/thuds 3:05.8–3:08.1; 4 s sub boom 3:14.7 (drone reveal). **No crash/impact sound for the accident** (silent elision). Density ≈ 5.4 detectable non-voice transients per minute — SFX mark state changes, never ambience.

**Voice.** Text-to-speech, high confidence: 0 fillers/disfluencies in 221 words; lines are pasted with uniform 0.4–0.6 s gaps (word-gap median 0.58 s); courier voice f0 median 94–100 Hz with only 4–7 semitones range per line (flat, read-out prosody); villain f0 ≈ 115–118 Hz with a non-native accent ("French accent" noted by commenters, 29 likes) and burned-in subtitles; servant voice deep (pitch tracker floor) with a different accent ("his worker is German", commenter). Channel-level corroboration: commenters on v05/v06/v07/v09 explicitly call the voices "AI voices", "voice bot", "TTS". Speaking rate inside a line 155–285 WPM (single short lines ≥ 225), 162 WPM averaged over turns. Processing: dry, no audible reverb, voice level constant (momentary −15…−17 LUFS on every line).

**Loudness map.** Act 1 dialogue −17 LUFS momentary; applying pocket −38; hired/montage −13…−16; black −13.5 (drone); act 2 −15; dry villain line −15 with music out. Integrated −16.6 LUFS is 3–5 LU louder than the voiced corpus videos made later (v02/v03/v05/v06 −20.6…−22.5) [inferred: older mastering habit, medium].

**Silence usage.** No silence ≥ 0.8 s anywhere. Drama is made by **removing music, not sound**: one music-off window (3:06.9–3:11.4) and one 8 s near-silent pocket (0:47.7–0:56.5).

---

## 7. Retention devices and why viewers stayed / replayed / commented

| Device | Time | Evidence |
|---|---|---|
| Dramatic-irony line + black screen | 1:58.7 → 2:00.8–2:06.4 | heat rises from 0.11 (1:55) to 0.20 at 2:06 |
| Command → consequence ladder (5 rungs in 51 s) | 2:14–2:51 | heat 0.20–0.27 on the whole stretch; comment "Bog: 'Great he enjoys his job, spawn a blind guy and run him over'" (1,700 likes), "Spawn a blind NPC driving a car got me" (116) |
| Elided accident + news-article proof | 2:57–3:03 | heatmap max 1.000 at 3:01.5–3:03.6 |
| Readable joke UI | 0:50–0:55 | heat 0.355 |
| Cosmic-conspiracy framing | whole act 2 | top comment (11,000 likes) is a riff on the universe spending millions to stop the protagonist; "The whole Universe wants to stop this guy" (547) |
| Real-job accuracy | whole | 3 of the top 4 comments are self-identified couriers confirming accuracy (6,800 / 5,300 / 5,100 likes), incl. pay cuts per delivery — the video triggers testimony |
| Quick-hire gag | 0:53 | "I love how he instantly got hired" (287) |

---

## 8. Weaknesses / risks (what not to transfer)

1. **Real-person likeness as villain** (photoreal meme of a real public figure) and real brands/likenesses (fast-food arches photo, a real news outlet's article screenshot, a delivery-brand-coloured rider) — defamation/IP risk; never copy. [ETİK]
2. The accident is so elided that some viewers must rewind to understand (heat max) — fine for replay, but a viewer who does not rewind gets a 2-s non-sequitur.
3. 50 fps master while the rest of the channel is 25 fps; mixed motion cadence of 25 fps stock inside a 50 fps timeline [inferred, low].
4. Bed only 2.8 LU below voice on average (music is loud in act 2) — dialogue intelligibility relies on subtitles for the accented villain.
5. Short end card (6.4 s) with a 1.7 s black before it — below YouTube's 5–20 s window only by margin; cheap.
6. The counter customer set-up is never paid off (a commenter proposes the missing callback).

---

## Why it works

- A two-act shape with a hard, **silent-black** hinge exactly at 57 % of runtime (2:00.8 of 3:30): 2:00 of rising contentment so the fall has height, then 1:22 of compressed escalation.
- Rhythm is driven by *speech density*: talky beats hold 8.9–9.5 s, pantomime beats cut every 1.1–1.7 s, so attention never has two jobs at once.
- The antagonist's commands are spoken, their effects are shown: viewers predict each rung, and the payoff (blind NPC) overshoots the prediction.
- Sound design changes **state**, not ambience: a cue change at the act break, music removed for the villain's last line, one garment-thud per costume item, no crash sound.
- Universal job pain + exaggeration triggers testimony comments from real workers.

## Rules to copy

1. [KOPYA] Keep the story at 3:10–3:30 with a two-act split; put the hinge (last happy line → black) at 55–60 % of the story runtime.
2. [KOPYA] End act 1 with one dramatic-irony line spoken by the protagonist (≤ 6 words, e.g. "What could go wrong?" style — write your own), then cut to pure black for 4–6 s with only a low sub-bass hit (≤ 100 Hz centroid, 1–1.5 s) and the antagonist's music entering.
3. [KOPYA] Edit rhythm targets for this format: 19–21 boundaries/min overall; 0:00–0:15 ≥ 14/min with the first cut ≤ 4 s; voiceless montage beats 25–45/min (shots 1.1–2.5 s); monologue beats 1 shot of 8–10 s with a slow push-in; no story shot > 10 s.
4. [KOPYA] Count quick reframes (0.16–0.4 s zoom/slide between two framings of one composite) as cuts; use ≥ 1 per 30 s to vary framing without new art.
5. [KOPYA] Escalation ladder: 4–5 antagonist commands within 45–60 s, each followed by its visible effect within 1–2.5 s; make the last rung absurd and elide its impact (show before + after, never the hit).
6. [KOPYA] Use one phone-in-hand UI template (cartoon hand, real-looking phone, blurred ground photo) 3–4 times with escalating sarcastic copy; keep each insert 1.5–3 s and the first one readable for ≥ 4 s (heat peak 0.355).
7. [KOPYA] Montage loop for "the job going well": ride (speed-line plate, colour changes every lap) → hand-off insert → ride, 2.4–2.9 s per shot, ≥ 3 laps, ≥ 90 % voiceless, music 3–4 LU louder than in dialogue scenes.
8. [KOPYA] Music map: light/playful cue for the setup, a dark cue starting exactly on the act break, and remove all music (not voice) for the antagonist's final line (3–5 s); mix the bed 3–10 LU under dialogue, static (no sidechain ducking needed — the corpus shows none).
9. [KOPYA] One SFX per state change (idea ding, throw hit, UI tap, one thud per costume item, notification whoosh, sub boom on reveals); 4–6 non-voice hits per minute; no ambience beds.
10. [KOPYA] Master the voiced short at −17 ± 1 LUFS integrated, LRA 9–11 LU; voice lines at −15…−17 LUFS momentary.
11. [İYİLEŞTİRME] Pay off the first-scene antagonist (bring the angry customer back in act 2 or the epilogue) — the audience asked for it.
12. [İYİLEŞTİRME] Give the elided accident a 0.3–0.5 s audio cue (tyre squeal cut off) so non-rewinders get it; keep the visual elision.
13. [ETİK] The puppet-master must be an original character that fills the "all-powerful bored overlord" role (own design, no real person's photo or name); brands are invented parodies with no logo/colour that copies a real company; news inserts use invented outlets and headlines.
14. [ETİK] Use an original character that fills the "tired worker meme-man" role instead of the channel's Wojak/Doomer art; original end-card design (do not reuse the orange #ED710A + beanie mascot layout).

## Open questions

- Which credited track is "I like Peanuts"? The montage loop (1:28–1:49) is the channel's later standard outro asset, so it may be a third, uncredited track. Needs a listening pass.
- Was the 50 fps master deliberate (e.g. a different editor/project preset in May 2022)? Check other 2022 uploads.
- Is the villain's accent a TTS locale preset or a human impression? Pitch/spacing suggest TTS; not provable from the file.
