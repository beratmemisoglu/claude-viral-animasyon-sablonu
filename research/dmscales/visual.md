# dmscales: visual design and typography spec (build-ready)

Sources: 5 videos (VQvIV__toUk 2026-06-13, EQUn6IVAgCg 2026-05-16, AGkRkNuhO_o 2026-05-04, -fS8na576Jc 2026-04-14,
N-q-XLQymnU 2026-04-01), their thumbnails, and 1 fps sheets. All measurements come from full-resolution frames pulled with
ffmpeg into `research/dmscales/work/visual/<id>_<t>.png`, read with numpy. Reference images are in `reports/visual_refs/`.

---

## 0. Critical: the canvas is 4:3, not 16:9

**All 5 videos are 1440x1080 (4:3, square pixels, AV1).** That includes "The Entire Shorts Algorithm Explained" and the
TikTok one. There is **no vertical video** in the sample. Frame rate is 60 fps (VQvIV, AGkR, -fS8, N-q) or 30 fps (EQUn6).
YouTube shows them pillarboxed. The 4:3 frame is part of the look.

- **Recommendation:** render at **1440x1080**. Every number below is in px at 1440x1080, with % of frame where it helps.
- If 16:9 is required: use a 1920x1080 white canvas and treat x = 240..1680 as the "frame", so x_1920 = x_1440 + 240.
  Never scale up to fill the width: the empty white sides are cheap and keep the composition.
- For 9:16 Shorts (not in the sample, so this is an extrapolation): stack the same 1440-wide composition scaled to
  1080 wide (factor 0.75), with its centre at y 860 of 1920.

## 1. Canvas

| property | value | evidence |
|---|---|---|
| Background | **#FFFFFF** flat (the three May-June videos); **#FCFCFC** flat (the two April videos) | 100x200 patches have std 0.00, corners all equal |
| Texture / grain / vignette | **none** (std 0, all four corners identical) | every frame measured |
| Edge artefact | VQvIV has a 1-2 px dark line on row 0 (#363636, #E7E7E7): an export artefact, don't copy it | VQvIV_47.5 |
| Ink black (text) | **#000000** | text pixel modes are (0,0,0) |
| Ink black (drawings) | **#1E1E1E** (30,30,30); #202020 in N-q | figures, crowds, phone outline |
| Alternate black scene | pure #000000 full frame for a "viewfinder reveal" (white corner brackets) | VQvIV_148.5 |

**Safe area, as measured.** Text lines never go past x 124..1299 (widest line is 1176 px = 82% W), so the side margin
is at least 124 px (8.6%). Media goes as far as x 92..1346 (margin 92 px = 6.4%) and y 62..1017 (margin 62 px = 5.7%).
Use: **text safe = 120 px sides, 70 px top/bottom; media safe = 90 px sides, 60 px top/bottom.**

## 2. Typography

### 2.1 Font identification: Arial (true italic), confirmed at pixel level

I rendered `ariali.ttf` at 97 px over "all it takes" (VQvIV_0.5) and got **IoU 0.88**; the only misses were 1 px
anti-alias fringes (see `work/visual/z_overlay.png`). Width and height also match on 15 other lines, always within 1-3 px.
The tells: straight diagonal leg on R, a slanted cut on top of t, a slanted e terminal, and G with no spur. That is
Arial, not Helvetica. It is a true italic, not an obliqued roman. Segoe, Verdana and Calibri all miss on the
height-to-width ratio.

- **Video font: Arial**, from `C:\Windows\Fonts`: `arial.ttf` (Regular), `ariali.ttf` (Italic), `arialbd.ttf` (Bold),
  `arialbi.ttf` (Bold Italic). All four are present, so headless Chrome on this machine uses them directly with
  `font-family: Arial`.
- Fallback stack: `Arial, "Arimo", "Liberation Sans", Helvetica, sans-serif`. Arimo (Google Fonts) and Liberation Sans
  are metric-compatible clones.
- **Thumbnail font is different: Roboto** (Bold, Bold Italic, Regular). The tells are the straight-tailed y and the
  shape of the "no one" glyphs. It is not in C:\Windows\Fonts, so load Roboto 400/700/700i from Google Fonts. The
  Windows fallback is Segoe UI Bold.

### 2.2 Text tiers (font-size = Arial em size in px at 1080 tall)

Sizes were found by matching the rendered ink width to the real ink width (`work/visual` frames; script in the session
scratchpad).

| tier | use | style | size px (% H) | measured examples |
|---|---|---|---|---|
| H0 hero | 1-4 words, alone, often the "punch" | Italic (May-Jun) or Bold Italic (Apr) | **90-100** (8.5-9%) | "all it takes" 97 (VQvIV_0.5), "HOW TO FIX:" 90 (N-q_16.5), "TRUST SCORE:" 92 Bold Italic (N-q_29.5), "everything i covered" ~74 + underline (EQUn6_1.5) |
| H1 tracked caps | section statements ("VIEWERS GO ON THE PLATFORM / LOOKING FOR ONE THING", "CREATORS PERSPECTIVE", "BECAUSE CONTENT IS JUST LIKE BUSINESS") | **Regular**, ALL CAPS, **letter-spacing +0.10..+0.12 em**; black words upright, red words italic | **62** (cap 46 px) | VQvIV_29.5 lines at y 165-211 / 224-269, VQvIV_49.5 |
| H1b tracked lowercase | AGkR (TikTok video) body | Regular upright, lowercase, letter-spacing **+0.08 em** | 60-78 | "the first thing / that happens" 78 px (AGkR_2.5) |
| B1 body line (the default) | the narration as a caption, 1-2 lines | **Italic** (May-Jun) / **Bold Italic** (Apr) | **62** (5.7%) | "this is another reason why you should" 62, "always go branded" 63, "the most important thing EVER" 61, "rather than risking showing yours" 62, "- enable third level feature eligibility" 62 BI |
| B2 secondary | second line under a hero, list items | Italic | **43-51** | "you knew about YouTube away" 51, "- aged channel" 49, "because in the next 5 minutes" 46, "-no gatekeeping" 43 |
| B3 list (dense) | two-column inventory | Bold Italic | **~38**, line pitch 39-40 | EQUn6_4.5 |
| N1 parenthetical | "(channel thats a couple years old, ...)" under a bullet | Italic, black; or Bold Italic grey **#525252** | **27-36** | N-q_20.5 (27 px lines), "(this will get you out of view jail ...)" 36 BI; grey note in N-q_29.5 31 BI |
| N2 footnote | "*not my screenshots", "*this is my thousands of hours ...", "*because then i appeal to more viewers" | Italic, starts with **"*"**, black or with a red keyword | **27** | N-q_13.5 (y 891-917), EQUn6_2.5 (y 330-355) |
| Q speech | quotes from viewers or the brain: "i really wanna watch a minecraft video ..." | Italic, wrapped in **straight " "** (sometimes curly “ ” in VQvIV crowd labels) | 50-62 for the top quote, ~30 for small labels ("Watch my video!") | VQvIV_34.5, VQvIV_57.5 |

**Line spacing is tight:** baseline-to-baseline is **0.95-1.0 em** for B1 (62 px font, 60 px pitch: EQUn6_301.5) and
about 0.9 em for Bold Italic B1 (N-q_29.5). Short notes are looser: about 1.15 em for 27-31 px text.

**Paragraph gaps:** hero to definition about 60 px (N-q_29.5: 430 to 489); definition to grey note about 28 px; bullet
to its parenthetical about 8 px; one bullet group to the next about 30 px.

**Alignment: everything is centred on x = 720** (measured cx 712-726 on every centred line). Multi-line blocks are
centred line by line (ragged both sides). The only exceptions:
- the **staircase list**: each new bullet starts further right (VQvIV_12.5: lines start at x 411, 648, 705, 753, so
  each step is about 50-60 px and the block drifts right);
- the **two-column list**: left-aligned columns at x 248 and about 770 (EQUn6_4.5);
- **figure-left layouts**, where text is centred in the right zone (cx about 910-920).

**Maximum line width:** 1176 px (82% W) for bold body; most lines run 650-1050 px. Lines wrap at about 40-55
characters for B1.

**Bullets:** a hyphen, either "- text" with a space (N-q, VQvIV_138.5 paragraphs) or "-text" with no space (VQvIV "-no
gatekeeping", EQUn6 list, AGkR "-your device"). There are no bullet dots. Never use a real bullet glyph.

**Case:** mostly **all lowercase**, including "i" and the start of sentences ("i'mma cut all the BS"). Proper nouns are
inconsistent ("YouTube", "youtube"). ALL CAPS is used for (a) colon headers, (b) tracked-caps statements, (c) single
stressed words inside a lowercase line.

**Colon headers:** "HOW TO FIX:", "TRUST SCORE:", "ZERO VIEW JAIL:", "PART 1: AUDIENCES EXPLAINED". All caps, ending in
":", hero size, with a definition or bullets below.

### 2.3 Underline
- Thickness **3-4 px at 62-74 px** (0.05-0.065 em). Offset: the top of the bar sits **0.21 em below the baseline**,
  at descender depth, so it touches the g, y and p tails (-fS8_76.5: baseline about 555, bar 568-571).
- **Same colour as the word** (red bar under a red word). The bar spans the word only. On the header "everything i
  covered" it spans the whole header, with each segment in its word's colour (EQUn6_1.5, y 317-319).

## 3. Colour palette (measured pixel modes)

| token | hex | used for |
|---|---|---|
| bg | **#FFFFFF** (alt #FCFCFC) | canvas |
| text | **#000000** | all typed text |
| text-red | **#FF0000** | emphasis words in typed text (pure red, in every video) |
| ink | **#1E1E1E** | stick figures, crowds, bust people, phone outline, thought dots |
| marker-red | **#E5161C** (229,22,28) | hand-drawn arrows, X-outs, circled metrics, play-badge on chests |
| neon-green | **#00FC16** (text, $ sign) / **#08FC00** (growth line) | "positive" side: DEMAND, "too", money, up-trend |
| note-grey | **#525252** (= black at about 67% over #FCFCFC) | secondary parenthetical under a definition |
| yellow | **#FCD400** (burst lines), #FCC000 (bulb clipart) | "excitement" burst around a phone, idea bulb |
| drool-blue | #0898FC | one-off doodle detail (EQUn6_16.5) |
| UI-dark | #0F0F0F / #272727 | the dropped-in YouTube and Studio dark screenshots (not drawn by us) |

**No gradients, no shadows, no outlines on text, no highlight boxes** in-video. The only "box" is the screenshot itself.
Faded or ghost text (previous line at 15-30% opacity, red turning pink) shows up only during transitions; the motion
analyst covers that.

## 4. Emphasis grammar

1. **Red = the concept word of the line.** Usually 1, at most 3, red words per line: the noun or verb the sentence is
   about ("new channel", "push", "channel data", "hidden", "trust", "enjoy", "niche", "flop", "viral", "audience",
   "algorithm", "competition"). In list items the red word is the payload after a function word ("-no
   **gatekeeping**", "-your **internet connection**").
2. **ALL CAPS inside a lowercase line = vocal stress or an intensifier**, almost always red: EXACTLY, MUCH, EVER, REALLY,
   MANY, VERY, ONE, FOR, EVERYTHING. A caps word in black happens when the stress is on a non-concept word ("BS",
   "VERY easy").
3. **Underline = "you" or "yours", or the word that changes the meaning**: "showing **yours**", "MUCH **easier**",
   "more **context**", "**your video**", "**FOR**", the header "everything i covered". It is often combined with red.
4. **Bold:** the April videos use Bold Italic as the default body (N-q, -fS8). There, emphasis is red only, and
   regular-weight italic shows up for asides. The May-June videos use Regular Italic for the body and keep Bold Italic
   for the **current** bullet or definition in a growing list, and for dense lists. Rule for our style: **default
   Italic 62; Bold Italic for the active item, colon headers' definitions and lists.**
5. **Green = the positive or desired counterpart of a red word** ("SUPPLY" in green vs "DEMAND" in red; "*VIEWERS ARE
   THE DEMAND" green under "*SUPPLY IS YOUR COMPETITON" red; "your thumbnail matters **too**"). Use it rarely: about one
   scene in 30.
6. **"*" prefix = an aside or footnote** ("*not my screenshots", "*killer video", "*viewer spends more time on youtube").
   The asterisk also opens on-screen definitions under a visual.
7. **Parentheses = a sub-explanation**, always one tier smaller, directly under its bullet.
8. **Shrinking history** (N-q_20.5): when a new bullet arrives, the earlier bullets and their notes drop to about 45%
   size (49 to 25 px, notes to 20 px), and the new item comes in at full B1 Bold Italic with its red keyword. The header
   stays at H0.

## 5. Drawings (procedural spec)

All drawings: a single colour **#1E1E1E**, **round caps and round joins**, uniform marker width, no fill except eye dots,
no shading. They should look like a drawing-tablet brush: a slight wobble, about 1-2% of length, low frequency (2-3
waves per stroke). Strokes overshoot or overlap at closures. Head loops are not perfectly closed: they overlap by 5-15%
of the stroke length, with a small tail.

### 5.1 Main stick figure ("marker guy")
Measured on VQvIV_32.5 (figure bbox 231-471 x 352-833; full height **H = 481 px = 45% of frame height**):

| part | spec (relative to H) | px at H=481 |
|---|---|---|
| stroke width | **0.050 H** (equals 0.105 x head width) | 24 |
| head | "gumdrop" or egg: narrower and rounder at top, widest at about 65% of head height, broad flat-ish bottom; width **0.48 H**, height **0.43 H** | 230 x 208 |
| eyes | filled dots, diameter 0.042 H, centres at 36% of head height, spaced 0.12 H apart (about 25% of head width), slightly right of head centre when the figure faces right | 20 px dots, 58 px apart |
| mouth | open arc, width 0.12 H, centred at 66% of head height | 58 px |
| torso | single near-vertical line from the bottom-centre of the head, length **0.37 H**, may lean 3-5 deg | 180 |
| arms | two straight strokes from a shoulder point 0.04 H below the head, going down and out about 30 deg from the torso, length about 0.30 H; no hands. Holding pose: one arm bent across the body to a held object | |
| legs | inverted V from the hip, each about 0.23 H, about 25 deg from vertical, feet about 0.21 H apart; no feet | |
| thought dots | 2 filled dots (0.037 H and 0.029 H) above and right of the head, rising diagonally | 18 and 14 |

**Face catalogue** (all built from 2 dot eyes plus 1 mouth stroke):
- neutral: short flat line;
- smile: shallow up-arc, often offset to one side (smug: AGkR, -fS8_64.5);
- frown: down-arc (VQvIV_32.5, N-q_0.5);
- big grin: open D-shaped mouth, outlined, white inside, with a tooth line (VQvIV_34.5 "wait, this is EXACTLY what i
  want");
- worried: eyes plus a small squiggle;
- drooling (EQUn6_16.5): blue drip from the mouth.
- Eyebrows are not used.

**Poses seen:** standing with arms down (default); holding a phone in front of the chest (phone = rounded rectangle
about 0.25 H x 0.45 H, 4-6 px #1E1E1E outline, white or a screen image inside, tilted 10-20 deg); tiny squat or arms-up
"ꆜ" pose for a mini icon (VQvIV_49.5, 173 x 185 px); shaking or excited with a yellow burst (#FCD400 radial ticks,
12-16 ticks, each about 0.08 H long and 8 px wide, in a 200-deg fan around the object: AGkR_20.5).

**Scale variants:** hero figure H 420-520 (40-48% of frame height); mid figure H about 260; tiny "corner commentator" H
about 90-110 (AGkR_9.5, beside text at the right edge, about x 1300).

**Older thin variant** (EQUn6_16.5): stroke 9-12 px, a big round head about 240 px, and a thought cloud (bumpy closed
outline with 3 trailing circles) holding 30 px italic quoted text. Use it only for "naive belief" bubbles, then
X-out the bubble with two marker-red strokes (14 px).

### 5.2 Bust people ("creators" / competitors) (VQvIV_57.5)
- Size about 150 x 170 px each. Stroke **22-24 px** #1E1E1E (very heavy relative to size).
- Head: a horizontally squashed oval, about 95 x 70 outer, so the white inside is a small slot. A short tick or notch
  hangs from the bottom-centre (neck).
- Body: an arch shaped like "A" or a capital omega, starting under the head and spreading down to about +/-75 px. The
  ends are the arms, with round caps.
- Chest badge: a **marker-red rounded play-wedge** (triangle pointing right, about 55 x 40, #E5161C, soft corners) =
  "a creator".
- Layouts: a **cluster of 8** in two overlapping rows (back row of 4 raised by about 0.35 x bust height, front row of 4
  overlapping by about 25%, cluster about 600 x 340, centred) plus **8 singles on a 3x3 ring** (corners and edges at
  about x 240/720/1200 and y 160/560/930), each with a 30 px italic quoted label ("Watch my video!") about 20 px above
  its head.

### 5.3 Crowd ("audience" / "viewers") (VQvIV_22.5, EQUn6_21.5, VQvIV_29.5)
- Cluster bbox about **780 x 515 px (54% W x 48% H)**, centred (or under a caption at y about 165-270).
- About **18-22 heads**. Head = a loose circle or oval, diameter 60-140 px. **Stroke 14-16 px** (lighter than the
  hero figure).
- Heads overlap. Each head is filled white so it hides heads behind it. Back rows sit higher and slightly smaller.
- Each head has 1-2 shoulder arcs: a short curve leaving the bottom of the head and hooking down, about 0.6-0.9 x head
  diameter long, ending in a little curl.
- 1-3 front heads are separate and smaller, with full shoulders (bottom right), so the cluster reads as "a crowd" and
  not a blob.
- Loops are not closed perfectly: the start and end overlap with about 10 px tails.

### 5.4 Arrows and marks (marker-red #E5161C, round caps)
| item | stroke | geometry | refs |
|---|---|---|---|
| standard arrow | **20-24 px** | about 230 x 85 bbox; shaft is a gentle arc (sagitta 10-20% of length) or a J-hook that swoops then turns up; open chevron head drawn as one continuation stroke, each barb **30-40% of shaft length at +/-40 deg** | EQUn6_23.5 (703-937 x 716-799) |
| hero arrow | **35-40 px** | about 265 x 210, a gentle S/arc pointing at a media inset from empty space | AGkR_3.5 (240-505 x 351-560) |
| small connector arrow | 6-8 px | straight down, about 45 px, between two lines of text (cause, then effect) | -fS8_60.5 |
| black arrow | 20 px #1E1E1E | same shapes, for a neutral pointer ("viewjailed") | N-q_136.5 |
| circle-out | 6-10 px | a loose ellipse around a number, 1.1 turns, ends overshoot | thumbnails, VQvIV_148.5 |
| X-out | 12-14 px | two long crossing strokes over the object | EQUn6_18.5 |
| growth line | **about 30 px #08FC00** | a zig-zag polyline with sharp miter joins, from bottom-left off-frame to top-right off-frame, drawn over or behind media | VQvIV_134.5 |
| scatter doodles | 8-10 px red or black | small circles, squares, x's, triangles flung around a title (a "FU-"/glitch accent) | VQvIV_15-20 |

### 5.5 Clipart (not drawn)
Photoreal or 3D cut-outs with no outline and no shadow, 150-260 px: brain, light bulb, 3D emoji, platform logos (YT
play, Shorts, TikTok disk), a neon-green "$". They are placed at about 1/3 W next to a figure, or alone in the centre
with a footnote. For our build: our own flat or 3D icons, same scale, no outline.

## 6. Media inserts (screenshots, thumbnails, video)

- **Raw rectangular crops: corner radius 0, no border, no shadow**, placed flat on white. Dark UI screenshots carry
  their own #0F0F0F/#272727 fill. A YouTube video card keeps its native rounded corners (about 12 px) and dark card.
- Single centred insert: **58-64% W** (840-920 px wide), centred at (720, 539). Examples: N-q_13.5 872 x 618; EQUn6_9.5
  webcam 840 x 474.
- Insert with caption below: the insert is raised so the group centres. The caption (B2/N2) sits **36-45 px under the
  bottom edge**, centred.
- Large grid or screenshot: **87% W** (1255 x 619 at y 63-681), with a 3-5 line B2 caption paragraph below (y 723-994,
  about 40 px text, 45 px pitch) (VQvIV_138.5).
- Side-by-side: **figure or object on the left third, media on the right** (media about 40-45% W, e.g. x 650-1260); a
  quote B1 across the top at y about 235-290 (VQvIV_34.5, -fS8_70.5).
- Vertical phone recordings (TikTok): about 310 x 665 (21% W x 61% H) at the left (x 110-420), text staircase to the
  right (AGkR_9.5).
- **B-roll** (gameplay "talking-head substitute", EQUn6): 16:9 inset 1150 x 648 (80% x 60%) centred, or 750 x 518 with
  a two-line caption below (y 840-1000). Chapter cards are a caption under the inset: "PART 7: HOW TO **IMPROVE** + GO
  **VIRAL**" ("PART n:" upright-italic black, title words bold, the key word red).
- Labels: "*not my screenshots" 27 px italic under the insert; "@channel" small label above the top-left of grids
  (VQvIV_143.5).
- Viewfinder reveal: a black frame, white 4 px corner brackets about 120 px long at about 15% insets, the media centred
  (VQvIV_148.5).

## 7. Layout grid

- Horizontal: a single centre axis at **x = 720**. Two-zone layouts split at about x 560: left zone centre x about 300-370
  (figure), right zone centre x about 900-1000 (text or media).
- Vertical anchors: **centre line y = 540** (a single line's ascender-to-baseline box is centred there, so the baseline
  is about 540 + 0.36 x size). Top caption band at **y 160-300** (15-28%). Bottom caption band at **y 840-1000**
  (78-93%).
- A text-only block is centred as a whole on y about 540 (N-q_20.5: block 338-751, centre 545).

## 8. Scene template catalogue

Coordinates are at 1440x1080. "ref" files are in `research/dmscales/reports/visual_refs/`; "frame" files are in
`research/dmscales/work/visual/`.

| # | template | layout (measured) | reference |
|---|---|---|---|
| T01 | **Single line, centred** (built up word by word) | B1 62 px or H0 97 px, cx 720, box centred on y 530-541; 1-2 red words | ref 01; frame VQvIV__toUk_0.5, -fS8na576Jc_76.5 |
| T02 | **Hero word + subline** | "EVERYTHING" H0 70 red (y 506-559) then 23 px gap, then B2 51 px (583-629) | frame VQvIV__toUk_8.5 |
| T03 | **Colon header + growing bullets (shrinking history)** | H0 90 "HOW TO FIX:" at y 338-404; old bullets 25 px plus notes 20 px; new bullet B1 BI 62 (y 607-665); its parenthetical 36 BI (682-751) | ref 02; frames N-q-XLQymnU_16.5/17.5/20.5 |
| T04 | **Definition card** | "TRUST SCORE:" H0 BI 92 (red + black) at y 360-430; definition B1 BI ~54, 2 lines (489-591); grey #525252 note 31 BI (619-690) | ref 03; frame N-q-XLQymnU_29.5 |
| T05 | **Staircase list** | lead line B2 46 at x 411; each "-item" B2 43 indented about 55 px further right, about 40 px pitch; red payload word | frames VQvIV__toUk_12.5; AGkR (ref 11) tracked version |
| T06 | **Tracked-caps statement over an illustration** | 2 lines of H1 62 px +0.11 em at y 165-211 and 224-269; crowd or figure below (y 387-930) | ref 04; frames VQvIV__toUk_29.5, _49.5 |
| T07 | **Figure left, text right** | figure H 425-445, centre x 300-370, y centre 540; text B1/B2 centred around x 910, baseline near figure mid-height | frames N-q-XLQymnU_0.5, AGkRkNuhO_o_2.5 |
| T08 | **Quote on top + reacting figure + media** | quote B1 at y 235-290; figure x 230-470, y 317-834; media x about 650-1260, y about 393-811; the figure's face changes with the media | ref 05; frames VQvIV__toUk_32.5, _34.5 |
| T09 | **Quote + object + figure with phone** | 2-line quote at top (y about 120-180); brain clipart left of centre; figure holding a phone right (H about 500) | ref 06; frame -fS8na576Jc_64.5 |
| T10 | **Centred screenshot + footnote** | insert 60% W centred; "*not my screenshots" N2 27 px 43 px below | ref 08; frame N-q-XLQymnU_13.5 |
| T11 | **Media + question + marker arrow + dashed answers** | grid 919 x 589 at top-left (x 92-1010, y 102-690); "what niche is this?" B1 at y 714-790; J-arrow right of it pointing up to the grid; answers "-commentary?" B3 30 px stacked below at x 140 | ref 09; frame EQUn6IVAgCg_25.5 |
| T12 | **Big grid + paragraph caption** | 87% W grid y 63-681; 3-5 line B2 caption with red key phrases, y 723-994 | frame VQvIV__toUk_138.5 |
| T13 | **Two-column inventory** | header H0 74 underlined (y 252-320), N2 footnote (330-355), then two left-aligned Bold Italic 38 px columns at x 248 / about 770, pitch 39 px, a red word at the end | ref 10; frame EQUn6IVAgCg_4.5 |
| T14 | **Crowd = audience** | crowd 780 x 515 centred (or under a 2-line caption, "the people you're making it **FOR**") | frames VQvIV__toUk_22.5, EQUn6IVAgCg_21.5 |
| T15 | **Creators field** | 8-bust cluster centred with a quote label; 8 single busts on a 3x3 ring with "Watch my video!" labels; final caption B1 at the bottom (y 860-990) | ref 07; frames VQvIV__toUk_57.5, _59.5 |
| T16 | **Icon + footnote definition** | clipart about 240 px at the centre, y 305-666; 3-line N2 "*IDEAS, as well as niches, ..." about 30 px at y 774-870 with red keywords | frame VQvIV__toUk_51.5 |
| T17 | **Logo flow** | icon, black arrow, icon on y = 540 (Shorts logo, then arrow, then YT logo), each about 200 px | sheet frames/EQUn6IVAgCg/sheets/sheet_0300s.jpg (t 328-329) |
| T18 | **B-roll inset + subtitle / chapter label** | 16:9 inset 80% W centred, or 52% W with a caption 2 lines below (y 840-1000); "PART n: TITLE" label | frames EQUn6IVAgCg_621.5, _610.5, _9.5 |
| T19 | **Contrast pair** | tiny figure (about 120 px) left at x about 230; two stacked words in Bold Italic tracked 0.12 em, about 100 px: green "SUPPLY" over red "DEMAND" | frame VQvIV__toUk_44.5 |
| T20 | **Growth-line overlay** | a neon-green zig-zag crossing the frame over a media card and caption | frame VQvIV__toUk_134.5 |
| T21 | **Viewfinder reveal** | black bg, white corner brackets, the hero card centred | frame VQvIV__toUk_148.5 |
| T22 | **Cause, then effect note** | figure left (H about 300); two "*" lines B2 at the right with a small red down-arrow between them | frame -fS8na576Jc_60.5 |

## 9. Thumbnails (.webp, 1280x720)

4 of 5 thumbnails follow one formula; VQvIV is the exception.
- **White background** (#FFFFFF, 52-91% of the pixels are white).
- **Left 55-60%:** a dark analytics or Studio card (a views graph or "Key metrics"), tilted 0 deg, no shadow. The key
  number is **circled with a marker-red hand-drawn ellipse** (stroke about 8 px).
- **Right 40%:** two words, stacked and staggered. Word 1 is black **Roboto Bold**, lowercase, about 100-110 px. Word 2
  is **red #FF0000 Roboto Bold**, slightly larger and offset right and down by about half a word ("stupid / easy",
  "tiktok / explained", "easy as / f*ck").
- A **marker-red curled arrow** (stroke about 10 px, open chevron head) runs from under the red word back to the
  circled metric.
- Variant (EQUn6): a top headline with red Bold Italic "no one" plus black Regular "will tell you this...", over a fan
  of 6 overlapping analytics cards.
- Variant (VQvIV): a full-bleed dark analytics screenshot with centred white Roboto Bold "you're **one video** away"
  (red middle, small dark drop shadow) and a red down-arrow at the chart's knee.
- No faces, no stick figures, no channel branding in thumbnails.

## 10. Build notes for the "dmscales" engine

- Text renderer: `ctx.font = "italic 62px Arial"` and similar. Implement letter-spacing (canvas `letterSpacing` in Chrome
  99+). Words are coloured individually, so lay out each line word by word and measure with `measureText`. Centre each
  line on x 720. Use line-height 0.97 em (Italic) or 0.9 em (Bold Italic).
- Token set: `{bg:#FFFFFF, text:#000, red:#FF0000, ink:#1E1E1E, marker:#E5161C, green:#00FC16, grey:#525252,
  yellow:#FCD400}`.
- Strokes: `lineCap = lineJoin = "round"`. Widths are figure 0.05 H, crowd 15, bust 23, arrow 22 (hero 36). Add
  deterministic wobble (seeded noise, amplitude 1.5% of segment length) and closure overshoot for the hand-drawn feel.
- Media frames: draw as plain rectangles, with radius 0 except YT cards (about 12 px).
- Do not add drop shadows, gradients, paper texture or vignette anywhere: flatness is part of the style.
