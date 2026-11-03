# 07 — Ürün stili (Mod F): maskotlu, yüzsüz finans anlatım videosu

Tutorial'ın öğrettiği ve 21:52–22:51'de gösterdiği bitmiş video stili + rakip kanalların (yüzsüz finans animasyonu) türü.
Kaynak: `deep-research/07` Part B (piksel ölçümleri, CapCut ayarları), `08` §3 (maskot brifi, Remotion reçetesi).

> **[ETİK] Zorunlu:** referans videodaki ve rakip kanallardaki karakter tanınmış bir ABD prime-time çizgi film babasına çok benziyor.
> Biz **her zaman özgün bir maskot** kullanırız; prompt'lara asla bir kanal adı, TV karakteri ya da gerçek kişi yazmayız;
> "beyaza yakın ten + kısa gri saç + düz mavi tişört" kombinasyonunu da kullanmayız.

## 1. Ölçülen stil (referansın bitmiş videosu)

| Özellik | Ölçüm |
|---|---|
| Kanvas | 1920×1080, 30 fps, H.264, Rec.709 SDR (6:44 ≈ 402 MB) |
| Arka plan | görselin içine gömülü düz kırık beyaz **#FAFAF7**; ayrı plaka yok |
| Vinyet | **eliptik, sadece köşeler**: köşe #595959 · %3 köşegen #797979 · %6 #A3A3A0 · %10 #D3D3D0 · ≥ %15 dokunulmamış; kenar ortaları beyaz kalır (CapCut ayar katmanı → Vignette + tüm zaman çizelgesinde "Renoir" filtre) |
| Çekim sayısı | 58,7 sn'de 8 çekim (ort. **7,3 sn**): önce 4 AI-animasyon klibi (biri tekrar), sonra 4 durağan görsel; tüm 6:43'te ~34–36 görsel, ort. ~11–12 sn (bazıları 28–32 sn — kötü) |
| Kesme yeri | her görsel değişimi **yan cümle/cümle başında**; asla kelime ortasında değil |
| Görsel başına metin | 1–2 cümle (15–30 kelime) |
| Hareket | ilk ~22 sn: AI görsel→video klipleri (el hareketi, ağız, göz kırpma, beliren "?"/düşünce balonları); durağanlardan 4'te 1'i **%100→110 ölçek, merkez, pan yok, ~0,9–1,1 %/sn, tüm çekim boyunca**; diğerleri statik |
| Geçiş | AI klip↔klip sert kesme; durağanlara 0,5–0,7 sn CapCut "In" animasyonu (siyah mürekkep/eğri silme, hareket bulanıklıklı siyah swoosh, yatay glitch smear); **dissolve yok, siyaha fade yok, geçiş SFX'i yok** |
| Anlatım | İngilizce AI TTS, ~165 wpm (duraklamasız ~183), cümle arası 0,3–0,6 sn, müzik **yok**, SFX **yok** |
| Altyazı | aşağıda §3 |
| Kompozisyon | maskot merkezde veya sol-merkezde; **≥ %40 boş beyaz alan**; alt %15'te önemli içerik yok (altyazı bölgesi) |
| Props | aynı kontur kalınlığında düz ikon objeler: altın para, yeşil $ rozet, telefon, araba, bina, kahve, pembe kumbara, kırmızı/yeşil oklu grafik; görsel başına ≤ 3 adet 1–2 kelimelik etiket ("TRAP", "SALARY") |
| Renk mantığı | yeşil = kazanç, kırmızı = kayıp |

Rakip (Nick Invests türü) farkları: görsel her **~3–9 sn**'de değişir ve tekrar kullanılır; altyazı tek satır, Impact benzeri **beyaz + siyah kontur + gölge**, ~8–11 kelime, alt-orta ~%88.

## 2. HEDEF kurallar (bizim üretim)

1. **Kanvas:** 1920×1080, 30 fps, H.264 CRF 18–20, AAC 320k; SRT'yi altyazı izi olarak da yükle.
2. **Görsel kadansı:** kavram başına 1 görsel; **ilk dakika 3–7 sn**, genel ortalama **5–8 sn**; min 2,5 sn; **maks 12 sn** (referansın 28–32 sn'lik tutuşları hatalı).
   10 dk için 85–120 görsel; tekrar kullanım ≤ %15 (sadece aynı kavrama dönülünce).
3. **Hareketi öne yükle:** ilk 20–30 sn'yi 3–5 AI görsel→video klibiyle (4–6 sn, dudak senkronu yok) kur; sonra dakikada ≤ 1 vurgu klibi.
4. **Durağan hareketi:** [KOPYA] 3–4 görselden birine %100→110 merkez itme (lineer, tüm çekim). [İYİLEŞTİRME] Remotion'da her durağana %4–8 itme/çekme, yön değiştirerek, ±%1 pan — hiçbir durağan > 4 sn tamamen sabit kalmasın.
5. **Geçişler:** varsayılan sert kesme; bölüm değişiminde 6–8 karelik crossfade veya tek tip stilize "In" (mürekkep silme); dakikada ≤ 2 stilize geçiş; SFX yok.
6. **Arka plan:** sıcak kırık beyaz **#FAF8F3–#FAFAF7**, görsele gömülü.
7. **Vinyet:** referans hedefleri (köşe #595959 → %15 köşegende sıfır) **veya** marka varyantı: %65 yarıçapa kadar şeffaf, köşelerde %35–45 siyah.
8. **Ses:** sakin anlatıcı ~155–165 wpm; > 0,6 sn boşlukları 0,30–0,40 sn'ye indir; **−16 LUFS**, true peak ≤ −1,5 dBTP; müzik istenirse ≥ 20 dB altta (−30…−28 dB) side-chain ducking; kesmelerde SFX yok.
9. **Sayıları düzelt:** otomatik altyazıdaki rakam hatalarını mutlaka düzelt (referans "$1.100"ü "11 dollar" bıraktı).
10. **Kapanış:** [İYİLEŞTİRME] tam cümlede bitir, ≥ 0,5 sn tut, 5–20 sn end screen plakası.

## 3. Altyazı spesifikasyonu
**[KOPYA] Referans görünümü:**
| Özellik | Değer |
|---|---|
| Kaynak | otomatik altyazı (kelime zaman damgası) |
| Yazım | **tümü küçük harf, noktalama yok** |
| Font | yuvarlak geometrik sans, semibold (Poppins/Montserrat benzeri), **beyaz #F9F9F7, kontur yok** |
| Boyut | satır kutusu **%6,3–6,7 H**; ascender ~%4,2 H |
| Zemin | her satırın arkasında **yırtık kenarlı siyah fırça kutusu** #1E1E1E–#222, %85–90 opak, ~10 px dikey dolgu |
| Konum | yatay ortalı; blok merkezi **%86,7 H** (1 satır %83,5–90; 2 satır %79,7–93,5) |
| Genişlik | ~%66 W'de sarar (~8 kelime) → 1–2 satır |
| Kelime/altyazı | 5–12 (ort. ~7,4) → her ~2,7 sn'de yeni altyazı |
| Animasyon | **kelime kelime karaoke**: ifadenin yeri ortalı ayrılır; yeni kelime ~%40 opak, bulanık, taban çizgisinin **~%1,9 H altında** belirir, 0,2–0,3 sn'de yükselip beyazlaşır; altyazı bir sonrakinden 0,1–0,4 sn önce temizlenir |

**Marka varyantı (opsiyonel, Remotion):** 3–6 kelimelik parçalar, maks 2 satır, metin bandı tabanı %88 H; yuvarlak bold sans (Nunito/Poppins Black, lisanslı);
dolgu #FFFFFF + 10 px #1A1A1A kontur; aktif kelime maskotun vurgu renginde.

## 4. Özgün maskot brifi (şablon + örnek)

**Şablon (her kanal için doldur):**
- **Ad / rol:** izleyicinin yerine geçen, anlatılan hataları yapan sıradan biri (izleyici onunla güler, ona değil).
- **Silüet testi:** 64 px siyah silüet olarak tanınmalı; tek bir imza özelliği (saç tutamı, şapka, atkı, gözlük şekli).
- **Oranlar:** büyük baş (görünen gövdenin ~%35–40'ı), 3–4 baş boyu, ekranda çoğunlukla büst/bel üstü.
- **Yüz:** oyunculuğu kaşlar yapar; basit göz/burun; ağız çizgi veya açık "D"; **çift çene / sakal yok** (tanınmış karakter benzerliğinden kaçın).
- **Kıyafet:** sabit; rakiplerin rengini (mavi tişört/hoodie) kullanma.
- **İmza obje:** logo, thumbnail ve end screen'de tekrar eden küçük bir nesne.
- **Çizim:** düz renkler + tek cel-shade tonu, gradyan/doku yok; tek tip kalın siyah kontur (~%1 H, 1080p'de 6–12 px).
- **Palet:** çizgi + kâğıt + 2 kimlik rengi + kazanç yeşili + kayıp kırmızısı + nötr gri + 2 ten tonu.
- **Yan kadro:** tekrar eden bir gag karakteri (ör. gizli masrafları temsil eden küçük yaratık) — format imzası.

**Örnek ("Penn", deep-research/08'den):** yumurta biçimli baş (altı geniş), yükselen-grafik oku şeklinde tek **cowlick**, yuvarlak kaplumbağa gözlük;
**hardal hırka #E0A526** + beyaz tişört + **lacivert chino #23395B** + beyaz ayakkabı; imza obje nane yeşili "defter" (coin ikonlu);
palet: çizgi #1A1A1A · kâğıt #FAF8F3 · kazanç #2FB37A · kayıp #E4572E · gri #BFC4CC; yan karakter "the Leak" (sızıntı damlası şeklinde sırıtan yaratık).

**Tutarlılık stratejisi:**
1. **Kanon sayfası önce:** turnaround (ön, ¾, yan, arka) + 12 ifade + 16 poz; 4–6 kanon PNG dondur.
2. **Referans-kilitli üretim:** her görsel çağrısında 2–3 kanon referans + sabit `STYLE_BLOCK` + sabit `MASCOT_BLOCK` (Higgsfield referans elemanları / nano-banana çoklu referans / Flux Kontext). Sahne başına serbest karakter tarifi **yazma**.
3. **Kompozit:** maskot pozlarını düz/şeffaf zeminde, sahne/props'u ayrı üret → Remotion'da birleştir (üretim sayısı %40–60 düşer, karakter kayması neredeyse sıfır).
4. **Otomatik QA:** maskot kırpımı ile kanon arasında embedding benzerliği (eşik 20 onaylı örnekle kalibre) + kıyafet renk kontrolü; en fazla 2 yeniden üretim, sonra insan.
5. **Opsiyonel LoRA:** 30–40 onaylı görselden sonra.
6. **Benzerlik denetimi:** yayından önce tanınmış karakterlere benzerlik için görsel kontrol.

Referansın kendi hilesi (Whisk "Subject" yuvası) aynı fikirdir: ilk iyi görseli referans olarak kilitle; Whisk kapandığı için eşdeğerini kullan.

## 5. Görsel prompt yapısı
```
<STYLE_BLOCK>  simple 2D cartoon explainer illustration, flat vector, minimal shading, bold uniform black outlines,
               clean warm off-white background (#FAF8F3), generous empty space, nothing important in the bottom 15%
<MASCOT_BLOCK> <kanon maskot tarifi — her prompt'ta birebir aynı> + [2–3 kanon referans görseli ekli]
<SCENE>        <pose>, <expression>, <1–3 props>, <≤ 3 one-or-two-word labels>, <green=gain / red=loss accents>
```
Sahne yoğunluğu: senaryodaki her `||` vuruş işareti = 1 sahne (≈ 12–18 kelimede bir).

## 6. Remotion reçetesi (CapCut adımlarının yerine)
- `scenes.json` (her sahne: id, start, end, text, concept, visual_type still|i2v|chart|text_card|reuse, mascot pose/expression, props, motion {push_in 1.00→1.06, pan}, transition_in, image_prompt, video_prompt) + `words.json`.
- `<Img>` / `<OffthreadVideo>` sahne başına; Ken Burns 1,00→1,05–1,08 easing, yön değiştirerek, ±%1 pan.
- Varsayılan sert kesme; bölüm değişiminde 6–8 kare crossfade; dakikada ≤ 2 stilize geçiş.
- Vinyet overlay'i (radyal gradyan) tüm kompozisyonun üstünde.
- Altyazı bileşeni `words.json`'dan (§3).
- Grafikler AI ile çizilmez: gerçek veriyle **programatik** bar/çizgi grafik + kaynak etiketi.
- Render sonrası: `python scripts/edit_rhythm_qa.py render/final.mp4 --profile animated`.

## 7. Ürün videosu paketleme (finans anlatım kanalı)
- **Başlık:** ≤ 60 karakter, tek merak kalıbı: "Why everything changes after $X" · "The X trap that keeps people poor" · "The hidden cost of X" ·
  "Why most people stay broke" · "What happens when you reach $X" · "The financial mistake almost everyone makes".
  Kalıpları rakip outlier başlıklarından **değişkenli şablon** olarak çıkar; başlığı asla birebir alma.
- **Konu seçimi:** tek kategoride 5–10'luk seri ("financial traps"); son 12 ayda ≤ 5 uzun video olan anahtar kelime.
- **Thumbnail:** 1 maskot (sol, ~%40–45 W, endişeli/şaşkın) + 1 fikir objesi veya 3–5 ikonluk oklu zincir (sağ) + üstte **2–4 kelime** ultra-bold siyah büyük harf (≥ %50 W) + beyaz zemin.
  Yazıyı görsel modele değil **programatik** koy (Sharp/Satori). 3 varyant + 5 başlık → YouTube Test & Compare. 168×94'te okunurluk.
- **SEO:** açıklamanın ilk 2 satırı vaadi tekrarlar; sahne/bölüm zamanlarından bölümler; 10–20 odaklı etiket (≤ 500 karakter); 3–5 hashtag; "not financial advice" satırı.
- **Uzunluk:** 8–12 dk başlangıç; seri oturdukça 12–25 dk (uzun = daha çok reklam yeri; ama tutma önce gelir).
