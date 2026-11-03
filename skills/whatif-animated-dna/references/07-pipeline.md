# 07 — Tam otomatik üretim hattı

Kaynak: `deep-research/E-pipeline.md`. Kod: `scripts/`, `templates/`. Smoke test başarılı (5 sn, 3 sahne, Türkçe glifler, kalabalık, karaoke altyazı).

## 1. Akış

```
idea → package → script → tts → shots → render → thumb → meta → upload
 LLM     LLM      LLM     kod    LLM     kod+göz   kod     LLM    kod
```

Sıra bilinçli: **önce TTS, sonra shot list**. Shot'lar gerçek konuşma sürelerine kilitlenir; ses-görüntü kayması birikmez.

| # | Stage | Çıktı | Araç | Süre (10 dk video) |
|---|---|---|---|---|
| 1 | idea | `idea.md` | Claude + NexLev MCP | 5–10 dk |
| 2 | package | `package.json` (başlık, alternatifler, hook, thumb) | Claude + `02`, `03` | 3 dk |
| 3 | script | `script.md` + `script.json` (60–120 segment) | Claude + `04` | 10–15 dk |
| 4 | tts | `audio/vNN.mp3` + `timeline.json` | `tts_segments.py` (ElevenLabs with-timestamps) | 3–6 dk |
| 5 | shots | `shots.json` (şemalı) | Claude + `05` + `shots_schema.json` | 10–20 dk |
| 6 | render | draft (0,5 ölçek) → QA kareleri → final h264 crf 18 | Remotion 4.0.535 | 5–8 + 15–25 dk |
| 7 | thumb | A/B/C PNG + 320 önizleme | `make_thumbnail.py` (headless Edge) ± Higgsfield | 1–4 dk |
| 8 | meta | `meta.json` → `description.txt` (bölümler otomatik) + `upload.json` | Claude + pipeline | 3 dk |
| 9 | upload | YouTube video id | `the-other-self/scripts/youtube/youtube_upload.py` | 3–8 dk |
| QA | — | kareler, kontak sayfası, ritim raporu | `qa_render.ps1` + `rhythm_qa.py` | 2–4 dk |

Makine ≈ 45–60 dk, LLM adımları ≈ 30–50 dk.

## 2. Çalıştırma

```powershell
$S = "$env:USERPROFILE\.claude\skills\whatif-animated-dna\scripts"
python "$S\pipeline.py" <slug> --idea "Ya herkesin maaşını görebilseydin?"
```

- LLM stage'i çıktı yoksa `prompts/<stage>.prompt.md` yazar ve **exit 3** ile durur. Claude o promptu bu skill'in referanslarıyla uygular, dosyayı yazar, sonra `--from <stage>` ile devam eder.
- Diğer bayraklar: `--only X`, `--to X`, `--status`, `--dry-run`, `--draft-only`, `--yt-python <venv python>`, `--llm "<komut>"` (test edilmedi).
- Her stage idempotent; `state.json` + `pipeline.log`. Hata olursa log "devam: --from <stage>" yazar.
- Proje kökü: `WHATIF_ROOT` env veya varsayılan `C:\dev\whatif-projects\<slug>`.

## 3. Veri omurgası

- `script.json`: `{slug, fps, segments[{id vNN, text, spoken (rakamlar yazıyla), style hook|narrator|calm, pause_after, scene, beat}]}`.
- `timeline.json`: TTS'ten gerçek `start/dur` + kelime zamanları.
- `shots.json`: `scripts/shots_schema.json`. Shot = `{id, t_start, dur 0,8–12, scene (street/office/home/school/transit/wedding), night, trans dip|fade|cut, characters[{pose 8, expr 6, x, scale, facing, hero, label, move, poseAt}], crowd{n, walk, labels}, camera push|pull|pan|static, overlay card|title|lower|counter, sfx, vo_segment}`.
- Üst düzey `profile`: "A" (18–26 kesme/dk) ya da "B" (8–13). `scene: "infocard"` + `card {kind counter|bars|grid, title, value, unit, items, source}`.
- Validator: şema, bitişiklik, vo id varlığı, toplam = timeline ±1,5 sn; profil ritmi (uyarı); sert sınırlar >30 kesme/dk, medyan <1,5 sn, ilk 15 sn >10 kesme, >10 sn planda değişim yok (hata); infografik kart sayısı (uyarı).
- Diğer doğrulayıcılar: package (≤55 karakter, ≤8 kelime, "?", rubrik ≥5, thumbnail metni başlığı tekrar etmez, `contradiction` var), script (tahmini ≤11 dk; `WHATIF_WPM` varsayılan 145), tts (toplam ≤11 dk, gerçek kelime/dk loglanır).
- Altyazı varsayılanı `--captions off` (hit'lerde karaoke yok); Shorts için `word`.

## 4. Remotion bileşenleri (`templates/remotion/`)

| Dosya | İş |
|---|---|
| `WhatIfFilm.tsx` | Tek kompozisyon `whatif-film`; props = shots + timeline; segment başına `<Audio>` |
| `StickFigure.tsx` | Özgün çöp adam FK rigi; 8 poz (stand, walk, run, sit, point, phone, armsUp, slump), 6 ifade, yürüme/koşma döngüsü; kahraman turuncu atkı |
| `HeadLabel.tsx` | Kafa üstü sayı/metin/ikon; count-up; 5 ton; pop girişi |
| `Crowd.tsx` | Seed'li N kişi + etiket havuzu + yürüyüş |
| `Caption.tsx` | Kelime kelime karaoke / satır / kapalı |
| `Scene*.tsx` | 6 sahne, gece modu |
| `SceneInfoCard.tsx` | Lacivert infografik kart: counter, bars ("NORMAL vs SEN"), grid; kaynak satırı |
| `theme.ts`, `fonts.ts` | Ölçülmüş palet (`05` §5), Fredoka latin-ext |
| `register.ts` | Stüdyoya ekleme talimatı |

Stüdyo: `C:\dev\the-other-self` (remotion 4.0.535, React 19). Bileşenler `src/lib/whatif/` altına eklenir; Root.tsx'e `register.ts`'teki blok eklenir. **Henüz eklenmedi.**

## 5. Kurulum (bir kez)

1. Stüdyoya ekle: `templates/remotion/*` → `C:\dev\the-other-self\src\lib\whatif\`; Root.tsx'e `register.ts` bloğu; `npx.cmd tsc --noEmit`.
2. Ses: `python scripts\tts_segments.py --list-voices` → Türkçe anlatıcı seç → `scripts/whatif_voice.json` içindeki `voice_id` placeholder'ını değiştir. Model `eleven_multilingual_v2`.
3. YouTube: `C:/dev/secrets/client_secret.json` + `yt_auth.py` ile token; `youtube_upload.py` içinde `defaultLanguage` için `m.get('language','en')` yaması.
4. `C:\dev\whatif-projects` klasörü.

## 6. Hata modları

| Hata | Çözüm |
|---|---|
| JSON "Unexpected token" (BOM) | JSON/TS dosyalarını PowerShell `Out-File` ile yazma; Python `encoding='utf-8'` kullan |
| chrome-headless-shell spawn ENOENT | `WHATIF_BROWSER=<gerçek exe>` |
| cp1252 UnicodeEncodeError | Script'ler stdout'u UTF-8'e çeviriyor; yeni script'te de yap |
| ElevenLabs 429 | `--from tts`; hash sayesinde yalnız eksik segmentler üretilir |
| TTS toplamı 7–11 dk dışı | `script.json`'ı düzelt, `--from tts` |
| shots validator hatası | Claude `shots.json`'ı düzeltir, `--from shots` |
| Final'de ses yok | mp3'ler `public/audio/whatif/<slug>/` altında mı |
| Upload private kaldı | Denetlenmemiş API projesi; Studio'dan elle yayınla |

## 7. Doğrulanmayanlar

- Gerçek ElevenLabs çağrısı (voice_id seçilmedi).
- Stüdyoya gerçek entegrasyon, 10 dk final render süresi.
- Windows'ta upload (token ve venv yok).
- Müzik/SFX Remotion'da çalınmıyor (şemada var, 2. sürüm).
- Shorts kompozisyonu yok.
