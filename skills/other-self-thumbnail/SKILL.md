---
name: other-self-thumbnail
description: Thumbnail brain + generator for the YouTube channel "The Other Self" (minimalist 2D animated short films about inner struggles, main character "Moon head" with his blue shadow twin). Reverse-engineered from the viral thumbnails of "DISCIPLINE | An Animated Short Film" (3.1M), DOPAMINE and "JUST SHOW UP." by 3 research agents (pixel measurements, click psychology, production system). Produces the thumbnail concept (text, scene, emotion, light, triggers, title pairing), renders real 1280×720 PNGs with an SVG generator using our character, optionally finishes them with Higgsfield (nano_banana_pro / flux_3_image) and runs mobile-legibility QA and an A/B plan. Use this skill WHENEVER the user asks for a thumbnail, kapak görseli, küçük resim, thumbnail fikri/metni, CTR artırma, Test & Compare varyantları, "tıklanma oranı", thumbnail analizi, or packaging for a The Other Self / inner-voice animated film — even if they only say "kapak yap" or "thumbnail üret".
---

# The Other Self — Thumbnail Brain

Bu skill iki iş yapar: **(1) tıklatan thumbnail fikrini kurar** (neden tıklanır mantığıyla), **(2) gerçek
1280×720 PNG'yi üretir** — kendi karakterimiz Ay kafa ile, rakibin çizimini kopyalamadan.

## Beyin (tek cümle)

> **Tek yüz · tek "bedeli olan" duygu · gözler tek nesnede · siyah dünyada tek renkli ışık · sonu noktalı 1–3
> beyaz kelime.** Kararın hemen öncesindeki an gösterilir; kötü karakter gösterilmez — izleyici kendini görür.

Ayrıntı ve tetikleyici taksonomisi: `references/01-thumbnail-brain.md`. Ölçülmüş şablon: `references/02-measured-spec.md`.

> Not (test sonucu): rakipte gölge karakter thumbnail'da yoktu; bizde ise **ikizin kahramana sabotajı yaptığı an**
> (ör. gözlerini kapatması) en güçlü fikir çıktı. İkiz, kahramandan küçük/arkada ve aynı siluette (filizli) olmalı; A/B ile doğrula.

> **Çizim kalitesi (en önemli ders):** Temiz vektör veya yumuşak 3B render rakip kalitesinde DEĞİL. Final her zaman
> `references/05-style-dna.md` stil bloğu ile Higgsfield'da çizilir: elle mürekkeplenmiş kalın değişken çizgiler,
> dokulu boyalı gölgeler, büyük beyaz göz akı + küçük göz bebeği (yorgunluk/korkuda damarlı kanlanmış göz ve çökük
> göz altı), ter/kırışık, detaylı beş parmaklı eller, tek sıcak kenar ışığı. Kalite referansı:
> `reference-thumbs/OURS-v3-BEST-not-today.png`.

## Değişmez kurallar

1. Kahraman yakın plan: kafa kadraj yüksekliğinin %34–49'u (filmdekinden ~4× yakın). Ay kafa birebir karakter sayfasındaki gibi (filiz, oval gözler, kum rengi, ince kontur).
2. Duygu bedel taşır: öfke-kararlılık, korku-kararlılık, yorgunluk/özlem. Gülümseme yok, şok çığlığı yok.
3. Gözler ışık kaynağına bakar; okuma yolu yazı → yüz → ışık. Ok, daire, emoji yok.
4. **Tek ışık rengi = konunun metaforu** (kehribar saat/kapı, soğuk telefon, sıcak lamba, ay ışığı). Kanalın mavisi `#2F6BFF` yalnızca **ipucu** (yansıma, mavi kenarlı gölge, köşede küçük ikiz). Rakibin kırmızısı yok.
5. Yazı: Fredoka 700, beyaz, BÜYÜK HARF, 1–3 kelime, **nokta ile biter** (soru işareti de olur: "IS THIS IT?", "WHAT IF?"), üst bantta, yüzün üstüne binmez, harf yüksekliği ≥120 px. "!" yok.
6. Yazı başlığı tekrarlamaz: başlık = konu/acı kelimesi ("LONELINESS | An Animated Short Film"), yazı = ilk adım / saat / iç sesin yalanı / sahne adı ("TABLE FOR ONE.", "3:07 AM.", "TOMORROW.").
7. Sahne filmde gerçekten var (ilk 15 sn veya dönüş anı) — Test & Compare izlenme süresiyle karar verir, abartılı vaat kaybeder.
8. Telefon boyutunda (320×180, 168×94) üç şey okunmalı: kelime, kaş açısı, tek parlayan şekil.

## İş akışı

**1. Girdi.** Film başlığı + konu (+ varsa senaryo `SCREENPLAY.md`: ritüel, dönüm anı, iç ses satırları,
dönüşüm sembolü). `inner-voice-film` skill'iyle birlikte çalışır; onun paketleme adımında bu skill kullanılır.

**2. Konsept — Kanca Motoru (zorunlu).** Doğru ama düz bir sahne ("yatakta karakter + saat") tıklatmaz —
kullanıcı testi bunu gösterdi. Her film için 4 kanca türünden birer fikir yaz: **H1 absürt abartı · H2 görünür
iç ses (mavi ikiz sabotajı yaparken) · H3 gerçeküstü metafor · H4 aşırı duygu yakın plan**; her birini 6 soruluk
"feed'de durdurur mu" puanıyla değerlendir, ≥8/12 olanların en iyi 2–3'ünü üret
(`references/01-thumbnail-brain.md` §6b). Tetikleyiciler §4, hazır konseptler §6. Her varyant için yaz: yazı (ve hangi "iş"i yaptığı), sahne/an, ifade +
filiz durumu, ışık nesnesi + renk, mavi ipucu, kullanılan tetikleyiciler, başlık eşleşmesi. Varyantlar A/B
mantığıyla **tek bir büyük eksende** farklı olsun (`references/04-qa-and-ab.md`).

**3. Üret (varsayılan: SVG).** İstek JSON'unu yaz (preset: `bedClock` / `doorLight` / `phoneBed`; uygun sahne
yoksa `generator/thumb.js` `PRESETS`'e yeni preset ekle), sonra:
```powershell
python "$env:USERPROFILE\.claude\skills\other-self-thumbnail\generator\render.py" <istek.json> --out=<film klasörü>\thumbs --debug
```
Ayrıntı: `references/03-generator-and-higgsfield.md` §1.

**4. Final: Higgsfield ile 3B hacimli bitiş (test edildi, çalışıyor).** Rakibin thumbnail'ları 3B gibi görünür;
düz SVG yetmez. Yazısız render → yükle → `nano_banana_pro` img2img, varyant başına 2 aday (≈2 kredi/aday) →
karakter sapmışsa reddet → yazıyı kendi aracımızla `baseImage` üzerine bas. Kullanıcı Higgsfield'ın thumbnail
için kullanımını onayladı (2026-10-14); her seferinde harcanan krediyi raporla, film başına ~12 krediyi aşacaksan
önce sor. Adımlar, upload başlıkları ve test edilmiş prompt: `references/03-generator-and-higgsfield.md` §2.
SVG sürümü taslak ve kompozisyon kararları için kullanılır.

**5. QA — görsellere bak.** Her `*.png`, `*_320.png`, `*_debug.png` ve `contact_320.png`'yi Read ile aç;
`references/04-qa-and-ab.md` listesini uygula; düzelt ve yeniden üret. Neyin doğrulandığını dürüstçe raporla.

**6. Teslim.** 3 varyant PNG (+_320), her biri için gerekçe (hangi tetikleyiciler, neden), başlık eşleşmesi,
Test & Compare planı ve kayıt şablonu.

## Dosya haritası

| Dosya | Ne zaman |
|---|---|
| `references/01-thumbnail-brain.md` | her zaman — formül, kurallar, metin işleri, tetikleyiciler, marka kuralları, 8 hazır konsept |
| `references/02-measured-spec.md` | kompozisyon ve yeni preset yazarken — ölçülmüş sayılar |
| `references/03-generator-and-higgsfield.md` | üretim: SVG aracı, istek formatı, Higgsfield adımları, prompt |
| `references/04-qa-and-ab.md` | teslimden önce QA + A/B planı |
| `references/05-style-dna.md` | **her Higgsfield üretiminde** — rakibin 11 thumbnail'ından çıkarılan çizim stili + hazır stil bloğu |
| `generator/` | çalışan üretici (thumb.html, thumb.js, hero-rig.js, render.py, examples.json) |
| `reference-thumbs/` | rakibin 3 viral thumbnail'ı — **sadece analiz için**, asla referans görsel olarak AI'a verilmez |
| `deep-research/` | 3 ajanın tam raporları (ölçüm tabloları, psikoloji kaynakları, üretim sistemi) |

## Linux VPS (ubuntu@51.222.36.151, ~/the-other-self)

Aynı sistem VPS'te de kurulu: stüdyo `~/the-other-self/studio` (Windows'taki `C:\dev\the-other-self`), proje dosyaları `~/the-other-self/project`. Windows'a özel `npx.cmd`/`.ps1` yerine `npx` ve `studio/scripts/*.sh` (`render-youtube.sh <slug>`, `stills.sh`, `audio.sh <slug>`) kullanılır. Ayrıntılar: `~/the-other-self/CLAUDE.md`.

