# 05 — Tutorial edit grameri (Mod T): ne görünür, ne zaman, nasıl

Kaynak: `deep-research/04` (nicel), `05` (03:12–09:25), `06` (09:25–15:55), `07` Part A (15:55–22:52), `02` (giriş).
Etiketler: **[KOPYA]** referansta ölçüldü · **[İYİLEŞTİRME]** referansın zayıflığını düzeltir · **[ETİK]** IP/politika/gizlilik.

## 0. Tek cümle
**İki hızlı edit:** ilk ~3 dakika *kanıt fragmanı* gibi kurgulanır (her 1,5–2 sn'de değişim, sayıya zoom, meme, kinetik yazı, CTA kartı);
sonra video **çıplak, 1:1, açık-mod tarayıcı kaydına** döner — vurguyu editör değil sunucunun faresi yapar
(metin seçimi + kırmızı tıklama halkası), bekleme kırpılır, sonuç anı müzik vuruşuyla işaretlenir.

## 1. Çekim türleri ve payları [KOPYA]
| Tür | Pay | Nerede |
|---|---|---|
| Tam kare ekran kaydı (1:1) | %71 | gövdenin tamamı |
| Zoomlu ekran kaydı | %5 (70 sn) | **sadece 0:16–4:14** |
| CapCut arayüzü | %13 | Editing bölümü |
| Bitmiş video oynatımı | %5 | 19:28 teaser 8,7 sn + final 58,7 sn |
| Rakip örnek klip | %3 | giriş + görseller adımı |
| Tam ekran yazı/grafik kartı | %1,5 | hook + CTA |
| Meme / B-roll | %0,6 | 0:00, 0:02, 2:15, 10:53 |

Uygulama değişimi (YouTube → Docs → ChatGPT → Whisk(sarı) → Claude → AI Studio → Grok → CapCut(koyu)) her 1–3 dk'da
renk ve düzeni **bedavaya** değiştirir — gövdenin görsel çeşitliliği budur.

## 2. Ekran kaydı çerçevesi [KOPYA]
- Açık mod tarayıcı, 1920×1030–1032 yakalama, üst-alt **24–25 px siyah bant**.
- Tüm kayıtların üstünde **sabit radyal vinyet**: merkez %100, kenar ortaları ~−%9, köşeler ~−%16 (beyaz → ~#D6D6D6). Zoom'la birlikte hareket etmez, kareye kilitli.
- Sistem imleci normal boyutta; konuşma sırasında boş alanda bekler, söylenen öğeye gider.
- **Tıklama halkası:** her tıklamada yarı saydam kırmızı halka (~#CA2C2C / #E08A8A), ~6 px'ten ~45 px'e (≈%4 H) 0,25–0,3 sn'de büyür ve söner.
- Ekran kaydı aracında tıklama görselleştirici açık (Screen Studio / OBS eklentisi / CapCut keyframe ile eşdeğer).

## 3. Kesme kuralları [KOPYA]
- **Sadece sert kesme**; gövdede dissolve/wipe yok; kesmelerde whoosh/pop SFX **yok**.
- Uygulamaya kesme, anlatıcı adını söyledikten **+0,4…+2,8 sn (medyan +0,9 sn)** sonra — *isme kes*.
- Ekran dışı işler görünmez kesmelerle atılır (sorgu yazmak, sekme aramak, sayfa yüklenmesi > 1 sn): neredeyse aynı kareden kareye kes, sonuç zaten ekranda.
- Gerçek zamanlı yazı sadece **talebin kendisi ders olduğunda** (≤ 8 sn, yazılırken kelime kelime söylenir).
- Tekrarlı manuel iş (görsel yerleştirme): ilk 2–3 tekrarı tam göster, sonra **jump-cut montajı** (1,2–1,5 sn/çekim; 14 kesme/18,7 sn);
  CapCut'ta ~10:1, en yoğun yerde 14:1 zaman sıkıştırma, anlatım hiç durmadan devam eder.
- AI bekleme süresi gönderdikten sonra **≤ 1 sn'ye kırpılır**; bölüm başına en fazla 1 uzun bekleme (≤ 8 sn), o da üstünde ipucu anlatılıyorsa. Alternatif: **4–10× hızlandırma** (Docs temizliği, Grok ilerleme çubuğu).

## 4. Zoom dili
- **[KOPYA] Kanıt girişinde:** söylenen her sayı/başlık için punch-in **1,45–1,67× (tipik 1,55×)**, 0,3–0,7 sn S-eğrisi + pan, 3–4 sn tut, sonraki cümlede %100'e dön. Yavaş itme 1,12–1,32× / 1–2,7 sn. Kırmızı ince kutu (~2 px #FF0000) sadece zoom ile, 2 kez.
- **[KOPYA] Gövdede:** 1:1, zoom yok — tek istisna izleyicinin değiştireceği **tek parametre** (ör. prompt'taki "30"): merkez 1,70×, 1,8 sn giriş, değer canlı yazılırken 4–20 sn tut, 2,5–3 sn çıkış. Aynı eylemin tekrarlarına zoom yok.
- **[İYİLEŞTİRME] Okunabilirlik:** prompt gövdesi %1,2–1,5 H (telefonda ~2 mm) → 29–44 "PDF nerede" yorumu. Kopyalanacak blok metni < %2 H ise **1,5–1,7× punch-in** ile ≥ 3 sn göster
  ya da paketi yüklemede linkle. Aksi halde native boyut kalabilir.

## 5. Vurgu sistemi [KOPYA]
| Araç | Kullanım |
|---|---|
| **Native metin seçimi** (ChatGPT mavisi #B5D4F6) | söylenen satır/öğe ≤ 1,5 sn içinde seçilir, 1–5 sn tutulur; liste/doküman ekranında her 7–14 sn'de bir (~27–33 adet / 6 dk) |
| Tüm prompt'u sürükleyerek seçme | 2–6 sn, sonunda uzunluğu göstermek için scroll |
| **Google Doc başlığı = bölüm kartı** | her alt adım kendi Doc başlığında açılır: kırmızı **#F7200E Lexend Bold ~24 pt** metin, gri **#D7D6D6** vurgu bandı; başlık tıklanır/seçilir, altındaki prompt sürüklenerek seçilir |
| İmleç okuma işaretçisi | anlatılan satırın altında gezdirilir |
| **YOK** | editörün çizdiği kutu (giriş hariç), ok, altı çizgi, daire, büyüteç, emoji, lower-third, picture-in-picture, webcam, yüz |

## 6. Overlay ve ek spesifikasyonları
### 6.1 Hook ekleri (ilk 10 sn) [KOPYA — içerik özgün olmalı]
| Zaman | Ek | Görünüm |
|---|---|---|
| 0:00–1,9 | film/meme kesiti (sessiz, letterbox) | tam kare; açılış sorusu 0. karede başlar |
| 1,9–3,3 | sinematik B-roll | tam kare |
| 3,3–4,8 | **kinetik yazı** (kelime kelime) | koyu sans, açık gri gradyan #E0E0E0–#F8F8F8 |
| 4,8–7,0 | görsel kart (gölgeli kart içinde illüstrasyon, fade+scale-in) | gri zemin |
| 8,0–9,2 | **siyah başlık kartı** (niş adı) | beyaz bold, hafif eğik, saf siyah zemin |
| ≤ 0:08 | ilk gerçek ekran kanıtı | YouTube kanal sayfası |
→ hook detayları: `03-hook-intro.md`. [ETİK] film/TV/güreş kesitleri yerine **lisanslı veya kendi** meme/B-roll kullan.

### 6.2 Abone animasyonu (3,4–3,9 sn) [KOPYA]
| Faz | Zaman | Ne olur |
|---|---|---|
| Kesme | 0 | arka plan **~%20 parlaklığa** karartılır (beyaz → #292929), hafif blur |
| Kart açılır | 0–0,4 sn | beyaz kart ince yatay çizgiden açılır (~%38 W × %19–25 H, merkez) |
| Buton | 0,4–0,9 | solda kırmızı oynat-dairesi (#F00005) + kırmızı **SUBSCRIBE** (#E80000, beyaz bold, cap ~%3 H) |
| Tıklama | 0,9–1,6 | beyaz el imleci sağ alttan girer ve tıklar |
| Durum | 1,7–2,3 | gri **SUBSCRIBED** (#DFDFDF, koyu yazı) + parçacık patlaması |
| Çıkış | 3,0–3,4 | kart aşağı kayar, sert kesme |
Sadece **bekleme anında** (senaryo üretimi, ses render) veya kanıt bölümünün sonunda; kopyalanan prompt'un üstüne asla.

### 6.3 Hedef kartı ("100K Subscribers" / "200 Likes") [KOPYA]
- Neon yeşil **#3AFC00–#3DFD02**, ağır yuvarlak geometrik sans (Poppins/Montserrat Black sınıfı), kalın siyah kontur + sert gölge.
- Yükseklik %10,5–14 H, genişlik %49–66 W, merkez y ≈ %49; arka plan sayfası **%10–20 parlaklığa** karartılmış.
- 2,3–4,9 sn, statik, sert giriş/çıkış, SFX yok. Videoda en fazla 2 adet (abone hedefi kanıt sonunda, beğeni hedefi finalden önce).

### 6.4 Meme / sticker [KOPYA + ETİK]
- Birebir anahtar kelimede ("para" → para meme'i), ≤ 2–5 sn, uzun tutorial'da 2–3 dk'da 1.
- 1,5–2 sn'lik kesik-çıkarma sticker bir **jump-cut'ı örtmek** için kullanılabilir (bekleme sonu → bitmiş sonuç).
- [ETİK] Silah, şiddet, telifli film/TV kesitleri **yok** — kendi maskotumuzun şaşkın/yalvaran pozu gibi zararsız özgün grafik.

### 6.5 Sonuç gösterimleri [KOPYA]
- Görseller aracın kendi ızgarasında (2-up, ~%45 W × %38 H) kalır; büyütülmez; çok-varyant ızgara 3–5 sn → kamerada **reddet** (en fazla 2 kez) → düzeltmeyi canlı yaz → iyi sonuç sting + 10 sn içinde görünür indirme.
- **Video çıktısı tam ekran bir kez:** saf siyah üstünde ~%78 W × %77 H, 5–6 sn, **kendi sesiyle**, sert kesme giriş/çıkış — bölümün ~%90'ında, en yüksek ses anıyla eşleşir (orta-üçteki "vay" anı).
- Ses demosu: mod, stil talimatı, ses listesi ≥ 5 sn; native oynatıcıda toplam süre görünür; üretilen ses 5 sn (anlatımın +3–4 dB üstü); dalga formu grafiği gerekmez.
- Her araç bölümünün sonunda 3–5 sn **galeri scroll'u** (hacim kanıtı).
- Editten sonra, thumbnail/SEO'dan önce 6–10 sn **bitmiş sonuç önizlemesi** tam ekran.
- Sosyal kanıt B-roll'ü: 2–3 adet 8–20 sn kanal sayfası (Popular sıralı, izlenmeler görünür), motivasyon anlatımı altında.

## 7. Ses grameri
| Öğe | Referans | Bizim kural |
|---|---|---|
| Anlatım | mono, ~200 wpm, %94 kaplama, nefes kesilmiş, LRA 2,8 | [KOPYA] 170–190 wpm (TR 150–170), ≥ %90 kaplama, nefes temiz, LRA ≤ 4 |
| **Sonuç sting'i** | 11 adet, anlatım boşluğunda sonuç belirdiği anda; bas ağırlıklı müzik vuruşu, 0,2–1,5 sn (bazıları 3–5,6 sn zincir); konuşma RMS'inin **~+12–14 dB** üstü (18:07'de doğrulandı: −10,7 dB vs anlatım −23,2 dB, 20–150 Hz bandında +18 dB) | [KOPYA] her sonuç açılışında 0,3–1,5 sn sting, 6 dk'da 3–5 adet; [İYİLEŞTİRME] seviye **+6…+10 dB** (referans kulak tırmalar), 50 ms fade-in, 200 ms fade-out |
| Montaj/hızlandırma boşluğu | anlatım ≥ 2,5 sn susunca ritmik müzik açılır | [KOPYA] aç, bir sonraki cümlede 0,3 sn içinde duck |
| Müzik yatağı | 21,8 sn periyotlu döngü, pratikte duyulmaz (≤ −45 dBFS) | yok **ya da** −30…−35 dB altta |
| SFX | kesmelerde/kartlarda yok | yok (opsiyonel: sadece hook başlık kartlarında yumuşak whoosh) |
| Ekler | WWE meme, rakip klip, Grok demosu, final video kendi sesiyle; diğer örnekler sessiz | [ETİK] üçüncü taraf sesli klip yok; kendi ürünümüzün sesi serbest |
| Mix | −19,4 LUFS | **−14…−16 LUFS**, true peak ≤ −1,5 dBTP |

## 8. Gizlilik ve temizlik [ETİK]
- Referans sızdırdı: Windows dosya seçicide kullanıcı adı, indirme panelinde dosya adları, yer imlerinde Gmail sayacı; tek blur maskesi (sol alt hesap alanı ~%13 W × %4 H, yumuşak Gauss).
- Bizim kural: ayrı tarayıcı profili (temiz yer imleri, eklenti rozetleri kapalı); export öncesi dosya seçici, indirme paneli, avatar, e-posta, API anahtarı kontrolü; gerekirse yumuşak blur.
- Bırakılabilir "gerçeklik kanıtı": dosya boyutları, ilerleme çubukları, otomatik kaydetme saati (zaman sıkıştırmayı dürüstçe gösterir).

## 9. Bölüm geçişi [KOPYA]
- Ekranda bölüm kartı **yok**; geçiş = tek cümle ("X hazır, şimdi sıra Y'de") + aynı anda uygulama/Doc başlığı değişimi.
- Bölüm işaretini izleyicinin en çok istediği adımdan **0–3 sn önce** koy (Voice bölümü −2 sn → global tekrar izleme zirvesi).
- [İYİLEŞTİRME] Referansın 06:41 sınırında hiç görsel değişim yok → yeni bölümün ilk cümlesinden ≤ 1 sn sonra yeni uygulamaya/Doc başlığına kes.

## 10. Kapanış [KOPYA + İYİLEŞTİRME]
- Son 40 sn: sözlü abone isteği kanal sayfası üstünde (8–10 sn) → hedef kartı (4 ± 0,5 sn) → kaynak paketi yeri → tek veda cümlesi → **sert kesme** ile bitmiş video (45–75 sn).
- [İYİLEŞTİRME] Referans final videoyu cümle ortasında kesiyor (tekrar izleme 0,00): tam cümlede bitir, ≥ 0,5 sn tut, 3–5 sn markalı outro + 5–20 sn end screen.

## 11. Edit Karar Listesi (EDL) şablonu — Mod T
Her tutorial için editöre/otomasyona verilecek tablo:

| # | Başlangıç | Bitiş | Bölüm | Çekim türü | Ekran/uygulama | Kamera | Vurgu | Overlay/ek | Ses olayı | Anlatım (özet) | Kural ref. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 00:00.0 | 00:01.9 | Important | meme | — | — | — | sessiz kesit | — | açılış sorusu | 03 §1 |
| 2 | 00:01.9 | 00:03.3 | Important | B-roll | — | — | — | — | — | soru devam | 03 §1 |
| … | | | | ekran 1:1 / zoom 1,55× / CTA kartı / sonuç tam ekran / montaj | YouTube / Docs / ChatGPT / … | static / punch-in / push | seçim / tıklama halkası / kırmızı kutu | abone kartı / hedef kartı / kinetik yazı | sting / müzik açılır / klip sesi | | |

EDL'yi senaryonun kelime zaman damgalarından üret (`words.json`): her "sayı/başlık/alan adı" kelimesi → zoom veya seçim satırı; her "şimdi bak" → sting + sonuç satırı;
her bekleme → kırp/hızlandır/CTA satırı. Sonra `edit_rhythm_qa.py --profile tutorial` ile doğrula.
