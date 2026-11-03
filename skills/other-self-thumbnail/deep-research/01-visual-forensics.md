# 01 · Visual Forensics & Measurement — the three viral thumbnails

Agent 1/3. Everything below is **pixel-measured** (Python 3.12 + Pillow/NumPy/SciPy/scikit-learn on the 1280×720 JPEGs)
unless marked (?) = estimate / judgement. Coordinates are `x0,y0 – x1,y1` in px at 1280×720; percentages are of
width (W = 1280) or height (H = 720). Luminance = Rec.709 luma 0–255; contrast = WCAG 2.x ratio.

Files in this folder
- `T1/T2/T3_layout.png` — measured boxes drawn over each thumbnail (text, head, face, eyes, object, light, rule-of-thirds lines, duration-badge zone).
- `T1/T2/T3_face_crop2x.png` — 2× face crops (line weight, shading and eye rendering).
- `small/*_168x94.png`, `small/*_320x180.png`, `small/*_168x94_zoom4x.png` — mobile/feed-size tests (§6).

---

## 1. Layout grid (measured boxes)

| Element | T1 "DAY 1." | T2 "JUST SHOW UP." | T3 "DOPAMINE." |
|---|---|---|---|
| Text block | 38,31 – 575,162 → **41.9 % W × 18.1 % H**, top-LEFT aligned | 31,42 – 1219,202 → **92.8 % W × 22.2 % H**, centred (centre x = 625, −15 px) | 143,27 – 1187,187 → **81.6 % W × 22.2 % H**, centred (centre x = 665, +25 px) |
| Text box area | 7.6 % of frame (ink 2.7 %) | 20.5 % (ink 10.0 %) | 18.0 % (ink 10.5 %) |
| Hero head | 280,196 – 622,550 (342×354) | 567,181 – 838,424 (271×243) | 331,186 – 660,520 (329×334, incl. brain) |
| Head centre | (451,373) = **35.2 %, 51.8 %** | (702,302) = **54.9 %, 42.0 %** | (496,353) = **38.7 %, 49.0 %** |
| Face features (brows→mouth) | 415,285 – 625,472 | 715,258 – 838,392 (3/4 profile, features crowd the right edge of the head) | 455,350 – 646,503 |
| Eyes box / centre | 452,352 – 612,428 / (532,390) = 41.6 %, 54.2 % | 716,280 – 836,362 / (776,321) = 60.6 %, 44.6 % | 477,368 – 646,450 / (561,409) = 43.9 %, 56.8 % |
| Key object | Alarm clock 800,345 – 1255,548; digits 838,383 – 1125,517 | Door-gap light strip x 945–995, full height; hand on handle 950,415 – 1095,695 | Phone 760,448 – 922,640; bubble arc 540,205 – 925,470 |
| Object centre | digits (981,450) = **76.7 %, 62.5 %** | light x = 970 (75.8 %); hand (1022,555) = 79.9 %, 77.1 % | phone (841,544) = **65.7 %, 75.6 %** |
| Main negative space | top-right 600–1280 × 0–340 ≈ 25 % of frame | left 0–270 × 200–720 ≈ 15 % (guitar case reads as black mass, adds ≈ 15 % more) | right 930–1280 × 190–560 ≈ 14 % + bed bottom-left |
| Text → head gap | 35 px (head clear of text) | **0–21 px — head top touches the text's black outline** (col 700: text ends y 175, outline 176–180, skin from 181) | **≈ 16 px — brain/skull kisses the text** (col 560: text ends 168, skin from 185) |
| Gaze direction | right → clock (pupils/brows aim at digits) | right → door/handle (pupils at right rim of the eye whites) | down-right → phone |
| Reading path | **Z**: text TL → face (centre-left) → gaze → red clock (right-middle) | **Top bar → face → arm → light**: horizontal text, then a left-to-right diagonal along the arm into the light strip | **Top bar → brain → arc of bubbles → phone**: a "C" curve, light feeds back into the head |

Cross-thumbnail pattern
- **Two-band layout**: text band occupies the top **18–22 % of H** (y ≈ 27–202); picture band below. Text never sits over the face.
- **Hero left / centre, light object right.** Head centre x = 35–55 % W; light object centre x = 66–80 % W, y = 62–77 % H (on or near the lower-right rule-of-thirds intersection 66.7 %, 66.7 %).
- **Eyes sit on the horizontal centre band**: eye centres y = 44–57 % H, x = 42–61 % W — i.e. within ±10 % of the frame centre, not on a thirds line. The *face* is the centre of the frame; the *light* takes the thirds point.
- **Gaze → object**: in 3/3 the hero looks at the light source; the eye-line is the bridge that makes the viewer's eye travel left → right.
- **Brightness map** (3×3 mean luma): bright cells are always the centre column + top row (text). T1 `[57 34 10 / 89 96 31 / 58 62 37]`, T2 `[74 107 84 / 6 91 38 / 9 77 57]`, T3 `[63 105 75 / 49 119 12 / 62 76 19]`. One flank (T1 right-top, T2 left, T3 right) is left near-black (luma ≤ 12) as negative space.
- **Bottom-right badge zone** (≈ x ≥ 1170, y ≥ 655 (?)) contains only low-information dark furniture/door/bed in all three. Text bottom is ≥ 450 px above it.

---

## 2. Scale — how far they zoom in vs. the film

| Measure | T1 | T2 | T3 | Film frames (2, 5, 10, 17) |
|---|---|---|---|---|
| Head width, % W | **26.7 %** | **21.2 %** | **25.7 %** | 5.7 % (f2), ≈ 7 % (f5), ≈ 8 % (f10, ?), ≈ 5 % (f17) |
| Head height, % H | **49.2 %** | **33.8 %** | **46.4 %** | 12.5 % (f2) – ≈ 15 % |
| Head ellipse area, % frame | ≈ 10.3 % | ≈ 5.6 % | ≈ 9.3 % | whole cream figure (head+body) = 0.5–2.3 % across 20 frames |
| Eye/pupil size | pupils ≈ 42 px Ø (3.3 % W) | eye white ≈ 70 px, pupil ≈ 30 px (?) | eye white ≈ 65 px, pupil ≈ 25 px (?) | eyes are 3–6 px dots/dashes |
| Light object, % frame | clock body 10.0 %, digits 4.2 % | strip 3.1 % (core 33–36 px wide) | phone 3.4 %; full light effect bbox ≈ 18 % | clock in f2 ≈ 0.5 % |
| Text ink, % frame | 2.7 % | 10.0 % | 10.5 % | "DAY n" label ≈ 0.2 % |

**Zoom factor: ×3.5 – ×4.8 linear on head width (≈ ×12 – ×23 by area).** The film keeps the hero at 5–8 % W in a wide
stage; the thumbnail is a close-up/medium close-up in which the head alone is 34–49 % of frame height and the
hero (head + visible body) fills ~35–45 % of the picture band. T1 is literally the film's frame-2 set (bed, nightstand,
5:00 clock) re-staged ~4.5× closer and with the clock moved to the right.

---

## 3. Typography

| Measure | T1 | T2 | T3 |
|---|---|---|---|
| Text | `DAY 1.` | `JUST SHOW UP.` | `DOPAMINE.` |
| Words / glyphs | 2 / 5 (+1 space) | 3 / 11 | 1 / 9 |
| Case, period | ALL CAPS, trailing period | ALL CAPS, trailing period | ALL CAPS, trailing period |
| Lines | 1 | 1 | 1 |
| Cap height (glyph bbox heights) | 118–131 px → **≈ 125 px = 17.4 % H** | 132–155 px → **≈ 142 px = 19.7 % H** | 144–158 px → **≈ 151 px = 21.0 % H** |
| Stroke width (2× median distance-transform ridge) | **22 px** = 18 % of cap height | **33 px** (p90 36) = 23 % | **34 px** = 22.5 % |
| Letter gaps (tracking) | 12, 5 px (4–10 % of cap) | 3–7 px, some glyphs touch/overlap (−7) | 6–14 px; P/A overlap −11 |
| Word space | 87 px (Y→1) | 43, 60 px | – |
| Period | 25×22 px, **floated 42 px** after the "1" | 36×38 px, tucked into the P's foot (−23 px) | 35×34 px, 12 px gap |
| Baseline | ±7 px | **wobbly: glyph bottoms 177–202 px (±12)** and tops 42–62 | ±5 px, slight rise |
| Colour | #FDFDFD (pure white, no tint) | #FDFDFD | #FDFDFD |
| Outline / shadow | ≈ 2–3 px dark rim (luma 6 vs bg 11) — effectively none | **8–10 px pure-black stroke** (luma 0–4; visible where it crosses the door light: x 1068–1080 on row 130) + soft dark falloff back to bg by ≈ 20–25 px | **≈ 8–10 px black stroke** + soft falloff to bg by ≈ 25 px |
| Shadow direction | – | none: halo luma below/above/left/right = 1/1/2/2 → uniform stroke, **no offset drop shadow** | same (2.1/1.0/2.0/2.0) |
| Text vs. local bg contrast | **19.1 : 1** | **19.9 : 1** | **19.9 : 1** |
| Margins | left 38 (3.0 % W), top 31 (4.3 % H) | left 31 (2.4 %), right 62 (4.8 %), top 42 (5.8 %) | left 143 (11.2 %), right 94 (7.3 %), top 27 (3.8 %) |
| Relation to head | 35 px above, no overlap | outline touches head top | 16 px above, touching |

Font identification (?)
- **T1** ≈ the film's own "DAY n" label face — a **Comic-Sans-Bold-like hand-drawn sans** (round terminals, "1" with flag and foot, narrow A). Candidates: Comic Sans MS Bold / Comic Neue Bold / a hand-lettered trace. Medium-heavy (stroke 18 % of cap).
- **T2/T3** = a **much heavier rounded "bubble" display sans** (stroke ≈ 23 % of cap, fully rounded terminals, closed counters, J with hook, M with pointed vertex). Closest free matches: **Fredoka (Bold/SemiBold condensed?)**, **Baloo 2 ExtraBold**, Sniglet ExtraBold; not Luckiest Guy (no slant). The wobbly baseline, size jitter (±8 %) and glyph overlaps indicate **lettering generated inside the image (AI image model) rather than set type** (?).
- Shared invariants: white, ALL CAPS, trailing period, one line, rounded, ≥ 17 % H cap height, contrast ≈ 19–20 : 1.

---

## 4. Colour & light

| Measure | T1 | T2 | T3 |
|---|---|---|---|
| k-means palette (7, by area) | #0C0C0C 46 % · #2A262B 33 % · #DCD9C9 7 % · #545256 6 % · #B3B0A2 4 % · #FEFEFE 2 % · **#C83A37 2 %** | #060506 48 % · #191311 21 % · #B2A190 11 % · #FCFCF8 10 % · #432D1D 5 % · **#F1CB7C 4 %** · #7F664D 2 % | #070508 46 % · #221720 21 % · #FDFDFD 9 % · #F1BAB1 7 % · #AC9D96 7 % · #812537 6 % · **#E9627C 3 %** |
| Background (dark) | #0D0D0D (luma 11–13); bed/blanket #1F232E–#2C2F40 cool navy | #050505–#070607 (luma 1–6) | #040404–#070607; bed #141720–#1F212D |
| Mean / median luma | 52.6 / 30.5 | 60.4 / 13.5 | 64.4 / 18.5 |
| % pixels luma < 30 | 49.8 % | 69.4 % | 62.6 % |
| Single accent hue | **red, hue ≈ 0–2°**, median #D93D3A, peak #F23937 | **amber/gold, hue 15–45°**, median #FDCA62, peak #F09A33 | **hot pink, hue ≈ 345°**, median #C42A48, peak #FE1C64 (+ magenta 315–330° and a thin blue/violet streak in the arc) |
| Saturated px (S>47 %, V>47 %) | **1.6 %** | **2.6 %** | **5.5 %** |
| Accent bbox | 841,384 – 1122,514 (only the digits) | 561,20 – 1045,714 (strip + rim light on hero) | 442,209 – 923,649 (phone, arc, brain, face spill) |
| Skin median (face) | #DCD9C8 (shade #B7B4A3) | #AC9E91 (lit #DAB996) | #F4B6AC (pink-lit; p10 #AF7A83) |
| Face vs. bg contrast | **13.7 : 1** | **7.2 : 1** | **11.2 : 1** |
| Brightest non-text pixel | (482,325) #F7F3E8 — on the forehead | (827,354) #FFFFD4 — rim light right beside the eye | (647,233) #FFFFFF — bubble highlight touching the skull |
| Glow / falloff | digit bloom: half-max ≈ 12–15 px, gone by ≈ 45–60 px | strip core 33–36 px at luma 220; left spill ≈ 50 px; **rim light 5–7 px** on every edge facing the door (head, arm, fist, guitar case) | phone edge R=243 → half at ≈ 15 px → ≈ 50 at 50 px → bg at ≈ 100 px; magenta spill on face, hands, sheets |
| Vignette | corners luma 9–13 vs centre 19 → none worth naming | corners 4–5 vs centre 15–24 — caused by light spill, not a vignette (?) | corners 4 vs 8–22 — same |

Cross-thumbnail pattern
- **One accent hue per thumbnail, and it is the light source.** Accent occupies only **1.6–5.5 % of pixels**; everything else is neutral (black, grey, cream, white). The accent changes with the topic (red alarm, gold door, pink dopamine) — the competitor does **not** keep red as a thumbnail brand colour.
- **Brightest non-text pixel is always on/next to the head** (≤ 100 px from the eyes): light is used to point at the face.
- Background is **near-black but not pure black** (luma 1–13); thumbnails are ~2.5–3× brighter on average (mean luma 53–64) than film frames (mean 11–45, median ≈ 20) because the subject fills the frame.
- Text is the most contrasted element (19–20 : 1), face second (7–14 : 1), accent third.

---

## 5. Rendering style vs. the film

| Trait | Film frames | T1 | T2 | T3 |
|---|---|---|---|---|
| Line | thin even grey/ink lines ≈ 2–3 px on 1270-wide frames; most props outlined in grey | thin black head outline ≈ 2–3 px; **tapered brush strokes for brows (≈ 20 px thick) and mouth (≈ 10 px)**; grey prop outlines (same as film) | **heavy black contour ≈ 7–8 px** (head left edge x 561–568); brows ≈ 13 px, tapered | **≈ 7 px black contour**; tapered brows; scribbly eye-bag strokes |
| Shading | flat fills, no shading | **2-tone cel**: skin histogram bimodal at luma 179 / 216 (hard terminator on the left of the head) | **soft gradient + rim light**: skin luma continuous 155→200, warm 5–7 px rim on lit edges | **soft airbrushed gradient + coloured light spill**; skin luma spread p5–p95 = 132–213 (std 28 vs 15 in T1) |
| Texture | none (bg grain std ≈ 0.0–0.1) | slight grain (std 0.42) | slight grain (0.40), painted wood door | slight grain (0.39), painterly bed sheets, cloudy brain |
| Eyes | dots / dashes, half-lidded | big solid black pupils, no highlight, under-eye crescents | **outlined white eyes + black pupils**, no specular highlight | outlined white eyes + small pupils, **smudged dark eye bags** |
| FX | glows on shadow figure only | bloom on digits | sweat drop, light leak, rim light | glowing particles, light arc, sparkle dots, exposed brain |
| Likely method (?) | vector/Moho-style limited animation | **bespoke redraw in the film's own vector style**, closer camera + extra cel shade (hand-made, high confidence) | **AI-assisted painterly illustration** (GPT-image/"cartoon" model look: heavy black outline, warm rim light, slightly mushy edges, generated lettering) — medium-high confidence | **AI-assisted** — airbrush eye-bags, particle bokeh, unstable small details (phone corners, finger shapes) — medium-high confidence |

Character design shifts in the thumbnails: head ≈ 1.0 aspect (round), face moved to one side of the head (3/4 view),
brows ≈ 4–6 % of head width thick and steeply angled (anger/worry readable at 168 px), mouth a short tapered
dash. Body simplified to a single soft mass; limbs become thick rounded tubes (not the film's stick limbs).

---

## 6. Mobile legibility (downscaled with Lanczos, files in `small/`)

At 168×94 the cap height becomes **16 px (T1), 19 px (T2), 20 px (T3)**, stroke ≈ 3–4.5 px.

| Survives at 168×94? | T1 | T2 | T3 |
|---|---|---|---|
| Text | **Yes** — "DAY 1." crisp | **Yes** — all 3 words readable | **Yes** — strongest of the three |
| Face emotion | **Yes** — angry V-brows + pupils still read | Partly — angry brow/eye reads; mouth lost | Partly — worried brow and eye bags faint; reads as "tired" more than "worried" |
| Object | **Yes** — red "5:00" still readable as digits | Yes as a **vertical gold line + hand**; door handle lost | Yes as a **glowing pink phone + pink brain**; bubbles merge into one pink arc |
| Lost | blanket, bed frame, nightstand | guitar case → black blob (reads as a cloak) | individual bubbles, pupils, finger detail |

At 320×180 everything above survives, including T2's sweat drop and T3's pupils. Rule extracted: **only three
things are designed to survive the feed size — the word, the brow-angle, and one glowing coloured shape.**

---

## 7. Measured template spec (1280×720) for a generator

| Parameter | Target | Tolerance | Source |
|---|---|---|---|
| Canvas | 1280×720, sRGB, JPEG q≥90 / PNG | – | all |
| Background | near-black, luma 2–13 (#050505–#0D0D0D); scene props dark navy/grey luma 20–60 | ≤ 15 luma | all |
| Text band | y 25 → 205 (top 4 %–28 % H) | ±15 px | all |
| Text content | 1–3 words, ALL CAPS, **ends with "."**, 1 line | max 13 glyphs | all |
| Text alignment | centred (offset ≤ 3 % W) when ≥ 2 words fill ≥ 80 % W; top-left (margin 30–40 px) for a short label | – | T2/T3 vs T1 |
| Text width | 80–93 % W for single words/phrases; ≈ 40 % W for a "DAY n." label | ±5 % | measured |
| Cap height | **140–155 px (19.5–21.5 % H)**; never < 120 px (17 % H) | ±8 px | T2/T3 (T1 125) |
| Stroke weight | 22–24 % of cap height (≈ 32–36 px) — rounded black/extra-bold sans (Fredoka / Baloo 2 ExtraBold class) | ±2 % | T2/T3 |
| Tracking | 4–8 % of cap height (5–12 px); word space 30–40 % of cap | – | measured |
| Text colour | #FDFDFD–#FFFFFF | – | all |
| Text outline | 8–10 px solid #000 stroke + 15 px soft black outer glow, **no offset** | ±2 px | T2/T3 |
| Text contrast | ≥ 15 : 1 vs local bg (measured 19–20) | – | all |
| Head size | width **270–345 px (21–27 % W)**, height **245–355 px (34–49 % H)** | – | all |
| Head position | centre x 35–55 % W, y 42–52 % H; head top 0–35 px below text bottom (may touch the text outline) | ±40 px | all |
| Eyes | centre within 42–61 % W, 44–57 % H; pupils ≥ 25 px; brows ≥ 12 px thick at ≥ 25° tilt | – | all |
| Gaze | points at the light object | – | 3/3 |
| Light object | centre x 66–80 % W, y 62–77 % H; area 3–10 % of frame | ±5 % | all |
| Accent | exactly **one hue**, 1.5–6 % of pixels, S ≥ 70 %, V ≥ 90 % at peak; topic-specific | – | all |
| Light behaviour | accent is emissive: bloom half-max 12–15 px, falloff to bg by 50–100 px; spill tints the face; 5–7 px rim light on edges facing it | – | T2/T3 |
| Face vs bg contrast | ≥ 7 : 1 (measured 7.2–13.7) | – | all |
| Brightest non-text pixel | on the face / within 100 px of the eyes | – | all |
| Hero line weight | 7–8 px black contour; inner features tapered 10–20 px | ±2 px | T2/T3 |
| Shading | 2-tone cel minimum (T1); soft gradient + rim light preferred (T2/T3) | – | – |
| Negative space | one flank ≥ 14 % of frame left at luma ≤ 15 | – | all |
| Badge zone | nothing important in x ≥ 1150, y ≥ 640 | – | all |
| Hard no | no second character (no shadow antagonist), no arrows/emojis/frames, no letterbox bars, no film "DAY" counter at film size | – | 3/3 |
| Feed test | at 168×94: word readable, brow angle readable, accent shape readable | pass/fail | §6 |

### Corrections to `research/10-packaging-strategy/README.md` (written before these thumbnails were known)
- "Hero vs red shadow on black" — **wrong**: 0/3 thumbnails show the shadow antagonist; each shows only the hero + one lit object.
- "Text: red, lowercase, handwritten shadow line; never the title word" — **wrong**: text is **white, ALL CAPS, heavy rounded, with a period**, and in T3 it *is* the title word (DOPAMINE.).
- "Font size ≥ 1/8 of height" — too small: measured **1/5.7 – 1/4.8** (17–21 % H).
- "Thin dark outline" — T1 yes (≈ 2–3 px); T2/T3 use a thick 8–10 px black stroke.
- "Hero ≥ 30 % of frame height" — confirmed and exceeded (head alone 34–49 %).
- "One red accent is the brand" — partly wrong: one accent per image, but its **hue follows the topic** (red / gold / pink).
- "Bespoke render, not a screenshot" + "keep bottom-right clear" — confirmed.
