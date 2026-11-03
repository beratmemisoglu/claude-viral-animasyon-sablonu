# E — Üretim hattı (full-automatic video pipeline) · 2026-10-28

Kapsam: Türkçe "Ya ___ olsaydı?" animasyon videoları (8–10 dk, 2. tekil şahıs, stick-figure, kafa üstü etiket UI) için
**fikir → paket → senaryo → TTS → shot list → Remotion render → thumbnail → metadata → YouTube upload** boru hattının tasarımı
ve çalışır iskeleti. Diğer ajanların alanına (başlık kalıpları, hook/retention, senaryo motoru) girilmedi; onlara notlar en sonda.

Teslim edilen dosyalar (hepsi `~/.claude/skills/whatif-animated-dna/`):

| Yol | Ne |
|---|---|
| `scripts/pipeline.py` | stage runner (idea·package·script·tts·shots·render·thumb·meta·upload), `state.json`, log, `--from/--only/--to/--dry-run/--status`, LLM stage'lerinde exit 3 = "needs_llm" |
| `scripts/shots_schema.json` | shots.json JSON Schema (draft 2020-12; `jsonschema` 4.26 kurulu → tam doğrulama) |
| `scripts/tts_segments.py` + `scripts/whatif_voice.json` | vuruş bazlı ElevenLabs TTS, `/with-timestamps` kelime zamanları, ffprobe süre, idempotent (hash), `timeline.json`; `--list-voices` |
| `scripts/make_thumbnail.py` + `templates/thumbnail.svg` | SVG şablon (A/B/C layout) → 1280×720 PNG + 320×180 önizleme; motor: headless Edge (kanıtlı), `--base-image` ile Higgsfield polish üstüne yazı |
| `scripts/qa_render.ps1` | shot başlangıçlarından kare çekme + kontak sayfası + `lowbudgetstories-dna/scripts/rhythm_qa.py` (voiced mod) |
| `templates/remotion/` | `WhatIfFilm.tsx` (kompozisyon, props=shots+timeline, calculateMetadata), `StickFigure.tsx` (rig, 8 poz, 6 ifade, yürüme/koşma döngüsü), `HeadLabel.tsx`, `Crowd.tsx`, `Caption.tsx`, `Scene{Street,Office,Home,School,Transit,Wedding}.tsx`, `scenes.ts`, `theme.ts`, `fonts.ts`, `register.ts` (stüdyoya ekleme talimatı), `sample/shots.json` + `sample/timeline.json` (5 sn smoke) |
| `templates/prompts/{idea,package,script,shots,meta}.md` | LLM stage'lerinin prompt şablonları (`{{placeholder}}` pipeline tarafından doldurulur) |

## Özet (10 madde)

1. **Animasyon yolu = Remotion 4.0.535 + SVG stick-figure rig** (AI video değil). Deterministik, kare başına sıfır maliyet, Türkçe metin/etiket overlay'i native; 10 dk'lık video ~15–25 dk'da render edilir. AI video (Higgsfield) yalnızca thumbnail polish'inde opsiyonel.
2. **Mevcut stüdyo `C:\dev\the-other-self`** (`C:\dev\dayone-studio` YOK); `remotion@4.0.535`, React 19, `@remotion/{media,google-fonts,paths,noise,captions,elevenlabs}` kurulu. Yeni kompozisyon **tek ve slug'dan bağımsız** (`whatif-film`), film verisi `--props=<dosya>` ile verilir → Root.tsx her videoda düzenlenmez.
3. **Smoke test BAŞARILI**: 5 sn / 3 shot / 3 sahne (sokak+kalabalık, ofis, başlık kartı) `tsc` temiz, `npx remotion render --scale=0.5` → `smoke-draft.mp4` 5.000 s h264 960×540; kareler gözle kontrol edildi (Türkçe karakterler, etiketler, altyazı doğru). İki kusur bulunup düzeltildi (oturma pozu kalça ofseti; altyazı kelime boşluğu).
4. **Veri omurgası iki JSON**: `timeline.json` (TTS'ten gelen gerçek süreler + kelime zamanları) ve `shots.json` (LLM'in ürettiği shot listesi; şema zorunlu). Sıra: senaryo → **önce TTS** (süreler bilinir) → shot list (sürelere kilitli) → render. Böylece ses-görüntü senkronu tahmin değil ölçümdür.
5. **TTS vuruş bazlı**: her segment ayrı mp3 (`v01.mp3`…), `eleven_say.py` reçetesi (sessizlik kırpma + loudnorm) korunarak; `eleven_say.py` **timestamp desteklemiyor** → `tts_segments.py` `/v1/text-to-speech/{voice}/with-timestamps` kullanır, başarısızsa düz TTS + orantılı tahmin. Kelime-kelime (karaoke) altyazı `Caption.tsx` ile hazır.
6. **Türkçe ses**: model `eleven_multilingual_v2` (varsayılan, timestamps kesin) veya `eleven_v3`; `voice_id` **placeholder** — kullanıcı `python tts_segments.py --list-voices` ile seçer (anahtar yazdırılmaz).
7. **Orkestrasyon**: `pipeline.py <slug>`; her stage idempotent (çıktı varsa atlar), `state.json` + `pipeline.log`, hata → `failed` + "devam: `--from <stage>`". LLM gerektiren stage'ler (idea/package/script/shots/meta) prompt dosyası yazıp **exit 3** ile durur; Claude dosyayı üretir, runner devam eder. İsteğe bağlı `--llm "claude -p"` ile tamamen başsız.
8. **Thumbnail**: SVG şablon, 3 layout (A karakter+büyük etiket, B kalabalık+tek etiket, C yakın yüz), Fredoka 700 BÜYÜK HARF, telefon önizlemesi; cairosvg/resvg/rsvg/ImageMagick bu makinede yok ve ffmpeg'de svg decoder yok → kanıtlı yol **headless Edge** (other-self-thumbnail ile aynı). 3 layout test edildi.
9. **Upload**: mevcut `the-other-self/scripts/youtube/youtube_upload.py` (Data API v3, resumable, thumbnail set, publishAt) yeniden kullanılır; token `C:/dev/secrets/youtube_token.json` (yt_common.py `ROOT=parents[3]`). Windows'ta henüz venv/token yok → ilk kurulum gerekir; script `defaultLanguage: 'en'` sabit → 2 satırlık `tr` yaması önerilir.
10. **Tahmini maliyet/süre (10 dk video)**: ElevenLabs ~9–11k karakter (Creator planda ≈ %10 aylık kota); Remotion render ~20 dk (CPU); Higgsfield thumbnail polish opsiyonel ≈ 4 kredi; toplam makine süresi ≈ 45–60 dk + LLM adımları. Tam zincir ilk kez ≈ 1 iş günü (kurulum dahil), sonrası ≈ 2 saat.

## 1. Keşfedilen mevcut altyapı (uydurma değil, `ls`/okuma ile doğrulandı)

| Bileşen | Bulgu | Yeniden kullanım |
|---|---|---|
| Stüdyo | `C:\dev\the-other-self` (package.json: `remotion ^4.0.535`, `@remotion/cli/media/google-fonts/noise/paths`, react 19.1; node_modules'ta ayrıca `@remotion/captions`, `@remotion/elevenlabs`). `C:\dev\dayone-studio` yok. `remotion.config.ts`: jpeg kareler, overwrite. tsconfig strict + `noUnusedLocals` + `resolveJsonModule`. | Aynı stüdyoya `src/lib/whatif/` olarak eklenir (kopya değil, yeni klasör). chrome-headless-shell indirilmiş (`node_modules/.remotion/...`). |
| Karakter rigi | `src/lib/character/rig.ts` (Ay kafa: FK/IK `solve()`, `POSES`, `EXPR` 17 ifade, `heroSVG` → string), `Hero.tsx` (`dangerouslySetInnerHTML`), `Twin.tsx`. | **Mimari** alındı (FK ile tek path uzuv → kopma yok; SVG string + `<g>`; `at()` step fonksiyonu; `Stage` push-in). Karakterin kendisi alınmadı — The Other Self markası; bu kanal özgün çöp adam kullanır. |
| Sahne/metin | `stage.tsx` (Stage push-in, DipOverlay, Letterbox, LightPool, Dust), `text.tsx` (Narrator, InfoText, Verdict, DayCounter, ClockHUD), `TitleCard.tsx`, `fonts.ts` (ComicRelief). Film = `timeline.json` (scenes[{id,dur,trans}]) + `<Series>` + `SCENE_COMPONENTS`. | DipOverlay mantığı ve `--props` yaklaşımı taşındı. Letterbox KULLANILMADI (hedef niş tam kare; bkz. LBS 06 §1: letterbox 10/10 yok). |
| Ses | `inner-voice-film/scripts/eleven_say.py`: `voice.json` ({voice_id, model_id eleven_v3, styles}) → `POST /v1/text-to-speech/{id}?output_format=mp3_44100_192` → ffmpeg silenceremove+highpass+loudnorm → wav. **Timestamps yok.** `build-film-audio.py` + `*-cues.mjs` (prosedürel müzik/SFX, ducking −8 dB, Float32 mix → wav), `sfxgen.mjs` (seed'li SFX üreteci). `references/08-audio.md`: `<Audio>` from `@remotion/media`, `volume` sayı, `trimBefore`. | `tts_segments.py` aynı reçeteyi segment bazlı + timestamps ile uygular. Müzik için `sfxgen.mjs`/cues yaklaşımı 2. sürümde (şimdilik `timeline.music` ile hazır dosya, −15 dB). |
| QA | `inner-voice-film/scripts/qa.ps1` (tsc → compositions → stills), `09-remotion-build-and-qa.md` (Windows: `npx.cmd`, `--frames` tırnaklı, `--props` dosya şart, EBUSY=OneDrive), `stills.ps1` + `contact.py`. `lowbudgetstories-dna/scripts/rhythm_qa.py` (ffmpeg+numpy; cut/reframe/pan tespiti, LUFS, transcript ile WPM/pause; exit 1 = FAIL). | `qa_render.ps1` = kare çekme + kontak + rhythm_qa (voiced). |
| Upload | `daily-film-pipeline/SKILL.md` (Linux VPS akışı): `.venv-yt/bin/python studio/scripts/youtube/youtube_upload.py --meta upload.json`; `yt_auth.py` (OAuth Desktop, scope upload+youtube+analytics, token `secrets/youtube_token.json`), `yt_common.py` (`ROOT = parents[3]`), `preflight.sh` (günde 1 film, key, token, disk, tsc), `publish_time.py` (17:00 Europe/London). Discord raporu SKILL'de metin olarak tarif edilmiş; ayrı script yok. Credential dosyaları Windows'ta `C:/dev/secrets/` altında olmalı — **şu an yok** (VPS'te var). | `s_upload` aynı script'i çağırır; `--yt-python` ile venv seçilir. |
| Thumbnail | `other-self-thumbnail/generator/render.py`: `thumb.html?config=` → headless Edge `--screenshot` → Pillow 320 önizleme + kontak; Higgsfield adımları `references/03`: `media_upload` → PUT (Content-Type + If-None-Match) → `media_confirm` → `generate_image nano_banana_pro` 2 aday ≈ 4 kredi → `baseImage` ile yazı. | Aynı Edge yolu + aynı Higgsfield adımı (Claude çağırır; kodda yok). |
| Araçlar | node 24.19, python 3.12.10 (PIL 12.3, numpy, jsonschema 4.26; **cairosvg yok**), ffmpeg/ffprobe 9.0.2 (svg decoder yok), Edge `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`, yt-dlp, `ELEVENLABS_API_KEY` env'de var. Google fonts: Fredoka/Nunito/Rubik/Poppins/Inter latin-ext mevcut. | |

## 2. Stage tablosu

| # | Stage | Girdi | Çıktı | Araç | Kim | Süre (10 dk video) | Maliyet |
|---|---|---|---|---|---|---|---|
| 1 | idea | `--idea` metni veya boş; `dataset.csv`, A/B/C raporları | `idea.md` (soru, mekanik, etiket türü, 6 sahne planı, hook) | Claude + **NexLev MCP** (`search_videos`, `faceless_outliers_videos`, `get_bulk_video_transcripts`) | LLM | 5–10 dk | NexLev kota |
| 2 | package | `idea.md` | `package.json` (title, 2 alt, hook, thumb{text,label,layouts,pick}) | Claude (A-packaging kuralları) | LLM | 3 dk | – |
| 3 | script | idea + package | `script.md` + `script.json` (60–120 segment, `spoken` rakamlar yazıyla, style) | Claude (D-script kuralları); validator: segment sayısı/kelime≈135 wpm | LLM | 10–15 dk | – |
| 4 | tts | `script.json`, `whatif_voice.json` | `audio/vNN.mp3` + `vNN.json` (hash, dur, words) → `timeline.json` | `tts_segments.py` → ElevenLabs `with-timestamps`, ffmpeg loudnorm, ffprobe | kod | 3–6 dk (API) | ~9–11k karakter |
| 5 | shots | `script.json` + `timeline.json` + şema | `shots.json` (150–220 shot; medyan 2.3–3.8 s) | Claude (prompt `shots.md`); validator: şema, bitişiklik, vo id, toplam = timeline ±1.5 s, ritim istatistiği | LLM | 10–20 dk | – |
| 6 | render | shots+timeline → `props.json`; mp3'ler stüdyo `public/audio/whatif/<slug>/` | `render/<slug>-draft.mp4` (scale 0.5, crf 28) → `qa/*.jpeg` (her shot start+5) → `render/<slug>.mp4` (h264 crf 18, aac 320k) | `npx remotion render` ×3, ffprobe (ses akışı kontrolü) | kod; **Claude kareleri gözle denetler** | draft 5–8 dk, final 15–25 dk (CPU, concurrency 4) | elektrik |
| 7 | thumb | `package.json.thumb` | `thumbs/<slug>-{A,B,C}.png` + `_320` + `<slug>-final.png` | `make_thumbnail.py` (Edge headless); opsiyonel **Higgsfield** `nano_banana_pro` img2img (Claude) → `--base-image` | kod (+Claude seçer) | 1 dk (+3 dk Higgsfield) | 0 (+≈4 kredi) |
| 8 | meta | package + script.md | `meta.json` (LLM) → `description.txt` (bölümler shots overlay'lerinden otomatik) + `upload.json` | Claude + pipeline | LLM+kod | 3 dk | – |
| 9 | upload | `upload.json`, mp4, png, token | YouTube video id/URL, `PUBLISHED.md` satırı | `youtube_upload.py` (Data API v3) | kod | 3–8 dk (yükleme) | ~1650 API birimi/gün (10k kota) |
| QA | (render sonrası) | mp4, shots, timeline | `qa/frames/*.jpg`, `qa/contact.jpg`, `qa/rhythm/report.json` | `qa_render.ps1` → ffmpeg + `rhythm_qa.py` | kod; Claude okur | 2–4 dk | – |

Toplam makine süresi ≈ 45–60 dk; LLM adımları ≈ 30–50 dk; insan onayı opsiyonel (package ve thumbnail seçimi önerilir).

## 3. Tasarım kararları (gerekçeli)

**(1) Remotion + SVG rig, AI video değil.** Hedef nişin videoları (dataset: 100 video, 8 hit) stick-figure/low-poly ve
yoğun metin/sayı overlay'li; görsel değer **bilgi UI'sındadır** (kafa üstü sayı), fotogerçekçilikte değil. Remotion:
(a) deterministik — aynı JSON aynı kareyi verir, QA tekrar edilebilir; (b) marjinal maliyet 0 (AI video 10 dk için
yüzlerce kredi + stil kayması + Türkçe metin bozulması); (c) Türkçe yazı/etiket native (font latin-ext); (d) mevcut
stüdyo ve kanıtlı QA döngüsü (inner-voice-film) hazır; (e) senaryo değişince yalnız JSON değişir, yeniden çizim yok.
AI görüntü yalnızca thumbnail polish'inde (ölçülmüş: nano_banana_pro ≈ 2 kredi/aday) ve ileride arka plan plakalarında
(LBS 06 §5.5 tarzı; şimdilik SVG sahneler).

**(2) Karakter rigi (`StickFigure.tsx`).** Rig birimleri: zemin y=0, kafa r=26 @ y=−150, boyun −122, kalça −80;
uzuvlar FK (üst açı + göreli büküm) → tek `path` → kopma imkânsız (the-other-self rig.ts ilkesi). **8 poz**: stand,
walk, run, sit, point, phone, armsUp, slump (`POSES`); walk/run **faz tabanlı döngü** (`cyclePose`, 24 f / 14 f;
diz bükümü yalnız ileri salınımda; gövde bob). **6 ifade** (`faceSVG`): neutral, happy, sad, shocked, angry, worried —
tek karede değişir (LBS: ifade twin'lenmez). Kahraman = izleyici ("sen"): `hero: true` → turuncu atkı; kalabalık gri
`inkSoft`. `lerpLimbs` yalnız fiziksel geçişler için. **HeadLabel**: pil + ok, `number` (binlik nokta, count-up
easeOutCubic, `from`), `text`, `icon` (heart/money/skull/clock/eye/lie/star), 5 ton, `appear` karesinde back-ease pop,
hafif süzülme (`sin(frame/12)`, deterministik). **Crowd**: N figür, `random(seed)` ile x/derinlik/poz/ifade/faz/etiket,
derinliğe göre ölçek+opaklık, `walk` ile sonsuz kayan yürüyüş, `exclude` kahraman alanı, etiket havuzu
(`values`/`texts`/`icons`). **6 sahne**: street (binalar, gece yıldız/pencere ışığı), office (4 masa+monitör+tabure,
x=420/820/1220/1620), home (kanepe x=760, lamba, TV), school (tahta + `boardText`, 3 sıra), transit (kayan pencere
bandı, direkler), wedding (kemer, ampul dizisi, masalar). Hepsi `night` destekler, çocuk olarak karakterleri alır.
Kamera: push (vars. 0.016/sn — LBS ölçümü 1.0–2.6 %/sn), pull, pan, static; `trans: dip|fade|cut`.

**(3) `shots.json` şeması** (`scripts/shots_schema.json`): `{slug, title, fps, shots[]}`; shot =
`{id s01.., t_start, dur (0.8–12 s), scene, night, boardText, trans, characters[{id, pose, expr, x, y, scale, facing,
hero, color, label, move{to,ease}, poseAt[{at,pose,expr}]}], crowd{n, walk, x, depth, exclude, labels{kind, values|texts|icons,
tones, unit}}, camera{type, rate, zoom, from, to, origin}, overlay{text, kind card|title|lower|counter, sub, at, dur}|[],
sfx[{name, at, gain}], vo_segment}`. Zamanlar saniye (LLM için doğal, fps'ten bağımsız); kare = `round(t·fps)`.
Validator ayrıca bitişiklik, vo id varlığı, toplam süre, medyan/kesme-dk hesaplar.

**(4) Senaryo → shot list dönüşümü = LLM (Claude).** Prompt `templates/prompts/shots.md`: script.json + timeline.json
(gerçek süreler) + şema verilir; kurallar: her segment ≥1 shot, >4 s segment bölünür, bitişiklik, kahraman sürekliliği,
etiket sayıları script ile aynı, kalabalık kullanımı, kamera ritmi, overlay'ler bölüm başlıklarıyla (meta stage bunlardan
zaman damgası üretir). Validator yakalayınca Claude düzeltir (`--from shots`). Neden LLM: sahne/poz/etiket seçimi
anlamsal; kural tabanlı eşleme (sahne ipucu → shot) ilk sürümde yetersiz kalır. İleri sürüm: `script.json`'daki
`scene`/`beat` alanlarından kural tabanlı **taslak** üretip LLM'e "düzelt" diye vermek (token tasarrufu).

**(5) TTS segment bazlı + timestamps.** Vuruş başına mp3: (a) segment süresi = shot süresi referansı; (b) tek segment
yeniden üretilebilir (hash ile idempotent, `--force`); (c) Remotion'da her segment `<Sequence from><Audio>` → senkron
kayması birikmez. `eleven_say.py` timestamps desteklemiyor → `with-timestamps` ucu (`audio_base64` + `alignment`
karakter zamanları → kelimeler). Kırpma (silenceremove) sonrası kelime zamanları lead'e göre kaydırılır. Fallback: düz
TTS + karakter uzunluğuna orantılı tahmin (`words_src: estimate`). `ffmpeg silencedetect` gerekmedi (ffprobe süre
yeterli). Caption `word` (karaoke, 5 kelimelik pencere, vurgu sarı) / `line` / `off`.

**(6) Render**: draft `--scale=0.5 --crf=28 veryfast` (hızlı gözle kontrol) → QA kareleri (her shot start+5, ≤24) →
final `h264 crf 18 yuv420p aac 320k`. ffprobe ile ses akışı doğrulanır. Tek shot için `whatif-shot` kompozisyonu +
`--props` (`shotId`) ile `npx remotion still`.

**(7) Thumbnail**: `thumbnail.svg` + `make_thumbnail.py`; metin 1–4 kelime BÜYÜK HARF (≤9 karakter satır → 150 px,
≤13 → 118, aksi 92), stroke 16 px + gölge, etiket pili + glow; layout A/B/C; `--base-image` ile Higgsfield çıktısının
üstüne aynı yazı/etiket (hibrit: kompozisyon bizim). Rasterizer kararı: cairosvg/resvg yok → Edge headless; Edge'in
PNG'yi süreç döndükten sonra yazdığı görüldü → dosya bekleme + `--headless` fallback eklendi (test: 3/3 başarılı).

**(8) Metadata**: `meta.json` LLM (başlık ≤70, açıklama ilk 150 karakter hook, etiketler ≤30, hashtag), pipeline
`description.txt` = açıklama + **Bölümler** (overlay `title|card` olan shot'ların `t_start`'ı; 0:00 zorunlu) + hashtag;
`upload.json` daily-film-pipeline formatında (+`language: tr`).

**(9) Upload**: `youtube_upload.py --meta upload.json` (resumable, thumbnail set, `publish_at` → private+scheduled);
`--dry-run` body'yi basar. Notlar: (a) `defaultLanguage/defaultAudioLanguage` script'te `'en'` sabit → `m.get('language','en')`
yaması (2 satır) önerilir; (b) denetlenmemiş API projesi yüklemeleri **private**'a kilitler (SKILL notu) → ilk haftalarda
"Publish"e elle basmak gerekir; (c) günlük kota 10k ≈ 6 upload.

**(10) Orkestrasyon**: `pipeline.py <slug>`; `STAGES` sabit sıra; `state.json` `{stages:{name:{status pending|running|
done|failed|needs_llm|dry, started, finished, error, outputs}}}`; `--from X` X ve sonrasını `pending` yapar; `--only`;
`--to`; `--status`. Hata: stage `failed`, log'a "devam: --from <stage>", exit 1. LLM stage'leri: çıktı yoksa prompt
dosyası + exit 3; `--llm "<komut>"` verilirse prompt stdin→komut, stdout→dosya (````json` bloğu ayıklanır), validator
geçmezse hata. Neden exit 3: Claude Code'un kendisi LLM; alt süreçten `claude -p` çağırmak hem pahalı hem iç içe
oturum sorunları yaratır. Varsayılan akış: Claude `pipeline.py`'yi çağırır → 3 alırsa promptu uygular → tekrar çağırır.

## 4. Smoke test sonucu

Yer: `<scratchpad>/whatif/remotion-smoke/` (stüdyo kopyalanmadı; `node_modules` → `C:\dev\the-other-self\node_modules`
**junction**; `src/lib/whatif/` = templates kopyası; Root.tsx `whatif-film` + `whatif-shot`).

| Adım | Sonuç |
|---|---|
| `npx tsc --noEmit` (strict, noUnusedLocals) | **0 hata** (ilk denemede) |
| `npx remotion compositions` | 1. deneme: package.json **UTF-8 BOM** (PowerShell `Out-File -Encoding utf8` BOM yazar) → cosmiconfig JSON hatası. Düzeltme: BOM silindi. 2. deneme: chrome-headless-shell **spawn ENOENT** — junction yolu üzerinden exe bulunamadı. Düzeltme: `--browser-executable=<stüdyodaki gerçek exe>`. 3. deneme: **OK** (`whatif-film` 150 kare, `whatif-shot`). |
| `npx remotion render whatif-film --scale=0.5 --crf=28` | **OK** → `out/smoke-draft.mp4`: h264, 960×540, **5.000 s** (calculateMetadata `totalFrames` doğru) |
| QA kareleri 10/40/70/100/130 | Başlık kartı (Türkçe ğ/ş/ı/İ doğru, Fredoka yüklendi), sokak + yürüyen kahraman (etiket "3" count-up) + 7 kişilik yürüyen kalabalık (etiketler 359 / 2.338 / 2.289, binlik nokta), ofis: oturan kahraman + kırmızı "✕ 1.204" + "Patron" etiketi + sağ üst "GÜN 1" sayacı, kelime-kelime altyazı (sarı vurgu). |
| Bulunan kusurlar | (a) oturma pozunda ayaklar zemine değmiyordu (kalça = −shin + hipY yanlış) → `hipY = sitting ? −shin : hipY` + ofis/okul tabure, kanepe oturağı düzeltildi; (b) altyazı kelimeleri arasında boşluk yoktu (inline-block margin render'da kayboldu) → `' '` metin düğümü + padding. Yeniden still: ikisi de **düzeldi** (gözle doğrulandı). |
| Thumbnail | `make_thumbnail.py` A/B/C → 3×PNG 1280×720 + `_320` **OK** (ilk denemede Edge PNG'yi geç yazdı → bekleme döngüsü eklendi). |
| pipeline.py | `--dry-run` → idea stage `needs_llm`, exit 3, `state.json` + `prompts/idea.prompt.md` yazıldı; örnek shots/timeline ile `--only shots` → şema + bitişiklik + istatistik **OK**, `--status` doğru. |
| Doğrulanmayan | Gerçek ElevenLabs çağrısı (voice_id placeholder, kota harcamamak için), gerçek stüdyoya entegrasyon (register.ts adımları uygulanmadı — talimat gereği kopyalanmadı), final crf 18 render, upload (token yok), rhythm_qa 10 dk videoda. |

Smoke komutu (tekrar için):
```powershell
cd <scratchpad>\whatif\remotion-smoke
npx.cmd remotion render src/index.ts whatif-film out/smoke-draft.mp4 --scale=0.5 --crf=28 --x264-preset=veryfast "--browser-executable=C:\dev\the-other-self\node_modules\.remotion\chrome-headless-shell\win64\chrome-headless-shell-win64\chrome-headless-shell.exe"
```
Gerçek stüdyoda (`src/lib/whatif/` içinde) junction olmadığı için `--browser-executable` gerekmez; gerekirse `WHATIF_BROWSER` env'i pipeline'a geçirir.

## 5. Hata modları ve kurtarma

| Hata | Belirti | Kurtarma |
|---|---|---|
| UTF-8 BOM | `JSON Error ... Unexpected token` (cosmiconfig/remotion) | JSON/TS dosyalarını PowerShell `Out-File -Encoding utf8` ile YAZMA (BOM ekler); Python `write_text(encoding='utf-8')` veya `[IO.File]::WriteAllText` kullan. pipeline.py tüm dosyaları BOM'suz yazar, okurken `utf-8-sig` tolere eder. |
| Chrome spawn ENOENT | junction/symlink'li node_modules | `WHATIF_BROWSER=<gerçek exe yolu>` (pipeline `--browser-executable` ekler) veya stüdyonun kendi klasöründen çalış |
| Windows konsol cp1252 | `UnicodeEncodeError ... '\u0131'` | Üç script `sys.stdout.reconfigure(utf-8)` yapar (eklendi) |
| ElevenLabs 401/429/422 | `HTTP 4xx` | 401: env anahtarı; 429: kota/eşzamanlılık → `--from tts` (hash sayesinde yalnız eksik segmentler); 422 `with-timestamps` v3'te → otomatik düz TTS fallback (`words_src: estimate`) |
| TTS süresi hedef dışı | tts log "UYARI: 8–10 dk dışı" | `script.json` vuruş ekle/çıkar → `--from tts` (değişmeyen segmentler yeniden üretilmez) |
| shots.json şema/bitişiklik | validator mesajı, exit 1 | Claude shots.json'ı düzeltir → `--from shots` |
| Remotion `delayRender timeout` (font) | ilk render'da Google Fonts indirme | ağ gerekli; ikinci deneme cache'den; alternatif: fontu `public/fonts`'a koy + `@font-face` |
| EBUSY/EPERM | OneDrive/antivirüs/açık oynatıcı | stüdyo OneDrive dışı (C:\dev); mp4'ü kapat |
| Render OOM / çok yavaş | 10 dk × 30 fps = 18k kare | `--concurrency=2`, ya da `--frames=a-b` parçalar + ffmpeg concat; kalabalık n ≤ 20, blur filtresi yok |
| Final'de ses yok | ffprobe audio stream yok → pipeline RuntimeError | mp3'ler `public/audio/whatif/<slug>/` kopyalandı mı; `timeline.file` göreli yol `audio/whatif/<slug>/vNN.mp3` |
| Edge PNG üretmedi | `Edge PNG üretmedi` | başka Chrome: `THUMB_BROWSER`, veya `npm i -g @resvg/resvg-js` + `--engine resvg` |
| YouTube token yok/expired | `youtube_token.json` yok | `python yt_auth.py` (Desktop OAuth client: `C:/dev/secrets/client_secret.json`); kota 10k/gün |
| Upload private kaldı | API projesi denetlenmemiş | YouTube Studio'da elle Publish; `publish_at` sonraya |
| rhythm_qa FAIL | plan medyanı > norm, LUFS düşük | shots.json'da uzun shot'ları böl; final `loudnorm I=-14` (ffmpeg `-c:v copy`) |

Resume ilkesi: her stage çıktı dosyasına bakar; `state.json` yalnız özet. `--from X` ile X'ten itibaren yeniden; dosyaları
silmez (tts hash'leri, mevcut draft/final atlanır — tam yeniden render için `render/` klasörünü sil).

## 6. İlk videoyu 1 günde çıkarma — adım listesi

**Kurulum (bir kez, ~1 saat)**
1. Stüdyoya ekle: `Copy-Item "$env:USERPROFILE\.claude\skills\whatif-animated-dna\templates\remotion\*.ts*" C:\dev\the-other-self\src\lib\whatif\ -Exclude register.ts` + `sample\` klasörünü kopyala; `Root.tsx`'e `register.ts`'teki `<Folder name="whatif">` bloğunu ekle; `npx.cmd tsc --noEmit` ve `npx.cmd remotion compositions src/index.ts`.
2. Ses: `python scripts\tts_segments.py --list-voices` → Türkçe erkek anlatıcı seç (Voice Library'den "Turkish" filtresiyle ekle) → `whatif_voice.json` `voice_id`; model `eleven_multilingual_v2`. 1 cümlelik `script.json` ile test; `vNN.json` içinde `words_src: elevenlabs-timestamps` olduğunu doğrula.
3. YouTube: `C:/dev/secrets/client_secret.json` (Desktop OAuth) → `python C:\dev\the-other-self\scripts\youtube\yt_auth.py` (google-api-python-client + google-auth-oauthlib kurulu bir venv; pipeline'a `--yt-python` ile ver). `youtube_upload.py`'de `defaultLanguage: m.get('language','en')` yaması (2 satır).
4. `mkdir C:\dev\whatif-projects` (veya `WHATIF_ROOT`).

**Üretim (video başına ~2–3 saat makine + LLM)**
5. `python pipeline.py <slug> --idea "Ya ... olsaydı?"` → exit 3 → Claude `prompts/idea.prompt.md`'yi uygular (NexLev ile kanıt), `idea.md` yazar → `--from idea`.
6. package → `package.json` (başlık, thumb metni; A-ajanı kuralları) → `--from package`.
7. script → `script.md` + `script.json` (60–120 segment, rakamlar yazıyla) → validator (kelime ≈ 8–10 dk) → `--from script`.
8. tts → `timeline.json` (toplam süre loga yazılır; 7–11 dk değilse script'e dön).
9. shots → Claude `shots.json` (prompt + şema + timeline) → validator (medyan 2.3–3.8 s, 11–20 kesme/dk).
10. render → draft + QA kareleri → **Claude kareleri açıp bakar** (etiket/yüz çakışması, güvenli alan, boş kare, Türkçe karakter) → düzeltme shots.json'da → `--from render` → final. `qa_render.ps1 -Project ... -Final` → rhythm raporu.
11. thumb → A/B/C + 320 önizleme → Claude seçer (`package.thumb.pick`); isteğe bağlı Higgsfield polish (`--no-text` ile üret → `media_upload` → nano_banana_pro 2 aday ≈ 4 kredi → `--base-image`).
12. meta → `meta.json` → description.txt (bölümler otomatik) + upload.json → `--dry-run` ile body kontrol.
13. upload → `PUBLISHED.md`; private kaldıysa Studio'dan Publish; sabitlenmiş yorum (`meta.pinned_comment`) elle.

**Zaman planı (ilk gün)**: 09:00 kurulum (1–3) · 10:00 idea+package+script (5–7) · 11:30 tts+shots (8–9) · 13:00 draft render + QA turu 1 (10) · 14:30 düzeltme + final render · 16:00 thumbnail + meta (11–12) · 17:00 upload (13).

## Neden çalışıyor (boru hattı açısından)

1. **Ölçülmüş süreler üstüne kurgu**: TTS önce, shot list sonra → her shot gerçek konuşma süresine kilitli; senkron kayması birikmez (segment başına ayrı `<Sequence>`).
2. **Tek veri kaynağı, iki JSON**: `timeline.json` + `shots.json` hem render hem QA hem bölüm zaman damgaları için kullanılır; bir düzeltme tek yerde yapılır.
3. **Deterministik görüntü**: `useCurrentFrame` + `interpolate` + `random(seed)`; aynı girdi aynı kare → QA karelerine güvenilir, yeniden render ucuz.
4. **LLM yalnız anlam gerektiren yerde** (fikir, paket, senaryo, shot seçimi, metadata); zamanlama/ses/render/yükleme kodda → maliyet ve hata yüzeyi küçük, çıktı şemayla denetlenir.
5. **İdempotent stage'ler + state**: ElevenLabs kotası, render dakikaları ve YouTube kotası tekrar harcanmaz; hata nerede kaldıysa oradan.

## Kopyalanacak kurallar (ölçülebilir, emir kipi)

1. Senaryoyu 60–120 segmente böl; her segment ≤ 25 kelime; rakamları `spoken` alanında yazıyla ver.
2. TTS'i segment bazlı üret, `with-timestamps` ile kelime zamanı al; toplam 7–11 dk değilse render'a geçme.
3. shots.json'ı şemadan geçir: bitişik, çakışmasız, toplam = timeline ±1.5 s; plan medyanı 2.3–3.8 s, 11–20 kesme/dk, hiçbir shot > 8 s.
4. Kahramanın kafa üstü etiketi ilk 10 sn içinde görünsün (`label.appear`), her 25–40 sn'de yeni sayı/ifşa.
5. Her render'da önce draft (scale 0.5) + her shot'tan 1 kare; kareler gözle denetlenmeden final render'a geçme.
6. Final: h264 crf 18, yuv420p, aac 320k; ffprobe ile ses akışı doğrula; LUFS −14 ±1 (rhythm_qa).
7. Thumbnail: 1–4 kelime BÜYÜK HARF, etiket pili görünür, 320×180 önizlemede okunur; yazı başlığı tekrarlamasın.
8. Açıklama: ilk 150 karakter hook; bölümler shots overlay'lerinden; 0:00 zorunlu.
9. Upload private + `publish_at`; `PUBLISHED.md`'ye satır; günde 1 video (kota 10k ≈ 6 upload üst sınır).
10. Gizli değerleri (API anahtarı, token, voice_id dışı kimlikler) hiçbir log/rapora yazma; `voice.json` yalnız kullanıcı onayıyla değişir.

## Türkçe uyarlama notları

- Font: `latin-ext` alt kümesi zorunlu (ğ, ş, ı, İ, ç, ö, ü); Fredoka 700 smoke testte doğru render etti. `toUpperCase()` JS'te "i" → "I" verir (Türkçe "İ" değil); thumbnail metnini kullanıcı/LLM baştan büyük harf yazsın veya `toLocaleUpperCase('tr')` kullanılsın (make_thumbnail.py `upper()` Python tarafında da aynı sorun → metni büyük harf ver).
- Sayı biçimi: `HeadLabel` binlik ayırıcı nokta, ondalık virgül (1.204 · 3,5). TTS'e sayılar yazıyla (`spoken`), ekrana rakamla (`text`).
- Türkçe konuşma hızı ≈ 130–140 kelime/dk (İngilizce 150–160); 8–10 dk için 1.100–1.450 kelime. Validator 135 wpm varsayar; ilk TTS'ten sonra gerçek oranla güncelle.
- ElevenLabs: `eleven_multilingual_v2` Türkçe'yi otomatik algılar (`language_code` parametresi bu modelde gönderilmez — kod bunu atlar); flash/turbo v2.5'te `language_code: tr` gönderilir.
- 2. tekil şahıs anlatım ("görüyorsun", "sen") altyazıda kısa kelimeler üretir → karaoke penceresi 5 kelime uygun.
- YouTube: `defaultLanguage/defaultAudioLanguage = tr` (upload script yaması), kategori 1 (Film & Animation) veya 24 (Entertainment) — A ajanı kararı.

## 7. Açık sorular / düşük güven

- **ElevenLabs `with-timestamps` + eleven_v3**: v3 için timestamps ucu belgelerde garanti değil; kod fallback yapıyor ama v3'te Türkçe kalite/zamanlama test edilmedi (kota harcamamak için gerçek çağrı yapılmadı). Öneri: multilingual_v2 ile başla, 1 segment v3 ile kıyasla.
- **Kelime zamanlaması kırpma düzeltmesi**: alignment ham sese göre; `silenceremove` baş/son kırpınca lead çıkarılıp süreye oranlanıyor (yaklaşık; ±50 ms). Altyazı için yeterli; "sayı ekranda tam o kelimede belirsin" isteniyorsa kırpmayı kapat.
- **Müzik/SFX**: `shots.sfx` şemada var, Remotion tarafında henüz çalınmıyor (`timeline.music` loop var). 2. sürüm: `sfxgen.mjs` ile pop/whoosh/ding → `public/sfx/` → `WhatIfFilm` içinde `<Sequence><Audio>`; ducking için cues yaklaşımı.
- **Render süresi tahmini** (15–25 dk) the-other-self 2:45'lik filmlerinin oranından; 10 dk + 20 kişilik kalabalık + metin ile ölçülmedi. İlk final render'da `--log=verbose` ile en yavaş kareleri ölç.
- **Stick figure görünümü** placeholder: palet ve karakter imzası (atkı rengi, kafa dolgusu) marka kararı bekliyor (`theme.ts`). Nişin low-poly/3D görünümlü örneklerine yaklaşmak gerekirse: arka plan plakalarını Higgsfield ile üretip `SceneX` içine `<image>` koymak (LBS 06 §5.5), karakter yine SVG.
- **Upload tarafı Windows'ta hiç çalıştırılmadı** (venv, client_secret, token yok); VPS'te çalışan akış birebir; `ROOT=parents[3]` → `C:/dev/secrets/`.
- **`--llm "claude -p"`** yazıldı ama test edilmedi (iç içe Claude oturumu riski); varsayılan akış exit 3.
- **Shorts**: ayrı 1080×1920 kompozisyon yok; `meta.shorts` yalnız öneri.

## Diğer ajan için not

- **A (paket/başlık)**: `package.json` alanları (`title ≤70`, `thumb.text 1–4 kelime`, `layouts`, `pick`) ve `make_thumbnail.py` layout tanımları (A karakter+etiket, B kalabalık, C yakın yüz) sizin kurallarınızla güncellenmeli; `templates/prompts/package.md`'ye başlık kalıplarınızı ekleyin.
- **D (senaryo)**: `script.json` segment formatı (`id vNN`, `text`, `spoken` rakamlar yazıyla, `style hook|narrator|calm`, `pause_after`, `scene`, `beat`) ve 135 kelime/dk varsayımı; vuruş sayısı 60–120. Retention kuralları `templates/prompts/script.md`'ye eklenmeli.
- **B/C (hook/retention, görsel)**: shot ritmi eşikleri şu an LBS normundan (medyan 2.3–3.8 s, 11–20 kesme/dk); "What If" nişinin ölçülen ritmi farklıysa `pipeline.py v_shots` eşiklerini ve `shots.md` kural 1'i güncelleyin. Kafa üstü etiketin ilk görünme anı `shots.json` `label.appear` ile kontrol ediliyor.
