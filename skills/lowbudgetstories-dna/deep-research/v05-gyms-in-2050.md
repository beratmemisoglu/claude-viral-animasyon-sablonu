# v05 — "Gyms in 2050" (QJLHIiro-Fk) — per-second teardown
Analyst 3. Evidence: all 15 intro 4 fps sheets (0–60 s), 1 fps sheets 006–048 (54–441 s), full-res frames (47.5, 127.5, 159, 265, 430.5, 435 s), per-frame difference series, 1-s zoom fits, transition-event list, faster-whisper word timings + per-utterance pitch (f0) estimate, 4-s RMS envelope, per-act grade stats, 400 comments. Extracts in `v05_QJLHIiro-Fk\data\extra\analyst3\`.

## 1. Card
| field | value |
|---|---|
| Title | Gyms in 2050 (3 words: everyday place + future year) |
| Upload | 2023-05-07 · 1080p25 · 440.81 s (7:21) |
| Views / likes / comments | 3,408,916 / 114,641 / 2,700 → like/view **3.36 %**, comments/view 0.08 % |
| Description | 3-sentence premise ("both positive and negative sides… AI coaches and VR… mandatory… forced by the gov") + crypto donation block; generic tag block |
| Voice | Voiced, ≥6 TTS-like voices; 816 words detected in 244.6 s of speech = **55 % of runtime voiced**, **200 WPM in-speech** |
| Cuts/min | scdet≥8: **11.57** (85 cuts), median shot 3.68 s, max 31.2 s (scdet misses whip-reframes). Frame-diff events: **128 = 17.4/min**, median 2.92 s: 76 hard 1-frame cuts (59 %), 4 short, 44 soft (mostly 8–14-frame motion-blurred reframes), 4 long (≥30 fr) |
| Loudness | **−21.4 LUFS integrated** (7.4 dB under YouTube reference), LRA 12.3 LU; 13 pauses ≥0.35 s (12.6 s total); opening silence 0–2.73 s |
| Motion | 1-s windows: 42.9 % fully static, 19.7 % zoom-in, 3.5 % zoom-out, 5.7 % pan, 28.3 % local/compound. 54.8 % of frames pixel-identical to the previous |
| Grade | mean luma 31.8, warmth −3.7 (coolest-but-one in corpus); steroid act warms to +2.2 |

**Thumbnail.** Giant outlined "2050" (black fill, thin light stroke) top-centre, ≈55 % frame width, partly hidden behind the characters. Left: a red-haired woman, more polished drawing than in the video (blush, freckles, make-up, gritted teeth) doing a dumbbell row. Right: a cyan holographic muscle man with halftone dot texture and glow, flexing, smug. Navy, blurred gym background; dominant cyan/navy. The protagonist is **not** in the thumbnail; neither thumbnail character appears in that form in the video (packaging ≠ content).

**Heatmap top peaks → on screen**
| rank | window | value | on screen |
|---|---|---|---|
| 1 | 2:47.6–2:52.0 | 1.00 | Monitor shows a video-site watch page "Gyms in 2023": real live-action gym footage + sidebar of thumbnails incl. the channel's own videos, dated "X years ago" — pause-and-read detail (comments 2:51 "level of detail", 2:57 thumbnail joke, 2:52 "25 years ago… feel weird") |
| 2 | 0:00–0:04.4 | 0.98 | start (normal) |
| 3 | 6:32.5–6:36.9 | 0.79 | Cut-away gag: gigantic red-haired bodybuilder on a bench — "the illegal juice" guy |
| 4 | 2:56.4–3:00.8 | 0.71 | same watch page, push-in on real crowd-and-lift footage |
| 5 | 7:03.4–7:07.8 | 0.46 | final reaction push-in after the punchline (2023 peak physiques "quite average now") |
| 6 | 2:38.8–2:43.2 | 0.38 | Community-gym neon exterior + gym website |
Least replayed (likely skip) zones: **1:14–1:32 (0.00–0.03)** = wordless walk through elevator and corridor; **4:51–5:13 (0.01–0.06)** = VR-treadmill group shot held 17 s.

## 2. Premise, turn, arc
**Premise:** in 2050 the state makes monthly gym sessions mandatory for health insurance; an unfit everyman does his supervised session in a caged solo cell, then switches to a private "community" gym — which still reports to the state — and learns steroids are now legal.

**Turn:** 3:03.1 "You know what? It's time I make something of my life." (after watching 2023 gym videos, 2:47–3:00). Protagonist face goes neutral → frown → angry scrunch with push-in (3:03–3:12).

**Arc**
1. 0:00–0:42 **Summons** — phone message from a state bot: fail = lose insurance; annoyed compliance ("Dammit, it's that time of the month again").
2. 0:43–1:06 **Bureaucratic check-in** — grey faceless receptionist, citizen ID, "You will be monitored"; "Good luck".
3. 1:07–1:51 **Isolation reveal** — elevator, corridor of numbered doors, cell 431 with red "59:00" timer, pull-back reveals a grid of identical cells each with one exerciser.
4. 1:52–2:26 **Surveillance coaching** — hologram trainer nags about a 2-minute rest.
5. 2:27–3:12 **Envy & decision** — commute, community-gym neon, nostalgia for 2023 → TURN.
6. 3:20–4:20 **Hopeful sign-up with a sting** — $100/month, "We aren't the government"… "We do however have to share our data with the government".
7. 4:30–5:42 **Belonging** — friendly blond mentor, VR treadmills (moon/Mars), hologram plates appear on the bar → first open-mouth smile (5:33).
8. 5:43–7:06 **Lore & punchline** — legal vs illegal steroids, cut-away giant, "2023 peak physique is average now" → side-eye reaction, black, end card.

## 3. Beat sheet / visual script
BG codes: CG = 3D render / game capture / AI still (not separable at 1080p), P = photo, V = real moving footage, U = UI mock, F = flat. Voices: GB = state bot, NPC = receptionist, P = protagonist, AI = hologram trainer, T = reception trainer, B = blond mentor.

**0–20 s second by second**
| s | picture | scale / motion | BG | text | audio |
|---|---|---|---|---|---|
| 0 | fade-in from black (~1 s) onto protagonist in gaming chair holding a controller, neon sci-fi capsule bedroom (purple/red, cyan light tube) | WS, push-in ≈1.2 %/s | CG | — | silence 0–2.73 s |
| 1–2 | same, push continues | WS | CG | — | ambience starts −28 dBFS |
| 3–5 | cut 2.92: huge white back of head fills right half (OTS); CRT TV shows a real retro platform-game title screen | OTS static | CG + game screenshot | game title | |
| 6 | cut 5.80: protagonist turns; phone appears in hand at 6.75 | MS | CG | — | |
| 7 | cut 7.32: POV drawn hand holding photoreal black phone; status bar 11:23 AM, profile "…Kowalski ✓", Citizen ID, "Credit: 639/1000", "1 new message: From governbot", drawn blonde avatar | POV, phone drift | U over blurred magenta CG | profile UI | GB "Good morning." at 7.15 |
| 8–12 | message types on word-by-word in sync with the voice | push 1.6 %/s | U | typewriter body text | GB ≈150–200 WPM, f0 ≈142 Hz |
| 13 | cut 12.96: CU protagonist face, grey tee | CU static | CG | — | GB continues |
| 14 | 14.48 single-frame swap neutral → tired (eye bags) | CU | | | |
| 15 | hold | | | | |
| 16–19 | cut 16.08: phone again, larger | POV push 1.4 %/s | U | text continues | GB "If you don't meet this requirement…" |
| 20 | phone hold | | | | GB "…lose your right to a health insurance" |

**20 s – end, per beat**
| time | beat | who / scale | BG | motion / transition | on-screen text | audio |
|---|---|---|---|---|---|---|
| 0:22.0–0:25.1 | CU face, brows furrow (0:23.5 swap) | P CU | CG | static | — | GB |
| 0:25.1–0:30.6 | phone, tighter (push 2.2 %/s); message completes | POV | U | push | free gov gym vs paid community gym | GB |
| 0:30.6–0:36.8 | MS seated with phone; tired → annoyed swap 0:33.75 | P MS | CG | 6-frame soft event 0:31.4 | — | P "Dammit, it's that time of the month again…" 247 WPM, f0 98 Hz |
| 0:36.8–0:42.4 | booking UI: slots 8/9/10 pm, District 67, finger taps 0:38.75, "Appointment made! ✓" + fine print (fail = −5 social credit) | POV | U | tap | booking UI | — |
| 0:42.4–0:46.3 | phone slides out; MS in dark-blue lobby; fast motion-blur whip 0:43.7 to WS: neon "GOVERNMENTAL GYM" | P MS→WS | CG | slide + whip | neon sign; wall neon "YOU WILL OWN NOTHING AND YOU WILL BE HAPPY" | P "Hello. I have a gym appointment for 8pm." |
| 0:46.3–1:06.0 | check-in shot/reverse-shot: OTS on grey faceless receptionist (dot eyes, L-nose) ↔ WS reaction ↔ CU NPC; whips at 0:54.4, 0:58.6 | NPC CU/OTS, P WS | CG | hard cuts + 6-frame whips; static holds | **subtitles only for NPC lines**: "Room number & Citizen-ID please." … "Good luck." | NPC voice f0 ≈80 Hz with octave jumps (IQR 104–120 Hz) = robotic processing; 168–221 WPM |
| 1:06.0–1:11.6 | walks off; elevator with 4 drawn gym-goers, push-in | WS | CG | 24-frame soft event 1:07 | — | music only |
| 1:11.6–1:18.0 | CU in elevator, crowd behind blurred (DOF on drawn characters) | P CU | CG | static | — | |
| 1:18.0–1:28.0 | doors open into grey corridor; endless numbered doors 400–407; profile looking | WS/MS | CG | push 4.2 %/s at 1:21–1:24 | door numbers | heatmap ≈0.00 |
| 1:28.0–1:35.0 | door "431"; stands in doorway | MS | CG | hard cuts | "431" | |
| 1:36.0–1:44.0 | cell: grey walls, dumbbells, bench, red LED "59:00" (never changes), screen-window with forest; reverse angle; centre of room | WS | CG | hard cuts | "59:00" | music −18 dBFS |
| 1:45.5–1:51.0 | **pull-back reveal**: grid of ≥16 identical cells, one drawn person in each | WS→EWS | CG duplicated | 94-frame zoom-out (3.8 s) | — | music swell |
| 1:52.0–2:02.0 | ~1 s crossfade; back squat in blurred grey gym; CU deadpan; sits with phone | P MS/CU | CG | dissolves 1:52, 1:56 | — | near-silence −39 dBFS (1:52–2:03) |
| 2:03.0–2:06.4 | magenta/teal light leak; hologram trainer materialises: pink-magenta glow, glasses, moustache, tank top, scan-line glitch, pink→blue gradient | AI MS | CG | glow/glitch overlay | — | sci-fi tone [inferred] |
| 2:06.4–2:26.5 | AI nags; alternating CU AI / CU P (annoyed squint swap 2:11) / MS P standing with hologram behind / squats | AI, P | CG | hard cuts every 1.6–3.0 s | **subtitles for AI lines**: "Hello there!" "I am Arnold," "your personal trainer." … "I'm here to help you become fit!" | AI voice f0 139–151 Hz, 145–268 WPM |
| 2:26.5–2:38.5 | dissolve; subway at night (CU tired); view through train window of P + grey faceless commuters; back of P at window, outside a blue-neon "COMMUNITY GYM" with drawn crowd | P CU/WS | CG | 29-frame dissolve 2:26.5 | sign | music |
| 2:38.5–2:47.0 | building exterior (game-like night city, neon sign + flexing-man logo, glow); sci-fi monitor with gym website; WS at laptop | WS | CG + U | 68-frame push 2:38.4 | "WELCOME TO THE COMMUNITY GYM! THE #1 GYM OF DISTRICT 64, EST 2043 / JOIN TODAY / WEIGHTLIFTING / VR BOXING / GALAXY RUNNING" | heatmap 0.38 |
| 2:47.0–3:02.9 | watch page "Gyms in 2023" playing **real gym footage**; sidebar = channel's own thumbnails + other creators'; push to full-screen footage | U + V | V | push 0.8 %/s, footage moves | page UI | P "People used to be so much fitter…" 2:54 (277 WPM); **heatmap peak 1.0** |
| 3:02.9–3:12.4 | CU P neutral → frown (3:05) → angry scrunch (3:06–3:12) with push-in | P CU | CG | push 1.6 %/s | — | P: the TURN line 3:03; silence 3:12.4–3:14.7 |
| 3:13–3:20 | empty bedroom; back of P before gym at night, wet street; CU angry with skyline | WS/CU | CG | 12-frame soft events | — | |
| 3:20.0–4:20.0 | reception: wooden desk with neon underglow, desaturated near-B/W photo set with coloured neon only; trainer (brown mohawk, square jaw, tan skin, blue shirt + tie, "TRAINER" badge) | T CU long holds (3:29–3:47 frozen 18 s), P CU (smile from 4:10), two-shots | P (desat) + neon | **reframe swishes 8–14 frames with motion blur** (3:28.9, 3:36, 3:48.2, 3:50.3, 4:09, 4:13, 4:18): the camera slides/zooms between CU and two-shot of the same composite | badge | T f0 107–130 Hz, P ≈96–101 Hz; $100/month line; data-sharing sting 4:01–4:08 |
| 4:20.0–4:30.0 | exterior again (time skip) → purple-neon gym interior: treadmills, dome window, posters, small drawn gym-goers pasted | P MS | CG (AI/3D look) | static | "COMMUNITY GYM" wall text | −43 dBFS gap 4:20 |
| 4:30.0–5:01.9 | blond mentor (spiky blond hair, grey tee): two-shot ↔ CU blond (8-s hold 4:41–4:48) ↔ angry CU P; reframe swishes 4:36, 4:40, 4:58, 4:59 | B, P | CG | swishes 8 fr | — | B f0 ≈96–103 Hz; "put in a cage…" |
| 5:02–5:19 | VR treadmills: grey faceless runner in headset, wall screens with rainbow-road and meadow | WS group, 17 s near-static | CG | none | — | heatmap 0.01–0.06 (skip zone) |
| 5:19–5:40 | cable rack; "Where are the plates?"; hologram weight selector 22/44/66/88 LBS, finger picks 44 (turns green); blue holographic plates materialise; P open-mouth smile; squat with strain | P, B | CG + glow FX | 17–50-frame FX events 5:23, 5:35–5:39 | "22 / 44 / 66 / 88 LBS" | metal-plate SFX (comment 81 likes) |
| 5:40–6:32 | locker room: lockers with graffiti, crypto sticker, plants; B on bench; steroid lore in alternating CU B (3–6 s) / two-shot / CU P; swishes 6:00, 6:03.8, 6:27 | B, P | CG/P | swishes 9–10 fr; push 1 %/s | graffiti "WE'RE ALL GONNA MAKE IT BRAH!" | B 165–202 WPM, 23 s of exposition 6:04–6:27 |
| 6:32.1–6:35.9 | cut-away: enormous muscular man, glasses, red hair, on bench against brick wall | WS | CG | hard cut | — | **heatmap 0.79** |
| 6:36–7:00 | dialogue continues; alternating CU | B, P | CG | swishes 6:37, 6:42, 6:45, 6:50, 6:55 | — | |
| 6:59.7–7:09.3 | CU P final reaction (side-eye, slight frown), slow push 2.0–2.2 %/s | P CU | CG | push | — | B punchline ends 7:06 |
| 7:09.3–7:13.4 | black (watermark still visible at 60 % white) | — | F | — | — | silence 7:09.4–7:11.7 |
| 7:13.4–7:20.8 | end card orange, socials, end-screen placeholders, fade | — | F | — | handles | −17 dBFS music |

Background share: CG stills ≈ **74 %** (≈325 s), desaturated photo set ≈ 13.6 % (3:20–4:20), UI ≈ 6.4 % (28 s), real moving footage 3.6 % (16 s), black + end card 2.7 % (12 s).

## 4. Script / communication mechanics
- **Dialogue-led satire.** 816 words; 6 speaking roles. State voices (bot, receptionist, hologram) are subtitled; human voices are not — the subtitle itself marks "machine/state". 
- **World-building by artefact:** credit score in the phone header, fine print ("lose 5 social credit points"), room 431 of 400+, frozen "59:00" timer, cell grid, district numbers, gym "EST 2043", 2023 video dated "X years ago". Comments reward pausing (2:51 "level of detail", 2:57 thumbnail).
- **Contrast structure:** public gym (cold blue, solo cage, AI nag, silence) vs community gym (purple neon, people, music) — then a sting reveals both report to the state (4:01).
- **Gag devices:** "Good luck" for a gym appointment (comment 4.3K likes); "Where are the plates?" → hologram plates; cut-away to the giant on "that guy over there" (6:32); the closing reversal that today's peak physique is average in 2050 (meta joke on the viewer's present).
- **Withheld:** the protagonist's name/backstory; whether he actually gets fit. Ending = reaction shot, no resolution.
- **Repetition:** "governmental public gyms are horrible" said by P (3:10) and echoed by B (4:40); "good luck" said twice (1:05 NPC, 4:15 T).
- **Weak spot in writing:** 23 s of steroid policy exposition (6:04–6:27) delivered as a static two-hander (one comment criticises it).

## 5. Visual grammar
- **Shot rhythm:** dialogue scenes = shot/reverse-shot built from ONE layered composite: the "camera" reframes between CU and two-shot in 8–14 frames with directional motion blur (37 such swishes) — cheap coverage without new drawings. Monologue holds are frozen frames (3:29–3:47: 18 s with zero pixel change; no lip-sync, no blinking).
- **Camera:** push-ins in 19.7 % of 1-s windows at 1.0–2.6 %/s (median 1.6 %/s), eased; one 3.8-s pull-back reveal (1:45.5); one 2.7-s push into a building (2:38).
- **Animation:** 1-frame expression swaps (e.g. 0:14.48, 2:11.1); drawn hand taps on UI; hologram materialisation with glow; plates appear with glow. No limb cycles except squats.
- **Transitions:** 59 % hard cuts; motion-blur swishes in dialogue; 3 cross-dissolves (1:52, 1:56, 2:26.5) for time passing; slide-out of phone (0:42.5).
- **Compositing:** drawn characters on CG stills; DOF blur applied to drawn background characters (elevator 1:12–1:18); no cast shadows; scene colour cast pushed onto characters (blue lobby: the protagonist's shirt reads #374552, the NPC's #3A4855, under the same blue light); hologram = additive pink/blue glow + scan lines.
- **Grade by act (measured):** gov gym luma 25 / warmth −5.6; hologram cell luma 38 / sat 19 (sterile); community-gym tour sat 41 / warmth −14 (purple neon); locker talk luma 44 / warmth +2.2 (the warmest, human act).
- **Typography:** subtitles = humanist sans, white with ≈3 px black stroke, centred, text block x 446–1472 px, lower edge ≈90 % of height. Neon signs = blue glow serif/sans. Phone UI = clean sans. No title cards.
- **Watermark:** YT icon + "Low Budget Stories", Comic Sans-style, white at 60 % opacity (measured 153/255 on black at 7:10.5), bbox x 31–619 px, y 996–1052 px (1.6–32.2 % W, 92.2–97.4 % H), present on every frame incl. black; absent on end card.

## 6. Audio grammar
- **Voices (pitch-estimated, faster-whisper timing):** GB f0 ≈136–150 Hz; NPC ≈80 Hz with octave-error jumps (robot/vocoder effect); AI hologram ≈139–151 Hz; P ≈94–101 Hz, pitch IQR only 8–12 Hz (monotone); T ≈107–130 Hz; B ≈96–106 Hz. In-speech rate 200 WPM (P peaks 277–292 WPM). Monotone pitch + uniform pace + comment "voice bot could be upgraded to the ElevenLabs level" → synthetic TTS voices [inferred, medium-high].
- **Music:** low under dialogue (RMS −24…−27 dBFS); swells on wordless reveals (1:36–1:40 −18 dBFS); near-silence in the cell workout (1:52–2:03, −39 dBFS); a hardstyle-type gym anthem in the community gym (comments name a meme gym-music genre) [inferred, low]; end card −17 dBFS.
- **SFX:** metal plates clanking on hologram plates (4:24/5:35 comments), console sounds (5:28 comment), UI taps [comment-evidenced].
- **Silence:** 0–2.73 (cold open), 3:12.4–3:14.7 (after the decision), 7:09.4–7:11.7 (before the end card).
- **Mix:** −21.4 LUFS — YouTube will not raise it; the video plays ~7 dB quieter than v04.

## 7. Retention devices & why viewers stayed / replayed / commented
| device | where | evidence |
|---|---|---|
| Cold open on a phone summons with stakes (insurance) | 0:07–0:31 | heatmap 0.25–0.36 in first 15 s |
| Absurd-bureaucracy deadpan | 0:46–1:06 | "Imagine being told 'good luck' for a gym appointment" 4.3K |
| Dystopian image reveal | 1:45 cell grid | comments on cages/privacy (70, 51) |
| Pause-to-read easter eggs in a UI of the future | 2:47–3:00 | heatmap #1 1.0 + 6 timestamped comments |
| Gadget wish-fulfilment (VR treadmill on Mars, hologram plates) | 5:02–5:40 | 3.3K, 981, 290 likes |
| Plausible-future debate | whole | "doesn't seem that far off" 3.3K; mandatory fitness "great idea" 1.1K/241 |
| Cut-away visual punchline | 6:32 | heatmap 0.79 |
| Price joke | 3:33 | "$100 a month in 2050? That's like $10 today" 12K (top comment) |
| Hope inside dystopia | 4:30–5:40 | "pockets of positivity and hope" 12K |
Creator comment: the video "turned out to be an insane lot of work" and came 3 weeks after the previous upload (893 likes).

## 8. Weaknesses / risks
- 18-s wordless corridor walk (1:14–1:32) and 17-s static VR group shot (5:02–5:19) are replay dead zones (heatmap ≤0.03).
- Frozen monologue holds of 8–18 s with no mouth or body motion.
- Exposition dump on steroid regulation (6:04–6:27); medically sensitive topic (drug normalisation) — risky for advertisers and minors.
- Mix too quiet (−21.4 LUFS); voices TTS-flat.
- IP: hologram named after and styled like a famous bodybuilder-actor; reception/mentor characters and gym logo reference a deceased fitness influencer meme; real brand parodies (sportswear logo, video-site UI with real creators' thumbnails), a real platform game title screen, real gym footage. None transferable.
- Thumbnail characters are not in the video.

## Why it works
1. A universal, low-stakes place (the gym) + one future rule (mandatory fitness for insurance) creates an instantly graspable dystopia with endless gag surface.
2. Two-world contrast (cold state gym vs warm community gym) with a sting that the "free" option is still surveilled — satire with a twist, not a lecture.
3. Dense pausable artefacts (credit score, room 431 of hundreds, dated video page) turn viewers into detectives; the replay peak sits on the most detailed frame.
4. Cheap coverage: one composite per scene, reframed by motion-blurred camera swishes, gives dialogue scenes cut-rhythm without new art.
5. Hope pocket (friendly mentor, VR on Mars) keeps a 7-min dystopia from becoming bleak.

## Rules to copy
1. [KOPYA] Premise formula: everyday place + year 2050 + exactly one new law/technology; state the rule in the first 25 s through a phone notification from a state bot (typewriter text synced word-by-word to the voice).
2. [KOPYA] Build each dialogue scene from one layered composite (BG still + 2 cut-out characters); create coverage by reframing between CU and two-shot in 8–14 frames with directional motion blur; ≥1 reframe per 6 s of dialogue.
3. [KOPYA] Subtitle only machine/state voices (white humanist sans, 3 px black stroke, centred, bottom edge at 88–91 % of height); leave human voices un-subtitled.
4. [KOPYA] Give every institutional voice a processed robotic timbre and every faceless official a grey head (#979996–#A3A3A3), dot eyes, L-nose, flat mouth — an original faceless design that fills the NPC role.
5. [KOPYA] Place one wordless dystopian "reveal" shot at 20–25 % of runtime: a 3–4-s eased pull-back from the protagonist's space to ≥16 identical duplicated spaces.
6. [KOPYA] Seed ≥5 pause-readable artefacts (scores, IDs, numbers, dates, fake UI) and put the densest one at 35–40 % of runtime.
7. [KOPYA] Contrast acts with grade: institutional act luma 22–28 / warmth ≤ −5; "human" act luma ≥40 / warmth ≥0.
8. [KOPYA] End on a reversal line about the viewer's present, then a 7–10-s slow push (2 %/s) on the protagonist's silent reaction, 2–4 s black, end card.
9. [İYİLEŞTİRME] No wordless walk or static group shot longer than 6 s without a gag, cut or new information (corpus skip zones at 18 s and 17 s).
10. [İYİLEŞTİRME] No frozen hold over 6 s while a character speaks: add a 1-frame expression/eye swap every 2–3 s or a 1 %/s push.
11. [İYİLEŞTİRME] Cap exposition at 3 consecutive lines (≈12 s) before a visual gag or cut-away.
12. [İYİLEŞTİRME] Mix dialogue to −14 LUFS integrated, music bed 12–18 dB under voice; use expressive TTS with per-role pitch separation ≥15 Hz.
13. [İYİLEŞTİRME] Thumbnail characters must appear in the video in the same design.
14. [ETİK] Never name or design a character after a real athlete, actor or influencer; invent the gym brand, logos, video site UI and thumbnails; use own-shot or licensed footage for screens-within-screens.

## Open questions
- Whether the CG stills are rendered 3D scenes, game captures or 2023 AI images (exterior at 2:39 resembles a game night-city render with an added neon logo) — not separable at 1080p.
- Exact music tracks and SFX list need listening; the RMS map only shows where music swells.
- Voice-count: B and P overlap in pitch (≈96–103 Hz); diarisation would confirm whether they are distinct voices or one TTS voice with different settings.
