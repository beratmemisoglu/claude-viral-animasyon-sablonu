# 07 — Kesme ritmi ve ses tasarımı (nicel)

Kaynak: `deep-research/L4-audio-edit-rhythm.md` — 10 videonun tamamında `scripts/rhythm_qa.py` ile ölçüldü (kare farkı + EBU R128 + mid/side ayrıştırması + spektral akış + pYIN perde + heatmap + whisper kelime zamanları). Tüm sayılar **yalnız hikâye** (0 → bitiş kartı başı) üzerinden, **kalibre edilmiş** sınırlarla.

## 1. "Kesme" ne sayılır (kalibrasyon)
Görüntüler karakterlerin sabit kompozitleri + sanal kamera olduğu için ham scdet hem fazla hem eksik sayar. v07/v08/v10'daki her sınır önce/sonra karelerinden elle kontrol edildi:
| Olay | scdet≥8 | Sayılır mı |
|---|---|---|
| Sert kesme (1 karelik değişim) | evet | **evet** |
| Hızlı yeniden kadraj (4–12 kare zoom/whip, aynı kompozitte 2'li → tekli; ya da hareketli görüntüye kesme) | **kaçırır** | **evet** — kanalın yeni çizim yapmadan "kesme" yolu (79 adet) |
| Slayt-pan (13–35 kare eased kayma, iki konuşmacı arası) | kaçırır | evet (25 adet) |
| Eriyik/üçlü pozlama | kısmen | evet |
| Siyah tutuş/fade | birleştirir | siyah ayrı "plan", istatistiklerden hariç; açılış fade-in <1,2 sn sayılmaz |
| Yavaş push-in, paralaks yürüyen, poz değişimi (yüz/kol çizimi) | bazen tetikler | **hayır** (poz değişimi ayrı raporlanır: 1,5–13,8/dk) |
**Net etki:** kalibre sınır = scdet≥8 kesme **+%17** (1.012 vs 864). Konuşmalı videolarda fark büyük (v05 +32, v10 +32, v06 +21). → `rhythm_qa.py --montage` ile elle onayla.

## 2. Ritim — karşılaştırma (kalibre)
| | v01 | v02 | v03 | v04 | v05 | v06 | v07 | v08 | v09 | v10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Aile | Doomer | Doomer | İş | Doomer | Distopya | İş | Distopya | İş | Distopya | Bağımlılık |
| Ses | yok | TTS | TTS | yok | TTS | TTS | TTS | TTS | TTS | TTS |
| Hikâye sn | 215 | 274 | 445 | 161 | 433 | 446 | 412 | 205 | 351 | 407 |
| **Sınır/dk** | 20,6 | 18,2 | 21,6 | **23,5** | 16,1 | 16,5 | 21,1 | 19,3 | **14,2** | 14,6 |
| 0–15 sn /dk | 20 | 16 | 24 | 20 | 16 | 28 | 20 | 16 | 20 | **8** |
| 15–60 sn /dk | 18,7 | 17,3 | 26,7 | 21,3 | 16,0 | 16,0 | 22,7 | 22,7 | 22,7 | 17,3 |
| gövde /dk | 22,6 | 19,3 | 21,1 | 25,3 | 16,6 | 16,5 | 21,0 | 19,7 | 12,9 | 15,5 |
| son 30 sn /dk | 16 | 14 | 18 | 24 | 10 | 12 | 20 | 14 | 10 | **4** |
| plan p10/medyan/ort/p90 sn | 1,54/2,64/2,88/4,43 | 1,28/2,96/3,30/5,64 | 1,28/2,28/2,77/5,00 | 1,49/2,44/2,53/3,66 | 1,52/3,12/3,70/6,18 | 1,48/3,00/3,60/6,08 | 1,40/2,34/2,82/5,10 | 1,14/2,44/3,03/6,17 | 1,69/3,60/4,23/7,63 | 1,27/3,08/4,07/7,28 |
| max plan sn | 6,5 | 10,0 | 9,6 | 6,1 | **17,3** | 14,0 | 8,7 | 9,5 | 14,6 | **35,1** |
| ilk sınır sn | 1,9 | 3,9 | 2,2 | 2,7 | 2,9 | 1,4 | 3,1 | 3,7 | 5,6 | 4,5 |
| bitiş kartı sn | 4,9 | 7,3 | 7,3 | 8,8 | 7,3 | 7,3 | 14,6 | 5,0 | 8,0 | 13,8 |
| LUFS / LRA | −14,6/11,3 | −20,6/10,1 | −21,9/12,8 | **−10,5**/10,8 | −21,4/12,3 | −22,5/15,7 | −19,9/11,9 | −16,6/9,6 | −18,1/12,5 | −20,1/12,7 |
| True peak dBTP | −3,0 | −2,6 | −0,5 | +0,7 | +0,3 | −4,2 | −0,7 | +0,7 | +0,4 | +0,4 |
| Müzik yatağı hikâyenin % | 100 | 99 | 95 | 98 | 97 | 85 | 93 | 87 | 97 | 77 |
| Konuşma payı % | 0 | 55 | 48 | 0 | 51 | 51 | 55 | 32 | 57 | 42 |
| Yatak sesin altında LU | – | 6,4 | 8,7 | – | 7,4 | 11,9 | 9,3 | 2,8 | 9,1 | 5,1 |
| Konuşma başlangıcında müzik değişimi dB | – | +0,1 | −0,8 | – | −2,7 | +0,2 | +2,0 | −1,6 | +0,9 | −1,1 |
| ≥1 sn sessizlik | 1 | 1 | 4 | 1 | 2 | 1 | 4 | 0 | 1 | 6 |
| Ses-dışı geçici ses (SFX)/dk | 0,5 | 2,1 | 7,8 | **0,0** | 4,8 | 7,7 | 3,2 | 5,4 | 3,3 | 5,7 |
| Top tekrar zirvesi (hikâye içi konum) | 0,87 ihanet | 0,87 ayna | 0,94 viral gönderi | 0,41 beyaz tahta | 0,39 meme klibi | 0,99 son gag | 0,89 gizli kayıt | 0,88 manşet | 0,85 catfish | 0,80 ödeme + yıkılmış yüz |
Sıralama sinyali (betimleyici, n=10, yıl ve konuyla karışık): ρ(izlenme, sınır/dk) = **+0,56**; hikâyede >13 sn plan olan her video (v05, v06, v09, v10) 5.–10. sırada; top-4'ün en uzun planı ≤10 sn.

## 3. Plan uzunluğu dağılımı (1.006 plan, birleşik)
p10 **1,36 sn** · p25 1,88 · **medyan 2,66** · p75 4,03 · p90 5,70 · ort 3,28 · %13,4 plan <1,5 sn · %3,3 plan >8 sn. Saga medyanı 2,44–2,96 sn, **max ≤10 sn**; iş 2,28–3,00; distopya 2,34–3,60 (en uzun konuşma tutuşları); döngü 3,08 + 35 sn tutuş.
**Kural: korpustaki her >8 sn tutuş bir diyalog/monolog planıdır; hiçbir aksiyon/montaj/tepki planı 6,5 sn'yi aşmaz.** Sözsüz videolar hiç >6,5 sn tutmaz. En uzun tutuşlar: v10 35 sn (ofis partisinde yalnız yakın plan = izolasyon), v10 21,5 sn (öğle masası), v05 17,3 sn (geniş plan grup diyaloğu), v09 14,6 sn (depo, slayt-pan'lı diyalog).

## 4. Ritim hikâye vuruşlarını nasıl izler
1. **Konuşma yoğunluğu kesme hızını belirler:** ≥%70 konuşmalı pencerelerde medyan **12 sınır/dk**, <%70'de **18** (294 on-saniyelik pencere; ρ=−0,25). v07'de sözsüz olay örgüsü vuruşları 25–32/dk, diyalog 10,7–18/dk; v08'de montaj 23–44/dk, monolog 6–12,5/dk.
2. **Düz gövde, yavaş bitiş:** onluk dilimler (tüm 10): 19,4 · 19,9 · 20,4 · 18,4 · 21,0 · 18,2 · 17,9 · 18,3 · 18,3 · **13,9** — son dilim 7/10'da yavaş (ifşa tutuşuna oturur).
3. **Hızlanma sivri uçları = sözsüz dönüm noktaları** (v08 işe alım 39/dk, sabotaj merdiveni 32/dk, hastane ifşası 44/dk); yavaşlama = tartışma ya da ironi.
4. **Perde arası kesme hızıyla değil siyah ya da müzik değişimiyle işaretlenir:** v08 5,6 sn siyah + sub vuruşu (hikâyenin %57'sinde); v02 siyah 2:15 (%49); v10 faz kartları (0:00, 2:16, 2:19, 3:18).
5. **Tekrar-izleme ≠ ritim:** heatmap vs yerel kesme yoğunluğu ρ=−0,06…+0,18 (ilişki yok). Zirvelerin ortak noktası **içerik:** en yüksek zirve hikâyenin **%80–99'unda (8/10)**, her zaman ifşa/ödeme karesi; 6/10'da okunur metin/arayüz.

## 5. SES — ölçülen gramer
- **Ses seviyesi.** Konuşmalı −16,6…−22,5 LUFS (medyan −20,4); sözsüz müzik filmleri −10,5 ve −14,6. LRA 9,6–15,7 (medyan 12,1). **10 videonun 5'inde kodlama sonrası >0 dBTP** (limiter disiplini yok). Açılış yumuşak: ilk 15 sn gövdeden **≥2,8 LU (8/10), ≥8,9 LU (7/10)** kısık.
- **Müzik.** Yatak hikâyenin %77–100'ünde (9/10'da ≥%85). Parça değişimi mekân kesmesi ve perde arasında; konuşmalı videoda 2–4 parça. Roller (spektral karakter + yerleşimden): *muzipli/komedi cue* (pizzicato kütüphane parçası; kurulum, entrika, gündelik aşağılanma) · *karanlık/kötü adam cue* (alçak, minör; perde arasından sona) · *serin/idil cue* (caz/boom-bap döngü; Chad'le yolculuk, montaj) · *hype cue* (kahraman girişi, v05) · *epik/metal* (bağımlılık tepeleri) · *duygusal marş:* sözsüz Doomer filmlerinde tüm film boyunca tek meme-ünlü şarkı enstrümantal/cover (v01 ≈129 BPM, v04 ≈99 BPM, v02 yumuşak ambient piyano ≈89 BPM). **Tempo tahmini karışık materyalde güvenilmez**; yalnız tek başına çalan parçalar güvenilir.
- **Lisans:** konuşmalı videolar royalty-free/CC-BY kütüphane parçaları kullanır [kredilerden çıkarım]; iki sözsüz top-5 film **ticari şarkı** (MGMT enstrümantali, cover edit) → Content ID riski → **kopyalama**.
- **Ducking YOK:** konuşma başlangıcında müzik değişimi −2,7…+2,0 dB (8/8 konuşmalı videoda çökme yok). Ayrım **statik miks:** yatak sesin 2,8–11,9 LU (medyan ≈8) altında; uzun diyalog sahnelerinde duck yerine daha kısık/low-pass cue (v07 tünel: yatak enerjisi yalnız <1 kHz).
- **Müzik-kapalı ve sessizlik kuralları.** ≥1 sn gerçek sessizlik hikâye içinde 0–6 kez (medyan 1); **hepsi karar, hüküm ya da ifşa üstünde**: v07 1:08 (seçim, 4,0 sn), 6:47 (hükümden sonra, 4,1 sn); v08'de sessizlik yok ama kötü adamın son repliği için müzik çekilir; v03 "vardiyan 30 dk sonra başlıyor" bildirimi ve zorla gülümseme altında 2,6+5,4 sn; v10 faz kartlarında 4,6–5,6 sn; v02 hikâyeyi **11,2 sn sessizliğe** bitirir (yorumcular "sondaki sessizlik" der).
- **Bitiş kartı sesi sabit bir varlıktır:** v03–v07 ve v10'da **aynı** (r=0,93–1,00): 1,81 sn ölçülü mono davul-ağırlıklı döngü; v08 aynı döngüyü montaj yatağı yapar; v01/v09 hikâye müziğini karta taşır; v02 sessiz. Bitiş kartı 4/10'da tam 7,28 sn → sabit şablon klibi.
- **SFX.** Sözsüz filmler 0–0,5/dk (müzik her şeyi yapar). Konuşmalı 2,1–7,8/dk, her biri ekranda bir durum değişimine bağlı:
| SFX | Şekil | Nerede |
|---|---|---|
| UI tık/bildirim tiki | 6,7–7,3 kHz merkez, 50–120 ms | her telefon/devlet-bot kartı (v07 ×8), "Başvur" dokunuşu |
| Bildirim whoosh | 4,3 kHz gürültü, 0,4 sn | "YENİ SİPARİŞ" insert'i (v08 1:27) |
| Fikir/ödül çanı | tonal 1,6–2,7 kHz, 0,3–0,65 sn | fikir gülümsemesi, skor kazancı |
| Obje/kostüm "tok" | merkez 280–430 Hz, ≥%60 enerji <300 Hz, 0,1–0,5 sn | her giysi, şapka atma, kapı |
| Sub boom | merkez 60–110 Hz, 0,7–4 sn | perde arası siyahı, kötü adam ifşası, "mutlak cehennem", dron ifşası, son hüküm |
| Müzikal vuruş/riser | 1,1–2,2 sn sürekli | yeni mekâna giriş (v07 tünel 1:51) |
| Yazı tıkırtısı | 1,2–1,7 kHz, 20–70 ms patlamalar | şikâyet yazan biri |
| **(yok)** çarpma/çökme, ayak sesi, oda tonu, ambiyans yatağı | – | şiddet **sessizce atlanır** (v08 2:57) |
- **Sesler (8 konuşmalı video): sentetik (TTS), yüksek güven.** 5.343 kelimede 1 dolgu ("Um…" yazılı), diğer kekeleme yok; 2 yıla yayılan 8 videoda aynı **0,44–0,58 sn** replik arası boşluk; düz prozodi (erkek replikler 3,5–10 yarım ton aralık, protagonist ve "Chad" f0 ≈86–103 Hz); aksan hazır ayarları (kötü adam Fransız-vari, hizmetkâr Alman-vari; v09'da Sydney/Brooklyn aksanı karışıklığı 1.400 ve 759 beğeniyle dalga geçilir); yorumlar "bariz AI sesler", "voice bot ElevenLabs seviyesine yükseltilebilir", "devlet botları için daha robotik". Hız 151–204 WPM (tek kısa replik 225–320). Sistem karakterleri (Governbot, spor salonu AI) = kadın asistan sesi; yaptırım/devlet = perdesi düşürülmüş monoton. İşleme: kuru, seviye-sabit (anlık −15…−20 LUFS), reverb yok, oda tonu yok. Aksanlı antagonist replikleri **yakılmış beyaz altyazı** alır.

## 6. Değişmezler (≥8/10)
1. Hikâye sınır oranı **14–24/dk** (10/10), plan medyanı **2,3–3,6 sn** (10/10), p90 ≤7,7 sn (10/10).
2. İlk sınır ≤5,7 sn (10/10); 15–60 sn ≥16 sınır/dk (10/10).
3. Aksiyon/tepki planı >6,5 sn yok; >8 sn tutuşlar yalnız diyalog/monolog (10/10).
4. Karadan ≤1,2 sn fade-in ve yumuşak ilk 15 sn (≥2,8 LU kısık) (8/10).
5. Müzik hikâyenin ≥%85'inin altında (9/10); parça değişimi mekân/perde kesmesinde; **sidechain ducking yok** (8/8).
6. TTS sesleri, kuru, 150–205 WPM, 0,44–0,58 sn boşluk (8/8).
7. ≥1 sn sessizlik ≤6 kez ve yalnız karar/hüküm/ifşada (10/10).
8. Yavaş push-in süre'nin %13–47'sinde + yeni plan yerine yeniden kadrajlar (10/10).
9. Turuncu bitiş kartı 4,9–14,6 sn; 6/10'da sabit çıkış sesi.
10. En yüksek tekrar zirvesi hikâyenin %80–99'unda ifşa/ödeme karesinde (8/10); tekrar-izleme kesme yoğunluğundan bağımsız (10/10).

## 7. Aile varyasyonları
| Aile | Ritim | Ses |
|---|---|---|
| Doomer saga (v01, v04 sözsüz; v02 konuşmalı) | en hızlı ve eşit: 18–24/dk, max plan ≤10 sn, son 30 sn 14–24/dk; poz değişimi 13,8/dk'ya kadar "oyunculuğu" taşır | tüm film için tek duygusal şarkı, −10,5/−14,6 LUFS, 0–0,5 SFX/dk; v02: yumuşak ambient + mentor sesi, sessiz bitiş kartı |
| İş "Life of a…" (v03, v06, v08) | 16,5–21,6/dk; soğuk açılış sabah/ev rutini montajı (v06 0–15 sn 28/dk, başlık kartı 0:16); v06'da 14 sn'ye kadar diyalog tutuşu | komedi kütüphane cue + kötü adam/dövüş cue; en çok SFX (5,4–7,8/dk: UI, çan, tok); v08 en yüksek (−16,6) |
| Distopya (v05, v07, v09) | 14,2–21,1/dk; her 20–60 sn'de sistem UI insert'i; tek plakada yeniden kadraj/pan'li diyalog; v05/v09'da 14–17 sn tutuş | kadın sistem TTS + daktilo metni, dönüş perdesi için karanlık cue, hüküm üstünde sessizlikler |
| Bağımlılık (v10) | en yavaş açılış (0–15 sn 8/dk, siyah faz kartı), 20 sn siyah kart, 35 sn izolasyon tutuşu, son 30 sn 4/dk | en çok sessizlik (6 koşu ≥1 sn, süre'nin %15'i müziksiz), epik → metal → gergin cue'lar |

## 8. RİTİM SPEC'İ (3:30–7:30 hikâye için)
| Segment | Hedef | Not |
|---|---|---|
| 0:00–0:01,2 | karadan fade-in (≤1,2 sn); isteğe bağlı bulanık ön plan katmanının yan kayması | kesme sayılmaz |
| 0:00–0:15 | **16–24 sınır/dk** (4–6), ilk kesme 1,5–4,0 sn; geniş kuruluş → orta → yakın/insert | 0:03'ten önce diyalog yok; konuşmalı videolar 0:14–0:33'e kadar sözsüz kalabilir |
| 0:15–1:00 | **17–27/dk**, plan medyanı ≤2,6 sn | öncül resimlerle + ≤3 replik |
| Gövde — sözsüz olay örgüsü/pantomim | 22–32/dk, planlar 1,8–2,7 sn | |
| Gövde — montaj (iş döngüsü, dönüşüm) | 25–45/dk, planlar 1,1–2,5 sn, ≥3 tur | müzik ses seviyesine çıkar |
| Gövde — diyalog (≥%70 konuşma) | 10–14/dk, plan medyanı 4–5 sn; tek plaka, konuşmacıyı ≤10 sn'de bir yeniden kadraj/slayt ile değiştir; **tek mekân diyaloğu en çok 60 sn** ya da araya kes | |
| Monolog/ironi cümlesi | 1 plan 8–10 sn, ≤1,15× yavaş push-in | tek yasal >8 sn tutuş |
| Perde arası | hikâyenin %45–60'ında 4–6 sn siyah (veya ≤4 sn faz kartı) | sub vuruşu + yeni cue |
| Son 30 sn | 10–20/dk; tek 6–10 sn ifşa/pull-back ile bitir | |
| Bitiş kartı | 7,3 sn statik (aralık 5–15) | sabit şablon + sabit çıkış sesi (**kendi** döngümüz) |
| Dağılım kontrolleri | p10 1,3–1,6 · medyan 2,3–3,0 · ort 2,8–3,5 · p90 5–6,5 · max ≤10 · plan >8 sn ≤%3 · <1,5 sn %10–15 | |
| Kamera | süre'nin ≥%25'inde yavaş push-in; ≥30 sn'de 1 yeniden kadraj; poz değişimi 2–9/dk | |

## 9. SES TASARIMI SPEC'İ
| Madde | Hedef |
|---|---|
| **Ses seviyesi (karar)** | **−14 ±1 LUFS entegre, ≤−1,0 dBTP** hem konuşmalı hem sözsüz. *Gerekçe:* korpusun konuşmalı videoları −16,6…−22,5 LUFS ile kısık karıştırılmıştı (YouTube yaklaşık −14 LUFS'a göre normalleştirir; kısık miks rakibe göre sessiz kalır) ve %50'si kodlamadan sonra 0 dBTP'yi aşmıştı = [İYİLEŞTİRME]. QA: `rhythm_qa.py --target-lufs -14`. (Korpus normu −20 ±2 yalnız referans.) |
| LRA | 10–13 LU (sözsüz film ≈11) |
| Açılış | ilk 15 sn gövdeden 3–10 LU kısık (kısa-dönem); yalnız yatak/ambiyans, sonra ilk replik |
| Diyalog seviyesi | her TTS satırı sabit, kuru, reverb yok; yatak diyalogun **8 ±2 LU altında (statik; sidechain duck yok)**; >60 sn diyalogda yatağı ≈1 kHz'de low-pass et ya da sahne kesmesinde −3 dB |
| Müzik-yalnız vuruşlar | yatak diyalog seviyesine çıkar |
| Müzik rolleri | konuşmalı videoda 2–4 cue: komedi/muzip (kurulum) → idil/serin döngü (yolculuk, montaj) → karanlık/kötü adam (perde arasından sona); sözsüz: tüm film için tek duygusal enstrümantal 90–130 BPM. **Yalnız özgün ya da lisanslı parça.** |
| Cue değişimi | mekân/perde sert kesmesinde; karanlık cue siyah üstünde sub vuruşuyla (60–110 Hz, 1–1,5 sn) girer |
| Müzik-kapalı | video başına 1–3 pencere × 2–5 sn; karar/hüküm/kötü adam vuruşunda; sesle ya da boom ile devam |
| Sessizlik | video başına ≤6 koşu ≥1 sn; faz kartları dışında hikâye içinde >5 sn yok |
| SFX | konuşmalı 3–8/dk, sözsüz 0–1; her ekran durum değişimine bir tane: UI tık (6–7 kHz, ≤120 ms), bildirim whoosh (≈4 kHz gürültü, 0,4 sn), fikir/ödül çanı (1,6–2,7 kHz, 0,3–0,6 sn), obje/kostüm tok (<300 Hz), ifşada sub boom; ambiyans yatağı yok, ayak sesi yok; şiddet çarpma sesi olmadan atlanır |
| Sesler | TTS, rol başına ayrı hazır ayar (tartışan karakterler için ≥4 yarım ton farklı ya da farklı aksan — korpusta v07 protagonist+sürücü ≈95 Hz = zayıflık); 150–205 WPM; 0,4–0,6 sn boşluk; sistem/AI = kadın asistan sesi + daktilo metni; yaptırım = perdesi düşük monoton; aksanlı antagonist = yakılmış altyazı |
| Bitiş kartı sesi | her videoda aynı 7–8 sn imza çıkış döngüsü (**kendi** döngümüz), aynı kart |

## 10. QA script'i — `scripts/rhythm_qa.py`
```bash
python scripts/rhythm_qa.py VIDEO.mp4 --transcript words.json --mode voiced --out qa_out --target-lufs -14 --montage
```
Gereksinim: ffmpeg/ffprobe, numpy, Pillow (yalnız `--montage`). 96×54 @25 fps çözer; kesme/reframe/slayt-pan/eriyik/siyah tutuş saptar, bitiş kartını bulur, **yalnız hikâye** istatistikleri: sınır/dk (0–15, 15–60, gövde, son 30 sn, dakika başına), plan p10/medyan/ort/p90/max, `--hold` üstü tutuşlar, plan başına kamera sınıfı (push/pull/pan/statik), poz değişimi/dk; ses: LUFS, LRA, anlık yüzdelikler, sessizlik haritası, müzik-kapalı koşuları, ≥1 sn dramatik sessizlikler, SFX adayları; transkriptle: konuşma payı, ilk kelime, en uzun sözsüz, WPM, yatak-ses LU, ducking testi. `report.json`, `shots.csv`, `seconds.csv`, `montage_cuts.jpg` (insan kalibrasyonu için her sınırın önce/sonra çifti) yazar. 22 metriği korpus normlarıyla karşılaştırır (PASS = korpus aralığı, WARN = dışında, FAIL = çok dışında; **exit 1 = herhangi bir FAIL**). `--target-lufs N`: kendi hedefimiz (±1,5 PASS, ±4 FAIL). Süre ≈40–70 sn / 3–7 dk video.
**Test:** v08, v03, v07, v04 hepsi PASS (exit 0); v10 5 WARN (bilinen zayıf noktaları: 0–15 sn'de 8/dk, son 30 sn 4/dk, max plan 35 sn, 20 sn siyah); sentetik negatif test (90 sn tek durağan görüntü+ses) 11 FAIL, exit 1; sessiz klipte ses kontrolleri atlanır. **Orkestra doğrulaması:** v08'i `--target-lufs -14` ile yeniden koştum: 66 sınır, 19,3/dk — analistin sayılarıyla aynı; −16,6 LUFS WARN verdi (beklenen).

## 11. Anti-kalıplar [ölçüm]
1. Yeniden kadrajsız >60 sn tek mekân diyaloğu (v07 araba 97,7 sn @14/dk → en düşük tekrar platosu; v05/v06/v09/v10 13–35 sn tutuşlar).
2. Açılışı siyah faz kartıyla yapmak (v10: 0–15 sn'de 8/dk; toplam 20 sn siyah).
3. Karttan önceki 30 sn'yi 4 sınır/dk ile bitirmek (v10).
4. Altyazısız, sesin altında <4 LU yatak (v08 2,8 LU; aksanlı kötü adamı için altyazı şart oldu).
5. Kodlama sonrası taşma >0 dBTP (5/10).
6. Skor olarak ticari şarkı (v01/v04): erişime yarar ama gelir/telif için güvensiz.
7. İki tartışmacıda aynı tonda TTS sesler (v07 ≈95 Hz).
8. Sidechain pompalaması ya da oda tonu — korpus hiç kullanmaz; düz "meme çizgi roman" sesini bozar.

## Why it works
- Kurgu bir **çizgi roman kadansıdır:** her 2,3–3,6 sn'de yeni kare; çizimler yeniden kadrajlar ve push-in'lerle yeniden kullanılır → görüntü hızlı değişir, sanat bütçesi düşük kalır.
- Ritim kulağı izler: TTS diyalog anlam taşıyorsa kesme hızı yarıya (12 vs 18/dk), resim taşıyorsa ikiye katlanır → dikkat bölünmez.
- Ses mimaridir, süs değil: neredeyse sürekli bir yatak her perdenin ruh hâlini kurar, cue'lar perde kesmelerinde değişir, nadir çıkarmalar (müzik-kapalı, 1,5–5 sn sessizlik) karar ve hükümleri işaretler.
- Sentetik sesler kanalın kabul görmüş geleneğidir (hatta şakası) ve üretimi ucuz/tutarlı tutar.
- Tekrar-izleme ifşa karelerinden ve sona yakın okunan metinden gelir, hızlı kesmeden değil — **ritim izleyiciyi tutar, ifşa onları geri sardırır.**

## Rules to copy
1. [KOPYA] Her hikâyeyi 16–22 sınır/dk'ya kur (korpus 14–24), plan medyanı 2,3–3,0 sn, p90 ≤6,5 sn, hikâyede max plan ≤10 sn; reframe/slayt-pan'ı sınır say, `rhythm_qa.py --montage` ile doğrula.
2. [KOPYA] 0:00–0:15'te 16–24/dk, ilk kesme ≤4 sn; 0:15–1:00'da ≥17/dk; ≤1,2 sn fade-in ve yumuşak ilk 15 sn (gövdeden 3–10 LU kısık).
3. [KOPYA] Beat kesme hızını konuşma yoğunluğuna göre ayarla: sözsüz olay örgüsü 22–32/dk, montaj 25–45/dk, diyalog (≥%70 konuşma) 10–14/dk ve ≤10 sn'de bir yeniden kadraj.
4. [KOPYA] >8 sn tutuşa yalnız monolog/ironi cümlelerinde izin ver (8–10 sn, yavaş push-in); aksiyon/tepki planı >6,5 sn olmasın.
5. [KOPYA] Perde arasını hikâyenin %45–60'ına 4–6 sn siyah (veya ≤4 sn faz kartı) + sub vuruşu + yeni, daha karanlık cue ile koy.
6. [KOPYA] En güçlü ifşayı — mümkünse okunur ekran yazısıyla — hikâyenin %80–95'ine koy ve bitiş kartından önce tek 6–10 sn tutuşla izle.
7. [KOPYA] Müzik hikâyenin ≥%85'inin altında, konuşmalı videoda 2–4 cue (komedi → idil → karanlık); diyalog altında statik yatak 8 ±2 LU, **ducking yok**; >60 sn diyalog sahnelerinde low-pass ya da −3 dB.
8. [KOPYA] 1–3 karar/hüküm/vuruş anında müziği 2–5 sn çıkar; video başına ≤6 gerçek ≥1 sn sessizlik.
9. [KOPYA] SFX yalnız durum değişimlerine (UI tık, bildirim whoosh, fikir çanı, obje tok, sub boom): konuşmalı videoda 3–8/dk, sözsüz müzik filmlerinde yok; ambiyans yatağı yok.
10. [KOPYA] TTS kadrosu: rol başına ayrı ses, 150–205 WPM, 0,4–0,6 sn boşluk, kuru; aksanlı antagonist için altyazı; her "sistem" için kadın asistan sesi + daktilo metni.
11. [KOPYA] Aynı turuncu-aile bitiş kartı ve aynı 7–8 sn imza çıkış döngüsü her yüklemede [İYİLEŞTİRME: kendi döngümüzü ve kart tasarımımızı yap].
12. [İYİLEŞTİRME] Her videoyu **−14 ±1 LUFS, LRA 10–13 LU, ≤−1,0 dBTP**'ye mastırla (korpus kısık ve taşmalıydı).
13. [İYİLEŞTİRME] Tek mekân diyaloğunu 60 sn ile sınırla; ilk 15 sn'de siyah faz kartı kullanma.
14. [ETİK] Yalnız özgün ya da lisanslı müzik — v01/v04'teki ticari şarkı/cover'lar ve kanalın çıkış döngüsü asla; aynı rolleri dolduran özgün karakterler, insertlerde gerçek kişi/marka/haber başlığı yok.

## Open questions
Hangi kredili parça hangi cue (örn. v07'de "Sneaky Snooper" mı "Brain Trust" mı) → insan dinleme geçişi gerekir · sabit çıkış döngüsü kredili "Milk Coffee" mi yoksa imza mı · izlenme–kesme hızı korelasyonu (ρ=+0,56, n=10) yıl ve konuyla karışık, 148 videoluk tam kanalla test edilmeli · TTS satıcısı/ses kimliği sesten çıkarılamaz (yalnız "sentetik, hazır aksan ayarları").
