# Dmscales - sound

Measured on the reference (research report script_audio.md 5): the two hits run on the voice and ONE music bed, with no
sound effects at all. This replaces the starter's sound_design.md (its "every entrance makes a small sound" is not this
style).

## The bed: audio/beds.json (write it in every build)
```json
{ "beds": [ { "from": 0, "to": <the video's end in s>, "type": "music", "mood": "curious", "bpm": 85, "gain": -30 } ] }
```
- One lo-fi bed from 0.0 s to the last frame: no intro, no fade-in, no swap (a video over 5 minutes may swap the mood at a
  `part()` card: a second bed from that time on).
- 75-95 bpm (`curious` 85 by default; `warm` for a calmer topic). Gain -30 to -33: about 8-10 LU under the voice.
- No `room` bed. Master around -16 LUFS, true peak -1 dBTP (the mix does it).

## Effects: none, unless the member gives their own
- The style's helpers (`say`/`pops`, `enter`, `leave`, `move`, `mark`, `media`, `clip`, `heading`, ...) make no sound.
- Never use `S.add`, `S.line` or `S.arrow` in this style: they schedule pops, swishes and clicks.
- Keep `trans: 'dissolve'` rare (about 15 % of shots): each one schedules a soft swish.
- The member's own sound effects library may be used when they ask: one hit on a `part()` card or a `viewfinder()` reveal
  at most, never on text pops.

## The voice
Fast and dry: about 270 words a minute, breaths cut, no pause over 0.35 s except a 0.5 s beat after a punchline. The
member's own recording is cleaned and timed by the app (Clean and time); scenes cue every event on its words.
