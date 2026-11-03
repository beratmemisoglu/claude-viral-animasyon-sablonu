# Dmscales - analysis of the references

Measured with ffmpeg + numpy on full-resolution frames (research/dmscales/reports: visual.md, motion.md,
script_audio.md). Px are at the reference's 1440 x 1080 frame; the style centres that frame in 1920 x 1080 (x + 240) and
scales it 0.75 for 9:16 (type 0.9).

## Sources
Five videos of one faceless explainer channel (YouTube), all 1440 x 1080 (4:3), AV1:
- "The Entire Shorts Algorithm Explained in 180 Seconds" 179 s, 60 fps, 705K views (the purest form; most numbers)
- "The Entire Longform Algorithm Explained in 300 Seconds" 300 s, 60 fps, 368K views
- "The Entire TikTok Algorithm Explained in 120 Seconds" 120 s, 60 fps, 30K views (kinetic-type variant)
- "10,000 Hours of YouTube Knowledge in 16 Minutes" 977 s, 30 fps, 99K views (gameplay b-roll variant)
- "how to blow up a youtube channel (with one killer idea)" 337 s, 60 fps, 43K views (After-Effects-heavy variant)
Whole runtimes used: 1 fps contact sheets, a frame after every scene change, 12 fps strips, per-frame change features at
native fps, VTT word timings.

## Source setup (only when converting an existing setup: docs/CONVERT.md)
not a conversion

## Shot types and share of time
Sampled every 2 s (the two hits / the later videos):
- text-only card on white: 33-42 % / 8-36 %
- real screenshot (analytics, UI) with caption, arrow or footnote: 26-31 %, bare screenshot 17-22 % (proof 53-75 % in the hits)
- marker figure / brain / silhouette with text: 3-9 % / 10-28 %
- crowd doodle 0-10 %; icons / logos 0-18 %; drawn diagram or chart 1-15 %; thumbnail grid / side by side 1-7 %
- footage, meme clip or photo: 1-7 % (71 % in the gameplay-b-roll video)
Median shot: 2.0 s (Shorts video), 3.0 s (Longform video).

## Pacing
- Scene changes per minute 23.1 (Shorts), 15.6 (Longform), 20.3, 6.5 (kinetic), 9.5 (b-roll); median 1.97 s, p10 0.70 s,
  p90 4.99 s (Shorts). Visible changes (pops included) 56-75 per minute; 108 per minute in the first 15 s of the hit.
- 86 % of scene changes hard cuts (Shorts), 58 % (Longform); the rest linear fades of 11-17 frames at 60 fps (0.18-0.28 s).
- Narration 265-282 words per minute, breaths edited out; no pause over 0.35 s except a 0.5 s beat after a punchline.
- Scene changes land on clause starts: median +67 ms (IQR 0 to +107 ms), 60-74 % within 250 ms against 25-27 % by chance.
  Keyword pops land 0 to +100 ms after their word's onset.

## Palette
- page #ffffff (#fcfcfc in two videos), 52-91 % of the frame; flat, std 0
- type #000000; emphasis #ff0000 (pure red), 1-2 words per card on 84 % of cards
- marker ink #1e1e1e (figures, crowds); marker red #e5161c (arrows, circles, X-outs)
- neon green #00fc16 (the good side, growth line), note grey #525252, burst yellow #fcd400
- contrast: #000000 on #ffffff 21:1; #ff0000 on #ffffff 4.0:1; #00fc16 on #ffffff 1.4:1 (the style's green TYPE uses
  #00960d, 3.9:1; strokes keep #00fc16)

## Type
Arial with its true italic (glyph overlay IoU 0.88 against a 97 px render), system font on Windows (fallbacks Arimo,
Liberation Sans). Tiers: hero 90-100 px, tracked caps 62 px (+0.10-0.12 em), body 62 px, secondary 43-51 px, dense list
38 px (39-40 px pitch), parenthetical 27-36 px, footnote 27 px starting with "*". Line pitch 0.95-1.0 em. Lowercase
except colon headers, tracked statements and single stressed words. Every line centred on x 720; widest line 1176 px
(82 % W), most 650-1050 px. Underline 0.055 em thick, 0.21 em under the baseline, the word's own colour.

## Lighting and finish
Flat 2D: no shading, no shadows, no gradients, no grain, no vignette, no texture (corner std 0). Mean light ~0.93; dark
pixels under 2 % except the screenshots' own dark UI (#0f0f0f / #272727) and one black viewfinder scene.

## Motion and camera
- Pop: 1 frame at 60 fps, opacity 0 to 1, no transform (67 % of all visible changes in the hit).
- Scene title: characters cascade in 6-10 frames (2-frame stagger, fade, a few degrees of tilt), then drift up ~40 px and
  level over 15 frames, ease-out (0.43 s total).
- Header + list: the header rises linearly 150-258 px in 8-10 frames, ending 0.15-0.37 s before the first item.
- Screenshot fade 17 frames linear; drop from the top edge 10 frames ease-out; push-aside 14 frames to scale 0.83;
  crowd scale-in 0.61 -> 1.0 in 15 frames; figure elastic 24 frames (0.97 at 8, 0.84 at 14, 1.0 at 19); arrow wipe 6 frames
  + fade 15 frames; exits cut, or fade 11 frames.
- Camera: none in the hits (holds pixel-identical; 7 % of the hit's runtime moves at all). No shake, no drift.

## Sound
Integrated about -19 LUFS (master -17 to -21), peaks at 0 dBFS; voice dry and fast; one lo-fi bed (75-95 BPM by
spectrogram) about 8-10 LU under the voice from 0.0 s to the last frame, no ducking. No sound effects in the hits; the
late AE-heavy video adds sub-booms on transitions about every 10-15 s.

## Narration trigger -> visual
- A clause starts -> a new shot within 0-107 ms of its first word.
- A key word is said -> it pops in red (one frame) within 0-100 ms.
- "This is called X" / "a metric called X" -> a caps header "X:" with its distinctive word red, bullets on their words.
- A list is spoken -> an invented header ending in ":" and one "- item" per spoken item, popping on each item's word.
- "this / these / here / like this" -> the referent (a real screenshot or list) on screen, a red arrow or circle on it.
- A number -> digits with "~" for "around", on the proof screenshot.
- "but most importantly" -> its own clean card, no red.
- What a viewer / the algorithm thinks -> a lowercase quote in double quotes next to a figure / an icon.

## What to avoid
The references never use: camera moves, shadows, gradients, textures, borders on pictures, drawn fake screenshots, counters,
typewriter carets, highlight sweeps, strike-throughs, screen shake, sound effects (in the hits). From NO_SLOP.md: no red
stamps or verdict plaques, no notice that the voice is AI, no sound effects the member did not supply, no drawn stand-in
for real evidence, every frame readable.
