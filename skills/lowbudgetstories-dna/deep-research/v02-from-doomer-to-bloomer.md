# v02: "From Doomer to Bloomer" (peretEtnvbc): per-second teardown

Analyst 2. Evidence: all 32 sheets of 1 fps (000–031), all 15 sheets of 4 fps intro (000–014), the thumbnail, a key-frame montage (s0011, s0014, s0051, s0053, s0057, s0062, s0114, s0115, s0119, s0131, s0167, s0203, s0236, s0238, s0259, s0267), cuts.csv / scdet / metrics / silences, the RMS envelope and spectral centroid of `audio16k.wav` in 5 s bins, per-line RMS and f0 (autocorrelation), faster-whisper word timestamps, the heatmap, and 400 comments.
Character labels (Doomer/Wojak, Gigachad) describe the channel's meme cast **for analysis only**. Every rule below means "an original character that fills this role".

---

## 1. Card

| Field | Value |
|---|---|
| Title | From Doomer to Bloomer |
| Views / likes / like% | 4,955,046 / 216,011 / **4.36 %**. This ties v04 for the 2nd-highest like rate in the top-10 (range 2.69–5.49 %). |
| Comments | 5,400, which is **1.09 per 1,000 views**. Corpus range is 0.79–2.70. |
| Upload | 2023-07-07, 109 days after its prequel v01 "Origin of a Doomer" (2023-03-20). |
| Duration | 281.0 s: 259 s of story, 11 s of fade/black, then an 8 s silent end card. |
| Format family | Doomer saga (redemption half). Voiced, two-hander dialogue, with advice montages. |
| Thumbnail | Delivered as a 640×480 hqdefault, so the 60 px black bars top and bottom (12.5 % each) are a letterbox artefact, not a design choice. The 16:9 content has **no text** and is a three-figure **before → after** layout. **Left ≈45 % of width:** the protagonist as Doomer (black beanie, black hoodie, red-rimmed eyes, stubble, a lit cigarette with a smoke trail) on a night city plate (left-third mean #22292E). **Centre-back ≈25 %:** a photoreal shirtless muscular bearded man, blue-lit and semi-ghosted (mid-third mean #474746). **Right ≈45 %:** the same character, clean-shaven, bald, in an orange polo, skin tinted gold, on a sunrise meadow (right-third mean #987D56). A thick **red curved arrow** runs from the Doomer's chest to the Bloomer's chest. Palette: black 27 %, #F9CE7D warm gold 22 %, #1E1416 18 %, #7AB0C6 sky blue 12 %. The dark-left / bright-right split is the promise of the video. |
| Description / tags | Opens by naming the video as the sequel and links v01. A one-sentence plot: at his lowest point, a mentor appears and helps him improve. Then a thesis line (happiness is made, not found), crypto donation addresses, and socials. Tags are the channel's generic meme/crypto set (wojak, doomer, zoomer, boomer, chad, meme, crypto…) and are **not** topic-specific. The description contains a Dutch article slip ("de sequel"), a sign of a non-native English writer (see §8 item 6 and L2 §"Authored vs generated"). |
| Cuts | @score≥8: **71 cuts = 15.16/min**, median shot **3.34 s**, mean 3.90 s, max 12.1 s (@≥25: 24 cuts, max 61.7 s, because soft cuts dominate). |
| Cut rate by act (measured) | cold open 0–13 s: 18.5/min (median shot 2.5 s) · hilltop dialogue 13–54: 14.6/min (3.8 s) · living-room act 56–135: 17.5/min (2.6 s) · workplace act 136–184: 17.5/min (3.2 s) · social/gym act 184–240: 15.0/min (3.0 s) · **gratitude + reveal 240–270: 8.0/min (8.0 s)** · outro 270–281: 5.5/min |
| Loudness | **−20.6 LUFS** integrated, LRA 10.1 LU. silencedetect pauses ≥0.35 s: 3 (12.4 s total): 104.46–104.95, 268.73–269.27 and **269.63–280.98 (11.4 s of silence at the end)**. |
| Speech | 619 words in 73 lines (84 sentences). First word at **14.1 s**, last at 258.6 s. 132 wpm over the full runtime; **192 wpm inside dialogue blocks** (runtime minus wordless gaps). Wordless gaps ≥3 s: 0–14, 50–63, 123–145, 175–185, 235–243, 259–281, totalling **88 s = 31 % of the runtime**. |

**Heatmap top peaks.** Bins are 2.81 s. The values measure replay density, not retention.

| # | Bin | Value | On screen |
|---|---|---|---|
| 1 | 0:00–0:03 | 1.00 | Back view on the night hilltop. This is the start/seek artefact plus the sequel hand-off: the plate is identical to v01's last 22 s. |
| 2 | **3:56–3:59** | **0.95** | Mirror reveal of the new body, a reflection smile, then a new face drawing (square jaw, no eye bags). This is also the **loudest 5 s of the video (−19.6 dB RMS)**, a music swell with no speech. |
| 3 | 0:14–0:17 | 0.90 | The mentor is revealed (photoreal still, B/W) and speaks the first line of the film. |
| 4 | **4:16–4:19** | 0.87 | The identity answer: he says he is a voice in the protagonist's head, then begins to dissolve. |
| 5 | 3:45–3:48 | 0.81 | Gym ECU (face slightly fuller, barbell passing) under the line about being happier with a fit body. |
| 6–8 | 4:10–4:13 (0.77) · 1:55–1:58 (0.77) · 3:22–3:25 (0.63) | – | The protagonist finally asks who the mentor is · the clean-room before/after plus the 7:00 alarm · the first greeting attempt fails (girl turns away, sweat drops). |
| low | 1:21–1:32 | 0.17–0.20 | The weakest stretch: the protagonist's verbal list of what is "hard". It is talk only, on reused plates, with no visual event. |

---

## 2. Premise, turn, emotional arc

**Premise (one line).** At his lowest point, a hopeless young man is visited by an idealised mentor figure. The mentor coaches him through four small habits until he is content, then reveals that he was only the man's own inner voice.

**The turn.** There are two. (1) **0:52**: the eye bags dissolve off the Doomer's face before he has done anything. The inner decision is shown as a drawing swap. (2) **4:13–4:21**: the mentor says he is a voice in the protagonist's head and vanishes from the chair. This retroactively turns the whole film into self-talk. The question "who are you?" is first asked at 0:16 and answered 237 s later.

| # | t | Point | Evidence |
|---|---|---|---|
| 1 | 0:00 | **Despair**: alone at night, holding a black pill | back view, red eyes, pill insert 0:06–0:08, −44 dB near-silence |
| 2 | 0:10 | **Intervention**: a hand on his shoulder | photoreal hand enters at 0:10.5 |
| 3 | 0:52 | **Acceptance** | eye-bag dissolve 0:52.0–0:52.25, then 2 s black |
| 4 | 1:49 | **Breakdown**: he cries while asking how | blue tear streaks, gritted teeth (s0109) |
| 5 | 2:01 | **First win**: first smile of the film, holding water instead of beer | s0121 |
| 6 | 2:03–2:14 | **Relapse**, then calm | cries on the sofa; the TV switches off and shows his reflection (2:11); eyes close, small smile at 2:14 |
| 7 | 3:56 | **Pride** | mirror reveal, loudest moment, heatmap 0.95 |
| 8 | 4:19–4:29 | **Revelation + solitude** | mentor dissolves; WS of him alone at a restaurant table among couples |

---

## 3. Beat sheet / visual script

### 3a. First 20 s (4 fps)

| t (s) | Shot | Who | Scale / BG | Motion / text / audio |
|---|---|---|---|---|
| 0.00–0.50 | fade from black | – | – | Silence (RMS −44 dB, ambience only) |
| 0.50–3.75 | back view of a hooded figure on a hilltop behind a park bench, city lights below, purple-blue sky, glowing street lamps | Doomer (beanie, black hoodie, jeans) | WS; **illustrated/painted plate** | Static (possibly a ≤2 % push; low confidence). This is the same plate and blocking as v01 3:10. No text. |
| 3.90 | cut | | | |
| 4.00–6.25 | 3/4 face: red-rimmed eyes, purple eye bags, stubble dots, down-turned mouth | Doomer | CU; blurred lamp/foliage BG (shallow-DOF look) | Blink at 5.75 |
| 6.40 | cut | | | |
| 6.50–8.75 | white cartoon palm, open, holding **one black capsule** | hand | insert CU; blurred teal foliage | The hand drifts slightly between 6.75 and 7.00. The pill is the "blackpill" metaphor made literal. |
| 8.90 | cut | | | |
| 9.00–10.25 | same face, head a little lower | Doomer | CU | – |
| 10.50–12.75 | a **photoreal greyscale veined male hand** enters frame-left and rests on his shoulder (from 10.75) | Doomer + hand | CU | The cartoon/photoreal clash signals "otherworldly". The Doomer doesn't react. |
| 12.90 | cut | | | |
| 13.00–16.25 | chest-up still of a photoreal, desaturated, muscular bearded man on a night-sky plate | Mentor | MCU, ≈45 % frame width | **3.25 s silent hold first.** The first line runs 14.1–16.0: a short question about his day, addressing him as "son". The still never moves its mouth, so no lip-sync is needed. |
| 16.60 | cut | | | |
| 16.50–18.00 | Doomer front-on, eyes widened | Doomer | MS, city overlook | He asks who this is (16.8–18.0) |
| 18.30 | cut | | | |
| 18.25–20.00 | the two face each other in profile across the skyline, the Doomer's head bottom-left (≈25 %), the mentor right (≈30 %) | both | 2-shot profile | The mentor deflects the identity question (18.5–21.7) |

Measured shot lengths for 0–20 s: 3.9 / 2.5 / 2.5 / 4.0 / 3.7 / 1.7 s.

### 3b. Rest of the film, per beat

| Beat | t | What happens | Frame / BG | Audio |
|---|---|---|---|---|
| B2 Thesis on the hilltop | 0:20–0:50 | The mentor refuses his hopelessness. The Doomer complains that the world keeps hurting him. The mentor answers with an either/or about how you react. The Doomer objects that this is easy to say. The mentor offers to guide him. | Strict **shot/reverse-shot on the speaker**: Doomer MS/CU, mentor MCU, profile 2-shot. **OTS from behind the beanie at 0:36** makes the mentor larger than the Doomer. 0:37–0:39 is a tighter re-crop of the mentor's face (≈50 % of frame) on the key either/or line. Only 3 setups are reused across 10 cuts. | Nearly no music: inter-line gaps sit at −43 to −47 dB |
| B3 Acceptance | 0:50–0:54 | Silent reaction. The background is now defocused bokeh. **The eye bags dissolve away at 0:52.** | MS frontal | silence −45.6 dB |
| B4 Act break | 0:54–0:56 | **2 s of black** | – | silence; whoosh/air (centroid 4.1 kHz at 55–60 s) |
| B5 New chapter: living room | 0:56–1:02 | Fade in on a stock-photo living room at sunset. A red crypto-propaganda poster is on the wall, a TV sits in the foreground. The protagonist is now **bald with no beanie**, in a grey tee and striped track pants, holding a game controller. TV insert 0:59–1:01: screen-replaced real driving-game footage. | WS; stock photo | music bed enters at a low level |
| B6 Complaint inventory | 1:02–1:16 | OTS reveal at 1:02: the mentor sits in an armchair in the room, arms crossed. Asked what bothers him, the protagonist lists six deficits in one breath (friends, love, wage job, not social, not good-looking, addictions). The mentor **cuts him off mid-word** at 1:13. | MS from behind the mentor's black silhouette (≈30 % of frame) · MCU mentor in a warm sepia armchair | – |
| B7 Socratic exchange | 1:16–1:49 | The mentor asks who can improve this. The protagonist pauses for 1.1 s, then answers that he can (1:19). He lists three "hard" things (1:31–1:36). The mentor **echo-corrects**: it *feels* impossible, but it isn't. Then a one-line aphorism that places all his limits inside his own head. **1:49: the protagonist cries while asking how.** | CU with red poster BG (6 s lingering sad CU 1:31–1:36); WS mentor full body in armchair, static 8 s (1:40–1:47) | pause 104.46–104.95; heatmap low (0.17–0.25) |
| B8 Advice montage 1 | 1:50–2:02 | The mentor's VO continues over 1–3 s inserts. **Messy room, then the same room clean, 1 s apart (1:53→1:54).** Alarm 7:00 at sunrise (1:55). A hoodie version of him drinks beer at a dark PC desk, then the bottle is swapped for water (1:56–2:00). **First smile at 2:01.** | stock photos with the character composited in | VO + music |
| B9 Relapse & reflection | 2:03–2:14 | Back on the sofa, crying (2:03). Gameplay insert (2:05–2:07). Push to ECU crying (2:09). **The TV switches off and its black screen shows his reflection (2:11).** Tears gone, eyes closed (2:13), small smile (2:14). | wordless 22 s (123–145 s) | music up (−25 to −28 dB RMS, centroid ≈1.05 kHz, mellow) |
| B10 Act break | 2:15 | 1 s black | – | – |
| B11 Workplace | 2:16–2:24 | Fast-food exterior stock photo (real brand marks visible). He stands small (≈12 % of height) in a red uniform and visor, the same job he ended up in during v01. The grade brightens 2:16→2:17. He lights a cigarette and exhales (2:21–2:23). | WS → MS → CU | – |
| B12 Smoking bargain | 2:24–2:47 | The mentor's silhouette enters the smoking CU. Exchange: the protagonist defends his one pleasure and bargains for a last one. The mentor delivers an **aphorism about fools persisting in error, on a new angle (profile CU, 2:39–2:42)**, the only profile CU of the mentor. **Eye bags gone again at 2:45.** Insert: a cigarette dropped into a street ash-bin (2:46–2:47). He never states that he quits; the prop says it. | mentor exterior MCU (blue sky, B/W) | mentor's f0 rises to 131 Hz on the aphorism (he sits at 98–113 Hz otherwise) |
| B13 Books | 2:48–3:01 | The hoodie version stands in a vast circular library (2:48). Bald version reads a book on a cosy sofa (2:50–2:53). ECU strain (2:55). Then the hoodie version sprawls on a dark-blue sofa while the TV plays a real self-improvement video (2:56–3:01); the gag is ambiguous. | stock photos | music only 2:55–3:04 (−30 to −32 dB) |
| B14 Social ladder | 3:02–3:31 | Night riverside, the two **walk side by side** (a companion now, not facing him). He asks how to talk to people. Whip-pan/motion-blur cut at 3:14. Advice: greet, then small talk, then practise. **Greeting ladder, wordless, ≈3 s each:** a girl in a choker side-eyes him and turns away while he sweats and grins (3:21–3:23, **fail**). A curly-haired guy on an autumn bench laughs with him (3:24–3:26, **success**). An old lady on a sidewalk stands arms crossed, unimpressed (3:27–3:31, **neutral**). | 3 new stock locations in 10 s | heatmap 3:22–3:25 = 0.63 |
| B15 Gym | 3:32–3:52 | Park CU, he asks about confidence. The mentor suggests the gym **while admitting it sounds like every online guru's advice (3:38–3:44)**, a self-aware meta line. Gym montage, desaturated (3:40–3:47): curls with a girl watching, lat pulldown, an ECU with the face fuller. Confident walk down a winter street, nodding to a stranger (3:48–3:50). **The 7:00 alarm insert returns at 3:51**, a callback to 1:55. | gym stock photo, B/W-ish grade | heatmap 3:45–3:48 = 0.81 |
| B16 Mirror reveal | 3:52–3:59 | Dark room. He stands before a mirror, broader. The reflection smiles (3:54). Cut to a **new face drawing**: square jaw, level brows, half-smile (3:57–3:59). | MS mirror 2-shot → MCU | **loudest 5 s (−19.6 dB)**, music swell, no words; heatmap 0.95 |
| B17 Gratitude | 4:00–4:13 | Dissolve to a mountain vineyard restaurant terrace. He sits at a back table in a tan polo, diners in the foreground. He thanks the mentor in a **triad** (for guiding, for every lesson, for believing in him), then asks the one remaining question: who are you? | OTS mentor silhouette; restaurant stock photo | line RMS rises to −20.4/−21.8 dB from the earlier −23/−25 (+2–3 dB intimacy lift) |
| B18 Reveal | 4:13–4:21 | The mentor, composited into the chair opposite (B/W), says he is nothing but a voice in the protagonist's head and that everything is within him, closing with the same paternal address used at 0:14 (**bookend**). **He dissolves to an empty chair (4:19–4:21).** | MCU → transparency dissolve → empty-chair plate | heatmap 0.87 |
| B19 Coda | 4:22–4:29 | He is alone with a faint smile (4:22–4:25). **WS: he is a tiny figure (≈10 % of height) alone at a back table while couples fill the foreground (4:26–4:29).** | static 4 s + 4 s | music fades: −44 dB at 260–270 s |
| B20 Out | 4:30–4:40 | 4 s black and silence, then an orange end card (#ED720B, 60 % of frame) with the channel's beanie mascot and 4 social handles, then black | – | **digital silence 269.6–281.0 s** |

---

## 4. Script / communication mechanics

- **Two-hander Socratic dialogue + illustration montage.** The mentor holds **67 % of the words** (415 of 619) and the protagonist 33 % (204), across **33 speaker turns** in 73 lines. The protagonist's lines are complaints, questions or confessions. The mentor's lines are questions back, corrections, aphorisms and instructions. Once a habit is named, the VO continues over a 1–3 s inserted proof shot (room, alarm, water, bin, book, gym). Advice is never shown being followed for more than ~3 s.
- **Line length.** Median 7 words per sentence (p25 4, p75 10, p90 12, max 20). **39 % of sentences are ≤5 words**, only 6 % are ≥15. 17 % are questions. These are the shortest lines in the voiced corpus after v09.
- **Rhetorical devices, by timestamp:**
  - paternal address bookend (0:14 / 4:16)
  - identity mystery planted at 0:16, paid off at 4:13
  - antithesis either/or (0:37–0:42)
  - a stock "easy to say" objection answered by a reach-what-is-humanly-possible principle (0:42–0:47)
  - **list cut off mid-word** (1:13)
  - Socratic who-can-fix-this question with a sheepish one-word self-answer (1:16–1:20)
  - **echo-correction** of a feeling into a fact (1:38–1:41)
  - aphorism on a new camera angle (2:38)
  - self-aware meta concession about clichéd advice (3:38)
  - **gratitude triad** (4:02–4:07)
- **Exposition by prop, not by statement:** pill = hopelessness (0:06), beer→water = sobriety (1:56–2:00), alarm 7:00 = routine (1:55, 3:51), ash-bin = quitting (2:47), reflection in a dead TV = facing himself (2:11), mirror = result (3:56), empty chair = the mentor was internal (4:21). **Seven of the film's eight state changes are shown by an object or a drawing swap, not by a line.**
- **Visual "progress meter" on the body.** Costume and face encode progress: beanie + eye bags + stubble + red eyes (0:00–0:52), then bald with eye bags (0:56–2:44), then eye bags gone (2:45), then a fuller face (3:45), then a new jaw design (3:57). Viewers can tell where they are in the arc with the sound off.
- **Escalation.** Each station is a step up in social exposure: alone on a hill, then home, then workplace, then public street/park, then gym, then restaurant among couples. Where the mentor sits escalates too: standing over him, then an armchair in his home, then outside his workplace, then walking beside him, then seated opposite as an equal, then gone.
- **Withheld.** The mentor's identity (237 s). His name is never given. The protagonist never states a decision; the prop does.
- **Contrast devices.** Cartoon protagonist vs a photoreal still mentor, so the mentor reads as "not of this world". Night-blue/purple grade (despair) vs warm interiors vs daylight vs a bright vineyard (resolution). Big mentor vs small Doomer in the hilltop OTS, later equal side-by-side framing.
- **The ending.** Hope without a fairy tale. He has improved, but is **still alone** among couples in the last WS (4:26). Comments read this exactly (see §7). This is deliberate under-resolution, not a plot hole.

---

## 5. Visual grammar

- **Rhythm.** About 15 cuts/min through the coaching acts (median 2.6–3.8 s). It halves to **8/min with 8 s median shots** for gratitude/reveal: the ending is slowed down. Act breaks are pure-black cards of **2 s (0:54) and 1 s (2:15)**.
- **Camera.** There are effectively no animated camera moves. Scale changes are done by **re-cropping across a cut**: OTS 0:36, then a tighter mentor 0:37, then an ECU of crying at 2:09. One whip/motion-blur cut (3:14). No parallax observed: characters are flat cut-outs on single plates (medium confidence).
- **Compositing.** Hand-drawn white-faced characters with black outlines over **stock photographs** (living room, fast-food exterior, library, gym, streets, restaurant) or a **painted night plate** (the hilltop). The mentor is a **still photoreal render in B/W** with a slight brightness flicker; he never animates. TVs carry **screen-replaced footage** (gameplay 0:59 and 2:05; a self-improvement video at 2:56).
- **Transitions.** Hard cuts by default. **Dissolves carry meaning:** the eye bags disappear (0:52), the restaurant entrance with a ghosted face (4:00), the mentor's disappearance (4:19–4:21). Fade-in after each black card.
- **Colour as emotion.** Hilltop #22292E-range navy/purple · living room warm orange window light · workplace day exterior (graded darker → brighter at 2:16–2:17) · gym desaturated · restaurant bright daylight. The thumbnail repeats the dark→gold mapping.
- **Watermark.** A YouTube icon plus "Low Budget Stories", bottom-left, ≈2.5 % of frame height, white semi-opaque, on every story frame.
- **Title card.** None in-video; the title lives only in metadata and thumbnail. This differs from the "Life of a …" videos (v03 0:21, v06 0:16).

---

## 6. Audio grammar

- **Music.** 0:00–0:14: none (−44 dB ambience). The hilltop dialogue 0:14–0:50 runs with a near-silent bed (inter-line gaps −43 to −47 dB), which isolates the voices. The music bed enters with the living-room act (gaps around −28 to −34 dB from 1:19). Montage stretches push music up to −25…−28 dB RMS with a low spectral centroid (≈1.0–1.1 kHz), i.e. a soft, mellow instrumental (genre not verifiable from the 16 kHz mono file). **Peak −19.6 dB at 3:55–4:00 (mirror)**. Fade-out 4:20–4:30. **11.4 s of digital silence** under the black and the end card.
- **Speech over bed.** The median word level is −23.0 dBFS against a gap (bed) median of −33.9 dBFS, so speech sits **+10.9 dB** above the bed.
- **Voices.** Male, calm, unhurried. Line-median f0: protagonist ≈90–103 Hz, mentor ≈98–113 Hz, rising to 127–131 Hz on aphorisms and on the "first, tell me why" counter-question (3:08). The pitch ranges overlap, so **one or two performers cannot be determined** from this file (open question). Per-line RMS spans −20.4 to −27.1 dB (≈7 dB). The protagonist's hesitant one-word self-answer at 1:19 is the quietest line (−27.1 dB), a vocal shrink. The final exchange is 2–3 dB louder than the opening.
- **WPM.** 192 wpm inside dialogue blocks, articulation ≈3.7 words/s within lines. Turn gaps are tight at 0.3–0.5 s. The only long in-dialogue gap is the 1.1 s hesitation before that self-answer (78.6→79.7 s).
- **SFX.** None is clearly separable in the mono mix. A whoosh-like high-centroid event at 0:55–1:00 (act break) is unverified.
- **Silence as punctuation.** 0–14 s, 50–56 s, and 259–281 s. Silence frames both ends and the first decision.

---

## 7. Retention devices and why viewers stayed, replayed and commented

| Device | t | Evidence |
|---|---|---|
| **Sequel hand-off.** v01's last 22 s (3:10–3:32: hilltop, pill, hand, mentor) are v02's first 14 s on the same plates. v01's description links v02 and vice versa. | 0:00–0:14 | heatmap 1.00 at 0:00; v01 comment "lore accurate" 16,000 likes |
| **Open question in the first 20 s** (who is he?) paid off at the end | 0:16 → 4:13 | heatmap 0.77–0.87 on the payoff bins |
| **Visible transformation checkpoint every ≈20–30 s** | 0:52, 1:54, 2:01, 2:47, 2:50, 3:40, 3:56 | heatmap peaks at 1:55, 3:45, 3:56 |
| **Wordless "proof" inserts** inside the talk | 1:53–2:01, 2:46–2:47, 3:21–3:31 | 31 % of runtime wordless |
| **Payoff slowed + silence** | 4:00–4:40 | cut rate drops to 8/min |

Comment themes (400 top comments, 78,452 likes in total):
- **The mentor as inner voice / higher power**: top 2 comments (19,000 and 11,000 likes), plus "everyone has one inside" variants (≈900+ likes in total).
- **Realism of the non-magical ending**: no riches, no girlfriend, still happier (8,400). The still-alone ending read as both inspiring and depressing (408).
- **Aphorisms rewritten by viewers as quotes**: 6,400 likes for a paraphrase that is **not** a line in the script; 2,500 for a near-verbatim line; 90 for the 2:19 aphorism with a timestamp. Viewers condense the theme into their own one-liner. A script needs 2–3 quotable ≤12-word lines to seed this.
- **Personal testimony from rock bottom**: 2,000; 1,200; 920; 859; 329. Thank-yous in several languages (Korean comments ≈660 + 123 + 97 + 63 likes).
- **Craft details noticed**: the reflection in the dead TV at 2:10 (879).
- **Requests for more**: a 5-episode series (1,600).

---

## 8. Weaknesses / risks (what would not transfer)

1. **It depends on lore equity.** Its power rests on v01 (6.4 M views) having built the character and ending on this exact cliffhanger. A new channel has no equivalent. **Fix:** make the redemption piece the second half of our own two-part arc, published within ≤4 months of part 1 (here it was 109 days).
2. **The mentor is a real person's photo-meme.** That is a likeness/IP risk. It also never animates, which only works because the meme is recognisable. We need an **original mentor design** with the same function: visually from "another layer of reality", larger than the protagonist, never lip-synced.
3. **Real brands and works on screen**: fast-food brand marks (2:16), a real finance book cover (2:50–2:53), a real YouTuber video on a TV (2:56–3:01), a crypto poster. Do not copy.
4. **Generic self-help content.** Clean room, sleep, quit alcohol/smoking, read, greet people, gym. The script has to pre-empt the cliché with a meta line (3:38). The replay curve's lowest stretch (1:21–1:32, 0.17–0.20) is the verbal complaint list with no visual event.
5. **The book gag at 2:56–3:01 is unreadable.** Is consuming self-help videos instead of reading a joke or not? No line clarifies it.
6. **Non-native English register** (uncontracted verbs, literal idioms) reads as earnest-stilted. It works for this deadpan mentor tone but would grate in comedy.

---

## Why it works

- **It literalises an internal process.** The inner voice is cast as a second character, so self-talk becomes dialogue and decisions become props (pill, water, ash-bin, mirror, empty chair). Viewers who are at that low point recognise their own head (the testimony comments).
- **One question, held for 237 s** (who is he?), answered with a twist that re-frames everything and points back at the viewer.
- **Progress you can see with the sound off**: costume, eye bags, posture and face design change on a schedule, every ≈20–30 s.
- **Realistic under-resolution.** He fixes his habits, not his circumstances: still the same job, still alone. That makes the hope credible, and the comments say so explicitly.
- **Packaging matches content**: a dark→bright, before→after thumbnail with a single arrow, and a title that is a two-state transformation (X → Y).

## Rules to copy

1. **[KOPYA]** For a redemption story, cast the inner voice as a separate original character who **never moves his mouth**: a still render, held 3 s before his first line, entering by touch (a hand on the shoulder) ≥2 s before his face is shown.
2. **[KOPYA]** Plant the mentor's identity question in the first 20 s and answer it in the last 10 % (here 0:16 → 4:13 of 4:41). The answer must re-frame the whole film.
3. **[KOPYA]** Split the coaching into **4 stations**, each in a new location with one rising social stake: alone, then home, then work, then public. Change the mentor's position each time: over him, then opposite, then beside, then gone.
4. **[KOPYA]** Show every piece of advice as a **≤3 s proof insert under the VO**, never a full scene: before/after of the same plate 1 s apart, a swapped prop, an alarm clock.
5. **[KOPYA]** Show every inner decision as a **drawing swap or prop**, not a line: eye bags dissolve, cigarette in the bin, dead-TV reflection. Target ≥6 such non-verbal state changes in a 4–5 min film.
6. **[KOPYA]** Keep 25–35 % of the runtime wordless (here 31 %), concentrated in montage, relapse and payoff.
7. **[KOPYA]** Dialogue lines: sentence median ≤7 words, ≥35 % of sentences ≤5 words, ≤10 % ≥15 words. Give the mentor ≈⅔ of the words. The protagonist talks in complaints, confessions and one-word answers.
8. **[KOPYA]** Write 2–3 aphorisms of ≤12 words. Give the main one **its own camera angle** (a profile CU used only once) and a +20–30 Hz lift in delivery.
9. **[KOPYA]** Use one callback prop at least twice (the 7:00 alarm at 1:55 and 3:51), the second time without comment.
10. **[KOPYA]** Put the transformation peak (mirror/new face) at **80–86 % of the runtime** as a wordless 6–8 s shot with the loudest music of the film (≥3 dB above the dialogue sections).
11. **[KOPYA]** Slow the final 10 % to ≤8 cuts/min, then 4 s of black and silence before the end card. Use no music under the end card.
12. **[KOPYA]** End improved but **not rescued**: the last wide shot keeps the original lack visible (alone among couples).
13. **[İYİLEŞTİRME]** Give the complaint/whining stretch a visual event every ≤5 s (here 1:21–1:32 is the lowest replay at 0.17). Cut the list to 3 items and show each as a 1 s insert.
14. **[İYİLEŞTİRME]** Replace generic guru advice with 1 specific, slightly surprising action per station. Keep the meta-concession line if a cliché is unavoidable.
15. **[ETİK]** The mentor must be an **original character** with no real person's photo or likeness. No real brand logos, book covers, YouTuber footage or crypto propaganda on screen; use invented equivalents.
16. **[ETİK]** Keep the rock-bottom imagery (pill = hopelessness) symbolic. Never depict self-harm methods, and close on hope. The comments include a bereavement story; the audience includes at-risk viewers.

## Open questions

- Are the protagonist and mentor voiced by one performer or two? Their f0 ranges overlap (90–131 Hz), and voice-matching needs the full-band audio.
- Is the voice human-recorded or synthetic? No artefact test was possible on 16 kHz mono.
- Which music track is it? The description in the info file was not parsed for credits (v09's description lists track credits; v02's may too).
- What is the intended reading of the self-improvement-video-on-TV beat (2:56–3:01)?
- What is retention, as opposed to replay? The heatmap cannot show drop-off in the 1:21–1:32 sag.
