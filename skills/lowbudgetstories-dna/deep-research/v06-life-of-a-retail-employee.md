# v06: "Life of a retail employee" (4h_3TRhCas0): per-second teardown

Analyst 2. Evidence: all 51 sheets of 1 fps (000–050), all 15 sheets of 4 fps intro (000–014), the thumbnail, a key-frame montage (s0017, s0018, s0041, s0101, s0130, s0153, s0155, s0216, s0231, s0240, s0268, s0345, s0356, s0361, s0437, s0442), a subtitle crop strip (s0228–s0241), cuts.csv / scdet / metrics / silences, the RMS envelope in 10 s bins, the bed level in inter-line gaps, per-line f0, faster-whisper word timestamps, the heatmap, and 400 comments.
Character labels (Wojak, Zoomer/Jimmy, Brian, Karen, NPC, Chad) describe the channel's meme cast **for analysis only**. Every rule means "an original character that fills this role".
Whisper caveat: it mis-hears the protagonist's name as "Jack" (2:31, 6:06) and garbles the gossip lines at 3:51–3:59. The burned-in subtitles are authoritative there.

---

## 1. Card

| Field | Value |
|---|---|
| Title | Life of a retail employee |
| Views / likes / like% | 3,460,306 / 93,229 / **2.69 %**. This ties v03 for the **lowest** like rate in the top-10 (range 2.69–5.49 %). |
| Comments | 5,800, which is **1.68 per 1,000 views** (corpus 0.79–2.70). That is high for a comedy: the job videos convert views into testimony, not likes. |
| Upload | 2023-10-07, 12 days **before** v03 "Life of a Fast Food employee" (2023-10-19, 4.93 M). Both are the 452–453 s template. |
| Duration | 453.5 s: 446 s of story, then a 7 s end card. |
| Format family | "Life of a …" job series. Ensemble workplace comedy, voiced (≥14 speaking roles), with a wordless cold open. |
| Thumbnail (1280×720) | **No text.** Three waist-up characters in identical bright-blue store polos (#017CE6 = 30 % of pixels) with a yellow spark logo and white name tags carrying the channel name. **Centre ≈45 % of width, full height (head cropped at the top edge):** the protagonist, deadpan, purple eye bags, the only face looking straight at the camera. **Left ≈25 %:** a blonde female coworker with a bun, tongue out, mocking. **Right ≈25 %:** a glasses-wearing coworker with a stitched neckbeard and a mirrored name tag, side-eye. Background: a blurred big-box store photo with a "SEAFOOD" sign (mid-third mean #7EA9CC, bright). The trio sets up the cast and the mood (tired / mocking / creep) without a plot. |
| Description / tags | One paragraph names the store as a parody of a real chain and the two coworker types, then says it applies to all retail chains (it lists several real chain names: an SEO line). Then donations and socials. Tags are the channel's generic meme/crypto set. |
| Cuts | @score≥8: **103 cuts = 13.63/min**, median shot **3.32 s**, mean 4.36 s, **max 20.3 s**. |
| Cut rate by act (measured) | routine 0–16 s: **26.2/min (median 2.1 s)** · title 16–26: 12.0 · arrivals 26–52: 13.8 · shelf talk 52–99: 20.4 · Karen 99–153: 12.2 (4.4 s) · interruptions 153–215: 14.5 · break room 215–242: 13.3 (max 15.0) · cock-block 242–275: 14.5 · **stocking alone 275–312: 8.1 (max 19.8)** · toilet hunt 312–353: 11.7 · **toilet/manager 353–375: 8.2 (max 17.0)** · Alice argument 375–429: 12.2 · Chad payoff 429–446: 14.1 |
| Loudness | **−22.5 LUFS**, **LRA 15.7 LU** (the widest dynamic range of the two assigned videos). silencedetect pauses ≥0.35 s: **18 (9.8 s total)**, clustered at 4:17–4:55 (argument beats) and **5:45–5:56 (four pauses, 2.6 s, right before the toilet door opens)**. |
| Speech | 781 words, 103 sentences. **First word at 26.6 s.** 103 wpm over the runtime, **159 wpm inside dialogue blocks**. Wordless gaps ≥3 s: 14 of them, totalling **159 s = 35 %** (0–27, 208–227, **309–358 = 49 s**, 371–378…). |

**Heatmap top peaks.** Bins are 4.54 s. The values measure replay density.

| # | Bin | Value | On screen |
|---|---|---|---|
| 1 | 0:00–0:05 | 1.00 | Alarm 5:59→6:00, bed, mirror (start artefact + hook) |
| 2 | **7:20–7:25** | **0.93** | Final punchline: the boyfriend's arm fills 35 % of the foreground. The creepy coworker raises a finger and threatens to scream if hit, a callback to the Karen at 2:18. |
| 3 | 0:41–0:45 | 0.71 | Third arrival. The protagonist's face turns to a scowl, and his inner voice dreads having to work beside this coworker (pattern break after two neutral greetings). |
| 4 | 6:03–6:08 | 0.66 | The manager discovers the coworker on the toilet with the door open. This sits inside a **17 s static 3-shot**. |
| 5 | 4:28–4:32 | 0.45 | The love interest smiles and asks to sit. The protagonist grins openly (the only grin of joy in the film), and then the creepy coworker walks in. |
| 6–8 | 3:38–3:42 (0.34) · 3:56–4:01 (0.30) · 3:47–3:52 (0.30) | – | He cries after seeing the muscular coworker get "his" hero moment · the gossip table laments the lack of gentlemen while he sits alone behind them |
| low | **1:53–2:30** | **0.009–0.05** | The middle of the Karen argument: 3 reused plates, median shot 4.4 s. The lowest replay in the video. |

---

## 2. Premise, turn, emotional arc

**Premise (one line).** One shift in a big-box store. A tired stocker wants to be the hero for the cute cashier, but customers, a creepy coworker and the manager keep blocking him. In the end her muscular boyfriend shows up.

**The turn.** The first-half turn is **2:35–3:38**: he finally decides to step in against the Karen, three customers block him in a row, and the muscular coworker planted at 0:31 takes the hero moment instead. The final turn is **7:16** (96 % of the runtime): the boyfriend reveal voids the entire rivalry the second half was built on.

| # | t | Point | Evidence |
|---|---|---|---|
| 1 | 0:00 | **Dread** | alarm 6:00, eye bags, forced grin in the mirror |
| 2 | 0:41 → 0:48 | **Disgust → relief** | scowl at the third arrival; then the friendly coworker pops in and he laughs |
| 3 | 1:23 | **Longing** | his eyes follow the cashier walking past (wordless) |
| 4 | 2:38 | **Resolve** | his face hardens under the inner monologue; he walks toward the checkout |
| 5 | 3:29 → 3:38 | **Frustration → humiliation** | third interruption sigh; crying CU after the muscular coworker steps in |
| 6 | 4:28 → 4:55 | **Hope → crushed** | open grin when she sits down; crying CU after the coworker drags him away |
| 7 | 6:09 | **Injustice** | the manager scolds both equally; he cries |
| 8 | 7:16 → 7:24 | **Comic defeat** | boyfriend reveal, then the callback punchline |

---

## 3. Beat sheet / visual script

### 3a. First 20 s (4 fps)

| t (s) | Shot | Who | Scale / BG | Motion / text / audio |
|---|---|---|---|---|
| 0.00–1.00 | green digital alarm clock flips 5:59 → 6:00 | – | ECU; dark bedroom photo | music/SFX bed −28.6 dB, bright (centroid 2.7 kHz) |
| 1.40 | cut | | | |
| 1.25–2.50 | in bed, head barely lifted, purple eye bags | protagonist | MCU; bed photo | – |
| 2.70 | cut | | | |
| 2.75–4.00 | bathroom mirror, shirtless, brushing teeth (reflection, washed-out) | protagonist | MS | – |
| 4.30 | cut | | | |
| 4.25–6.00 | a white cartoon hand takes a blue polo from a rail of **identical blue polos** | hand | insert | sameness gag |
| 6.40 | cut | | | |
| 6.25–8.50 | mirror again, now in uniform. **Forced teeth grin 7.25–8.50**, clenched fists | protagonist | MS | wordless self-pep-talk |
| 8.60 | cut | | | |
| 8.75–10.50 | concrete graffiti wall, rusty door. He steps out of the dark doorway at 9.25 | protagonist | WS | – |
| 10.70 | cut | | | |
| 10.75–12.50 | on a bus, rain on the window, looking at his phone | protagonist | MCU | – |
| 12.80 | cut | | | |
| 12.75–13.25 | a vehicle passes in a blur (object wipe) | – | – | – |
| 13.25–15.75 | back view walking toward the store front (stock photo with a parody logo) | protagonist | WS | camera tilt-up starts at 15.0 |
| 16.00–18.60 | **tilt continues to blue sky; title card** | – | sky | **Text:** "LIFE OF A RETAIL EMPLOYEE", white, heavy rounded display caps, ≈7 % of frame height, ≈67 % of frame width, centred at y≈45 %. Beneath it the channel name, ≈2.5 % height. The title slides in with the tilt (16.0–17.0) and holds to 18.6 (2.6 s on screen). |
| 18.76–18.84 | soft transition (scdet 4.6–7.6, no hard cut) | | | |
| 18.75–22.75 | break room (blue cinder block, lockers, coffee machine, US flag), protagonist standing small (≈25 % of height) | protagonist | WS | static |

The first 13 s are **7 shots of 1.3–2.2 s (26 cuts/min)**: the fastest stretch of the film, with zero words.

### 3b. Rest of the film, per beat

| Beat | t | What happens | Frame / BG | Audio / text |
|---|---|---|---|---|
| B2 Arrivals (rule of three + reversal) | 0:23–0:52 | Same WS plate and same CU reaction plate, alternated. **Arrival 1**: the old manager in sunglasses, shirt and tie greets everyone (0:26), and the protagonist answers with one tired word (0:29). **Arrival 2**: a blond pompadour muscular coworker greets everyone (0:32), and he answers the same way (0:35). **Arrival 3**: the glasses/neckbeard coworker. **His face turns at 0:40.5**, and his inner voice begs not to be paired with him (0:40.9–0:44.7). **Reversal (0:45)**: a friendly orange-haired zoomer coworker pops in from the right and says they are working together. Relief and an open laugh (0:48.75–0:50.25). | WS break room · CU reaction · 2-shot by the coffee machine; radial zoom-blur micro-transitions at 0:46.25 and 0:52.75 | first spoken word at 26.6 s; heatmap 0:41–0:45 = 0.71 |
| B3 Shelf talk (escape dream) | 0:53–1:38 | Back view at a roll cage of boxes; **heads turn toward camera when speaking** (walk-and-talk substitute). Topics: crypto losses, rent, the year everyone could escape, a former coworker who made it out, a degree in progress, and the agreement that money is the only reason to be here. **1:18–1:21, wordless**: the blonde cashier walks behind them with a roll cage. His eyes follow her (1:23–1:24). **1:33–1:38**: POV down the aisle to her checkout, his second glance. | stock aisle photo; CU/CU shot/reverse (his BG blurred, the friend's BG sharp) | 20.4 cuts/min; heatmap bump 1:17–1:26 (0.25–0.27) |
| B4 Karen | 1:39–2:33 | An obese customer on a mobility scooter leaves (1:39–1:40). A Karen enters (1:41, short blonde hair, pink sweater, arms crossed). Escalation ladder: she complains about prices, then demands a discount, then claims to know the CEO, then rejects being spoken to, then threatens to scream, then **counts to three** (2:24–2:29). **2:33: payoff**: her face turns red, bloodshot eyes, mouth open screaming; the cashier sweats. | 3 plates reused for 52 s (WS checkout; MS Karen foreground; MS cashier foreground). Register display reads in red. | median shot 4.4 s; **heatmap 0.009–0.05 (lowest)** |
| B5 Call to heroism | 2:34–2:42 | His wide-eyed CU, **with the screaming checkout visible in the background left (≈20 % of frame)**: reaction and action in one composite. Inner voice: another Karen, this is his chance to show masculinity (2:30–2:41). His face hardens (2:38), he turns and walks (2:40–2:42). | CU with deep background | inner monologue in his own voice |
| B6 Interruption ladder ×3 | 2:43–3:29 | **#1 (2:43)**: a grey NPC customer steps into his path and asks where the milk is. He points. The NPC asks to be shown. Forced grin (2:59–3:00), dissolve to the drinks aisle (3:01), he hands over the milk. He **re-commits** (3:08, inner voice: time to help her now). **#2 (3:10)**: a hand taps his shoulder; a grandma pops in from the foreground and asks for pizza. He takes her (3:20–3:23). **#3 (3:25)**: a second grey NPC asks for vegan products. **His eyes close (3:29)**: the sigh is the punchline, no line. | aisle photos (pasta, drinks, pizza); 2-shots | each interruption takes ≤2 s from his resolve to the block |
| B7 Hero stolen | 3:30–3:39 | Glare (3:32–3:34). **POV (3:35–3:37)**: tiny figures (≈12 % of frame height) at the far checkout. The muscular coworker from arrival 2 is now standing with the Karen and the cashier: the 0:31 setup pays off. **Crying CU (3:38–3:39)**: blue tear streaks, gritted teeth. | WS aisle → CU | heatmap 0.34 |
| B8 Break room irony | 3:40–4:01 | Alone at a round table with his phone (3:40–3:43). WS (3:44–3:46): a hi-vis zoomer on his phone, a gossip table of three women, a blond guy. The gossip covers who didn't clean the toilets and how gross men are at the toilet (the **toilet payoff is planted here**). One woman's line is in a non-English language (comment, 2,800 likes). **Burned-in subtitles** (white, black outline, bottom centre, y≈93–95 %) at 3:51–3:52 (with the typo "was is") and 3:59–4:01 (the lament about the lack of gentlemen). The protagonist, the gentleman, sits alone **in frame between them**. | 3-shot with him in the background, center | heatmap 0.30 |
| B9 Hand-over | 4:02–4:22 | The friendly coworker signs off for the day (4:03). The protagonist asks who takes over (4:07). **OTS reveal (4:14–4:15)**: the creepy coworker sits at a far table on his phone. This fulfils the fear from 0:41, 3.5 min later. Sad CU (4:16–4:18). The friend exits left (4:19–4:20). | MCU 2-shot; OTS from behind both heads | – |
| B10 Cock-block | 4:23–4:55 | The cashier enters from the right (4:23) and asks to sit (4:24). **CU of her slight smile (4:25–4:27). His open-mouth grin (4:28–4:29).** The creepy coworker appears standing over them (4:30) and says their break is over. He refuses, then threatens to report to the manager, using the **same refusal formula the Karen used at 1:46** (verbal mirror: he is a male Karen). **4:34.5–4:54.8: a single 2-shot held 20.3 s** (the longest shot of the film); only mouths and eyes change. Crying CU (4:55–4:56). | break room | pauses 4:17–4:55 (9 of the 18 pauses) |
| B11 Dump | 4:57–5:12 | At the shelf, a man on a red mobility scooter asks for burgers (5:03–5:05). The **creepy coworker volunteers (5:07) with a toothy grin** and leaves with him, dumping the stocking on the protagonist (glare foreground, 5:08–5:11). | CU foreground / background | – |
| B12 Alone + hunt | 5:12–5:54 | Stocking alone, back view, "Men's Wear" sign (5:12–5:17). **Clock insert, hands sweep 1:30→2:00 (5:18–5:22)**: time skip. Looking left and right (5:25–5:30). Searching aisles (5:31–5:42). Swing doors to the back (5:43–5:44). Warehouse (5:45–5:48). Storage aisle with a toilet door in the far background (5:49–5:52). **Insert of a "TOILET" pictogram sign (5:53–5:54).** | **49 s wordless (309–358 s)**; 8.1–11.7 cuts/min | music only at −37 to −40 dB RMS; 4 pauses 5:45–5:56 (tension) |
| B13 Toilet | 5:55–6:12 | The door opens (fade from dark): the coworker sits on the toilet with his phone, smug (5:55–5:57). The protagonist insults him (5:58). **The manager enters with motion blur (6:00)**, asks why the door was open, says it is not tolerated, and sends both back. **The protagonist cries while being scolded equally (6:09–6:11).** | **static 3-shot held 17.4 s (5:58.0–6:15.4)** | heatmap 0.66 at 6:03–6:08 |
| B14 Time-lapse | 6:12–6:14 | Store exterior; the sky grade shifts blue → pink/purple dusk | exterior photo | – |
| B15 Rivalry | 6:15–7:08 | Back view of both at the shelf (6:15–6:17). The coworker threatens him. The protagonist asks what his problem is and mocks his age (≈34). The coworker accuses him of staring at the cashier and lays claim to her, escalating through four rungs: ownership, then the claim that she simply hasn't realised it yet, then a self-awarded medieval protector title, then a guardian duty (6:29–6:55). Face-off with mutual dares (6:56–7:08). | shot/reverse CUs alternating every 3–6 s (6:18–6:55), then a 2-shot face-off (6:56–7:08); hand on chest at 7:07 | – |
| B16 Reveal | 7:09–7:20 | The cashier enters (7:09) and asks if they are talking about her. She **doesn't remember the coworker's name** (7:13–7:15). **Her boyfriend appears (7:16)**: tanned, mohawk, mustache, beard, black tank top, the deepest voice of the film (f0 81 Hz). He asks if these guys are bothering her. She shrugs teasingly (7:18–7:20). | CU cashier; 2-shot couple | – |
| B17 Callback punchline | 7:20–7:25 | The boyfriend's arm fills ≈35 % of the foreground. Both coworkers are deflated. **The creepy coworker raises an index finger and threatens to start screaming if hit (7:21.8–7:24.3)**: the Karen's threat from 2:18, now in a man's mouth. Hard out. | MS 3-shot | heatmap 0.93; this line sits at −32.6 dB, the quietest line (whimper) |
| B18 End card | 7:26–7:33 | Orange end card (#ED720B ≈60 % of frame) with the beanie mascot and socials, then black | – | – |

---

## 4. Script / communication mechanics

- **Spine: desire versus blockers.** The protagonist wants one thing (to be noticed by the cashier), and every scene is a new blocker: customer, customer, customer, coworker, manager, coworker, boyfriend. **8 blocks in 7:33, one every ≈52 s.** The desire is never stated aloud until the antagonist voices it for him (6:29). Before that it is carried by 3 wordless glances (1:23, 1:37, 4:28).
- **He is the reactor, the world talks.** By manual attribution (approximate), the protagonist speaks ≈27 % of the 781 words. ≥14 roles speak. His most expressive moments are **wordless**: the scowl (0:40), the sigh (3:29), 4 crying CUs (3:38, 4:55, 6:09, 2:42-adjacent), the grin (4:28).
- **The inner monologue sets up each interruption gag.** The inner voice states the intention (0:40, 2:30–2:41, 3:08), and the next shot blocks it in ≤2 s. Intention said, then denied, is the core comic unit (3 times in 2:30–3:29).
- **Line length.** Median 6 words per sentence (p25 3, p75 10, p90 14). **49 % are ≤5 words.** 26 % are questions: customers ask, he answers. Register: everyday workplace English, mild profanity (2 instances), meme slang (bro, rat race, masculinity, knight).
- **Escalation ladders inside scenes:**
  - The Karen: complain, then demand, then status claim, then indignation, then threat, then countdown, then scream (52 s).
  - The interruptions: NPC, then grandma, then NPC again; the third costs him the moment.
  - The rival's claim: 4 rungs of delusion in 26 s.
  - Across the film: annoying customer, then lost hero moment, then lost seat with her, then unjust punishment, then lost girl.
- **Repetition and callback map:**
  - Same reaction-CU plate for the 3 arrivals (0:28 / 0:34 / 0:40).
  - Threat to scream: Karen 2:18, then the rival 7:21 (final line).
  - The refusal formula ("do not accept"): Karen 1:46, then the rival 4:47.
  - Fear of being paired with the rival, voiced at 0:41, fulfilled at 4:14.
  - Toilet gossip at 3:47, then the toilet reveal at 5:55.
  - The muscular coworker introduced wordlessly at 0:31, then steals the hero moment at 3:35.
  - The cashier's glances 1:23, then 1:37, then 4:28.
  - **The crypto/escape thread (1:03–1:21) is set up and never paid off** (see §8).
- **Withheld information.** Where the rival went (5:12 → 5:55, 43 s hunt, wordless). The cashier's boyfriend (withheld for the whole film, revealed at 96 %). The viewer is ahead of the protagonist at 4:14 (sees the rival before he does) and **behind** him at 7:16.
- **Visual irony.** Women lament the absence of gentlemen while one sits alone in their frame (3:59). The forced mirror grin (0:07) foreshadows the customer-service grin (2:59, 3:00).
- **The ending.** A comic defeat plus an absurd callback, cut on the punchline with **no reaction beat** after it (hard out to the end card within 2 s). The protagonist's situation is unchanged and slightly worse.

---

## 5. Visual grammar

- **Rhythm.** A wordless 26/min open, then 12–20/min through dialogue, dropping to **8/min with 17–20 s holds** for the two rival confrontations (4:34, 5:58). Static long holds are used **when the comedy is in the words** and the absurdity lands without cutting.
- **Camera.** One true animated move: the **tilt-up to the sky for the title** (0:15–0:18). Radial zoom-blur whip transitions (0:46, 0:52.75, 1:55, 2:03). One dissolve as a time skip (3:01). A fade from dark to open the toilet door (5:55). A motion-blur entrance for the manager (6:00). Scale is otherwise changed by cutting between plates.
- **Plates.** Real big-box store photographs with the chain logo replaced by a parody wordmark: aisles, checkout, warehouse, break room, exterior. Characters are flat hand-drawn cut-outs. The **name tags carry the channel name** (in-world branding), and the rival's tag is mirrored (a flipped asset).
- **Depth trick.** Reaction CU in the foreground with the action small in the background (2:34–2:37 Karen screaming; 3:35 POV to the checkout; 5:08 the rival grinning behind). Two beats in one frame.
- **Time devices.** The alarm clock (0:00), clock hands sweeping 30 min (5:18–5:22), and the exterior sky time-lapse (6:12–6:14). The exterior time-lapse also appears in v03 at 4:06–4:09: a shared channel device.
- **Colour.** The fluorescent retail blue dominates. Emotion lives **in the face drawings** (blue tear streaks, the red/bloodshot Karen face, sweat drops), not in the grade, except for the dusk time-lapse.
- **Text on screen.** Only the title card, 2 subtitle lines, a "TOILET" sign insert, a parody store wordmark and aisle signs that carry the channel name. That is ≤1 text element per 90 s.
- **Watermark.** The same bottom-left channel mark as v02.

---

## 6. Audio grammar

- **Music.** The wordless open has a bright music/SFX bed (−28.6 dB RMS, centroid 2.2–2.7 kHz) that stays under the dialogue at **−37.9 dBFS median in inter-line gaps**, with speech at −25.2 dBFS (**+12.6 dB** over the bed). The 49 s wordless stretch (5:09–5:58) drops to −37…−40 dB RMS: quiet, tension. **LRA 15.7 LU**, wide because of these quiet stretches against the shouting.
- **Voices: pitch-cast ensemble** (line-median f0): the protagonist and his inner voice ≈94–108 Hz (same voice for both); the friendly coworker and the rival ≈145–180 Hz; the Karen 150–204 Hz; the manager 127–140 Hz; the grandma ≈168 Hz; **the boyfriend 81 Hz, the lowest line of the film**, given to the alpha. The film has ≥5 distinguishable voices. Whether they are human actors or synthetic is not determinable here.
- **WPM.** 159 wpm inside dialogue blocks; 103 over the runtime.
- **Silence and pauses.** 18 pauses ≥0.35 s. Four (2.6 s) sit right before the toilet reveal (5:45–5:56), building tension. The rest punctuate the break-room argument.
- **SFX.** Not separable in mono at 16 kHz. Likely an alarm (0:00) and a door (5:55); unverified.
- **The final line is whispered/whimpered** (−32.6 dB), so the punchline lands on a small voice.

---

## 7. Retention devices and why viewers stayed, replayed and commented

| Device | t | Evidence |
|---|---|---|
| Wordless 16 s routine at 26 cuts/min before any word or title: an "everyone knows this morning" hook | 0:00–0:16 | heatmap 1.00 at 0:00 |
| Pattern break on the third arrival | 0:41 | heatmap 0.71 |
| Visible desire (glances) then repeated blocking, so the viewer waits for him to "win" | 1:23 → 7:16 | peaks at 3:38, 4:28 |
| Planted payoffs (toilet gossip, the muscular coworker, the rival fear) | 3:47→5:55, 0:31→3:35, 0:41→4:14 | heatmap 0.66 on the toilet payoff |
| Final line is a callback | 7:21 | heatmap 0.93 |

Comment themes (400 top comments, 88,837 likes; "work" appears in 195 comments with 63,400 likes, "retail" in 105 with 13,840, "customer" in 51 with 5,575):
- **Moral take on customers**: the top comment (21,000) is about adults' lack of critical thinking; a "customers are getting dumber" comment (2,000).
- **Job testimony** ("I worked at … for N years"): 8,800, 3,300, 3,100, 3,100, 1,500, 1,300, 1,300, 703, 694, 516, 466, 314, 290… This is the dominant genre of comment. The video works as a **prompt for viewers' own stories**.
- **Accuracy checks of specific details**: phone on the toilet (3,200), the lunch room "at 3:50" (2,500), a coworker speaking a foreign language (2,800), customers asking where obvious items are (348; 130 for the chain of show-me requests), the price-complaining Karen (226). One counter-nitpick (customers ask the person dragging pallets, 1,000) is still an accuracy discussion.
- **The work crush who always has a boyfriend**: 3,200, 753, 609, 145. The ending is read as painfully relatable.
- **Production value versus channel name**: 7,000.
- **The crypto 2021 escape line**: 1,100 (a reference that lands even without a payoff).

---

## 8. Weaknesses / risks

1. **Mid-film sag in replay.** 1:53–2:30 (0.009–0.05) is the Karen argument, 52 s on 3 reused plates with a 4.4 s median shot, building to a single payoff. **Fix:** cap single-gag escalations at ≤30 s or insert a cutaway gag every ≤10 s.
2. **Dangling setup.** The crypto/escape thread (the coworker who got out, the degree) is never paid off. It is pure world-building that costs 25 s.
3. **Two 17–20 s static holds.** These work because the dialogue is absurd, but they are the riskiest seconds for drop-off (the heatmap shows replay, not retention; unverified).
4. **IP / brand risk.** Parody of a real chain's logo and uniform (blue vest, yellow spark mark), a real store interior with signage, chain names listed in the description. Do not copy: invent a fictional chain with its own colour and mark.
5. **Stereotype risk.** Karen, an obese customer on a mobility scooter (twice), toilet humour, a "creepy" coworker. These are high-reward in comments but carry demonetisation and fairness risk. Keep the antagonist's **behaviour** the joke, not their body.
6. **The ending hierarchy relies on meme canon** (the muscular alpha always wins). It needs an original visual design that reads "alpha" in ≤1 s without the meme.
7. **Subtitle typo** at 3:51 and a whisper-unfriendly mix. Small quality debt.

---

## Why it works

- **Universal job pain, rendered as a checklist viewers can tick**: dumb questions, the Karen, the creepy coworker, the unfair manager, the break-room gossip, the work crush. Each is a 30–60 s vignette, and each produces its own comment thread of testimony (the 1.68 comments per 1k views are the proof).
- **One simple want, blocked 8 times.** The desire is visible (glances) but never stated by the protagonist, so the viewer supplies it.
- **Setups that pay off 1–4 min later** (rival fear, toilet gossip, the muscular coworker, the scream threat): the film rewards attention in a 7.5 min video.
- **Pantomime between the talk.** 35 % wordless, with the protagonist's biggest emotions all silent close-ups.
- **The punchline as a callback**, cut hard with no reaction shot.

## Rules to copy

1. **[KOPYA]** Open with a **wordless morning-routine montage of 7 shots × 1.3–2.2 s** (alarm flips to the hour, bed, mirror, uniform from a rail of identical shirts, forced mirror grin, commute, arrival). No words before 25 s.
2. **[KOPYA]** Title card at **3.5–4.7 % of the runtime** (here 0:16 of 7:33): white heavy rounded caps ≈7 % of frame height on a plain sky, attached to a tilt-up, on screen ≈2.5 s, channel name ≈2.5 % beneath.
3. **[KOPYA]** Introduce the cast by **three arrivals on the same WS/CU plates**. The third breaks the pattern (dread face plus a ≤12-word inner line), then a fourth reverses it (relief). Total ≤30 s.
4. **[KOPYA]** Give the protagonist one physical want, shown **only through ≥3 wordless glances** in the first 5 min. Let an antagonist say it aloud later.
5. **[KOPYA]** Block the want **6–8 times, ≈1 block per 50–60 s**, each block a different archetype (customer, customer, customer, coworker, boss, rival, alpha). An original character fills each archetype.
6. **[KOPYA]** Comic unit: **inner voice states the intention, then a block arrives ≤2 s later, then a wordless reaction**. Run it as a ladder of 3 (two neutral blocks, the third costs the prize).
7. **[KOPYA]** Plant each payoff with a wordless or throwaway setup **60–240 s earlier** (a background character, a gossip topic, a feared pairing). Aim for ≥4 setup→payoff pairs in a 7 min film.
8. **[KOPYA]** The final line must be a **callback of an earlier antagonist's line transferred to a new speaker**. Cut to the end card ≤2 s after it, with no reaction shot.
9. **[KOPYA]** Keep the protagonist at ≤30 % of spoken words; his strongest beats are silent CUs (≥4 crying/grimace CUs, one open grin).
10. **[KOPYA]** Pitch-cast the voices: the protagonist low and flat (≈95–110 Hz), the irritants high (≥150 Hz), the alpha **lowest** (≈80 Hz) and used for ≤2 lines.
11. **[KOPYA]** Include one **≥40 s wordless search/stocking sequence** with a time-skip device (clock hands, exterior time-lapse) before a reveal, with music dropped to ≈−38 dB RMS and 2–4 short pauses before the reveal.
12. **[KOPYA]** Use the reaction-in-foreground / action-in-background composite for at least 3 beats.
13. **[İYİLEŞTİRME]** Cap a single escalating argument at ≤30 s or insert a cutaway gag every ≤10 s (the Karen stretch hit the lowest replay, 0.009–0.05).
14. **[İYİLEŞTİRME]** Every setup thread must pay off; if a world-building thread (crypto escape) cannot pay off by the end, cut it to ≤8 s.
15. **[İYİLEŞTİRME]** Proofread burned-in subtitles; use them only for lines that are fast, overlapped or non-English.
16. **[ETİK]** Invent the store chain (name, colour, logo) and never mimic a real retailer's mark or uniform. Use original characters for every archetype. Don't make body type or disability the joke: the antagonist's *behaviour* is the joke.

## Open questions

- Are the voices human actors or synthetic? There are ≥5 distinct pitch profiles; this file cannot tell.
- What language is the foreign-language gossip line (≈3:51–3:56)? Whisper renders it as garbled English. A Dutch line would fit the creator's other non-native traces.
- Retention vs replay: do the 17–20 s static holds cause drop-off? Not visible in replay data.
- What is the music track, tempo and key? Not derivable from the 16 kHz mono file with confidence.
