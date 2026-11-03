# 08 — The production system the tutorial teaches (tool-by-tool pipeline)

Analyst #8 of 8. Source: AI Flow, "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)" (22:52, 144.5K views).
Evidence: full-res frames I extracted with ffmpeg into `tmp\a8\`, the 1 fps frames, the English Whisper translation, `v.info.json`, `cuts.csv`, `scdet_scores.csv`, `heatmap.json`, `comments.json`, and loudness/silence measurements I ran on the final-video segment (21:52–22:52).
All prompts below are **summarised by structure**. The "improved" templates are my own wording, not the tutorial's PDF (which I did not download).

---

## 0. What the tutorial actually teaches (one paragraph)

It is a free-tool, copy-paste prompt pipeline. ChatGPT (and Claude for the script) writes every text asset from six prompts kept in one Google Doc ("Finance Niche / Nick Invests"). That doc holds the prompts for channel name, channel logo, video ideas, video script, images, thumbnail and SEO. Google Whisk makes every still, with one trick: the first good character image goes into Whisk's **Subject** slot so the same mascot appears in every later image. Google AI Studio's free Gemini TTS ("Charon" voice) makes the voice. Grok Imagine animates only the stills of the first minute. CapCut assembles the video: voice → images matched to concepts → simple zoom/combo animations → auto-captions → filter + vignette → 1080p30 export. The tutorial skips the slow parts: generating the ~30–120 images, the bulk workflow, banner/description and upload. The top comment (39 likes) says these take 10–15 hours per video.

---

## 1. PIPELINE TABLE

Free/paid status is as shown in the video (March 2026). Status changes since then are flagged ⚠.

| # | Step | Tool (exact name · cost) | Input | What is done | Output | Time / cost (tutorial → realistic) | Tips & warnings mentioned | Timestamps |
|---|---|---|---|---|---|---|---|---|
| 0 | Competitor study | YouTube channel page + **vidIQ** browser extension (free tier) | Competitor channel URLs (Legend Investor Mindset, Nick Invests) | Note subs vs number of uploads, sort Videos by **Popular**, read top titles and durations | List of winning title patterns + proof the niche pays | 3 min on screen → 30–60 min | Look for "evergreen" videos that still gain views every hour. Long videos (44–52 min) = more ad slots. Titles are "relatable + FOMO" | 00:12–02:31, 03:12–03:33 |
| 1 | Channel name | **ChatGPT** (free); **Grok** as fallback "if names are bad" | "Prompt for channel Name" | Generate 30 names in 3 groups of 10, pick one, search it on YouTube, check vidIQ score | Channel name ("Adam Money Lab") | ~1.5 min → 10–15 min · $0 | Before you commit, check that no big channel already uses the exact name. You can ask for 300 or 3,000 names instead of 30 | 03:22–04:53 |
| 2 | Logo | **ChatGPT** → **Google Whisk** (Google Labs, free) at **1:1 Square** | "Prompt for Channel Logo" (no channel name needed) | ChatGPT writes 5 logo prompts; run each 2–3× in Whisk; if all are bad, tell ChatGPT what you want (here: a "slightly chubby" character on a white background) and get 5 new prompts | Square PNG mascot-logo (chubby man, glasses, green hoodie, gold coin) | ~2 min → 20–30 min · $0 | Results differ on every run, so regenerate. The first batch was rejected twice (green-hoodie youth, owl) | 04:55–06:41 |
| 2b | Banner / description | — | — | **Not demonstrated** | — | — | Nick Invests' banner (03:15) is a model: heavy black caps name + small tagline + mascot head on white | 03:15 |
| 3 | Video topics | **ChatGPT** (free); topic check on **YouTube search + vidIQ** | "Video ideas" prompt (no edits needed) | 50 ideas in 5 categories × 10. Then a follow-up asks for 30 more in one category ("financial trap"). Pick a topic with few or no long videos on YouTube | Topic → pasted into Google Doc ("The Small Upgrade Trap That Slowly Makes You Poor") | ~3 min → 20–40 min · $0 | Start with one category (series) rather than mixed topics. vidIQ score shown: 25 "Low" | 06:41–09:25 |
| 4 | Script | **Claude** (free plan; shown as best writer); ChatGPT works too | "Video Script" prompt + topic; length 1,800–2,200 words | Paste, run, then copy the text to Google Doc and delete headings/separator lines | ~1,850-word script with 6 sections (Hook → Ending) that opens with a question | ~2 min → 15–30 min incl. reading · $0 | The hook does not say "hi / welcome back" but asks a question. Change the word range to change the length (claims 1,800–2,200 words ≈ 8–10 min) | 09:25–11:38 |
| 5 | Voice-over | **Google AI Studio → Gemini 2.5 Pro Preview TTS**, *Single-speaker audio*, voice **Charon** (default was Zephyr), free, no API key | Clean script, in 2–3 parts | ChatGPT writes a **one-line style instruction**, which goes into "Style instructions"; paste the script, Run, download WAV | `download (4).wav` (10:56 long) | ~1.5 min → 20–40 min · $0 | Split long scripts into 2–3 parts or the output has **silent gaps** (seen at 16:20–16:35). Comment: the free tier only gives about 1 min per generation | 11:38–13:00 |
| 6 | Image prompts | **ChatGPT** | "Prompt for Images" + full script | 1 prompt per 2 sentences by default. The narrator then sends a follow-up for "1 concept = 1 scene" | 30 numbered scenes, each = 1-line description + image prompt | ~1 min → 10–20 min · $0 | You can change the density ("every two sentences"). Comment: long script + prompt gives a ChatGPT "message too long" error | 13:00–14:18 |
| 7 | Images | **Google Whisk**, **16:9 Landscape** | Scene prompts | Generate image 1 → put the best result in the **SUBJECT** slot → generate every other scene with that subject locked | ~30 PNGs (`Whisk_<hash>.png`), same mascot | Skipped on screen → 2–6 h for 100–120 images · $0 | "Don't miss this": the subject lock is the consistency trick, and the thumbnail uses it too. Bulk method is in a separate video. ⚠ Whisk banner: moving to **Flow**, Whisk usable only until **30 Apr 2026** | 14:10–15:10 |
| 8 | Cleanup / upscale | **cleanup.pictures**, **Pixelcut** upscaler | Bad/low-res images | Listed in description only; **never shown** | — | — | Probably for removing artefacts/watermarks and upscaling to 1080p (low confidence) | description |
| 9 | Image → video | **Grok** (grok.com/imagine → Upload image → *Animate Image*), free then | Stills of the **first minute** + the same image prompt | Upload still, paste the original image prompt, generate, download MP4 (a few seconds) | 3 clips `grok-vide_*.mp4` | ~0.5 min → 10–20 min | "No complex animation needed". ⚠ Comments: Grok "became paid", watermark appears | 15:10–15:55 |
| 10 | Edit | **CapCut** desktop (free + **2 Pro items** flagged at export) | WAV, Grok MP4s, Whisk PNGs | Voice on track → cut long silences by hand → Grok clips first (mute their audio) → place images per concept → animations → auto captions + caption style → filter "Renoir" + adjustment layer with Vignette → export | `0306` project → MP4 **6 m 44 s, ≈402 MB** | ~3.5 min → 2–4 h | Keep editing **slow-paced** ("for a child or an old man"). Image timing follows concepts, not a fixed clock. Images may be reused | 15:55–19:30 |
| 11 | Thumbnail | **ChatGPT** → **Google Whisk** 16:9 (subject = mascot) | "Thumbnail" prompt + topic | ChatGPT returns idea + 3–5-word text + image prompt; generate in Whisk; ask ChatGPT to **put the text into the image prompt** so Whisk renders "UPGRADE TRAP" | 16:9 thumbnail with baked-in text | ~1 min → 20–40 min | Clean composition, 1–2 elements, leave space for big text. If you don't like it, ask for new prompts | 19:30–20:38 |
| 12 | SEO | **ChatGPT** | "Prompt for SEO" + topic or script | One run | 5 titles (A/B test), description, ~24 tags, 15 keywords, 7 hashtags | ~1 min → 10 min | Use the 5 titles for YouTube title A/B testing | 20:38–21:50 |
| 13 | Upload | YouTube Studio | — | Not shown | — | — | (A comment asks about the "AI content" toggle; unanswered) | — |

**Tutorial cash cost: $0** (all free tiers). **Real labour: 10–15 h/video** (top comment, 39 likes). My estimate for a 10-min video done exactly this way: 6–12 h, mostly image generation, re-rolls and placing 100+ images by ear.

---

## 2. Step-by-step logic

### 2.1 Channel setup (03:12–06:41)

**Name prompt structure** (frame 03:36–04:12, doc at 03:39):
1. *Context*: a channel about personal finance, investing, passive income and money psychology, told through simple animated explainers, explicitly "similar to channels like Nick Invests". Goal: a memorable, trustworthy, simple name.
2. *Role*: expert brand strategist for finance/education YouTube names.
3. *Task*: 30 names.
4. *Rules*: short; 2–3 words; trustworthy/educational; branding like the reference channel; easy spelling; mix of "personal-brand" names (First-name + money word) and "authority" names.
5. *Output*: 3 sections × 10 (personal brand / finance authority / minimal modern).
6. *Audience line*: 18–40-year-olds who want simple money explanations.

Output pattern (04:15–04:36): personal-brand names follow `<FirstName> + Invests/Explains/Builds Wealth/Money Lab`. Validation (04:39–04:54): search the name on YouTube. vidIQ's search panel scored one candidate 37 and the chosen "Adam Money Lab" 56 ("Medium"). The narrator accepts it because no channel has the *exact* name, although a near-identical "Adam Smith Money Lab" channel showed up in the results (04:48).

**Logo prompt structure** (05:03–05:15): same context. "Logo = character only, no text". Role: brand-identity designer + AI image-prompt specialist. Task: 5 prompts. Design rules: no text; finance-themed; flat/simple cartoon; friendly, smart, trustworthy; works as a tiny profile picture; finance colours (green/blue/white, or a dark background with bright highlights). Each prompt must specify appearance, clothing/finance props, palette, illustration style and background. Whisk at **1:1** (05:45). Iteration loop: 2 rejected batches → a plain-language requirement to ChatGPT (06:24–06:30) → accepted mascot at 06:36–06:48 (chubby, glasses, green hoodie, gold coin, white background).

**Banner & description**: not covered. Generic style from Nick Invests' banner (03:15): white field, channel name in ultra-heavy black caps, short tagline underneath, mascot head on the right.

### 2.2 Topic research (00:12–02:31, 03:12–03:33, 06:41–09:25)

**How competitors are mined (manual):**
- Open the competitor's Videos tab, sort by **Popular** (03:12–03:33), and read subs ÷ uploads as a growth signal. Legend Investor Mindset had 46K subs from 24 videos (00:16); Nick Invests had 155K from 184 (01:21).
- Look for one outlier ("popular video ~1M views in 5 months", 01:33) and check it still gets views "every hour" (evergreen).
- Read title mechanics aloud. The $20,000 milestone title creates a curiosity gap, and it is relatable plus FOMO (01:48–02:05).

**How titles are reverse-engineered:** the competitor's top titles are turned into **variable templates** written into the topic prompt (07:03–07:19, heatmap 425–439 ≈ 0.45). The six patterns are:
- "Why everything changes after $X"
- "The X trap that keeps people poor"
- "The hidden cost of X"
- "Why most people stay broke"
- "What happens when you reach $X"
- "The financial mistake almost everyone makes"

**Topic prompt structure:** context → role (growth strategist + finance content researcher focused on high-CTR topics) → task (50 ideas) → rules (finance sub-themes; challenge beliefs; similar style to the reference channel; no generic "how to save money"; psychology, hidden traps, surprising truths; educational but clickable) → the 6 patterns → 5 output categories × 10 (money psychology; personal finance; financial traps; investing & wealth building; passive income & milestones) → audience.

**Selection logic:**
1. Pick one *category* and stay in it (a series): "financial trap", because everyone relates to wasted money and it carries FOMO (07:47–08:06).
2. Ask for more in that category (30 more, 08:08–08:50).
3. Search the candidate topic on YouTube. Prefer topics with **no or few long videos** (09:01–09:16). vidIQ showed "Overall score 25 · Low" (09:12).
4. Save to Google Doc.

### 2.3 Script (09:25–11:38) — prompt sections, then my improved template

**Tutorial script-prompt structure** (doc 09:42, ChatGPT 09:48–10:12, Claude 10:18–10:42):
1. *Channel context*: explains personal finance / money psychology / wealth / investing through animated explainers "similar to" the reference channel. Uses storytelling, psychology, simple examples, relatable life situations.
2. *Role*: expert YouTube scriptwriter for high-retention educational finance/money-psychology videos.
3. *Task*: full script on `[INSERT VIDEO TOPIC HERE]`.
4. *Script rules* (≈9 bullets): conversational storytelling; strong psychological hook; real-life money situations; very simple explanations; psychology insights; examples/metaphors/comparisons; build curiosity and reveal step by step; no jargon; educational-engaging tone.
5. *Structure*: **Hook** (relatable situation or surprising truth) → **Problem setup** (common belief/mistake) → **Core explanation** (step by step, examples and psychology) → **Insight** (the deeper mechanism) → **Practical takeaway** → **Ending** (thought-provoking conclusion).
6. *Additional instructions*: **1,800–2,200 words**; voice-over friendly; **no scene or camera directions**; don't copy existing scripts but keep the "same storytelling style and pacing".
7. *Audience line* (18–40).

Result (10:45–11:24): Claude (Free plan) returned "~1,850 words, voiceover-ready, structured across all six" sections as an MD artifact. The opening is a direct question to the viewer, followed by a stack of familiar micro-upgrades (phone, car, apartment). Post-processing: copy into Google Doc, strip the section headings and divider lines (11:27–11:36). The heatmap's all-time peak is 686–700 s (= 11:26–11:40, the finished script in the doc → start of Voice).

**Gaps in the tutorial prompt:**
- No target duration math (1,850 words ≈ 11–12 min at the measured ~160–170 wpm, not "8–10 min").
- No open loops or re-hooks.
- No fact sourcing, no numbers policy and no retention checkpoints.
- No sentence-length limit for TTS.
- No visual-beat markers for the editor.
- It names a competitor, which pulls the output toward imitation.

**Improved script prompt template (own wording):**

```text
ROLE
You write narration for <CHANNEL>, a faceless 2D-animated personal-finance channel.
Narrator persona: <PERSONA: e.g. "a calm older friend who learned money the hard way">.
Mascot on screen: <MASCOT NAME> (the viewer's stand-in; refer to him as "you" / "most people", never by name in narration unless noted).

GOAL
A <TARGET_MINUTES>-minute script (= TARGET_MINUTES × 155 words, ±5%) on: <TOPIC>
Core promise in one line (what the viewer will understand by the end): <PROMISE>
Audience: 18–40, beginners, English as a second language for many. Grade-7 reading level.

HOOK (first 45–60 words, ≤ 20 s)
- Open with a second-person question or a micro-scene the viewer has lived. No greeting, no channel name.
- State the stake (money lost / gained) with ONE concrete number in the first 15 seconds.
- End the hook with an open loop that is only closed in the final third.

BODY
- 4–6 "concept blocks", 150–300 words each. Each block = one idea, one everyday example, one number, one "so what".
- Every 60–90 s insert a re-hook line (a question, a reversal, or "but here's the part nobody mentions").
- Use at least 2 named mental models (e.g. hedonic adaptation) explained in one plain sentence each.
- Numbers: round, realistic US figures; mark every statistic with [SRC?] so a fact-checker can verify or replace it.
- Sentences ≤ 18 words; no parentheses, no abbreviations, numbers written the way they are spoken.

ENDING (last 120–180 words)
- Close the opening loop, give 3 practical steps, end on a reflective one-liner. No "like and subscribe" beg; one soft CTA max.

FORMAT
- Plain narration only. No headings, no stage directions, no emojis.
- Put "||" at every point where the visual concept changes (target: one "||" every 12–18 words).
- After the script, output: word count, estimated minutes at 155 wpm, the open loop and where it closes, and the list of [SRC?] claims.

DON'TS
- Do not imitate any existing channel's wording, catchphrases or recurring segments.
- No personalised investment advice; no specific tickers to buy; add nothing that sounds like a guarantee.
```

### 2.4 Voice (11:38–13:00)

- **Tool:** Google AI Studio → Playground → Gemini 2.5 Pro Preview TTS (`gemini-2.5-pro-preview-tts`), "No API Key" free mode, **Single-speaker audio** (12:00–12:06).
- **Style instruction:** ChatGPT is asked (in Hinglish, 12:15–12:18) for a one-line instruction for this script. The line used combines: clear, calm male voice; friendly and trustworthy; natural pacing; conversational; slightly energetic but educational; "YouTube animated finance explainer" (12:21–12:24).
- **Voice:** Charon (12:27–12:30), picked from a dropdown that defaulted to Zephyr.
- **Measured delivery** (final segment): ~75 words in 28 s (22:15–22:43) ≈ **160 wpm**. Integrated loudness **−18.9 LUFS**, LRA 2.8 LU. Inter-sentence pauses after trimming: **0.26–0.42 s**.
- **Warnings:**
  - Long scripts fail silently. The 10:56 WAV contained a silent stretch, which the narrator ignored (16:20–16:35). The finished video is only 6:44 against a ~1,850-word script, so content was probably lost.
  - Commenters report a ~1-min per-generation cap and ask for the voice name: voice is a visible demand driver (heatmap 700–755 ≈ 0.45–0.70).

### 2.5 Image prompts & consistent character (13:00–15:10)

**Tutorial image-prompt-generator structure** (doc 13:27–13:30, crop at 13:27):
- Context + role (storyboard artist / image-prompt engineer). "Do NOT generate images", prompts only.
- Rules: 1 prompt per 2 script sentences; each prompt depicts its script moment; one consistent character described as "a simple round-faced cartoon man" in the style of animated finance explainers; minimal flat vector; thick black outlines; clean white or light background; palette of green, blue, grey and white; finance props (piggy bank, coins, wallet, vault, charts, house, money stacks, laptop); scenes easy to animate.
- Style block repeated in every prompt: simple 2D cartoon finance-explainer illustration · flat vector · minimal shading · bold outlines · clean background · consistent character.
- Output format: `Scene N / short description / Image prompt`, continued to the end of the script. Script pasted at the end.

Follow-up used (14:18): "1 concept = 1 scene", answered with 30 scenes. Every prompt starts with the same fixed prefix ("simple 2D cartoon finance explainer illustration, round faced cartoon man…, casual blue shirt, flat vector style, thick black outlines, minimal shading, clean white background, simple colour palette blue green grey white…").

**Consistency trick (14:21–14:51):**
1. Paste scene-1 prompt, choose **16:9** (14:24).
2. Generate, pick the best image.
3. Click its small arrow and drag it into **SUBJECT** (14:36–14:42).
4. Every later prompt (and the thumbnail) is generated with that subject reference, so the same chubby man in the blue T-shirt appears throughout.

Images per minute:

| Source | Images per minute | Seconds per image |
|---|---|---|
| Tutorial default rule (1 per 2 sentences) | ≈ 7–9 | ≈ 6–9 |
| What was actually built | ≈ 31 clips in 6:44 ≈ **4.6/min** | mean ≈ 13 s, range ≈ 3 s to 42.7 s |
| Final 58-s demo | 7 segments | 10.5 / 3.1 / 8.4 / 11.0 / 9.8 / 8.3 / ≥6.3 → mean ≈ 8.5 |
| Competitor (Nick Invests) excerpts at 02:48–03:02 and 13:09–13:24 | ≈ 7–20 | ≈ 3–9, with reuse |
| Top comment | **100–120 images per 10 min** | ≈ 5–6 |

For the actual build: one Combo-animated clip lasted 42.7 s (18:02), and images were reused back and forth (17:12).

**Upscaling/cleanup:** cleanup.pictures and Pixelcut are linked in the description but never used on screen.

### 2.6 Image → video with Grok (15:10–15:55)

- **Rule:** convert **only the first minute's images** into video. The competitor does this ("in the beginning… converted into videos for a short period", 13:05–13:19). The rest stay stills with simple animation.
- **Steps:** grok.com/imagine → Upload image → "Animate Image" → paste **the same prompt that made the image** → generate → download (15:24–15:45).
- **Result:** gesturing-mascot clips. In the final, the first **≈22 s** (21:52–22:14) are animated clips, with a mean scene-change score of 0.33–0.41. From 22:15 on the scenes are near-static (0.035–0.06, 81–93 % of frames ≈ zero motion).
- The heatmap's second peak is here: 919–947 s ≈ 0.70–0.85. Animating the hook is the "secret" viewers rewatch.
- ⚠ Grok is now paid and watermarked (comments).

### 2.7 CapCut editing recipe (15:55–19:30): every visible setting

| Item | Setting seen | Time |
|---|---|---|
| Project | Name `0306`; 16:9 canvas (default), exported 1080P | 18:02, 18:52 |
| Voice | Imported WAV → own track; long silences cut manually (split + delete) | 16:07–16:34 |
| Video clips | Grok MP4s first, their own audio turned off | 16:37–16:45 |
| Image placement | Listen to voice; **one image per concept** (1–3 sentences); topic changes (e.g. car → bike) trigger the next image; reuse images freely; check the script if unsure | 16:58–17:50 |
| Clip transform | Scale 100 %, Position 0/0, Rotate 0°, Uniform scale on, Blend on; **no keyframes** | 17:54–17:57 |
| Animation | Animation › **In** presets (default duration **0.5 s**) on early short clips (arrow markers on the first ~5 image clips); Animation › **Combo** on a long clip with duration = full clip (**42.7 s**). Spoken advice: "Zoom In, Zoom Out" | 18:00–18:12 |
| Measured motion in final | One still with slow zoom-in, **+8.6 % over 10 s (≈0.86 %/s)** (22:15–22:25); other stills static; 2 transitions in 58 s (black shape wipe at 22:26, blur/glitch at 22:44); rest hard cuts | 22:15–22:50 |
| Captions | Text › **Auto captions**, Spoken language English, Bilingual none, Identify filler words off → Generate | 18:20–18:30 |
| Caption style | Captions › Text › **Effects**, "Apply to all main captions" ✔. An orange/red gradient style was tried (18:34) and rejected; the final is white text on a black rough-edged highlight with a word-by-word karaoke reveal | 18:32–18:48 |
| Filter | Filter track **"Renoir"** across the whole timeline | 18:49 |
| Adjustment | Adjustment › Custom adjustment ("Adjust1", full length) › Basic › Effects › **Vignette** raised (field reads "3…"; slider ≈35–40 % of travel); every other value 0 | 18:49–18:51 |
| Music | None added (final's pause floor ≈ −60 dBFS RMS = no audible BGM) | measured |
| Export | **1080P · Bit rate Recommended · H.264 · mp4 · 30 fps** · Optical flow off · Rec.709 SDR · "Sync to space" on → **6 m 44 s, ≈402 MB**; "Pro benefits: 2 items" (paid features in use) | 18:52–18:55 |
| Pace rule | "Slow-paced editing that a child or an old man can watch"; avoid fast editing | 18:27–18:36 |

### 2.8 Thumbnail (19:30–20:38)

- **Prompt structure** (19:35–19:50):
  - Context: thumbnails for animated personal-finance videos "similar to" the reference channel; simple cartoon character, bold text, minimal elements, clickable, readable on mobile.
  - Role: thumbnail strategist + image-prompt engineer; *do not generate the image*.
  - Rules include clean composition with **1–2 main visual elements** and **space for big bold text**.
  - Output: *Thumbnail Idea / Thumbnail Text Suggestion (3–5 words) / AI Image Prompt*. Topic pasted at the end.
- **Tool:** Whisk 16:9 with the mascot as Subject. First output had no text. The narrator asked ChatGPT to include the text in the prompt, and Whisk rendered it (20:22–20:30).
- **Layout of the result (20:30):**
  - Left 45 %: worried mascot, upper body, pointing right.
  - Right: a diagonal chain of 5 small icons (phone → coffee → car → apartment → wallet), joined by green arrows that climb to the upper right, with coins spilling from the wallet.
  - Top-left: "UPGRADE TRAP" in black ultra-bold sans, spanning ~65 % of the width.
  - White background, flat colours.

### 2.9 SEO (20:38–21:50)

- **Prompt structure** (09:24–09:27 doc, 20:41):
  - Context: SEO metadata for animated finance videos; maximise discoverability, CTR, ranking.
  - Role: SEO strategist for educational finance videos.
  - Rules: curiosity-driven titles similar to successful explainer channels; psychological triggers (curiosity, surprising facts, milestones); avoid generic; readable SEO description; natural keywords.
  - Output: 5 titles; description 2–3 paragraphs; 20–30 tags; 15 high-search keywords; 5–8 hashtags.
  - Topic or script pasted at the end.
- **Output seen** (21:00–21:10):
  - 5 titles built on the topic ("…Trap That Keeps People Poor", "Why Small Upgrades Slowly Make You Broke", "…Nobody Warns You About", "How … Quietly Destroy Your Wealth", "The Hidden Cost of …").
  - Description opening with a "most people believe X, but there is a hidden trap" frame.
  - ~24 broad tags (lifestyle creep, money psychology, personal finance…), 15 long-tail keywords, 7 CamelCase hashtags.

---

## 3. The finished-video style: measured, generic, plus an original mascot

### 3.1 What the tutorial's final video looks like (21:52–22:52)

| Attribute | Measurement |
|---|---|
| Canvas | 1920×1080, 30 fps, H.264 |
| Background | Warm off-white **#FAFAF7** (flat to ~70 % of the half-diagonal) |
| Vignette | Radial: #F8F8F5 at 70 % → #D3D3D0 at 80 % → #959592 at 90 % → **#525252** at the corners (22:32). Mid-edges only drop to #E7E7E4. Animated clips have near-black corners (#000, 22:10) |
| Character | Chubby, round-faced cartoon man; dark-grey hair tuft; **blue T-shirt (#347EB2 sampled)**; white skin with one flat grey shade; thick black outline (~6–8 px at 1080p); 3–4 heads tall; head ≈ 30–40 % of frame height in medium shots |
| Props / palette | Green (money, up arrows), red (expense arrows), gold coins, pink piggy bank, grey buildings; flat fills, no texture |
| Composition | Mascot centre or left third, props orbiting; whitespace ≥ 40 % of frame |
| Shot length | 3.1–11.0 s (mean ≈ 8.5 s) in the demo; competitor ≈ 3–9 s |
| Motion | First ~22 s: AI image-to-video gestures. Then stills: mostly static, occasional slow push-in ≈ 0.86 %/s; 2 stylised transitions per minute; otherwise hard cuts |
| Captions | CapCut auto captions; white rounded geometric sans; **black rough-brush highlight** behind already-spoken words, upcoming words ghosted; 2–6 words per chunk; lower third, text band ≈ y 81–89 % of height; cap height ≈ 45–50 px |
| Audio | Narration only, −18.9 LUFS integrated, LRA 2.8 LU, pauses ≤0.42 s, ~160 wpm |
| Grade | "Renoir" filter (slight warm/soft) + vignette adjustment layer |

**Competitor reference (Nick Invests excerpts, 02:48–03:02, 13:09–13:24):**
- Character: same flat-cartoon register, but a well-known TV-sitcom dad look-alike in a blue hoodie with a peach-skinned double chin.
- Captions: a single line of condensed, Impact-like **white text with black stroke + shadow**, ~8–11 words, bottom-centre at ≈ 88 % height.
- Background: white with a light grey vignette.
- Pacing: images change every ≈ 3–9 s and are reused.

Legend Investor Mindset instead builds on a real billionaire's photos/likeness (thumbnails 00:12–00:45), which is a different and riskier formula.

### 3.2 Original-mascot design brief

Our pipeline must **not** reproduce the sitcom-dad look or Nick Invests' character, and must not put "similar to Nick Invests" in any prompt. Brief:

- **Name / role:** "Penn" (working name), a 30-something everyman who keeps making the money mistakes the narrator explains. The viewer laughs *with* him, not at him.
- **Silhouette test:** recognisable as a black silhouette at 64 px. Egg-shaped head, wider at the bottom (not a round sitcom face). One upward hair **cowlick** shaped like a rising-chart arrow (signature). Small round ears. 3.5 heads tall. Short legs, slightly long arms for gestures.
- **Face:** two vertical oval eyes with thick eyebrows that do all the acting; small button nose; mouth only a line or an open "D"; **no double chin, no stubble**. Round tortoise glasses as an optional brand cue.
- **Wardrobe (fixed):** **mustard-yellow cardigan (#E0A526)** over a white tee, **navy chinos (#23395B)**, white sneakers. Never blue tee/hoodie (the competitors' colour).
- **Signature prop:** a small mint-green notebook ("the ledger") with a coin icon; it shows up in the logo, thumbnails and end screen.
- **Palette (whole channel):**
  - Line #1A1A1A
  - Paper #FAF8F3
  - Mustard #E0A526
  - Navy #23395B
  - Money-up mint **#2FB37A**
  - Loss coral **#E4572E**
  - Neutral grey #BFC4CC
  - Skin: 2 tones, flat
- **Line & render:** uniform 6 px outline at 1920 px width, flat fills, **one** cool-grey shadow tone, no gradients, no texture.
- **Recurring cast (differentiation):** "Future Penn" (same design, grey hair, cardigan faded) and **"the Leak"** (a small grinning drip-shaped creature) that personifies hidden costs. These give every video a recognisable gag system.

**Consistency strategy:**
1. **Canon sheet first.** Generate one turnaround (front, ¾, side, back), 12 expressions and 16 poses (pointing, thinking, shrugging, walking, holding phone, holding coin, shocked, sitting at desk…). Hand-pick and freeze 4–6 canonical reference PNGs.
2. **Reference-locked generation.** Every image call sends 2–3 canon refs plus a fixed STYLE_BLOCK and MASCOT_BLOCK text. Use Whisk-Subject-like features: Gemini/nano-banana multi-image reference, Flux Kontext / Redux, or Higgsfield reference elements / Soul ID. Lock the seed where the API supports it.
3. **Composite instead of re-generating.** Generate mascot poses on a plain background (or transparent via background removal) and props/scenes separately, then composite in Remotion. This cuts generations by ~40–60 % and almost removes character drift.
4. **Automatic QA gate.** Embedding similarity (CLIP/DINOv2) of the mascot crop vs canon ≥ a threshold set from 20 approved samples. Cardigan hue check (mustard in the top-third torso region). Reject and re-roll at most 2× before routing to a human.
5. **Optional LoRA.** After 30–40 approved images, train a small Flux LoRA on Penn for near-perfect identity at low cost per image.

---

## 4. Economics & risks

### 4.1 Image budget per 10 minutes

- Narration at 155–160 wpm → 1,550–1,600 words per 10 min.
- At **one visual every 5–7 s → 85–120 visuals/10 min.** This matches the top comment (100–120).
- With ~30 % rejects → **110–160 generations**.
- With pose-library compositing and planned reuse (10–20 % of shots reuse an earlier image) → **60–90 unique generations**.

### 4.2 Cost/time per 10-min video

Prices are approximate and must be re-checked before budgeting.

| Item | Tutorial way (free tools) | Our automated way (estimate) |
|---|---|---|
| Script (+ fact-check pass) | $0, 15–30 min | Claude API ≈ $0.20–1.00 (3–5 passes), 2 min machine + 10–15 min human read |
| Voice | $0 (AI Studio free; quota and silent-gap risk) | ElevenLabs ≈ 9–10k chars ≈ $2–3 at subscription rates (or Gemini TTS API, cheaper), 3 min |
| Images | $0 (Whisk), 2–6 h human | 90–160 gens × ~$0.02–0.05 (nano-banana / Flux class) ≈ **$3–8**, 10–20 min machine + 15 min human pick |
| Image→video | $0 (Grok, now paid/watermarked) | 6–10 clips × ~$0.20–0.60 ≈ **$2–5** |
| Edit / assembly | 2–4 h CapCut by hand | Remotion render 10–25 min machine; 15–30 min human review |
| Thumbnail + SEO | 30–60 min | ≈ $0.20–0.50, 10 min human pick |
| **Total** | **$0 cash, 10–15 h** | **≈ $8–18 cash, ≈ 1–1.5 h human** |

Tutorial revenue claims are unverified: finance RPM "$5–15", so 668K views × $5 ≈ $3,340 (00:45–00:57). Break-even on ~$15/video needs only ~3K views at $5 RPM. The real risk is views, not cost (comments: "made 4 channels none of them work", "getting views too difficult").

### 4.3 Platform / legal risks of copying a channel

1. **YouTube "inauthentic content"** (the YPP policy formerly called "repetitious content", renamed July 2025): mass-produced, template-identical videos can demonetise the *whole channel*. The tutorial's method, where the same six prompts all name the same competitor, produces exactly that. The second-most-liked comment (15 likes) raises this point.
2. **Reused content**: never insert competitor footage or re-voice their scripts. The tutorial's "keep the same storytelling style and pacing" clause pulls scripts toward paraphrase.
3. **Character IP**: the reference channel's mascot resembles a famous TV-animation character. Prompting "similar to" it invites copyright/trademark claims and derivative-looking output.
4. **Likeness / impersonation**: real-person formats (billionaire face, voice-alike) carry impersonation and misleading-content risk. A commenter claims such channels "got removed" (unverified).
5. **Synthetic-content label**: a clearly cartoon video generally doesn't need YouTube's "altered or synthetic" disclosure, but a realistic voice clone of a real person would. Keep a policy file.
6. **Finance compliance**: add a "not financial advice" line. Avoid tickers and guarantees, and flag every statistic for verification.
7. **Tool fragility**:
   - Whisk sunset (30 Apr 2026, banner at 05:39).
   - Grok Imagine went paid and watermarks output.
   - Free Gemini TTS quotas and silent-gap failures.
   - ChatGPT long-message errors.
   - CapCut Pro gates on captions ("not free for me").

### 4.4 How to differentiate (minimum bar)

- Original mascot + recurring cast + a recurring gag ("the Leak").
- **Real data, programmatic charts.** Remotion-animated bar/line charts with on-screen source tags, never AI-drawn charts with fake numbers.
- **Own voice**: a designed ElevenLabs voice (not the stock voice every tutorial follower uses) and a consistent narrator persona with opinions.
- **Format signatures**: chapter cards, a "trap meter" or "cost counter" overlay, a closing "3-step fix" card.
- **Variation**: vary structure (story-led, myth-busting, list, case study) and length (12–25 min) between videos. Never reuse the same opening line.
- Human edit pass on every script, plus fact-check against primary sources (BLS, Fed SCF, Census).

---

## 5. Automation blueprint for our stack

### 5.1 Pipeline (Claude = brain; ElevenLabs = voice; image model via Higgsfield/nano-banana/Flux; Remotion for assembly; ffmpeg utilities)

| Stage | Automated? | Tool / method | Input → Output (formats) |
|---|---|---|---|
| A. Channel bible | once, human-approved | Claude + human | → `bible.json` (persona, audience, palette hexes, STYLE_BLOCK, MASCOT_BLOCK, caption style, banned phrases, disclaimer) + `canon/*.png` |
| B. Competitor radar | **yes** | YouTube Data API v3 (`search.list`, `channels.list`, `videos.list`), daily snapshots | → `radar/YYYY-MM-DD.json` (views, age, views/day, outlier = views ÷ channel median, title, duration) |
| C. Topic generation | yes + **human pick** | Claude: abstract title patterns from top outliers into templates, generate 30 topics, score novelty vs YouTube search (count of long videos on the same keyword in 12 months) | → `topics.json` → chosen `topic.json` |
| D. Script | yes + **human read** | Claude (improved prompt §2.3), then a second pass "fact-check/simplify/retention audit" | → `script.md` (with `||` beat marks), `claims.json` |
| E. Voice | **yes** | ElevenLabs TTS *with timestamps* per paragraph (≤2,500 chars, previous/next-text stitching) | → `voice/part_##.wav` + `alignment.json` → ffmpeg concat → loudnorm (−16 to −14 LUFS) → trim pauses >0.6 s to 0.35 s → `voice.wav`, `words.json` |
| F. Scene plan | **yes** | Claude reads `script.md` + `words.json` and emits a scene list aligned to beat marks (target 5–7 s, hard max 10 s, min 2.5 s) | → `scenes.json` (schema below) |
| G. Images | yes + **human 1-click QA** | Higgsfield `generate_image_batch` (nano_banana_pro / flux) or Gemini image API with canon refs; 16:9 at ≥1920×1080 | → `img/scene_###.png` + `qa.json` (similarity scores) |
| H. Upscale / cleanup | yes (only if < 1920 px or flagged) | Higgsfield `upscale_image` / Real-ESRGAN; background removal for compositing | → overwritten PNGs |
| I. Image→video | yes | Higgsfield `generate_video` (Kling/Seedance/Veo class), 5 s, 1080p, only for hook scenes (first 30–60 s) + ~1 accent/min | → `clip/scene_###.mp4` |
| J. Assembly | **yes** | **Remotion** composition driven by `scenes.json` + `words.json` | → `render/final.mp4` (1920×1080, 30 fps, H.264, CRF 18–20, AAC 320k) |
| K. Captions file | yes | from `words.json` | → `captions.srt` (upload as a CC track too) |
| L. Thumbnail | yes + **human pick of 3** | Claude concept → image model (mascot ref, no text) → text set programmatically (Sharp/Satori, own font) | → `thumb_A/B/C.png` 1280×720 < 2 MB |
| M. SEO | yes | Claude | → `seo.json` (5 titles, description with chapters from scene/section times, tags ≤ 500 chars, 3–5 hashtags, pinned comment) |
| N. Upload | yes (scheduled, private first) | YouTube Data API `videos.insert`, `thumbnails.set`, `captions.insert` | → video id, log |

Human checkpoints: topic pick (2 min), script read (10–15 min), image QA grid (10–15 min), final watch at 1.5× (10 min), thumbnail pick (2 min).

### 5.2 `scenes.json` schema (per scene)

```json
{
  "id": 17,
  "start": 102.36, "end": 108.10,
  "text": "Each time, the upgrade felt reasonable.",
  "concept": "small upgrades stacking up",
  "visual_type": "still",            // still | i2v | chart | text_card | reuse
  "reuse_of": null,
  "mascot": {"pose": "holding_briefcase", "expression": "content_smile"},
  "props": ["briefcase", "coin_above_head"],
  "on_screen_text": null,
  "motion": {"type": "push_in", "from": 1.00, "to": 1.06, "pan": [0, -0.01]},
  "transition_in": "cut",            // cut | crossfade_8f | wipe (≤2 per minute)
  "image_prompt": "<STYLE_BLOCK> <MASCOT_BLOCK> ...scene...",
  "video_prompt": null
}
```

### 5.3 Remotion recipe (replaces the CapCut steps)

- `<Img>`/`<OffthreadVideo>` per scene.
- Ken Burns: scale 1.00 → 1.05–1.08 over the scene with easing, alternating in/out, ±1 % pan. **Never static > 4 s.**
- Transitions: hard cut by default; crossfade 6–8 frames at section changes; ≤2 stylised transitions per minute.
- Vignette overlay: radial gradient, transparent to 65 % radius, 35–45 % black at the corners (warmer and lighter than the tutorial's near-black corners).
- Captions:
  - Fed from `words.json`; chunks of 3–6 words, max 2 lines, centred.
  - Bottom of the text band at 88 % height.
  - Rounded bold sans (e.g. Nunito/Poppins Black, own licence).
  - Fill #FFFFFF, 10 px #1A1A1A stroke, active word highlighted in mascot mustard #E0A526 (our own look, not the tutorial's black brush).
- Audio:
  - Voice at −16 LUFS integrated, true peak ≤ −1.5 dBTP; YouTube normalises playback to around −14 LUFS.
  - Optional royalty-free BGM at −30 to −28 dB under voice with side-chain ducking. The tutorial used none.

### 5.4 What stays manual (and why)

Taste decisions only: topic pick, script approval, image QA, thumbnail choice. Everything the tutorial does by hand in CapCut can be scripted, including silence trimming, image placement by concept, zooms, captions, grade and export.

---

## Why it works

1. **It sells copy-paste prompts, not skills.**
   - 43 of 133 comments (32 %) ask for the PDF/prompts.
   - The most-replayed moments are where a usable artefact appears:
     - 686–700 s = 1.00 (the finished Claude script in the doc → free TTS setup)
     - 700–755 s ≈ 0.45–0.70 (AI Studio voice settings)
     - 919–947 s ≈ 0.70–0.85 (Grok animating the mascot)
     - 425–439 s ≈ 0.45 (title patterns in the topic prompt)
     - 796–837 s ≈ 0.42–0.50 (competitor animation + image prompt)
     - 1084–1098 s ≈ 0.53 (CapCut animation panel)
2. **It removes the two perceived blockers**: "I can't draw a consistent character" (Whisk Subject lock) and "I can't afford tools" (every tool free, Claude free plan shown on screen).
3. **The money proof comes first**: subs ÷ uploads, a 668K-view video × $5 RPM = $3,340, and 44–52-min videos with more ads (00:12–02:31). This frames the 20-minute walkthrough as an investment.
4. **The taught style itself works for the target channels** because the elements stack into a low-effort, high-RPM, evergreen formula:
   - relatable FOMO titles built on $X milestones and traps;
   - a calm, slow, "anyone can follow" edit;
   - one recurring cartoon everyman;
   - long durations.
5. **Honest weak spot**: the hidden labour (100–120 images, 10–15 h) is the top comment. The inauthentic-content warning is the second. The tutorial gets views by under-stating effort and risk, so our system's edge is automating exactly that labour and adding originality.

---

## Rules to copy

1. Write narration at **150–160 wpm**: target words = minutes × 155 (a 10-min video ≈ 1,550 words, not 2,000).
2. Open with a second-person question or relatable micro-scene. **No greeting** in the first 20 s; include one concrete $ number within 15 s.
3. Insert a re-hook (question, reversal, or "part nobody mentions") **every 60–90 s**; close the opening loop in the final third.
4. Keep sentences **≤ 18 words**, no parentheses, numbers spelled as spoken. Mark every statistic `[SRC?]` and verify before voicing.
5. Generate TTS in chunks of **≤ 2,500 characters** and auto-check every chunk for silent gaps > 1.0 s (the tutorial lost content to silent failures).
6. After TTS, trim pauses > 0.6 s down to **0.30–0.40 s**; normalise voice to **−16 LUFS** integrated, true peak ≤ −1.5 dBTP.
7. Plan **one visual per concept, 5–7 s on average**; never hold one visual > 10 s; never cut faster than 2.5 s. That is **85–120 visuals per 10 min**.
8. Reuse a previous image for **≤ 15 %** of shots, and only when the narration returns to the same concept.
9. Animate (image-to-video) **every shot in the first 30–60 s**, then at most **1 accent clip per minute**. Clips 4–6 s, no lip-sync.
10. Give every still a slow push/pull of **4–8 % scale over the shot** (≈0.5–1 %/s) with alternating direction. Use **≤ 2 stylised transitions per minute**; otherwise hard cut.
11. Background: warm off-white (#FAF8F3–#FAFAF7) with a radial vignette that starts at **≈65–70 % radius** and darkens the corners by 35–45 %.
12. Captions: auto from word timestamps; **3–6 words per chunk**, max 2 lines; bottom of the text band at **≈ 88 % height**; white bold rounded sans with dark stroke; highlight the active word in the brand accent colour.
13. Every image prompt = fixed STYLE_BLOCK + fixed MASCOT_BLOCK + scene description, with **2–3 canonical mascot reference images attached**. Never write a free-form character description per scene.
14. Lock the character on a canon sheet (turnaround + 12 expressions + 16 poses) **before** video 1. Reject any image whose mascot similarity to canon falls below the calibrated threshold; max 2 re-rolls, then human.
15. Never write a competitor's channel name, a TV character or a real person into any prompt (name, logo, topics, script, images, thumbnail, SEO).
16. Mine competitors weekly with the API: flag videos with **views ≥ 3× the channel median** and turn their titles into **variable templates**, never verbatim titles.
17. Validate each topic: prefer keywords with **≤ 5 long-form (> 8 min) videos in the last 12 months** on YouTube search; run topics as **series of 5–10** in one category.
18. Titles: one curiosity-gap pattern ($X milestone / "the X trap" / "hidden cost of X" / "why most people…"), **≤ 60 characters**, include the core keyword.
19. Thumbnail: **1 mascot + 1 idea object**, mascot on one side and object(s) on the other, **2–4 words** of text in ultra-bold caps covering ≥ 50 % width. Render text programmatically, not in the image model. Check legibility at 168×94 px.
20. Generate **3 thumbnail variants and 5 titles** per video; run YouTube Test & Compare.
21. SEO pack per video: description first 2 lines restate the promise, chapters from section timestamps, **10–20 focused tags (≤ 500 chars)**, **3–5 hashtags**, and a not-financial-advice line.
22. Export **1920×1080, 30 fps, H.264, CRF 18–20, AAC 320 kbps**; upload the SRT as a caption track.
23. Vary format (story / myth-bust / list / case study) so that no two consecutive videos share the same structure and opening line (inauthentic-content defence).
24. Budget gate: ≤ **$20** cash and ≤ **90 min** human time per 10-min video. If a stage exceeds 2× its budget, stop and log why.
25. Keep tool fallbacks configured for every stage (image, i2v, TTS), because free/consumer tools in the tutorial (Whisk, Grok) were discontinued or paywalled within months.

---

## Open questions / low-confidence

- **cleanup.pictures and Pixelcut**: linked in the description, never shown. Their exact role (watermark/artefact removal, upscaling Whisk output) is my inference.
- **Prompt PDF**: not downloaded (per brief). My structural summaries come from the Google Doc and ChatGPT text visible on screen; the PDF may differ.
- **Caption preset name** and the exact "Effects" style chosen are not legible. The final look (white text, black rough highlight, ghosted upcoming words) is measured from output frames, not from a readable preset label.
- **Vignette value**: the field shows "3…" mid-drag (18:50); the final intensity is inferred from pixel sampling only. "Renoir" filter intensity is unknown.
- **Zoom method**: only one still shows measurable zoom (+8.6 %/10 s). I could not tell whether it comes from a CapCut Combo/In animation or a manual effect; other stills appear static in the final.
- **Real length vs script**: the WAV was 10:56 but the export is 6:44. Silent TTS failure and silence trimming explain part of the gap; whether script content was dropped is likely but not proven.
- **Whisk output resolution** and **Grok clip length/resolution** were not measurable from the screen recording.
- **Revenue/RPM figures** ($5–15 RPM, $3,340 per video) are the narrator's claims and unverified. So is the comment about finance channels built on real people "being removed".
- **Competitor pacing** (3–9 s per image) is measured from short, browser-embedded excerpts (≈30 s total). Full-video statistics may differ.
- **Cost figures in §4** are approximate list-price estimates as of my knowledge. Verify ElevenLabs, image-model and video-model pricing before budgeting.
