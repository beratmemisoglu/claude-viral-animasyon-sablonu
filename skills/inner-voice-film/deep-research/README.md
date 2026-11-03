# deep-research — raw expert reports (read on demand)

These are the 10 specialist reports + 6 frame-by-frame analyses this skill was built from. They contain
long code listings (Hero.tsx, FK/IK, expression path data, motion keyframe tables, InnerVoice SVG, ShatterText,
TitleCard, FilmRenderer, Music/SFX layers, set SVG specs) — reuse that code instead of rewriting it.

**Precedence when sources disagree:**
1. `frame-analysis/*.md` (measured from the real films) and `../references/03-visual-canon.md` (their synthesis)
2. `../references/*.md` (reconciled decisions)
3. the files in this folder (estimates from 20 stills + web research)

Known conflicts already resolved in references: continuous breathing/idle sway/glow pulse (→ off; limited
animation), far limbs gray (→ cream @ 0.58 opacity), body outline (→ none), 64 px top-only letterbox
(→ 96 px top and bottom), lamp cone (→ radial pool), line boil (→ off), single red villain colour (→ per-topic
accent), DAY counter at (86,113) (→ (150,147), #BBB), whisper-faint voice text (→ normal; faint = mid-fade),
TransitionSeries fades (→ custom dip-to-black overlay), slap with IK reach + shake (→ effect on the prop).

| File | Use it for |
|---|---|
| 01-hook-retention.md | 20-topic hook table, open-loop map, pattern-interrupt list, sources |
| 02-story-architecture.md | DISCIPLINE & DOPAMINE beat sheets, 5 fully worked topic films |
| 03-inner-voice.md | exact SVG + filters, pose joint table, entrance/lunge/split frame tables, 8 topic ladders |
| 04-typography.md | text component code (ShatterText, TitleCard underline, CountUp), font verification |
| 05-character-design.md | full Hero.tsx, FK/IK, EXPRESSIONS path data, pose library, token rules |
| 06-motion-library.md | motion core (track/sample/springs/noise), every action's keyframe table + poseAt(), shake/hit-stop/smear/ribbon |
| 07-environments-lighting.md | SVG set specs, wobbly path, 7-seg digits, mirror crack, city parallax, summit, new-topic sets |
| 08-remotion-architecture.md | types, validateScript, renderer, helpers, QA commands, package.json |
| 09-sound-music.md | music map, SFX table, audio components, procedural audio toolkit |
| 10-packaging-strategy.md | catalog analysis, 22 titles, thumbnail templates, description, Shorts, metrics |
| frame-analysis/discipline-*.md | DISCIPLINE 0:00–0:30 frame-accurate (30 fps timings in "Rebuild notes") |
| frame-analysis/dopamine-*.md | DOPAMINE 0:00–0:30 frame-accurate incl. HUD, parallax, reward, creature |
| script-DISCIPLINE.txt / script-DOPAMINE.txt | the original scene descriptions (Turkish; partly inaccurate — see canon §11) |
