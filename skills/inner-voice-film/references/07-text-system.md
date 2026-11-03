# 07 — Text System (the white narrator is text only; the blue inner-voice lines are ALSO spoken with ElevenLabs — see 08-audio §0)

Contents: 1 Font · 2 Roles · 3 Animation vocabulary · 4 Hold times · 5 Writing style · 6 Components

Measured specs live in `03-visual-canon.md` §5–6 and win on conflict. Component code (ShatterText,
TitleCard wavy underline, CountUp spring): `deep-research/04-typography.md` §5.

---

## 1. Font

The films use Comic Sans MS (measured). Use **Comic Relief** (metric clone, Google Fonts, has `latin-ext` for
Turkish ğ ş İ) → fallback **Mali** → Pangolin. Comic Neue / Short Stack lack Turkish glyphs.

```ts
import {loadFont as loadComicRelief} from '@remotion/google-fonts/ComicRelief';
export const {fontFamily: COMIC} = loadComicRelief('normal', {weights: ['400', '700'], subsets: ['latin', 'latin-ext']});
export const FONT = `${COMIC}, "Comic Sans MS", cursive`;
```
Turkish casing: `toLocaleUpperCase('tr-TR')` / `toLocaleLowerCase('tr-TR')`.
Topic HUD label may use a small rounded sans (e.g. Nunito 600 caps, wide tracking).

## 2. Roles

| Role | Colour | Case | Where | Anim |
|---|---|---|---|---|
| HOOK / NARRATOR (story, past tense) | white `#FFFFFF`, no glow | Sentence case + "." | centre on black; over scenes y ≈ 13–21 % | linear fade 18–21 f in / 12 f out, slow rise |
| LESSON couplets (2nd person) | white | Sentence case + "." | upper third, centred, only when motion is calm | same, line 2 after a 6–10 f gap, +0.5 s hold |
| INFO / excuse (voice before it has a body) | accent (brand `#7DA5FF`) | lowercase, "..." | above hero, left-anchored | typewriter 16 cps, dots one by one |
| VERDICT | accent (brand `#7DA5FF`) | lowercase "." | same baseline | pop 1.18→1 in 3 f |
| VOICE | accent, soft glow | lowercase "." | over the shadow's head | fade 3–6 f, continuous upward drift, fade 9–12 f |
| VOICE SHOUT (boss / word targets) | accent, strong glow | lowercase | upper left/centre, beside the giant | slam: scale 1.6→1 in 6 f + shake 10 f + ±2 px jitter |
| DAY | `#BBBBBB` bold | "DAY N" | (150, 147) screen-space | 6 f fade, rolls |
| REP counter | white `#EEECE6`, strong white bloom, ≈150 px bold | digits | above hero centre | spring pop scale 1.35→1 per rep, glow 28→12 px |
| HUD label / clock | gray caps / off-white | — | under the top bar / top-right | static, clock changes only at cuts |
| TITLE | cream `#F2EFE6` bold ≈250 px, soft glow | ALL CAPS | y ≈ 40 % | fade+scale .96→1 24 f |
| UNDERLINE | brand `#4F86FF` (reference film: `#E8463A`) 8–9 px wavy, 105 % of title width, 4–5 waves | — | y ≈ 53.6 % | stroke draw 20 f, starts 8 f after title settles |
| SLOGAN | cream ≈66 px | Sentence case | y ≈ 66.5 % | fade in after underline, hold to end |

One message at a time (DAY/HUD may coexist). White and red never in the same frame. Red count ≈ white count.
≈12–16 text cards in a 2:40 film.

## 3. Animation vocabulary (30 fps)

A-fade (default, linear, no blur for hook) · typewriter (excuse/whisper; 1 char per 2 f; ellipsis dots 3–4 f
apart) · pop (verdict, counters) · drift (all voice text rises slowly while visible) · slam + shake (shouts) ·
shatter (punched words — glyphs fly, settle dim, keep floating) · dissolve-to-light (grief) · underline draw
(`evolvePath`) · count roll (DAY, ease-out integer, hard swaps every 3 f) · keyword tint (per-letter colours).

## 4. Hold times

`holdFrames = round(30 * max(1.2, 0.8 + 0.3 * words)) + (lesson || sceneEnd ? 15 : 0)`
Turkish: 0.33 s/word, max 6 words per line. Total on-screen = in + hold + out.
Text appears **after** the picture beat it comments on; the shot must last at least `in + hold + out`.

## 5. Writing style

- Narrator: ≤ 7 words, one clause, sentence case, always a period; past tense until the reframe, "you" after.
- Voice: ≤ 4 words (boss ≤ 3), lowercase, period (drop it only on words about to be destroyed), never "!".
- Excuse: lowercase first-person-ish, digits not words ("5"), trailing "...".
- Couplets: setup → flip, line 2 usually shorter and starts with So / But / It's.
- Slogan: chiasmus / word-flip ≤ 6 words (+ optional "You decide.").

## 6. Components (props sketch)

```ts
<HookCard text keyword?={{word, colors}} />                // 0.4s empty → fade 0.6–0.7s → hold → fade 0.4s
<NarratorText text position="center"|"top" lesson? />
<InfoText text x y entrance="typewriter"|"pop" accent />
<VoiceText text anchor={{x,y}} line={1|2} level accent seed shatterAt? />
<DayCounter day rollFrom? rollStart? />                     // screen space
<CountUp values hitFrames />
<ShatterText text origin impact fontSize seed />            // closed-form, deterministic
<TitleCard title slogan accent seed />
<TopicHUD kind="dopamine"|... events />                     // global layer, global frame clock
<ClockHUD time="2:14 PM" />
```
Every component reads `useCurrentFrame()` locally inside its `<Sequence>`; motion only via
`interpolate`/`spring`/`random(seed)`.
