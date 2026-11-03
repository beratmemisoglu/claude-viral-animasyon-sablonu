# 06 — Görsel makine ve yeniden kurma spesifikasyonu (özgün karakterlerle)

Kaynak: `deep-research/L3-visual-production-recipe.md` (10 videonun tamamında 92.000+ kare farkı ölçümü; v04+v05 saniye saniye). Kanalın karakterleri yalnızca analiz için tarif edilir; **biz özgün cast kullanırız**.

## 1. Görsel sistem özeti (ölçüm)
- **1920×1080, tam kare, letterbox yok (10/10); 25 fps (9/10; v08 50 fps).** Açılış: karadan 1,2–1,4 sn'de oturan ease-out fade-in (10/10). Sol-alt sabit filigran (beyaz %60 opaklık, aynı kutu, siyah karelerde bile görünür). Turuncu #ED720B marka bitiş kartı 3–14 sn (medyan 6,5) — çoğunda 0–6 sn siyah öncesi.
- **Karakter animasyonu yok:** ağız oynamaz, yüz ifadesi **tek karede değişir** (twin yok), konuşan planlar donuk. Hareket **kameradan**: eased push-in (medyan 1,0–2,1 %/sn; tipik 1,6) + 8–14 karelik hareket bulanıklı yeniden kadrajlar ("swish"; v05'te 37 adet). Fiziksel aksiyon: **2 çizim × 5 kare tutuş** (5 fps döngü).
- **Arka plan hep sabit görüntü:** ≥%85 süre; fotoğraf (Doomer/İş videolarında %61–95), 3D/AI-görünümlü CG (distopyada %55–81), çizim/boyama %0–8, UI maketleri %0–15, gerçek hareketli görüntü yalnız ekran içinde ≤%11.
- **Kesme dili:** sert kesme olayların %39–83'ü (8/10'da ≥%55); plan medyanı 2,3–3,8 sn; çapraz-eriyik 12–30 kare zaman atlaması/montaj için. Kare-aynı oranı: sözsüz %25, konuşmalı %43–59.
- **Vinyet:** köşe/merkez parlaklık 0,24–0,57 (karanlık köşe, aydınlık merkez, 10/10).
| | v01 | v02 | v03 | v04 | v05 | v06 | v07 | v08 | v09 | v10 |
|---|---|---|---|---|---|---|---|---|---|---|
| kesme/dk | 19,0 | 15,2 | 19,9 | 20,5 | 11,6 | 13,6 | 18,7 | 17,4 | 11,7 | 10,1 |
| plan medyanı sn | 2,72 | 3,34 | 2,28 | 2,48 | 3,68 | 3,32 | 2,58 | 2,65 | 3,80 | 3,38 |
| push-in penceresi % | 39 | 28 | 26 | 42 | 20 | 17 | 6 | 15 | 11 | 20 |
| BG (foto/CG/UI/video/çizim %) | 72/1/3/8/8 | 80/3/0/1/8 | 82/6/5/2/0 | 78/4/11/0/4 | 14/74/6/4/0 | ≈95/0/2/0/0 | 17/58/12/0/0 | 61/0/8/11/6 | 12/81/0/0/0 | 8/55/15/11/0 |

## 2. Karakter anatomisi (kanalın kadrosu — analiz)
- **Protagonist:** yetişkin oran (baş ≈ boy/6–7), uzun kel kubbe, yüz özellikleri kafanın alt ≈%55'inde, 3–4 px tüylenen siyah mürekkep konturu (baş ≈350 px iken); dolgu **#FEFFFD** (ışıklı yan) / **#E8EFEE** (gölge bandı); giysi düz dolgu + koyu kıvrım çizgileri; kıyafet bölüm kimliği (parodi markalı üniforma, kanal adı yaka kartında).
- **Duygu bindirmeyle çizilir, animasyonla değil:** göz torbası **#B99CB9** (yorgunluk/umutsuzluk) · kırmızı göz çevresi · mavi gözyaşı akıntısı + sıkılı dişler · mavi ter damlaları · nokta sakal + dağınık saç (ihmal) · pembe allık (kadın) · sunset 2-tonlu yeniden ışık (#F7AA5A turuncu / #9B5CA8 mor). **≈14 ifade** kütüphanesi (nötr, yan bakış L/R, yorgun, üzgün, ağlama, kararlı kaş çatma, kendini beğenmiş, coşkulu gülümseme, zorla gülümseme, tiksinme, şüpheli kısık göz, şok, gözler kapalı, huzurlu gülümseme).
- **Gövde pozları ayrı çizimler**; aynı poz çok planda yeniden kullanılır, yalnız yüz katmanı değişir. Yeniden tasarım = yay işareti (sonda sakal/torba/bere gider).
- **Yüzsüz kalabalık ("NPC" rolü):** aynı gövde grameri, kafa düz orta-gri **#979996–#A3A3A3**, nokta göz/L burun/düz ağız, ifade değişmez; çoğaltılmış sprite'lar; plaka ile birlikte bulanık (DOF). Anlam: "kişi olarak görülmemek".
- **İdealize rakip/güç figürü:** farklı, "daha yüksek" ortamda çizilir (foto-gerçek adam, 3B hologram, canlı çekim); protagonist düz 2B kalır → statü farkı diyalogsuz görünür.

## 3. Kompozit kuralları
| parametre | kural |
|---|---|
| Ölçek | Geniş: karakter kare yüksekliğinin %30–45'i · Orta: %80–110 (bel kesik) · Yakın: baş %50–70 · OTS: ensesi genişliğin %35–50'si bir kenarda |
| DOF | Plaka geniş planda net; orta/yakında Gauss bulanık; ön plan örtücü (halter, el, siluet) çok bulanık; **üç düzlem + blur, paralaks yok** |
| Gölge | **yok** (temas/atılı gölge yok) |
| Kenar | mürekkep konturu = kenar; stroke/glow/feather yok |
| Renk uyumu | güçlü ışıklı sahnede sahne rengi karakterlere itilir (mavi lobi → beyaz gömlek #374552); kurumsal sahnelerde plaka ≈S/B'ye desatüre, yalnız neon renk kalır |
| Perspektif | göz kararı; ufuk karakterin göğüs/göz hizası; küçük uyumsuzluk kabul |
| Ekranlar | TV/monitör içinde gerçek video/oyun/arayüz kompozitlenir (biz: kendi yaptığımız sahte arayüz/klip) |

**Metin:** diegetik öncelikli (telefon arayüzü, beyaz tahta, pano, neon, ürün etiketi). Altyazı yalnız "başka" sesler için (devlet/AI sesi, canlı çekim "patron"): beyaz hümanist sans, ≈3 px siyah kontur, ortada, alt kenar %86–91, büyük harf yüksekliği ≈%4. Faz kartı (yalnız v10): siyah ekran, beyaz kalın yuvarlak sans ≈%3,5 yükseklik, 1 sn fade-in, 3 sn tut, 0,5 sn çapraz-eriyik. Telefon metni TTS ile kelime kelime daktilo.

## 4. Pipeline, emek, maliyet (çıkarım; güven orta)
Senaryo → TTS (karakter başına ses; devlet/AI sesine robot efekti) → plaka topla (foto/CG), ekran görüntüsü, prop kesimleri → şablondan karakter katmanları (şeffaf PNG; vücut pozu + değiştirilebilir baş/yüz) → keyframe editöründe kompozit/animasyon (scale/pozisyon keyframe + easing, blur, yönlü hareket bulanıklığı, radyal blur, glow/light-leak, opaklık, daktilo, katman tonu) → müzik yatağı + SFX (**sözsüz filmlerde kesmeler beat'e kilitli: v04'te 57 kesmenin 52'si 97,6 BPM vuruşunun 80 ms çevresinde, 40'ı downbeat'te**) → 1080p25 export + filigran track'i + bitiş kartı şablonu.
**Emek:** kanal 2021–24'te ≈2 bitmiş dakika/hafta; yaratıcı "3 hafta" (v05, 7,35 dk) → **≈16 saat/bitmiş dakika (12–25)**. 2025–26 çıktı 178 → 261 dk/yıl (yardım/araç değişimi). **Maliyet (özgün cast ile 7 dk bölüm, USD):** karakter sayfası bir kerelik 900–2.000 · bölüm başı 20–40 yeni poz/ifade 300–600 (veya kendin) · 30–50 plaka kendi AI üretimiyle <20 hesaplama · TTS ~aylık plan · müzik/SFX aylık $15–30 · editör 40–70 sa (Remotion şablonuyla ≈3–5 sa/dk).

## 5. YENİDEN KURMA SPESİFİKASYONU
### 5.1 Proje/ihracat
1920×1080, 25 fps, progressif, Rec.709 SDR. H.264 High, CRF 16–18 (veya 12–20 Mbps VBR 2-pass), AAC-LC 48 kHz 320 kbps. Plakaları ≥2304×1296 (%120) üret/sakla (push'lar upscale etmesin). Ses: **−14 LUFS entegre, ≤−1 dBTP** (korpusun 7/10'u −20…−22,5 LUFS ile sessizdi = zayıflık); konuşma sahnelerinde müzik yatağı konuşmanın 12–18 dB altı.

### 5.2 Katman yığını (alttan üste)
1 BG plaka (blur 0 px geniş / 6–12 orta / 14–24 yakın) · 2 plaka propları (aynı blur) · 3 kalabalık (protagonistin %50–80'i; blur plaka×0,5–1,0) · 4 ana karakterler (2× boyda PNG; sahne tonu %20–40) · 5 ön plan örtücü (blur 10–30 px; genişliğin %25–50'si bir kenarda) · 6 FX (glow, light leak, gözyaşı bindirmesi, hız çizgileri; screen %40–80) · 7 sahne grade'i · 8 vinyet (köşe −%40…−60; köşe/merkez 0,25–0,55) · 9 diegetik arayüz/faz kartı/altyazı · 10 filigran (BİZİM kanal adı, sol-alt, beyaz %60, yükseklik ≈%5, x≈%1,6, y≈%92–97, kendi fontumuz — korpustaki görünümü kopyalama) · 11 geçiş katmanı.

### 5.3 ÖZGÜN CAST BRIEF'İ (hiçbir meme/IP'ye benzemez)
| Rol | Özgün tasarım | Benzerlik kontrolü |
|---|---|---|
| Sıradan adam protagonist ("Nob") | yumuşak yuvarlak-kare "ekmek somunu" kafa (en:boy 1:1,1), 3 telli saç tutamı, yuvarlak kulaklar; ten sıcak açık gri **#ECE8E2**, gölge **#D9D4CC**; gözler iki küçük dikey oval; duygu kalın kaş + ağızla; imza hardal **#D9A21B** atkı/fermuarlı mont; baş ≈ boy/6. *(Humdrum Hours projesinde marka paletiyle hizalandı: ten chalk `#F4F2ED`, gölge paper `#D8D5CE`, imza atkı amber `#F2A71B` — bkz. proje klasörü `brand/MARKA-RENK-PALETI.md` §5.)* | uzun kel kubbe, çene-kırışık meme yüzü, bere+kapüşon, nokta-sakal "doomer" varsayılan yok |
| Yüzsüz kalabalık ("Blanks") | aynı gövde şablonu, **özelliksiz** pürüzsüz yumurta kafa + tek koyu yatay vizör bandı; dolgu soğuk arduvaz **#8E959C**; kontur %70 ağırlık; ifade değişmez; çoğalt: ±%5 ölçek, ±4° ton | nokta göz + L burun + düz ağız (NPC memi) yok |
| İdealize rakip ("Vance") | protagonistten 1,25× boy, V gövde, 3 tonlu degrade gölgeli parlak saç savurma (Nob'dan "daha pahalı" render — orta-kontrast numarası), ten **#D9A47E**, imza: beyaz spor ayakkabı + altın kulaklık; hep 3/4, çene yukarıda | düz tepe-koni saç, aşırı kare çene profili, gerçek kişi fotoğrafı yok |
| Mentor/iç ses ("Ora") | yalnız dış çizgi, yarı saydam siluet, yumuşak camgöbeği parlama **#6FE3FF** %60, **yüz özelliği yok**; yansıma/ekran/hologram olarak görünür; sakin TTS sesi | foto-gerçek sakallı figür, gerçek sporcu/aktör benzerliği/adı yok |
| Devlet/AI sesi | UI avatarı: yuvarlak altıgen ikon + animasyonlu dalga formu **#7B61FF**; robot-işlenmiş TTS | gerçek uygulama/marka kopyası yok |
| Destek | aşk ilgisi (kıvırcık kumral bob, yeşil hırka), yüksek sesli müşteri, patron (hep arkadan/gölge), yaşlı komşu | "tradgirl/Karen" meme yüzleri yok; hepsini uydur |
| Bitiş kartı maskotu | Nob atkısıyla ¾ görünüm, el sallıyor | yalnız özgün |

### 5.4 Karakter sayfası teslimatları (2× boyda; kafa ≈700 px)
Adlandırma `{KARAKTER}_{parça}_{görünüm}_{durum}_v{n}.png` (şeffaf, 3840 px tuval). Kontur #111111, 2×'te 8 px (1080p orta planda 4 px), uçlar tüylenir; düz dolgu + ışığın zıt yanında tek cel-gölge bandı.
- **Gövde (karakter başına 18):** ayakta ön / ¾L / ¾R / arka · profil yürüyüş A/B · koşu ön A/B · kanepede oturma (+kumanda) · masa/dizüstü · bank · uzanma (üstten) · çömelme A/B · telefon tutma (POV uyumlu kol) · kollar kavuşuk · işaret · OTS ense büyük kırpım.
- **Yüz (protagonist, 16):** nötr, yan-L, yan-R, yorgun (+torba bindirmesi), üzgün, ağlama (+gözyaşı), kararlı, kendini beğenmiş, coşkulu, zorla gülümseme, tiksinme, şüpheli, şok, gözler kapalı/uyku, huzurlu, çaba (+ter).
- **Bindirmeler (8):** göz torbası (#B9A0C4), gözyaşı (#8EC1F0), ter, allık (#F2A7A7), sakal noktaları, kırmızı göz çevresi, sunset 2-tonlu relight maskeleri (turuncu #F7AA5A / mor #9B5CA8), soğuk-gece tonu maskesi.
- **Eller (6):** POV telefon L, dokunan parmak, işaretleyici el, işaret eden, fincan, yumruk.
- **Kalabalık:** 6 gövde × 3 kıyafet; rakip 10 gövde × 8 yüz; mentor 4 parlama pozu. **Bölüm başı:** 1 üniforma katman seti (uydurma marka logosu).

### 5.5 Arka plan kaynağı ve lisans
1. Yalnız kendi ürettiğimiz görseller (ticari lisanslı üretici), kendi fotoğraflarımız veya CC0/ticari video kullanımına izinli kütüphane.
2. **Görünür gerçek marka, logo, ürün ambalajı, okunur gerçek tabela, gerçek kişi, gerçek oyun/film görüntüsü, gerçek platform arayüzü YOK**; ekran-içi-ekranda kendi sahte arayüz ve klibimiz.
3. Plaka prompt şablonu: `photorealistic empty {mekân}, eye-level 35mm, {günün saati} lighting, no people, no text, no logos, clean composition, room for a character in the {sol/orta/sağ} third`; geniş ve sıkı orta kırpım varyantı üret; distopya için `neon {mor|mavi} accents, sterile, symmetrical`.
4. "Çoğaltılmış grid" ifşa plakasını tek üretilmiş hücreyi (≥4×4) döşeyerek yap.
5. Hareketli arka plan (image-to-video) ≤%10 ve yalnız ekran/pencere içinde; **karakterleri video modelle üretme** (stil kayması).
6. Her varlığı kaydet: kaynak, lisans, prompt/seed, tarih.

### 5.6 Grade tarifi (mood başına ölçülmüş hedefler)
| mood | ort. parlaklık | doygunluk | sıcaklık R−B | plaka | karakter tonu |
|---|---|---|---|---|---|
| umutsuzluk/gece | %15–25 | %40–46 | −5…−10 | −%40 koyult, mavi cast | %20 mavi |
| kurum | %22–28 | %19–28 | ≤−5 | plakayı %10–20 doygunluğa desatüre, neon rengi tut | %30 sahne rengi |
| nötr gün | %40–50 | %25–36 | 0…+3 | olduğu gibi | %0–10 |
| umut/insan sıcaklığı | %38–45 | %30–45 | +2…+6 | sıcak vurgular | %10–20 sıcak |
| coşku günbatımı (≤3 sn) | %35–45 | %40–50 | +5…+12 | gün batımı plakası | düz 2-tonlu relight |
**Yay kuralı:** dönüşüm hikâyesinde ort. parlaklık ilk perdeden son perdeye ≥+15 puan artsın (v04: 18 → 39).

### 5.7 Hareket presetleri (Remotion/AE/CapCut; 25 fps)
| preset | spec |
|---|---|
| FADE_IN | siyah katman opaklığı 1→0, 32 kare, ease-out cubic (plato 1,3 sn) |
| FADE_OUT | doğrusal 55 kare (2,2 sn) siyaha, sonra bitiş kartından önce 25–100 kare siyah |
| PUSH | scale 1,000 → 1 + r·t, r = %1,6/sn (aralık 1,0–2,6), easeInOutCubic, çıpa = yüz merkezi; plan başına toplam ≤%6 |
| PUSH_TURN | 2,2 sn eased push, tepe hız ≈7 px/kare, ZOOM_BLUR ile biter |
| PULL_REVEAL | scale 1,0 → 0,25 (90–100 kare), easeInOutQuad, döşenmiş grid plakaya |
| SWISH | tek kompozitin yakın↔ikili yeniden kadrajı 10 kare (8–14), ölçek oranı 1,6–2,2×, easeInOutCubic, hareket bulanıklığı 180° (yönlü blur tepe 40 px) |
| ZOOM_BLUR | kesme boyunca 6 kare radyal blur 0→30→0 px |
| DISSOLVE | zaman atlaması 12–25 kare; montaj çift pozlama 25–30 kare |
| EXPR_SWAP | yüz katmanını 1 karede değiştir; plan başına 0–3; vuruşa ya da replik bitişinden 4–8 kare sonra |
| CYCLE_2 | 2 çizim dönüşümlü, her biri 5 kare tut (5 fps); isteğe bağlı adım başına ±%1 ölçek sallanma |
| RACK_FOCUS | ön blur 0→20 px, arka 20→0 px, 12–20 kare |
| UI_DRIFT | telefon POV sürüklenmesi 5–10 px/sn + PUSH %1,4–2,2/sn; dokunma = parmak katmanı 3 karede, düğme vurgusu 4 kare |
| HOLO_IN | opaklık 0→1 10 karede, 2 glitch karesi ±8 px, additive glow 30 px, 3 px tarama çizgisi %20 |
| POP_IN | karakter/prop 1 karede belirir (komik vuruş) |
| **Yasak** | kamera sarsıntısı, lens flare spam'i, dudak senkronu, tween'lenmiş ifade, biri konuşurken >6 sn tutuş |

### 5.8 Kesme ritmi hedefleri (L4 ile birlikte: bkz. 07-audio-edit-rhythm)
Konuşmalı: plan medyanı 2,9–3,7 sn; 14–25 geçiş olayı/dk; ≥%55 sert kesme; her 6 sn diyalogda ≥1 SWISH; ≤6 sn donuk tutuş. Sözsüz: plan medyanı 2,4–2,5 sn **beat ızgarasında** (2–6 beat), kesmelerin ≥%85'i beat'e ±80 ms; saniyelerin ≥%40'ında push. Plan ölçeği (saniyeye göre): yakın %15–35, orta %40–55, geniş %15–30, insert/UI %5–15.

### 5.9 Remotion uygulama eskizi
Her JSON shot-list satırı için bir `Shot` bileşeni: `{id, durFrames, plate, plateBlur, crowd:[], chars:[{asset,x,y,scale,tint,faceSwaps:[{frame,asset}]}], fg, camera:{preset,rate,anchor}, transIn, ui, subs, audioCues}`. Kamera presetleri frame→transform saf fonksiyonları (`interpolate` + `Easing.inOut(Easing.cubic)`); hareket bulanıklığı yalnız SWISH'te (`@remotion/motion-blur` `CameraMotionBlur`). Daktilo metni TTS kelime zaman damgalarıyla; filigran ve grade üst düzey sarmalayıcılar; bitiş kartı sabit 7 sn kompozisyon. QA: fps=25, konuşmada kare tutuşu ≤150 kare, sert-kesme oranı ≥%55, push oranı 1,0–2,6 %/sn, LUFS −14 ±1.
**CapCut/AE eşlemesi:** PUSH = ease in/out scale keyframe · SWISH = 10 karede pozisyon+scale + hareket bulanıklığı efekti · ZOOM_BLUR = radyal/zoom blur geçişi 0,24 sn · DISSOLVE = 0,5–1 sn çapraz-eriyik · RACK_FOCUS = Gauss blur keyframe · HOLO_IN = glow + glitch · filigran üst track'te %60.

## 6. Anti-kalıplar
Tam karakter animasyonu/dudak senkronu/3B karakter/kamera sarsıntısı/letterbox (10/10 hiçbirinde yok; maliyet ekler, görünümü tutturmaz) · **tamamen çizim arka plan** (hiciv "gerçek dünya plakası üstünde kaba karakter"e dayanır) · 8–18 sn donuk konuşma tutuşları ve 17–18 sn sözsüz yürüyüşler (v05 ısı haritası ≤0,03) · sessiz miks (−20…−22,5 LUFS, 7/10) · gerçek marka/kişi/oyun/platform/hit şarkı/meme karakteri (korpusta var, bizim için yasak) · videoda hiç görünmeyen thumbnail karakterleri.

## Why it works
1. **En ucuz animasyon** (statik kesimler + kamera) ritimle gizlenir: her 2,2–4,3 sn'de bir olay ve çoğu saniyede push gözü meşgul eder.
2. **Kaba düz karakter + gerçek/gerçekçi plaka = anında hiciv:** "bizim dünyamızda yaşayan bir meme"; plaka dünya kurmayı bedavaya getirir.
3. **Duygu küçük, okunaklı bir bindirme sözlüğüyle** taşınır (torba, gözyaşı, kaş çatma, allık, grade) → telefon boyutunda ve her dilde okunur.
4. **Gri yüzsüz figüran vs tek çizili protagonist** yabancılaşma temasını sanat yönetiminin kendisine kodlar.
5. **Rakip/güç figürünü "daha yüksek" ortamda** (foto, hologram, canlı çekim) çizmek statü farkını diyalogsuz gösterir.
6. **Sabit şablon** (filigran, fade-in, bitiş kartı, üniforma değişimi, telefon POV) tek kişinin haftada ≈2 bitmiş dakika yapmasını sağlar.

## Rules to copy
1. [KOPYA] 1920×1080, 25 fps, tam kare, letterbox yok; her videoyu 1,2–1,4 sn ease-out fade-in ile aç.
2. [KOPYA] Sürenin ≥%85'i özgün düz dolgulu siyah mürekkep kesim karakterler **sabit plaka** üstünde (foto-gerçek ya da CG); hareketli görüntü ≤%10, yalnız ekran içinde.
3. [KOPYA] Kamerayla anime et: push-in %1,0–2,6/sn (varsayılan 1,6, eased), saniyelerin %20–45'inde; sarsıntı yok, paralaks rig yok.
4. [KOPYA] Karakter dudak senkronu yapmaz; ifade yalnız **1 karelik yüz değişimiyle** (plan başına 0–3, 16 durumluk kütüphaneden); fiziksel aksiyon 5 kare tutuşlu 2 çizim döngüsü.
5. [KOPYA] Geçişlerin ≥%55'i sert kesme; plan medyanı 2,4–3,7 sn; diyalog kapsamını 8–14 karelik hareket bulanıklı yeniden kadrajlarla kur.
6. [KOPYA] Plakayı plan ölçeğine göre blur'la (0 / 6–12 / 14–24 px: geniş/orta/yakın), ön plan örtücüyü 10–30 px bulanıklaştır, asla gölge ekleme; güçlü sahne ışığında karakterleri %20–40 tonla.
7. [KOPYA] Grade'i §5.6 tablosuna göre; vinyet köşe/merkez 0,25–0,55.
8. [KOPYA] Kurumlar ve kalabalıklar için özgün yüzsüz arduvaz-gri figüranlar; sprite'ları ±%5 ölçekle çoğalt; distopya bölümünde bir kez "çoğaltılmış grid" ifşası.
9. [KOPYA] Protagonistin durumunu bindirmelerle çiz (torba #B9A0C4, gözyaşı #8EC1F0, ter, allık, sakal) ve dönüşüm yayında sonunda daha temiz yeniden tasarla.
10. [KOPYA] Rakip/güç figürünü protagonistten daha ayrıntılı bir ortamda render et (degradeli gölge, hologram, ya da rıza veren oyuncunun kendi çekimi).
11. [KOPYA] Bilgiyi diegetik arayüze koy (çizili elli telefon POV, TTS kelime zamanlarıyla daktilo); yalnız makine/devlet seslerine altyazı.
12. [KOPYA] Sol-altta sabit %60 beyaz filigran; 6–8 sn marka bitiş kartı, 2 bitiş ekranı slotu, 1–4 sn siyah öncesi.
13. [İYİLEŞTİRME] Biri konuşurken tutuş >6 sn yok; yeni gag/kesme/ifşasız sözsüz uzatma >6 sn yok.
14. [İYİLEŞTİRME] Her videoyu **−14 LUFS** entegre, ≤−1 dBTP'ye mastırla.
15. [İYİLEŞTİRME] Thumbnail karakter ve propları videoda aynı tasarımla bulunsun.
16. [ETİK] Meme yüzü (Wojak/NPC/Chad/Pepe türü), gerçek kişi veya adı, gerçek marka/logo/ambalaj, gerçek platform arayüzü, oyun/film görüntüsü, hit müzik **asla**; her plaka, UI ve parça kendi yapımımız veya ticari video için lisanslı, kaynak+lisansla kayıtlı.
17. [ETİK] Parodi markalar **uydurma isim ve uydurma logo**; gerçek logonun şekil/renk eşleşmesini hatırlatmasın.

## Open questions
Kullanılan çizim/edit uygulamaları pikselden kanıtlanamaz (yalnız artefakt tipinden çıkarım) · CG plakaların kaçı AI, kaçı render/yakalama (1080p bit hızında ayrılamaz) · 8 atanmamış videonun BG yüzdeleri 72'şer örnek saniyeye dayanıyor (±10 puan) · 2025–26'da ≈5 dk/hafta çıktıya geçiş (ekip/araç değişimi) bu korpusta (≤2024) görünmüyor.
