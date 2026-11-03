# 03 — Generator (SVG) + Higgsfield finishing pass

Full design notes: `deep-research/03-production-system.md`. Code: `generator/` (thumb.html, thumb.js, hero-rig.js
copy with `noHead`/`headAnchor`, render.py, examples.json).

## 1. Default path — SVG generator (free, deterministic, 100 % on-model)

```powershell
$G = "$env:USERPROFILE\.claude\skills\other-self-thumbnail\generator"
python "$G\render.py" requests.json --out=<film folder>\thumbs          # PNG 1280x720 + _320 previews + contact_320.png
python "$G\render.py" requests.json --out=<...> --debug                # + *_debug.png safe-zone overlays
```
Requires Python + Pillow and Microsoft Edge (headless). Fonts come from Google Fonts (network once).
Request = JSON list of objects:
`{id, preset: bedClock|doorLight|phoneBed, text, textLayout?, accent?, expression: glare|resolve|tired|shocked|sad|hopeful|anxious|content, look?, extras?: [sweat,bags], noExtras?, head?: {x,y,r,tilt}, zoom?, focus?, props?: {clock, bubbles}, twin?: {x,y,scale,opacity,mood,facing}, grain?, baseImage?, debug?}`
(full JSON schema in `deep-research/03-production-system.md` §2.4). Notes: the clock time goes in `props.clock`;
long text in `bedClock` auto-switches to centred; `text: ""` renders without text.

Layer stack: bg → back props → one emitter (core + bloom + screen spill) → lit body (form shade, accent tint,
rim) → thumbnail head (bigger eyes, angled lids, thick brows, eye bags, outlined sweat, light-aware shading) →
front props → FX (≤ 7 particles) → vignette + grain → text (stroke + shadow) → safe-zone check.

New scene = new preset in `thumb.js` `PRESETS` (copy an existing one: `build(c, L)` returns `{back, hero, front}`).
Keep presets reusable across films (kitchenTable, deskLaptop, moonBed, floorBed, doorClosed…).

## 2. Final path — Higgsfield 3D/painterly finish (hybrid) — TESTED 2026-10-14, works

The competitor's thumbnails look "3D" (soft volumetric shading, rim light, depth). The flat SVG alone does not.
**Tested result** (`thumbnail-research/higgsfield-test/`): nano_banana_pro, 2 candidates from our no-text SVG →
both kept the character on-model (sprout, oval eyes + highlights, sweat drop, 8:47 clock) and gained soft 3D
volume; 4 credits total. Output 2752×1536 (16:9) — the generator's `baseImage` scales it to 1280×720.
Notes from the test: the job metadata reported model `nano_banana_2` although `nano_banana_pro` was requested;
the presigned upload needs headers `Content-Type: image/png` **and** `If-None-Match: *`
(`curl.exe -X PUT -H "Content-Type: image/png" -H "If-None-Match: *" --data-binary "@file.png" "<upload_url>"`);
results come from `mcp__higgsfield__jobs_wait` as `result_url` → download with `curl.exe -o`.
Use the SVG render for drafts/A-B composition decisions and the Higgsfield finish for the uploaded final.

Why hybrid: our SVG fixes the character, pose, composition and light; the AI only adds soft painterly lighting
and texture (T2/T3-style). Pure AI generation drifts off-model (sprout disappears, eyes change, body grows) and is
not reproducible → only for brainstorming scenes.

Costs measured 2026-10-14 (`get_cost`): `nano_banana_pro` 16:9 2k ≈ 2 credits · `flux_3_image` 1.5k ≈ 2 credits ·
`gpt_image_2_5` ≈ 0.25 credits. Always preflight with `get_cost: true` and tell the user before spending.

Steps:
1. Render the SVG version **without text**: same request with `"text": ""` → `X-notext.png`.
2. Upload: `mcp__higgsfield__media_upload {filename: "X-notext.png"}` → PUT the bytes to `upload_url`
   (PowerShell: `Invoke-WebRequest -Uri $url -Method Put -InFile X-notext.png -ContentType image/png`) →
   `mcp__higgsfield__media_confirm {media_id, type: "image"}`.
3. Generate 2–4 candidates: `mcp__higgsfield__generate_image {model: "nano_banana_pro" (or "flux_3_image" /
   "gpt_image_2_5"), aspect_ratio: "16:9", count: 2–4, medias: [{role: "image_references", value: <media_id>}],
   prompt: <below>}`. Check the role name with `models_explore {action:"get", model_id}` if it errors.
4. **DEFAULT since test 4 (2026-10-14): use the style block in `05-style-dna.md`** (gritty hand-inked painted
   cartoon, white-sclera eyes with veins/eye bags, detailed hands, warm rim light) + the scene from the Hook Engine.
   Result `reference-thumbs/OURS-v3-BEST-not-today.png` = competitor-level drawing, on-model (both sprouts).
   The prompts below (v2 "3D", v1 "restyle") are older and produce weaker, too-clean drawings.
   **Quality lesson (test 2):** prompt v1 below ("re-render this exact image") only beautified our
   weak composition → user: "not the same quality as the competitor". What closed the gap (prompt v2): let the
   model improve camera and lighting, ask for **bold thick outlines, one hard key light sculpting the face (lit side
   + deep-shadow side + bright rim), body acting (hands clutching the blanket), stronger expression, close crop,
   top 25 % left empty for the title**. Result `thumbnail-research/higgsfield-test/final-v2-b.png` ≈ competitor
   level. Candidate v2-a was rejected: eye highlights lost (hollow ovals) → off-model. Use v2 by default:
   > Use the reference ONLY for the character design, the idea and the props; you may improve the camera and
   > lighting. Create a premium, high-contrast YouTube thumbnail illustration for an animated short film, stylized
   > 3D-looking cartoon with crisp bold outlines. SAME CHARACTER, strictly on-model: a big perfectly round warm
   > sand-coloured (#E9C9A2) head, a small leaf sprout on top of the head, two solid dark tall oval eyes each with one
   > white highlight, thick dark eyebrows, small simple body, bold clean dark outline (thick, 6-8 px), soft volumetric
   > 3D shading. SCENE: {moment just before the decision, body acting with hands/props}. Close-up, {head ≈45 % of
   > frame height, left of centre}; {expression: brows, eyes, mouth, sweat/tear}. On the right, very close,
   > {emitter + exact content}; it is the ONLY light source: strong {hue} light hits the {side} of his face hard with a
   > bright rim light and sculpted shadows, the other side falls into deep shadow. Soft bloom around the {emitter},
   > light spilling over {surfaces}. {set}, near-black background, cinematic contrast, subtle grain. Leave the top 25%
   > of the frame dark and empty for a title. Only one light colour: {hue}. No text, no letters, no logos, no other
   > characters, no red, not photorealistic.
   Prompt v1 (conservative restyle, use only if v2 drifts):
   > Re-render this exact image as a polished stylized 3D-looking cartoon illustration with soft volumetric shading,
   > like a high-quality animated short film thumbnail. Keep the composition, camera framing, character position,
   > pose, facial expression and every object exactly the same. Keep the character perfectly on-model: a big perfectly
   > round warm sand-coloured (#E9C9A2) head with a thin dark outline, a small leaf sprout on top of the head, two solid
   > dark tall oval eyes each with a small white highlight, thick dark eyebrows {brow state}, {mouth}, {extras}. Give
   > the head real volume: soft gradient shading from the light, subtle ambient occlusion where it meets {surface},
   > a {hue} rim light on the side facing the {emitter}. {emitter description with exact digits/screen content}.
   > {set description}, near-black background, subtle film grain. Only one light colour: {hue}. No text, no letters,
   > no logos, no extra characters, not photorealistic.
5. Download the chosen result into the film's thumbs folder (result URL from the generation output / `job_display`).
6. Put the text back with our generator: `{id: "X-final", preset: "<same>", text: "TOMORROW.", baseImage: "file:///…/X-ai.png"}`.
7. **Reject** any candidate that drifted: sprout missing/changed, eye highlights missing (hollow ovals), pupils or
   eye whites added, extra colours, body proportions changed, red accent. Re-run or fall back to SVG.
   Always generate ≥ 2 candidates — in test 2 one of two drifted.
8. Never feed competitor thumbnails or the words "Day One Films" as references/prompts.

Rights: the SVG composition is ours; AI-finished images may have weaker copyright protection in some
jurisdictions — the hybrid keeps the human-authored layer dominant. Keep the SVG source next to every upload.

## 3. Remotion later

When the studio exists: port to `<Still id="<slug>-thumb-a" width={1280} height={720}>` using the same layer
stack; fonts via `@remotion/google-fonts/Fredoka`; text fitting via `@remotion/layout-utils` `measureText()`.
Until then the Edge generator is the production path.
