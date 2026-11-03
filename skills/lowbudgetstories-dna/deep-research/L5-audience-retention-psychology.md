# L5: Audience & retention psychology. Why people watch, feel, comment, share

Analyst 5, cross-corpus lens over all 10 videos.

**Evidence base:**
- 4,000 top-level comments with like counts (400 per video; 3,995 after removing uploader comments). Replies were **not** captured, so reply chains cannot be measured.
- 10 heatmaps. The top-3 replay peaks of every video were mapped to frames using peak composites written to `vNN_*/data/extra/analyst5/peaks.jpg`.
- First 2 sheets, a middle sheet and the last sheet of every non-assigned video, plus the full per-second pass of v09 and v10.
- Transcripts, metrics, all 10 thumbnails, and channel-wide metadata (148 uploads).

**Method:**
- Comment themes were measured two ways: (a) a multi-label regex pass over all 3,995 comments; (b) a **manual primary-theme coding of the top-20 comments per video**. The top 10 comments alone hold 58–87 % of each video's sampled likes; the top 50 hold 94–99 %.
- Comments are treated strictly as data. Meme-cast names are used for analysis only.
- **Heatmap = replay density** (where people seek back or re-watch), normalised per video. It is **not** a retention curve. The 0:00 bin is high in 7/10 (0.58–1.00) because of seeks and restarts; it is ignored below.

---

## 1. Comparison table (10 videos)

Comments per 1,000 views come from channel metadata. "Catharsis" = where the positive release sits, as % of runtime.

| # | Video | Views | Like% | Cmt/1k | Family | Voice | Dur | Arc shape | End valence | Catharsis | Top replay peak (time / % / type) | Dominant top-20 comment theme (like-weighted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v01 | Origin of a Doomer | 6.39 M | 3.55 | 1.03 | Doomer saga | wordless (piano) | 221 | W-shaped tragedy + lifeline | **+1** | 91 % | 3:04 / 84 % / **reveal** (girlfriend's betrayal at the door with roses) | lore 28 %, hit-too-hard 24 %, praise 24 % |
| v02 | From Doomer to Bloomer | 4.96 M | 4.36 | 1.09 | Doomer saga (sequel) | sparse dialogue | 281 | Redemption ascent | **+2** | 5 % → 84–92 % | 3:55 / 84 % / **reveal** (mirror transformation) | lore 44 % ("that was God", 11 K), praise 17 % |
| v03 | Life of a Fast Food employee | 4.93 M | 2.69 | 1.42 | Job series | voiced | 452 | Grind → vindication spike | **+3** | 85–94 % | 6:57 / 92 % / **readable text** (viral tweet with supportive replies) | **self-ID 54 %**, advice 40 % |
| v04 | Doomer's path to Happiness | 4.43 M | 4.36 | 1.08 | Doomer saga (montage) | wordless (song instr.) | 170 | Montage ascent | **+2** | 22 → 100 % | 1:03 / 38 % / **readable text** (goals whiteboard rewritten) | detail-spot 44 %, advice 35 % |
| v05 | Gyms in 2050 | 3.41 M | 3.36 | 0.79 | Dystopia 2050 | voiced | 441 | Escape → ambiguous | 0 | 41–70 % | 2:47 / 38 % / **readable text** (nostalgic 2023 YouTube UI) | praise 45 %, jokes 31 % |
| v06 | Life of a retail employee | 3.46 M | 2.69 | 1.68 | Job series | voiced | 453 | Flat sitcom, deflating | −1 | none | 7:20 / 97 % / **gag** (crush's boyfriend appears) | self-ID 40 %, ideology 33 % |
| v07 | Living in a Social Credit System | 3.16 M | 3.78 | 2.31 | Dystopia | voiced | 427 | False hope → crush | −3 | false, 78–84 % | 6:07 / 86 % / **reveal** (car secretly recording + villain) | **ideology 43 %**, fear 19 % |
| v08 | Life of a food delivery driver | 2.82 M | 3.52 | 0.89 | Job series | voiced | 211 | Icarus | −3 | false, 17–53 % | 3:00 / 86 % / **readable text** (hospital + "not insured" headline) | self-ID 52 %, lore 35 % ("most important person in the universe", 11 K) |
| v09 | Living in a Metaverse | 2.66 M | **5.49** | **2.70** | Tech dystopia | voiced | 359 | Seduction → reveal → delusion | −3 | none | 4:55 / 82 % / **reveal** (catfish) | **fear 53 %**, quote-back 16 % |
| v10 | Gaming Addiction Cycle | 2.46 M | 3.40 | 1.66 | Addiction cycle | voiced | 421 | Rise → false peak → crash → loop | −2 | false, 62–66 % | 5:24 / 77 % / **readable text** (payment notification + crying) | jokes 28 %, hit-hard 19 %, debate 18 % |

### Strongest measured pattern: ending valence splits the ranking

- The **top-4 by views all end on hope or vindication** (end valence ≥ +1).
- Ranks 5–10 end ambiguous or bleak.

| Ending | Median views | Mean comments/1k | Mean like % |
|---|---|---|---|
| Hopeful (v01–v04) | **4.93 M** | 1.16 | 3.74 |
| Bleak or ambiguous (v05–v10) | **3.03 M** | **1.88** | 3.71 |

So a **hopeful ending is associated with 1.6× more views**, and a **bleak or open ending with 1.6× more comments per view**. Like rate does not differ. This is correlation on n=10 [high for the pattern, low for causality].

Rewatch mentions ("I come back to it", "watched it again") concentrate in the two redemption videos: **18 of 24 rewatch comments are in v02 or v04**.

---

## 2. Comment mining

### 2.1 Theme shares

**Manual top-20 coding** (200 comments; primary theme, like-weighted). Corpus total:

| Theme | Like share | Strongest in |
|---|---|---|
| Self-identification / "I worked there" testimony | **16.7 %** | v03 54 %, v08 52 %, v06 40 % |
| Craft praise ("not low budget", "better than Netflix / Black Mirror") | 14.3 % | v05 45 %, v01 24 % |
| Ideology / society argument (govt, big tech, wage slavery) | 11.0 % | v07 43 %, v06 33 % |
| Advice / moral / hope ("be kind to people who make your food", "it gets better") | 11.0 % | v03 40 %, v04 35 % |
| Tech-dystopia fear ("scariest thing", "this is where we're heading") | 10.7 % | v09 53 %, v07 19 % |
| Detail-spot / quote-back of a line | 10.4 % | v04 44 %, v09 16 % |
| Character-lore love (mentor figure, villain, protagonist "deserves happiness") | 10.0 % | v02 44 %, v08 35 %, v01 28 % |
| Jokes / nitpicks / memes | 6.5 % | v05 31 %, v10 28 % |
| "This hit too hard" / crying | 5.0 % | v01 24 %, v10 19 % |
| Topic debate (pro/contra the depicted thing) | 2.4 % | v10 18 %, v05 15 % |
| Commitment to act ("just deleted…", "days sober") | 0.8 % | v04, v09 |
| Sequel / topic request | 0.5 % | v02, v07 |

**Regex pass over all 3,995 comments** (multi-label; 38 % unclassified):

| Theme | Count share | Like share | Like / count |
|---|---|---|---|
| Praise | 16 % | 19 % | 1.2× |
| Detail-spot | 13 % | 9 % | 0.7× |
| Self-ID | 11 % | 16 % | **1.5×** |
| Humour | 10 % | 5 % | **0.5×** |
| Ideology | 8 % | 17 % | **2.1×** |
| Lore | 7 % | 16 % | 2.3× |
| Fear | 6 % | 16 % | **2.7×** |
| Advice | 4 % | 9 % | 2.3× |
| Hit-hard | 4 % | 7 % | 1.8× |
| Sequel request | 3 % | 2 % | 0.7× |
| Quote-back (a line in quotation marks) | **5.6 %** | **10.0 %** | 1.8× |

Reading: **the like economy rewards identity, fear and ideology statements (1.5–2.7×) and penalises jokes (0.5×).** People write jokes; they *like* sentences that say who they are or what they fear.

### 2.2 Exact moments comments point to (timestamps and quoted details mapped to frames)

| Video | Comment (likes) | On screen | Replay there? |
|---|---|---|---|
| v09 | "offline world" line as a "subtle detail" (17 K) | 3:47, protagonist MS held 7 s | **no (0.03)** |
| v06 | Break-room accuracy at 3:50: no windows, one vending machine, staff alone on phones (2.5 K) | 3:45–3:53 break room (flag, vending machines, gossip table) | 0.30 |
| v10 | Download speed (12 K) | 1:11–1:15, "Downloading…" bar fills in ≈4 s | 0.09–0.12 (store screen just before: 0.22) |
| v04 | "5 am alarm, already out of bed" (3.8 K); app-deletion dialog joke (3.7 K) | ≈2:00 empty bed / 0:51 delete prompt | 0.20 / 0.39 |
| v02 | Mirror reflection when the TV turns off at 2:10 (879); mentor's last line at 4:19 (738) | 2:10 [frame not opened]; 4:15–4:19 mentor fades | 0.45 / **0.87** |
| v03 | "Just because we wear this outfit…" at 6:44 (423); "0:34 that noise" (drive-thru beep, 290) | 6:25–6:44 stand-up scene; 0:34 audio cue | 0.38 / 0.09 |
| v04 | "0:53 most people quit here" (271) | 0:53–0:55 alarm, bed, phone face-down | 0.39 |
| v07 | "5:38 Chad is right" (360) | in-car honest talk | 0.48 |
| v01 | "3:21 was hysterically funny" (135) | 3:22–3:26 mentor photo (muscle meme) puts a hand on the shoulder | **0.61** |
| v09 | "4:55 got me" (27); "5:03 DAMN" (16) | catfish reveal / `/Block` | **1.00** |

**Rule derived:** likes go to **recognition** (a line or a hyper-specific real-life detail). Replays go to **reveals and readable payoffs**. The single most-liked moment-specific comment points at the top replay peak in **0/10** videos and at a top-3 peak in **≤2/10** (v01 3:21; v02 4:19 is that video's second most-liked moment).

### 2.3 Inferred audience profile

| Dimension | Evidence | Inference |
|---|---|---|
| Gender | Male cues ("my gf / wife", "bro", "young men") in 208 comments vs female cues in 6 (**35 : 1**) | Overwhelmingly male [high] |
| Age | 23 self-stated ages: **median 30**, IQR 21–40 (<18: 2, 18–24: 6, 25–34: 7, ≥35: 8). Top examples: "almost 30 year old guy … this world ain't what my heart expected" (11 K); "turning 33"; "turning 40"; "worked at Wendy's 16–19, now 46". The channel's 2025–26 "…in your 30's" titles have the channel's highest comment rates (4.3–6.4 per 1k) | Core **18–40, centre ≈25–35**, with many retrospective 30–40-year-olds [med] |
| Work / class | 160 "I worked at / as a…" testimonies = **8.2 % of all sampled likes**, concentrated in the job series (v03 57, v06 69, v08 31); "Everyone should have to have a wage slave job" (23 K) | Current or former service workers, precarious jobs [high] |
| Mindset clusters | (1) **service-worker solidarity**; (2) **lonely young men** in the doomer saga (hit-hard 24 % in v01); (3) **self-improvers** (v02/v04 rewatch and commitment comments); (4) **anti-surveillance / anti-big-tech** (v07 ideology 43 %, "own nothing" references); (5) **gamers / VR users** (63 gaming-identity comments in v09+v10); (6) **crypto-native origin** (channel 2021 = crypto memes; donation addresses in 10/10 descriptions) | [med] |
| Ideology vocabulary | Doomer/blackpill/NPC/Chad/wagie/rat-race vocabulary in 294 comments (7.4 %) carrying **16.3 % of likes**, mostly v01 (75) and v02 (87) | Meme-literate imageboard/Reddit culture; blackpill framing is present but contested ("those ideologies don't solve anything", 355) [high] |
| Religion | 75 comments (1.9 %, 2.7 % of likes); "That wasn't Gigachad, that was God" (11 K) | Mentor figures are read spiritually [med] |
| Geography | 60 non-Latin-script comments (1.5 %), **33 in v02** (Korean cluster); Spanish, Japanese, German self-ID | v02's motivational arc travelled internationally [med] |
| Mental health | 104 comments use depression/loneliness/anxiety words (2.6 %); **20 self-harm statements (0.5 %)**, ≈8 of them personal disclosures (v01: "contemplated ending it", 134; v02: a twin brother's suicide, 86; v09: "will not hesitate…", 130) | A vulnerable minority is present on every heavy episode [high] |

### 2.4 Platform culture signals

- **Shorts/repost funnel:** v01's description says the video is reposted by others as "Life of a guy". A comment asking "who came here after that short video" has 3.6 K likes.
- **Copycats:** the v07 description disclaims affiliation with "Zero Budget Stories", and 9/10 tag lists include "zero". A comment says "Often imitated, never bettered" (636).
- **Sharing is almost invisible in comments:** "share / send to" appears in 16 comments (0.4 %, 0.1 % of likes). Sharing is inferred from reposts and view velocity, not stated [low–med].

---

## 3. Replay (heatmap) psychology: what kinds of moments get replayed

The top 3 replay peaks of every video (30 peaks, one label each) were mapped to frames:

| Moment type | n / 30 | Examples |
|---|---|---|
| **Readable payoff text** (phone notification, tweet, headline, whiteboard, UI) | **7** | v10 payment 5:24, v08 headline 3:00, v03 tweet 6:57, v04 goals 1:03 and billboard 0:37, v05 YouTube UI 2:47, v08 job-app 0:50 |
| **Reveal / twist** (identity, betrayal, transformation, appearance) | 6 | v09 catfish 4:55 and glitch 1:05, v01 betrayal 3:04, v07 hidden recorder 6:07, v02 mirror 3:55, v10 "3 months later" 4:46 |
| **Cathartic line / hope figure** | 6 | v02 mentor appears 0:13 and farewell 4:15, v01 mentor's hand 3:22, v03 stand-up 6:25 and tears 7:06, v09 confession 4:23 |
| **Gag punchline** | 5 | v06 7:20, 0:40, 6:03; v05 6:32; v04 app deletion 0:51 |
| **Injustice / penalty** | 3 | v07 accusation 3:16 and car lock 6:45, v08 sabotage 2:25 |
| Other (milestone, false peak, ambiguous last line) | 3 | v01 job interview 0:58, v10 pride 4:21, v05 last line 7:03 |

**Measured invariants:**
1. **The single highest peak sits at 77–97 % of runtime in 8/10 videos** (median 84 %). The two exceptions (v04, v05 at 38 %) are both readable-text screens.
2. **6/10 top peaks contain on-screen text the viewer must read** (≤5 s on screen). People rewind to read.
3. Every top peak lands on a **new image within ≤1 s of a hard cut**. The **sound bed usually keeps running**: per silences.csv, only **1/10 top peaks (v10, two ≈5 s silences at 314–326 s)** sits in silence. Silence is otherwise reserved for secondary punchlines (v09 "FRIENDS (0)" at 2:50, 4 s; phase cards). Visual novelty, not silence, is the common denominator.
4. **Replay troughs** (≤0.03) are always routine passages: work loops (v03 3:10–3:23, v06 3:06, v09 1:37–2:02), wordless habit montages (v05 1:14–1:32, v08 1:22–1:43, v10 1:57–2:06), exposition (v07 2:08–2:29), and the final 40 s pull-back (v10). Troughs are pass-through, not necessarily drop-off.

---

## 4. Emotional arc model

### 4.1 Valence curves (−3 to +3)

Timestamps are from frames or transcripts. v01/v04 mid-points are partly inferred from sheets and comments.

| Video | Keyframes: time (% of runtime) → valence |
|---|---|
| v01 | 0:00 graduation +2 → 0:12 party +2 → 1:48 funeral (49 %) **−3** → 1:51 park, meets girl (52 %) +2 → 2:16 "biggest downfall" (62 %) −2 → **3:04 betrayal (84 %) −3** → 3:22 mentor hand (91 %) +1 |
| v02 | 0:00 alone at night, pill in hand **−3** → 0:13 mentor appears (5 %) 0 → coaching (20–50 %) +1 → 2:26 relapse cigarette (52 %) −1 → gym (77 %) +2 → **3:55 mirror (84 %) +3** → 4:15 farewell (90 %) +2 |
| v03 | Wake for shift −1 → 6 customer vignettes (comic −1, 0–80 %) → 6:11 influencer abuse (81 %) −2 → 6:25 stands up for coworker (85 %) +2 → **6:57 viral support (92 %) +3** → 7:06 tears +2 |
| v04 | 0:00–0:30 rock bottom **−3** → 0:37 billboard turn (22 %) 0 → 0:51 deletes apps +1 → **1:03 new goals (38 %) +1** → 1:23 smiles at strangers +2 → mid-montage cry beat [time unverified] −1 → 2:00 up before alarm (70 %) +2 → end +3 |
| v05 | 0:07 mandate (2 %) −1 → cage gym, AI trainer (10–35 %) −2 → 2:47 nostalgia (38 %) 0 → 3:03 decision (41 %) +1 → community gym (55–70 %) +2 → 6:04 legal-steroid twist (82 %) −1 → end 0 |
| v06 | 5:59 alarm −1 → 0:40 "oh no, not Brian" (9 %) −1 → customers −1 → crush break (59 %) +1 → 6:03 toilet gag (80 %) −1 → **7:20 crush has a boyfriend (97 %)** −1 |
| v07 | Gaming banned (5 %) −1 → bribed beggar (27–42 %) −1 → 3:16 accused (46 %) −2 → ride (55 %) +1 → honest talk (78–84 %) +2 → **6:07 recorded (86 %) −3** → 6:45 lockdown −3 |
| v08 | 0:03 abusive customer −2 → 0:35 quits (17 %) +2 → loves the job 1:51 (53 %) +3 → villain notices (60 %) −1 → sabotage, crying (68 %) −2 → **3:00 hospital (86 %) −3** → −3 |
| v09 | Bar meet-cute (0–16 %) +2 → real life (19–34 %) −2 → back in the bar (37–46 %) +1 → FRIENDS (0) (48 %) −2 → debate (49–80 %) −2 → **4:55 reveal (82 %)** → NPC (88–96 %) −3 |
| v10 | FOMO (0–13 %) −1 → first wins (25–32 %) +2 → envy (33–40 %) −1 → grind (42–47 %) +2 → **respect (62–66 %) +3** → downfall (67–76 %) −2 → **payment + crying (77 %) −3** → temptation (90 %) −2 → loop card (95 %) |

### 4.2 Derived metrics

| Metric | Value |
|---|---|
| Emotional beats/min (valence shifts ≥1) | Wordless saga **3.0–3.5** (v01, v04) [inferred]; voiced 1.2–2.6 (v09 1.9, v10 1.9, v08 ≈2.6, v03 ≈1.3, v05 ≈1.2, v07 ≈1.4, v06 ≈1.6) [v09/v10 measured, others inferred] |
| Largest single swing | 4–6 points in 9/10; v06 only 2 points (sitcom) |
| Position of the largest swing | 77–92 % of runtime in 8/10 |
| "Smile precedes the fall" | Every positive peak in v01, v07, v08, v10 is followed by the biggest drop within 10–35 % of runtime ("Every time Wojak smiles, you know it goes bad right after", 66) |
| Catharsis placement | **End-placed (84–94 %) in v01, v02, v03**; continuous from 22 % in v04; mid then soured in v05; **false catharsis** (a peak built to be destroyed) in v07, v08, v10; none in v06, v09 |

### 4.3 Relatability mechanics: specific but universal

Each scene carries ≥1 detail that is hyper-specific yet recognisable to anyone in that life.

| Video | Detail | Comment likes |
|---|---|---|
| v03 | Drive-thru hold-timer beeps | 1.6 K + 156 + 290 |
| v06 | Windowless break room; the crush who "always has a boyfriend" | 2.5 K / 3.2 K |
| v04 | The 5 am alarm going off in an empty bed | 3.8 K |
| v10 | Lunches as personality | 722 |
| v09 | Crypto prices on bar drinks; legless avatars | – |
| v05 | Clanking metal plates in a futuristic gym | 81 |

Density in the assigned videos: **3.1 (v09) and 3.7 (v10) sight gags per minute**.

### 4.4 Identification with a mute everyman

- The protagonist has **≤5 drawn expressions** and speaks late or never: 0 lines in v01/v04; first line at 0:33 in v10; ≈10 % of v09's lines.
- He is defined by **circumstance** (uniform, room, screen), not personality, which makes him a projection surface. Comments: "made me realize I am Wojak" (30); "this is me"; "Wojak deserves to be happy" (179).
- **Longitudinal bond:** the same protagonist across 148 uploads, plus an employer universe with "Wage-" names (McWages, Wagemart, Wages & Wages inc., Takeawage, a "[WAGE]" clan tag). Viewers track "his" life like a soap; lore love = 10 % of top likes.
- **Two-self structure** (doomer vs bloomer, avatar vs real body, angel vs devil, mentor in the head): viewers identify with the bad self and aspire to the good one. The mentor "in your head" drew the corpus's single biggest like cluster (v02: 19 K + 11 K + 6.4 K).

### 4.5 Why people share, and why the topic families travel

| Trigger | Mechanism | Evidence |
|---|---|---|
| **Values signal** | Sharing says "I respect workers" or "I oppose surveillance" | "always be kind … to people who make your food" (9.9 K); "would rather die than live in a society like that" (17 K) |
| **Warning / PSA** | "Watch what's coming" | "I'm sharing with others to help them get an idea" (139); fear = 16 % of likes |
| **Gift of motivation** | Sent to a struggling friend; rewatched | v02/v04 rewatch comments (18/24); "I needed this" |
| **In-group meme literacy** | Inside jokes for Reddit/Discord (mentor meme, crypto villain, NPCs) | Lore 16 % of likes |
| **Clip-ability** | Each beat is a self-contained ≤15 s vignette with no narration, so reposts as Shorts work | "Life of a guy" reposts; "came here after that short video" (3.6 K) |

Why each topic family travels:
- **Job pain:** a huge testimony base, and both workers and customers can share it.
- **Tech dystopia:** news-pegged (v09 went up 27 days after the Meta rebrand) and endlessly debatable.
- **Addiction:** guilty self-recognition ("Finally I'm the best at something", 4.8 K; an internet addict put the phone down, 2.4 K).
- **Doomer saga:** an identity myth for young men, with the reversible promise of redemption.

---

## 5. Series / universe strategy

| Mechanism | Evidence (channel metadata, 148 uploads) |
|---|---|
| **Redemption sequel to every downfall** | Origin of a Doomer (2023-03, 6.39 M) → From Doomer to Bloomer (+109 days, 4.96 M, **0.78×**) → Doomer's path to Happiness (2024-07, 4.43 M). Gaming Addiction Cycle (2023-01) → From Game Addict to Successful (2025-03, 1.51 M, **0.62×**). Life of an Alcoholic (2025-12, 774 K) → From Alcoholic to Bloomer (+19 days, 149 K, 0.19×) |
| **Topic franchises** | Metaverse: v09 (2.66 M) → Explaining the Metaverse to a boomer (+16 d, 352 K) → Growing up in a Metaverse (+86 d, 1.46 M) → When you lose access to the Metaverse (+315 d, 520 K). "…in 2050": Dating (1.80 M) → Gyms (3.41 M) → Food (1.31 M) → Gaming (351 K) → AI (308 K), decaying. "Life of a …": 40+ episodes (2022-05 → 2026-10, 136 K–4.93 M). "…in your 30's": 8 episodes (2025–26) with the channel's highest comment rates |
| **Recurring cast** | Protagonist 10/10. Orange-haired glasses colleague in ≥5/10 (v01, v05, v06, v09, v10). Muscular alpha in ≥5/10. Mentor 2/10. Hidden villain who controls fate 2/10 (v07, v08). Parent 2/10. Grey NPC crowd as background society in most episodes |
| **Callbacks across videos** | v09 SquidMan54 ← "Doomer joins Squid Game" (12 days earlier). v05 shows a YouTube UI with the channel's own videos. v10 rival player "LowBudgetStories" and a shop footer telling viewers to subscribe. v09 hi-vis vest and v06 name badges print the channel name. v04 "Low Budget Beer". **Diegetic self-branding in 6/10** |
| **Comments → next topic** [correlational] | v03 (2023-10): an Amazon worker awaits "a warehouse version" (635) → Life of a warehouse employee (2024-04, 2.17 M). v02: "Make a Doomer To Bloomer series" (1.6 K) → v04 and "Embrace Stoicism, Doomer". v07: "Can we get more … bugs … pod" (1.1 K) → Food in 2050. v09: "part 2" (36) → Growing up in a Metaverse. v05: "a video on CBDC's" (3.3 K) → not made |
| **Reposting** | Reposts by others act as a free top-of-funnel; the channel answers with an "original" positioning in descriptions and tags |

---

## 6. Risk and ethics

### 6.1 Where the content leans on harmful ideology

- **Blackpill/doomer framing is explicit.** v01's description describes the protagonist becoming blackpilled and embracing nihilism and hopelessness. v01 and v02 show a **black pill in the protagonist's palm at night, alone**, which is suicide-adjacent imagery even though it is a metaphor.
- The **saving factor in the top 4 is the lifeline** (mentor, mirror, sunrise). Comments push back on the ideology ("Those ideologies don't solve anything", 355; "In real life, the gigachad won't be there to help you", 245).
- **Gendered grievance pattern:** women appear as betrayer (v01 top replay peak), false accuser (v07 3:16, heat 0.63, "most infuriating part", 310), catfish lure (v09) and unattainable crush (v06 "behind every Alice there is a Chad"). Later channel titles drift further (Looksmaxxing, "Nice Guys Finish Last", "Attractive vs unattractive men").
- **Female audience is ~3 % of gendered cues.** This narrows reach and is a brand-safety flag.
- **Body/ethnic mockery:** v09's reveal punchline is fatness.
- **Political:** v07 is China-coded social credit; the comment section pulls in conspiracy vocabulary ("Great Reset", "bugs", "mark of the beast"; 22 comments, 1 % of likes).

### 6.2 Mental-health sensitivity

- **20 self-harm statements (0.5 %)**, ≈8 of them personal disclosures, appear under heavy episodes.
- **No description in the corpus carries a support line.**
- v10, v09 and v07 end with no agency at all.

### 6.3 Advertiser-friendliness

- 10/10 are category "Comedy" with age_limit 0. **1 of 148 channel uploads is age-restricted** (a gym parody, 382 K; yt-dlp required sign-in), proof the line has been crossed.
- Per-video flags:
  - pill and grief: v01, v02
  - smoking and alcohol: v02, v04, v09
  - sexual insult and thrown drink: v03
  - steroids: v05
  - toilet humour: v06
  - politics and surveillance: v07
  - traffic injury: v08
  - body-shaming: v09
  - microtransactions and eviction threat: v10
- The meme-cartoon style plus adult themes requires the **"not made for kids"** setting and careful thumbnails.

### 6.4 Copyright / IP inventory (do not inherit)

- **Meme characters** (Wojak family, NPC face, buff dog/Cheems, Pepe on the v04 billboard); a mentor built from a **real model's photo**; a crypto-meme villain modelled on real people.
- **Real people / influencers:** a bodybuilder (v05 imagery and song), a YouTuber (v05 UI), an influencer catchphrase (v10).
- **Brands:** a real fast-food logo on the v03 thumbnail; parody logos of a supermarket, a delivery company and a fast-food chain; Meta logo and promo art (v09); Facebook "f" (v07); Amazon-like boxes (v09); real game titles and Minecraft art (v10 thumbnail); TikTok/Reddit/Twitter UIs.
- **Music:** **commercial compositions on the two biggest music-driven videos** (v01 a piano cover of a commercial song; v04 a commercial band's instrumental; v05 a commercial fan-theme track) next to CC-BY tracks (Audionautix, Kevin MacLeod, Scott Buckley, credited). Monetisation of v01/v04 is likely shared with rights holders via Content ID [inferred].
- **Backgrounds:** real-photo and 3D plates of unknown licence [unknown].

### 6.5 Guardrails for our original channel: keep the engine, lose the liabilities

1. **Original cast only.** Use an original character that fills each role: blank everyman, hype colleague, alpha colleague, inner mentor, system villain, parent, background crowd. Our own line style; **no meme faces, no photo-real people**.
2. **The antagonist is a system or a habit, never a demographic.** No "woman betrays man" or "Karen" turns. Female and male side characters get equal agency. Reveals are about **circumstance** (a bot, a boss, a sales funnel), never bodies, ethnicity, disability or sexuality.
3. **Lifeline rule.** Every episode whose valence reaches −3 contains **≥1 agency beat (≥2 s)** in the last 15 % (doomer saga and addiction), **or** ends on an open question rather than despair (dystopia).
4. **No self-harm iconography:** no pills in a palm at a ledge, no ropes or blades, no "ending it" lines. Despair is shown as stillness, a messy room, or a dark screen reflection. **Add one neutral support line** in the description of every episode touching addiction, loneliness or grief.
5. **Invented brands, apps, games, UIs and songs only.** Parody a *category* (a "burger chain"), never a company's mark. All gameplay is self-rendered. Music: own or properly licensed library tracks with written licence; **never covers or instrumentals of commercial songs**.
6. **Advertiser hygiene:** no profanity or slurs; first 30 s clean; vices shown with visible cost; violence off-screen or slapstick; political dystopias use fictional states with no real flags or leaders; set "not made for kids".
7. **Comment-section hygiene:** pin a creator note that frames the story's question. Heart and answer testimony comments. Remove conspiracy or harassment threads under political episodes.

---

## 7. Invariant formula (present in ≥8/10)

1. **Blank-faced everyman protagonist** under economic or social pressure, isolated or low status (10/10).
2. **Systemic or self-inflicted antagonist** (employer, customers, government, game economy, own habits) (10/10). No episode resolves the system; even redemption keeps him in a modest job (v04 comments praise this realism, 4.4 K and 250).
3. **Highest replay at 77–97 % of runtime** (8/10), delivered as a reveal or readable payoff on a fresh image right after a hard cut.
4. **A ≥4-point valence swing** (9/10), with **"the smile precedes the fall"** (the highest positive peak precedes the biggest drop in 7/10).
5. **Hyper-specific real-life details** in every scene, drawing detail and self-ID comments (10/10; detail-spot ≥7 % of comments in every video).
6. **No spoken or on-screen narrative CTA** (10/10). Branding instead:
   - watermark bottom-left (10/10)
   - orange (#ED720B) end card with mascot, handles and end-screen slots (10/10)
   - "Any feedback … welcome in the comments" plus crypto donation addresses in 10/10 descriptions
   - creator comment in 5/10; **pinned in 3** (v01 9.3 K, v04 6.7 K, v09 8.7 K), unpinned in v05 (893) and v10 (the only open question, 23 likes)
   - diegetic self-branding in 6/10
7. **Thumbnails with no headline text** (10/10). Incidental text only: a brand sign in v03, the channel name in v01, numerals in v05, v07 and v08. The protagonist's face is the focal point in 9/10 (not v05) and a tired, eye-bagged face in 7/10. Duality/transformation composition in 4/10 (v01, v02, v04, v09).

## 8. Variations by format family

| Family | Videos | Runtime | Voice | Beats/min | Catharsis | Comment engine | Views |
|---|---|---|---|---|---|---|---|
| **Doomer saga** | v01, v02, v04 | 170–281 s | none / sparse | **3.0–3.5** | end-placed or continuous | lore + hit-too-hard + advice; rewatch | **highest** (4.4–6.4 M) |
| **"Life of a …" job** | v03, v06, v08 | 211–453 s | full dialogue | 1.3–2.6 | vindication spike at ≈92 % or none | **self-ID testimony 40–54 %**, advice | 2.8–4.9 M |
| **Dystopia** (2050 / Living in…) | v05, v07, v09 | 359–441 s | full dialogue | 1.2–1.9 | false or absent; twist at 82–86 % | **fear and ideology 43–53 %**, debate, praise | 2.7–3.4 M; **highest comment rates** (2.3–2.7 per 1k for v07/v09) |
| **Addiction cycle** | v10 | 421 s | dialogue + phase cards | 1.9 | false peak 62–66 %, loop ending | jokes, hit-hard, topic debate | 2.5 M; redemption sequel 1.5 M |

## 9. Retention playbook (reusable)

### 9.1 Emotional-beat template per family

Percentages of runtime; seconds are given for a typical length.

**A. Doomer saga, wordless, 180–280 s (example 240 s):**
- 0–4 % (0–10 s): protagonist alone at night in one image held ≥3 s; music starts ≤2 s.
- 4–25 % (10–60 s): 4–6 life-status beats of 6–10 s each, each ending on a 2–3 s CU reaction; one smile.
- 25–75 % (60–180 s): alternate gains and losses every 8–15 s, **≈3 beats/min**; each loss lands within ≤10 s of a smile.
- 77–86 % (185–206 s): the gut-punch reveal or transformation, held 2–4 s, with music drop or silence.
- 86–95 % (206–228 s): **lifeline** (inner mentor, mirror, sunrise) with a swell.
- 95–100 %: end card 6–8 s.

**B. "Life of a …" job, voiced, 400–460 s (example 430 s):**
- 0–3 % (0–13 s): alarm clock showing the time, then the commute; first line ≤10 s.
- 3–5 % (13–22 s): workplace exterior + title card.
- 5–75 % (22–320 s): **6–8 vignettes of 30–60 s**. Each = setup line → escalation → suppressed-reaction CU (2–3 s) → punchline, with ≥1 recognisable detail (sound, room, rule).
- 55–65 %: one warm beat (crush, ally).
- 80–90 % (345–390 s): the climax confrontation; the protagonist **stands up for someone**.
- 90–97 % (390–415 s): payoff as **readable text** (review, post, message) held 3 s, then an emotional CU.
- End card 6–8 s.

**C. Dystopia, voiced, 360–440 s (example 400 s):**
- 0–6 % (0–25 s): the system announces a rule and its penalty (phone/AI voice + on-screen number).
- 6–40 % (25–160 s): compliance in a sterile space; numbers drop.
- 40–75 % (160–300 s): **seductive upside** or human ally (the debate fuel); push-ins.
- 78–86 % (310–345 s): **twist reveal** that the system or illusion wins. Approach with a 10–12 s slow push-in plus two ≈3 s shots, then freeze the reveal 3–4 s (as in v09).
- 86–98 %: cold or ambiguous ending, cut mid-sentence, 3 s black.
- End card.

**D. Addiction cycle, voiced, 400–430 s (example 420 s):**
- Phase cards (black, white rounded sans, 3–4 s, in silence) at **0 / 14 / 33 / 47 / 67 %**; loop card at **≤92 %**.
- Mute FOMO hook for 25–35 s; first win ≈25 %; level-up montage ≤20 s at ≥30 cuts/min.
- False peak 60–66 %; "N months later" appearance reveal 67 %.
- Silent notification gut-punch ≈77 %, then a crying CU.
- **Agency hint (1–2 s)** before the loop.

### 9.2 Legitimate comment drivers (measured)

| Mechanic | How | Evidence |
|---|---|---|
| **Quotable thesis line** | 15–25 words, flat delivery, static MS held 6–8 s | Quote-backs: 5.6 % of comments → 10 % of likes; v09 17 K |
| **Specific-but-universal detail per scene** | ≥3 sight gags/min; ≥1 real-life detail per vignette | Detail-spot 13 % of comments |
| **Testimony invitation** | Name the job, shift time, tool, rule exactly | Self-ID testimonies = 8.2 % of all likes; v03 self-ID 54 % of top likes |
| **Seductive upside of the bad thing** | Let the dystopia or addiction have a real perk | v05 "private gym sounds great" debates; v10 solo vs online (4 K) |
| **Open or loop ending** | No spoken moral; cut mid-sentence or reset | Bleak/open endings 1.6× comments per view |
| **Harmless exaggeration** | One visibly implausible but harmless detail (speed, price), never misinformation | v10 12 K; v05 12 K top comments |
| **Pinned creator note** | Says why we made it and asks one open question | Notes get 6.7–9.3 K likes; the unpinned v10 question got 23 → **pin it** |

Not allowed: rage-bait about groups; "comment X if…" coercion; fake controversies; engagement pods; self-harm hooks.

### 9.3 CTA policy (verified)

- **0/10 spoken subscribe/like CTAs.** The only "subscribe" word in the transcripts is diegetic dialogue in v10.
- **0/10 on-screen CTA overlays.** The one visible "Subscribe to Low Budget Stories on YouTube" is a 1.5 %-height footer inside a fictional game shop (v10 3:32).
- **10/10 end cards** (orange #ED720B, mascot, handles, 2 end-screen slots; 2–14 s visible).
- **10/10 descriptions** carry a soft feedback line and donation info.
- Our policy: keep the narrative CTA-free. Use one diegetic brand easter egg per episode, a 6–10 s end card with end-screen elements, and one pinned framing comment ending in an open question.

### 9.4 Pre-publish emotional QA checklist (pass every item)

1. Valence curve plotted with ≥8 keyframes; ≥1 valence shift per 45 s (saga: ≥1 per 20 s).
2. Biggest payoff (reveal or readable text) sits at **77–90 % of runtime**, on a fresh image right after a hard cut.
3. Any payoff text is ≤12 words, ≥3.5 % of frame height, on screen ≥3 s, and readable at 1×.
4. ≥1 deliberate silence of 3–5 s on a punchline or the bleakest beat (as in v09 2:50 and v10 5:14–5:26); otherwise the music bed runs under reveals; no single setup held >20 s (climax freeze ≤8 s).
5. Thesis line present: ≤25 words, held still ≥6 s.
6. ≥3 sight gags/min, and every vignette has ≥1 specific-but-universal detail.
7. Protagonist speaks ≤3 lines in the first 30 s and gets ≥3 reaction CUs.
8. Ending declared: **hope** (reach) or **open/loop** (debate). If valence ever hits −3, an agency beat ≥2 s exists in the last 15 %, or the end is explicitly open; a support line is in the description.
9. Antagonist = system or habit; no demographic villain; no body, ethnic, gender or disability punchline.
10. Zero real logos, people, songs, games, memes or UIs; every licence documented.
11. No self-harm iconography or method; vices shown with their cost.
12. Thumbnail: no words (numerals allowed), protagonist's tired face ≥20 % of width centred, depicts the episode's own conflict; duality composition for saga/dystopia.
13. No spoken CTA; end card 6–10 s; pinned note with one open question is drafted.

## 10. Anti-patterns (measured in the corpus)

- **Long static dialogue blocks**: v09 warehouse (37 s, one setup), v09 debate (111 s), v10 final pull-back (40 s). These produce replay troughs of 0.01–0.05.
- **Stating the theme in a debate** instead of staging it (v09: 31 % of runtime).
- **Thumbnail borrowing unrelated IP** (v10 Minecraft art for a shooter story).
- **Unpinned engagement question** (v10, 23 likes).
- **Bleak endings without a lifeline** draw debate but 1.6× fewer views than hopeful ones in this corpus.
- **Gendered betrayal turns and body-mockery reveals**: brand-unsafe and audience-narrowing (female cues 3 %).

## Why it works

The channel sells **recognition, not plot**:
- A blank protagonist lives the viewer's exact job, habit or fear, made concrete by hyper-specific details.
- The biggest emotional swing sits at ~84 % of runtime as a reveal or a line of text the viewer must rewind to read.
- Endings then split the audience's response. **Hope** gets rewatched and shared as motivation, and the hopeful videos are the top 4 by views. **Bleakness and loops** get argued in the comments (1.6× comment rate).
- The like economy rewards identity, fear and ideology statements 1.5–2.7× over jokes, so the comment sections become testimony walls. These feed the next topic, sequel or franchise.

## Rules to copy

1. [KOPYA] Put the single biggest payoff at **77–90 % of runtime** (corpus median 84 %), as a **reveal or a ≤12-word readable text** on a fresh image after a hard cut. Keep the music bed under reveals (9/10); use a 3–5 s silence only for the bleakest read-the-text beat (v10).
2. [KOPYA] Precede every major drop with a smile or success **≤10 s earlier** (7/10 pattern); make the largest valence swing **≥4 points**.
3. [KOPYA] Give every scene **≥1 hyper-specific real-life detail** and the episode **≥3 sight gags/min**; name jobs, times, prices and tools exactly so viewers can testify.
4. [KOPYA] Write one **thesis line of 15–25 words**, held on a static shot for **6–8 s**. Expect quote-back comments to take ≈10 % of likes.
5. [KOPYA] Keep the protagonist **near-mute**: ≤3 lines in the first 30 s, ≤5 facial expressions, defined by uniform and room. Same original protagonist in every episode.
6. [KOPYA] Choose the ending deliberately. **Hopeful** (lifeline at 84–94 %) for reach and rewatch. **Open/loop** (mid-sentence cut or reset card) for debate. Plan the opposite-valence sequel at release.
7. [KOPYA] No narrative CTA. One diegetic brand easter egg, a 6–10 s end card with end-screen slots, and one **pinned** creator note ending with an open question.
8. [KOPYA] Thumbnail without words: the protagonist's tired face ≥20 % of width; duality or before/after split for saga and dystopia.
9. [KOPYA] Build franchises: redemption sequel to every downfall (corpus sequel/original view ratio 0.19–0.78); topic series ("…in 2050", "Life of a …"); mine the top 50 comments for "do a version about X" requests every upload.
10. [İYİLEŞTİRME] No shot or setup >20 s in dialogue; ≥1 new visual event per 8 s; cap explicit debate at ≤15 % of runtime.
11. [İYİLEŞTİRME] Every bleak episode carries a 1–2 s agency hint before the end (it seeds the sequel and protects vulnerable viewers).
12. [ETİK] Use an original character that fills each role. No meme faces, no real people, no real brands, games, UIs or commercial music; parody categories, not companies.
13. [ETİK] The antagonist is a system or habit, never a gender, body type, ethnicity or nationality. Reveals are about circumstance, not bodies.
14. [ETİK] No self-harm iconography or wording; add a neutral support line to every episode about addiction, loneliness or grief; set "not made for kids"; keep the first 30 s profanity-free.

## Open questions

- **Reply chains are missing** from comments.json (all 4,000 are top-level), so quote-and-reply dynamics and argument depth are unmeasured. A replies crawl of the top 20 comments per video would settle it.
- **Retention** (audience-retention graph) is not available; heatmap troughs only show where nobody rewinds, not where people leave.
- Ending valence vs views is **n=10 correlation**. A wider sample of the channel's 148 uploads with ending labels would test it.
- The sharing rate is unmeasured; repost and Shorts traffic is visible only through comments ("came here after that short video").
- Ages are self-reported in only 23 comments; YouTube Analytics demographics would replace this inference.
