---
name: aiflow-video-dna
description: 144K izlenen AI Flow tutorial'ının ("How To Make Videos Like Nick Invests With AI", 22:52, kanal medyanının 10,3 katı) 8 paralel analist ajanıyla kare kare tersine mühendisliğinden çıkarılmış VİDEO ÜRETİM + EDIT + PAKETLEME sistemi. İki çıktı modu var: (T) "How to make videos like {X} with AI" tarzı ekran kaydı tutorial'ı — iki hızlı edit (yoğun kanıt girişi + 1:1 çıplak ekran kaydı), adım döngüsü, zoom/vurgu/sting kuralları, EDL; (F) bu tutorial'ın öğrettiği yüzsüz maskotlu finans/anlatım videosu — görsel kadansı, Ken Burns, vinyet, kelime kelime altyazı, özgün maskot, Remotion reçetesi. Ayrıca başlık/thumbnail/açıklama şablonları, edit-ritmi QA script'i ve herhangi bir YouTube videosunu aynı yöntemle analiz eden kanıt paketi script'i içerir. Kullanıcı "AI Flow tarzı", "Nick Invests gibi", "videos like X tutorial'ı", "tutorial videosu kurgula/editle", "edit stilini uygula", "kaç saniyede bir kesme/zoom", "EDL çıkar", "edit QA / ritim kontrolü", "faceless finans videosu", "maskotlu anlatım videosu", "FULL COURSE thumbnail", "bu videoyu tersine mühendislik yap / kare kare analiz et / edit mantığını çıkar", "hook/CTR/başlık neden başarılı" dediğinde MUTLAKA bu skill'i kullan — skill adı geçmese bile.
---

# AI Flow Video DNA — tutorial + yüzsüz anlatım videosu üretim sistemi

Bu skill dört rol oynar: **Mimar** (senaryo iskeleti + adım döngüsü), **Editör** (EDL + tempo + overlay spec'i),
**Paketleyici** (başlık, thumbnail, açıklama), **Denetçi** (QA script'i + kontrol listesi). Ayrıca **Adli Analist** modu
yeni bir referans videoyu aynı 8-analist yöntemiyle çözer.

Referansın kelimeleri, prompt metinleri, karakteri ve görüntüleri **kopyalanmaz**; *yapı, ritim, ölçüler ve karar mantığı* kopyalanır.

## Tek cümlelik DNA
> İzleyicinin zaten aradığı bir **başarılı kanalın adını** başlığa koy, ilk 3 dakikayı **rakamlı kanıt + para aritmetiği** ile
> yoğun kurgula (her 1,5–2 sn'de değişim, söylenen her sayıya 1,55× zoom), sonra **çıplak 1:1 ekran kaydında** tek bir koşan örneği
> 9 adımlık **kopyalanabilir reçeteyle** bitmiş ürüne kadar taşı (her adım aynı 12 vuruşlu döngü, her sonuçta müzik vuruşu,
> her beklemede CTA), **bitmiş videoyu en sona** koy ve konuşmadan bitir.

## Neden kazandı (kısa) — ayrıntı `references/01-why-it-won.md`
1. **Dağıtım:** 4 kanallı YouTube Collaboration (collab medyanı 47K vs solo 8K).
2. **Kanıtlanmış para konusu + seri:** finans serisinin 3. hiti; aynı thumbnail etiketi.
3. **İsimli-varlık başlığı:** zirvedeki "Nick Invests" → arama + önerilen komşuluğu.
4. **Para vaadi:** "High RPM", para yığını, 1. dakikada RPM hesabı.
5. **Video = kılavuz:** her ~53 sn'de kopyalanabilir öğe; tekrar izleme zirveleri hep prompt/ayar/sonuç ekranında (zirve 1,00 = bitmiş senaryo → ücretsiz TTS ayarları; 0,85 = görsel→konuşan klip).
6. **Engelleri sırayla kaldırma:** fikir, İngilizce, beceri, bütçe, başarısızlık korkusu.
7. **Edit başarının nedeni değil:** görsel değişim yoğunluğu tekrar izlemeyle zayıf negatif ilişkili; edit iki hızlı ve işini yapıyor.

## Modlar

| Mod | Tetik | Çıktı |
|---|---|---|
| **T-PLAN** | "X gibi video nasıl yapılır tutorial'ı planla", "tutorial senaryosu" | konu/kanıt kanalı seçimi → paket → zaman kodlu senaryo iskeleti + koşan örnek + prompt listesi |
| **T-EDIT** | "bu kaydı AI Flow tarzında kurgula", "EDL çıkar", "edit talimatı" | Edit Karar Listesi (EDL) + overlay/zoom/sting zamanları + export ayarları |
| **F-PRODUCE** | "faceless finans videosu", "maskotlu anlatım videosu yap" | senaryo (`||` işaretli) → `scenes.json` → görsel prompt'ları → Remotion montaj planı → altyazı + paket |
| **PACKAGE** | "başlık / thumbnail / açıklama / etiket" | 5–10 başlık (şablon etiketli), thumbnail katman spec'i + QA, açıklama + etiket + sabit yorum |
| **QA** | "edit ritmini kontrol et", "render'ı denetle" | `edit_rhythm_qa.py` çıktısı + `09-qa-checklist.md` PASS/FAIL + düzeltme listesi |
| **ANALYZE** | "bu videoyu tersine mühendislik yap", "kare kare analiz et", "edit mantığını çıkar" | kanıt paketi + 8 paralel analist + birleştirilmiş DNA (yeni skill veya bu skill'e ek) |

## T-PLAN iş akışı (adımları atlama)
1. **Konu ve kanıt kanalı.** `{SUCCESS_CHANNEL}` filtresi: ≤ 200 video, ≥ 50K abone, son 6 ayda ≥ 500K'lık video. Kaynak: `competitor-radar` skill'i veya kullanıcı. Kendi yorumlarında istenen kanallar öncelikli. 2. ve 3. kanıt kanalı da seç.
2. **Paket ÖNCE** (`references/02-packaging.md`): iskelet başlık + 4 alternatif; thumbnail katman spec'i (özgün maskotla 4 örnek kart, doğru kanıt sayısı).
3. **Hook** (`references/03-hook-intro.md`): soru ≤ 0:02 → cevap ≤ 0:08 → kanıt yığını → para aritmetiği → itiraz kontrolü → vaat ~2:30 → teaser → abone misyonu.
4. **İskelet** (`references/04-script-engine.md` §2): 17 bölümlük tablo, yüzdeleri hedef süreye ölçekle; ilk adım ≤ %14'te; "vay" anı %55–70'te; fırsat hatırlatması %80–87'de; final %95+.
5. **Koşan örnek:** tek konu, 5/5 adımda taşınır, finalde oynar. Önce o örnek ürünü (Mod F) gerçekten üret — teaser ve final ondan gelir.
6. **Her adımı 12 vuruşlu döngüyle yaz** (T→N→E→P→C→Z→K→(W)→R→X→V→T′), kotaları doldur (güvence ≥ 18, açık döngü ≥ 8, mizah ≥ 5, abone ≤ 4).
7. **Prompt paketi:** adım başına 1 prompt (≥ 7) — kendi yazdığımız; link yüklemede canlı.
8. **Çıktı:** `tutorials/<slug>/01-package.md`, `02-script.md` (zaman kodlu, `[SCREEN: …]` notlu), `03-prompt-pack.md`, `04-edl.md`.

## T-EDIT iş akışı
1. Ham kaydı + anlatımı al; anlatımı kelime zamanlı transkribe et (`scripts/evidence_pack.py <video> <dir> --whisper medium` veya ElevenLabs alignment).
2. **Ses önce:** nefes ve > 0,5 sn boşlukları kes (ön-reveal boşlukları hariç), −14…−16 LUFS, LRA ≤ 4.
3. **Giriş (0:00–~3:00) — kanıt fragmanı** (`05-edit-grammar-tutorial.md` §4, §6.1; `06-edit-tempo-spec.md` §3–4): ilk 10 sn'de 5–7 değişim / ≥ 3 kaynak türü; söylenen her sayıya 1,55× punch-in (0,3–0,7 sn S-eğrisi, 3–4 sn tut); her 15–30 sn'de ek; kanıt sonunda abone animasyonu + hedef kartı.
4. **Gövde — çıplak 1:1:** isme kes (+0,9 sn), ekran dışı işi görünmez kesmelerle at, AI beklemesini ≤ 1 sn'ye kırp veya 4–10× hızlandır, tekrarlı işi montajla (1,2–1,5 sn/çekim), native seçim + kırmızı tıklama halkası, sabit vinyet + letterbox, tek parametre zoomu; kopyalanacak metin < %2 H ise 1,5–1,7× punch-in.
5. **Ses olayları:** her sonuç açılışında sting (+6…+10 dB); montaj/hızlandırma boşluğunda müziği aç; kesmelerde SFX yok.
6. **CTA yerleşimi:** sadece bekleme anlarında; abone kartı (3,4 sn, karartma %20), hedef kartı (neon yeşil, 4 sn), en fazla 2 kart.
7. **Sonuçlar:** her üretim adımından sonra 4–8 sn demo; "vay" anı tam ekran kendi sesiyle; editten sonra 6–10 sn bitmiş önizleme.
8. **Kapanış:** CTA bloğu (≤ 40 sn) → sert kesme → bitmiş video (45–75 sn) → tam cümlede bitir + end screen.
9. **EDL yaz** (`05` §11 şablonu), sonra **QA:** `python scripts/edit_rhythm_qa.py final.mp4 --profile tutorial` → FAIL'leri düzelt.
10. **Gizlilik taraması** (`05` §8) ve `09-qa-checklist.md`.

## F-PRODUCE iş akışı
`references/07-finance-explainer-style.md` + `08-production-pipeline.md` §2–3:
1. Kanal kitabı yoksa oluştur (persona, palet, STYLE_BLOCK, **özgün** MASCOT_BLOCK, kanon sayfası).
2. Konu: rakip outlier başlıklarından değişkenli kalıp → seri kategorisi → aramada az uzun video.
3. Senaryo şablonu (`08` §3): dakika × 155 kelime, `||` vuruşlar, `[SRC?]` → doğrula.
4. Ses: ElevenLabs timestamps, ≤ 2.500 karakter parça, boşluk kontrolü, −16 LUFS.
5. `scenes.json`: kavram başına sahne, ilk dakika 3–7 sn, ortalama 5–8 sn, maks 12 sn; ilk 20–30 sn görsel→video.
6. Görseller: Higgsfield (nano_banana_pro/flux) + 2–3 kanon referans; benzerlik QA.
7. Remotion: Ken Burns %4–8, vinyet, kelime kelime altyazı, programatik grafikler.
8. QA: `edit_rhythm_qa.py --profile animated` + kontrol listesi C/D/E/F.
9. Paket: ≤ 60 karakter merak başlığı, maskot + obje thumbnail'i (yazı programatik), SEO + "not financial advice".

## ANALYZE iş akışı (başka bir videoyu çöz)
`references/10-reverse-engineering-method.md`:
1. `python scripts/evidence_pack.py "<url>" <yeni_boş_klasör> --whisper medium --lang <dil> --device cuda` (yazılar 429 verirse yerel Whisper zaten devrede).
2. Paylaşılan BRIEF + 8 analist (paketleme · hook · senaryo · nicel edit · 3 kare tarayıcı · öğretilen sistem/ürün stili) **paralel**.
3. Birleştir: ölçüm > kare kanıtı > yorum; her kuralı [KOPYA]/[İYİLEŞTİRME]/[ETİK] etiketle; çelişkileri kendin ölç ve çöz.

## Değişmez DNA (her videoda) — ihlal edilemez
1. **Paket önce:** başlık + thumbnail yazılmadan senaryo yazılmaz; başlık vaadi = videonun ödemek zorunda olduğu sözleşme.
2. **Kanıt önce, yöntem sonra:** ilk %12–14 kanıt + para aritmetiği + vaat; ilk eyleme geçilebilir adım ≤ %14.
3. **Kopyalanabilir eser:** her ≤ 60 sn öğretimde bir prompt/ayar/hile; eser ekranda okunur ≥ 3 sn.
4. **Tek koşan örnek** baştan finale; **bitmiş ürün en sonda**, ondan sonra konuşma yok.
5. **İki hızlı edit:** yoğun giriş, 1:1 gövde; gövdede süs yok, vurgu fareyle.
6. **Sonuç anı işaretlenir:** sting + "şimdi bak" + sonuç ≥ 3 sn.
7. **Bekleme asla ölü değil:** kırp / hızlandır / CTA; hiçbir bekleme ekranı > 8 sn.
8. **Ses metronomdur:** ≥ %90 konuşma kaplaması, nefes ve uzun boşluk yok.
9. **Ölç:** her render `edit_rhythm_qa.py`'den geçer.
10. **[ETİK] Özgünlük ve dürüstlük:** özgün maskot (tanınmış karakter benzeri yok), prompt'larda kanal/karakter/gerçek kişi adı yok,
    rakip klibi/sesi yok (kanal sayfası kaydı kanıt için serbest), lisanslı/özgün meme (silah yok), thumbnail'de sadece doğru sayılar,
    kaynak paketi linki yüklemede canlı, garanti gelir iddiası yok, finans videolarında "not financial advice", gizlilik blur kontrolü,
    format çeşitliliği (inauthentic-content riski).

## Esnek DNA (konuya göre)
Collab partnerleri · otomatik dublaj · ses dili (Türkçe tutorial + İngilizce ürün videosu referanstaki gibi) · bölüm sayısı (9–12) ·
meme yoğunluğu · müzik yatağı (yok ya da −30…−35 dB) · altyazı görünümü (referans fırça kutusu veya marka varyantı) · süre (Mod T 18–28 dk; Mod F 8–25 dk).

## Referanslar
- `references/01-why-it-won.md` — rakamlar, heatmap okuması, sıralı başarı faktörleri, kopyalanmaya değmeyen zayıflıklar.
- `references/02-packaging.md` — başlık iskeleti + 25 şablon, thumbnail "house template" katman spec'i + QA, açıklama/etiket/sabit yorum şablonu, dağıtım.
- `references/03-hook-intro.md` — ilk 3 dakika saniye saniye, hook anatomisi, şablon ve örnek hook'lar.
- `references/04-script-engine.md` — makro iskelet, 12 vuruşlu adım döngüsü, tutma cihazı kotaları, anlatım spec'i, özgün satır bankası (EN + TR).
- `references/05-edit-grammar-tutorial.md` — Mod T görsel gramer: çekim türleri, kesme, zoom, vurgu, overlay spec'leri, ses, gizlilik, EDL şablonu.
- `references/06-edit-tempo-spec.md` — tüm sayılar: referans ölçümleri, hedef tempo tablosu, zoom spec'i, QA eşikleri.
- `references/07-finance-explainer-style.md` — Mod F ürün stili: ölçülen stil, hedef kurallar, altyazı, özgün maskot brifi, prompt yapısı, Remotion.
- `references/08-production-pipeline.md` — öğretilen araç hattı, otomasyon hattımız, senaryo prompt'u, ekonomi, riskler.
- `references/09-qa-checklist.md` — yayın öncesi kontrol listesi.
- `references/10-reverse-engineering-method.md` — kanıt paketi, 8 analist ayrımı, birleştirme kuralları, çözülmüş çelişkiler.
- `deep-research/` — 8 ham analist raporu (İngilizce; kare zaman damgaları, piksel ölçümleri, tablolar).

## Script'ler
- `scripts/evidence_pack.py` — URL veya yerel video → kareler, tüm karelerin scdet skoru, sessizlik, loudness, heatmap, yorumlar, transkript (+çeviri), metrics.json.
  Gereken: ffmpeg/ffprobe, yt-dlp, (ops.) faster-whisper; GPU için aynı venv'de `nvidia-cublas-cu12` + `nvidia-cudnn-cu12` 9.x.
- `scripts/edit_rhythm_qa.py` — render'ın edit ritmini ölçer (değişim/dk, çekim/dk, medyan çekim, statik tutuşlar, zoom'lar, sting'ler, LUFS) ve `tutorial`/`animated` profiline göre PASS/FAIL verir. Gereken: ffmpeg, numpy, Pillow.

## İlgili skill'ler
`competitor-radar` (kanıt kanalı + konu fikri) · `inner-voice-film` (Remotion altyapısı örnekleri) · `lbb-content-dna` (anlatım senaryosu disiplini) · `watch` (hızlı video izleme).
