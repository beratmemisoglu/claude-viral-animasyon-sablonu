# Kare Kare Motion Design Rekonstrüksiyonu

Seçilen segmentler (videonun en yoğun ve en çok yeniden kullanılabilir üç bölümü):
- **SEG-A · 0:00,0–0:24,3** — Soğuk açılış (S1) + ilk geçiş
- **SEG-B · 0:23,6–0:53,0** — Halka deneyi (S2)
- **SEG-C · 1:40,7–2:09,4** — Havadan bakış ve zaman-uzay diyagramı (S5)
- Ek: **2:23,5–2:25,5 reframe** (S6 içindeki tek belirgin kompozisyon hareketi)

Ölçüm: SEG-A/B 1 fps + 2 fps şerit, sınırlar 10 fps; SEG-C 1 fps + 2 fps; reframe 10 fps.
Konumlar kare genişliği/yüksekliğinin yüzdesi (x→sağ, y→aşağı), **tümü yaklaşık**. [G] gözlem · [Ç] çıkarım · [B] belirsiz.

---

## SEG-A · Soğuk açılış (0:00,0–0:24,3)

### 1. Zaman çizelgesi

| # | Başla | Bitir | Süre | Öğe | Başlangıç durumu | Son durum | Hareket | Ölçek/Rot | Opaklık | Tür | Eşzamanlı | Anlatım |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | 0:00,0 | 0:24 | 24 sn | Arka plan dokusu | Görünür | Görünür | Yok/çok yavaş [B] | — | 1 | Statik | Tümü | — |
| A2 | 0:00,0 | 0:24 | 24 sn | S-eğrili otoyol | Görünür (ilk karede tam) | Aynı | Yok | — | 1 | Statik | — | "You're on the motorway" |
| A3 | 0:00,0 | 0:24 | sürekli | ~100 araç | Akışta | Akışta | Sağa-yukarı (yol yönünde), sim hızı | — | 1 | Hareket | A4 ile | — |
| A4 | 0:00,0 | 0:23 | 23 sn | Kırmızı glow kümesi (üst taşıt yolu) | Merkez x≈%80 (x %65–100) | Merkez x≈%45 (x %30–60) | **Sola-aşağı, yol ekseni boyunca geriye** (~1,5 %W/sn) | Küme uzar | Glow yoğunluğu sim'e bağlı | Dönüşüm (veri) | A3'e ters yön | "everything stops… you crawl" |
| A5 | 0:03 | 0:23 | 20 sn | "YOU" kehribar araç + etiket | Kümenin önünde x≈%62, y≈%30 | Kümenin içinde, kırmızıların arasında | Sağa çok yavaş (sıkışık) | — | 0→1 (~0,3 sn) [Ç] | Reveal (fade) | A4 | "You crawl for ten minutes" |
| A6 | 0:07 | 0:12 | 5 sn | İkon 1 (kaza, üstü çizili) | Yok | x≈%52, y≈%57, çap ≈%7H | Yok | — | 0→1 (~0,3 sn) | Reveal | — | "No crash" |
| A7 | 0:08 | 0:12 | 4 sn | İkon 2 (yol çalışması konisi) | Yok | x≈%57 | Yok | — | 0→1 | Reveal (stagger +1 sn) | A6 | "no roadworks" |
| A8 | 0:09 | 0:12 | 3 sn | İkon 3 (kamyon) | Yok | x≈%62 | Yok | — | 0→1 | Reveal (stagger +1 sn) | A6–A7 | "no broken down lorry" |
| A9 | 0:12 | 0:12,5 | 0,5 sn | İkon 1–3 | Görünür | Yok | Yok | — | 1→0 birlikte | Remove | — | "So what stopped you?" |
| A10 | 0:08 | 0:23 | 15 sn | Alt taşıt yolu tekil kırmızılar | Sol uçta | Sol uçta yeniden | Araçlarla | — | Yanıp sönen | Sim | — | (arka plan hikâyesi) |
| A11 | ~0:15 | 0:23 | 8 sn | Kırmızı yuvarlatılmış kontur | Yok | Kümeyi çevreler (~%30W × %10H, yol açısına hizalı) | **Kümeyle birlikte sola kayar** | Döndürülmüş (yol açısı ~−12°) | 0→1 | Reveal + takip | A4 | "the jam you sat in" |
| A12 | ~0:17 | 0:18 | ~1 sn | Kehribar halka (YOU) | Çap ~%4H | Çap ~%6H | Araçla | Büyür | 1 | Vurgu | A11 | "was never in one place" |
| A13 | 0:18 | 0:23 | 5 sn | Kırmızı ok "geriye" | Yok | x %5–20, y≈%45, sola bakan | Kümenin altında sola kayar | — | 0→1 | Reveal | A11 | "travelling… backwards" |
| A14 | 0:21 | 0:22 | ~1 sn | Büyük kehribar pulse halkası | Çap ~%5H | Çap ~%15H | Araç merkezli | Genişler | 1→0 | Pulse | — | "long before you arrived" |
| A15 | 0:23,6 | 0:23,7 | 0,1 sn | Tüm sahne | Görünür | Lacivert #0B121E | — | — | 1→0 (lacivert üzerine) | Dip-out | — | "Once you know how it works…" |
| A16 | 0:23,7 | 0:24,3 | 0,6 sn | Halka + başlık (sonraki sahne) | Lacivert | Görünür | — | — | 0→1 | Dip-in | — | — |

### 2. Katman yığını (arkadan öne)
1. L1 — Bulut dokulu koyu yeşil zemin (statik)
2. L2 — Yol gövdesi (asfalt + kenar çizgileri + kesik şerit çizgileri) (statik)
3. L3 — Araç gövdeleri (sim)
4. L4 — Fren glow katmanı (additive/screen, blur) — araçların **üstünde**, çünkü kırmızı araç gövdesini de boyuyor [G]
5. L5 — Vurgu şekilleri: kırmızı kontur, kehribar halka, kırmızı ok
6. L6 — Durum ikonları (A6–A8)
7. L7 — Metin etiketi "YOU"
8. L8 — Geçiş katı (tam ekran lacivert, opaklık animasyonlu)

Sabit: L1, L2. Hareketli: L3, L4 (veri), L5 (takip eden), L8 (geçiş).

### 3. Hareket rekonstrüksiyonu (ana öğeler)
| Öğe | Başlangıç pos. | Bitiş pos. | Boyut | Yörünge | Hız profili | Kamera |
|---|---|---|---|---|---|---|
| Kırmızı küme (merkez) | (80, 28) | (45, 36) | uzunluk %35W → %30W | S-eğri path boyunca geriye | Sabite yakın (dalga hızı sabit) | Statik |
| YOU aracı | (62, 30) | (~64, 30) | araç ~%2,2W | Path boyunca ileri, çok yavaş | Dur-kalk | Statik |
| Kırmızı kontur | kümeyle | kümeyle | kümeyi +%10 sarar | Kümeyi takip | Doğrusal takip | Statik |
| Kırmızı ok | (20→5, 45) | — | ~%15W | Sola | Doğrusal | Statik |

### 4. Reveal türleri
- İkonlar: **opaklık fade**, 1 sn stagger, soldan sağa — anlatımdaki üç olumsuzlama ile birebir.
- Kontur ve ok: opaklık fade + ardından nesne takibi.
- Pulse halka: **ölçek + opaklık** (genişleyip sönme).
- Glow: veri güdümlü opaklık (fade değil, simülasyonun yavaşlama değeri).

---

## SEG-B · Halka deneyi (0:23,6–0:53,0)

### 1. Zaman çizelgesi

| # | Başla | Bitir | Süre | Öğe | Başlangıç | Son | Yön/hareket | Opaklık | Tür | Anlatım |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 | 0:23,7 | 0:24,0 | 0,3 | Halka pist | Lacivert üzerinde soluk | Tam | — | 0→1 | Dip-in | "In 2008, physicists in Japan" |
| B2 | 0:24,0 | 0:52,6 | sürekli | 22 araç | Eşit aralıklı | Kümelenmiş | **Saat yönünde** dönüş | 1 | Sim | — |
| B3 | 0:24,1 | 0:24,7 | 0,6 | "THE JAM WITH NO CAUSE" + kehribar alt çizgi | Yok | Sol üst (x %2–23, y %4–7) | — | 0→1 | Fade | "set out to make a jam from nothing" |
| B4 | ~0:29,5 | 0:30,5 | ~1 | H1 başlık | Görünür | Yok | — | 1→0 | Fade-out | — |
| B5 | 0:29 | 0:52,6 | 23,6 | "22 CARS" | Yok | Merkez (x %50, y %44), yükseklik ≈%7H | — | 0→1 | Fade | "twenty two cars" |
| B6 | 0:31 | 0:52,6 | — | "230 M ROUND" | Yok | Merkez y≈%52 | — | 0→1 | Fade | "230 metres round" |
| B7 | 0:35 | 0:52,6 | — | "ASKED TO HOLD 30 KM/H" | Yok | Merkez y≈%57 | — | 0→1 | Fade | "hold thirty kilometres an hour" |
| B8 | 0:38 | 0:44,5 | 6,5 | Beyaz yay ok + "ALL GOING ROUND" | Yok | Halka içi üst, ~100° yay (saat 10:30→1:30), ok başı sağda | Statik | 0→1, sonra metin 1→0 (0:44,5) | Fade | "For a while it worked" |
| B9 | 0:41 | 0:45,0 | 4 | "NO JAM YET" | Yok | Merkez y≈%63, beyaz | — | 0→1→0 | Fade in/out | "with nobody doing anything wrong" |
| B10 | 0:43 | 0:52,6 | 9,6 | Halka üzerinde kırmızı küme | Saat 11–12 civarı küçük | Saat 7–11 arası uzun | Küme **saat yönünün tersine** uzar/kayar | Veri | Sim | "a jam appeared" |
| B11 | 0:44 | 0:52,6 | 8,6 | Dış kırmızı yay | Saat ~11–12 kısa yay (~20°) | Saat ~7→12 (~150–200°) | Kuyruk ucu CCW ilerler | 0→1 | Veri güdümlü uzama | "A handful of cars came to a complete stop" |
| B12 | 0:50,5 | 0:52,6 | 2 | Yayın ucunda ok başı | Yok | Saat ~7 yönünde, aşağı-sola bakan | Yayla birlikte | 0→1 | Reveal | "began to move backwards round the circle" |
| B13 | 0:47,5 | 0:52,6 | 5 | Kırmızı sayaç "N STOPPED" | "6 STOPPED" | "11 STOPPED" | 6→7→8→9→10→11, ~1 sn'de bir **anlık** değişim | 1 | Veri | — |
| B14 | 0:52,6 | 0:53,0 | 0,4 | Tüm sahne → sonraki | — | Lacivert → tek şerit yol | — | — | Dip | "Here's what happened" |

**Örtüşen olaylar ayrıştırıldı:** B8 (beyaz yay ok) kalırken B9 metni söner (0:45,0) ve yerini 2,5 sn sonra B13 alır — arada ~2,5 sn durum satırı boş [G, 2 fps şeridi].

### 2. Katman yığını
1. L1 doku zemin
2. L2 halka yol gövdesi (dış ve iç kenar çizgisi + ince orta çizgi)
3. L3 araçlar (halka teğetine göre döndürülmüş)
4. L4 fren glow (additive)
5. L5 dış kırmızı yay + ok başı (halka dış kenarından ~%3H dışarıda)
6. L6 iç beyaz yay ok
7. L7 merkez metin bloğu (dikey yığın: H0 + 2×H3 + durum satırı)
8. L8 H1 başlık + alt çizgi
9. L9 geçiş katı

Sabit: L1, L2, L6 (gösterildiği sürece), L7 düzeni (yalnız içerik değişir). Hareketli: L3/L4 (sim), L5 (veri).

### 3. Hareket rekonstrüksiyonu
| Öğe | Değer |
|---|---|
| Halka merkezi | (50, 50) sabit |
| Halka dış çapı | ≈ %78H (≈ %44W) |
| Yol genişliği | ≈ %4,5H |
| Araç boyu | ≈ %3,5H, teğete hizalı |
| Araç açısal hızı (serbest) | ~1 tur / 10–12 sn [Ç, 1 fps'den tahmin] |
| Kırmızı yay yarıçapı | dış çap + ~%4H |
| Yay kalınlığı | ≈ %0,7H, yuvarlak uç |
| Merkez metin satır aralığı | ≈ %5H |

### 4. Reveal analizi
- Metinler sırayla, anlatımla birebir eklenir (B5→B6→B7): "aşamalı kimlik kartı" — merkez blok giderek uzar.
- Durum satırı bir **değişken yuvası**: önce nötr beyaz (NO JAM YET), sonra kırmızı sayaç. Aynı konumu yeniden kullanmak gözün yer değiştirmesini engeller.
- Kırmızı yay: **veri güdümlü ölçek/uzunluk** (trim). Dalganın yönünü (CCW) gösteren ok başı en sonda gelir → anlatımda "backwards" kelimesine saklanmış "punchline".

---

## SEG-C · Havadan bakış + zaman-uzay diyagramı (1:40,7–2:09,4)

### 1. Zaman çizelgesi
| # | Başla | Bitir | Öğe | Olay | Anlatım |
|---|---|---|---|---|---|
| C1 | 1:40,7 | 1:41,2 | Geçiş | Lacivert dip; yeni kompozisyon: dikey yol şeridi x≈%93 (genişlik ~%3W, tam yükseklik) | "You can watch this from the air" |
| C2 | 1:41,2 | 2:09 | Dikey yol | Araçlar yukarıdan aşağı (veya tersi) akar, kırmızı kümeler [G]; yön [B] | — |
| C3 | 1:42 | 1:46 | "SEEN FROM ABOVE" | Sağ üst, fade-in | "researchers in Ohio flew along a motorway" |
| C4 | 1:46 | 2:09 | Fotoğraf çerçevesi | Yol üzerinde yuvarlatılmış dikdörtgen (~%6W × %55H), ince beyaz | "photographing the same stretch" |
| C5 | 1:46 | 1:49 | "ONE PICTURE A SECOND" | C3'ün yerine (aynı konum) | "over and over" |
| C6 | 1:49 | 1:49,3 | Lacivert panel | Fade-in, x %2–80, y %8–96 | "traced every car" |
| C7 | 1:49 | 1:51,5 | Nokta matrisi | Sütunlar soldan sağa eklenir; her sütun = bir fotoğraf; durmuş araç noktaları kırmızı | "from one picture to the next" |
| C8 | 1:51,5 | 1:52 | Nokta→çizgi | Noktalar **tek adımda** sürekli çizgilere dönüşür (beyaz çapraz, kırmızı yatay) | "Each car becomes a line on a chart" |
| C9 | 1:49 | 2:09 | Eksenler | Sol dikey "DISTANCE ALONG THE ROAD" (90° döndürülmüş), alt sağ "TIME →" | "time running across and distance running up" |
| C10 | 1:52 | 1:57 | Kehribar çizgi | Tek bir aracın çizgisi kehribar; ucu zamanla sağa/yukarı uzar (line-draw) | — |
| C11 | 1:52 | 2:04 | Çizgi alanı sınırı | Sağ kenar zamanla ilerler (grafik "canlı" çiziliyor) | — |
| C12 | 1:57 | — | Lejant "/ MOVING" | Panel sol üst | "Where the lines climb steeply, traffic is moving" |
| C13 | 2:00 | — | Lejant "— STOPPED" (kırmızı) | Altına | "Where they go flat, it has stopped" |
| C14 | 2:02 | 2:05 | Kırmızı bölge | Daha fazla çizgi eklenir, kırmızı paralelkenar genişler | "The flat patch doesn't stay with any one car" |
| C15 | 2:05 | 2:06 | Kırmızı dalga cephesi | Sol üstten (x≈%15, y≈%12) sağ alta (x≈%68, y≈%45) düz çizgi, line-draw ~1 sn | "It slides down the chart" |
| C16 | 2:08 | 2:08,6 | "THROUGH CAR AFTER CAR" | Çizginin üstünde, kırmızı | "through car after car" |
| C17 | 1:58 | 2:09 | Kılavuz çizgiler | Yol şeridinden panele uzanan ince kesik yatay çizgiler (konum eşlemesi) | — |
| C18 | 2:08,6 | 2:09,4 | Geçiş | Dip → halka "12 CARS" | "It only happens when…" |

### 2. Katman yığını
1. L1 doku zemin (panel dışı alanda görünür)
2. L2 dikey yol + araçlar + glow
3. L3 fotoğraf çerçevesi
4. L4 lacivert panel (opak)
5. L5 eksenler + eksen etiketleri
6. L6 nokta matrisi / çizgi demeti (beyaz, kırmızı)
7. L7 kehribar vurgu çizgisi
8. L8 kırmızı dalga cephesi + etiketi
9. L9 lejant
10. L10 panel–yol kılavuz kesikli çizgiler
11. L11 sağ üst etiket

### 3. Reveal analizi
Sıra: bağlam (yukarıdan bak) → yöntem (saniyede bir foto) → ham veri (noktalar) → soyutlama (çizgiler) → okuma kuralı (lejant) → bulgu (kırmızı alan) → sonuç (kırmızı dalga çizgisi). Her adım bir önceki katmanı **silmeden** üstüne eklenir; izleyici ham veriden sonuca kadar zinciri görür.

---

## Ek · Reframe (2:23,5–2:25,5)
| Zaman | Olay |
|---|---|
| 2:23,5–2:24,0 | Halka merkezde (x %50), "23 CARS / THE SAME TAP GROWS" |
| 2:24,0–2:24,5 | Halka **sola kayar** x %50 → ~%28 (~0,5 sn); boyut korunur [G]; hız profili: başta hızlı, sonda yavaşlayan → ease-out/ease-in-out [Ç, orta] |
| 2:24,1–2:24,4 | Sağda lacivert grafik paneli (x %52–98, y %10–95) **fade-in**; eksen etiketleri panelle birlikte |
| 2:24,3 | Kehribar veri noktası grafik içinde belirir (x≈%60, y≈%60 kare) |
| 2:25–2:31 | Nokta eğri boyunca ilerler, arkasında beyaz iz |

---

## 5. Uygulama Reçeteleri

> Yazılımdan bağımsız yazıldı; parantez içinde AE / Remotion karşılığı.

### R1 · FREN GLOW SİSTEMİ
- **ELEMENT:** Araç başına kırmızı fren parıltısı
- **PURPOSE:** Dalganın kendisini görünür kılmak (videonun ana "aktörü")
- **STARTING STATE:** Glow opaklığı 0
- **TIMELINE:** Sürekli; araç başına `brake = clamp((v_prev − v)/dt / a_max, 0, 1)` veya `slow = 1 − v/v_free`
- **MOVEMENT:** Araçla birlikte
- **TRANSFORMATIONS:** Opaklık = smoothstep(brake), glow yarıçapı ≈ 3–4 × araç uzunluğu
- **LAYER ORDER:** Araçların üstü, vurgu şekillerinin altı
- **EASING:** Opaklıkta ~0,15 sn yükseliş, ~0,5 sn düşüş (attack/release)
- **SECONDARY EFFECTS:** Çekirdek: aracın arka kenarında 2 küçük parlak nokta; dış: Gauss blur, blend = add/screen
- **ENDING STATE:** Araç hızlanınca söner
- **TRANSITION TO NEXT SHOT:** Dip ile birlikte söner
- **SIMPLIFIED IMPLEMENTATION:** AE: araç pre-comp'unda kırmızı daire + Fast Box Blur 30 + Add mode, opaklığı "slider" ile; Remotion: SVG `<circle>` + `filter: blur()` + `mix-blend-mode: screen`, opaklık sim verisinden.

### R2 · HALKA SAHNESİ (T-RING)
- **ELEMENT:** Dairesel pist + 22 araç + merkez metin + dış veri yayı
- **PURPOSE:** Kontrollü deneyin "laboratuvar" görüntüsü
- **STARTING STATE:** Lacivert dip içinde görünmez
- **TIMELINE:** 0,0 dip-in (0,3 sn) → +0,4 başlık → +5 sn ilk merkez metin → her yeni olgu ~2–4 sn → dalga başlangıcı sahnenin ~%70'inde → sayaç → ok başı son 2 sn
- **MOVEMENT:** Araçlar açı θ_i(t) ile saat yönünde; pozisyon = merkez + R·(cos θ, sin θ), rotasyon = θ + 90°
- **TRANSFORMATIONS:** Dış yay: `startAngle` = kümenin kuyruğu, `endAngle` = başı (sim'den), r = R_dış + 0,04H
- **LAYER ORDER:** R2 katman yığını (SEG-B §2)
- **EASING:** Metin fade 0,3 sn ease-out; yay uzunluğu veriye bağlı (easing yok)
- **SECONDARY EFFECTS:** Glow (R1); ok başı yay ucuna eklenir, yönü teğet
- **ENDING STATE:** 11 STOPPED, uzun kırmızı yay + ok
- **TRANSITION TO NEXT SHOT:** R5 dip
- **SIMPLIFIED IMPLEMENTATION:** Simülasyon yerine: 22 aracı eşit açılarla döndür; t=19 sn'den itibaren bir "yavaşlama bölgesi" açısını `θ_jam(t) = θ0 − ω_dalga·t` ile CCW kaydır; bölgeye giren araçların hızını 0'a indir, çıkınca tekrar hızlandır. Bu, gerçek simülasyon olmadan aynı görüntüyü verir.

### R3 · ZİNCİRLEME FREN ÇUBUKLARI (S3)
- **ELEMENT:** Araç üstü dikey kırmızı çubuklar + kesik zarf
- **PURPOSE:** "Her sürücü problemi biraz büyüterek geri verir"i ölçülebilir göstermek
- **STARTING STATE:** Çubuk yüksekliği 0
- **TIMELINE:** Araç i fren yaptığında çubuk i büyür (0,4 sn); i+1 ~1 sn sonra; pasta zamanlayıcı i ile i+1 arasında 1 sn dolar
- **MOVEMENT:** Çubuk aracı yatayda takip eder (bağlı)
- **TRANSFORMATIONS:** Yükseklik = maks fren şiddeti × k (k ≈ %25H / maks)
- **LAYER ORDER:** Yol < araç < glow < çubuk < zarf < etiket
- **EASING:** Ease-out (hızlı başla, yavaş otur)
- **SECONDARY EFFECTS:** Kesik beyaz polyline çubuk tepelerinden geçer, yeni çubukla güncellenir
- **ENDING STATE:** Soldan sağa artan çubuk dizisi + STOPPED
- **TRANSITION TO NEXT SHOT:** 1:14 zoom-out (ölçek ~0,6×, 1 sn ease-in-out), sonra dip
- **SIMPLIFIED IMPLEMENTATION:** Değerleri elle yaz: [0,15, 0,35, 0,55, 0,75, 1,0, 1,0, 1,0] — gerçek sim gerekmez.

### R4 · ZAMAN-UZAY DİYAGRAMI (S5)
- **ELEMENT:** Panel + nokta matrisi → çizgi demeti + dalga cephesi
- **PURPOSE:** Dalganın geriye gittiğinin bilimsel kanıtı
- **STARTING STATE:** Panel yok
- **TIMELINE:** 0,0 panel fade (0,3) → 0–2,5 sn nokta sütunları (her ~0,15 sn bir sütun) → 2,5 noktalar→çizgiler (tek kare değişim) → 2,5–15 çizgilerin sağ ucu zamanla uzar → 8 lejant 1 → 11 lejant 2 → 16 dalga cephesi line-draw (1 sn) → 19 etiket
- **MOVEMENT:** Çizgiler: x = t·sx, y = konum·sy (sim kaydından)
- **TRANSFORMATIONS:** Renk: araç durmuşken segment kırmızı (`v < v_eşik`), değilse beyaz %60; seçili araç kehribar
- **LAYER ORDER:** SEG-C §2
- **EASING:** Line-draw doğrusal; panel fade ease-out
- **SECONDARY EFFECTS:** Panel–yol kesik kılavuz çizgileri
- **ENDING STATE:** Kırmızı paralelkenar + çapraz dalga çizgisi
- **TRANSITION TO NEXT SHOT:** Dip
- **SIMPLIFIED IMPLEMENTATION:** Python/JS ile basit bir "takip eden araç" modeli çalıştır, x(t) kaydını CSV'ye yaz, SVG polyline'a çevir; AE'de "Trim Paths End" 0→100.

### R5 · LACİVERT DİP GEÇİŞİ (tüm bölümler)
- **ELEMENT:** Tam ekran #0B121E katı
- **PURPOSE:** Bölüm sınırı; "nefes"
- **STARTING STATE:** Opaklık 0
- **TIMELINE:** 0,00–0,12 sn opaklık 0→1 · 0,12–0,20 sn tam · 0,20–0,50 sn 1→0 (yeni sahne altında) · +0,3–0,5 sn sonra H1 başlık fade
- **MOVEMENT / TRANSFORMATIONS:** Yok
- **EASING:** Çıkış ease-in, giriş ease-out
- **SECONDARY EFFECTS:** Müzik devam eder; VO'da 0,5–1 sn duraklama ile hizalı
- **SIMPLIFIED IMPLEMENTATION:** AE: solid + 2 opaklık keyframe çifti; Premiere/Resolve: "Dip to Color" (renk #0B121E), süre 12–15 kare @30 fps.

### R6 · BÖLÜM BAŞLIĞI (H1 + alt çizgi)
- **ELEMENT:** Sol üst başlık
- **STARTING STATE:** Opaklık 0
- **TIMELINE:** Dip bitişi +0,3–0,5 sn fade-in (0,3 sn) → 5–10 sn bekle → fade-out (0,3 sn)
- **MOVEMENT:** Yok [G]; alt çizgi için soldan sağa wipe opsiyonel [B]
- **LAYER ORDER:** En üst
- **SIMPLIFIED IMPLEMENTATION:** Tek metin preset'i + 4 px kehribar dikdörtgen (genişlik = metin genişliği × 0,75).

### R7 · ETİKET / SAYAÇ
- **ELEMENT:** ≤6 kelimelik büyük harf etiket; sayısal değişken
- **TIMELINE:** Anlatımdaki anahtar kelime anında fade-in 0,25 sn; sayaçlar tween'siz anlık değişim
- **SIMPLIFIED IMPLEMENTATION:** `Label({text, color, x, y, inAt, outAt})` bileşeni; sayaç = `Math.round(simValue)`.

### R8 · REFRAME (T-RING → T-SPLIT)
- **ELEMENT:** Halka + yeni panel
- **TIMELINE:** Halka x: %50→%28, 0,5 sn ease-in-out; panel opaklık 0→1, 0,3 sn, halka hareketinin 0,1 sn sonrasından başlayarak
- **SIMPLIFIED IMPLEMENTATION:** Tek position keyframe çifti + panel fade.

---

## 6. Kalite Kontrol
- [x] Üç segmentteki tüm görünür değişiklikler listelendi (A1–A16, B1–B14, C1–C18 + reframe).
- [x] Örtüşen olaylar ayrıldı (ör. B8/B9/B13; A4/A11/A13 aynı anda ama ayrı satır).
- [x] Statik (L1, L2, eksenler) ile hareketli (sim, veri yayları) katmanlar ayrıldı.
- [x] Kamera hareketi yalnız iki yerde (1:14 zoom-out, 2:24 reframe); 1:41 "dönüş" görünümü aslında geçiş — ayrıldı.
- [x] Tüm zamanlar yaklaşık; ölçüm hassasiyeti başlıkta belirtildi.
- [x] Belirsizlikler [B] ile işaretlendi (doku hareketi, dikey yol akış yönü, alt çizgi wipe'ı).
