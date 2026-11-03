# B — Hook + Senaryo Motoru ("What If" animasyon nişi) — 2026-10-28

Veri: 20 video (10 hit ≥100K, 10 flop), 18 İngilizce transkript (YouTube auto-caption, NexLev), 2 sessiz video (Hour Seven; ekran metni 1 fps karelerden okundu), 1 Danca video (K01r4f2PJN4). Ölçümler: `scratchpad/whatif/stats.json` (`scripts/stats.py`), yapısal kodlama `scratchpad/whatif/coding.csv`. Video başına notlar: `B-transcript-notes/<id>.md`. Heatmap: 11 paketin hepsinde `null` (videolar <2 hafta) — tekrar-izleme zirvesi kullanılamadı.

## Özet (10 madde)

1. **Hit'lerin 10/10'unda ilk somut mucize/tehdit ≤15 sn** (medyan 6.5 sn); flop'larda 6/10 (medyan 12 sn; Tesla 60 sn, Water 28 sn). İlk sahne her iki grupta da 0. saniyede başlıyor — fark "sahne var mı" değil, **"sahnenin içinde kural ihlali ne zaman"**.
2. **Kural ≤60 sn'de ve tek cümle**: hit'lerde 9/10 (medyan 30 sn), flop'larda 5/9 (medyan 60 sn). Kuralı 2+ madde + metaforla anlatan 3 video (Erase 115 sn, Water 96–190 sn, Partners 200 sn, ikisi sonradan yeniden tanımlıyor) flop.
3. **"So what if…" sorusu** hit'lerde medyan 26 sn (6/7 ≤45 sn), flop'larda 42 sn (3/6). Soru her zaman **sahneden sonra** geliyor; asla açılış cümlesi değil (tek istisna başlık cümlesiyle açan Readout formatı).
4. **Karanlık vaat** ("by the end of this video…", "you're going to wish…") hit'lerin 7/10'unda, 28–45 sn arasında; flop'larda 4/10 ve geç (42–170 sn).
5. **İlk karanlık dönüş** hit'lerde medyan %37.5 (aralık %17–53), flop'larda %46 (aralık %13–70). İki ConChaser flop'u %60 ve %70 — en geç ikisi.
6. **Süre**: hit medyanı 8:17 (4:57–10:48), **hiçbir hit ≥11 dk değil**; flop'ların 4/10'u 11:13–14:55. Aynı kanal çiftlerinde flop hep daha uzun (ConChaser 14:55/13:01 vs 10:48; Jeremy 13:40 vs 6:17/4:57; Miko 11:13 vs 10:10).
7. **Dil ölçüleri grupları ayırmıyor**: "you"/100 kelime 8.1 vs 8.2, rakam/100 2.2 vs 2.3, ilk 10 sn kelime 30 vs 29. Ayıran: WPM (167 vs 148) ve medyan cümle (5 vs 6 kelime) — hit'ler daha hızlı ve kısa cümleli. Dil "giriş bileti", "fark yaratan" değil.
8. **Premise tipi**: hit'lerin 5/10'u vücut-temelli fiziksel (ölümsüz, kalp, acı, nefes, ıskalamamak), 3/10 sosyal-bilgi gücü (servet, yalan sayısı, nefret), 1 anlaşma-kovalamaca (meme), 1 ölçek. Flop'larda 3 klasik süper güç (elektrik, su, silme), 1 marka (Tesla), 1 zaman döngüsü, 2 ölçek, 3 sosyal. **İzleyicinin kendi bedeninde/ilişkisinde test edebildiği premise'ler tutuyor; "waterbending" tipi süper güçler tutmuyor** (düşük-orta güven, n küçük).
9. **Aynı kanal çiftleri senaryo zanaatının eşit olduğunu gösteriyor** (aynı yazar sesi, ritim, bilim dozu, CTA yeri). Farkı açıklayan: (a) premise'in tek karede anlaşılırlığı ve arzu edilirliği, (b) süre/sahne ekonomisi, (c) 2 durumda **paketleme-dışı neden** (Readout flop'u Danca seslendirme; Iflord flop'u 1 günlük). Hour Seven çifti (sessiz format) tek "saf senaryo" kıyası: karar + kişisel bedel + ironi olan tutuyor, trivia listesi tutmuyor.
10. **Bitiş**: hit'lerin 9/10'u "Would you…?" sorusuyla bitiyor (7'si + subscribe); 1'i (Readout) soru/CTA'sız rüya-sıfırlama. CTA sayısı başarıyı belirlemiyor (Future Wealth 482K: sıfır CTA). Orta-video CTA (%43–55) hit'lerin 5/10'unda var ve hep bir soru/ödül cümlesine sarılı.

## Bulgular

### Tablo 1 — 20 video ölçümleri (transkript; sessiz/Danca videolar işaretli)

| id | kanal | hit | izlenme | süre | kelime | WPM | you/100 | med. cümle | rakam/100 | ilk 10 sn kelime | ilk mucize (sn) | "what if" sorusu (sn) | kural (sn) | karanlık vaat (sn) | ilk karanlık % | zaman sıçr. | CTA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M_t2ZUz7_pc | Iflord | 1 | 656K | 8:45 | 1176 | 137 | 7.6 | 6 | 2.2 | 18 | 12 | 24* | 24 | 32 | 43 | 11 | 3 |
| rvyd0ylInfY | Jeremy B. | 1 | 584K | 6:17 | 1062 | 170 | 8.0 | 5 | 2.2 | 31 | 7 | 44 | 48 | – | 46 | 1 | 1 |
| rLCVK9llntQ | Hour Seven | 1 | 568K | 7:46 | sessiz (~105 ekran satırı) | ~60 eşd. | – | ~6 | – | – | 10 | 5 ("Accept the deal?") | 10 | 28 | 17 | 23 | 1 |
| DK4EOHCrVvM | ConChaser | 1 | 482K | 10:48 | 1793 | 167 | 8.9 | 5 | 4.8 | 30 | 6 | – | 111 | 38 | 45 | 1 | 0 |
| MGZdDZyQUGg | Miko | 1 | 460K | 10:10 | 1739 | 172 | 8.3 | 5 | 2.5 | 29 | 1 | 26 | 6 | 31 | 21/85 | 10 | 2 |
| JSl2v4lH4Y4 | Jeremy B. | 1 | 364K | 4:57 | 844 | 171 | 9.7 | 5 | 1.3 | 31 | 2 | 25 | 26 | – | 28 | 1 | 1 |
| jJCQG4Actqk | Iflord | 1 | 345K | 8:11 | 1173 | 146 | 6.2 | 6 | 2.9 | 34 | 15 | – | 34 | 36 | 53 | 6 | 1 |
| ggRf0ZYzrr8 | Ifsphere | 1 | 226K | 9:09 | 1640 | 180 | 7.0 | 6.5 | 2.7 | 35 | 4 | 36 | 40 | 45 | 40 | 8 | 2 |
| nOheMXyWXGg | Ifquirky | 1 | 223K | 8:22 | 1220 | 148 | 9.1 | 5 | 2.0 | 23 | 0 | 66 | 58 | 126 | 35 | 3 | 2 |
| x3Pb_x6bq6E | The Readout | 1 | 158K | 7:37 | 712 | 94 | 8.1 | 6 | 1.0 | 5 | 15 | – | 0 | – | 31 | 0 (25 ölçek basamağı) | 0 |
| uVUDl0qUpXo | Miko | 0 | 23K | 4:57 | 828 | 169 | 9.1 | 6 | 2.5 | 28 | 60 | 11 | 20 | – | 45 | 6 | 1 |
| A2qgnQC-ZQA | Miko | 0 | 21K | 11:13 | 1952 | 174 | 7.3 | 6 | 1.7 | 32 | 19 | 58 | 115 | – | 38 | 2 | 2 |
| 7jLDdD-uIEQ | Iflord | 0 | 3.5K (1 gün) | 8:36 | 1258 | 148 | 6.3 | 6 | 1.8 | 33 | 9 | 27 | 31 | 42 | 50 | 5 | 1 |
| L3PPO4MdLyY | ConChaser | 0 | 12K | 14:55 | 2308 | 155 | 9.9 | 6 | 2.5 | 35 | 6 | 22 | 100 | 65 | 70 | 7 | 0 |
| grnsQxRNEII | ConChaser | 0 | 23K | 13:01 | 1925 | 148 | 9.8 | 5 | 0.9 | 25 | 0 | – | 200 | 45 | 60 | 1 | 0 |
| K01r4f2PJN4 | The Readout | 0 | 17K | 9:01 | **Danca** 780 | 87 | – | – | – | 25 | 13 | – | 0 | – | 34 | 0 | 0 |
| gukICwORPZo | Hour Seven | 0 | 7.8K | 8:21 | sessiz (~55 satır) | – | – | ~7 | – | – | 20 | – | – | – | 13 | 0 (derinlik sayacı) | 0 |
| nHLPOEAvx8c | Ifquirky | 0 | 26K | 8:31 | 1230 | 146 | 10.2 | 5 | 2.5 | 30 | 3 | 71 | 60 | – | 47 | 4 | 2 |
| E6jt1aVSQ00 | Alternate You | 0 | 8.7K | 9:37 | 1218 | 128 | 4.6 | 7 | 7.9 | 21 | 11 | – | 30 | – | 50 | 20+ | 0 |
| 80ZDrI4AN64 | Jeremy B. | 0 | 10K | 13:40 | 1996 | 146 | 6.9 | 7 | 2.1 | 25 | 28 | 94 | 96 | 170 | 45 | 2 | 1 |

\* Immortal'da soru yok; 24. sn'de "Congratulations, you're immortal" ilanı. "–" = yok.

### Tablo 2 — Hit vs flop medyanları (coding.csv + stats.json)

| metrik | HIT medyan | FLOP medyan | yorum |
|---|---|---|---|
| süre | 8:17 | 9:19 | hit max 10:48; flop 4/10 ≥11 dk |
| ilk mucize/tehdit | 6.5 sn | 12 sn | hit 10/10 ≤15 sn; flop 6/10 |
| "what if" sorusu | 26 sn | 42.5 sn | hit 6/7 ≤45 sn; flop 3/6 |
| kural cümlesi | 30 sn | 60 sn | hit 9/10 ≤60 sn; flop 5/9 |
| karanlık vaat | 36 sn (7/10 var) | 55 sn (4/10 var) | |
| ilk karanlık dönüş | %37.5 | %46 | |
| zaman sıçraması sayısı | 4.5 | 3 | |
| mizah (ilk 3 dk) | 3.5 | 3.5 | ayırmıyor |
| CTA sayısı | 1 | 0.5 | ayırmıyor |
| WPM (EN, n=9 vs 8) | 167 | 148 | |
| "you"/100 kelime | 8.1 | 8.2 | ayırmıyor |
| medyan cümle (kelime) | 5 | 6 | |
| rakam/100 kelime | 2.2 | 2.3 | ayırmıyor |
| ilk 10 sn kelime | 30 | 29 | ayırmıyor |
| ölüm/yaralanma riski var | 8/10 | 8/10 | ayırmıyor |
| açık ders var | 6/10 | 6/10 | ayırmıyor |

### Tablo 3 — Aynı kanal çiftleri: senaryo mu paketleme mi?

| kanal | hit | flop | ölçülen senaryo farkı | sonuç (güven) |
|---|---|---|---|---|
| ConChaser | Future Wealth 10:48, 482K | Days Left 14:55, 12K · Partners 13:01, 23K | Yapı birebir (in medias res → sabah flashback → gag vinyetleri → "sayılar tahmin" → kahramanlık → bedel). Flop'lar +20–38% uzun; karanlık %70/%60 vs %45; Days Left'te 4 dk tek mekân (büyükanne evi 5:30–9:30); Partners'ta kural 2 kez yeniden tanımlanıyor (%25, %80) ve rakam/100 0.9 vs 4.8. | Yarı senaryo (süre, sahne ekonomisi, kural tasarımı) yarı paketleme (servet = arzu, ölüm günü = keder, partner sayısı = reklam riski). Orta güven. |
| Miko | Lie Count 10:10, 460K | Erase 11:13, 21K · Tesla 4:57, 23K | Aynı yazar sesi, aynı %50 CTA, aynı bilim dozu. Lie Count 1. sn'de ihanet + 6. sn'de tek cümle kural. Erase: 60 sn bağlamsız flash-forward, 3 kural + 2 metafor (%17–28), tür değişimi (%55'ten sonra gizli teşkilat). Tesla: mucize 60 sn'de, kurallar bürokratik (FAA, 254 lb), %65'te gerçek haber özeti. | Fikir + paketleme ağırlıklı; Erase'te kural yükü senaryo hatası. Orta güven. |
| Hour Seven (sessiz) | Immortal Snail 7:46, 568K | Sank 8:21, 7.8K | Tek "saf senaryo" kıyası (format, kanal, hafta sabit). Snail: 5. sn'de "Accept the deal?", 3 numaralı kural, "What could go wrong", kişisel bedel ("friends get older", "moved 200 times"), 23 yıl damgası, YES/NO sorusu. Sank: karar yok, kural yok, 45/55 satır belgesel trivia, soru/CTA yok. | **Senaryo içeriği** (karar + bedel + ironi) + premise meme gücü. Orta-yüksek güven. |
| The Readout | Brighter 7:37, 158K | Charged Up 9:01, 17K | Aynı 7 perdelik şablon (ev → sokak → şehir → gezegen → uzay → "Wait"). **Flop'un sesi/altyazısı Danca** (caption listesi da/sv/nl/fi…, İngilizce yok; Whisper dil tespiti İskandinav). | Dil/dağıtım; senaryo kıyası geçersiz. Yüksek güven. |
| Jeremy Bearimy | Heart 6:17, 584K · Pain 4:57, 364K | Water 13:40, 10K | Hook'ta tehlike yok (yağmur kubbesi), soru 1:34'te (vs 0:44/0:25), kural 105 sn + duygu haritası, medyan cümle 7 (vs 5), 2–3 kat uzun. | Senaryo kaynaklı (hook + kural yükü + süre). Orta-yüksek güven. |
| Ifquirky | Secretly Hates 8:22, 223K | Dreams 8:31, 26K | Yapı, ritim, bilim, cliffhanger, part-two CTA **aynı**. Fark: izleyicinin kazanacağı güç yok (rüya = sadece utanç); kriz premise'den organik değil. | Fikir + paketleme. Orta-yüksek güven. |
| Iflord | Immortal 656K · Never Missed 345K | Electricity 3.5K (1 günlük) | Aynı Max sidekick, Day 1/2/3, planted-payoff; hook daha hızlı (9 sn). | Erken; 7 gün sonra tekrar ölç. Düşük güven. |

## Neden çalışıyor

- **"Ben olsam" simülasyonu**: 2. tekil şahıs + izleyicinin kendi bedeninde/ilişkilerinde deneyebileceği güç. Kalp, acı, nefes, ıskalamamak, yalan sayısı, nefret rengi — hepsi "sınıfta, evde, otobüste ne olurdu" diye anında hayal edilebiliyor. Su bükme, elektrik, silme ise süper kahraman fantezisi; izleyici kendini değil bir karakteri izliyor.
- **Kural ihlali ilk 15 sn'de, kural cümlesi ilk 30 sn'de**: izleyici önce anomaliyi görüyor (kamyon çarptı, çizik yok), sonra kuralı duyuyor. Ters sıra (önce açıklama) flop'larda (Same Day 80 sn fizik, Water 105 sn kural).
- **Karanlık vaat = tutma sözleşmesi**: "Sounds amazing, right? By the end of this video immortality is going to look very different" (M_t2ZUz7_pc 32 sn). İzleyici bedeli bekliyor; her komik avantaj sahnesi aynı zamanda "ne zaman çökecek" gerilimi taşıyor.
- **Tırmanma iki eksende**: ölçek (okul → şehir → ülke → gezegen → evren) ve bedel (komik → sosyal → fiziksel → duygusal → varoluşsal). Zaman damgaları (Day 1 / Week 1 / Year 10 / Year 10,000) her 30–60 sn'de "sonraki bölüm" vaadi veriyor; Immortal 11, Snail 23 damga.
- **Bilim = silah**: hit'lerde her bilim parçası ≤40 sn ve sonraki sahnede kullanılıyor (1-10-1 kuralı → nehir kurtarması; rip current → plaj; güvercin → düşen hat). Flop'larda bilim süs (Same Day: atom saati, yörünge; Sank: 45 trivia).
- **Planted & payoff**: bıçak torpido gözünde (ggRf 2:05 → 7:05), düdük 3 blast (nOhe 4:10 → 5:12), Max'in "snacks" (M_t2 2:45 → 7:51). İzleyici farkına varmadan ikinci bir "tamamlanmamış döngü" taşıyor.
- **Bitiş sorusu = yorum motoru**: "Would you…?" + ikili seçenek (YES/NO; "zengin ol / başkasının geleceğini değiştir"). Snail'de 400 yorumun çoğu YES/NO + loophole tartışması.

## Kopyalanacak kurallar (ölçülebilir, emir kipi)

1. İlk somut sahneyi 0. saniyede başlat; ilk kural ihlalini (mucize/tehdit) **≤15 sn**'de göster.
2. Kuralı **tek cümleyle ≤30 sn**'de söyle ("Can't get sick, can't get hurt, never age"); istisnayı ("except…") ikinci cümleye koy; **video boyunca kuralı yeniden tanımlama**, sadece istisna ekle.
3. "Ya … olsaydı?" sorusunu **sahneden sonra, 20–45 sn** arasında sor; açılış cümlesi yapma.
4. **28–45 sn** arasında karanlık vaat ver ("videonun sonunda bunu istemeyeceksin").
5. İlk karanlık dönüşü **%30–45**'te koy; %55'ten sonraya bırakma.
6. Toplam süre **6–10 dk**; 11 dk'yı geçme. Tek mekânlı sahne **≤60 sn**.
7. Her 30–60 sn'de bir **zaman damgası veya ölçek basamağı** (≥6 damga/8 dk).
8. Her bilim vuruşu **≤40 sn** ve en geç 3 dk içinde bir sahnede **kullanılmalı** (silah/çözüm/bedel).
9. En az **2 planted-payoff** çifti (mesafe ≥3 dk).
10. İlk 3 dk'da **≥3 mizah vuruşu**; kriz sahnesinde (son %30) mizahı 1'e düşür, rahatlatıcı gag'ı krizin hemen sonrasına koy ("He's just hibernating").
11. WPM **150–175**; medyan cümle **≤6 kelime**; "sen/siz" yoğunluğu ≥7/100 kelime (TR karşılığı için §10).
12. Bitişi **ikili soruyla** kapat; subscribe çağrısı soruya sarılı ve ≤10 sn.
13. Premise testi: izleyici gücü **kendi bedeninde veya günlük bir ilişkisinde** 5 sn içinde hayal edebiliyor mu? Edemiyorsa (süper kahraman gücü, marka, zaman döngüsü) premise'i değiştir.
14. Karakter kadrosu: sen + 1 isimli yakın (sidekick/kardeş/sevgili) + 1 otorite (doktor/koç/ajan) + 1 yabancı. Fazlasını ekleme.

---

## (2) Hook formülü — ilk 30 sn şablonu (saniye bütçeli, 10 hit'ten ölçüldü)

| sn | bütçe | iş | ölçülen örnekler |
|---|---|---|---|
| 0–3 | 3 sn, 6–10 kelime | **Sıradan an + sen**. Zaman/mekân tek cümle: "Sıradan bir salı. Karşıdan karşıya geçiyorsun." Mekân izleyicinin bugün bulunduğu yer (sınıf, otobüs, havuz, mutfak). | M_t2 0:00, jJCQ 0:00, nOhe 0:00, ggRf 0:00 |
| 3–10 | 7 sn, 15–20 kelime | **Kural ihlali** (mucize ya da tehdit): kamyon çarpar/çizik yok; kâğıt top 4 sekmeyle çöpe; evsizin başında 8 milyar. Caption boşluğu bırak (M_t2 5→10 sn) — görsel vuruş. | M_t2 5–12, rvyd 7, DK4E 6, MGZd 1, JSl2 2, ggRf 4 |
| 10–20 | 10 sn, 25 kelime | **Tanık tepkisi + kontrast cümlesi**: bir yan karakter sorar ("Bro, how did you do that?"), anlatıcı kontrastı çivileyer ("truck is dented, you're not"; "20 phones pointed at you"). | M_t2 15–21, jJCQ 19, rvyd 18, ggRf 18–23 |
| 20–30 | 10 sn, 25 kelime | **Kural ilanı, tek cümle** + "Kulağa harika geliyor, değil mi?" tonu. Rakamla kıyas varsa buraya (70 vs 700 bpm; 1 dk vs 5 dk; 9,317 yalan). | M_t2 24–30, JSl2 20–26, rvyd 38–44, nOhe 0–30 (renk kuralı örnekle) |
| 30–45 | 15 sn, 35 kelime | **Soru + karanlık vaat**: "Peki ya … olsaydı? Videonun sonunda bunu hiç istemeyeceksin." (veya in medias res'te: "9 gün önce ikisine de inanırdın") | M_t2 32–40, jJCQ 34–40, DK4E 38–45, MGZd 19–31, ggRf 36–45 |

Kelime bütçesi: ilk 10 sn **25–35 kelime** (hit medyanı 30), ilk 30 sn **65–100** (medyan 71). Readout formatı istisna (5 kelime + sessizlik) — yalnızca "…ve duramazsın" ölçek formatı için.

**İki açılış varyantı (hit'lerde 5/5 dağılım):**
- **A. Kronolojik** (Immortal, Heart, Pain, Never Missed, Breathe): gün 0, ilk mucize, kural, vaat.
- **B. In medias res** (Lie Count, Future Wealth, Secretly Hates, Snail kısmen): en çarpıcı andan başla (ihanet, 8 milyar), 30–50 sn'de "Here's how it started / this morning…" ile geri sar. B'de karanlık vaat zaten açılış sahnesi; ek vaat cümlesi %7'de ("by the end of the week you're going to wish…").

**Anti-kalıplar (flop'lardan):** açılışta fizik dersi (Same Day 0:30–1:20), bağlamsız şiddet (Erase 0–60 sn), markalı nesne satın alma (Tesla), tehlikesiz mucize (Water yağmur kubbesi), "Now imagine waking up…" tipi anlatıcı özeti (Days Left 22 sn).

## (3) 10 vuruşluk ana şablon — 8–10 dk (480–600 sn) video

| # | % | süre (8 dk / 10 dk) | amaç | mekanizma / örnek |
|---|---|---|---|---|
| 1 | 0–7 | 35 / 42 sn | **Hook** (§2): sahne → ihlal → tanık → kural → soru+vaat | M_t2 0:00–0:40; MGZd 0:00–0:36 |
| 2 | 7–15 | 40 / 50 sn | **Mekanizma + bilim #1**: "Here's how it works" — 1 benzetme + 1 gerçek hayvan/insan vakası + 1 rakam | telomer/jellyfish (M_t2), sinek kuşu kalbi (rvyd), motor noise + Curry 9/10 (jJCQ) |
| 3 | 15–28 | 60 / 80 sn | **Avantaj montajı ("At first it's amazing")**: 4–6 mini sahne, her biri 10–15 sn, ölçek büyüyerek (ev → okul → şehir → ülke); 2–3 gag; zaman damgası "Day 1 / Week 1" | rvyd 1:25–2:30 (5 sahne), jJCQ 1:25–3:10, DK4E 0:50–3:10 (8 vinyet) |
| 4 | 28–38 | 50 / 60 sn | **Sosyal kanıt / ölçek zirvesi**: viral video, teklif, rekor, uzman testi ("Error, heart rate too high") | rvyd 2:30 hastane; jJCQ 3:12 100 atış; ggRf 1:30 3M görüntülenme; MGZd 5:53 "polygraph" |
| 5 | 38–48 | 50 / 60 sn | **"And there's a cost" — ilk karanlık dönüş**: fiziksel ya da sosyal bedel; bilim #2 bedeli açıklar | rvyd 2:50 torpor; nOhe 2:55 self-fulfilling prophecy; jJCQ 4:20 "I kind of miss missing"; DK4E 4:53 sayı düşer |
| 6 | 48–57 | 45 / 55 sn | **Bedel derinleşir + planted ögeler**: yakın kişi etkilenir (Max yaşlanır, Mia kırmızı, Noah ihmal), kural/istisna #2 (1-10-1, "never why"), orta-video CTA buraya sarılı | M_t2 4:07 CTA + 4:20 Max; ggRf 4:30–5:25; nOhe 3:55–4:52 |
| 7 | 57–70 | 65 / 80 sn | **Kriz kurulumu**: zaman sıçraması ("3 years later", "Friday, April, rain"), tehdit başkasına (çocuk, kardeş, arkadaş), geri sayım/saat ("10 good minutes", "4 minutes is too long") | rvyd 3:35 Alpler; JSl2 3:10 yangın; ggRf 5:25 kamyon; nOhe 4:52 plaj |
| 8 | 70–85 | 70 / 90 sn | **Kriz çözümü = gücün bedeliyle birlikte kullanımı**: planted öge payoff (bıçak, düdük, güvercin, lastik eldiven); kahraman kendi bedelini öder (çöker, donar, dibe batar) | ggRf 6:20–7:35 dakika sayacı; JSl2 3:27–4:05 "look at your hands"; nOhe 6:10–6:50 |
| 9 | 85–95 | 50 / 60 sn | **Ders / anlam + rahatlatıcı gag + ödül**: tek cümlelik ders (vaaz yok), callback (snacks; "came up for air"), yeni kapı (Mars, bilim, part two) | M_t2 7:35 "special because it didn't"; rvyd 5:22 Mars; jJCQ 7:50 |
| 10 | 95–100 | 25 / 30 sn | **İkili soru + CTA (+ cliffhanger opsiyonel)**: "Sen olsan … mı, yoksa … mı? Yorumlara yaz." + "haftaya yeni what if" | DK4E 10:26; MGZd 9:52; nOhe 7:45 cliffhanger + 8:05 CTA |

Uzun ölçek-formatı (Readout/Snail tipi) için şablon farklı: hook (başlık cümlesi + sessizlik) → 7 perde (ev → sokak → şehir → gezegen → yıldız → galaksi → "Wait"), her perde 60–70 sn, 25+ kıyas basamağı, bitiş sıfırlama.

## (4) Tırmanma merdiveni kuralları

- **Basamak sayısı**: 8 dk için **8–12 basamak** (hit medyanı 4.5 açık zaman damgası + 4–6 ölçek/sahne basamağı). Immortal 11 yıl damgası, Snail 23, Never Missed 6 ("Day 1 / Week 1 / Month 1 / 3 / 6"). 3'ten az damga olan hit yok (Readout hariç — orada 25 ölçek basamağı).
- **Her basamakta tek değişken büyür**: ya **ölçek** (kaç kişi görüyor: sınıf 30 → okul → 12,000 stadyum → 10M canlı yayın → gezegen), ya **zaman** (gün → hafta → yıl → 10 yıl → 10,000 yıl), ya **bedel** (sosyal utanç → yalnızlık → fiziksel hasar → ölüm riski → anlam kaybı). İki değişkeni aynı basamakta büyütme (Erase'te hem kural hem tür değişiyor → kafa karışıklığı).
- **Sıra** (hit'lerde 8/10 aynı): **komik-fiziksel test → sosyal avantaj → sosyal maliyet → fiziksel tehlike (başkasına) → kendi bedenine bedel → duygusal/varoluşsal → ders**. Sosyal→fiziksel→varoluşsal sırası korunuyor; fiziksel tehlike hiç yoksa (Partners, Same Day) flop.
- **Logaritmik büyüme**: her basamak öncekinin ×3–×10'u (Year 1→10→40→70→120→500…; $100→$13K→$4T; 3kV→10kV→100kV→1MV). Lineer artış (Days Left: 400 gün, 2,000 gün) düz hissettiriyor.
- **Zaman damgası ekrana ve sese birlikte** (Snail HUD "Year 10 / SNAIL 4,000 mi"; Immortal chapters "Year 70: Max"). TTS'te damga tek başına cümle: "Onuncu yıl."
- **Mikro-merdiven krizde**: kriz sahnesinde dakika/metre sayacı (ggRf "Minute one… Minute ten"; rvyd "50 m, 30, 10"; uVUD "10…0" batarya). Kriz süresi 60–90 sn, sayaç 5–10 adım.
- **Geri sayım ile ileri sayımı eşleştir**: avantaj bölümünde sayılar büyür, kriz bölümünde küçülür (batarya %11→0, 10 dakika → kollar durur).
- **Son basamak hep ironi/döngü**: salyangoz tek sadık varlık; "Round two"; ateş böceği; "the hungriest thing… everybody hovers". Düz ders cümlesiyle bitirme.

## (5) 50 vuruşluk özgün vuruş bankası

Kullanım: her vuruş bir sahne cümlesidir; köşeli parantez şablondaki (§3) yuvayı gösterir. Hiçbiri mevcut videolardan kopya değildir; mekanizma tipleri hit'lerden çıkarıldı.

### A. Sosyal bilgi gücü (başkasının üstünde sayı/renk/etiket görürsün) — 13
1. [#1] Ev sahibinin başındaki sayı, kira zammını söylemeden önce artıyor — zammı ondan önce biliyorsun.
2. [#3] Öğretmen "Kim gönüllü?" diyor; herkesin etiketini gören tek kişi sensin, gönüllüyü sen seçiyorsun, öğretmen sana bakıyor.
3. [#3] İş görüşmesinde mülakatçının etiketi sen konuşurken değişiyor; cümlenin ortasında yön değiştiriyorsun (canlı geri bildirim gag'ı).
4. [#3] Düğünde 200 etiketi okurken pastayı devirmek üzere olan kuzeni kaçırıyorsun (komik bedel).
5. [#4] Bir yayıncı "canlı yayında 100 yabancıyı oku" teklifi getiriyor; 99. kişide durup okumamayı seçiyorsun.
6. [#5] En yakın arkadaşının etiketi 3 gündür değişmiyor; güç ilk kez sana bir şey söylemiyor — boşluk korkutucu.
7. [#5] Kendi etiketini göremiyorsun: ayna, vitrin, telefon ekranı boş (kör nokta = gerilim).
8. [#6] Etikete göre davrandıkça 2 hafta sonra herkesin etiketi sana göre değişmiş — kendi kendini gerçekleştiren kehanet.
9. [#6] Annenin etiketi yıllardır sabit; bir sabah değişiyor ve sebebini sormaya korkuyorsun.
10. [#7] Krizde kalabalıkta 80 etiket; hiçbiri "kim yardım edebilir" sorusunu cevaplamıyor — güç yanlış soruyu cevaplıyor.
11. [#8] Seni en az seven kişinin tek yardım edebilecek kişi olduğunu anlıyorsun; ona koşuyorsun.
12. [#9] Kuralın tersine dönmesi: etiket bir hüküm değil, bir sorunun başlangıcıymış ("Neden?" diye sorunca değişiyor).
13. [#10] Tanımadığın birinin etiketinde senin adın yazıyor — cliffhanger.

### B. Lanet / bedelli güç — 13
14. [#1] İlk dakika mucize, ikinci dakika yan etki: dokunduğun bardak buz tutuyor, sonra parmak uçların.
15. [#2] Bedel bir sayıyla söylenir: "Her kullanım bir saat uykuna mal oluyor."
16. [#3] Avantaj montajında bedel görünmez ama küçük işaret bırakılır (titreyen el, duran saat) — planted.
17. [#5] "Ve bunun bir bedeli var." tek başına, ardından 2 sn sessizlik.
18. [#5] Bedeli ilk kez başkası fark eder (anne, kardeş, doktor); sen inkâr edersin. "İyiyim." Değilsin.
19. [#6] Bedel kurala dönüşür: okul yasaklar, apartman yönetimi toplantı yapar, sigorta seni kapsamaz.
20. [#6] Kendine kural koyarsın ("asla kalabalıkta kullanma") — kriz bu kuralı çiğnetecek.
21. [#7] Kriz tam olarak gücün zayıf olduğu koşulda gelir (soğuk, karanlık, kalabalık, yorgunluk).
22. [#7] Saat başlar: "On iyi dakikan var." Sayaç ekranda.
23. [#8] Planted eşya çözümü açar (babanın çakısı, ninenin düdüğü, eski metro kartı).
24. [#8] Kurtarırsın ama bedeli ödersin; kurtardığın kişi seni kurtarır (rol değişimi).
25. [#9] Krizden 10 sn sonra komik rahatlama: kurtardığın çocuk büyüklere seni nasıl ayıltacaklarını anlatır.
26. [#9] Bedel başkası için anlam kazanır (bilim insanı, ilaç, uzay görevi teklifi).

### C. Ölçek (her basamak ×3–×10) — 12
27. [#3] Ev → apartman → mahalle → ilçe: etki her 15 sn'de bir harita katmanı büyür.
28. [#3] Kıyas nesnesi merdiveni: çay bardağı → küvet → havuz → baraj → Haliç → Marmara.
29. [#4] Tanınırlık merdiveni: 3 komşu → okul grubu → 50 bin izlenme → ana haber → 30 milyon.
30. [#4] Uzman testi: cihaz "ölçülemedi" hatası verir.
31. [#5] Ölçek bedeli büyütür: 1 kişide gag olan şey 10 bin kişide tehlike (stadyum, metro).
32. [#7] Kuşbakışı: kamera yükselir, etkin bir daire olarak şehri kaplar.
33. [#7] Dış gözlemci cümlesi: "Uçaktan bakan biri seni bir yıldız sanırdı."
34. [#8] Ölçeği küçültme: dev güç tek bir küçük işe odaklanır (bir kapı, bir nabız).
35. [#9] Ölçeğin anlamsızlaştığı an: "Herkes seni tanıyor. Kimse seni bilmiyor."
36. [#10] Son kıyas izleyicinin kendisi: "Ve sen, şu an bunu izlerken…"
37. [#3] Rakamla ölçek: "Bugün 100 lira, yüzde 5 faizle 100 yılda yaklaşık 13 bin" (doğru formül, yuvarlanmış).
38. [#7] Sayacın tersine dönmesi: büyüyen sayı ilk kez küçülmeye başlar.

### D. Zaman — 12
39. [#3] "Birinci gün." tek cümle + ekran damgası; ardından 3 mini sahne.
40. [#3] "Birinci hafta." okul/iş/aile tepkisi.
41. [#4] "Birinci ay." resmi kurum devreye girer (hastane, federasyon, belediye).
42. [#5] "Onuncu yıl." herkes değişti, sen değişmedin (veya tersi).
43. [#6] Yakının yaş damgası seninkinden ayrılır (o 40, sen 16).
44. [#6] Ritüel tekrarı her damgada değişir: bayram sofrası 12 kişi → 6 → 1.
45. [#7] "Dört yıl sonra." meslek değişimi; güç artık işin.
46. [#7] Kriz saatle anlatılır: "Cuma, 23.40." "23.52." "00.03."
47. [#8] Dakika sayacı: "Birinci dakika… dördüncü dakika… onuncu dakika."
48. [#9] Kuşak atlaması: torununun torunu elinde eski bir fotoğrafla kapını çalar.
49. [#9] Kozmik damga: "Beş milyar yıl." tek cümle, sonra sessizlik.
50. [#10] Döngü: son damga ilkinin aynısı ("Birinci gün. Yine.").

## (6) Dil kuralları

| kural | hedef | ölçüm kaynağı |
|---|---|---|
| Hitap | 2. tekil, şimdiki zaman ("Karşıdan karşıya geçiyorsun.") | hit "you"/100 = 8.1 (6.2–9.7) |
| Sen yoğunluğu (TR) | Türkçede zamir düşer; **2. tekil çekimli fiil + sen/senin/sana ≥ 10/100 kelime** | EN'den uyarlama (düşük güven) |
| Cümle uzunluğu | EN medyan ≤6 → **TR medyan ≤5 kelime**; ≥15 kelimelik cümle 30 sn'de en fazla 1 | hit 5, flop 6 |
| Konuşma hızı | EN 150–175 WPM → **TR 135–155 kelime/dk** | hit 167, flop 148 |
| İlk 10 sn | 20–28 TR kelime | hit 30 EN |
| Parça cümle | 3 cümlenin 1'i fiilsiz olabilir ("Çizik yok. Morluk yok.") | rvyd, MGZd |
| Rakam | 2–3 rakam/100 kelime, her rakam bir kıyasla ("normal 70, seninki 700") | hit 2.2 |
| Bilim | ≤40 sn/blok, 1 benzetme, 1 isim veya yıl; sonraki 3 dk'da sahnede kullanılmalı | Neden çalışıyor |
| Mizah | ilk 3 dk ≥3 gag; son %30'da ≤1; tip: öz-aşağılama, absürt somut ayrıntı, yan karakterin tek repliği | hit 3.5 |
| Diyalog | metnin %10–20'si; replik ≤8 kelime; en fazla 3 konuşan | M_t2, jJCQ |
| Motif | 1 kısa ifade ≥3 kez tekrar ("Hâlâ nefes alıyorsun" tipi) | ggRf, MGZd |
| Retorik soru | 0.5–1.5/100 kelime | nOhe 1.6 |
| Yasak | anlatıcı özeti ("Şimdi hayal et…"), 2 cümleden uzun ders, marka/ünlü/gerçek kişi | flop'lar |

## (7) Bitiş tipleri — hangisi hit'lerde

| bitiş tipi | hit (10) | flop (10) | örnek |
|---|---|---|---|
| "Would you…?" ikili soru | **9** | 7 | DK4E, MGZd, rLCV (YES/NO) |
| + subscribe/like CTA | 7 | 5 | M_t2, rvyd, JSl2 |
| Ödül / yeni kapı | 2 | 0 | rvyd (Mars), JSl2 (bilim) |
| Döngü / sıfırlama | 2 | 3 | M_t2 yeni evren, x3Pb ateş böceği |
| Cliffhanger / part two | 2 | 4 | ggRf, nOhe vs Dreams, Water, Same Day, Electricity |
| Ders cümlesi | 6 | 6 | |
| Soru yok, trivia/mesaj | 0 | 1 | Sank |

Kural: **ödül veya döngü + ikili soru + ≤10 sn CTA**. Cliffhanger flop'larda daha sık (4 vs 2) — tek başına güvenilir değil; kullanılacaksa ders ve ödülden sonra, son 20 sn'de. Soru iki somut seçenek sunmalı ("zengin mi olursun, birinin geleceğini mi kurtarırsın?"), "ne düşünüyorsun?" değil.

## (8) Senaryo QA rubriği (10 kriter, 0/1; geçme ≥8, 1 ve 2 zorunlu)

| # | kriter | eşik | nasıl ölçülür |
|---|---|---|---|
| 1 | İlk kural ihlali | ≤15 sn | zaman damgalı metinde ilk mucize/tehdit |
| 2 | Kural cümlesi | ≤30 sn, ≤20 kelime, video boyunca yeniden tanımlanmıyor | okuma |
| 3 | "Ya … olsaydı?" sorusu | 20–45 sn, sahneden sonra | damga |
| 4 | Karanlık vaat | 25–50 sn arasında var | metin |
| 5 | İlk karanlık dönüş | %28–48 | vuruş tablosu |
| 6 | Süre/sahne ekonomisi | 6–10 dk; tek mekân ≤60 sn; bilim bloğu ≤40 sn | vuruş tablosu |
| 7 | Tırmanma | ≥6 zaman/ölçek damgası, ×3+ büyüme, sosyal→fiziksel→varoluşsal | damga listesi |
| 8 | Planted-payoff | ≥2 çift, aralık ≥3 dk | not |
| 9 | Dil | TR medyan cümle ≤5; 135–155 kelime/dk; sen-çekimi ≥10/100; ilk 3 dk ≥3 gag | stats.py TR uyarlaması |
| 10 | Bitiş | ikili soru + (ödül veya döngü) + CTA ≤10 sn | son 30 sn |

Kırmızı bayraklar (biri bile = yeniden yaz): premise marka/ünlü/haber bağımlı; kahraman edilgen, karar yok (Sank dersi); kriz premise'den organik değil (Dreams dersi); ses/altyazı dili başlık dilinden farklı (Readout dersi); kural ikinci kez tanımlanıyor (Partners dersi).

## (9) Türkçe örnek senaryo — "Ya herkesin seni en son ne zaman düşündüğünü görseydin?"

**Premise (özgün):** Herkesin başının üstünde, seni en son ne zaman düşündüğü yazıyor ("Şimdi", "Üç ay önce", "Hiç"). Sadece sen görüyorsun; kendi yazını göremiyorsun. Tip: sosyal-bilgi gücü (hit'lerin 3/10'u). Lie Count / Secretly Hates / Future Wealth'ten farkı: sayı bir yargı (yalan, nefret, servet) değil, **dikkat**; bu yüzden karanlık dönüş "seni en çok düşünen kişi yardım istiyor olabilir" ters kuralına bağlanıyor.

**Başlık önerileri** (paketleme ajanına aday): "Ya Herkesin Seni En Son Ne Zaman Düşündüğünü Görseydin?" · "Ya Herkesin Başında Seni Ne Zaman Düşündüğü Yazsaydı?"

**Ölçümler (`script_tr.md`, python):** 1,326 kelime · 155 kelime/dk + vuruş başına 1.5 sn sessizlik → **8:48** · medyan cümle 3 kelime, ≥15 kelimelik cümle 4 · 10 vuruş · rakam: dört yıl, yarı, dörtte bir, 81 yaş, 112, 12 dk, 50 bin, 11 yıl.

**Self-QA (§8 rubriği):**

| # | kriter | sonuç |
|---|---|---|
| 1 | ilk ihlal ≤15 sn | ✔ 4 sn (ev sahibinin başında yazı), 8.5 sn (yazı "Şimdi"ye döner) |
| 2 | kural ≤30 sn, tek cümle | ✔ 22.5 sn, 13 kelime; video boyunca değişmiyor (sadece "kendi yazını göremezsin" istisnası) |
| 3 | soru 20–45 sn | ✔ 37.5 sn |
| 4 | karanlık vaat | ✔ 41 sn |
| 5 | ilk karanlık %28–48 | ✔ %44 (baba "On bir yıl önce") |
| 6 | süre / sahne | ✔ 8:48; en uzun tek mekân kriz sahnesi ~55 sn; bilim blokları ~45 sn ve ~15 sn (sınırda) |
| 7 | tırmanma | ✔ 9 damga (Salı, Birinci gün, hafta, ay, ikinci ay, üç hafta sonra, Cuma 23.40/23.46/23.52, dakika 1/4/8) + ölçek: 1 → 12 → 300 → 50,000 → 1 |
| 8 | planted-payoff | ✔ 4 çift: üç tık (02:35 → 05:24), sardunya anahtarı (02:35 → 06:12), kumanda (02:35 → 07:08), "Şimdi'den uzak dur" kuralı (02:35 → 05:24 çiğnenir) |
| 9 | dil | ✔ medyan 3; ilk 3 dk 6 gag (duş, kuaför, Barista kedisi, öğretmen kornası, konserve, 50 bin "Hiç") |
| 10 | bitiş | ✔ döngü (aynada yazı) + ikili soru ("Bakarım / Bakmam") + CTA 6 sn |

Bilim notları (yayın öncesi doğrulanacak): Ebbinghaus unutma eğrisi (1885) — 1 günde öğrenilenin yarıdan fazlası unutulur; "spotlight effect" tişört deneyi (Gilovich ve ark., 2000) — katılımcılar ~%50 tahmin etti, gerçek ~%25'in altında; 65 yaş üstü yaklaşık her 4 kişiden 1'i yılda bir düşer (ABD CDC verisi; TR verisi bulunursa değiştir); "uzun süre yerde kalma" riski (long lie) geriatri literatürü.

**Tam seslendirme metni** (zaman damgaları 155 kelime/dk + vuruş arası 1.5 sn ile hesaplandı; TTS hızına göre `script_tr.md`'den yeniden hesapla):

### [00:00] Vuruş 1 — Hook: ev sahibi, anne, Emre  (116 kelime, %0)

Salı sabahı. Kapı çalıyor. Ev sahibin Cengiz Bey, elinde bir zarf.
Ve başının üstünde, havada, yeşil bir yazı yanıyor: "İki dakika önce."
Sen daha ağzını açmadan yazı değişiyor: "Şimdi."
"Evladım, kirayı bir konuşalım."
Tabii. Bu adam seni her gün düşünüyor. Ayın birinde. Ayın on beşinde. Muhtemelen duşta bile.
Kapıyı kapatıyorsun. Annen arıyor. Görüntülü. Başının üstünde: "Şimdi." Hep şimdi.
Kural tek cümle: Herkesin başının üstünde, seni en son ne zaman düşündüğü yazıyor.
Sonra en yakın arkadaşın Emre mesaj atıyor. Profil fotoğrafının üstünde: "Üç ay önce."
Dün akşam birlikte maç izlediniz. Aynı çekirdeği yediniz.
Kulağa eğlenceli geliyor, değil mi?
Peki ya herkesin seni en son ne zaman düşündüğünü görebilseydin?
Bu videonun sonunda, bazı yazıları hiç görmemiş olmayı dileyeceksin.

### [00:46] Vuruş 2 — Mekanizma + bilim  (121 kelime, %9)

Önce şunu bil: insan beyni unutmak için tasarlanmış.
On dokuzuncu yüzyılda Hermann Ebbinghaus adında bir psikolog, anlamsız heceler ezberledi ve kendini test etti.
Bir gün sonra öğrendiklerinin yarısından fazlası gitmişti.
Yani biri seni gerçekten düşünüyorsa, beyni seni bilerek geri çağırıyor demek. Seni masaya geri koyuyor.
Ama asıl ilginç kısım şu.
İnsanlar, başkalarının onları ne kadar düşündüğünü sürekli abartıyor.
Bir deneyde öğrencilere utanç verici bir tişört giydirip kalabalık bir sınıfa soktular.
Odadakilerin yarısının fark edeceğini sandılar. Fark eden dörtte birden azdı.
Herkes kendi filminin başrolünde. Sen herkesin filminde figüransın.
Senin tek farkın şu: artık figüranlığının saatini görebiliyorsun.
Ve bir şey daha: yazıyı kimse görmüyor. Sadece sen.
Annene söylemeyi deniyorsun. "Anne, başının üstünde bir yazı var."
Annen saçını düzeltiyor. "Kuaföre gitmem lazım zaten."

### [01:34] Vuruş 3 — Avantaj montajı  (152 kelime, %18)

Birinci gün. Metrobüs. Sabah sekiz.
Önündeki adamın başında "Şimdi" yazıyor. Tanımıyorsun. Sonra fark ediyorsun: ayağına basıyorsun.
Özür diliyorsun. Yazı "Bir dakika önce"ye dönüyor. Affedildin. Hızlı bir şehir burası.
Birinci hafta. Okul.
Kimya hocası Nermin Hanım. Başında: "Dört yıl önce." Dört yıldır derse giriyorsun.
Hatırladığı tek an, adını yazmayı unuttuğun o sınav kâğıdı. Mantıklı.
Sıradaki kız, Defne. Başında: "Şimdi."
Dönüp bakıyor. Sen de dönüp bakıyorsun. Yazı titriyor: "Şimdi. Şimdi. Şimdi."
Kalbin dört dakika boyunca trafikte sıkışmış bir dolmuş gibi kornaya basıyor.
Akşam E-5. Trafik kilit. Arka arabadaki adam kornaya asılıyor. Başında: "Şimdi."
Dikiz aynasından bakıyorsun. İlkokul öğretmenin. Yirmi kilo almış, sen de on iki yaş.
Camı açıp el sallıyorsun. Korna duruyor. Yazı "Yirmi yıl önce" oluyor. Bazı şeyleri bilmemek daha iyi.
Sonra iş görüşmesi. Kadıköy'de bir kafe, yarı zamanlı.
Müdürün başında: "Hiç."
Konuşmaya başlıyorsun. Notlarını anlatıyorsun. Hiç.
Kahve sevdiğini söylüyorsun. Hiç.
Kedine "Barista" adını verdiğini söylüyorsun.
"Şimdi."
İşi alıyorsun. Kedine bir konserve borçlusun.

### [02:35] Vuruş 4 — Ölçek + planted ögeler  (189 kelime, %29)

Birinci ay. Bunu kimseye anlatmıyorsun. Ama kullanıyorsun.
Kim seni unuttuysa ona yazıyorsun. Kim seni düşünüyorsa ondan kaçıyorsun.
Çünkü "Şimdi" genelde bir şey isteyen insan demek.
Bankacı. Telefon şirketi. Cengiz Bey. Bir de site yönetimi.
İskelede yüzlerce kişinin arasından geçiyorsun. Neredeyse hepsinde aynı kelime: "Hiç."
Üç yüz kişi. Üç yüz "Hiç." Garip bir şekilde rahatlatıcı.
Maç günü stadyuma gidiyorsun. Elli bin kişi. Tribünden aşağı bakıyorsun: elli bin "Hiç."
Ve tam o an kaleci topu kaçırıyor, sen ayağa fırlayıp bağırıyorsun, kamera sana dönüyor.
Dev ekranda yüzün. Elli bin kişinin başında aynı anda: "Şimdi."
Üç saniye. Sonra gol oluyor ve elli bin kişi seni sonsuza kadar unutuyor.
Bir insanın hatırlanması üç saniye sürüyor. Unutulması da.
Bir de apartmanın en üst katındaki Nuriye Teyze var.
Seksen bir yaşında. Başında hep "Şimdi."
Seni merdivende görünce duvara üç kere vuruyor. Tık, tık, tık.
Çocukken sana mercimek çorbası getirdiği günlerden kalma bir işaret.
Üç tık: "Gel, bir bak bana."
Bir keresinde sana yedek anahtarını gösterdi. Paspasın altında değil, sardunya saksısının içinde.
"Hırsız saksıya bakmaz evladım."
Ve sen her üç tıkta merdivenleri ikişer ikişer çıkıyorsun.
Çünkü tahmin et. Ne istediğini biliyorsun.
Televizyon kumandası. Her seferinde televizyon kumandası.

### [03:49] Vuruş 5 — İlk karanlık dönüş: bedel  (102 kelime, %44)

Ve bunun bir bedeli var.
İkinci ay. Emre'nin yazısı değişiyor. "Altı ay önce."
Geriye gidiyor. Zaman geriye gitmez. Ama bu yazı gidiyor.
Ona her gün yazıyorsun. Cevap veriyor. Gülen surat atıyor. "Altı ay önce."
Annene bakıyorsun. "Şimdi."
Babana bakıyorsun.
Babanın başında: "On bir yıl önce."
Aynı evde yaşıyorsunuz. Aynı kumandayla aynı haberi izliyorsunuz.
Psikologların buna verdiği bir ad var: yanımızdaki insanı en az düşünürüz, çünkü zaten hep orada.
Bunu okuduğun gece bir şey daha fark ediyorsun.
Kendi yazını göremiyorsun. Aynada boş. Vitrin camında boş. Telefonun karanlık ekranında boş.
Yani sen de birini on bir yıldır hiç düşünmüyor olabilirsin.
Ve kim olduğunu bilmiyorsun.

### [04:30] Vuruş 6 — Bedel derinleşir  (134 kelime, %51)

Derse çalışmayı bırakıyorsun. Herkesin yazısını okuyorsun.
Kantinde, otobüste, Bağdat Caddesi'nde, bayram sofrasında.
Bayramda on iki kişi. On iki ayrı yazı.
Halan: "Geçen bayram." Kuzenin: "Hiç." Dayın: "Şimdi." Çünkü ona hâlâ borcun var.
Gülümsüyorsun. Baklavanı bitirmeden sofradan kalkıyorsun.
Artık insanları görmüyorsun. Yazılarını görüyorsun.
Üç hafta sonra Defne'nin yazısı: "Dün."
Sonra: "Üç gün önce."
Ona bir şey olmadı. Sana bir şey oldu.
Çünkü sen artık ona bakmıyorsun. Başının üstüne bakıyorsun.
İnsanlar bunu fark eder. Konuşurken gözünün yukarı kaydığını herkes görür.
Teneffüste Defne yanına geliyor. "Saçımda bir şey mi var?"
"Yok." Var. Ama sana söyleyemezsin.
"Sen konuşurken hep tepeme bakıyorsun. Ben aşağıdayım, biliyorsun değil mi?"
Gülüyor ama gitmeden önce yazısı bir kez daha kayıyor: "Bir hafta önce."
Buraya kadar izlediysen, abone ol. Kimse seni unutmasın.
Ve bir şey daha fark ediyorsun.
Nuriye Teyze üç gündür duvara vurmuyor.

### [05:24] Vuruş 7 — Kriz kurulumu  (121 kelime, %61)

Cuma gecesi. Saat 23.40.
Ders çalışıyormuş gibi yapıyorsun. Aslında Emre'nin profiline bakıyorsun.
Tavan tıkırdıyor.
Tık.
Bekliyorsun. İkincisi gelmiyor.
Saat 23.46.
Yukarıdan kapı sesi yok. Su sesi yok. Televizyon sesi de yok.
Telefonu açıp Nuriye Teyze'nin bayramda çektiğin fotoğrafına bakıyorsun.
Yazı: "Şimdi."
Ama fotoğrafta bile titriyor. "Şimdi. Şimdi. Şimdi."
Seksen bir yaşında biri, gece yarısına yakın, seni düşünüyor. Hiç durmadan.
Yaşlıların yaklaşık dörtte biri her yıl en az bir kez düşüyor.
Ve yere düşen birinin en büyük düşmanı kırık kemik değil.
Saatlerce kimsenin bilmemesi.
Saat 23.52.
Annen uyuyor. Baban uyuyor. Apartman uyuyor.
Kulaklığını takıyorsun. Çıkarıyorsun. Tekrar takıyorsun.
Kendine bir kural koymuştun, hatırlıyor musun? "Şimdi" yazan insandan uzak dur. Bir şey isteyecektir.
"Teyze kumandayı düşürmüştür" diyorsun kendine.
Kendine yalan söylemeyi bu ay öğrendin.

### [06:12] Vuruş 8 — Kriz çözümü  (141 kelime, %71)

Ama bu sefer bakıyorsun.
Kendi tavanına bakıyorsun ve oraya, betonun üstüne, yeşil bir yazı vuruyor.
Duvarın arkasından. Tavanın arkasından. Birinin seni çağırması gibi.
"Şimdi."
Merdivenleri ikişer ikişer çıkıyorsun.
Kapı kilitli. Zile basıyorsun. Ses yok.
Yedek anahtar. Nerede?
Sardunya. Hırsız saksıya bakmaz.
Toprağı tırnaklarınla eşeliyorsun. Anahtar. Paslı ama dönüyor.
Mutfakta, yerde. Gözleri açık. Bir eli hâlâ duvarda.
Üçüncü tıkı vuramamış.
"Geldin mi?"
"Geldim teyze. Geldim."
112'yi arıyorsun. Ambulans on iki dakika diyor.
Başını dizine alıyorsun. Konuşuyorsun. Çorbayı anlatıyorsun. Kumandayı anlatıyorsun.
Birinci dakika. Eli soğuk. Battaniyeyi koltuktan çekip üstüne örtüyorsun.
Dördüncü dakika. Gözleri kapanmak istiyor. "Teyze, kumandanın pilini kim değiştirdi, hatırlıyor musun?" "Sen." "Kaç kere?" "Yüz kere." Gözleri açık kalıyor.
Sekizinci dakika. Sokakta siren. Merdivende ışık.
Yazısı bir an bile değişmiyor. "Şimdi."
Sonra kapıda bir ses. Baban. Pijamayla, terliğin tekiyle.
Merdivende koşan ayak seslerini duymuş. Seni duymuş.
Ve babanın başında, yeşil, net: "Şimdi."

### [07:08] Vuruş 9 — Anlam, rahatlama, ödül  (174 kelime, %81)

Ambulans geliyor. Kalça kemiği çatlak. Ama zamanında.
Doktor diyor ki, bir gece daha yerde kalsaymış, iş bambaşka olurmuş.
Hastane koridorunda baban yanına oturuyor.
Bir şey söylemiyor. Otomattan iki çay alıyor. Birini sana uzatıyor.
Onun yazısı artık "On bir yıl önce" değil.
Ama asıl değişen onun yazısı değildi. Senin bakışındı.
On bir yıl boyunca yan yana oturdunuz ve ikiniz de ekrana baktınız.
Ertesi sabah Nuriye Teyze'nin ilk sözü: "Kumandayı getirdin mi?"
Getirmişsin. Bütün gece cebindeymiş.
Hemşire soruyor: "Torunu musunuz?" Nuriye Teyze cevap veriyor: "Daha iyisi. Alt kat komşusu."
Sonra sana dönüp fısıldıyor: "Duvara üç kere vurdum, sen ikisini duydun. Yeter."
Bir hafta sonra apartmanın grubuna yeni bir kural yazıyorsun: Her akşam dokuzda herkes bir kere tavana vurur. Kimse cevapsız kalmaz.
Site yönetimi bunu da aidata eklemeye çalışıyor. Ama ilk kez kimse itiraz etmiyor.
Ve Emre? Ona yazmıyorsun. Kapısına gidiyorsun.
Başında hâlâ "Altı ay önce."
"Altı ay önce babam hastaneye yattı" diyor. "O günden beri kimseyi düşünemedim."
Yazı bir hüküm değilmiş. Bir sorunun başlangıcıymış.
Ve o soruyu sormak için tek yapman gereken, yukarı değil, karşına bakmakmış.

### [08:17] Vuruş 10 — Döngü + ikili soru + CTA  (76 kelime, %94)

O gece aynanın önünde duruyorsun.
İlk kez kendi başının üstünde bir yazı var.
Ama senin değil. Aynada bir isim yazıyor.
"Defne. Dört gün önce."
Senin onu en son düşündüğün an.
Güç baştan beri doğru soruyu soruyordu. Sen yanlış yere bakıyordun.
Peki sen olsan?
Herkesin seni en son ne zaman düşündüğünü görmek mi isterdin?
Yoksa bazı yazıları hiç bilmemek mi?
Yorumlara tek kelime yaz: Bakarım ya da Bakmam.
Ve abone ol. Haftaya yeni bir "Ya … olsaydı?"

## (10) Türkçe uyarlama notları

### İngilizce hook kalıplarının Türkçe karşılıkları

| İngilizce kalıp (hit'lerde ölçülen) | Türkçe karşılık | not |
|---|---|---|
| "So, what if you could …?" | "Peki ya … görebilseydin / yapabilseydin?" | "Peki ya" ile başla; soru eki "-seydin" TTS'te yükselen tonla okunur |
| "Here's how it works." | "Olay şu." / "Nasıl çalışıyor, anlatayım." | "İşte nasıl çalışıyor" çeviri kokar |
| "Sounds amazing, right?" | "Kulağa harika geliyor, değil mi?" | |
| "Stick around, because by the end of this video…" | "Bu videonun sonunda … hiç istemeyeceksin." | "Sonuna kadar izle" deme — emir değil vaat |
| "But there's a catch." / "And there's a cost." | "Ama bir şartı var." / "Ve bunun bir bedeli var." | tek cümle + 1.5–2 sn sessizlik |
| "At first, it's amazing." | "İlk başta harika." | |
| "But here's where it gets dangerous." | "Ama işler burada karışıyor." | |
| "Congratulations, you're immortal." | "Tebrikler, artık ölümsüzsün." | |
| "Day one. / Week one. / Year ten." | "Birinci gün. / Birinci hafta. / Onuncu yıl." | sıra sayısını yazıyla yaz |
| "Bro, how did you do that?" | "Kanka, bunu nasıl yaptın?" | "Kardeşim" yaş grubuna göre |
| "Would you …? Tell us in the comments." | "Sen olsan … mı, yoksa … mı? Yorumlara tek kelime yaz: …" | iki kelimelik seçenek ver (Bakarım/Bakmam, Evet/Hayır) |
| "Subscribe for a new What If every week." | "Abone ol, haftaya yeni bir 'Ya … olsaydı?'" | |

### Türkçe dil farkları
- **Kelime sayısı**: Türkçe eklemeli dil; aynı süre için EN'den ~%20–30 daha az kelime. EN hit medyanı 1,220 kelime/8:22 → TR karşılığı ~950–1,100 kelime. Brief'teki 1,300–1,500 hedefi ancak **155–165 kelime/dk** hızlı okumayla 8–9 dk'ya sığar; TTS sesi 130–140 kelime/dk okuyorsa 1,326 kelime ≈ 9:45–10:15 olur → bu durumda Vuruş 2'deki tişört deneyini ve Vuruş 4'teki stadyum sahnesini kes (≈170 kelime). Önce TTS sesinin gerçek kelime/dk'sını 100 kelimelik örnekle ölç.
- **"Sen" yoğunluğu**: zamir düşer; ölçüt 2. tekil çekimli fiil sayısı (örnek metinde ≈10/100).
- **Şimdiki zaman** ("-iyorsun") bütün anlatıda; geçmiş anlatı yalnızca flashback'te ("-mıştı").
- **Gündelik yerleşim**: kira/ev sahibi, metrobüs/E-5 trafiği, bayram sofrası, apartman/site yönetimi, komşu teyze, iş görüşmesi, okul. İstanbul semt adı ≤2 (Kadıköy, Bağdat Caddesi) — taşra izleyiciyi dışlama.
- **Mizah**: öz-aşağılama ve aile mizahı TR'de güçlü; siyasi/dini/marka mizahı yok.

### TTS okunuş kuralları (rakam/kısaltma)
1. Sayıları **yazıyla** yaz: "on bir yıl", "seksen bir yaşında", "elli bin kişi". Rakam yalnızca ekranda (HUD) kalsın.
2. Saatler: "23.40" yazma → "saat yirmi üçü kırk geçiyor" veya "gece on biri yirmi geçe"; ekranda 23.40.
3. Telefon kısaltmaları: "112" → "yüz on iki"; "E-5" → "E beş"; "TL" → "lira".
4. Yüzde: "%25" → "yüzde yirmi beş"; kesir tercih et: "dörtte bir".
5. Büyük sayılar: "8.742.619.300" gibi sayıyı TTS'e verme; "sekiz milyar" de, tam sayıyı ekranda göster.
6. Yabancı özel ad: fonetik yaz ("Ebinghaus" değil "Ebbinghaus" yazıp TTS sözlüğüne "e-bing-haus" ekle). Gerçek kişi adı sadece bilim kaynağı için.
7. Tırnaklı ekran yazısı ("Şimdi.") TTS'te ayrı paragraf + öncesinde 0.4 sn duraklama (SSML `<break time="400ms"/>`).
8. "…" yerine nokta + duraklama kullan; TTS üç noktayı farklı uzatır.
9. Soru cümlelerinde "mı/mi" ekini ayrı yaz ve sona soru işareti koy; aksi halde düz okunur.
10. Ünlem kullanma; yükselişi kelime seçimiyle ver.

## Açık sorular / düşük güven

1. **n küçük**: 10 hit vs 10 flop, 8 kanal; medyan farkları (6.5 vs 12 sn, 30 vs 60 sn) yönlü ama istatistiksel test yapılmadı. Kanal etkisi (abone 2.3K–10.7K, yaş 4–14 gün) kontrol edilmedi.
2. **Heatmap yok**: 11 paketin hepsinde `heatmap.json` = null; tekrar-izleme zirvesi ve gerçek tutma eğrisi ölçülemedi. Vuruş başına izleyici kaybı tahmindir. 2 hafta sonra paketleri yeniden çek.
3. **Senaryo mu paketleme mi**: yalnızca Hour Seven ve Jeremy Bearimy çiftlerinde senaryo farkı ölçülebilir ve yönlü; ConChaser/Miko/Ifquirky çiftlerinde senaryo zanaatı eşit, fark büyük olasılıkla fikir + thumbnail. Readout çiftinin farkı dil (yüksek güven); Iflord çifti erken (1 gün).
4. **TR hız ve uzunluk**: TR kelime/dk hedefi EN'den çevrildi, ölçülmedi. TR'de hit veren "what if" kanalı analiz edilmedi.
5. **Premise sınıflaması** ("vücut-temelli tutar, süper güç tutmaz") 20 videodan; Iflord Electricity 7 gün sonra tutarsa kural zayıflar.
6. Hit'lerin 2'si **seslendirmesiz/ekran metinli** (Snail) veya çok yavaş (Readout, 94 WPM) — dil kuralları sesli anlatım formatı içindir; sessiz/ölçek formatı için ayrı alt şablon gerekebilir.
7. Örnek senaryonun bilim iddiaları yayından önce kaynakla doğrulanmalı (Ebbinghaus oranı, tişört deneyi oranları, düşme istatistiği).
8. Transkriptler auto-caption; kelime sayıları ±%3, zaman damgaları ±1 sn.

## Diğer ajan için not

- **Başlık/thumbnail ajanı**: Hit başlıklarının 6/10'u "What If You Could See / You Were / Your X" (2. tekil + tek somut nesne). Flop'larda marka (Tesla), soyut fiil (Erase Anything), meme-dışı edilgen ("Sank and Couldn't Stop") var. ConChaser'da "Everyone's Future Wealth" (arzu) tuttu, "Days People Have Left" (keder) ve "Partners" (mahremiyet) tutmadı. Hour Seven "Immortal Snail" internet meme'ine yaslanıyor. Readout'ta Danca seslendirmeli videonun İngilizce başlıkla yayınlanması dağıtım hatası — dil tutarlılığını kontrol et.
- **Animasyon/kurgu ajanı**: Hour Seven ikisi de sessiz, POV low-poly Blender, italik tek satır alt yazı + sol üstte HUD sayaç (TIME/Year, SNAIL mi, DEPTH m); rLCVK9llntQ kesme 12.8/dk (score≥4), medyan plan 5 sn, −19.9 LUFS. Readout: kuşbakışına yükselen kamera, 7 perde. ggRf0ZYzrr8 transkriptinde [music] işareti ~her 5 sn (yoğun müzik vurgusu). Ekrandaki sayaç (yıl/derinlik/sayı) hem senaryo hem görsel motor — HUD tasarımını standart yap.
- **Yayın ajanı**: Miko ve Readout çok dilli altyazı/dub kullanıyor (uk, da, sv, nl…); TR kanalda EN altyazı + çok dilli başlık testi düşünülebilir.
