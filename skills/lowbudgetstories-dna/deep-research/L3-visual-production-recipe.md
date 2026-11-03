# L3 — The visual machine and how to rebuild it (cross-corpus, 10 videos)
Analyst 3. Scope: look, motion, backgrounds, compositing, pipeline/cost, and a rebuild spec with ORIGINAL characters.

**Evidence base.** v04 + v05 every second (see their teardowns). Other 8 videos: 8 contact sheets each spread over the runtime (first, ~1/7 steps, last = 64 sheets ≈ 570 s of 1 fps frames) + single frames. Measured on ALL 10 at full frame rate with my own scripts: per-frame difference (240×136 / 384×216 gray, 92,000+ frames), transition events, 1-s global zoom/pan fits (phase correlation × 51 scales), drawn-cycle spike intervals, per-second luma/saturation/warmth (R−B), corner/centre luma (vignette), share of near-white "skin" pixels, opening/closing fades, end-card span, watermark opacity on black frames, hex samples. Scripts/outputs: scratchpad `a3\` (not part of the skill).
Note: v08 is the only **50 fps** file (all others 25 fps); its frame-based numbers are converted to seconds below.

---
## 1. Comparison table (visual system, all 10)
| | v01 Origin | v02 Bloomer | v03 Fast food | v04 Path | v05 Gyms 2050 | v06 Retail | v07 Social credit | v08 Delivery | v09 Metaverse | v10 Gaming |
|---|---|---|---|---|---|---|---|---|---|---|
| family | Doomer | Doomer | Life of… | Doomer | Dystopia | Life of… | Dystopia | Life of… | Dystopia | Addiction |
| dur s | 221 | 281 | 452 | 170 | 441 | 453 | 427 | 211 | 359 | 421 |
| spoken words | 4 (wordless) | 691 | 820 | 0 (wordless) | 882 | 862 | 902 | 247 | 782 | 640 |
| fps | 25 | 25 | 25 | 25 | 25 | 25 | 25 | **50** | 25 | 25 |
| cuts/min scdet≥8 | 19.0 | 15.2 | 19.9 | 20.5 | 11.6 | 13.6 | 18.7 | 17.4 | 11.7 | 10.1 |
| median shot s | 2.72 | 3.34 | 2.28 | 2.48 | 3.68 | 3.32 | 2.58 | 2.65 | 3.80 | 3.38 |
| transition events/min (frame-diff) | 21.8 | 17.5 | 24.8 | 27.9 | 17.4 | 20.8 | 22.5 | ≈29.7 | 14.0 | 18.1 |
| hard 1-frame cuts % of events | 70 | 74 | 67 | 72 | 59 | 55 | 70 | 42 | 83 | 39 |
| frames identical to previous % | 25 | 56 | 50 | 25 | 55 | 59 | 35 | 47 | 56 | 43 |
| 1-s windows with push-in % | 39 | 28 | 26 | 42 | 20 | 17 | 6 | 15 | 11 | 20 |
| 1-s windows fully static % | 6 | 21 | 36 | 8 | 43 | 44 | 26 | 36 | 49 | 27 |
| median push rate %/s | 1.8 | 1.4 | 1.4 | 1.6 | 1.6 | 1.0 | 1.2 | 1.6 | 1.2 | 2.1 |
| drawn-cycle hold (frames @25) | 10 | – | – | **5** | – | – | **5** | n/a (50p) | **5** | – |
| BG mix (P photo / CG / U UI / V footage / I painted) | 72/1/3/8/8 | 80/3/0/1/8 | 82/6/5/2/0 | 78/4/11/0/4 | 14/74/6/4/0 | ≈95/0/2/0/0 | 17/58/12/0/0 | 61/0/8/11*/6 | 12/81/0/0/0 | 8/55/15/11/0 |
| mean luma % | 36 | 30 | 42 | 32 | 32 | 49 | 35 | 43 | 26 | 43 |
| mean saturation % | 35 | 48 | 25 | 37 | 31 | 36 | 27 | 46 | 49 | 31 |
| warmth R−B | +3.7 | +5.8 | +2.2 | +3.1 | −3.7 | −5.6 | +3.9 | +17.2 | +0.1 | −1.6 |
| corner/centre luma | 0.24 | 0.24 | 0.39 | 0.25 | 0.35 | 0.57 | 0.45 | 0.47 | 0.54 | 0.34 |
| white-skin px median % / CU seconds % | 10 / 34 | 5 / 10 | 12 / 32 | 6 / 19 | 4 / 10 | 9 / 17 | 11 / 23 | 6 / 15 | 5 / 0 | 13 / 42 |
| letterbox | none | none | none | none | none | none | none | none | none | none |
| integrated LUFS | −14.6 | −20.6 | −21.9 | −10.5 | −21.4 | −22.5 | −19.9 | −16.6 | −18.1 | −20.1 |
| subtitles | – | n/c | n/c | – | machine voices only | n/c | n/c | "boss" lines | n/c | n/c |
| title/chapter cards | – | – | – | – | – | – | – | – | – | "Phase N – …" |
| end card s (pre-black s) | 3 (2) | 6 (4) | 6 (0) | 8 (2) | 7 (4) | 7 (0) | 14 (0) | 5 (2) | 5 (4) | 13 (6) |
BG mix for v04/v05 = per-beat classification of the full video; for the other 8 = classification of the 72 sampled seconds (± ~10 pts, confidence low-medium). *v08 V = a live-action man in a private jet used as the faceless "boss". n/c = not checked across the full video. Corner/centre luma is lowered both by vignetting and by the bright white face sitting in the centre.

---
## 2. Character design anatomy (channel's cast, described for analysis only)
### 2.1 Protagonist ("everyman"; the channel uses a well-known meme face)
- **Proportions:** near-adult, not chibi: head ≈ 1/6–1/7 of standing height (v10 0:08: head 62 px of 407 px). Tall bald skull dome; facial features packed into the lower ≈55 % of the head; no ears drawn on the front view; jaw flows into neck with 2–4 neck/jaw crease lines.
- **Face construction:** small black almond eyes with a thin white sclera crescent; 2–4 forehead wrinkle lines; nose = one curved stroke; mouth = one short stroke; cheek fold lines; age/neglect added as dot stipple (stubble) and wrinkles.
- **Line:** black ink, hand-drawn, tapered ends; 3–4 px at 1080p when the head is ≈350 px tall (≈1 % of head height, ≈0.3 % of frame height). Pure black core (#000000–#0B0B0B), anti-aliased.
- **Fill (sampled):** lit side #FEFFFD / #FFFFFF; shade side #E8EFEE–#F3F6F2 (one cool cel-shade band on the side away from the light, 15–25 % of head width). Clothes flat with darker fold lines: hoodie navy-black, polos #126FB9 (retail), red (fast food), orange (courier), grey tees.
- **Emotion is drawn with overlays, not animation:** lavender eye bags #B99CB9 (fatigue/despair), red-rimmed eyes (crying, blackpill), blue tear streams from eye to chin + gritted teeth (breakdown), blue sweat drops (stress), stipple stubble + messy hair (neglect, v10 4:57), pink blush (women), flat 2-tone relight for euphoric sunsets (#F7AA5A orange / #9B5CA8 purple, v04 1:29).
- **Expression library observed (≈14 states):** neutral; side-glance L; side-glance R; tired (half lids + bags); sad (brows up); crying (streams + teeth); angry-determined scrunch (brows down, crease lines between brows, pursed lips); smug smirk; open-mouth euphoric grin; forced grin with teeth; disgust (pursed, chin up); skeptical squint; shocked open mouth; eyes closed / sleeping; content soft smile. Swapped as whole face/head layers in **1 frame**, never tweened (e.g. v05 0:14.48, v05 2:11.1, v04 0:39–0:42 ladder).
- **Body poses are separate drawings per action** (sit on sofa with controller, stand front/back, profile walk, run, squat, lie, at desk, holding phone, OTS back-of-head): the same pose is reused across many shots; only the face layer changes.
- **Costume = episode identity:** each "Life of…" job gets its own uniform with a parody brand and the channel name printed on name tags/vests/caps (v06 name tag, v09 vests, v03 cap).
- **Redesign as arc marker:** the "after" version drops stubble, bags and beanie (v02 4:03, v04 2:11 mirror).

### 2.2 Faceless crowd ("NPC" role)
- Same body grammar and line as the protagonist; head fill flat mid-grey **#979996–#A3A3A3** (v05 0:47, v10 0:08), sometimes with one darker shade band; dot eyes, L-shaped nose, flat mouth, no expression changes.
- Used for officials, co-workers, commuters, audiences; duplicated sprites for masses (v01 0:00 ≈20 identical graduates; v05 1:45 cell grid ≥16 copies). Often blurred (DOF) behind the protagonist (v01 0:04, v05 1:12).
- Narrative use: grey = "not seen as a person"; v04 swaps a grey co-worker for a drawn individual at the end.

### 2.3 Idealised rival / power figures
- Drawn version: tan skin, yellow flat-top hair cone, huge square jaw, thick neck lines, usually in **profile**, gold watch (photo cut-out), open white shirt (v07 4:03, v09 0:03 bartender).
- **Medium contrast trick:** the rival or the power figure is rendered in a different, "higher" medium: a greyscale photoreal bearded man (v02), a 3D hologram (v05), a live-action man in a jet with subtitles (v08). The protagonist stays flat 2D.
- Mentor/"voice": v02's photoreal figure ends "I am nothing but a voice in your head" (comment-evidenced); v05's blond gym mentor.

### 2.4 Other recurring roles
Blonde girlfriend/co-worker with blush; angry "Karen" customer (pink top, crossed arms); old lady; manager with glasses + neckbeard; obese customer. Devil/angel shoulder heads with coloured glows (v10 3:54).

---
## 3. Compositing: how drawn characters sit on real/CG plates
| parameter | measured / observed rule |
|---|---|
| Plate type | still image in ≥85 % of runtime in every video; moving footage only inside screens or short inserts (≤11 %) |
| Scale | WS: character 30–45 % of frame height; MS: 80–110 % (cropped at waist); CU: head 50–70 % of frame height; OTS: back of head fills 35–50 % of frame width at one edge |
| Depth of field | plate sharp in WS; Gaussian-blurred in MS/CU (bokeh look); drawn background characters blurred with the plate (v05 1:12); foreground occluders (barbell, hand, silhouette head) blurred heavily (v04 1:05, v10 5:01) — three-plane depth with blur, almost never parallax |
| Shadows | none: no contact or cast shadows (feet simply placed, v07 2:04) |
| Edge | the ink outline is the edge: no stroke, no glow, no feather |
| Colour match | scene tint pushed onto characters in strong-light scenes (blue lobby makes white shirts #374552; v04 night jog tinted blue; desaturated sleeping head; sunset flat relight). Institutional scenes desaturate the plate to near-B/W and keep only neon colour (v05 3:20, v07 0:00) |
| Vignette / centre weighting | corner/centre luma 0.24–0.57 in all 10; dark corners, lit centre |
| Letterbox | 0 % of frames in all 10 videos |
| Scale/perspective matching | eyeballed; horizon roughly at character chest/eye level; occasional mismatches accepted |
| Photo-texture fills | clothing patterns filled with photo textures (v08 Hawaiian shirt), real-object cut-outs as props (phones, watches, paper bags, bottles, dollar notes) |
| Screens | real video / game footage / video-site UI composited into monitors and TVs (v03, v05, v07, v10) |

### Watermark
YouTube play icon + "Low Budget Stories" in a Comic Sans-style casual font, **white at 60 % opacity** (153/255 measured on black, v05 7:10.5); bbox x 31–619 px, y 996–1052 px at 1080p (1.6–32.2 % W, 92.2–97.4 % H); constant on every frame including black frames, absent on the end card; in v04 it fades out with the final fade. Present in 10/10.

### Typography / text on screen
- Diegetic first: phone UIs (state bot messages, dialogs, chats, alarms), whiteboards, billboards, neon signs, product labels with the channel name.
- Subtitles only where a voice must be marked as "other": state/AI voices (v05), the live-action "boss" (v08). Style: white humanist sans, ≈3 px black stroke, centred, bottom edge 86–91 % of height, cap height ≈4 % of frame.
- Chapter cards only in v10: black screen, white bold rounded sans ≈3.5 % height, fade-in ≈1 s, hold ≈3 s, cross-dissolve into a desaturated first frame.
- Phone UI text appears word-by-word in sync with the TTS voice (typewriter).
- End card: orange **#ED720B**, channel name in heavy rounded black caps across the top, the beanie mascot at left (0–28 % W), 3–4 social handles, two translucent end-screen placeholders (dark rectangle ≈ x 1–35 % / y 52–85 %, light circle ≈ x 82–98 % / y 55–82 %), last ≈1 s fades to black; duration 3–14 s (median 6.5 s), preceded by 0–6 s of black in 7/10.

---
## 4. Motion: what actually moves
| element | how | numbers |
|---|---|---|
| Opening | fade from black, ease-out | 10/10; luma plateau reached at **1.2–1.4 s** |
| Camera push-in (Ken Burns) | uniform scale of the whole composite, eased in/out | in 6–42 % of 1-s windows; median rate **1.0–2.1 %/s** per video (pooled typical 1.6 %/s, p90 2.4–5.0 %/s); one long eased push at a turn (v04 0:39.5–0:41.8, bell-shaped speed) |
| Pull-back reveal | eased zoom-out to a duplicated grid | v05 1:45.5, 94 frames |
| Reframe "swish" | camera slides/zooms between CU and two-shot of the same composite with directional motion blur | 8–14 frames (0.32–0.56 s); 37 in v05 alone |
| Pans/trucks | rare | 0–7 % of windows; one 2-layer truck with rack focus (v04 1:39) |
| Parallax | essentially none (single plane); the fitted global scale explains pure pushes | – |
| Camera shake | none detected | – |
| Expression swaps | 1-frame layer replace | 0–3 per shot |
| Drawn action cycles | 2 drawings alternating, each held **5 frames** (5 fps) while the camera moves at 25 fps | v04 run/squat, v07, v09 conveyor; v01 holds 10 frames |
| Lip-sync / blinks / breathing | none: talking shots are frozen frames | v05 3:29–3:47 = 18 s zero pixel change |
| Object appear/disappear | opacity fades or 1-frame pops | v04 bottles fade 0:45.5–0:46.75; v01 0:28 girls pop in |
| FX | light leaks + glow + scan-line glitch for holograms; radial zoom-blur at a turn; speed-line backgrounds for action (v08 1:33) | 6–25 frames |
| Transitions | hard cuts dominate (39–83 % of events, ≥55 % in 8/10); cross-dissolves (12–30 frames) for time jumps and montages; double-exposure dissolves in montage (v10 1:59) | – |
| Closing | linear fade to black over ≈2.2 s (v04 2:37.1–2:39.3) or cut to black | – |

Static-ness splits by audio mode: the two wordless videos have only 25 % identical frames (constant pushes on the beat), voiced videos 43–59 % (the voice carries the shot, the picture freezes).

---
## 5. Backgrounds: types, tells and sourcing
| type | share | where | quality tells |
|---|---|---|---|
| Real photos (stock/web) | dominant in Doomer + "Life of…" (61–95 %) | supermarkets, fast-food counters, streets, gyms, homes, hospitals | legible real products and signage (pasta brands, mints, Chinese-language fast-food menus, a coffee chain), consistent lens perspective, no stock watermarks seen → licensed stock or web photos [inferred] |
| CG stills (3D render / game capture / AI image) | dominant in dystopia family (55–81 %) | sci-fi rooms, neon gyms, metaverse bars, car interiors, living rooms | perfect but empty rooms, game-engine lighting (v09 metaverse plates resemble a known virtual-world client), a night-city exterior resembling a game screenshot (v05 2:39); 2023+ uploads plausibly AI-generated (over-saturated painterly sky v04 0:30) [inferred, low–medium] |
| Painted/illustrated | 0–8 % | anime-style night city on a bench (v01 3:10, reused in v02 0:00), speed lines (v08 1:33) | reused across videos |
| UI mocks | 0–15 % | phone/laptop/TV screens with a drawn hand | built from real phone photos + custom UI |
| Real moving footage | 0–11 % | inside screens: gameplay, gym footage, news page; one live-action "boss" | third-party footage |
| Flat | 3–8 % | black, title cards, end card | – |
Asset reuse across videos is visible (same painted bench/city plate and the same black-pill hand shot in v01 and v02; same "HODL" crypto poster in v07 and v10; same end card since 2022).

---
## 6. Inferred pipeline, tools, effort and cost
**Pipeline (inferred from artefacts):**
1. Script → (voiced videos) TTS lines per character; state voices given a robotic effect (v05 receptionist pitch track jumps an octave between frames = vocoder/robot FX). Evidence for TTS: protagonist pitch IQR only 8–12 Hz at 200 WPM average; comment "voice bot could be upgraded to the ElevenLabs level". Confidence medium-high.
2. Shot list → gather one plate per scene (photo/CG), screen footage, prop cut-outs.
3. Draw character layers per shot as transparent PNGs from a reusable template (body pose + interchangeable head/face). Hand-inked raster lines with pressure taper → a drawing app (Photoshop/Krita/Clip Studio/Procreate class) [medium].
4. Composite + animate in a keyframe editor: scale/position keys with easing, Gaussian blur, directional motion blur on reframes, radial blur, glow/light-leak overlays, opacity fades, typewriter text, per-layer tint. Typical of After Effects/Premiere-class tools [low-medium; CapCut/DaVinci could do the same].
5. Music bed + SFX; in wordless films cuts snapped to the beat grid (v04: 52/57 cuts within 80 ms of a 97.6 BPM beat).
6. Export 1080p25 (v08 50p), watermark track over everything, end-card template.

**Effort (inferred):** channel output 2021–2024 = 90–110 finished minutes/year ≈ **2 min/week**; creator comments: v01 "took a while because of the large amount of editing-time", v05 "insane lot of work… 3 weeks" for 7.35 min (≈2.5 min/week). Assuming one person at ~40 h/week → **≈16 h per finished minute (range 12–25 h)**. Output rose to 178 min (2025) and 261 min (2026), suggesting help or tooling later [inferred].

**Per-minute asset load (v05 measured):** 17.4 transition events/min, ≈8 new compositions/min, ≈6–10 new drawn poses/expressions/min, 1 new plate per ≈30 s.

**Cost estimate for our rebuild (7-min voiced episode, USD):**
| item | qty | cost |
|---|---|---|
| Character sheet (one-off, original cast) | 60–80 assets | 900–2,000 once |
| New poses/expressions per episode | 20–40 | 300–600 (or in-house) |
| Background plates (own AI generation, commercial licence) | 30–50 | <20 compute (+ subscription) |
| TTS voices | ≈1,000 words | covered by a ~$22/month plan |
| Music/SFX library | 1–3 tracks | $15–30/month subscription |
| Editor/compositor time | 7 min × 6–10 h with templates | 40–70 h |
**Minimum viable team:** 1 writer-director-editor (compositing in a template) + 1 part-time illustrator (can be the same person after the sheet exists) + TTS + image generator. A Remotion template lowers editor time to ≈3–5 h per finished minute [inferred].

---
## 7. Invariant formula (identical in ≥8/10)
1. 1920×1080, no letterbox, 16:9 full frame (10/10); 25 fps (9/10).
2. Fade-in from black, plateau at 1.2–1.4 s (10/10).
3. Flat-filled, black-ink, cut-out 2D characters on a still plate (photo or CG) for ≥85 % of runtime (10/10).
4. Characters do not animate except 1-frame expression swaps and rare 2-drawing cycles; no lip-sync (10/10).
5. The camera is the animator: eased push-ins at 1.0–2.1 %/s median, plus reframes; no shake (10/10).
6. Hard cuts are the default transition (≥55 % of events in 8/10).
7. Shot median 2.3–3.8 s (10/10).
8. Dark corners / lit centre (corner/centre luma ≤0.57, 10/10).
9. Constant semi-transparent channel watermark bottom-left (10/10).
10. Orange branded end card with mascot, 3–14 s (10/10).
11. Grey faceless background people and a phone POV with a drawn hand appear in most videos (seen in ≥6–7/10 samples — not fully invariant).

## 8. Variations by format family
| family | videos | visual signature |
|---|---|---|
| Doomer saga | v01, v02, v04 | music-led (2 wordless, 1 sparse VO), most motion (25–56 % static frames, 28–42 % push windows), deepest vignette (0.24–0.25), dark night grades turning warm, photo plates 72–80 %, painted night-city plate, beat-locked editing (v04) |
| "Life of a …" jobs | v03, v06, v08 | bright real workplace photos (luma 42–49, photo plates 61–95 %), parody uniforms/brands with channel name on name tags, customer archetype parade, highest CU share (v03 32 %), dialogue-led, v08 adds speed-line action plates and a live-action "boss" |
| Dystopia / future | v05, v07, v09 | CG plates 58–81 %, neon purple/blue grades, desaturated institutions, phone messages from a state bot, subtitles for machine voices, longest shots (median 3.7–3.8 s in v05/v09), many frozen dialogue holds (43–49 % static windows) |
| Addiction cycle | v10 | chapter cards ("Phase N – …"), one CG living room re-graded for time of day (blue night → golden sunset), real gameplay inside the TV, angel/devil glows, CU share 42 %, longest single shot 43.9 s |

---
## 9. REBUILD SPEC — original characters, own/royalty-free assets
### 9.1 Export & project settings
- 1920×1080, 25 fps, progressive, Rec.709 SDR. Render H.264 High, CRF 16–18 (or 12–20 Mbps VBR 2-pass), AAC-LC 48 kHz 320 kbps stereo.
- Audio: −14 LUFS integrated, ≤−1 dBTP; voice-led scenes music bed 12–18 dB under dialogue; wordless films may run −12 to −14 LUFS.
- Plates generated/stored at ≥2304×1296 (120 %) so pushes never upscale.

### 9.2 Layer stack (bottom → top)
| # | layer | default settings |
|---|---|---|
| 1 | BG plate (photo/CG still) | blur 0 px (WS) / 6–12 px (MS) / 14–24 px (CU) at 1080p; grade per scene |
| 2 | Plate props (cut-out objects) | same blur as plate |
| 3 | Crowd layer (faceless extras) | scale 50–80 % of protagonist; blur = plate blur × 0.5–1.0 |
| 4 | Main characters (PNG, drawn at 2× size) | sharp; scene tint 20–40 % (colour/multiply layer) |
| 5 | Foreground occluder (OTS head, hand, object) | blur 10–30 px; fills 25–50 % of width at one edge |
| 6 | FX (glow, light leak, tears overlay, speed lines) | additive/screen 40–80 % |
| 7 | Scene grade (adjustment) | see 9.6 |
| 8 | Vignette | radial; corners −40…−60 % luminance; target corner/centre luma 0.25–0.55 |
| 9 | Diegetic UI / phone / chapter card / machine-voice subtitles | see 9.7 |
| 10 | Watermark | OUR channel name, bottom-left, white 60 %, height ≈5 % of frame, x≈1.6 %, y≈92–97 %, our own font (not a copy of the corpus look) |
| 11 | Transition layer | cuts / swish / dissolve / zoom-blur |

### 9.3 Original cast brief (fills the corpus roles; must not resemble any meme or existing IP)
| role | our original design | anti-resemblance checks |
|---|---|---|
| Everyman protagonist ("Nob") | head = soft rounded-square "bread-loaf" shape, width:height 1:1.1, with a 3-strand hair tuft and round ears; skin warm light grey **#ECE8E2**, shade band #D9D4CC; eyes = two small vertical ovals; emotion carried by thick eyebrow strokes + mouth; signature mustard **#D9A21B** scarf or zip jacket; adult proportions head ≈1/6 of height | no tall bald dome, no chin-crease meme face, no beanie+hoodie combo, no stipple-stubble "doomer" look as default |
| Faceless crowd ("Blanks") | same body template; smooth egg head with NO features except one slightly darker horizontal visor band; fill cool slate **#8E959C**, outline at 70 % weight; never change expression; duplicate with ±5 % scale and ±4° hue jitter | no dot eyes + L-nose + flat mouth (the NPC meme) |
| Idealised rival ("Vance") | 1.25× protagonist height, V torso, glossy hair swoop rendered with 3-tone gradient shading (a more "expensive" render than Nob — keep the medium-contrast trick), skin **#D9A47E**, signature: white sneakers + gold earbuds; always 3/4 view, chin up | no flat-top cone hair, no extreme square-jaw profile, no photo of a real person |
| Mentor / inner voice ("Ora") | outline-only translucent silhouette with soft cyan glow **#6FE3FF** at 60 % opacity, no facial features; appears in reflections, screens or as a hologram; calm TTS voice | no photo-realistic bearded figure, no real athlete/actor likeness or name |
| State/AI voice | a UI avatar: rounded hexagon icon with an animated waveform, colour **#7B61FF**; robot-processed TTS | no copy of any real app/brand |
| Support | love interest (curly auburn bob, green cardigan), loud customer, boss (always seen from behind or as a shadow), old neighbour | invent all; no "tradgirl/Karen" meme faces |
| Mascot for end card | Nob in his scarf, ¾ view, waving | original only |

### 9.4 Character sheet deliverables (draw at 2× = head ≈700 px tall for CU sets)
Naming: `{CHAR}_{part}_{view}_{state}_v{n}.png` (transparent, 3840 px canvas). Line: black #111111, 8 px at 2× (→4 px at 1080p MS), tapered ends; flat fills + one cel-shade band on the side away from key light.
- **Bodies (per character, 18):** stand front, stand ¾L, stand ¾R, back view, profile walk A/B, run front A/B, sit sofa (+controller), sit desk/laptop, sit bench, lie (top view), squat A/B, hold phone (POV-compatible arm), arms crossed, point, OTS back-of-head large crop.
- **Faces (protagonist, 16):** neutral, glance-L, glance-R, tired (+bags overlay), sad, cry (+tear overlay), angry-determined, smug, euphoric grin, forced grin, disgust, skeptical, shocked, eyes-closed/sleep, content smile, focused/strain (+sweat overlay).
- **Overlays (8):** eye bags (#B9A0C4), tear streams (#8EC1F0), sweat drops, blush (#F2A7A7), stubble stipple, dark-circle red rims, sunset 2-tone relight masks (orange #F7AA5A / violet #9B5CA8), cold-night tint mask.
- **Hands (6):** POV phone hold L, tap finger, marker hand, pointing hand, holding cup, fist.
- **Crowd:** 6 bodies × 3 outfits; rival 10 bodies × 8 faces; mentor 4 glow poses.
- **Uniform swaps per episode:** 1 outfit layer set aligned to the body templates (invented brand logo).

### 9.5 Background sourcing & licensing rules
1. Only own-generated images (commercial-licence generator), own photos, or CC0/royalty-free libraries whose licence allows commercial video use.
2. No visible real brands, logos, product packaging, readable real signage, real people, real game/film footage, or real platform UIs; screens-within-screens show our own fake UIs and own-made clips.
3. Plate prompt template: `photorealistic empty {location}, eye-level 35mm, {time-of-day} lighting, no people, no text, no logos, clean composition, room for a character in the {left/centre/right} third`; generate WS and a tighter MS crop variant; for dystopia add `neon {purple|blue} accents, sterile, symmetrical`.
4. Make the "duplicated grid" reveal plates by tiling one generated cell (≥4×4).
5. Moving backgrounds (image-to-video) ≤10 % of runtime and only for screens/windows; never generate the characters with video models (style drift).
6. Log every asset: source, licence, prompt/seed, date.

### 9.6 Colour-grading recipe (per scene, measured targets)
| mood | mean luma | saturation | warmth R−B | plate treatment | character tint |
|---|---|---|---|---|---|
| despair / night | 15–25 % | 40–46 % | −5 … −10 | darken −40 %, blue cast | 20 % blue |
| institution | 22–28 % | 19–28 % | ≤ −5 | desaturate plate to 10–20 %, keep neon colour | 30 % scene colour |
| neutral day | 40–50 % | 25–36 % | 0 … +3 | as shot | 0–10 % |
| hope / human warmth | 38–45 % | 30–45 % | +2 … +6 | warm highlights | 10–20 % warm |
| euphoric sunset beat (≤3 s) | 35–45 % | 40–50 % | +5 … +12 | sunset plate | flat 2-tone relight masks |
Arc rule: raise mean luma ≥+15 points from first act to last act in transformation stories (v04: 18 → 39).

### 9.7 Text & typography
- Phone UI: clean sans 28–36 px on 1080p, typewriter reveal on TTS word timestamps; dialog boxes ≤8 words; ≥1.2 s per dialog.
- Machine-voice subtitles: white humanist sans, 3 px black stroke, cap height ≈4 % (≈44 px), centred, bottom edge at 89 %; ≤42 characters per line.
- Chapter cards (cycle/explainer formats): black, white bold rounded sans ≈38 px, fade-in 1 s, hold 2.5–3 s, cross-dissolve 0.5 s into a desaturated first frame that saturates over 1 s.
- Diegetic signs/whiteboards: handwriting font for boards, glowing sans for neon (outer glow 20–40 px), all text in our invented world.

### 9.8 Motion presets (Remotion/AE/CapCut numbers @25 fps)
| preset | spec |
|---|---|
| FADE_IN | opacity of black solid 1→0 over 32 frames, ease-out cubic (luma plateau at 1.3 s) |
| FADE_OUT | linear 55 frames (2.2 s) to black, then 25–100 frames black before end card |
| PUSH | scale 1.000 → 1 + r·t, r = 1.6 %/s default (range 1.0–2.6), easeInOutCubic over the shot, anchor = face centre; ≤6 % total per shot |
| PUSH_TURN | 2.2 s eased push, peak speed ≈7 px/frame, ending in ZOOM_BLUR |
| PULL_REVEAL | scale 1.0 → 0.25 over 90–100 frames, easeInOutQuad, onto a tiled grid plate |
| SWISH | reframe CU↔two-shot of one composite in 10 frames (8–14), scale ratio 1.6–2.2×, easeInOutCubic, motion blur shutter 180° (or directional blur peak 40 px) |
| ZOOM_BLUR | 6-frame radial blur 0→30→0 px across a cut |
| DISSOLVE | 12–25 frames (time jump), 25–30 frames for montage double exposure |
| EXPR_SWAP | replace face layer in 1 frame; 0–3 per shot; place on a beat or 4–8 frames after a line ends |
| CYCLE_2 | 2 drawings alternating, hold 5 frames each (5 fps); optional bob ±1 % scale per stride |
| RACK_FOCUS | fg blur 0→20 px and bg 20→0 px over 12–20 frames |
| UI_DRIFT | phone POV drift 5–10 px/s + PUSH 1.4–2.2 %/s; tap = finger layer in 3 frames, button highlight 4 frames |
| HOLO_IN | opacity 0→1 in 10 frames, 2 glitch frames offset ±8 px, additive glow 30 px, scan-lines 3 px at 20 % |
| POP_IN | character/prop appears in 1 frame (comic beat) |
| No-go | camera shake, lens-flare spam, lip-sync, tweened expressions, holds >6 s while someone speaks |

### 9.9 Edit rhythm targets
- Voiced: median shot 2.9–3.7 s; 14–25 transition events/min; ≥55 % hard cuts; ≥1 SWISH per 6 s of dialogue; ≤6 s frozen hold.
- Wordless: median shot 2.4–2.5 s on a beat grid (2–6 beats), ≥85 % of cuts within 80 ms of a beat; pushes on ≥40 % of seconds.
- Shot-scale mix (by seconds): CU 15–35 %, MS 40–55 %, WS 15–30 %, inserts/UI 5–15 %.

### 9.10 Remotion implementation sketch
- One `Shot` component per row of a JSON shot list: `{id, durFrames, plate, plateBlur, crowd:[], chars:[{asset, x, y, scale, tint, faceSwaps:[{frame, asset}]}], fg, camera:{preset, rate, anchor}, transIn, ui, subs, audioCues}`.
- Camera presets are pure functions of frame → transform (spring/interpolate with Easing.inOut(Easing.cubic)); motion blur via `@remotion/motion-blur` `CameraMotionBlur` on SWISH only.
- Typewriter text driven by TTS word timestamps (JSON from the TTS provider or a forced aligner).
- Watermark and grade as top-level wrappers; end card as a fixed 7-s composition.
- QA script: assert fps=25, no frame hold >150 frames during speech, hard-cut share ≥0.55, push rate within 1.0–2.6 %/s, LUFS −14 ±1.

### 9.11 CapCut / AE quick map
PUSH = keyframe scale with "ease in/out"; SWISH = keyframe position+scale over 10 frames + motion-blur effect; ZOOM_BLUR = radial/zoom blur transition 0.24 s; DISSOLVE = cross-dissolve 0.5–1 s; RACK_FOCUS = Gaussian blur keyframes; HOLO_IN = glow + glitch effect; watermark on a top track at 60 % opacity.

## 10. Anti-patterns (what the corpus never does or what hurt it)
- Full character animation, lip-sync, 3D characters, camera shake, letterboxing — none in 10/10; adding them raises cost without matching the look.
- All-illustrated backgrounds: the satire depends on a "real world" plate behind a crude character.
- Frozen speaking holds of 8–18 s and wordless walks of 17–18 s (v05 heatmap ≤0.03 at 1:14–1:32 and 5:02–5:19).
- Quiet mixes (−20 to −22.5 LUFS in 7/10 voiced videos).
- Real brands, real people, real game/platform footage, licensed chart songs, meme characters — all present in the corpus, all forbidden for us.
- Thumbnail characters that never appear in the video (v05).

## Why it works
1. The cheapest possible animation (static cut-outs + camera) is hidden by rhythm: an event every 2.2–4.3 s and a push on most other seconds keeps the eye busy.
2. Crude flat characters on real or realistic plates create instant satire: "a meme living in our world"; the plate does the world-building for free.
3. Emotion is carried by a small, legible overlay vocabulary (bags, tears, scrunch, blush, grade) that reads at phone size and in any language.
4. Grey faceless extras vs one drawn protagonist encodes the theme (alienation) in the art direction itself.
5. Rendering the rival/power in a "higher" medium (photo, hologram, live action) makes status difference visible without dialogue.
6. A fixed template (watermark, fade-in, end card, uniform swaps, phone POV) lets one person ship ≈2 finished minutes per week.

## Rules to copy
1. [KOPYA] Render 1920×1080 at 25 fps, full frame, no letterbox; start every video with a 1.2–1.4 s ease-out fade from black.
2. [KOPYA] Keep ≥85 % of runtime as original flat-filled, black-ink cut-out characters on still plates (photo-real or CG); moving footage ≤10 % and only inside screens.
3. [KOPYA] Animate with the camera: push-ins at 1.0–2.6 %/s (default 1.6 %/s, eased), on 20–45 % of seconds; no shake, no parallax rigs.
4. [KOPYA] Characters never lip-sync; change expressions only by 1-frame face swaps (0–3 per shot) from a 16-state library; use 2-drawing cycles held 5 frames for physical action.
5. [KOPYA] Hard cuts for ≥55 % of transitions; median shot 2.4–3.7 s; for dialogue build coverage with 8–14-frame motion-blurred reframes of one composite.
6. [KOPYA] Blur plates by shot size (0 / 6–12 / 14–24 px at 1080p for WS/MS/CU), blur foreground occluders 10–30 px, never add cast shadows; tint characters 20–40 % toward strong scene light.
7. [KOPYA] Grade by mood table 9.6; vignette to a corner/centre luma ratio of 0.25–0.55.
8. [KOPYA] Use an original faceless slate-grey crowd for institutions and masses; duplicate sprites ±5 % scale for crowds; reveal a duplicated grid once per dystopia episode.
9. [KOPYA] Draw the protagonist's state with overlays (bags #B9A0C4, tears #8EC1F0, sweat, blush, stubble) and redesign him cleaner at the end of a transformation arc.
10. [KOPYA] Render the rival or power figure in a more detailed medium than the protagonist (gradient-shaded, hologram, or own-shot live action of a consenting actor).
11. [KOPYA] Put information on diegetic UI (phone POV with a drawn hand, typewriter text synced to TTS word times); subtitle only machine/state voices.
12. [KOPYA] Constant watermark bottom-left at 60 % white; branded end card 6–8 s with 2 end-screen slots, preceded by 1–4 s black.
13. [İYİLEŞTİRME] No hold >6 s while a character speaks; no wordless stretch >6 s without a new gag, cut or reveal.
14. [İYİLEŞTİRME] Mix to −14 LUFS integrated, ≤−1 dBTP, in every video.
15. [İYİLEŞTİRME] Thumbnail characters and props must exist in the video in the same design.
16. [ETİK] Never use meme faces (Wojak/NPC/Chad/Pepe-type), real people or their names, real brands/logos/packaging, real platform UIs, game or film footage, or chart music; every plate, UI and track is own-made or licensed for commercial video, logged with source and licence.
17. [ETİK] Parody brands must be invented names and invented logos that do not echo a real logo's shape or colour pairing.

## Open questions
- Which exact editor/drawing apps the channel uses cannot be proven from pixels; tools are inferred from artefact types only.
- How many CG plates are AI-generated vs rendered/captured: indistinguishable at YouTube 1080p bitrate; a frame-level AI-artefact check on originals would be needed.
- BG percentages for the 8 non-assigned videos rest on 72 sampled seconds each; a per-second classifier pass would tighten them.
- The 2025–2026 jump to ≈5 min/week output may reflect a team or AI tooling change not visible in this top-10 corpus (all ≤2024).
