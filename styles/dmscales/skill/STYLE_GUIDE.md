# Dmscales - style guide

Read this before building anything. Numbers are px in the REFERENCE frame (1440 x 1080, origin top-left, y down); scenes
pass them through `P(x, y)` (models.js), which centres that frame in 16:9 and scales it 0.75 for 9:16 (type keeps 0.9).

## In one paragraph
A fast, plain explainer on a flat white page. The narration's own words appear as Arial italic lines centred on one axis,
popping in on the spoken word, with one or two red keywords. Colon headers ("HOW TO FIX:") grow lists item by item.
Asterisk footnotes add what the voice doesn't say. Hand-drawn marker figures, crowds and red arrows carry the
"you / viewers / creators" beats; the member's REAL screenshots and video clips carry the proof. Hard cuts on clause
starts, a new thing about every second, no camera moves, no grain, no shadows.

## How a video is made from the member's script and files
1. **Files first.** The member's screenshots and video clips go in with
   `node .claude/skills/<this skill>/scripts/add_media.mjs <project dir> <file> [<file> ...]` (pictures: png jpg webp;
   video: mp4 mov webm, frames at 15 fps, its sound is not used). Read `assets/media/media.json` for the names, sizes,
   frame counts and seconds. Look at every file (Read the picture / a few frames) and know what it shows before using it.
2. **Map every narration clause to a template** (table below). A clause that names or points at something the member
   gave ("this", "here", "like this", a number, a channel, a result) gets THAT file on screen, with a red arrow or circle
   on the part that matters. Never draw or invent a screenshot, a chart of real data, a channel page or a number: use the
   member's file, or a text card if there is none.
3. **Cue everything on the voice.** A shot starts on its clause's first word (`cue('word', near)`, or `words(src, near)`
   for word-by-word builds). Pops land on their word; a figure or picture arrives in the pause before its clause.
4. **Check** each scene file (check_preview), then look at frames at every entrance.

## Templates (the reference's scenes; use these, in these proportions)
Screen time to aim for: proof media 40-55 %, text cards ~35 %, figures / crowd / creators ~15 %.

| # | template | when the narration... | build |
|---|---|---|---|
| T01 | single line | says one clause | `pops(S, say(null, 'all it {takes}', { size: 62, ...xy(P(720, 540)) }), words(src, near))`; first word `lead: true` on a scene's first line |
| T02 | hero word + subline | punches one word | `say` 97 px (`T.hero`), then a 48 px line 70 px under it |
| T03 | header + growing list | lists steps / fixes | `heading(S, 'HOW TO {FIX}:', [{ src: '- aged channel', at, note: '(...)' }, ...], { at })`; the hit's grammar `{ shrink: true }`: each new item big at the bottom, the earlier ones drop to 45 % above it |
| T04 | definition card | "this is called X" / "a metric called X" | `say` 92 bold `'{TRUST} SCORE:'` at y 395, definition 54 bold (2 lines) at y 535, grey note 31 bold `color: GREY` at y 640 |
| T05 | staircase list | rattles off short items | `say(null, 'line1\nline2\nline3', { align: 'left', indent: 55, size: 46 })` at x 411..; or one say per line, each popped on its word |
| T06 | tracked caps over a picture | states a big truth | `say(null, 'LINE ONE\nLINE {TWO}', { size: 62, italic: false, track: .11 })` at y 190-250, crowd / figure below |
| T07 | figure left, text right | "when you..." (the viewer acts) | `figure(null, { h: 440, face, pose, ...xy(P(330, 540)) })` + line centred at x 930 |
| T08 | quote + figure + media | a viewer thinks something about a video | quote 62 at y 260, figure x 350, member's picture right half (`media`, w 600 at x 955) |
| T10 | screenshot + footnote | shows proof | `media(null, key, { w: 870, ...xy(P(720, 520)) })` + `'*not my screenshots'` (27 px) 43 px under it |
| T11 | media + question + arrow | asks "what is this?" about a picture | picture top-left (x 92-1010), question 62 under it, red `mark('arrow')` pointing up at it, `-answers` 30 px below |
| T12 | big screenshot + caption | walks through a big screenshot | `media` w 1255 at y 63-681, 3-5 lines of 40 px under it with red key phrases |
| T13 | two-column inventory | lists many things at once | header 74 px underlined (`_everything_ i covered`), footnote 27, two left-aligned bold 38 px columns at x 248 / 770, 39 px pitch |
| T14 | crowd = audience | says viewers / audience / people | `crowd(null, { w: 780, h: 515 })` centred or under a T06 caption; enter `'scale'` |
| T15 | creators field | competition / other creators | 8 `bust()` in two overlapping rows + singles around with `"Watch my video!"` 30 px labels |
| T16 | icon + footnote | a single object / idea | the member's icon picture ~240 px centred (`media`), 3-line footnote 30 px under it |
| T17 | logo flow | A leads to B | picture, black `mark('arrow', { color: INK })`, picture on y 540 |
| T18 | clip inset + label | gameplay / example footage, a chapter | `clip(S, name, { w: 1150 })` centred, or w 750 + caption; chapter: `'PART 3: HOW TO {IMPROVE}'` under it |
| T19 | contrast pair | supply vs demand, A vs B | tiny figure (h 120) left, two stacked bold tracked words ~100 px: `{g:SUPPLY}` over `{DEMAND}` |
| T22 | cause then effect | "X, so Y" | figure left (h 300), two `*` lines right with `mark('down')` between them |
| C1 | phone clip + side text | a vertical example (Short / TikTok) | `clip(S, name, { h: 790, r: 28, ...xy(P(400, 540)) })`, bold 48 px lines at (1030, 430/480), small red arrow pointing at it; then `move(S, clip, t, { ...P(720, 430), s: .8, frames: 6 })` + footnote at y 900 |
| T13 | two-column inventory | lists many topics | `columns(S, '_{everything} i covered_', leftItems, rightItems, { at, times, foot })` |
| CMP | compare cards | two sides (viewer vs creator) | `compare(S, [{ label: 'Viewer', items: ['- loves {animals}'] }, { label: 'Creator', items }], { at, times })` |
| CLD | thought cloud + X | a belief that is wrong | `figure` left + `cloud(null, 'a niche is the content you make', { w: 420, h: 280 })` right, then `enter(S, mark(null, 'x', ...), t)` on the word that kills it |
| CRV | explanatory curve | the shape of retention / growth / a drop | `curve(S, { shape: 'bad' / 'good' / 'drop' / 'rise' / 'flat', at })` + label 52 bold + footnote; a shape, never data |
| GRW | growth line | a win, going viral | `growth(S, { at })` built first, the member's card + a question over it |
| BST | burst | excitement on a phone | `figure(..., { pose: 'phone', face: 'grin' })` + `enter(S, burst(null, { r: 120, arc: 220 }), t, 'scale')` |
| BOX | tick boxes | days, a streak, a schedule | `boxes(null, { n: 7, marked: [4, 6] })` under a line, footnote below |
| PRT | chapter card | a new section | `part(S, 2, 'HOW TO {IMPROVE}', { at, media: key })` (or `clip: name`) |
| VF | viewfinder reveal | the best result, a reveal | `viewfinder(S, { at })` then the member's card on it, type in white |
| C2 | screenshot pile | several results in a row | `stack(S, [k1, k2, k3], [t1, t2, t3], { w: 700 })` then arrow + footnote |

## Palette
| Role | Hex | Use |
|---|---|---|
| page | #ffffff | the whole background, always |
| type | #000000 | every typed word |
| red | #ff0000 | 1-2 key words per line (`{word}`), never pronouns or articles |
| marker ink | #1e1e1e | figures, crowds, busts, black arrows |
| marker red | #e5161c | arrows, circles, X-outs (`mark`) |
| green type | #00a80f | the good / wanted side (`{g:word}`), about one scene in 30 |
| grey | #525252 | the smaller note under a definition |

## Type
Arial italic (system font), regular 400 for body, bold 700 for headers, active list items and definitions. Tiers:
hero 97, caps 62 (upright, tracked .11), body 62, secondary 48, list 38, note 32, footnote 27 (`T` in models.js).
Lowercase everywhere except colon headers, tracked statements and single stressed words (`{EXACTLY}`). Line pitch .97 em.
Lines 40-55 characters; centred on x 720. Underline (`_word_`) marks "you / yours" or the contrast word. Bullets are a
hyphen ("- item" or "-item"), never a dot. Footnotes start with "*". Parentheses = a smaller explanation under its item.

## Elements
`say` (type), `figure` (faces: neutral smile frown grin worried shock; poses: stand phone armsup point shrug), `crowd`,
`bust`, `mark` ('arrow' | 'circle' | 'x' | 'down'), `media` (member's picture), `clip` (member's video), `stack`,
`heading`. Nothing else appears: no drawn screenshots, no charts of real data, no logos drawn by hand.

## Motion (measured on the reference at 60 fps; motion.md)
- Default entrance: **pop**, one frame, no transform (`pops`, `enter(S, el, t, 'pop')`). Holds are perfectly still.
- A scene's first line: first word settles (fade .13 s, 40 px rise, 3 deg, .43 s): `pops(..., { lead: true })`.
- Lines re-centre instantly as words arrive. Earlier lines never dim.
- Header + list: header alone at the centre, slides up linearly in 9 frames ending .2 s before item 1 (`heading`).
- Screenshot: pop, or `'fade'` 17 frames. Phone clip from the top edge: `'drop'` 10 frames. A second thing joining:
  `move` the first one aside 14 frames, scale .83. Clip to the top centre: `move` 6 frames, scale .8.
- Crowd: `'scale'` 15 frames from .61. Figure: pop, or `'elastic'` 24 frames. Arrow: `'wipe'` 15 frames.
- Exits: cut (default), or `leave(..., 'fade')` 11 frames.
- Shots: `trans: 'cut'` (about 85 %), the rest `trans: 'dissolve'` with the look's .28 s.
- Cut on the word the first thing shows: something is on screen within 0.25 s of every cut (a chart's axes come with the
  cut and its line draws on its word; an audience comes with the cut and its caption pops word by word).
- Timing: a new shot every 2.0 s median (0.7-5 s), 55-75 visible changes per minute, ~100 in the first 15 s, nothing
  held over 6 s without a pop.

## Camera
None. `S.noCamera = true` in every shot. No push, no punch, no shake, no drift.

## Layout per frame
16:9: the 1440 x 1080 reference frame centred, white sides. Text safe 120 px left/right, 70 px top/bottom; media safe
90 / 60. Centre axis x 720; single lines on y 540; top caption band y 160-300; bottom caption band y 840-1000.
9:16: the same compositions stacked (picture above, text below), never side by side; type at 0.9 size, drawings at
0.75, positions spread 1.15x vertically by `P()` (a phone frame is tall). A phone clip is h 1000 reference px.
Captions are off: the on-screen lines ARE the captions.

## Finish
style.json defaults: theme `dmscales`, grain 0, vignette 0, contrast 1, camera push 0 / punch 0, transitions .28 s,
captions off. Nothing is added on top.
The **Era** control (`settings.era`, looks `look-default` "Clean" and `look-hit` "Hit"): `later` = regular italic lines on
#ffffff (the channel's later videos); `hits` = bold italic lines (every italic line of 40 px and up) on #fcfcfc (its two
most-viewed videos). Scenes never set the weight of a narration line themselves unless the line needs it.

## Sound
skill/SOUND.md: the voice and one music bed (audio/beds.json), no effects; never `S.add` / `S.line` / `S.arrow`.

## What the checks enforce (this style's own)
- RED: more than 3 red words in one line. PAGE: a page other than the era's (#ffffff / #fcfcfc; black only through
  `viewfinder()`). HOLD: nothing new for over 6 s. VOID: nothing on screen 0.25 s after a cut.
- A text-only card sets `S.sparse = true` (single lines, transition cards); `heading()` does it itself.

## Never
- No drawn stand-in for evidence (a fake analytics card, a made-up screenshot or number).
- No sound effects (the style runs on the voice and one music bed).
- No red stamps or verdict plaques, no "AI voice" notices (NO_SLOP.md).
- No shadows, gradients, borders on pictures, textures or vignette.
- No more than 3 red words in a line; no red on pronouns, articles or prepositions.
