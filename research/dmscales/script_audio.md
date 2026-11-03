# dmscales: script, on-screen text, audio and packaging spec

Scope: words, structure, sound and packaging only. Visual design and typography, motion and edit rhythm are covered in the other two reports.
Evidence: 5 videos (auto-caption VTT word timing, 1 fps contact sheets, cut frames, info.json, thumbnails). Work files (scripts, word timings, sentence files, measurements, spectrograms) are in `research/dmscales/work/script/`.

| id | title | dur | views | age (d) | views/day | like % | comments/1k |
|---|---|---|---|---|---|---|---|
| N-q-XLQymnU | The Entire Shorts Algorithm Explained in 180 Seconds… | 180 s | 705,107 | 214 | **3,295** | 5.57 | 2.1 |
| -fS8na576Jc | The Entire Longform Algorithm Explained in 300 Seconds... | 300 s | 368,426 | 201 | **1,833** | 5.78 | 2.0 |
| EQUn6IVAgCg | 10,000 Hours of YouTube Knowledge in 16 Minutes | 977 s | 99,356 | 169 | 588 | 5.77 | 3.6 |
| VQvIV__toUk | how to blow up a youtube channel (with one killer idea) | 337 s | 42,622 | 141 | 302 | 6.15 | 4.3 |
| AGkRkNuhO_o | The Entire TikTok Algorithm Explained in 120 Seconds… | 120 s | 29,594 | 181 | 164 | 4.66 | 2.9 |

The channel has 23.3K subscribers. The top video has about 30 times as many views as the channel has subscribers.

The channel uses two sub-formats, and the spec below is built on the first:
- **A. Scripted explainer** (N-q, -fS8, AGk, VQ). A tightly written voiceover, cut to one text card or proof picture per clause. Both hits use this format.
- **B. Knowledge dump** (EQUn). Unscripted talking ("like" appears 27.9 times per 1,000 words, against 1.2 to 3.8 in format A) over Minecraft parkour B-roll, with meme clips as chapter stings. It is mid-performing. Use it only as a "long cut" variant.

---

## 1. Script structure

### 1.1 Hooks: first 15 s, word for word (VTT)

| video | first ~15.5 s (74 to 77 words in every video) | hook type |
|---|---|---|
| N-q (705K) | "When you make a new channel, the first thing that happens is YouTube reviews your account to verify you're not a bot. If YouTube thinks you're a real person who posts good content, then they'll push your videos out to a seed audience of around 30,000 people to start building channel data. If your channel isn't trustworthy, your shorts won't be pushed out to anyone. This is called zero view jail. To avoid this," | Step-0 cold open |
| -fS8 (368K) | "When you start a new long form channel, the first thing that happens is YouTube reviews your account to figure out if you're a real person and you're worth pushing out. If your channel looks empty or suspicious, YouTube has no reason to trust you yet and won't push your videos out anywhere beyond search. To avoid this, you need to make your channel look legit from the start. Warm it up, brand it personally," | Step-0 cold open |
| AGk (30K) | "When you make a new TikTok account, the first thing that happens is the algorithm reviews it to figure out if it's safe to push out your content. During this time, TikTok tracks and reviews a ton of different things from your device to your internet connection to your screen size to your time zone and even how you behave in the app among many other things. If any of those match a previously banned or suspicious" | Step-0 cold open |
| VQ (43K) | "All it takes a single video to blow up a channel and everyone who says you need to stick with it for months is spewing you BS because all you need to blow up a channel is a single killer video. Throw everything you knew about YouTube away because in the next 5 minutes with no gatekeeping, no courses, or no BS mentorships, I'm going to teach you how to make this process easy as [cut, glitch 'FU-']" | Contrarian plus promise |
| EQUn (99K) | "All right, I'm going to cut all the BS. This is going to be the most valuable YouTube video you'll probably ever watch. So, you know, watch it if you want to. Don't watch it if you don't. You know, I don't really care because you're the one missing out. Someone called DM Skills on YouTube broke the YouTube algorithm in one >> [clip] to start the first thing we're going to cover is niches." | Arrogant dare plus third-party social proof clip |

Findings:
- The three "Algorithm Explained" videos have **no spoken promise and no intro**. The title is the promise. Second 0 is already step 1 of the lifecycle, and all three use the same template sentence:
  **"When you [make/start] a new [account type], the first thing that happens is [platform] reviews [it/your account] to [verify/figure out] if [you're real / it's safe to push]."**
- By 13 to 14 s the hook has named a **failure state with a jargon label** ("This is called zero view jail") and started the fix ("To avoid this,").
- The two other hooks attack a belief ("everyone who says… is spewing you BS") and promise to remove friction ("no gatekeeping, no courses, or no BS mentorships"). Both perform worse.

### 1.2 Beat sheet template (fits all five)

Times are shares of runtime, measured on N-q (180 s); the other videos are noted where they differ.

| # | beat | share | sentence frame (from the transcripts) | N-q example |
|---|---|---|---|---|
| B1 | Step-0 cold open | 0 to 3% | "When you make a new X, the first thing that happens is [system] reviews…" | 0:00 |
| B2 | Failure state plus jargon name | 3 to 8% | "If your X isn't [trusted], [bad outcome]. This is called [NAME]." | 0:10 to 0:14 |
| B3 | Fix list | 8 to 14% | "To avoid this, you need to A, B, **but most importantly**, C." Then a one-line why. | 0:14 to 0:24 |
| B4 | The one hidden principle | 14 to 25% | "All of this feeds into a hidden metric called X." / "[Platform], just like every other app, only cares about one thing: [goal], because more [time] means more ads watched and more money made. So every single decision the algorithm makes comes from that one goal." | 0:24 to 0:35 |
| B5 | Lifecycle walk, 3 to 5 stages | 25 to 70% | Each stage opens with a sequence clause: "Once you start posting…", "If the video's good enough…", "After your first viral video…". Inside a stage: mechanism, then analytics proof, then a myth flip ("A lot of people hate on X, but it's actually…"), then an instruction ("you need to…"). | 0:35 to 1:51 |
| B6 | The stats block | inside B5 | "There's three stats you need to be focusing on, with the first being X… The next stat… Beyond that, the algorithm tracks a ton of different things: a, b, c, d…" (rapid-fire list) | 1:29 to 1:51; -fS8 2:14 to 4:10 |
| B7 | Endgame plus warning | 70 to 88% | "Once your X is high enough… But when you reach this point, [try harder]. If you get lazy now…" | 2:21 to 2:39 |
| B8 | Pivot to the real need | 88 to 94% | "**But the most important thing you need is** a niche…" / "But it's pretty hard to [goal] if you can't [ideas]." | 2:39 |
| B9 | CTA loop | 94 to 100% | "So, to help with that, I have a playlist of a bunch of viral niches I find… These are niches I would use myself, so check it out. If you want a free personalized channel review or need help with anything, join the Discord." The video ends within 0.5 to 3 s of the last word: no outro and no end-screen talk. | 2:49 to 2:59 |

Where the end CTA starts: N-q 94%, AGk 87%, -fS8 95%, VQ 98%, EQUn 98%.
-fS8 also places a **mid-roll plug**: the niche playlist at 58% and a tool at 60%, plus a "side tangent" plug for the creator's Studio extension at 41%.
Affiliate tools are often named **on screen only** (AGk 1:46: "*best tool for finding viral niches ^ algrow (link in description)").

### 1.3 Section transitions and list intros (verbatim inventory)

- **Sequence clauses** carry the lifecycle and are the main transition device: "Once you start posting,", "As you post more,", "After your first viral video,", "Once your trust score is high enough,", "Then over the next 24 to 48 hours,", "Once the data is collected and the target audience is determined,", "As you continue to post more videos".
- **Self-asked question plus "Well,"**: "So how do we get YouTube to push your video as much as possible? Well, this comes down to the stats." VQ uses "Well," 10 times and has 17 question marks in 337 s.
- **Callbacks**: "Like I said before,", "And once again,", "Similar to shorts,".
- **List intros**:
  - "There's three stats you need to be focusing on, with the first being…"
  - "Your target audience is composed of three groups of people. Regular viewers,… The casual viewers,… Finally, the new viewers,"
  - "from your device to your internet connection to your screen size to your time zone and even…"
  - "To avoid this, A, B, but most importantly, C."
- **Contrast pivots**: "But most importantly", "But the most important thing", "Beyond that,", "Now, these two stats are the most visible things…"

### 1.4 Ending
The CTA is near-identical in all five videos (playlist plus free channel review plus Discord). There is no sign-off, except for the trailing "See you guys" in EQUn. On-screen-only goodbyes appear, for example "thank you guys for everything <3" (-fS8 4:58, not spoken). VQ ends on a deliberately awkward "and uhh" text card.

---

## 2. Sentence style (measured)

| metric | N-q | -fS8 | AGk | VQ | EQUn |
|---|---|---|---|---|---|
| words / min (whole video) | 282 | 265 | 277 | 281 | 271 |
| syllables / s (est.) | 7.1 | 6.8 | 7.0 | 7.0 | 6.8 |
| sentences | 48 | 78 | 29 | 116 | 252 |
| words / sentence, mean (median) | 17.6 (16.5) | 17.0 (15) | 19.1 (17) | 13.6 (10) | 17.5 (15) |
| longest sentence | 31 | 45 | 39 | 45 | 60 |
| "you/your" : "I/my/me" | 53:4 (13:1) | 79:17 (4.6:1) | 32:2 (16:1) | 79:20 (4:1) | 229:70 (3.3:1) |
| question marks | 0 | 2 | 0 | 17 | 12 |
| "like" (filler) per 1k words | 1.2 | 3.8 | 3.6 | 2.5 | **27.9** |

Note: ~275 wpm is far above normal narration (150 to 170). The read is fast, and breath gaps are edited out (see §5).

Writing rules derived from the transcripts:

1. **Second person, present tense, conditional**. "If you / your" appears 5 to 11 times per 1,000 words. The scripted hits are 13 to 16 times more "you" than "I".
2. **"I" only for proof or anecdote**: "The first long form video on my channel went viral", "my most recent video flopped".
3. **Name the system as an actor with motives**: "YouTube would rather push out someone else's video instead of wasting viewers on you", "YouTube doesn't want to take the risk". Cause is always money: "more time… means more ads watched and more money made".
4. **Invent or reuse jargon labels** for states and metrics: zero view jail, 30k view jail, trust score, honeymoon phase, seed audience, waves, impression "slot". A label is introduced with "This is called X" or "a hidden metric called X", and then reused verbatim.
5. **Concrete numbers in every stage**: "around 30,000 people", "200 to 500 people", "5 times bigger", "24 to 48 hours", "4 to 5%", "anything below 3".
6. **Casual register with light profanity and gamer slang**, used about once a minute and never more:
   - "easy as hell"
   - "spewing you BS"
   - "Screw the whole make a good video propaganda"
   - "a bunch of lazy chuds"
   - "easy as f[cut]"
   - "cuz", "wanna", "pretty simple", "a ton of"
7. **Myth flip**: "A lot of people hate on the 30k view jail, but it's actually a really good spot to be in because…"
8. **Recurring stock phrases** (reuse them):
   - "the first thing that happens is"
   - "To avoid this,"
   - "but most importantly,"
   - "only cares about one thing:"
   - "as … as possible" (4.7 per 1k in N-q, used for the retention-graph triad "as flat as possible, as high as possible, and get the initial dip as small as possible")
   - "every single"
   - "Picture it like this."
   - "Like I said before,"
   - "And once again,"
   - "Guess what?"
   - "I want to ask you, why did this video go viral when this one… didn't? Well, it's the angle they took."
   - "You know what everyone can't do?"
   - "And if you don't understand this, you're destined to fail."
   - "Well, the thing is, you can't."
9. **Deictic words that demand a picture** ("this", "these", "here", "like this", "one of these"): "it's due to one of these", "aim to get your VVSA and AVD up to here", "Doing CTA like this", "right around here". The script points, and the screen must show the referent (§3, rule 7).
10. **Sentence shape**: mostly one main clause plus one "because" or "if" clause (median 15 to 17 words). Short punch lines sit between them:
    - "YouTube just needs more data."
    - "If it fails, it stops there."
    - "Execution is the easy part."
    - "Everyone can edit."

---

## 3. On-screen text vs narration (the key rules)

### 3.1 What the screen does with the words (examples)

Times are spoken onsets (VTT). In the on-screen column, **bold** = red, _italic_ = green highlight, a plain underscore name in the notes = underlined.

| # | video, time | spoken | on screen | relation |
|---|---|---|---|---|
| 1 | N-q 0:00 | "When you make a new channel," | "when you make a **new channel**" next to a sad stick figure | verbatim chunk |
| 2 | N-q 0:07 | "then they'll push your videos out" | "then they'll **push** your videos out" | verbatim |
| 3 | N-q 0:09 | "…around 30,000 people to start building channel data." | "to start building **channel data**" | tail of the clause, verbatim |
| 4 | N-q 0:11 | "If your channel isn't trustworthy," | "ie: anything that makes you look like a bot" | added clarification |
| 5 | N-q 0:12 | (same) | Studio table screenshot plus "*not my screenshots" | disclaimer footnote |
| 6 | N-q 0:13.7 | "This is called zero view jail." | "ZERO **VIEW JAIL**:" header, then bullets "- happens when youtube doesn't trust you at all", "- **easy as hell** to get out of" | header plus added bullets |
| 7 | N-q 0:14.8 | "To avoid this, you need to use an aged channel, an older email with a lot of history," | "HOW TO FIX:" header, then "- aged channel (channel thats a couple years old, or one thats been warmed up by watching youtube normally for a bit)", then "- older email (a couple years old is optimal…)" | invented header; bullet per item; parenthetical adds info |
| 8 | N-q 0:18 | "but most importantly," | the card "but most importantly" alone, no colour | verbatim, transition card |
| 9 | N-q 0:20 | "enable third level feature eligibility." | earlier bullets shrink; "- enable **third level** feature eligibility (this will get you out of view jail instantly most of the time…)" | escalation of the last list item |
| 10 | N-q 0:24.8 | "All of this feeds into a hidden metric called trust score." | "all of this feeds into a **hidden** metric", then "**TRUST** SCORE:" | split into chunk plus header |
| 11 | N-q 0:27 | "Basically, how much YouTube trusts that when they push out your videos, people will actually watch them…" | "- the metric of youtube's **trust** in your **channel**, that will viewers **enjoy** the shorts you post" plus "*(its impossible to know your trust score as its an invisible metric)" | condensed definition plus footnote |
| 12 | N-q 0:31.6 | "Low trust means YouTube would rather push out someone else's video instead of wasting viewers on you." | "*why would youtube **waste** viewers on channels that post bad shorts, when they can push out channels that post good ones?" | rewritten as a rhetorical question |
| 13 | N-q 0:37 | "…to around 30,000 people." | analytics screenshot plus "to ~**30,000** viewers" | number made exact, with tilde |
| 14 | N-q 0:42 | "YouTube builds profiles on both the viewers and also the creators." | "Viewer" box: "- loves **animals** / - likes watching cars shorts / - swipes away on roblox". "Creator" box: "-posts **animal** shorts / -viewers who like animals love this channel" | invented concrete example |
| 15 | N-q 0:45 | "Every short you post will get shown to a different group of 30,000 people," | 3 stacked analytics cards plus "*different 30k people everytime" | proof plus condensed footnote |
| 16 | N-q 0:48 | "YouTube is just trying to find the perfect audience for your content." | stick figure with name tag and phone: "hmm, who would watch this all the way through…" | voiced thought of a viewer |
| 17 | N-q 1:00 | "If your short flatlines in the thousands, it's due to one of these." | screenshot plus "100 - 10,000" plus list "-Low quality short -Low trust score -Oversaturated niche -TERRIBLE VVSA+AVD" | deictic "these" resolved to a list |
| 18 | N-q 1:06 | "A lot of people hate on the 30k view jail," | brain image plus "my last 10 shorts all got 30k views :( youtube hates me", then "*DONT FALL FOR THIS TRAP" | myth voiced as a quote |
| 19 | N-q 1:37 | "aim to get your VVSA and AVD up to here." | "VVSA: <80% / AVD: 100% on shorts >30 seconds, 85-90% on shorts 40 - 1 min+" plus glossary "vvsa = viewed versus swiped away / avd = average view duration" | "here" resolved to numbers; acronyms glossed |
| 20 | N-q 1:46 | "If you ever do it, you can lose a lot of trust" | award-eligibility screenshot plus "trust me its not worth it 😓🙏" | personal aside, emoji |
| 21 | N-q 1:49 | "Doing CTA like this is actually against their policies." | example clip with arrow: "doing **CTA** like this / is actually **against** their policies" plus "*falls under spam and deceptive practices" plus "*not my video" | verbatim plus source footnote plus disclaimer |
| 22 | N-q 2:07 | "you need to be uploading every single day." | analytics plus "Quick note: dont schedule videos until you have a stable ~200k realtime… Also, NEVER DELETE or PRIVATE shorts…" | bonus tip, not spoken |
| 23 | N-q 2:33 | "If you get lazy now, then you might have to restart." | own channel graph plus arrow: "**stopped posting** for ~1.5 months due to vacation + putting time into a longform channel (that ended up failing 😓✌)" | personal proof, not spoken |
| 24 | -fS8 0:06 | "If your channel looks empty or suspicious," | "*If your channel looks like **spam**" plus channel screenshot "for example 😭🙏 ai slop" | synonym swap plus joke |
| 25 | -fS8 0:11.6 | "To avoid this, you need to make your channel look legit from the start. Warm it up, brand it personally, use an older trusted email, and enable third-level feature eligibility." | "HOW TO GET **YOUR VID** IN THE **ALGO**:" / "goal: make yt know your not a bot posting spam" / "Warm up:" plus a line / "Brand:" plus a line / "Use A Trusted Email:" plus a line / "Enable 3rd Level Feature Eligibility" | invented goal header; each spoken item becomes a bold sub-head with a small explanation |
| 26 | -fS8 0:35.8 | "…what your video is, who's it for, and whether it's safe to push." | "the **algorithm** is trying to figure out:" / "**what** your video is" / "**whos** the video for" / "will **advertisers** pay for ads" | list; 3rd item swapped for a sharper one |
| 27 | -fS8 0:59 | "…more ads watched means more money to YouTube." | stick figure: "*viewer spends more time on youtube ↓ *they watch more ads ↓" | causal chain with arrows |
| 28 | -fS8 1:10 | "it would rather push out someone else's content it actually understands" | brain plus "yea none of our viewers would watch this bs 😭" (bad thumbnail) vs "now this is peak, everyone would love this 😎" | algorithm's voice, A/B |
| 29 | -fS8 2:17 | "This is the percent of people who saw your video in their feed and actually clicked on it." | "**CTR**: the **%** of people who saw your video in their feed, and **clicked** on it" | near-verbatim definition |
| 30 | -fS8 2:40 | "Your click-through rate is determined by your thumbnail, your title, and your idea." | "**CTR** comes from:", then "thumbnail", "title", "idea" appear on their words, then "*also niche/audience", "+ the first 2 sentences of your description" | list plus extra items |
| 31 | -fS8 3:05 | "What percent should you be shooting for?" | "but whats an optimal CTR?" | rephrased question |
| 32 | -fS8 3:24 | "If you're losing too many viewers at the start, your hook is bad." | drawn retention curve, "Bad Hook" plus "*you didnt capture a viewers attention and give them a reason to stay till the end (payoff)" | diagnosis label plus footnote |
| 33 | -fS8 3:55 | "Engagement, what the comments are about, likes, shares, subscriptions gained or lost, returning viewers…" | "Main things the **algo** tracks:" plus one "- item" per spoken item, scattered in 2 columns | 1:1 list |
| 34 | AGk 0:04.9 | "…from your device to your internet connection to your screen size to your time zone…" | "during this **time**" / "-your **device**" / "-your **internet connection**" / "-your **screen size**" / "-your **timezone**", typed word by word, plus "*TikTok tracks **hundreds** of device signals when you **make** an account… VPNs dont work later" | verbatim build plus fact footnote |
| 35 | AGk 0:23.7 | "don't post anything for at least a couple days on a new page." | "dont post for a couple days [ ] [ ] [ ] [ ] [0] [ ] [0]" plus "*warmup your acc for ~**7 days** minimum before posting your **first** video…" | footnote is stricter than the VO |
| 36 | VQ 0:00 | "All it takes a single video to blow up a channel" | "all it takes", then analytics plus "*killer video" plus "*you can literally be monetized tomorrow morning, all it takes is just ONE good video" | fragment plus hype footnote |
| 37 | VQ 0:03 | "everyone who says you need to stick with it for months" | "and **everyone** who says:" plus quote "you need to stick with youtube for months before you succeed" plus meme image | quoted opponent |
| 38 | VQ 0:09 | "in the next 5 minutes with no gatekeeping, no courses, or no BS mentorships," | "because in the next 5 minutes / -no **gatekeeping** / -no **courses** / -no BS **mentorship**" | verbatim list |
| 39 | VQ 0:15 | "easy as—" | glitch "FU-" with an impact hit | censored punchline |
| 40 | VQ 1:07 | "But what if the idea looked like this?" | crowd doodle: "we wanna watch modded Roblox videos!" | idea shown as audience demand |
| 41 | VQ 1:18 | "Screw the whole make a good video propaganda." | "**screw** the whole make good video propaganda" plus thumbnail | verbatim |
| 42 | VQ 2:03 | "The audience I'm targeting is a bunch of lazy chuds" | "is a bunch of **lazy chuds**" plus tiny "*jk yall are goated" | verbatim plus apology footnote |

### 3.2 Measured proportions (catalogue of N-q captions, 0:00 to 3:00, about 60 caption elements)

| on-screen relation to the spoken words | share |
|---|---|
| **Verbatim chunk** of the current clause (3 to 8 words, filler dropped, lowercase) | ~55% |
| **Header or label** condensed from speech ("HOW TO FIX:", "TRUST SCORE:", "First viral video", "viewjailed", "outlier") | ~15% |
| **Asterisk footnote** with info not in the VO (caveat, source, extra tip, disclaimer, personal aside, joke) | ~20% |
| **Quoted thought** of a viewer, the algorithm or an opponent (in quotes, often with emoji) | ~10% |

- About 30% of all sampled frames in N-q carry an asterisk line, which is roughly one new footnote every 6 to 10 s.
- About 84% of text cards have at least one red word.
- Cards with no red are all transition or filler cards: "but most importantly", "and during this:", "you need to try", "so help with that", "so check it out", "this happens naturally".

### 3.3 Rules for the engine (narration line to on-screen text)

1. **Chunking.** Split each sentence at commas, conjunctions ("and", "but", "because", "so", "then") and prepositions after about 6 words.
   - One card per chunk: 3 to 8 words (median 6), held for about 1.2 to 1.8 s at 275 wpm.
   - A long clause shows only its **last** content chunk (example 3).
2. **Text form.**
   - All lowercase, except headers and the stressed words in rule 6.
   - Drop "basically", "you know", "like" and "pretty". Keep "so", "and" and "but".
   - Use casual spelling in footnotes: no apostrophes ("dont", "its", "whats"), "yt", "algo", "ie:", "~" for approximate numbers, and real typos are tolerated.
3. **Definitions.** "This is called X" or "a hidden metric called X" becomes a HEADER card "X:" in caps.
   - The distinctive word of X is red ("ZERO **VIEW JAIL**:", "**TRUST** SCORE:").
   - The header persists while 1 to 3 definition bullets ("- …") appear on their spoken words.
4. **Lists.**
   - Invent a header that ends with a colon: "HOW TO FIX:", "CTR comes from:", "Main things the algo tracks:", "the algorithm is trying to figure out:", "its hard to go viral when:".
   - Each spoken item adds a "- item" line **on its word**.
   - An item may carry a small parenthetical explanation (about 50% of the item's size).
5. **Escalation.** "but most importantly" or "but the most important thing" always gets its own clean card with no colour. Then the final item is shown large and the earlier items shrink (example 9).
6. **Colour and emphasis** (1 to 2 marked words per card, never more than 3):
   - **Red**: the concept noun or term (about 45%: "channel data", "retention", "niche", "target audience"), an evaluative adjective or adverb (about 25%: "hidden", "same", "bad", "hard", "significantly", "free"), the key action verb (about 20%: "push", "waste", "study", "double down", "monetized", "lowers"), or a number (about 5 to 10%: "30k", "24 - 48").
   - Never pronouns, articles or prepositions.
   - **Green highlight** marks good outcomes or goals (newer videos): "_push_", "_well_", "_scale_", "_suggested_", "_clearer_", "_most_", "_money_", "_link in description_", "SESSION TIME".
   - **CAPS plus red** marks a stressed intensifier: "REALLY", "EXACTLY", "VALUABLE", "REALLY BAD", "EVER", "MANY", "NEVER DELETE".
   - **Underline** marks the contrast target: "more than any other stat" (any other stat underlined), "rather than risking showing yours" (yours underlined), "all give the algorithm more context" (context underlined).
7. **Deictics.** If the VO says this, these, here, like this, one of these or right around here, the shot **must** show the referent (screenshot, list, number or example). Keep the spoken words as the caption, and add a hand-drawn red arrow pointing at the referent.
8. **Numbers** become digits, with "~" for "around" and ranges as "100 - 10,000". Thresholds become a stat card ("VVSA: <80%"), with a small glossary footnote for every acronym.
9. **Footnotes** start with "*", sit centered under the main element at about 40% of the caption size, and use the same red-keyword rule. Use them for:
   - a caveat ("*its impossible to know your trust score")
   - a stricter or extra tip (example 35)
   - a source or proof note ("*first short", "*a channel of mine")
   - a disclaimer: "*not my screenshots", "*not my video", "*not sponsored", "*link in description"
   - a jokey aside with an emoji: "*jk yall are goated", "(that ended up failing 😓✌)"
10. **Quotes.**
    - Viewer thoughts: lowercase in "double quotes" next to a stick figure.
    - The algorithm's thoughts: next to a brain image.
    - Opponent or myth views: next to a meme image.
    - Write a quote whenever the VO describes what someone wants, thinks or decides ("YouTube is just trying to find the perfect audience" becomes "hmm, who would watch this all the way through…").
11. **Questions.** VO statements of a problem may be rewritten on screen as questions ("*why would youtube waste viewers…?", "but whats an optimal CTR?").
12. **Profanity.** The VO is cut before the word, and the screen shows a glitch fragment ("FU-") or a censored word ("f*ck" only on the thumbnail).
13. **Not spoken, screen only.** Thank-yous, plugs and tool names, and "Quick note:" tips can live on screen only. Plan at least 1 per 30 s.

---

## 4. Sentence-type to visual mapping and screen-time shares

### 4.1 Mapping table

| sentence type (VO) | picture | caption |
|---|---|---|
| "When you [do step]…" (the viewer acts) | **stick figure** ("you"), with expression matching outcome (neutral, sad, happy, holding phone) | verbatim chunk |
| platform claim with a number or result | **real analytics or UI screenshot** (dark card on white) with red hand-drawn arrow or circle | verbatim or condensed, plus footnote |
| "This is called X" / definition | **header text card** "X:" plus bullets | header plus definition plus "*" caveat |
| fix or how-to list | **text card list** that builds ("HOW TO FIX:") | 1 line per item |
| transition ("but most importantly", "and during this:", "so naturally") | **plain text card**, no colour | verbatim |
| what the algorithm wants or thinks | **realistic brain image** plus quote, with thumbnails it judges | invented quote |
| what a viewer wants or thinks | **stick figure plus phone or thought cloud** plus quote | invented quote |
| supply and demand, audience, competition | **crowd doodle** (tight cluster) plus "Watch my video!" creator figures | label quotes |
| two options or two titles | **side-by-side**: two boxes, two thumbnails, "BRANDED vs CASH COW", "Viewer vs Creator" | labels plus one-line verdict each |
| "the graph looks like…" / shape claim | **drawn chart** (hand line on axes) or real retention graph plus red arrows | label ("Bad Hook") plus footnote |
| growth or "go viral" | **green zig-zag line** across frame (newer videos) | none or short |
| "only cares about one thing: money" | **icon** (green $, platform logo, people icon, lightbulb, globe) | short label "(tiktok loves this)" |
| example of someone else | **their thumbnail or channel** | "*not my video" / "*this channel is an example" |
| personal proof or anecdote | **own Studio screenshot** | "*my first video went viral", plus emoji |
| hype punchline or profanity | **kinetic glitch type** ("FU-", "BEST") | the word itself |
| CTA | **own channel page or playlist screenshot**, Discord logo | "*subscribe: i update this playlist everyday (~40 viral niches already)", "*link in description" |

### 4.2 Screen-time share by picture type
Method: dominant picture classified every 2 s from the 1 fps contact sheets.
- N-q: 90 samples. -fS8: 150. AGk: 60. VQ: 169.
- EQUn: 75 samples from 5 of 33 sheets (0:00, 2:00, 5:30, 9:00, 13:00).

| type | N-q 705K | -fS8 368K | AGk 30K | VQ 43K | EQUn 99K |
|---|---|---|---|---|---|
| text-only card (white bg) | 33% | **42%** | 8% | **36%** | 24% |
| screenshot plus caption, arrow or footnote | **31%** | 26% | 15% (with bare) | 15% | — |
| bare screenshot or UI | 22% | 17% | (in above) | 9% | — |
| stick figure, brain or silhouette plus text | 3% | 9% | **28%** | 10% | 3% |
| crowd doodle | — | — | — | 10% | — |
| icons or logos (TikTok, $, people, bulb) | — | — | 18% | 5% | — |
| diagram or drawn chart | 2% | 1% | 15% | (green line in T) | — |
| thumbnail grid or side-by-side | 1% | 3% | — | 7% | 3% |
| footage, meme clip or photo (incl. Minecraft B-roll) | 7% | 1% | 15% | 6% | **71%** |
| transition frame (shatter, blur) | — | — | — | 2% | — |

Reading the table:
- **The two hits are 53 to 75% screenshot proof plus 33 to 42% text cards, with only 3 to 9% character drawings.** The "proof density" (a real analytics screenshot roughly every 4 to 6 s) is the signature.
- The later videos (AGk in May, VQ in June) shift to icons, figures, crowds and kinetic type, with fewer proof screenshots. Both perform much worse.
- For our code-drawn engine, keep a **proof stand-in at 40 to 55% of screen time**: drawn "analytics cards" with real-looking numbers, circled and arrowed. The rest should be text cards (about 35%) and figures, brain or crowd (about 15%).

---

## 5. Audio spec

### 5.1 Measurements (ffmpeg ebur128, volumedetect, silencedetect; numpy RMS and FFT on 50 ms frames)

| | N-q | -fS8 | AGk | VQ | EQUn |
|---|---|---|---|---|---|
| integrated loudness | -19.1 LUFS | -19.9 | -19.6 | -17.3 | -21.2 |
| loudness range (LRA) | 3.7 LU | 3.4 | 5.0 | 4.8 | 7.5 |
| true peak | +0.1 dBTP | -0.0 | +0.1 | -0.0 | -0.4 |
| silences < -40 dBFS, ≥ 0.25 s | 0 | 1 (0.34 s) | 0 | 1 (0.25 s) | 3 (1.2 s total) |
| silences < -55 dBFS | 0 | 0 | 0 | 0 | 0 |
| speech frame median (RMS) | -21.9 dBFS | -22.9 | -22.0 | -20.9 | -24.3 |
| bed proxy (min of each 400 ms window, median) | -30.0 | -31.3 | -28.7 | -29.9 | -31.1 |
| bed vs voice | **~8 dB under** | ~8.4 | ~6.7 | ~9.0 | ~6.8 |
| sub 25 to 65 Hz, pauses minus speech | +0.8 dB | -1.1 | -1.1 | +0.1 | +0.1 |
| est. bed tempo (autocorrelation, < 150 Hz envelope) | ~73 BPM | ~97 | ~79 (158/2) | ~88 | ~73 |
| hard cuts with a sub-bass hit (vs random times) | 5.5% (vs 5.8%) | 5.3% (vs 7.8%) | 3 of 5 (vs 16.5%) | **38.6% (vs 11.0%)** | 6.6% (vs 3.5%) |
| word-onset gap median / p90 | 0.16 / 0.40 s | 0.16 / 0.44 | 0.16 / 0.44 | 0.16 / 0.44 | 0.20 / 0.44 |
| gap after sentence end (onset to onset), median | 0.40 s | 0.44 | 0.44 | 0.36 | 0.40 |

What the numbers mean:
- **Music bed under the entire video**, from frame 1 to the last frame. No stretch ever falls below -55 dBFS, and the auto-captions tag "[music]" 5 to 51 times per video.
  - Spectrograms (`work/script/spec_*.png`) show sustained tonal lines at 500 to 1,000 Hz (keys or pads) plus continuous sub-bass. The bed reads as a mellow lo-fi or chill-trap instrumental at about 75 to 95 BPM.
  - The track itself cannot be identified from the data.
- **No ducking.** Sub-bass energy is the same under speech and in pauses (±1.1 dB), so the bed is a static level about 7 to 9 dB RMS under the voice. In loudness terms: voice about -19 LUFS, bed about -27 to -29 LUFS.
- **Voice is heavily compressed and loud**: LRA 3.4 to 5 LU, peaks hitting 0 dBFS (no true-peak ceiling). Close, dry mic with no audible room.
- **Pauses are edited out.** The median gap between word onsets is 0.16 s. After a full stop, the next word starts about 0.4 s after the last word's onset, which leaves roughly 0.1 to 0.2 s of actual silence. Gaps over 1 s occur at most once per video, so the result is a breathless 270 to 280 wpm read.
- **SFX are absent in the two hits** (cut hit-rate equals the random baseline).
  - The June video (VQ) adds **sub-bass impacts on about 39% of hard cuts**, about 3.5 times chance, including a broadband glitch impact at 0:15.5 on "FU-".
  - The TikTok video has hits on 3 of 5 hard cuts.
  - There are no pops or dings: text cards change silently.

### 5.2 Build spec

- **Voice**:
  - ElevenLabs, young male, casual and confident, slightly monotone and matter-of-fact (not hype).
  - Target 265 to 280 wpm, so use speed about 1.15 to 1.2.
  - After render: trim every inter-sentence silence to 0.10 to 0.20 s and inter-clause silence to 0.05 to 0.12 s. Never leave a pause over 0.35 s, except a deliberate 0.5 s beat after a punchline.
  - Processing: compressor 4:1, then limiter. Voice integrated loudness -18 to -19 LUFS. True peak ceiling -1.0 dBTP (they clip to 0; we should not). Target LRA 3 to 5 LU.
- **Music**:
  - One continuous lo-fi or chill-trap instrumental, 75 to 95 BPM, with keys or pad plus soft drums and sub-bass. No vocals, no drops.
  - Starts at 0.00 at full bed level, with no fade-in and no intro.
  - Runs to the last frame and is cut with the video (an optional 0.3 s fade).
  - Level 8 to 10 LU under the voice (about -27 to -29 LUFS short-term), static, no sidechain ducking.
  - On long videos (over 5 min), swap the track at chapter boundaries (EQUn's bed level varies by section).
- **SFX** (the "classic" profile used by the hits): none.
  - "Modern" profile (VQ): a sub-boom or impact on kinetic-type transitions and on the censored punchline, about 1 per 10 to 15 s, peaking about 3 dB under voice peaks.
  - A soft whoosh is allowed on blur or shatter transitions.
  - Never use pops or dings on text cards.
- **Master**: -16 to -18 LUFS integrated (they sit at -17 to -21), true peak -1 dBTP.

---

## 6. Packaging

### 6.1 Titles

| formula | example | result |
|---|---|---|
| **"The Entire [System] Explained in [N] Seconds…"** (N = exact runtime in s, trailing "…") | Shorts 180 s, Longform 300 s, TikTok 120 s | 705K, 368K, 30K |
| "[huge number] Hours of [Topic] Knowledge in [N] Minutes" | 10,000 Hours… in 16 Minutes | 99K |
| lowercase "how to [big outcome] (with one [adj] [noun])" | how to blow up a youtube channel (with one killer idea) | 43K |

The creator explains the hit himself (VQ 2:20 to 2:33): the title "pushes the idea that this is everything you need to know". It filled an unsaturated angle ("algorithm explanation", not "how to go viral") for an audience he calls lazy, so the video is short.

**Why N-q overperformed** (11 to 20 times the views per day of AGk and VQ, 1.8 times -fS8):
1. Core-audience topic (Shorts creators) plus the "entire / in 180 seconds" completeness-and-speed promise.
2. A Step-0 cold open with no intro (hook = first lifecycle step).
3. Named pains that match search queries. Tags include "why do my shorts stop at 30k views", "how to escape 0 view jail" and "30k view jail".
4. The densest proof: 53% screenshots.
5. A thumbnail showing real money ($9,505.60 circled) plus "easy as f*ck".

AGk used the same formula but is off-niche (TikTok, for a YouTube-automation audience), with a descriptive thumbnail text ("tiktok explained") and an icon-heavy look. It got 5% of the views.

### 6.2 Thumbnails (1280×720, from .webp)

- **Layout (4 of 5)**: white or off-white background.
  - Left 50 to 55%: one real dark-UI analytics card (views or revenue), with the key number **circled by a red hand-drawn ellipse**.
  - Right: 2 to 3 words in heavy black lowercase sans, set on 2 staggered lines. The second line is red and offset right.
  - A **curly red hand-drawn arrow** loops from the words back to the circled number.
- **Texts**: "easy as / f*ck" (705K), "stupid / easy" (368K), "tiktok / explained" (30K), "you're **one video** away" (43K, dark full-bleed graph variant), "**no one** will tell you this…" (99K, collage of 6 analytics cards).
- **Rule**: the text is an *attitude claim about difficulty* ("easy"), never a topic label. The proof number is the hero. The creator says the white background stands out because his audience browses in dark mode.

### 6.3 Description (identical skeleton in all 5)

1. "In this video, I explain [X]'s entire [algorithm] to help you understand what makes a video go viral, and why most don't. You'll learn the entire purpose of the [X] algorithm, what each stat means, what [X] tracks and values, and how to make your video stand out by optimising things you didn't even know affect your videos performance."
2. Credibility: "I've been doing [youtube automation] for close to 2 years, and during that time I've generated hundreds of millions of views, almost 500k subscribers, and 5 figures in earnings across my many channels. [X] is my passion, and I'm going to share exactly what I did, what I learned, and how YOU can go viral … and make a lot of money from it :)"
3. Affiliate tool links (`?ref=`).
4. "Join the discord (i don't sell a course/mentorship) if you want to talk to me or network with other creators: <link>"
5. "Subscribe so you don't forget about me, I have some insanely valuable videos planned 👀"
6. Chapters: Intro / "[Jargon] Explained" / "How To …" / Outro, one about every 20 to 60 s on short videos.
7. 3 to 6 CamelCase hashtags.
8. Tags: 10 to 25, including long-tail problem queries.

---

## 7. Sample: 60-second script in this format (original topic)

**Title:** The Entire Credit Score System Explained in 60 Seconds…
**Thumbnail:**
- White background. Left: a drawn "credit report" card reading "Score **812**", with the number circled by a red hand-drawn ellipse.
- Right: "lowkey" in black and "easy" in red, staggered, with a curly red arrow back to 812.
- Use a generic card, not a real bank's UI.

**Voice:** 266 words, about 59 s at 270 wpm, with sentence gaps trimmed to 0.15 s.
**Music:** lo-fi bed from 0.00, 9 LU under the voice, no ducking, no SFX ("classic" profile).

Legend for the on-screen column: **red**, _green highlight_, CAPS for stressed words, a plain underscore name in the notes means underlined, "*" marks a footnote.

| # | t (s) | narration (VO) | on screen | picture type |
|---|---|---|---|---|
| 1 | 0.0 | "When you apply for your first credit card," | "when you apply for your **first credit card**" | stick figure holding a card, neutral |
| 2 | 1.6 | "the first thing that happens is the bank pulls your credit file" | figure on the left, drawn "credit file" folder on the right: "the bank **pulls** your credit file" | figure plus doc icon |
| 3 | 3.9 | "to figure out if you're safe to lend to." | brain-style "bank" icon plus quote "is this person gonna pay us back..?" | algorithm-voice quote |
| 4 | 6.2 | "If you've never borrowed anything, there's no file to pull." | empty folder with a dashed outline, plus "*no loans, no cards = **nothing** to score" | icon plus footnote |
| 5 | 8.4 | "This is called being credit invisible." | "CREDIT **INVISIBLE**:" / "- the bank cant see you at all" / "- **easy** to fix tho" | header card plus bullets |
| 6 | 9.7 | "To fix this, open one starter card or become an authorized user on someone's old card," | "HOW TO FIX:" / "- starter card (low limit, made for no-history people)" / "- authorized user (you get added to a parent's old card)" | building list |
| 7 | 13.4 | "but most importantly," | "but most importantly" | plain transition card |
| 8 | 14.3 | "let it report for at least six months, because that's the minimum before a score even exists." | earlier bullets shrink; "- let it **report** for **6+ months**" plus "*thats the minimum before a FICO score can be generated" | escalated final item plus footnote |
| 9 | 17.7 | "Every lender only cares about one thing: will you pay them back." | "every lender only cares about **one thing**:", then green $ icon plus "(will you _pay them back_)" | text card, then icon |
| 10 | 20.6 | "So every number in your score comes from that one question." | drawn score dial (300 to 850) with needle; arrow plus "*every number = that **one question**" | drawn chart plus footnote |
| 11 | 22.8 | "Thirty-five percent of it is payment history." | "SCORE BREAKDOWN:" / "**35%** payment history" (pie slice grows) | header plus drawn pie |
| 12 | 25.1 | "One payment that's thirty days late can sit on your report for seven years." | the pie stays; "*1 payment **30 days** late = on your report for **7 YEARS** 😭" | proof stand-in plus footnote |
| 13 | 27.5 | "Thirty percent is utilization, basically how much of your limit you're using." | 2nd slice: "**30%** utilization" plus a drawn card "$300 / $1,000 limit" with "30%" circled red | pie plus drawn card |
| 14 | 30.5 | "Keep it under thirty percent, and under ten if you want the best scores." | "UTILIZATION:" / "- under **30%** = fine" / "- under **10%** = _best scores_" | stat card |
| 15 | 33.3 | "The rest is how old your accounts are, how many new ones you open, and your mix of credit." | remaining slices appear on their words: "**15%** account age", "**10%** new credit", "**10%** credit mix", plus "*FICO weights, VantageScore is a bit different" | 1:1 list plus caveat |
| 16 | 37.5 | "Every time you apply for something new, the lender does a hard inquiry," | "HARD **INQUIRY**:" / "- the lender checks your file when you **apply**" plus "*stays on your report 2 years" | header plus footnote |
| 17 | 40.2 | "and too many in a short time make you look desperate." | 5 card icons, then the bank-brain quote "why does this guy need 5 cards this week 💀" | algorithm-voice quote |
| 18 | 42.8 | "So, never close your oldest card," | "**never** close your _oldest_ card" plus "*it keeps your average account age high" | text plus footnote |
| 19 | 44.6 | "pay the full balance every month," | "pay the **full** balance every month" plus "*not just the minimum" | text plus footnote |
| 20 | 46.0 | "and don't apply for five cards in one week." | "dont apply for **5 cards** in one week" | text card |
| 21 | 47.5 | "Once your score is high enough, lenders stop testing you and start competing for you." | green zig-zag line rising through the frame, then "lenders stop **testing** you / and start _competing_ for you" | growth line plus text |
| 22 | 50.8 | "But it's pretty hard to stay on top of all this if you can't see what's on your report." | "but its pretty **hard** to stay on top of all this", then a stick figure squinting at a blurred report | text, then figure |
| 23 | 54.2 | "So, to help with that, I made a free checklist," | "so to help with that", then a drawn checklist page plus "***free** checklist: every step in this video" | text, then page plus footnote |
| 24 | 56.6 | "it's in the description, so check it out." | "so check it out" plus "*_link in description_" | plain card plus footnote |
| 25 | 59.0 | (end) | "thank you guys <3" (screen only, 0.6 s), then cut | screen-only sign-off |

Checks against the spec:
- Step-0 cold open: shot 1.
- Jargon label by about 9 s: shot 5.
- Fix list with "but most importantly": shots 6 to 8.
- One hidden principle: shots 9 to 10.
- Lifecycle and numbers: shots 11 to 21.
- Pivot and CTA at 85 to 100%: shots 22 to 24.
- Picture mix:
  - text cards: about 40%
  - drawn proof stand-ins (dial, pie, card, report): about 35%
  - figures, brain or icons: about 25%
- Footnotes: 12 in 60 s (one per 5 s).
- Red words: 1 to 2 per card. No red on transition cards (7, 23 first half, 24).

---

## 8. Limits of this analysis

- Picture types were judged by eye from 1 fps sheets at 2 s steps. EQUn was sampled on 5 of 33 sheets.
- Caption proportions (§3.2) come from a hand catalogue of the N-q captions, so treat them as ±5 to 10%.
- Bed level is an RMS proxy (the quietest frames inside 400 ms windows), not a stem measurement.
- Tempo values are rough autocorrelation estimates, and genre is inferred from spectra, not identified.
- SFX detection only covers sub-bass impacts at the detected hard cuts (scene > 0.25). Quiet whooshes under speech would not be caught.
- Auto-caption punctuation sets the sentence boundaries, so the sentence-length figures are approximate.
