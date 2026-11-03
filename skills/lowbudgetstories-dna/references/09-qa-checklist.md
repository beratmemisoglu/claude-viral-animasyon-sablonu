# 09 — Yayın öncesi QA kapısı (birleştirilmiş)

Her bölüm yayınlanmadan önce **tüm kapılar geçmeli**. FAIL = düzelt, WARN = bilinçli gerekçe yaz. Ayrıntılı gerekçeler ilgili referans dosyalarındadır (02 senaryo · 05 paketleme · 06 görsel · 07 ses/ritim · 08 duygu/etik).

## K1 — Senaryo (02, 03)
- [ ] Aile seçildi (saga / iş / distopya / döngü) ve şablon yüzdeleri yazıldı; süre aile aralığında, **≤455 sn**.
- [ ] Protagonist ≤0:06'da ekranda; ilk 5 sn'de açıklayıcı cümle yok; **ilk çatışma ≤0:45**.
- [ ] Tek arzu + 3–8 engel basamağı yazıldı; her basamak {saçmalık, maliyet, görünürlük, antagonist büyüklüğü}'nden tam birini artırıyor; **hiçbir basamak >45 sn** (görsel ≤20 sn).
- [ ] ≥1 üçlü kural birimi, ≥1 niyet→engel gagı.
- [ ] **Kurulum→ödeme haritası:** 7 dk'da ≥4, 3 dk'da ≥2 çift; ödeme kurulumdan 60–240 sn sonra; hiçbir ipliği ödemesiz bırakma (ya öde ya ≤8 sn'ye kes).
- [ ] Gizlenen şey **≤5 sn'lik insert'le %80–96'da** açılıyor; ölüm/ihanet/dönüş diyalogla söylenmiyor.
- [ ] Süre'nin **%25–40'ı sözsüz** (saga %100); protagonist kelimelerin ≤%35'ini söylüyor; iç ses ≤3.
- [ ] Bilgi dünya-içi metinle (≤12 kelime/öğe, 4–8 öğe/film); anlatıcı yok.
- [ ] Dakikada ≥1 doğrulanabilir gerçek-dünya ayrıntısı; ≥3 görsel şaka/dk.
- [ ] **Bitişte maddi durum değişmedi**; 4–8 sn tutulan son görüntü ya da vurucuda sert kesme; ≤4 sn siyah; bitiş kartı.
- [ ] Mute testi: ses kapalıyken her basamakta neyin değiştiği anlaşılıyor.
- [ ] Konu testi (02 §11) ≥9/12 ve kriter 1–2 = 2 puan.

## K2 — Duygu/tutma (08)
- [ ] ≥8 anahtar karelik valans eğrisi; her 45 sn'de ≥1 valans değişimi (saga: her 20 sn).
- [ ] En büyük ödeme **%77–90'da**, yeni görüntüde, sert kesmeden sonra; ödeme metni ≤12 kelime, ≥%3,5 kare yüksekliği, ≥3 sn.
- [ ] Her büyük düşüşten ≤10 sn önce bir gülümseme/başarı; en büyük sallantı ≥4 puan.
- [ ] Tez cümlesi (≤25 kelime) ≥6 sn statik tutuluyor.
- [ ] Bitiş ilan edildi: umutlu (erişim) **veya** açık/döngü (tartışma). Valans −3'e değdiyse son %15'te ≥2 sn **eylem gücü ipucu** ya da bilinçli açık bitiş.
- [ ] Devam (zıt valanslı) planlandı; saga'da son 20 sn = sonraki bölümün ilk 15 sn'si.

## K3 — Görsel (06)
- [ ] 1920×1080, 25 fps, tam kare, letterbox yok; 1,2–1,4 sn fade-in.
- [ ] Sürenin ≥%85'i özgün düz-dolgulu kesim karakter + **sabit plaka**; hareketli görüntü ≤%10 ve yalnız ekran içinde.
- [ ] Dudak senkronu yok; ifade değişimi 1 karelik; plan başına ≤3 değişim; fiziksel aksiyon = 2 çizim × 5 kare.
- [ ] Push-in %1,0–2,6/sn, saniyelerin %20–45'inde; kamera sarsıntısı yok.
- [ ] Sert kesme ≥%55 (geçiş olayları); blur plan ölçeğine göre; gölge yok; vinyet köşe/merkez 0,25–0,55.
- [ ] Grade mood tablosuna uygun; dönüşüm hikâyesinde ort. parlaklık ≥+15 puan artıyor.
- [ ] Sol-alt filigran (bizim ad), %60 beyaz, ≈%5 yükseklik; 6–8 sn marka bitiş kartı + 2 bitiş ekranı slotu.
- [ ] Thumbnail'deki karakter/propların hepsi videoda aynı tasarımla var.

## K4 — Ritim ve ses (07) — `rhythm_qa.py` çalıştır
```bash
python scripts/rhythm_qa.py VIDEO.mp4 --transcript words.json --mode voiced --out qa_out --target-lufs -14 --montage
```
- [ ] **Exit 0 (FAIL yok)**; WARN'lar gerekçelendi.
- [ ] Sınır/dk 14–24, plan medyanı 2,2–3,7 sn, max plan ≤10 sn, >8 sn tutuşlar yalnız diyalog/monolog.
- [ ] 0–15 sn ≥14/dk, ilk kesme hedef ≤4 sn (script ≤5,7 sn'yi PASS sayar), 15–60 sn ≥16/dk, tek mekân diyaloğu ≤60 sn.
- [ ] **−14 ±1 LUFS, LRA 10–13, ≤−1,0 dBTP** (kodlama sonrası ölç); ilk 15 sn gövdeden 3–10 LU kısık.
- [ ] Müzik yatağı hikâyenin ≥%85'i; diyalog altında 8 ±2 LU, ducking yok; 1–3 müzik-kapalı pencere (2–5 sn) ve ≤6 gerçek sessizlik.
- [ ] SFX yalnız durum değişimlerinde (konuşmalıda 3–8/dk; sözsüz film 0–1/dk).
- [ ] TTS: rol başına ayrı ses, 150–205 WPM, 0,4–0,6 sn boşluk; debater'lar ≥4 yarım ton farklı; aksanlı antagonist altyazılı.
- [ ] Bitiş kartı sesi = **kendi** imza döngümüz.

## K5 — Paketleme (05)
- [ ] Başlık 3–6 kelime, 12–32 karakter, konu ismiyle biter; "?" / BÜYÜK HARF / emoji / yıl dışında rakam yok; aile şablonundan (T1–T18).
- [ ] Thumbnail: 0 başlık kelimesi, ≤4 sayısal jeton, tek karşıtlık, ana yüz ≥%40 kare yüksekliği, ort. parlaklık 0,38–0,65, sıcak ≥%15 ve soğuk ≥%15 (veya açık iki-dünya bölmesi); **koyu monokrom neon değil** (ort. <0,30 + tek soğuk ton ≥%59 = reddet); sağ-alt 230×110 boş.
- [ ] **Piksel ölçümü:** `python scripts/thumbnail_qa.py thumb.png --layout A|B|C --palette brand-palette.json` → exit 0 (ort. parlaklık, sıcak/soğuk payı, koyu-monokrom, amber/coral payı, sağ-alt boş alan, A düzeninde sol/sağ parlaklık farkı).
- [ ] Aynı thumbnail düzenini ≥6 ay önceki bir videomuzdan farklı konuya klonlamıyoruz.
- [ ] Açıklama iskeleti: ilk 2 satır öncül + aranabilir ifadeler; önceki/sonraki bağlantıları; 5–6 bölüm; müzik kredileri; destek satırı (gerekirse); 8–12 konuya özgü etiket; rakip kanal/marka adı yok.
- [ ] **Sabit** yaratıcı yorumu (1–2 cümle + tek açık soru) hazır; 2–3 dikey klip planlandı.
- [ ] Süre: sözsüz film 170–280 sn, konuşmalı 300–480 sn.

## K6 — Etik / IP / platform (08 §6)
- [ ] **Özgün cast** — meme yüzü, gerçek kişi fotoğrafı, tanınmış karakter benzerliği yok (bkz. 06 §5.3 benzerlik kontrolleri).
- [ ] Gerçek marka/logo/ambalaj/okunur tabela, gerçek platform arayüzü, oyun/film/YouTuber görüntüsü, haber başlığı **yok**; parodi markalar uydurma isim+logo.
- [ ] Müzik özgün ya da yazılı lisanslı; hit şarkı cover/enstrümantali yok; her varlık kaynak+lisansla kayıtlı.
- [ ] Antagonist sistem/alışkanlık; hiçbir cinsiyet/beden/etnisite/milliyet/engel vuruşu; kadın ve erkek yan karakterlere eşit eylem gücü.
- [ ] Kendine zarar ikonografisi/sözü yok (hap/ip/bıçak/"bitirmek"); bağımlılık/yalnızlık/yas bölümünün açıklamasında nötr destek satırı.
- [ ] İlk 30 sn küfürsüz; vice'ler görünür maliyetle; şiddet ekran dışı/slapstick; "çocuklara yönelik değil" ayarı; siyasi distopyada kurgusal devlet.
- [ ] Anlatısal CTA yok (sözlü/ekran); bitiş kartı + sabit yorum dışında yönlendirme yok.

## Sonuç
Tüm kutular işaretli → yayına hazır. K4'ün `rhythm_qa.py` çıktısını (report.json) bölüm klasörüne kaydet; ilk 10 bölümden sonra **kendi** normlarımızı (korpus yerine) bu çıktılardan türet.
