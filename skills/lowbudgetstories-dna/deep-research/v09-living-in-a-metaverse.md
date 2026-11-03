# v09: "Living in a Metaverse" (lng9u26JAvk): per-second teardown

Analyst 5. Evidence: every 1 fps sheet (000–039), every 4 fps intro sheet (000–014), single frames s0161/s0165/s0230/s0296 and others, scdet/cuts/metrics/silences, RMS and band-energy analysis of `audio16k.wav` (5 s bins), faster-whisper word timestamps, heatmap, and 400 comments (all top-level; no replies were captured).
Character names (Wojak, Chad, Zoomer, NPC, "tradgirl") describe the channel's meme cast **for analysis only**. Every rule below means "an original character that fills this role".

---

## 1. Card

| Field | Value |
|---|---|
| Title | Living in a Metaverse |
| Views / likes / like% | 2,662,620 / 146,139 / **5.49 %**. This is the highest like rate in the top-10 (corpus range 2.69–5.49 %). |
| Comments | 7,200, which is **2.7 per 1,000 views**. This is the highest rate in the top-10 (range 0.8–2.7). |
| Upload | 2021-11-24. That is 27 days after Facebook renamed itself Meta (2021-10-28), so the video rides a news peg. It was the channel's first ≥2 M video, 2.0× the previous record (1.36 M). |
| Duration | 359.3 s: 345 s of story, then 4 s black, then a 7 s end card. |
| Format family | Tech-dystopia ("Living in a …"). It is voiced and dialogue-driven. |
| Thumbnail (1280×720) | No text. A split-face protagonist sits centred (head ≈35 % of frame width, full height, split line at x≈51 %). The **left half** is warm-lit and smiling (skin #E7E3C0) over colourful official Meta/Horizon avatar promo art (avg #B78883), with a blue Meta ∞ logo bottom-left (≈20 % of width). The **right half** is grey, stubbled, frowning and has an eye bag (#B2AFB2) over a rainy night street photo (#16181F). The comparison it sets up: virtual joy vs offline misery. |
| Description | Opens with the Meta announcement and frames the video as "a real Doomer scenario". It **spoils the plot** (he swaps the girl for an NPC) and adds a creator note saying this is a "serious video for once" (the same text is the pinned comment, 8.7 K likes). Then crypto donation addresses, credits for 3 tracks ("Milk Coffee" jazz loop; "Broken Piano" by Vivek Abhishek; "Mysterious" by Radomir Kirovich), and socials. Tags (8): wojak, doomer, zoomer, boomer, chad, meme, crypto, cryptomeme. Category: Comedy, age_limit 0. |
| Cuts | @score≥8: **70 cuts = 11.69/min**, median shot **3.8 s**, mean 5.06 s, max 36.8 s. scdet undercounts here because shot/reverse-shot pairs share colour palettes. |
| Cut rate by section | 0–66 s: 18.2/min · 66–89: 5.2 · **89–126 (warehouse): 1.6** · 126–294: 10–15 · 294–303 (reveal): 20.0 · 345–359: 0 |
| Loudness | **−18.1 LUFS**, LRA 12.5 LU. Pauses ≥0.35 s: **4 (6.2 s total)**: 0–1.81, 126.38–126.73, **170.07–174.10** (the Deny beat). The music bed is essentially continuous. |
| Speech | 714 words in 72 lines (9.9 words/line). 119 wpm over the full runtime; **185 wpm inside speech**. Wordless gaps >3 s: 65–88 (23 s, real-world reveal), 124–137 (13 s), 169–177 (8 s), 308–315 (7 s), 319–323. |

**Heatmap.** The replay curve is nearly flat (0.01–0.09 for 70 % of the runtime) with one dominant spike.

| # | Bin (s) | Value | On screen |
|---|---|---|---|
| 1 | **295.2–298.8 (4:55)** | **1.00** | **Reveal.** A still of the real person behind the blonde avatar: an obese, hairy, shirtless grey man in a cheap VR headset with wires, a laptop showing the bar scene. The voice switches to a deep male voice mid-sentence at 294.3. The curve climbs 0.25 → 0.58 → 0.84 → 1.00 from 280 to 295 s. |
| – | 0.0–3.6 | 0.18 | Start bin (re-watch/seek artefact) |
| 2 | 64.8–68.4 (1:05) | 0.12 | First reveal: the avatar pixelates ("STUPID WIFI!", 62.3 s), a Meta ∞ boot screen, then a top-down headset on the stubbled face in a squalid bed |
| 3 | 262.8–266.4 (4:23) | 0.08 | Wage-cage monologue (rent and food eat the pay; asks what he is living for), with the SquidMan54 avatar hovering at his shoulder |
| 4 | 36.0–39.6 (0:36) | 0.07 | Price gag: two vodkas cost **0.005 Ethereum** |
| 5 | 129.6–133.2 (2:10) / 169.2–172.8 (2:50) / 342–345.6 (5:43) | 0.06 | Meme avatars walk in with floating usernames / Deny click → "FRIENDS (0)" / avatar crowd and the cut-off ending |

---

## 2. Premise, turn, arc

**Premise.** A wage worker spends his nights as a suave avatar in a crypto metaverse bar. When a girl there questions his escapism, he blocks her and spawns an obedient NPC instead.

**The turn: 4:54–5:15 (294–315 s).** At 294 s the girl is revealed to be a man. He types `/Block` at 303–305 s. At 315 s he types `/Spawn female_blonde_NPC#126`, which completes the flip. The thematic turn is earlier, at 3:31–3:47 (211–233 s), where he says the offline world "sucks" and that it is not the real world. That line drew the most-liked viewer comment (17 K) but only 0.03 replay.

**Emotional arc (valence −3 to +3):**

| # | Time | Label | Valence |
|---|---|---|---|
| 1 | 0:00–0:59 | Meet-cute in a neon bar, flirting, friend added | +2 |
| 2 | 1:00–1:07 | Glitch: avatar pixelates, Meta shutdown | 0 (comic deflation) |
| 3 | 1:08–2:05 | Real life: shirtless in a dirty bed, then a warehouse job; dodges a kind colleague's real-life friendship | −2 |
| 4 | 2:06–2:41 | "Later that night…", back in the bar with meme avatars and NFT glasses | +1 |
| 5 | 2:42–2:56 | Denies the colleague's request → "FRIENDS (0)" in silence | −2 (sad gag) |
| 6 | 2:56–4:47 | Reality-vs-offline debate; wage-cage confession at 4:18–4:26 | −1 → −2 |
| 7 | 4:54–5:08 | Catfish reveal, then cold `/block` | shock-laugh, then −2 |
| 8 | 5:15–5:50 | Spawns a compliant NPC; crowd of avatars; cut mid-word; 4 s black | −3 (ironic "happy ending") |

**Measurements:** 11 valence shifts in a 345 s story = **1.9 emotional beats/min**. **No catharsis**: the last positive moment is hollow (an NPC with "kindness, humor" switched on). Hope is placed nowhere. The ending is a tragic-irony freeze.

---

## 3. Beat sheet / visual script

**Shot setups.** Seven background plates carry 90 % of the runtime:
- (A) bar wide: pink-red brick, bottle shelves, purple neon counter, Chad bartender
- (B) protagonist MS on a black void (#000100) with purple-teal counter (#6E4A97) and a wine glass foreground right
- (C) girl MS on dark teal brick (#1C2C33)
- (D) 2-shot MCU on teal brick
- (E) over-the-shoulder (OTS) toward the girl against the pink bar (#4A1737)
- (F) warehouse: photo factory (#A3ACB1) plus illustrated conveyor
- (G) real-world photo rooms (#60636F bedroom, #2D373E reveal room)

**Composition rules seen throughout:**
- Characters are flat 2D cut-outs with thick black outlines, composited on 3D-rendered or photo plates. Plates look like stock or 3D-kit renders [inferred, med].
- Animation is limited to mouth-swaps, opacity fades, 5–10 % scale-pops on shot entry (e.g. 10.50 → 11.00 s), slow push-ins, and sliding walk-ins.
- Watermark is present in every non-black frame: YouTube icon plus "Low Budget Stories" in a rounded handwriting font, white ≈70 % opacity, bottom-left (x 2–32 %, y≈94 %, cap height ≈4 % of frame).

### 0–20 s at 4 fps

| t (s) | Picture | Camera / motion | Text | Audio |
|---|---|---|---|---|
| 0.00–2.25 | Night city skyline (3D), starry purple-blue sky, red neon **"SKY BAR"** sign, red round crypto-world logo on a rooftop | WS, slow downward drift/scale ≈5 % | "SKY BAR" (diegetic neon) | digital silence 0–1.81, then the jazz loop starts |
| 2.25–2.75 | Cross-dissolve, 0.5 s | – | – | jazz |
| 2.75–5.60 | Plate A: bartender (yellow pointed hair, tux, bow tie) on the left; protagonist's back on a stool, centre | WS, static | – | jazz, no dialogue |
| 5.64–10.50 | Plate B: protagonist frontal in black shirt, faint smile, alone | MS, micro drift | – | jazz (5 s of silent character intro) |
| 10.52–12.50 | Plate C: blonde girl, rosy cheeks, black catsuit with gold piping | MS, scale-pop 10.50→11.00 | – | "Hi." at 12.9 |
| 12.56–13.90 | B | MS | – | "Hi." |
| 13.92–14.80 | C | MS | – | girl: small talk |
| 14.84–16.10 | B | MS | – | reply |
| 16.16–17.90 | C, re-enters with a scale-pop at 16.25 | MS | – | girl |
| 17.96–20.00 | B | MS | – | "…chilling … in this building" |

The hook works with **no title card and no narration**. It is a mood plate, then a lonely character held 5 s, then a girl, then cutting every 1.0–2.0 s.

### 20–359 s by beat

| Time | Beat | Picture / framing | On-screen text (verbatim) | Audio |
|---|---|---|---|---|
| 0:21–0:27 | She "came from a party" and wants time away from friends | D, slow push-in | – | jazz under dialogue (−21 dB, <250 Hz share 0.5) |
| 0:27–0:34 | Drink offer | B alternate angle, then E | – | |
| 0:34–0:38 | **Crypto price gag**: two vodkas for 0.005 ETH; two shot glasses pop onto the counter at 34.25 | 3-shot OTS (bartender L, protagonist's back, girl R) | – | Heat 0.07 |
| 0:38–0:44 | "Where are you from?": Sydney / Brooklyn (accents swapped; comments 1.4 K + 759 likes) | D | – | |
| 0:44–0:56 | "Can I add you as a friend?" → "move this … to my place?" | OTS, then **protagonist CU** (tighter at 47.2 and 52.1 = hope beats), then C | – | |
| 0:57–1:02 | Glitch: girl fades, a white **loading spinner** sits over her | D, push-in at 1:02 | – | "goooooo…" is time-stretched (60.0 s) |
| 1:02–1:06 | Girl **pixelates** (mosaic) into the void; protagonist side-eyes | D → B | – | "NOT AGAIN! STUPID WIFI!" (62.3) |
| 1:06–1:07 | Protagonist dims to black; embossed dark-grey Meta ∞ logo | full black | – | Heat peak 2 |
| 1:08–1:14 | **Real world**: top-down ECU of a VR headset on a stubbled face, pull-out to a shirtless man in a lilac-sheet bed (photo); cigarette pack (comments read the brand as "Death accelerators", 754), keyboard, dirty plate | top-down, slow pull-out | – | quiet (−35 dB), low pad/piano [inferred, med: "Broken Piano"] |
| 1:15–1:21 | Takes off the headset; CU of the real face (purple eye bags, stubble, frown) held ≈6 s | CU, static | – | near-silent |
| 1:22–1:24 | **Costume dissolve**: a yellow hi-vis vest printed "Low Budget Stories" fades onto his body; background dissolves to a blurred factory | MS | vest logo (diegetic branding) | |
| 1:25–2:01 | **Warehouse**: Zoomer colleague (orange spiky hair, glasses), smiling, asks about a CoD update, says he sent a friend request, offers a beer; protagonist dead-eyed and evasive ("I was very busy") | plate F, 2-shot; smile-arrow cardboard boxes slide R→L every 3–4 s; slow pans 94–96 and 112–115 | – | dry dialogue, no bass music (<250 Hz share 0.10–0.17), −17 to −19 dB. **Lowest replay (0.01) of the video** |
| 2:02–2:06 | Guilt: protagonist CU, eyes averted downward | CU | – | |
| 2:06.4 | **Hard cut** back to plate A (largest scene-change score of the video, 43.6) | WS | "Later that night…" (white handwriting font, x≈5 %, y≈81 %, ≈3 % of frame height, 2:07–2:09) | 0.35 s silence, then jazz back |
| 2:08–2:12 | **Meme avatars walk in**, each with a floating grey condensed-bold username: SquidMan54 (red Squid-Game-guard suit), 2003_Justin7 (rainbow sunglasses, robot arm), a buff-dog meme, a blue man with a Rolex as a foreground wipe | WS with sliding entries | usernames | Heat 0.06 |
| 2:13–2:41 | Girl returns after a "boxing session" wearing **orange NFT glasses**; price 0.8 ETH; "you must have a lot of money" | B / D / E; buff dog blurred in the foreground (2:22–2:25); D00m3R_1995 avatar lurks (2:26–2:33) | – | |
| 2:38–2:41 | A floating hologram panel appears beside him (text mirrored = seen from behind) | B | mirrored panel | |
| **2:42–2:49** | **Friend-request insert**: the colleague asks to play or have a beer | full-screen glassmorphism panel (translucent grey, rounded), 8 s slow push-in | `NEW FRIEND REQUEST` / `@JIMMY_INU_69` / `Now playing Call Of Duty: Black Ops 8` / `Hi Wojak, I found your username via our manager. Up for a match of Call of Duty? Or a beer?` / buttons `Deny` (#DF001C) and `Accept` (#39F776), sans-serif | colleague's voice; **bass drops out** (<250 Hz share 0.00–0.08 at 160–170 s) |
| 2:50–2:53 | Hesitation; Deny gets a white outline (cursor-select) | B, then insert | – | |
| **2:53–2:56** | Punchline | insert | `FRIENDS (0)` / `No pending requests.` | **4.0 s silence** (170.07–174.10). Heat 0.06 |
| 2:56–3:31 | "Was that a friend?" "A colleague." She has a party "in real life"; he asks "in which lobby?" (3:24) → "offline world sucks" (3:31) | the 4 setups B/C/D/E cycle every 2–6 s; her glasses vanish (continuity slip); buff dog passes behind | – | jazz bed |
| **3:47–3:53** | **Thesis line**: the offline world is just where people were "forced to live" before the metaverse | B held **7 s**, static | – | Most-liked viewer comment (17 K); heat only 0.03 |
| 3:53–4:11 | Her counter-argument (breathe, eat, feel); his line about everyone having their own perception of reality | C, E, B CU at 4:01 | – | |
| 4:12–4:26 | **Confession**: the digital world is his real life; work eats his money (rent, food); what is he living for? | B, then **CU with SquidMan54 hovering at his shoulder** (background gag under the saddest line) | SquidMan54 nametag | Heat 0.08 |
| 4:26–4:36 | Pitch: choose your company, no laws, he can fly | B (SquidMan54 leaves at ≈4:30) | – | |
| 4:36–4:48 | "But isn't it lonely too?" Most people here are NPCs | D, 12 s slow push-in | – | |
| 4:48–4:53 | He snaps "Shut up…"; she apologises "I am just—" | CU, then E | – | |
| **4:54–4:57** | **Reveal**: obese, hairy man in a VR rig; laptop shows the bar scene | one held still, 4 s; dark photo room #2D373E | – | **Voice switches to deep male at 294.3, mid-sentence.** **Heat 1.00** |
| 4:58–5:02 | Protagonist unmoved; asked for a username, he gives it | B CU, C | – | |
| 5:02–5:08 | **Blocks her**: a floating command line types `/Block Faze_pro` (red slash command, grey argument, typewriter); in the OTS she opacity-fades out (≈1 s) during "Are you serious?"; empty stool at 5:08 | B, E | `/Block Faze_pr…` (on screen; the audio says "PhasePro32") | |
| 5:09–5:13 | Alone at the bar with the bartender; 2003_Justin7 slides in | A | – | |
| 5:14–5:22 | `/Spawn female_blonde_NPC#126` typed; a dark silhouette fades in; **NPC girl**: blonde hair on a grey NPC meme face, light-blue sweater, daisy skirt | B, then C | command text | [inferred, low] music change ("Mysterious") |
| 5:23–5:31 | `/disable movement, /activate kindness, humor` → the NPC chirps a greeting and gives her name | B, C | command text | upbeat female voice |
| 5:32–5:44 | He says he had a rough day and asks if she likes his muscles; she flatters him; **avatar crowd floods the foreground** (buff dog, SquidMan54, 2003_Justin7, D00m3R_1995 with a huge blurred nametag); her sentence is **cut mid-word at 5:44** | B, A wide (isolation), FG crowd push | nametags | Heat 0.06 |
| 5:45–5:50 | Fade to black; **4 s of black** | – | – | quiet |
| 5:51–5:58 | End card: orange **#ED720B**, doomer mascot (black hoodie, beanie) on the left ≈30 %, "LOW BUDGET STORIES" in black heavy rounded caps at top, IG/Twitter @LOWBUDGETSTORY, Reddit @LOWBUDGETSTORIES, two end-screen placeholder shapes (dark rectangle, light circle); fades in at 5:51, out at 5:57 | static | handles | quiet (−31 to −35 dB). **No spoken CTA.** |

---

## 4. Script / communication mechanics

1. **Two-world structure.** Virtual world: dark, neon, jazz, suave black suit. Real world: grey photos, no music, eye bags, shirtless. The switch is always a **technical failure or reveal**: Wi-Fi at 1:02, headset at 1:08, catfish at 4:54. Each switch is one of the three biggest replay peaks.
2. **Diegetic UI as dialogue.** The friend request, FRIENDS (0), `/Block`, `/Spawn`, and `/activate kindness, humor` deliver the plot as text. The two coldest acts (blocking a person, spawning a person) are **typed commands, not spoken lines**, so the protagonist never has to emote.
3. **Callbacks inside the video.** The colleague's offer (1:42–1:56, spoken at work) returns as a UI panel (2:42), and he refuses it twice. The "boxing session" claim (2:17) is paid off by the reveal body. "NPCs" (4:40) is paid off literally by the spawned NPC (5:21).
4. **Withholding.** The girl's real identity is withheld for 4:44 (0:10 → 4:54). The NPC's last sentence is withheld (cut mid-word). No resolution or moral is spoken: the audience has to say it in the comments.
5. **Background gags under serious lines.** SquidMan54 hovers behind the saddest confession (4:12–4:30); the buff dog walks by during the NFT talk. Comedy and despair are layered in the same frame instead of alternating.
6. **Specific-but-universal props:** crypto prices for drinks, NFT glasses, a CoD sequel number ("Black Ops 8"), usernames (`@JIMMY_INU_69` puns on a memecoin), legless avatars (a comment says they "aren't grounded"). ≈18 sight gags in 345 s = **3.1 gags/min**.
7. **Channel callbacks:** SquidMan54 calls back the channel's previous upload ("Doomer joins Squid Game", 12 days earlier); the Low Budget Stories vest; Ethereum jokes from the crypto era.
8. **On-the-nose thesis.** The debate (2:56–4:47, 111 s, 31 % of runtime) states the theme outright. Commenters praise it as "deep", but it is also the lowest-replay stretch (0.02–0.05).

---

## 5. Visual grammar

- **Rhythm:**
  - Intro shot/reverse-shot 1.0–2.5 s.
  - Dialogue scenes 2–6 s.
  - Thesis and confession shots held 7–12 s.
  - Warehouse: one 37 s setup (only box slides and slow pans move).
  - Reveal: one 4 s still.
  - Pre-reveal pattern: a **12 s slow push-in (4:36–4:48), then two ≈3 s shots (snap, half-apology), then the reveal frozen 4 s**.
- **Push-ins** mark emotional pressure: 21–27 s (flirt), 62 s (glitch), 162–169 (friend request), 204–215 (debate), 276–287 (the "lonely" question), 340–344 (crowd).
- **Transitions:** 0.5 s cross-dissolves for space changes; a costume dissolve (1:22) instead of showing travel; a hard cut for the return to fantasy (2:06.4); opacity fades for digital (dis)appearance (block, spawn); a mosaic pixelation for a connection drop.
- **Compositing:** 2D characters on 3D or photo plates with a depth-of-field foreground (blurred buff dog, blurred nametag) to fake depth. Characters never touch the set except by overlap.
- **Colour as emotion:**
  - Fantasy: saturated purple (#6E4A97) and teal-black on void black.
  - Reality: desaturated grey-blue photos (#60636F, #A3ACB1, #2D373E).
  - Warmth is never used, except in the thumbnail's "joy" half.
- **Recurring motif:** floating text above or beside people (usernames, panels, command lines). Identity reads as a label.
- **Title cards:** none. The only caption is "Later that night…", lower-left in a small handwriting font.

## 6. Audio grammar

- **Music:** a continuous jazz loop under every bar scene (bass-band share ≈0.5, −20 to −24 dB RMS). It is removed under the warehouse (dry voice plus ambience), under the friend-request insert, and for the 4 s Deny silence. A quiet low pad/piano plays in the real-world bedroom (−35 dB) [inferred, med]. The end card is quiet, unlike v10's loud outro.
- **SFX:** wifi-glitch tone stretch (60 s), UI hums, typing [inferred]. There is little SFX overall; the dialogue carries the video.
- **Voices:** human voice actors [inferred, med; comments hear an American female voice say "Sydney" and an Australian male voice say "Brooklyn"]. Delivery is flat and conversational. 185 wpm inside speech is fast. A **gender/voice switch carries the reveal** at 294.3 s.
- **Silence is used 3 times**: 0–1.8 (open), 126.4 (the cut back to the bar), and 170–174 (the Deny punchline). The 4 s silence before "FRIENDS (0)" is the only rest in a 185 wpm script.
- **Loudness map:** steady −20 to −24 dB in the bar; −17 to −19 at the warehouse (louder voices, no music); dips to −54 dB at 170–172; −30 to −35 for the ending.

## 7. Retention devices and why people stayed, replayed and commented

| Device | Timestamp | Evidence |
|---|---|---|
| Open loop: who is the girl? | 0:10 → 4:54 (284 s) | Replay curve rises steadily 280→295 s, peak 1.00; comments "every RuneScape player knew that was a man" (94) and "girl … could be a man who's fat" (56) |
| Fantasy/reality cut gag | 1:02–1:21 | Second-highest replay peak (0.12) |
| Sympathetic third party rejected | 1:25–2:56 | "felt bad when he rejected his coworker's request" (5.6 K), "the zoomer … seemed cool" (1.3 K) |
| Quotable thesis line held 7 s | 3:47 | **17 K-like comment** quotes it. Quote-back comments = 6 % of comments but **19 % of likes** |
| Wage-cage confession (catharsis by recognition) | 4:12–4:26 | Heat 0.08; comment on grinding 40 hours for subsistence while in the metaverse you can be a god (2.7 K) |
| Twist + cold power fantasy (block/spawn) | 4:54–5:31 | Heat peak; "the scariest part … trade interactions with real humans for … NPCs" (2.2 K) |
| News-peg dread | whole video | **Tech-dystopia fear = 53 % of like-weighted top-20 comments** ("scariest thing in existence", 19 K) |
| Genre break framed by the creator | pinned note | "serious video for once" (8.7 K); craft praise 12–24 % of comments ("A piece of art, certainly not low budget", 6.4 K; Black Mirror comparisons) |

**Comment profile.** The regex pass is multi-label, over 399 non-uploader comments; the manual pass codes the top 20.

| Theme | Count share | Like share (regex) | Top-20 manual like share |
|---|---|---|---|
| Fear / dystopia | 23 % | 52 % | **53 %** |
| Quote-back / detail-spot | 11 % | 16 % | 16 % |
| Craft praise | 24 % | 17 % | 12 % |
| Ideology | 6 % | 3 % | 8 % |
| Hurt | 4 % | 5 % | 5 % |
| Self-ID | 3 % | 1 % | 3 % |

Other signals:
- 23 of 400 comments mention gaming identity (VRChat, RuneScape).
- 1 explicit self-harm statement ("will not hesitate to commit suicide" if the metaverse takes over, 130 likes).
- Timestamped comments (19) cluster at 4:50–5:03 (4 of them: "4:55 got me lmfao", "@5:03 DAMN").

## 8. Weaknesses / risks (what would not transfer)

1. **Static middle.** From 97 s to 260 s the replay value is 0.01–0.06. The warehouse (37 s, 1 setup) and the debate (111 s) depend on the script alone, and the theme is stated rather than shown.
2. **Fat-reveal punchline.** The twist leans on body-shaming (obese, hairy, shirtless man = disgust). Comments repeat "fat and a pervert". This is not acceptable for us; it is also brand-unsafe.
3. **Trademark and IP load:** Meta logo and official Meta promo art in the thumbnail; Meta boot logo; a Squid-Game costume; a buff-dog meme; a Decentraland-like logo; Amazon-like box logo; a cigarette pack; "Call of Duty" by name; the channel's meme cast.
4. **News-peg dependency.** The upload rode the Meta rebrand window. Its sequels drew 0.35–1.46 M views (≈13–55 % of v09's 2.66 M).
5. **Fast in-speech pace** (185 wpm) with no subtitles burned in. Non-native viewers depend on YouTube captions [inferred].
6. **Continuity slips** (glasses vanish at 2:59; the typed username differs from the spoken one). They are tolerated, but each costs a comment of nit-picking.

## Why it works

The video **turns a news-cycle fear into a two-world fable** in which every switch between worlds is a visual reveal. It also adds a **sympathetic human to reject** (the colleague) and an **unfinished ending**. Viewers do the moralising themselves, which produced the corpus's highest like rate (5.49 %) and comment rate (2.7/1000). Replays go to the moments where the illusion breaks (1:05, 4:55). Likes go to the protagonist's most chilling sentence, held still for 7 s.

## Rules to copy

1. [KOPYA] Open with a 2–3 s mood plate (location + neon or diegetic sign), then hold the lone protagonist **≥5 s silent** before the first line. The first spoken line lands at **10–13 s**.
2. [KOPYA] Build a **two-world grammar**: fantasy = saturated purple/teal (#6E4A97 / #1C2C33) over continuous music; reality = desaturated photo plates (#60636F–#A3ACB1) with no music. Never mix the two palettes in one shot.
3. [KOPYA] Switch worlds only through a **technical failure or reveal** (pixelation, loading spinner, logo shutdown, voice swap). Plan **≥2 such switches**, at ≈18 % and ≈82 % of runtime.
4. [KOPYA] Place the main reveal at **80–84 % of runtime**. Approach it with a **10–12 s slow push-in**, then **two ≈3 s shots**, then hold the reveal still for **3–4 s**. Sync the reveal cut to a **mid-sentence voice change**.
5. [KOPYA] Give the protagonist **one thesis line of 15–25 words**, delivered flat and held on a static MS for **6–8 s** with no cutaway. It is the quote-comment magnet.
6. [KOPYA] Include a **kind third party whom the protagonist rejects** at 30–48 % of runtime (offer by voice first, then repeated as UI). Follow it with a **3–4 s total silence** and a one-line UI punchline ("FRIENDS (0)").
7. [KOPYA] Deliver the coldest acts as **typed diegetic commands** (red slash-command + grey argument, typewriter ≈0.5 s/word), not as acting.
8. [KOPYA] Layer **one background sight gag under the saddest line** (an avatar hovering, a passer-by), ≥1 per 60 s; target **≥3 sight gags/min** overall.
9. [KOPYA] End **without a moral**: cut the last line mid-word, then **3–4 s of black**, then a 6–8 s branded end card. No spoken CTA.
10. [KOPYA] Thumbnail: no text. A **split-face protagonist** (head ≈35 % of width, split at x≈50 %): warm-lit and smiling on the left over the fantasy world, grey with eye bags on the right over a dark rainy photo.
11. [İYİLEŞTİRME] Keep the middle moving. Every dialogue scene >30 s needs **≥1 new visual event per 8 s** (prop change, walk-in, UI pop, push-in), and no single setup may exceed **20 s**. v09's 37 s warehouse plate is the anti-pattern.
12. [İYİLEŞTİRME] Show the theme instead of debating it. Cap the explicit debate at **≤15 % of runtime** (v09: 31 %); move half of its lines into actions or UI.
13. [ETİK] The reveal must not punch at a body type, gender identity or disability. Reveal **circumstance** instead (e.g. the "girl" is a bot farm, a marketing script, or the protagonist's own boss).
14. [ETİK] No real logos in thumbnails or frames (Meta, Amazon, game franchises, cigarette brands). Use invented brands that parody a *category*, not a company. Avatars are **original designs**, never franchise costumes or existing meme animals.
15. [ETİK] Use an original character that fills the "everyman avatar", "seductive stranger", "kind colleague" and "compliant NPC" roles. Never reuse the channel's meme faces.

## Open questions

- Is the reveal voice a pitch-shift of the same actor or a second actor? A spectral pitch track around 294 s would settle it.
- Exactly where does each of the 3 credited tracks enter? Band-energy analysis only separates "jazz bed" from "no bass".
- Comment replies were not captured, so quote-and-reply chains under the 17 K and 19 K comments cannot be measured.
- Would v09 have performed without the Meta news peg? The topical-vs-evergreen split is untestable from these data; the sequels suggest ≈50 % retention of interest.
