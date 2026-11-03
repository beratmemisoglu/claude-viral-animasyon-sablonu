# 06 — Edit tempo spesifikasyonu (sayılar) + QA

Kaynak: `deep-research/04-edit-rhythm-metrics.md` (41.103 karenin tamamı + 10 fps sınıflandırıcı, 47 olay gözle kalibre, %89 doğru).
"Referans" = AI Flow videosunda ölçülen; "Hedef" = bizim yayınlayacağımız. Referansın zayıf noktaları hedefte sıkılaştırıldı.

## 1. Referansın tamamı tek bakışta

| Ölçü | Değer |
|---|---|
| Görsel değişim olayı (imleç hariç) | **582 → 25,5/dk**, herhangi iki değişim arası medyan **1,4 sn** |
| Kırılım | 106 anlık kesme · 92 kademeli tam-kare değişim · 105 scroll/pan · **14 animasyonlu zoom** · 265 lokal UI değişimi |
| Çekim değişimi (kesme + kademeli) | 198 → **8,7/dk**, medyan çekim **2,6 sn**, ortalama 6,9 sn |
| Sadece anlık kesme | 4,6/dk |
| Ekran payı | tam-kare ekran kaydı %71 · zoomlu kayıt %5 · CapCut %13 · bitmiş video %5 · rakip klip %3 · yazı/grafik kartı %1,5 · meme/B-roll %0,6 |
| > 8 sn statik bekleme | 28 adet = 376 sn (%27); en uzun 31,9 sn |
| Ekler (meme, kart, klip, CTA) | 18 adet: **11'i ilk 3:12'de** (her ~17 sn), sonra her ~2,7 dk; en uzun eksiz aralık 7,6 dk |
| Ses | ~200 wpm, %94 kaplama, öğretimde 11 duraklama, −19,4 LUFS, LRA 2,8; mono ses; neredeyse duyulmaz müzik döngüsü (21,8 sn periyot); **11 yüksek müzik "sting"i** sonuç anlarında; kesmelerde whoosh/pop **yok** |

**scdet uyarısı:** beyaz→beyaz sekme geçişleri skor 5–15 alır; tek eşik kesme sayamaz (≥15'te recall %36, ≥8'de olayların yarısı kesme değil).
Aday üretmek için ≥4 kullan, sonra sınıflandır (`scripts/edit_rhythm_qa.py` bunu yapar).

## 2. Bölüm bazında referans

| Bölüm | Değişim/dk | Kesme/dk | Çekim değ./dk | Medyan çekim | Zoom | Ek | Heat |
|---|---|---|---|---|---|---|---|
| Important 0:00–3:12 | **31,6** | 5,6 | 12,8 | 2,6 | 12 | 11 | 0,10 |
| Channel Setup | 26,4 | 4,0 | 7,2 | 2,8 | 2 | 0 | 0,23 |
| Video topics | 15,7 | 1,8 | 2,9 | 4,9 | 0 | 0 | 0,23 |
| Script | 16,7 | 0,9 | 0,9 | 46,4 | 0 | 2 | 0,37 |
| Voice | 8,0 | **0** | 0 | 82 | 0 | 0 | **0,47** |
| Visuals | 30,0 | 10,2 | 14,3 | 1,5 | 0 | 1 | 0,37 |
| Videos | 33,3 | 12,0 | 18,7 | 2,2 | 0 | 1 | **0,55** |
| Editing (CapCut) | 27,9 | 6,4 | 10,9 | 2,3 | 0 | 1 | 0,16 |
| Thumbnail | 37,9 | 6,2 | 17,6 | 1,9 | 0 | 0 | 0,18 |
| SEO | 32,5 | 4,2 | 10,0 | 2,8 | 0 | 1 | 0,12 |
| Final Video | 25,4 | 1,0 | 5,9 | 8,3 | 0 | 1 | 0,07 |

İki yoğun bölge (kanıt girişi; görsel/video/thumbnail iş akışındaki sekme geçişleri) + iki statik bölge (konular→senaryo→ses: ekran okunuyor).
**En çok tekrar izlenen bölümler en statik olanlar.**

## 3. Hedef tempo tablosu (editör veya Remotion/ffmpeg hattı için)

| Segment | Referans | HEDEF | Uygulama |
|---|---|---|---|
| **Hook 0:00–0:10** | 9,2 sn'de 6 görsel kaynak; değişimler 1,9/3,3/4,8/7,0/8,0/9,2 sn | 5–7 değişim (her 1,2–2 sn); ≥ 3 kaynak türü (meme/B-roll, kinetik yazı, siyah başlık kartı, ekran kanıtı); ilk ekran kanıtı ≤ 0:08 | Remotion `<Sequence>` 30–60 kare; kinetik yazı 6–8 kare/kelime |
| **Kanıt bölümü ≈0:10–3:00** | 31,6 değişim/dk, 12,8 çekim/dk, 3,7 zoom/dk, her 17 sn'de ek | 25–35 değişim/dk; söylenen her sayıya 1 zoom (2–4/dk); her 15–30 sn'de 1 ek; 3:00'ten önce kendi bitmiş ürünümüzden 8–12 sn teaser (kendi sesiyle) | zoom keyframe 100→155 %, 12–20 kare, ease-in-out; tut 90–120 kare; çıkış 9–15 kare |
| **Öğretim adımı (ekran kaydı)** | 16–38 değişim/dk; zoom yok; 32 sn'ye kadar statik | 20–30 değişim/dk (motive UI hareketleri sayılır); tam kare ≥ %70; **kopya-dışı ekranda ≤ 8 sn statik**; tek çekim ≤ 45 sn | statik > 8 sn ise: seçim, scroll, 1,3× itme veya destek ekranına kesme |
| **Kopyalanacak ekran (prompt/ayar/senaryo)** | 8–20 sn statik; en çok tekrar izlenen | **8–15 sn tutmaya izin var** ama metin mobilde okunur olmalı: gövde < %2 H ise 1,5–1,7× punch-in; alan adını söyle | tutma = cümle uzunluğu; cümle ortasında kesme |
| **Bekleme / üretim süresi** | 17 sn spinner (dip 0,20); bazıları hızlandırılmış | ≤ 1 sn'ye kırp veya 4–8× hızlandır; > 3 sn ise CTA veya sting | — |
| **Sonuç açılışı** | sting → "şimdi bak" → sonuç 2–5 sn | 0,3–0,5 sn boşluk/sting → (ops.) 1,3–1,6× punch-in → 2–4 sn tut | — |
| **CTA overlay** | 2 abone animasyonu (3,4–3,9 sn, arka plan %20 parlaklık); 2 neon-yeşil hedef kartı | her 6–8 dk'da 1 animasyonlu CTA, sadece bekleme/düşük bilgi anında; kopyalanan prompt üstüne asla | karartma: siyah %75–80 + vinyet |
| **Tam ekran yazı kartı** | ilk 9 sn'de 3, sonra sadece CTA kartları | hook kartları + CTA kartları; gövdede bölüm kartı yok | 0,8–1,5 sn |
| **Meme / B-roll** | 3 + 1 sticker, hep birebir anahtar kelimede | uzun tutorial'da 2–3 dk'da 1; ≤ 2–5 sn; birebir kelimede; özgün/lisanslı; silah yok | — |
| **Üretilen varlık demosu** | ses 24 sn, hareket 5,7 sn, final teaser 8,7 sn, final 58,9 sn | her üretim adımından sonra 4–8 sn demo; ses örneği 5–15 sn; final 45–75 sn | video çıktısı: siyah üstünde %78 W, 5–6 sn, kendi sesi |
| **Bitmiş ürün (Mod F)** | ~8,3 sn'de bir görsel, kelime kelime altyazı, vinyet, 2 sert geçiş | 5–7 sn'de bir görsel (min 2,5, maks 10); 3–6 kelimelik altyazı; ≤ 2 stilize geçiş/dk; görsel başına %4–8 itme | bkz. `07` |
| **Ses** | 200 wpm, %94 kaplama, −19,4 LUFS, LRA 2,8, SFX yok | 170–190 wpm (TR 150–170); > 0,5 sn boşlukları kes (ön-reveal hariç); **−14…−16 LUFS**; yatak müzik ya yok ya −30…−35 dB altta; sting en fazla +6…+10 dB konuşma üstü | ffmpeg `silenceremove`, `loudnorm=I=-15:LRA=4` |
| **Geri dönüştürülmüş B-roll** | girişte aynı 2–7 sn kanal-gezinti çekimleri 2–3× | izinli ama her tekrarda kırpma/zoom değiştir | — |

## 4. Zoom spesifikasyonu (referanstan ölçülen)

| Tür | Faktör | Hareket | Tutma | Tetik |
|---|---|---|---|---|
| Punch-in | **1,45–1,67× (tipik 1,55×)** | 0,3–0,7 sn S-eğrisi (ilk 0,1 sn'de ~%15, ortada ~%70, son 0,2 sn yerleşme) + aynı anda pan | 3–4 sn (= bir cümle) | anlatıcı ekrandaki sayıyı/başlığı/alanı **söyledikten 0–1 sn sonra** |
| Yavaş itme | 1,12–1,32× | 1–2,7 sn lineer/ease-out | sayfa değişene kadar | "şu sayfaya bak" anları |
| Parametre zoomu | 1,67–1,70× merkez | 1,4–1,8 sn ease-in-out giriş, 2,5–3 sn çıkış | 4–20 sn (değer canlı yazılırken) | değiştirilecek tek düğme (ör. "30") |
| Zoom-out | her zaman tam %100'e | 0,3–0,5 sn | — | bir sonraki cümle |

- Asla kırpılmış kareye **sert kesme** yok; hep animasyonlu.
- 14 zoom'un hepsi 0:16–4:14 arasında; sonrası 1:1. Kırmızı kutu sadece 2 kez, hep zoom ile, ~2 px `#FF0000`.
- Referansta tek araç: CapCut keyframe ya da Screen-Studio tarzı otomatik zoom (pikselden ayırt edilemez).

## 5. QA kapısı — `scripts/edit_rhythm_qa.py`

```bash
python scripts/edit_rhythm_qa.py render/final.mp4 --profile tutorial --out qa_out
python scripts/edit_rhythm_qa.py render/final.mp4 --profile animated --out qa_out   # Mod F ürün videosu
```
Çıktı: `events.csv`, `minutes.csv`, `report.json` + PASS/FAIL tablosu. Bağımlılık: ffmpeg + numpy + Pillow (OpenCV yok).
Referansta 3 dk 14 sn'de çalıştı ve bu rapordaki sayıları yeniden üretti (25,5 değişim/dk, 8,7 çekim/dk, medyan 2,6 sn, en uzun 31,9 sn, −19,4 LUFS).

| Profil | değişim/dk | çekim değ./dk | medyan çekim | maks statik | > 8 sn statik |
|---|---|---|---|---|---|
| tutorial | 20–45 | 6–18 | 1,5–5,0 sn | 15 sn | ≤ 6 / 10 dk |
| animated | 15–40 | 5–12 | 3,0–9,0 sn | 10 sn | ≤ 3 / 10 dk |

Kural: FAIL varsa `holds_over_limit` listesindeki zamanlara itme/zoom/kesme ekle ve yeniden render et.
Not: referansın kendisi tutorial profilinde "en uzun statik" kontrolünden **bilinçli olarak** kalır (31,9 sn).
Koyu UI'larda eşik `frac > 0.02` → `0.015`.
