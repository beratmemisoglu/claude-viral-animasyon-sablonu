# 03 — Script architecture, storytelling, retention devices and narration delivery

Analyst #3 of 8. Subject: "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)", AI Flow (@AIFlowOfficial), 22:52 (1372 s), 144,518 views, 4,498 likes, 133 comments.

**Evidence used:** the original-language Whisper transcript (`transcript_transcribe.txt/.json`, Hindi/Urdu in Devanagari with word timestamps) as the primary source. The English translation (`transcript_translate.*`) was used as a cross-check only, because it **dropped several lines**: the subscribe CTA at 2:58–3:11 and the second wait-time CTA at 12:44–12:50 are missing from it. I also used `silences.csv`, `loudness.txt`, my own 50 ms RMS / spectral / pyin / breath analysis of `audio16k.wav`, `heatmap.json`, `comments.json`, `channel_videos.tsv`, `v.info.json` (chapters, description), and about 120 sampled frames (contact sheets for 0:00–1:00, 2:40–3:15, 10:00–11:10, 11:20–13:02, 15:05–15:50, 18:50–19:30 and 21:12–22:48, plus single frames). Temp files are in `ROOT\tmp\a3\`.

Copyright: the narration is paraphrased throughout. Direct quotes are kept under 15 words and used only where the exact wording is the pattern.

---

## 0. One-paragraph verdict

The video is a **"proof → promise → 9-step recipe → reward" tutorial**. A guide ("bhai", meaning brother) talks the viewer through it at about 3.5 words/s with almost no dead air. Each step follows the same 10–12-beat loop, built around a **copyable asset** (one of 7 "PDF prompts"). A **single running example** ("The small upgrade trap that slowly makes you poor") is chosen on screen at 9:18 and carried all the way to a **58-second finished English video** that ends the tutorial with no outro.

The retention machinery is dense: 118 hand-coded devices in 1,310 s, a median of one every 10 s, with no gap over about 31 s.

- **Reassurance** comes about every 65 s.
- **Processing waits** are used for CTAs (script generation, voice generation, export).
- The PDF prompt pack is mentioned 7 times, but **how to get it is revealed only 9 s before the final video**: a like target, then Telegram/WhatsApp.

The most-replayed moments are not the talk. They are the **exact UI settings and readable prompts**: the voice setup in Google AI Studio is the global maximum, and the Grok image-to-video sample is second. Viewers use the video as a manual.

---

## 1. Macro structure

### 1.1 Chapter skeleton (creator's own chapters, from `v.info.json`)

| # | Chapter | Start–end | Dur (s) | % runtime | Role | Spoken words* | Gross WPM* | EN-token share** |
|---|---|---|---|---|---|---|---|---|
| 1 | Important | 0:00–3:12 | 192 | 14.0 % | Hook, proof, money math, promise, teaser, subscribe CTA | 611 | 204 | 20 % |
| 2 | Channel Setup | 3:12–6:41 | 209 | 15.2 % | Setup: name (prompt #1) and logo (prompt #2), with a failure→fix | 737 | 212 | 27 % |
| 3 | Video topics | 6:41–9:25 | 164 | 12.0 % | Research: topic prompt #3, category strategy, YouTube-search validation, **running example chosen** | 559 | 205 | 27 % |
| 4 | Script | 9:25–11:38 | 133 | 9.7 % | Script prompt #4, Claude (free), length knob, wait-time CTA #1 | 478 | 216 | 25 % |
| 5 | Voice | 11:38–13:00 | 82 | 6.0 % | Google AI Studio TTS: clicks, style instructions, speaker; wait-time CTA #2; 24 s voice sample | 210 | 217 | 37 % |
| 6 | Visuals | 13:00–15:10 | 130 | 9.5 % | Competitor visual analysis, image prompt #5, Whisk, character-consistency trick | 372 | 172† | 24 % |
| 7 | Videos | 15:10–15:55 | 45 | 3.3 % | Grok image→video for the first minute; 6 s motion sample | 115 | 182 | 28 % |
| 8 | Editing | 15:55–19:30 | 215 | 15.7 % | CapCut: silence cut, place clips and images, zoom, auto-captions, pacing rule; **FOMO re-injection during export** | 756 | 211 | 21 % |
| 9 | Thumbnail | 19:30–20:38 | 68 | 5.0 % | Thumbnail prompt #6 → Whisk → text-in-image | 223 | 197 | 23 % |
| 10 | SEO | 20:38–21:50 | 72 | 5.2 % | SEO prompt #7 (5 titles for A/B, description, tags), then **outro CTA block 21:11–21:50** | 255 | 213 | 17 % |
| 11 | Final Video | 21:50–22:52 | 62 | 4.5 % | **Reward / proof:** 58 s of the finished English AI video, then a hard end | — | — | — |

\* Words are Whisper word tokens from the original-language transcript, excluding non-narrator inserts (meme 2:16, teaser 2:48–2:58, voice sample 12:30–12:54, Grok sample 15:39–15:45, final video). Hindi/Urdu tokens include postpositions, so 1 Hindi token ≈ 0.92 English-translation words (4,316 vs 3,948).
\*\* EN-token share is a lower-bound heuristic: Latin-script tokens plus a list of Devanagari transliterations of English words (video, prompt, channel, copy, paste…).
† Visuals is under-counted: Whisper produced garbled text for 13:23–14:26.

### 1.2 Functional phases (re-cut on the spoken boundaries, not the chapter markers)

| Phase | Time | Dur | % | What happens |
|---|---|---|---|---|
| A. Hook + proof + money | 0:00–2:48 | 168 s | 12.2 % | Question → niche reveal → two outlier channels → RPM math → "why long videos pay" |
| B. Teaser + CTA | 2:48–3:11 | 23 s | 1.7 % | ~10 s preview of a finished AI cartoon (letterboxed, captioned), then subscribe with a 100K-before-2027 goal |
| C. Pre-production | 3:11–9:26 | 375 s | 27.3 % | Name, logo, topics (prompts #1–#3) |
| D. Production | 9:26–15:55 | 389 s | 28.4 % | Script, voice, images, motion (prompt #4, #5, and the voice-instruction trick) |
| E. Post-production | 15:55–18:53 | 178 s | 13.0 % | CapCut edit |
| F. Opportunity re-injection | 18:53–19:28 | 35 s | 2.6 % | "Still unsure about finance? Channels with zero finance knowledge make money; faceless; can be sold" |
| G. Packaging | 19:29–21:11 | 102 s | 7.4 % | Thumbnail, SEO (prompts #6, #7) |
| H. Outro CTAs | 21:11–21:50 | 39 s | 2.8 % | Rewatch/comment, ease claim, subscribe, like target → PDF on Telegram/WhatsApp |
| I. Final reveal | 21:50–22:52 | 62 s | 4.5 % | The finished video, cut mid-thought at 22:52 |

**First actionable step at 3:11 (13.9 % of runtime). First copyable payoff at 3:32.** The intro chapter is named **"Important"** rather than "Intro". That label discourages chapter-skipping past the proof and the CTA.

### 1.3 Where the payoffs are (things a viewer can copy)

| t | Payoff | Type |
|---|---|---|
| 3:32 | Prompt #1: 30 channel names in 3 categories (knob: ask for 300 or 3,000) | PDF prompt |
| 4:00 | "Insider" alternative: Grok if ChatGPT's names are weak | Tool tip |
| 4:32 | Search the name on YouTube before finalizing (live demo: "Adam Money Lab") | Check |
| 4:59 | Prompt #2: 5 logo prompts, no channel name needed | PDF prompt |
| 5:38–5:46 | Google Whisk, square aspect for the logo, generate 2–3 times | Settings |
| 6:14–6:35 | **Fix for bad logos:** tell ChatGPT your requirements (thicker character, white background) → 5 new prompts | Failure→fix |
| 6:58–7:06 | Prompt #3: 50 topics using title patterns ("Why everything changes after $X", "The X trap that keeps people poor"); readable on screen at 7:05 | PDF prompt |
| 7:36–8:04 | Strategy: start with one category (Financial traps), not mixed content, because it is relatable and FOMO-heavy | Strategy |
| 8:50–9:12 | Validation: pick a topic with no or few long videos; check by YouTube search | Check |
| 9:38 | Prompt #4: script prompt with a topic placeholder | PDF prompt |
| 10:03–10:18 | Use **Claude (free)**, judged the best script writer | Tool |
| 10:28–10:32 | Length knob: 1,800–2,200 words ≈ 8–10 min video | Number |
| 11:04–11:07 | Script lesson: open with a question, never "hi / welcome back" | Craft |
| 11:42–12:27 | **Google AI Studio (free):** Single Speaker Audio → paste → ChatGPT writes one-line style instructions → speaker "Charon" | Settings (global replay max) |
| 11:57 | Split long scripts into 2–3 parts | Warning |
| 13:23–13:56 | Prompt #5: one image prompt per concept; script pasted at the end; granularity knob | PDF prompt |
| 14:31–14:44 | **Consistency trick:** drag the generated character into Whisk's "subject" box so every image and the thumbnail share the character | Trick |
| 15:10–15:30 | Convert only the first minute's images to video with Grok, reusing the image prompt | Strategy and settings |
| 16:13 | Cut long silences in the voice track | Edit step |
| 18:02–18:22 | Zoom in/out on stills, CapCut auto-captions, caption template | Settings |
| 18:28–18:36 | Rule: slow-paced editing a child or an old man can follow | Rule |
| 19:35 | Prompt #6: thumbnail prompt (later "put the text inside the image") | PDF prompt |
| 20:45–21:05 | Prompt #7: 5 titles for A/B testing, description and tags | PDF prompt |

**Payoff density:** 7 PDF prompts plus about 14 concrete settings, tricks and rules over 18:39 of instruction (3:11–21:50). That is one copyable item every ~53 s, and one PDF prompt every ~2.7 min.

### 1.4 Why the final video sits at the very end
- **It is the reward that the outro CTAs stand in front of.** The narrator announces the final video at 21:11 ("before the final video, some important things"), then delivers the rewatch/comment ask, the subscribe ask and the like-target/PDF gate, and only then plays it (21:50). Viewers who stay for the reveal must pass through every CTA.
- **It closes the running-example loop.** The topic chosen at 9:18 comes back as a script (10:55), a voice sample (12:55), images (14:28) and a thumbnail (20:29), and finally plays as a finished video. Its first line echoes the hook formula taught at 11:04, which is also how the tutorial itself opened at 0:00. The tutorial practises what it preaches.
- **It was previewed** at 2:48–2:58 (a ~10 s finished-cartoon teaser). Promise early, deliver late.
- **There is no talking outro after it.** The video stops at 22:52 in mid-flow, which hands viewers straight to the end screen and the next video. Heatmap replay there is 0.00–0.11, which is normal for an ending.

---

## 2. Micro structure: the repeated step loop

### 2.1 Generic beat pattern (observed in every step chapter)

```
T  TRANSITION      "Now that we have X, it's time for Y"         (1–3 s)
N  NEED / WHY      why this step matters, often via the competitor   (3–10 s)
E  EMPATHY         "I know you don't have an idea right now" / "don't worry" (2–4 s)
P  PAYOFF SOURCE   "that's why I wrote this prompt in the PDF" / name the tool (+ "free") (3–5 s)
C  CLICK PATH      copy → open tool → paste → set 1–2 settings → run (10–25 s)
Z  ZERO-EFFORT     "don't change anything, just run it"            (2–3 s)
K  KNOB            default value and how to change it (30→300 names; 1,800–2,200 words) (3–8 s)
W  WAIT-FILL       (only if the tool is processing) CTA or motivation (5–12 s)
R  RESULT REVEAL   "now look…" + show the output (+ media sample)  (3–25 s)
X  TIP / WARNING / FAILURE→FIX   alternate tool, check, or bad output fixed (5–25 s)
V  VALIDATE/CHOOSE pick one, check on YouTube, save to Google Doc     (5–15 s)
T' NEXT TRANSITION
```

Measured frequencies across the tutorial (original transcript):
- **"After this" (iske baad):** 18×.
- **"After getting X…" (mil jaane ke baad):** 13×.
- **The full chapter-boundary formula "after X, now it's time for Y":** 5 of the 5 main step boundaries (6:42, 9:26, 13:01, 15:55, 19:29).
- **"Don't change anything in the prompt":** 5× (4:00, 5:18, 7:17, 10:40, 13:41).
- **"(now) look" (dekho):** 31×, about once every 42 s. **The full reveal phrase "now look":** 7× (5:25, 5:59, 6:36, 10:55, 11:35, 14:28, 15:50).
- **"Simple":** 17×.
- **The directive "you have to …" (aapko … hai):** about 45×.

### 2.2 Worked example A — Channel name (3:22–4:55, 93 s)
| t | Beat | Content (paraphrased) |
|---|---|---|
| 3:22 | T | Now let's talk about the channel name and logo |
| 3:25 | N | First we need a good name |
| 3:28 | E | "I know you have no good name idea right now" (mind-reading empathy) |
| 3:32 | P | That's why there's a special prompt in the special PDF |
| 3:38–3:46 | C | Copy all of it → open a chatbot, ChatGPT for now → paste |
| 3:47–3:55 | K | Default is 30 names; you can ask for 300 or 3,000 |
| 4:00–4:06 | X | "Let me tell you an insider thing": if ChatGPT's names are weak, use Grok |
| 4:06–4:13 | Z | Change nothing else, just run it |
| 4:17–4:24 | R | Now look: 30 unique names in 3 categories |
| 4:24–4:27 | V | Pick one, or ask for more |
| 4:32–4:50 | X+V | Warning: search the name on YouTube first. Live demo: no exact match, so it's usable |
| 4:53–4:55 | T' | Once you have a name, create the channel; next, the logo |

### 2.3 Worked example B — Voice (11:39–13:01, 82 s; contains the global replay peak)
| t | Beat | Content |
|---|---|---|
| 11:39 | T | After the script, generate the voice-over |
| 11:42–11:45 | P+E | Google AI Studio is "totally free", so no tension |
| 11:48–11:52 | C | Click Single Speaker Audio → paste the script into the box |
| 11:57–12:02 | X (warning, seeded) | Long script → split it into 2–3 parts; it can't do long text in one go. **Paid off at 16:19**, when the silent gap appears in the edit |
| 12:06 | N (importance flag) | Changing the style instructions is "very important" |
| 12:08–12:19 | C (sub-tool) | Ask ChatGPT for one-line voice instructions → paste them back (prompt readable on screen at 12:20) |
| 12:24–12:27 | K | Choose a good speaker; Charon for now |
| 12:34–12:41 | E | Render time depends on script length |
| 12:44–12:50 | W | Wait-time CTA: subscribe if you haven't… then a self-retracting joke (paraphrase: "leave it, I know you already have") |
| 12:30–12:54 | R | About 24 s of the generated English voice plays over a static AI Studio screen |
| 13:01 | T' | After the voice, it's time for visuals |

### 2.4 Worked example C — Video topics (6:42–9:26, 164 s)
| t | Beat | Content |
|---|---|---|
| 6:42–6:45 | T | After the logo, time to make videos; first we need topics |
| 6:49–6:55 | N | The competitor's topics are personal finance and money management, and they raise curiosity |
| 6:58–7:06 | P | My prompt bakes in his title patterns (patterns readable on screen at 7:05: **replay bump 0.45**) |
| 7:11–7:22 | C+Z | Copy → ChatGPT → paste → change nothing → run |
| 7:24–7:29 | R | 50 topics in categories |
| 7:36–8:04 | X (strategy) | Mixed content is possible, but start with one category ("financial trap"): relatable, FOMO, so people watch to the end |
| 8:06–8:22 | K+R | Ask for more in that category → 30 more |
| 8:27–8:47 | N (explain) | Why the examples work: every ordinary person relates |
| 8:50–9:12 | V | Fast results need topics with no or few long videos; check by YouTube search. None exist for the chosen one |
| 9:18 | **Running example locked** | "The small upgrade trap that slowly makes you poor" |
| 9:21 | V | Paste it into a Google Doc |
| 9:26 | T' | With good topics, it's time for the script |

---

## 3. Retention devices: timestamps and counts

### 3.1 Device inventory
Each device was hand-coded from the original transcript and frames. 118 devices between 0:00 and 21:50: mean gap 11.2 s, median 10 s, longest real gap about 31 s (19:36–20:07, thumbnail generation). A 41 s "gap" at 13:31–14:12 coincides with garbled Whisper output and is probably a coding artifact.

| Device | Count | Timestamps |
|---|---|---|
| **Direct question / mind-reading** | 6 | 0:00 opening question (which niche always has high RPM?); 0:05 "Yes, you're absolutely right" (answers for the viewer, brain-connection stock visual); 0:20 "guess what"; 2:07 "stop for a second and think why…"; 10:10 "if you're thinking I mean Claude — yes"; 15:58–16:02 "if you think editing is simple — yes, you're right" (callback to 0:05) |
| **Open loops / promises** | 11 | 2:34 main promise (make videos like Nick Invests); 2:39 future video about the first channel (cross-video loop); 2:43–2:46 "the video will be very interesting, sit comfortably"; 2:48–2:58 visual teaser of the output; 6:14 "I'll give you the solution" (closed 6:35); 10:03 "but wait a minute — another chatbot" (closed 10:14); 11:57 warning seeded (closed 16:19); 13:51 "you'll understand this during editing" (closed 17:25); 14:53 bulk-image video elsewhere; 21:11 "before the final video, important things"; 21:45 PDF after the like target (post-video loop) |
| **Reassurance** | ~20 (≈1 per 65 s) | 2:43, 3:28, 4:10, 5:18, 5:21, 6:12 (failure normalized: "this will happen to you too"), 7:17, 9:01, 10:40, 11:45 (free, no tension), 13:41, 15:45, 16:02, 16:48–16:51 (Claude used easy English, so you'll understand it), 17:05–17:12 (nobody will ask why an image stays long), 17:50–17:52 (sounds confusing, actually easy), 19:17, 20:41, 21:26 (even a child can start), 21:30 |
| **Warnings / importance flags** | 9 | 4:32, 5:50, 8:50, 11:57, 12:06, 14:12 ("important, don't miss this"), 15:10 ("very important job"), 16:19 ("one more thing"), 18:28 ("remember one thing every time") |
| **"Insider / secret / twist" framing** | 3 | 4:00 ("an insider thing"), 10:03 ("wait a minute"), 14:12–14:44 (consistency trick). The word "secret" is never used in this video |
| **Free-tool emphasis** | 4 | 10:18 Claude free version; 11:42–11:45 AI Studio totally free; 10:50 subscribing costs "not a single penny"; 19:15 faceless |
| **Money mentions** | 10 (7 in the first 2:31) | 0:45 RPM $5–15; 0:50–0:58 minimum-RPM calculation → $3,340 for one video; 1:02 lakhs of views; 1:50 "$20,000" title; 2:12 "the simple reason is money"; 2:16 WWE "Here comes the money" meme (3 s); 2:18–2:28 52/44-minute videos → more ads → more earnings; 19:07 goal is maximum money; 19:17 grow and sell the channel; 19:20–19:26 one working channel earns a year's income in a month |
| **Social proof** | 9 in the intro + 3 re-injections | 0:14 Legend Investor Mindset (24 videos → 46K subs); 0:31–0:35 first upload 2 months ago, viral 2 weeks ago; 0:38 668K views; 1:04–1:15 "not fake views — check likes and comments"; 1:20–1:23 Nick Invests (184 videos, 155K subs); 1:33–1:37 ~1M views in 5 months; 1:39–1:41 evergreen, views every hour; 1:50–2:02 title analysis (relatable + FOMO); 2:18 long durations. Re-injections: 6:49 and 13:05 ("if you watch our competitor…"), 19:09 a third faceless finance channel (Sticky Academy on screen) |
| **Humor / meme beats** | 6 | 0:01 Kung Fu Panda clip; 2:16 WWE money meme; 9:31–9:36 "if we write the script ourselves, AI will feel bad"; 10:50–10:54 "no compulsion" over a pointed-gun meme (frame 10:54); 10:55 "the script finished the moment you subscribed"; 12:49 self-retracting subscribe ask |
| **Subscribe CTAs** | 4 | 2:58–3:11 (knowing wink "yes, it's that same thing"; goal of 100K subs before 2027; Subscribe-button animation 3:04–3:06; "100K Subscribers" card 3:10); 10:46–10:58 (wait-time #1; "SUBSCRIBED" animation 10:51); 12:44–12:50 (wait-time #2); 21:31–21:41 (subscribe for easy tutorials of hard niches) |
| **Like CTA (target)** | 1 | 21:41–21:45: "200 Likes" card at 21:44, tied to releasing the PDF |
| **Comment / rewatch CTA** | 1 (both) | 21:15–21:24: everything was covered in detail; if confused, rewatch, then comment and I'll clarify there |
| **Off-platform** | 1 | 21:45–21:50: PDF on the Telegram and WhatsApp channels once the target is met |
| **PDF lead-magnet mentions** | 7 + gate | 3:32, 4:59, 6:58, 9:38, 13:23, 19:35, 20:45. How to get it is revealed only at 21:45 |
| **Cross-video links** | 3 | 3:17–3:20 channel creation taught in previous videos; 14:53 bulk Whisk video; 2:39 promised video on Legend Investor Mindset |
| **Respect-for-time line** | 1 | 14:49: generating every image on camera would make the video too long (then a time-lapse) |
| **Result-sample playbacks** | 4 + finale | 2:48–2:58 teaser (≈10 s); 12:30–12:54 voice (≈24 s); 15:39–15:45 Grok motion clip (≈6 s); thumbnails 20:07/20:29; finale 21:54–22:52 |

**Wait-time pattern.** "While it's generating" (jab tak) is used 4× (10:46, 12:44, 17:42 is a different usage, 18:53). Three times, a processing wait is turned into a CTA or a motivation beat: script generation → subscribe; voice render → subscribe; export → finance-FOMO re-injection.

**Transitions between chapters.** All five main step boundaries use the same "after getting X, now it's time for Y" sentence, and the screen switches tool at the same moment. There is no title card or stinger; the chapters exist only in the description.

### 3.2 Heatmap ("most replayed") vs narration

| Bucket (s) | Value | mm:ss | What is said / on screen | Reading |
|---|---|---|---|---|
| 0–110 | 0.02–0.12 | 0:00–1:50 | Hook and proof | Watched once; not replayed (normal) |
| 123–151 | 0.24–0.25 | 2:03–2:31 | Relatable + FOMO; WWE money meme; long videos → more ads | Mild replay on the money mechanism |
| 178–261 | 0.19–0.32 | 2:58–4:21 | Subscribe CTA → name prompt pasted into ChatGPT | Chapter-1 landing plus first prompt |
| 329–343 | 0.34 | 5:29–5:43 | Logo prompt → Whisk, square ratio | Settings |
| 384–439 | 0.35–**0.45** | 6:24–7:19 | Logo fix; **topic prompt patterns fully readable in Google Docs (7:05)** | Viewers pause to read and copy the prompt |
| 576–631 | 0.29–0.37 | 9:36–10:31 | Script prompt; Claude free; 1,800–2,200-word knob | Prompt and knob |
| **686–700** | **1.00** | 11:26–11:40 | Clean script in Google Docs (section headings visible: HOOK, PROBLEM SETUP, CORE EXPLANATION, INSIGHT, PRACTICAL TAKEAWAY, ENDING) → start of the **Voice** chapter (11:38) | Global maximum: Voice chapter landing plus readable script |
| 700–755 | 0.70→0.45 | 11:40–12:35 | **Google AI Studio clicks, style instruction (readable 12:20), speaker Charon** | The step the audience can't do alone (an English voice). Most-replicated step |
| 755–768 | 0.20 | 12:35–12:48 | Static screen while the voice sample plays | Drop: nothing to copy |
| 796–837 | 0.47–0.50 | 13:16–13:57 | Competitor visual style; image prompt per concept; paste the script | Prompt mechanics |
| 851–878 | 0.35–0.40 | 14:11–14:38 | Whisk + "don't miss this" consistency trick | Trick |
| **919–947** | **0.70–0.85** | 15:19–15:47 | **Grok image→video; same prompt; animated compound-interest sample** | Second peak: the "motion" trick plus the visual proof |
| 1015–1070 | 0.03–0.06 | 16:55–17:50 | Talking: images per concept, car/bike analogy | No new screen info, no replays |
| **1084–1098** | **0.53** | 18:04–18:18 | Zoom in/out demo (4.9 s silent demo) → auto-captions | Exact CapCut clicks |
| 1170–1310 | 0.09–0.24 | 19:30–21:50 | Thumbnail, SEO, CTAs | Low (packaging is less novel) |
| 1310–1372 | 0.00–0.18 | 21:50–22:52 | Final video | Watched once |

**Pattern.** The top 4 replay zones all coincide with (a) **exact UI click paths and settings**, (b) **prompts readable on screen**, and/or (c) **generated media samples**. Zones of pure explanation have the lowest replay. Because the PDF is gated, readable prompts on screen invite pause-and-copy behavior. The audience is non-native English speakers making English videos, and the **voice step** is their biggest barrier, which explains why the global maximum sits there. Voice-related comments ("which AI voice", "Google AI voice only does 1 minute, solution?", "how do you generate voice for long videos?") support this.

---

## 4. Language and delivery

### 4.1 Speed and density
- **Words per minute (original language):** 4,316 word tokens over about 1,190 s of narrator time gives **≈ 205–215 tokens/min** (gross 204–217 per chapter). Visuals and Videos read lower (172–182) because of Whisper dropouts and time-lapses. **English-translation equivalent: 186 wpm** (3,948 words). For an English remake of the same content, plan **≈ 3,700–4,100 words for 21 min of instruction**.
- **Sentence length (English translation, 356 sentences):** mean 11.2 words, median 10, 90th percentile 18. 35 % of sentences have ≤ 8 words. These are short, imperative, one-instruction-per-sentence lines.
- **Pauses (silencedetect, −35 dB / 0.35 s):** 26 in total, but **only 15 occur before 21:50**, in 21:50 of narration (0.7 per minute). The other 11 sit inside the 58 s English final video (11.4 per minute).
- **My 50 ms RMS analysis:**
  - About 89 % of tutorial time is above −35 dB (narration effectively continuous).
  - Gaps ≥ 0.20 s run at 13–21 per minute, almost all at phrase boundaries; gaps ≥ 0.30 s at 2–17 per chapter.
  - The final video has 27 % gap time against about 11 % in the tutorial.
- **Non-narration stretches ≥ 1.5 s (word-timestamp gaps):** only 9 in 21:50: 2:16 meme 3 s, 2:48 teaser 9.9 s, 4:13 1.6 s, 11:32 2.7 s, 12:30 voice sample 24 s, 15:04 time-lapse 6.5 s, 15:32 Grok sample 12.9 s, 18:06 zoom demo 4.9 s, 20:03 thumbnail generation 4 s. **Six of the nine are "show the result" moments.** Otherwise the voice never stops.
- **Breaths:** a breath-like-event detector (broadband, −40 to −18 dB relative to peak, 120–600 ms) finds **0.19 per minute in the tutorial narration vs 6.3 per minute in the final AI video**. Breaths have been removed: either breath-cut jump edits or a clean synthetic source. The spectrogram (62–76 s) shows hard phrase onsets with no pre-onset breath noise.
- **Loudness:** −19.4 LUFS integrated, **LRA 2.8 LU** (heavily compressed and flat). RMS medians are −23.8 to −25.6 dB in every chapter, so there is no energy arc. Delivery is constant and high-pace rather than dynamic.
- **Bed:** gap floors sit around −44 to −47 dB with tonal low-frequency peaks (187–312 Hz, spectral flatness 0.002–0.02) and horizontal harmonic lines in the spectrogram. That points to **a faint background music bed about 20–25 dB under the voice**, consistent with a commenter asking for the background track.
- **Pitch:** male, F0 median about 120 Hz (narrator) vs about 111 Hz (the "Charon" TTS in the final video).

### 4.2 Hinglish / Urdu code-switching
- **The base language is Urdu-leaning Hindustani.** Urdu lexical markers include the words for "only" (wahid), "achieve" (hasil), "purpose" (maqsad), "form" (surat), "besides" (ilawa), "trust me" (yaqeen mano) and "compulsion" (zor-zabardasti). Other clues: a "PK" region badge on YouTube (frame 3:02), a typed Roman-Urdu ChatGPT request (frame 13:32), and a commenter noting "you don't seem Indian". On-screen kinetic text is **Roman Urdu/Hindi plus English caps** (0:04 "RPM Hamesha HIGH rehta hai"; 0:08 "Finance Niche").
- **English share: ≥ 17–37 % of tokens per chapter (≈24 % overall).** It peaks in Voice (37 %), where UI labels dominate.
- **What stays in English:**
  - Every **tool name** (ChatGPT ×16, Claude, Grok, Google Whisk, Google AI Studio, CapCut, Google Doc).
  - Every **UI label** (Single Speaker Audio, style instructions, aspect ratio, auto captions, template, export, high quality).
  - **YouTube and money terms** (niche, RPM, views, viral, evergreen, content, upload, FOMO, relatable, A/B testing, SEO, faceless).
  - **Generic action verbs inside a Hindi light-verb frame:** copy/paste/run/generate/select/click + "kar lena hai / kar dena hai / karwana hai". "Prompt" appears about 50 times.
- **What stays Hindi/Urdu:** the reassurance and the relationship lines ("tension mat lo", "bhai", "chhodo yaar", "mujhe pata hai"), sequencing ("iske baad", "sabse pehle") and the deictic "dekho". **Rule:** emotional glue in the mother tongue, technical nouns in English.
- **Register:** second-person plural-informal ("aap … karo/kar lo") mixed with "bhai" (brother) 6× and "yaar" 1×. Friendly elder-brother mentor, never formal. There are no disfluencies: no "umm", no restarts, reduplications only ("achhe achhe", "dekh dekh").

### 4.3 Human voice or AI?
**Verdict: undetermined. The measurable signature is "processed or synthetic".** Confidence is low.
- **Points to AI or heavy processing:**
  - Zero breaths (0.19 per minute).
  - About 0 disfluencies across 4,300 words.
  - 89 % voiced time; LRA 2.8 LU.
  - Two commenters perceive it as AI or odd (one asks "the name of the AI voice you're using", one says the voice is "kinda weird").
  - The channel's audience openly discusses ElevenLabs voices (a comment names "Liam" and "Alice").
- **Points to a human read:**
  - Natural colloquial asides and reduplications.
  - Context-sensitive playful prosody around jokes (12:49, 10:55).
  - Urdu-specific word choices.
  - Wide pitch movement.
- For a production system this question doesn't matter much. What to copy is the **spec**: ~3.5 words/s, no breaths, no pauses > 0.35 s except before a reveal, LRA ≤ 3–4 LU, and a friendly, unhurried-sounding but fast mentor tone.

---

## 5. Storytelling

- **Arc (problem → opportunity → method → proof):**
  1. *Problem posed as a question* (0:00: which niche never has low RPM?).
  2. *Opportunity* with proof and money math (0:09–2:31).
  3. *Promise* plus a teaser of the outcome (2:34–2:58).
  4. *Method*: 9 steps with a single running example (3:11–21:11).
  5. *Mid-arc reminder of the stakes* (18:53–19:28).
  6. *Proof of result*: the finished video (21:50).
  It is a classic "guide-and-hero" (StoryBrand-style) structure.
- **Hero = the viewer.** The narrator positions himself as the guide who already did the work: "I designed this prompt so you don't even need a name" (5:21); "I read the whole script and didn't notice it end" (11:11). The viewer's obstacles are named and removed one by one:
  - no ideas → prompts
  - no English → "Claude used easy English" plus an AI voice
  - no editing skill → "even a child"
  - no budget → free tools
  - fear of failure → "this will happen to you too", then the fix
- **Antagonists:** low-RPM niches, blank-page fear, competition (solved by picking untouched topics), complexity, and the specific failure modes the video pre-empts (long-script silence, inconsistent characters).
- **Stakes and FOMO:**
  - Money is quantified early with conservative-sounding math (minimum RPM × views = $3,340).
  - **Recency** ("first video two months ago, viral two weeks ago") signals the window is open now.
  - **Smallness** (24 videos → 46K subs) says it's reachable.
  - **Evergreen** (views every hour) says it compounds.
  - The re-injection at 18:53 escalates to the boldest claim (a year's income in a month) at the exact point where effort feels highest (end of editing).
- **Community stakes:** "we must reach 100K before 2027". The channel had 31.6K subscribers on screen at 21:36. This turns subscribing into joining a mission.
- **How the end lands:** it ends on the artifact, not on a talking summary. The last spoken narrator line is essentially "here's the final video, bye". The narrated English cartoon then plays and ends mid-paragraph. The viewer's final impression is "I could make this", the strongest possible close for a how-to.

---

## 6. Reusable script template: "How to make videos like {SUCCESS_CHANNEL} with AI" (18–25 min)

### 6.1 Section list with target durations (scaled to a 22:00 master; keep the percentages for other lengths)

| # | Section | Target | % | Must contain |
|---|---|---|---|---|
| 0 | Cold-open question → niche reveal | 0:00–0:12 | 1 % | Viewer-directed question by 0:02; "you're right" mind-read; niche as kinetic text |
| 1 | Proof stack | 0:12–2:05 | 9 % | ≥ 2 outlier channels: upload count, subs, first-upload age, top video views, recency, min-RPM × views = $; anti-fake-views check |
| 2 | Why it pays (mechanism) | 2:05–2:30 | 2 % | One mechanism (length → more ads; evergreen); 1 meme beat ≤ 3 s |
| 3 | Promise + reassurance + teaser | 2:30–2:55 | 2 % | "In this video I'll teach you…"; "no tension"; ≤ 10 s clip of the finished output |
| 4 | Subscribe CTA #1 (mission) | 2:55–3:10 | 1 % | Numeric goal + date; subscribe animation |
| 5 | Step 1: Identity (name + logo) | 3:10–6:30 | 15 % | Prompts #1, #2; YouTube-search check; one failure→fix |
| 6 | Step 2: Topics | 6:30–9:15 | 12 % | Prompt #3 with title patterns readable ≥ 3 s; pick one category; validate by search; **lock the running example** |
| 7 | Step 3: Script | 9:15–11:25 | 10 % | Prompt #4; best free model; words→minutes knob; **wait-time CTA #2**; read the generated hook aloud |
| 8 | Step 4: Voice | 11:25–12:50 | 6 % | Free TTS; exact click path; style-instruction trick; speaker name; split warning; **wait-time CTA #3**; 15–25 s sample |
| 9 | Step 5: Visuals | 12:50–15:00 | 10 % | Competitor visual analysis; prompt #5 (one image per concept); consistency trick flagged "don't miss this" |
| 10 | Step 6: Motion | 15:00–15:50 | 4 % | Animate only the first minute; reuse the image prompt; 5–8 s sample |
| 11 | Step 7: Edit | 15:50–18:45 | 13 % | Silence cut; place media per concept (one analogy); zoom; auto-captions; pacing rule; callback to the earlier warning |
| 12 | Export wait = opportunity re-injection | 18:45–19:20 | 3 % | "Still unsure?" + 1 more channel + strongest (defensible) upside line |
| 13 | Step 8: Thumbnail | 19:20–20:25 | 5 % | Prompt #6; regenerate if weak; text in image |
| 14 | Step 9: SEO | 20:25–21:05 | 3 % | Prompt #7: 5 titles for A/B, description, tags |
| 15 | Outro CTA block | 21:05–21:45 | 3 % | "Before the final video…"; rewatch + comment; "even a beginner can"; subscribe reason; like target → resource unlock; off-platform channel |
| 16 | Final video reveal | 21:45–22:45 | 4–5 % | "Here's the final video. Bye." → 45–75 s of the finished video; no outro after |

### 6.2 Beat pattern per step (copy for every step 1–9)
`T (transition, 1–3 s) → N (why, ideally via the competitor, 3–10 s) → E (empathy/reassure, 2–4 s) → P (asset: "the prompt is in the PDF" / tool + "free", 3–5 s) → C (click path, 10–25 s) → Z ("don't change anything", 2–3 s) → K (default + knob, 3–8 s) → [W wait-fill CTA ≤ 12 s] → R ("now look" + output on screen ≥ 3 s, media sample if audio/video) → X (one tip, warning or failure→fix) → V (choose/validate/save) → T'`

### 6.3 Bank of 40 original lines (English; same functions as the source, new wording)

**Transitions (10)**
1. "The script is done — now let's give it a voice."
2. "Name and logo are sorted. Next question: what is this channel actually going to talk about?"
3. "With the voice ready, let's build what people will actually see."
4. "Images are done. Now we make the first minute move."
5. "That's every raw piece. Time to stitch it together."
6. "The video is ready — but nobody clicks without a reason. Thumbnail time."
7. "One last thing before upload: the words YouTube reads."
8. "Whatever the niche, step one never changes: identity first."
9. "Copy, open the chatbot, paste — you know the drill by now."
10. "Hold on to this topic. We'll use it in every step, right up to the final video."

**Re-hooks / open loops (8)**
11. "Stay till the end — I'll play the finished video we're building right now."
12. "This next setting is the one most people skip, and it's why their voice-overs sound flat."
13. "Remember this warning. In about five minutes you'll see what happens if you ignore it."
14. "I'll fix this in a second — first, look at what went wrong."
15. "There's a better tool for this exact job, and it's free. Guess which one."
16. "Judge the prompt by the result, not by how long it is. Look."
17. "Before the final video, two quick things that decide whether this works for you."
18. "This part only fully makes sense once we get to editing — park it for now."

**Reassurance (8)**
19. "Don't touch anything in the prompt. I've already done that work for you."
20. "If your first result looks bad, that's normal. Mine did too, thirty seconds ago."
21. "Weak English? No problem — the script is written in simple English on purpose."
22. "Nobody is timing how long each image stays on screen. Go with what feels natural."
23. "It sounds complicated when I explain it. On the timeline it takes two minutes."
24. "Every tool in this step is free. No card, no trial."
25. "If you can copy and paste, you can do every step in this video."
26. "Missed a click? Go back ten seconds — everything is on screen."

**Warnings / tips (5)**
27. "Before you fall in love with a name, search it on YouTube."
28. "Long script? Generate the voice in two or three parts, or you'll get silent holes."
29. "Pick topics with almost no long videos yet — that's where new channels win."
30. "Keep the edit calm: a kid and a grandparent should both be able to follow it."
31. "Use the same character reference for every image, thumbnail included."

**CTAs (9)**
32. "While the model is writing, tap subscribe — it's free, and you'll finish before the script does."
33. "The voice takes a minute to render. Perfect moment to subscribe if you haven't yet."
34. "We're aiming for {GOAL} subscribers by {DATE}. If this saved you a day of work, you're part of that."
35. "Let's give this video a like goal: {N}. When we reach it, the full prompt pack goes live in {COMMUNITY}."
36. "Stuck on a step? Comment the timestamp and I'll answer right there."
37. "If this niche feels hard, subscribe — every week I turn another 'hard' channel into easy steps."
38. "Channel creation is in my previous video; it's on screen now."
39. "Want to generate all the images in one go? There's a separate tutorial for that — top corner."
40. "Here's the finished video. See you in the next one."

### 6.4 Turkish adaptation
**Adaptation notes:**
- **Register:** informal "sen", warm mentor. "Arkadaşlar" for the group address and "dostum" or "kardeşim" sparingly, as the equivalent of "bhai". Avoid "siz".
- **Code-switch the same way the source does.** Keep tool names, UI labels and YouTube/money terms in English with Turkish suffixes after an apostrophe (prompt'u, CapCut'ta, export'u, RPM'i, voiceover'ı). Keep reassurance and sequencing in Turkish.
- **Money:** show USD RPM, with the TL equivalent in brackets.
- **Output language:** as in the source (Hindi tutorial, English deliverable), the deliverable can be an English video for US RPM. That makes the "you don't need English" reassurance and the voice step central. Expect the Voice step to be the replay peak.
- **Speed:** Turkish words are longer (agglutinative), so target about 150–170 Turkish words/min. That is roughly equivalent in information rate to 205–215 Hindi tokens/min, but it is an estimate; validate it on a pilot.

**10 sample lines (original, Turkish):**
1. "Sana bir soru sorayım: YouTube'da RPM'i neredeyse hiç düşmeyen niş hangisi?"
2. "Evet, tam düşündüğün gibi — finans nişi."
3. "Bu kanal sadece {N} video atmış ve {M} abone toplamış; ilk videosu da {X} ay önce."
4. "Hiç stres yapma, prompt'ta hiçbir şeyi değiştirmiyorsun: kopyala, yapıştır, çalıştır."
5. "Şimdi şuna bak — tek seferde otuz kanal adı, üç kategoriye ayrılmış."
6. "İngilizcen zayıfsa dert etme; script'i bilerek çok basit İngilizceyle yazdırıyoruz."
7. "Claude script'i yazarken sen de abone ol butonuna bas — tek kuruş ödemiyorsun."
8. "Bu uyarıyı aklında tut: script uzunsa sesi iki üç parçada üret, yoksa araya sessiz boşluklar girer."
9. "Ses de hazır olduğuna göre, sıra izleyicinin göreceği görsellerde."
10. "Bu videoya bir beğeni hedefi koyalım: {N}. Hedef dolunca tüm prompt PDF'ini Telegram kanalında paylaşacağım. Şimdi final videosu geliyor — görüşürüz!"

---

## 7. Why it works (hypotheses tied to evidence)

1. **It removes every barrier of a specific audience.** The audience is South-Asian aspiring creators who want USD RPM but lack English, ideas, skills and budget. Each step answers one barrier: prompts, "easy English", an AI voice, "even a child", free tools.
   - *Evidence:* the replay maximum sits on the free English voice setup (11:26–12:35). Voice questions recur in the comments. Only 1 of 133 comments complains about difficulty of understanding (speed).
2. **Proof before method, quantified.** 2:48 of outlier proof plus RPM math front-loads motivation; the step-by-step begins only after desire is built. The ~20× outperformance (144.5K vs a channel median of 7,250 views over 84 public videos) fits the "high-RPM niche plus named outlier channel" pull. Packaging details are covered by the packaging analyst.
3. **The video works as a manual.** Copyable prompts plus exact click paths make people scrub back. The replay peaks coincide with readable prompts and settings, and pure-talk zones have almost zero replays (16:55–17:50 = 0.03–0.06). Rewatching is even requested explicitly (21:18).
4. **The gated lead magnet converts attention into engagement.**
   - The PDF is mentioned 7 times, but the unlock is revealed only at 21:41–21:50, so anyone who wants it must reach the end.
   - The like target of 200 is shown on a card; actual likes are 4,498 (22×, a 3.1 % like rate).
   - **44 of 133 comments (33 %) ask about the PDF or prompts.** That is free comment volume, at the cost of some frustration ("likes completed, still no PDF").
5. **Single running example plus final reveal.** One topic carried end to end lowers cognitive load and creates a natural "will it turn out good?" loop that pays off in the last 62 s. The 10 s teaser at 2:48 set up that loop.
6. **Relentless micro-rhythm.** ~3.5 words/s, < 1 pause/min, a device every ~10 s, a reassurance every ~65 s, 31 "look" cues, and 6 humor beats clustered in the hook (0:01, 2:16) and around the wait-time CTAs (9:31–12:50). There is no dead air to drop off in.
7. **A mentor tone without ego.** He shows failures (bad logos 5:59–6:10, a silent gap in the voice 16:27–16:35), admits shortcuts ("I'm only teaching, so we'll ignore it"), and uses self-deprecating CTAs. That builds trust, and 25 praise/thanks comments follow.
8. **A series flywheel.** "How to make videos like X" is a repeatable franchise on this channel: 19 such titles, with a median of 25K views across the 15 visible ones (3.4× the channel median). Cross-video loops (3:17, 14:53, 2:39) feed the session.

## Rules to copy

1. Open with a question addressed to the viewer within the first 2 s, and answer it yourself by 0:08 with the niche name as on-screen kinetic text.
2. Name the first chapter "Important" (never "Intro") and spend 12–14 % of runtime in it before step 1. Step 1 must start by 3:15 on a 22-min video.
3. Present ≥ 2 outlier channels, each with exactly these five facts: upload count, subscriber count, age of first upload, top-video views, and recency of the viral video.
4. Convert views into money once, using the *minimum* RPM of the niche, and show the dollar result on screen. Add one anti-skepticism check (likes and comments prove the views are real).
5. Before step 1, show a ≤ 10 s teaser of the finished output, preceded by a promise sentence and a "no tension" line.
6. Put subscribe CTA #1 at 2:45–3:15 with a numeric community goal and a date. Keep it ≤ 15 s.
7. Lock one running example topic on screen during the topics step, and carry it through script, voice, images, thumbnail and final video (5/5 steps).
8. Deliver ≥ 7 copyable prompts (one per production step) and ≥ 12 concrete settings, knobs or tricks. That is one copyable item at least every 60 s of instruction.
9. Run every step through the beat loop T→N→E→P→C→Z→K→(W)→R→X→V→T′. Never skip R (show the output for ≥ 3 s) or X (one tip, warning or fix).
10. Use the same sentence template at every chapter boundary ("Now that we have X, it's time for Y"), together with a tool or screen switch.
11. Say "don't change anything in the prompt, just run it" at least 5 times, and say "now look" at every generation result (≥ 7 times).
12. Insert a reassurance line at least every 75 s (≥ 18 in a 22-min video). Include one about language ("easy English") and one about skill ("even a beginner/child").
13. Show at least one real failure→fix in the first third of the video.
14. Seed at least 2 warnings that pay off later on screen, with a callback to the earlier warning ≥ 3 min later.
15. Fill every processing wait (script generation, voice render, export) with a ≤ 12 s CTA or opportunity re-injection, at most 3 per video. Use self-deprecating wording on the second one.
16. Make at most 4 subscribe asks in total, none before 2:45.
17. Mention the resource (prompt PDF) at every step (≥ 6×), but reveal how to get it only in the last 60–90 s before the final video (like target on screen + off-platform channel).
18. Keep every prompt readable on screen for ≥ 3 s (zoomed, 11 pt+ at 1080p). Make every click path visible, cursor included.
19. Play generated media samples: voice 15–25 s, motion 5–8 s, finished video 45–75 s. Keep any other static screen ≤ 8 s.
20. Narrate at 200–220 words/min in Hindi/Urdu (≈ 180–190 in English; ≈ 150–170 in Turkish, an estimate).
    - Allow ≤ 1 pause ≥ 0.35 s per minute, except before reveals.
    - Remove breaths.
    - Target loudness range ≤ 4 LU, with a music bed 20–25 dB under the voice.
21. Keep sentences short: median ≤ 10 words, ≥ 30 % of sentences ≤ 8 words, one instruction per sentence.
22. Code-switch on purpose: tool names, UI labels and money/YouTube terms in English (20–35 % of tokens); reassurance, sequencing and "look" cues in the mother tongue.
23. Re-inject the opportunity once at 80–87 % of runtime with a third proof channel and the strongest *defensible* upside line. Prefer arithmetic from public numbers over income promises.
24. Insert ≥ 5 humor beats (meme ≤ 3 s or a self-aware joke): ≥ 2 in the hook/proof section and ≥ 2 attached to the wait-time CTAs.
25. End with "Here's the final video — bye", play the finished example, and stop. No outro talk after the reveal.

## Open questions / low-confidence

- **Human vs AI narration** is unresolved; see §4.3. Breath and disfluency absence could be editing (breath-cut jump edits plus denoise) or a voice clone.
- **The teaser at 2:48–2:58** (blue-hoodie cartoon, "BALANCE" phone) is probably the creator's own AI output. It may instead be a clip from a reference channel, and it does not match the final video's character.
- **The heatmap measures replays, not audience retention.** Drop-off per section is unknown, and the 686–700 maximum may partly be chapter-jump landings on "Voice" (11:38).
- **Whisper garbled 13:23–14:26** (Visuals) in the original language, so word counts, WPM and device coding there are under-estimated. The English translation silently dropped the CTAs at 2:58–3:11 and 12:44–12:50; both were recovered from the original.
- **The PDF link is now in the description.** It is unknown whether it was added after the 200-like target (comments suggest a delay).
- **The money claims** ($3,340 per video; "a year's income in a month") are the creator's statements, not verified. A production system should use arithmetic from public numbers and avoid guaranteed-income claims.
- **The music bed** is inferred from spectral evidence and one comment; its exact level and genre were not measured against a clean stem.
- **The Turkish WPM target** is an extrapolation and should be validated with a pilot recording.
- `channel_follower_count` in `v.info.json` reads 509, which looks wrong. The on-screen channel page at 21:36 shows 31.6K subscribers and 76 videos at recording time.
