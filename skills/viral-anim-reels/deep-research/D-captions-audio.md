# D — Altyazı, ses ve seslendirme (Ricks Clips + 5 rakip, 40 video)

Analist D · 2026-10-29 · Veri: `videos/ricksclips` (25 video; en yeni 22'si **core**) ve `videos/competitors` (15 video).
Scriptler `analysis/scripts/` altında:

- `d_captions.py`: yakılmış altyazıyı 10 fps'te, 720×1280 tam çözünürlükte ölçer. Bant, konum, yükseklik, kart sayısı, json3'e göre senkron.
- `d_audio.py`: ebur128, silencedetect, mid/side, F0, transient, kesme anı HF şişmesi.
- `d_pop.py`: 30 fps kare kare bbox ölçer, pop/scale animasyonu var mı diye bakar.
- `d_aggregate.py`: tabloları ve hit/flop medyanlarını üretir.

Ham çıktılar `d_captions_results.jsonl`, `d_audio_results.jsonl` ve `d_aggregate_out.md` dosyalarında. Videoların hepsi 720×1280. Piksel değerleri **1080×1920 tuvale ölçeklenmiştir (×1,5)**.

Gruplar (core 22): **HIT** ≥5M (n=12), **MID** 1–5M (n=6), **FLOP** ≤1M (n=4: Slot Machines 0,09M, Painkillers 0,29M, Memory 0,32M, Tree 0,96M).

---

## 0. Tek paragrafta sonuç

Ricks Clips'in altyazısı ve sesi **bir şablon**: 22 core videonun 22'sinde aynı.

- **Altyazı:** beyaz, Montserrat ExtraBold/Black benzeri, yazıldığı gibi büyük/küçük harf, ~3 px siyah kontur ve sert siyah gölge. Kart başına **1,3 kelime**, kart süresi **0,3 sn**. Konum sabit, **y = 1352–1355 px (yüksekliğin %70,5'i)**. Senkron ASR kelime başlangıcına göre **0 ile −20 ms** arasında. Pop animasyonu, vurgu rengi ve emoji yok.
- **Ses:** **−14,0…−16,1 LUFS** (hit medyanı −14,2), true peak **≈ −2,4 dBTP**, LRA **≈ 2 LU** (çok sıkıştırılmış). **Hiç sessizlik yok** (−35 dB altında ≥0,25 sn boşluk: 22/22 videoda 0). VO'nun altında sürekli, sessiz ve neredeyse mono bir müzik yatağı var. Anlatım **~220 kelime/dk** ile çok hızlı ve **0,00 sn'de** başlıyor.
- **Hit/flop farkı altyazıda ve seste yok denecek kadar küçük.** Viralliği konu ve hook belirliyor; bu katman "hijyen". Ses tarafında tek anlamlı sinyal şu: hit'lerde VO duraklamaları ses (SFX/müzik şişmesi) ile dolduruluyor (ρ=+0,50, p=0,03). Hit'ler ayrıca biraz daha yavaş ve daha çok mikro-duraklamalı.
- **Instagram uyarısı:** Ricks'in y≈1352 konumu IG'nin alt 672 px UI bölgesinin içinde kalıyor (y>1248). Bizim spec'te altyazıyı **y≈1060 merkezine** taşıyoruz.

---

## PART 1 — Yakılmış altyazılar

### 1.1 Ricks Clips (core 22) — ölçümler

| Metrik | Değer | Yöntem / kanıt |
|---|---|---|
| Kelime / kart | **1,29 (hit) · 1,28 (flop) · 1,31 (mid)**. Videolar arası aralık 1,17–1,37 | Kart değişim olayı sayısı ÷ json3 kelime sayısı. Manuel sayımla teyit: 3 kontak sayfasında **60 an → 77 kelime = 1,28 kelime/kart**, %70'i tek kelime, %30'u iki kelime, hiç 3 kelime yok |
| Kart süresi | **medyan 0,30 sn** (0,3–0,4) | Ardışık kart olayları arası |
| Her kelimede değişiyor mu? | **Evet**. Kart, kelime başlangıcında değişiyor. 2 kelimelik kartlar "işlev kelimesi + sonraki kelime" kalıbında: *to a, and no, a guy, your boss, the city, So he, The Emperor, every place* | Kontak sayfaları |
| Ekranda altyazı oranı | **%99,8–100**. Kartlar arasında boşluk yok, bir sonraki kart gelene kadar kalıyor | d_captions |
| Senkron (json3'e göre) | **medyan −20 ms** (12 videoda −20, 10 videoda 0). Altyazı kelimeyle aynı anda ya da en fazla 1 kare önce geliyor. Ölçüm çözünürlüğü ±50 ms | Kart olayı → en yakın kelime tOffset |
| Font | **Montserrat ExtraBold/Black** benzeri: çift katlı "a", tek katlı "g", eğik üstlü "t". İkinci aday Poppins Bold | 4× zoom (Imagine, The whole court) |
| Ağırlık | 800–900. "I" gövdesi 10 px@720 = cap yüksekliğinin %28'i | Piksel ölçümü |
| Boyut | Cap yüksekliği **54 px**@1080 ("I" 36 px@720). Küçük harfli kelimelerde dolgu bbox medyanı **59 px** (asc+desc). **Font boyutu ≈ 74–78 px** (1080 genişlik) | ffmpeg tam kare + numpy |
| Kelime genişliği | Medyan 290 px, p90 ≈ 600 px (1080 tuvalde). Genişliğin %27'si / %55'i | d_captions |
| Harf durumu | **Konuşulduğu gibi (sentence case)**: cümle başı büyük, özel isimler büyük, gerisi küçük. Noktalama korunuyor (*Japan, · nothing. · Wait,*) | Kareler |
| Renk | **#FFFFFF**, saf beyaz. Vurgu rengi **yok** (60+ anın tamamı beyaz) | Kareler + sarı oran ≈ arka plan gürültüsü |
| Kontur | **Siyah, ~2 px@720 = 3 px@1080** | Yatay tarama: dolgu → 2 px siyah → arka plan |
| Gölge | **Sert siyah gölge, ofset ≈ (+3, +4) px@720 = (+4, +6) px@1080**, blur ≈ 0–1 px | Sağ ve altta 5–6 px koyu bant, solda 2 px |
| Dikey konum | **Merkez y = 1352–1355 px (%70,5)**, 22/22 videoda ±2 px. Tek satır | d_captions (`y_center_med_1080`) |
| Pop/scale animasyonu | **Yok**. "impossible" 0,20–0,80 sn boyunca 18 karede genişlik 270 px'te sabit kaldı, sert kesmeyle değişti. Nadiren ~%6'lık yavaş büyüme görülüyor; muhtemelen tüm kareye uygulanan push-in | d_pop.py |
| Emoji | **Yok** (altyazıda). Eski dönem başlıklarında 😭🤣 vardı |  |
| Flop farkı | **Yok**. Slot Machines (0,09M) ile Jar (28,8M) altyazıları piksel düzeyinde aynı | Tablo 1.3 |

> Eski dönem (4 video): komedi/film klipleri; altyazı ya yok ya da tutarsız (`LUGcyIwlcto` 1,67 kelime/kart, y %75,8). Spec'e dahil edilmedi.

### 1.2 Rakip kanallar

| Kanal | Kelime/kart | Kart sn | Senkron | Font (tahmin) | Harf | Renk / kontur / gölge | Yazı yük. (1080) → font | Merkez y | Animasyon |
|---|---|---|---|---|---|---|---|---|---|
| **Circle Toon History** (Ricks'e en yakın) | **1,0** | 0,2 | +40…+60 ms (biraz geç) | Komika Axis / Luckiest Guy tarzı çizgi roman | **UPPER** | Beyaz, **kalın siyah kontur ~5–6 px**, hafif gölge | ~70 px cap → ~95 px | 1382–1426 (%72–74) | Statik |
| **Low Poly Shorts** | **3,3** (öbek) | 1,0 | 0…+20 ms | Verdana/Tahoma Bold, harf aralığı geniş | lower | **Sarı ≈ #F2E21A**, ince siyah kontur + gölge | ~34 px → ~40 px (küçük) | 1297–1344 (%67–70) | Statik |
| **Loaded Dice** | **3,1** | 0,9 | −70…+20 ms | Arial/Helvetica Bold | Sentence | Beyaz, ince siyah kontur 1–2 px | ~33 px → ~40–45 px (küçük) | 1357–1514 (%71–79) | Statik |
| **The Why Side** | 1,1–2,1 | 0,1–0,5 | 0…+20 ms | **Montserrat Bold/ExtraBold** | Sentence | Beyaz, ince koyu kontur + yumuşak gölge | ~55 px → ~65 px | 1273–1452 (%66–76) | Kısa giriş animasyonu var (kart medyanı 0,1 sn) |
| **i think it's george** | **0,9** (kelime parçalı) | 0,1–0,35 | −40 ms | **Bebas Neue / Anton** (dar) | **UPPER** | Beyaz, kontur yok, yumuşak gölge | ~85 px cap → ~120 px | 1316–1434 (%69–75) | **Pop**: genişlik 83→90→112→116→110 px, 4 karede ≈ ölçek 0,75→1,05→1,0 (overshoot) |

**Ortak kurallar (6 kanalın 6'sı):**
- Tek satır, yatay ortalı.
- Merkez yüksekliğin **%66–79**'unda (YT Shorts'a göre konumlanmış).
- Beyaz ya da sarı dolgu + siyah kontur/gölge.
- Hiçbirinde emoji ya da çok renkli vurgu yok.
- Senkron ±70 ms içinde.

İki okul var:
1. **Hızlı tek kelime** (Ricks, Circle Toon, george, Why Side): 0,1–0,4 sn kart, büyük font (65–120 px).
2. **Öbek altyazı** (Low Poly, Loaded Dice): 3+ kelime, ~1 sn, küçük font (~40 px), "ciddi belgesel" tonu.

**Bizim format (Ricks tarzı hikâye anlatımı) için 1. okul.**

### 1.3 Video bazlı tablo (core + rakip)

Tam tablo: `analysis/scripts/d_aggregate_out.md`. Grup medyanları:

| metrik | HIT (12) | MID (6) | FLOP (4) | Circle Toon | Loaded Dice | Low Poly | Why Side | george |
|---|---|---|---|---|---|---|---|---|
| kelime/kart | 1,29 | 1,31 | 1,28 | 1,01 | 3,07 | 3,28 | 1,71 | 0,89 |
| kart sn (med) | 0,3 | 0,3 | 0,3 | 0,2 | 0,9 | 1,0 | 0,1 | 0,1 |
| senkron ms | −20 | 0 | −10 | +40 | −20 | 0 | 0 | −40 |
| merkez y % | 70,5 | 70,6 | 70,5 | 72,0 | 75,7 | 70,0 | 67,3 | 74,6 |
| yazı bbox yük. px (1080) | 59 | 61 | 56 | 70 | 33 | 35 | 56 | 86 |

Core 22'de altyazı metriklerinin izlenmeyle korelasyonu sıfıra yakın (|ρ| ≤ 0,28, hepsi p > 0,2).

### 1.4 BİZİM ALTYAZI SPEC'İ (1080×1920)

**İlke:** Ricks'in kanıtlanmış hızlı tek kelime ritmi korunur. Yalnızca konum, Instagram güvenli alanına göre yukarı alınır.

| Parametre | Değer |
|---|---|
| Font | **Montserrat ExtraBold (800)**. Yedek: Montserrat Black 900, sonra Poppins Bold. Açık lisans (OFL), Google Fonts |
| Boyut | **80 px** (tek kelime). Kart >12 karakterse otomatik **72 px**'e iner. Maks. genişlik **950 px** (sol/sağ 65 px güvenli alan) |
| Harf durumu | Konuşulduğu gibi (sentence case), noktalama korunur. UPPERCASE yalnızca A/B testi varyantı (Circle Toon/george tarzı) |
| Dolgu | `#FFFFFF` |
| Kontur | Siyah `#000000`, **3 px görünür** (dış kontur) |
| Gölge | Siyah, **ofset x +4, y +6 px, blur 0–2 px**, opaklık %100 (sert "sticker" gölge) |
| Konum | **Merkez y = 1060 px (%55,2)**, yatay ortalı, tek satır. İzinli bant **900–1150 px**. Kesin yasak: üst 270 px, alt 672 px (y>1248), yanlarda 65 px |
| Kart kuralı | Maks. **2 kelime / 14 karakter**. İşlev kelimeleri (a, an, the, to, of, in, on, at, and, but, so, or, your, his, her, my, it's, is, was, no, just) bir sonraki kelimeyle birleşir; birleşen kelime ≤10 karakterse. Noktalama (`, . ? !`) kartı bitirir. Hedef: **1,25–1,35 kelime/kart, medyan 0,30 sn** |
| Zamanlama | Kart, ilk kelimenin başlangıcından **1 kare (33 ms) önce** girer ve bir sonraki karta kadar kalır (boşluk yok). VO bitince son kart +0,4 sn kalır |
| Animasyon | Varsayılan **yok** (Ricks gibi sert değişim). Opsiyonel test varyantı "pop": ölçek 0,85→1,06→1,00, 4 kare (~130 ms), easeOutBack, yalnızca vurgu kartlarında |
| Vurgu | Ricks kullanmıyor. Bizde **opsiyonel**: sayı, para ya da twist kelimesi `#FFD60A` sarı. **≤1 vurgu / 10 kart**, ilk 3 sn'de en fazla 1. Emoji yok |
| Okunabilirlik testi | Her kart, 360 px genişlikte küçültülmüş karede okunmalı. Parlak beyaz arka planlarda kontur 4 px'e çıkar |

**ASS stili (ffmpeg `subtitles` filtresi, PlayRes 1080×1920):**

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Word,Montserrat ExtraBold,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,5,2,65,65,820,1
Style: WordHi,Montserrat ExtraBold,80,&H000AD6FF,&H000AD6FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,5,2,65,65,820,1
```

- `Alignment=2` (alt-orta) ve `MarginV=820` → metnin alt kenarı y=1100, görsel merkez ≈1060.
- ASS'de `Shadow` x ve y'ye eşit uygulanır (5,5). Tam (4,6) istenirse olay içinde `{\xshad4\yshad6}` kullanılır.
- Pop varyantı: `{\fscx85\fscy85\t(0,70,\fscx106\fscy106)\t(70,130,\fscx100\fscy100)}`.
- Sarı ASS renk kodu BGR: `&H000AD6FF` = #FFD60A.

Render komutu:
`ffmpeg -i in.mp4 -vf "subtitles=caps.ass:fontsdir=fonts" -c:a copy out.mp4`

Olay satırı örneği:
`Dialogue: 0,0:00:00.17,0:00:00.47,Word,,0,0,0,,impossible`

**Remotion bileşeni: `<WordCaptions>` props tanımı**

```ts
type CaptionWord = { text: string; startMs: number; endMs: number; highlight?: boolean };
type WordCaptionsProps = {
  words: CaptionWord[];            // ElevenLabs /with-timestamps veya WhisperX çıktısından
  fontFamily: 'Montserrat';        // @remotion/google-fonts/Montserrat, weights ['800','900']
  fontWeight: 800;
  fontSize: 80;                    // >12 karakterde 72
  color: '#FFFFFF';
  highlightColor: '#FFD60A';
  strokeColor: '#000000';
  strokeWidthPx: 6;                // CSS -webkit-text-stroke ortalanır → paint-order:'stroke fill' ile görünür ≈3 px
  shadow: '4px 6px 0px #000000';   // textShadow
  centerY: 1060;                   // 1080x1920 kompozisyon; güvenli bant 900–1150
  maxWidth: 950;
  maxWordsPerCard: 2;
  maxCharsPerCard: 14;
  joinFunctionWords: true;         // "to a", "the city", "your boss"
  leadMs: 33;                      // 1 kare erken
  holdLastMs: 400;
  textCase: 'asSpoken';            // 'upper' A/B varyantı
  pop: false | { from: 0.85; overshoot: 1.06; frames: 4; easing: 'easeOutBack' };
};
```

Bileşen davranışı:
- `useCurrentFrame()` ile aktif kartı bulur.
- `<AbsoluteFill>` içinde `top: centerY`, `transform: translateY(-50%)` uygular.
- Kartlar arasında boşluk bırakmaz.
- Altyazı katmanı kamera push-in'inden **etkilenmez**; en üst katmanda ayrı render edilir.

---

## PART 2 — Ses

### 2.1 Ölçüm sonuçları (grup medyanları)

| metrik | HIT | MID | FLOP | Circle Toon | Loaded Dice | Low Poly | Why Side | george |
|---|---|---|---|---|---|---|---|---|
| Integrated LUFS | **−14,2** | −14,1 | −14,6 | −14,6 | −15,9 | −14,6 | −16,1 | **−11,4** |
| True peak dBTP | **−2,5** | −2,3 | −2,4 | −0,2 | −1,6 | −0,4 | −1,7 | **0,0** (taşıyor) |
| LRA LU | 2,2 | 2,0 | 2,2 | 1,7 | 2,4 | 1,7 | 2,9 | 2,2 |
| Sessizlik (<−35 dB, ≥0,25 sn) sayısı | **0** | 0 | 0 | 0 | 0 | 0 | 0 (1 videoda 3) | 0 |
| Konuşma hızı (kelime/dk, toplam süre) | **219** | 228 | 225 | 242 | 206 | 204 | 202 | 174 |
| Artikülasyon hızı (duraklamalar hariç) | 233 | 240 | 234 | 244 | 229 | 220 | 237 | 185 |
| Duraklama >0,6 sn (adet/video) | **8** | 6,5 | **3,5** | 0 | 9 | 6 | 26 | 5 |
| En uzun duraklama sn | 0,84 | 0,76 | 0,80 | 0,56 | 1,36 | 0,72 | 1,16 | 0,80 |
| VO duraklamasındaki seviye (medyana göre dB) | **−1,9** | −4,5 | **−6,5** | – | −2,5 | −1,9 | −7,8 | −3,4 |
| Taban (p10, medyana göre dB) | −9,0 | −9,4 | −9,8 | −4,1 | −6,6 | −7,2 | −9,2 | −9,8 |
| Side − Mid (dB) — stereo genişlik | **−29** (neredeyse mono) | −30 | −25 | −19 | −17 | −20 | −18 | −16 |
| F0 medyan Hz | **~197** | 204 | 199 | 239 | **~106** | 162 | 142 | 211 |
| Tonlama aralığı (p10–p90, yarım ton) | 14,1 | 13,7 | 13,6 | 16,1 | 12,3 | 15,2 | 19,3 | 15,4 |
| Transient indeksi /10 sn | 7,8 | 7,4 | 7,4 | 6,9 | 4,0 | 7,0 | 6,7 | 7,7 |
| Kesme anında HF (>5 kHz) şişme % | 57 | 71 | 71 | 61 | 42 | 74 | 37 | 40 |
| VO başlangıcı sn | **0,00** (22/22) | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,08 |
| VO bitişinden sonra kalan sn | 0,6 | 0,6 | 0,6 | 0,6 | 1,9 | 0,8 | 1,3 | 0,6 |
| ASR "[music]" etiketi | 22 videonun 17'sinde var | | | | | | | |

**Notlar:**
- **WPM** = json3 kelime sayısı ÷ (son kelime − ilk kelime) × 60. ASR, birleşik kelimeleri ayırabildiği için ±%5 sapma olabilir.
- **F0** autokorelasyonla hesaplandı, müzik altında oktav hatası olabilir. Mutlak değer yaklaşıktır; kanallar arası **göreli** fark güvenilir (Loaded Dice'ın derin bas sesi ~100 Hz olarak doğru çıktı).
- **Transient indeksi** konuşma hece başlarını da sayıyor. Bu yüzden yalnızca göreli bir ölçü; mutlak SFX sayısı değil.
- **Kesme tespiti** sahne skoru 0,05 ile yapıldı. Ricks yumuşak geçişler (blur/zoom) kullandığı için sayım düşük çıkıyor (~2,2/10 sn). Kesin kesme sayısı kurgu analistinin raporunda.

### 2.2 Yorum

1. **Mastering şablonu:**
   - Ricks −14 LUFS'a normalize ediyor (YT ve IG referansı). 22 videonun 21'i −14,0…−15,6 aralığında.
   - True peak −2 dBTP civarında (güvenli, limiter'lı).
   - LRA ~2 LU: radyo gibi sıkıştırılmış, fısıltı ile bağırma arasında seviye farkı yok.
   - george −11 LUFS / 0 dBTP ile çok yüksek mastering yapıyor; platform zaten kısıyor, fayda yok.
2. **Sessizlik yok; altta sürekli bir müzik yatağı var:**
   - 22 videonun hiçbirinde −35 dB altına inen ≥0,25 sn boşluk yok.
   - Spektrogramda (Jar, 0–15 sn) 1,0–1,3 kHz, 1,8 kHz ve 2,4 kHz'te **sürekli tonal çizgiler** (sustained notalar) ve kesintisiz <100 Hz bas enerjisi görülüyor. Bu bir müzik yatağı.
   - Taban (p10), VO medyanının ~9–10 dB altında: **müzik VO'nun ≈10 dB altında**, yani yaklaşık −24/−25 LUFS.
   - YouTube ASR 22 videonun 17'sinde "[music]" etiketi koymuş.
3. **Mix neredeyse mono:**
   - Ricks'te side−mid −29 dB; rakiplerde −16…−20 dB.
   - Ricks'in müziği ya mono ya da çok dar. VO baskın, müzik "duyulmaz ama hissedilir".
   - Rakipler daha geniş stereo müzik kullanıyor.
4. **Anlatım çok hızlı:**
   - Ricks ~220 kelime/dk (normal anlatıcı 150–170). Toplam 60 sn'de ~220–240 kelime.
   - VO **0,00 sn'de** başlıyor ve sonda yalnızca ~0,6 sn boşluk bırakıyor. Sessiz giriş yok, döngüye (loop) uygun.
5. **Hit ve flop arasındaki tek ses farkları** (küçük örneklem, keşif niteliğinde):
   - Hit'ler biraz daha **yavaş** (219 vs 225 wpm; ρ=−0,37, p=0,09).
   - Hit'lerde **daha çok mikro-duraklama** var (>0,6 sn: 8 vs 3,5; ρ=+0,35, p=0,11).
   - Hit'lerde bu duraklamalar **sesle dolu**: duraklama seviyesi −1,9 dB vs flop'larda −6,5 dB (**ρ=+0,50, p=0,03**). Yani hit'lerde twist öncesi nefes anları SFX vuruşu, whoosh ya da müzik şişmesiyle doldurulmuş. Flop'larda duraklamalar "boş" kalıyor.
   - Diğer her şey (LUFS, peak, LRA, F0, transient) gruplar arasında aynı.
6. **Anlatıcı profili (dinleme yerine geçen ölçüm + transkript):**
   - F0 ≈ 180–210 Hz, yani erkek sesi için **üst register**, heyecanlı/neşeli bir enerji.
   - Tonlama aralığı ~14 yarım ton: canlı, "hikâye anlatan arkadaş" tonu, monoton değil.
   - Loaded Dice'ın tok ~100 Hz belgesel sesinin tam tersi.
   - Transkriptlerde:
     - 2. tekil şahıs ("you/your") sık: Job 20, Second Draw 20, Tree 17, Teleport 15.
     - Bağlaçla ilerleyen anlatım: "So," (22'nin 19'unda), "Then,", "You see,".
     - **Karakter seslendirmesi**: tırnak içi diyaloglar 22 videonun 11'inde var (örn. `"Bro, it's just warming up."`). Anlatıcı karakterlerin replikleri için ses ve ton değiştiriyor.
   - Ton hafif alaycı ve eğlenmiş; ciddi bir belgesel sesi değil.
7. **SFX:**
   - Kesme anlarının ~%57–71'inde >5 kHz bantta ≥10 dB şişme var: **geçişlerde whoosh/swish standart**.
   - Transient yoğunluğu hit ve flop'ta aynı (~7,5/10 sn). SFX miktarı değil, **yerleşimi** fark yaratıyor (bkz. madde 5).
8. **Müzik ruh hâli tahmini:**
   - Sürekli tonal yatak (orta frekansta sustained akorlar) + bas, belirgin vurmalı ritim yok.
   - "Merak/gizem" tonunda, hafif quirky bir bed: pizzicato veya marimba + yumuşak pad türü.
   - Vurgu anlarında kısa şişmeler var.
   - BPM tahmini yapılamadı: yatak çok sessiz ve perküsyonsuz.

---

## PART 3 — Bizim seslendirme ve ses üretim spec'i

### 3.1 Anlatıcı personası

**"Arkadaşına inanılmaz bir şey anlatan, enerjik Amerikalı erkek hikâyeci."**

- Konuşma dili, hafif eğlenmiş ve alaycı.
- Üst-orta register.
- Cümle sonları düşmez; merakı canlı tutan yükselen tonla biter.
- Twist'ten hemen önce yarım saniyelik "bekle bunu" duraklaması.
- Karakter repliklerinde ses ve tonu hafifçe değiştirir: patron alçak, kahraman şaşkın.
- Ricks'in sesini **taklit etme**; aynı enerji bandında özgün bir ElevenLabs sesi seç. Library'de "energetic storyteller / narrator, American, young adult male" filtresi kullanılabilir.

### 3.2 ElevenLabs ayarları

| Parametre | Öneri | Gerekçe |
|---|---|---|
| Model | `eleven_multilingual_v2` (tutarlılık) ya da `eleven_v3` (daha ekspresif, `[excited]`, `[laughs]`, `[whispers]` etiketleri) | Seriler için v2 daha istikrarlı. v3'ü karakter replikleri için dene |
| stability | **0,35–0,45** | Düşük değer canlı tonlama verir (~14 yarım ton hedefi). 0,3'ün altında artefakt riski var |
| similarity_boost | **0,80–0,90** | Ses kimliği videolar arasında sabit kalsın |
| style | **0,35–0,55** | Abartmadan "eğlenmiş" ton. Karakter replikleri için 0,7 |
| use_speaker_boost | true |  |
| speed | **1,10–1,15** (API sınırı 0,7–1,2) | ElevenLabs'ın doğal hızı ~160–180 wpm. Hedef 205–220 wpm. Kalanı post'ta sessizlik kırpmayla sağla |
| Çıktı | `mp3_44100_192` veya `pcm_44100` + **`/with-timestamps`** endpoint'i | Kelime zamanları doğrudan `<WordCaptions>`'a gider, ayrıca hizalama gerekmez |

**Pacing hedefleri:**
- Toplam **205–220 kelime/dk**. 60 sn'lik video ≈ **200–225 kelime** script.
- Artikülasyon hızı ~230.
- **0,0 sn'de başla**. İlk kelimeden önce sessizlik ≤50 ms (`silenceremove`).
- **6–10 mikro-duraklama / 60 sn**, her biri **0,35–0,8 sn** (en uzun ≤0,9 sn). Konumlar:
  1. Hook cümlesinden sonra (≈2 sn).
  2. "You see," / "So," / "But," gibi dönüş bağlaçlarından önce.
  3. Twist ifşasından hemen önce (en uzun duraklama).
  4. Karakter repliğinden önce ve sonra.
  5. Son punch line'dan önce.
- **Diğer cümle araları ≤250 ms**'ye kırpılır.
- Bitiş: son kelimeden sonra ≤0,6 sn, sonra kesme (loop).
- Script'te duraklama işareti: v2'de `<break time="0.5s" />`; v3'te noktalama ("…") ve `[pause]`.

### 3.3 SFX ve müzik planı

| Katman | Kural | Seviye |
|---|---|---|
| **Müzik yatağı** | Tek parça, merak/quirky (pizzicato, marimba, hafif synth pad, perküsyon yok ya da çok hafif). Video boyunca kesintisiz; **sessizlik yok** | **−24…−26 LUFS** (VO'nun ~10 dB altı). Sidechain ducking: VO varken −4 dB, VO duraklamasında **yükselir** (duraklama dolu kalsın) |
| **Mono/dar stereo** | Müzik genişliği dar (side ≈ mid −20…−25 dB). VO tam mono, merkezde | — |
| **Whoosh** | Her sahne geçişinde (kesmelerin ≥%60'ı), peak kesme anında | Peak −10…−12 dBFS |
| **Pop / tık** | Vurgulu altyazı kartında ve nesne belirmesinde (≤1 / 3 sn) | Peak −14 dBFS |
| **Hit / impact** | Twist ve ifşa anında 1–2 kez; varsa öncesindeki duraklamayı doldurur | Peak −8 dBFS |
| **Duraklama dolgusu** | Her >0,4 sn VO duraklaması bir SFX, riser ya da müzik şişmesi ile dolar (hit/flop farkındaki tek ses sinyali) | — |
| **Ambians/foley** | Sahneye özgü (kumarhane uğultusu, ofis saati tık-tak), çok düşük | −30 LUFS |
| **Final master** | Kompresör → limiter → **−14 LUFS integrated, −1 dBTP**, LRA 2–4 LU. 48 kHz stereo, AAC 320k | IG ve YT için tek master |

**ffmpeg mix örneği** (VO + müzik ducking + SFX bus → master):

```
ffmpeg -i vo.wav -i music.wav -i sfx_bus.wav -filter_complex "
[0:a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120,asplit=2[vo][vosc];
[1:a]volume=-12dB[mus];
[mus][vosc]sidechaincompress=threshold=0.05:ratio=4:attack=20:release=300[musd];
[vo][musd][2:a]amix=inputs=3:normalize=0[mix];
[mix]alimiter=limit=0.89,loudnorm=I=-14:TP=-1:LRA=4:print_format=summary" -ar 48000 -ac 2 mix.wav
```

En doğru sonuç için `loudnorm` iki geçişli kullanılmalı: 1. geçişten `measured_*` değerlerini al, 2. geçişte ver. QA: `ffmpeg -i mix.wav -af ebur128=peak=true -f null -` → I = −14 ±0,5, TP ≤ −1,0.

### 3.4 Mevcut yardımcı scriptler (`~\.claude\skills\inner-voice-film\scripts\`)

| Dosya | Ne yapıyor | Bizde yeniden kullanım |
|---|---|---|
| `eleven_say.py` | `voice-lines.json` → ElevenLabs TTS (mp3) → başı/sonu sessizlik kırpma, highpass 70 Hz, `loudnorm -18`, mono 48 kHz wav. Ses ayarlarını `voice.json`'daki style preset'lerinden alıyor | **Kalıp olarak yeniden kullanılabilir.** `voice.json` "The Other Self" kanalının sabit sesine kilitli (dosyada "kullanıcı onayı olmadan değiştirme" notu var). **Bu dosyaya dokunma.** Ayrı bir `voice-narrator.json` oluştur (yeni voice_id, `narrator` style: stability 0,4 / similarity 0,85 / style 0,45 / speed 1,12). Script'e iki ekleme gerek: `--config` parametresi ve `/with-timestamps` çağrısı (kelime zamanları için) |
| `sfxgen.mjs` | Bağımlılıksız, deterministik prosedürel SFX: `whoosh_text`, `whoosh_cut`, `punch`, `slap_clack`, `title_thud`, `rumble_low`, `glass_crack`, `alarm_beep`, `heartbeat`, `drone`, `wind`, `shimmer`, piano motifleri | **Whoosh ve impact'ler doğrudan kullanılabilir.** Eksikler: **pop/bubble** (kısa sinüs pitch-up, ~60 ms), **tık/tick**, **riser**, quirky müzik yatağı (pizzicato). Ya generator eklenir ya da lisanslı/telifsiz kütüphane kullanılır |
| `audio.sh` / `build-film-audio.py` | VO + prosedürel skor + kompresör + `loudnorm I=-15:TP=-1.5` | Zincir kullanılabilir; hedefleri **I=-14, TP=-1** olarak güncelle |
| `qa.ps1` | Remotion tsc + still render QA | Altyazı konumunu (y 900–1150) still'lerde görsel kontrol için kullanılabilir |

### 3.5 Kontrol listesi (yayın öncesi)

- [ ] Altyazı: 1,25–1,35 kelime/kart, medyan kart ~0,3 sn, merkez y 1060 ±40, alt kenar <1150, tek satır, ≤950 px genişlik
- [ ] Senkron: kart, kelime başından 0–33 ms önce (ElevenLabs timestamps); kartlar arasında boşluk yok
- [ ] VO 0,00 sn'de başlıyor; 205–220 wpm; 6–10 mikro-duraklama, hepsi SFX ya da müzikle dolu
- [ ] Hiçbir yerde −35 dB altına inen ≥0,25 sn sessizlik yok (`silencedetect=noise=-35dB:d=0.25` → 0 sonuç)
- [ ] Master −14 LUFS ±0,5, TP ≤ −1 dBTP, LRA 2–4
- [ ] Kesmelerin ≥%60'ında whoosh; twist anında impact
