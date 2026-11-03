# Dmscales - the direction (step 1 of every build)

Before any scene file, turn the member's script and files into `edit-plan.md` in the project root: the edit plan the
scenes are then built from, shot by shot. It is the dmscales version of a director's notes, written by you from the
rules below (measured on the reference channel, research report script_audio.md). Show it in the chat in short form
(shot count, template mix, which file goes where) and build from it; when the member changes edit-plan.md, rebuild the
shots that changed.

## Inputs
- `audio/script_timed.txt` (the narration with times) and `script.txt`: the words are the member's. Never change,
  add or drop a spoken word. The screen may condense, add footnotes and quotes (below); the voice never changes.
- `assets/media/media.json`: the member's screenshots (kind image) and clips (kind clip: n frames, fps, seconds). Look at
  every one (Read the picture, or frames 0 / middle / last of a clip) and write one line on what it shows before
  placing it. Files not yet added: run scripts/add_media.mjs first.
- The member's notes in the build request (tone, what to stress, where a file belongs) beat these rules.

## The format (one block per shot, in narration order)
```
## S07  1:12.4  T10 screenshot + footnote
say:    "aim to get your retention up to here."          <- the clause, verbatim, from script_timed.txt
screen: to get your {retention} up to _here_             <- markup: {red} {g:green} _underline_ **bold**
media:  analytics_week3 (w 870) + mark circle on the 70% bar
foot:   *anything above 60% on a 10 min video is great
enter:  pop on "aim" ; mark wipe on "here" ; foot pop +0.4 s
```
Fields: `say` (verbatim), `screen` (what the type says, with markup), `media` (file name from media.json, size,
mark), `foot` (asterisk line, screen only), `quote` (a thought in "double quotes"), `enter` (what pops on which word),
`note` (anything the builder must know). Use a template id from STYLE_GUIDE.md "Templates" in the header.

## Rules: narration -> shots
1. **One shot per clause** (split at . , ? ! : and at "and / but / because / so / then" after ~6 words). Target a new
   shot every 2.0 s median (0.7-5 s), 20-23 shots per minute, ~100 visible changes per minute in the first 15 s.
2. **Text = the spoken chunk, condensed**: 3-8 words (median 6), lowercase, fillers dropped ("basically", "you know",
   "like", "pretty"), "so / and / but" kept. A long clause shows only its LAST content chunk.
3. **Red** (`{word}`): 1-2 words per card, max 3: the concept noun / term (~45 %), an evaluative word (~25 %: hidden,
   same, bad, free), the key verb (~20 %: push, waste, study), a number (~10 %). Never a pronoun, article or preposition.
   Transition cards ("but most importantly", "and during this:") have NO red.
4. **CAPS + red** for a stressed intensifier: {EXACTLY}, {REALLY}, {NEVER}. **Underline** the contrast target: "_yours_".
   **Green** (`{g:word}`) only for the good / wanted side, about once per 30 shots.
5. **Definitions** ("this is called X", "a metric called X") -> T04: header `X:` in caps, its distinctive word red, then
   1-3 "- " bullets on their spoken words, a grey parenthetical if needed.
6. **Lists** -> T03: invent a header ending in ":" ("HOW TO FIX:", "CTR comes from:"); each spoken item pops "- item" on
   its word; an item may carry a small (parenthetical). "but most importantly" gets its own clean card, then the last
   item comes in big.
7. **Deictics** ("this", "these", "here", "like this", "one of these"): the shot MUST show the thing: the member's file
   with a red arrow or circle, or a list / number. No file for it -> say so in `note` and use a text card.
8. **Proof**: a number, result, channel or example -> the member's screenshot / clip (T10, T12, C1, C2) with an arrow or
   circle on the exact part. Aim for proof media on 40-55 % of the runtime when the files allow it.
9. **Footnotes** (`*`, 27 px, centred under the main thing): a caveat, a stricter tip, a source ("*not my screenshots",
   "*not my video", "*a channel of mine"), a joke. Screen only, never spoken. About one every 6-10 s.
10. **Quotes**: what a viewer / the algorithm / an opponent thinks becomes a lowercase quote in "double quotes" next to a
    figure (viewer), the member's icon picture (algorithm), or a picture (opponent).
11. **People**: "you" acting -> T07 figure (face matches the outcome: frown for a fail, grin for a win, phone for
    watching); viewers / audience -> T14 crowd; other creators / competition -> T15 busts.
12. **Numbers** as digits, "~" for "around", ranges "100 - 10,000"; every acronym gets a glossary footnote.
13. **Hook** (first 15 s): something new every ~0.6 s; the first shot is on screen at 0.0 s.
14. **Ending**: the CTA line on its own card or the member's channel / playlist screenshot; no outro.

## Variety (videos of 5-10 minutes must never feel like one shot repeated)
15. **No template more than 2 times in a row** (T01 single lines included: a third line in a row becomes a T02 punch,
    a T05 staircase, a T06 caps statement or a picture). Write the template id in every block header so this is visible.
16. **Every minute holds all three families**: proof (the member's media: T10 T11 T12 T18 C1 C2), type (T01-T06 T13),
    and drawing (T07 T08 T14 T15 T19 T22, cloud, curve, boxes, burst, compare). If the files run out, carry the proof
    family with compare cards, curves (shapes, not data), boxes and the T13 inventory, never with invented screenshots.
17. **Chapters**: a `part()` card ("PART 2: HOW TO {X}") at every section of the script, at least every 1-2 minutes;
    on its own 1.5-2.5 s shot, with the member's picture or clip above it when there is one.
18. **Figures rotate**: never the same face + pose twice in a row; use all six faces and five poses across a video.
    The "you" figure frowns on a fail, grins on a win, holds the phone when watching, shrugs at a myth, points at a fix.
19. **Accents, used sparingly** (each at most once per ~45 s): cloud + X-out (a belief proven wrong), curve (a shape of
    retention / growth / drop), growth line (a win), burst (excitement around a phone), boxes (days / streaks),
    viewfinder (a reveal of the member's best result), compare (two sides).
20. **Re-hook every ~60 s**: a question card, a myth flip ("a lot of people think X, but..."), or a viewfinder reveal.

## Pacing for long videos
- First 15 s: a new shot every 0.7-1.2 s (~100 visible changes per minute).
- After that: 15-20 shots per minute (median 3-4 s), never a shot over 6 s without a pop inside it.
- A 6-7 minute video is about 100-130 shots; plan the whole edit-plan.md before building any scene.
- Clips: keep each under ~6 s on screen (add_media cuts them at 12 fps); about 90 s of clips per video at most.

## Checks before building
- Every spoken clause has a shot; nothing invented on the voice side.
- Every media name exists in media.json; every deictic has its picture or a note.
- Red count per card <= 3; transition cards have none.
- Shot lengths: none over 6 s without a pop; median near 2 s in the hook, 3-4 s after it.
- No template id three times in a row; every minute has proof, type and drawing; a part() card every section.
