# Dmscales - pitfalls

One line per fault that was found and fixed, so it is never made again: in this style, in every video built in it, and
in the next styles. Written by the Claude that fixed it, in the same turn as the fix. Every video in the style reads this
file before it builds.

Each line is a rule that holds outside the moment it was found, with the evidence in brackets:
`- <rule> (<check or "eye">, <view> <aspect> <t> s: <the finding as printed>)`

Example: `- A label on a photo gets a plate: text straight on a busy picture fails contrast (contrast, sample 9:16 6.2 s:
#e8e1d4 on #b9ad97 is 1.4:1, needs 4.5).`

- A scene file that fails to load shows an empty, "clean" check: after any edit to models.js run `node --check` on a copy, and distrust a view whose findings all vanish at once (eye, mustfail_red 16:9: "reports nothing" from a SyntaxError in models.js).
- The layout check measures the mesh's geometry, not the ink: give canvas-drawn type a tight boundingBox (cap height + descender), or stacked lines read as overlaps (overlap, motion 16:9 2.25 s: st.l1 + st.l2 31% covered from padded word canvases).
- Text on a plate needs the plate's colour in an ANCESTOR's userData.bg, not on the text mesh itself (contrast, templates 16:9 3.75 s: #ffffff on #ffffff 1.0:1 for the tagBox label).
- Neon green #00fc16 is a stroke colour only: as type on white it reads at 1.4:1; green type uses #00960d (contrast, hero 16:9 5.0 s: #00fc16 on #ffffff 1.4, needs 3).
- A picture or clip given h only must keep its own aspect: never default w when h is set (eye, motion 16:9 0.5 s: a 9:16 phone clip squashed into 870 x 600).
- On the kit's dark board the white-page elements sit on their own white sheet; never recolour the style's ink for a dark ground (frames, kit 16:9 1.5 s: BLANK, black type on #1d1e24).
- Hand-drawn boxes are straight strokes with jittered corners: the smoothing used for organic strokes rounds a square into a "D" (eye, templates 16:9 14.5 s).
- Canvas type: the mesh's y is the line's y MINUS (canvas centre - baseline) MINUS 0.36 em; a flipped sign floats every line 0.72 em high (eye, hero 16:9 3 s: "SWIPE RATE:" 66 px above its y at 92 px).
- A cached "last painted" state must key the finished state apart from the frames before it, or a frame drawn after playing differs from the same frame drawn alone (repeat, sample 16:9 11.34 s: 0.36 % of pixels differ, a half-typed title).
- A title cascade must be in within ~10 frames (N-q: 11 characters in 8 frames); a slow one leaves the first frames after the cut blank (frames, sample 16:9 4.88 s: BLANK).
- A shot cut on its clause must show something with the cut: cut on the word the first thing shows, or show the drawing's base (axes) before its line moves (VOID, sample 16:9 5.52 s and 14.61 s: nothing on screen 0.25 s after the cut).
- A check that probes another time must replay every visibility source (our ticks AND the engine anims we registered), or it reports things missing that are on screen (VOID false positive, sample 16:9 9.85 s).
- Write files with LF line endings from Python on Windows (newline='\n'), and keep backslash escapes out of shell heredocs that write JS (text: sample/timeline.json CRLF; a "\n" became a real newline and broke models.js).
- Caps lines in Turkish: write İ for i and I for ı, and lowercase cue words the narration language's way (words() does): cue() lowercases the English way, so "NASIL" looked for "nasil" and missed the spoken "nasıl" (eye, ilk-30-saniye: a caps line popping on the wrong word). A number spoken as a word ("otuz") and shown as digits ("30") gets its time from the spoken word: pops(..., [at('ilk'), at('otuz'), ...]).
- A pose's arms must clear the head: 'armsup' hands ended inside the head outline and read as hands on the cheeks (eye, ilk-30-saniye 16:9 13.6 s).
- Check a weight against the reference before "fixing" it: a list header looks thin among bold lines, but the hits set it regular on purpose (N-q 20.5 s "HOW TO FIX:", fS8 17.6 s): only the current item and its note are bold (eye, side by side of ilk-30-saniye 22.2 s with N-q 20.5 s; a header made bold in round 7 was reverted).
- Add clips at the video's own rate (`add_media.mjs --fps 30` for a 30 fps export): at 12-15 fps every clip frame shows twice and screen recordings and animation stutter (measured, claude-3d-5-adim: 85-88 % of frames in a clip alternated moving / still; 0-2 % at 30 fps).
- Cut every clip to its shot and play it with `loop: false`: a recording longer than its shot stops mid-action at the cut (typing, a download, a quoted line), a shorter one jumps back to its start; trim, or speed it up to 2x at most (`setpts`), and merge the shots one recording runs across into one shot. Trim a recording's own fade-in / fade-out frames, or the cut flashes black (claude-3d-5-adim, the member's report: "video yarıda kalıp diğer sahneye geçiyor").
- A thought cloud's trailing circles start at its top-left: put the thinker's head level with the cloud's top, beside it (as in the reference), or the circles point away from the head (eye, ilk-30-saniye 16:9 7.9 s).
