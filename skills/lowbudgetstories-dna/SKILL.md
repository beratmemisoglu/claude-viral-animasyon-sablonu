---
name: lowbudgetstories-dna
description: LOW BUDGET STORIES (@LowBudgetStories, ~1,27M abone, en çok izlenen 10 video 2,4M–6,3M, "Origin of a Doomer", "Life of a Fast Food employee", "Gyms in 2050"…) kanalının beynini — senaryo motoru, görsel makine, kesme ritmi, ses tasarımı, paketleme, izleyici psikolojisi — 5 paralel analist ajanıyla 10 videonun transkript + kare-kare (saniye saniye kontak sayfaları) + nicel ölçümüyle tersine mühendislikten çıkarılmış ÜRETİM + SENARYO + QA sistemi. Çıktı: özgün karakterlerle "Life of a [iş]", "Origin/From A to B" (sözsüz duygusal saga), "[alan] in 2050 / Living in a [sistem]" (distopya), "[aktivite] Addiction Cycle" (döngü) ailelerinde sözsüz-pantomim veya az konuşmalı kısa hikâye videoları; 70'lik vuruş bankası, sözsüz senaryo yazma yöntemi, Remotion katman/preset spec'i, özgün cast brief'i, kesme-ritmi + ses QA script'i (rhythm_qa.py), başlık/thumbnail/açıklama şablonları, yayın öncesi QA ve etik/IP korkulukları. Kullanıcı "Low Budget Stories gibi", "Wojak/doomer videosu tarzı", "Life of a … videosu yaz", "sözsüz hikâye / pantomim senaryo", "meme çizgi film kanalı", "bu kanalın makinesini/beynini kopyala", "senaryo nasıl yazılıyor", "hikâye videosu kurgu ritmi", "kesme ritmi / ses QA", "sıradan adam protagonist kanalı", "kısa animasyonlu hiciv videosu" dediğinde veya bu kanalı/başka bir kanalı aynı yöntemle analiz etmek istediğinde MUTLAKA bu skill'i kullan — skill adı geçmese bile.
---

# Low Budget Stories DNA — "tanıma makinesi" üretim sistemi

Kaynak: 5 analist ajan × 2 video (saniye saniye) + 10 videoluk mercek raporları (2026-10-23). Ham raporlar `deep-research/` (İngilizce), birleştirilmiş Türkçe kurallar `references/`.
**Kopyalanan:** yapı, ritim, ölçüler, karar mantığı. **Kopyalanmayan:** Wojak/NPC/Chad/Pepe vb. meme karakterleri, gerçek markalar/kişiler, oyun/film/YouTuber görüntüsü, ticari müzik, kanalın filigran/bitiş kartı tasarımı, birebir başlıklar. **Her kural "aynı rolü dolduran özgün karakter" demektir.**

## Tek cümlelik DNA
> **Boş yüzlü bir sıradan adamın gündelik acısını ≤6. sn'de göster; tek arzu × 3–8 basamaklı tırmanan engel merdiveniyle (çoğunlukla sözsüz, dünya-içi metinle) ilerlet; gerçek-fotoğraf plakaları üstündeki kaba kesim karakterleri kamerayla animasyona sok (14–24 sınır/dk); süre'nin ≈%84'ünde geri sardıracak bir ifşa/okunur yazıyla öde; maddi durumu asla düzeltme.**

## Neden kazandı (kısa) — ayrıntı `references/01-why-it-won.md`
1. **Tanıma motoru:** izleyicinin yaşadığı acı görüntüyle gösterilir → "orada çalıştım / bu benim" tanıklık yorumları.
2. **Dilden bağımsız:** en çok izlenen 4'ün 2'si sözsüz; konuşmalıların da %25–61'i sözsüz.
3. **Son beşte birde ödeme:** tekrar-izleme zirvesi 8/10'da %77–97, ifşa ya da okunur ekran yazısı.
4. **Dürüst bitiş:** hiçbir video maddi sorunu çözmez (10/10).
5. **Aileler + sprintler + devam:** "Life of a [iş]" = toplam izlenmenin %29'u; hit'ten 1–4 ay sonra kardeş/devam.
6. **Ucuz şablon:** statik kesim + push-in + sabit filigran/fade-in/bitiş kartı ≈16 sa/bitmiş dk.
7. **DİKKAT — zamanlama:** 2023 medyanı 1,60M vs 2026 0,28M; eski hit'in klonları 0,03–0,3×. Motoru kopyala, **şablonu klonlama**.

## Modlar
| Mod | Tetik | Çıktı |
|---|---|---|
| **S-IDEA** | "konu bul", "hangi aile", "seri planı" | konu testi (≥9/12) + aile seçimi + 6 aylık yükleme planı → `02 §11`, `05` |
| **S-SCRIPT** | "senaryo yaz", "sözsüz hikâye", "Life of a … yaz", "saga yaz" | logline → durum-işaret sayfası → merdiven → kurulum→ödeme haritası → shot list → duygu eğrisi → `02`, `03`, `08` |
| **S-PRODUCE** | "üret", "Remotion", "cast çiz", "plaka üret" | özgün cast brief + karakter sayfası + katman yığını + `shots.json` → Remotion planı → `06`, `07` |
| **PACKAGE** | "başlık/thumbnail/açıklama" | 5–10 başlık (şablon etiketli), thumbnail spec + QA kapıları, açıklama iskeleti, sabit yorum → `05` |
| **QA** | "denetle", "ritim kontrol", "yayına hazır mı" | `rhythm_qa.py` çıktısı + `09-qa-checklist.md` PASS/FAIL |
| **ANALYZE** | "bu kanalı/videoyu tersine mühendislik yap" | kanıt paketi + 5 paralel analist + birleştirme → `10-reverse-engineering-method.md` |

## S-SCRIPT iş akışı (adımları atlama)
1. **Aile + süre:** `02 §3` (saga 170–281 sn · iş 211–453 sn · distopya 359–441 sn · döngü ≈421 sn; **>455 sn yok**).
2. **Konu testi:** `02 §11` ≥9/12 ve kriter 1–2 = 2 puan. Distopya için ≤60 gün haber çapası.
3. **Logline = durum değişimi** ("[özgün karakter], C yüzünden A'dan B'ye gider").
4. **Durum-işaret sayfası** (`03 §A` adım 2): kostüm, yüz çizimi, oda, obje, yoldaşlar, grade; ana işaret %50–60'ta döner.
5. **Merdiven:** 3–8 basamak, her biri {saçmalık, maliyet, görünürlük, antagonist büyüklüğü}'nden tam biri; ≤45 sn; protagonist harekete geçince dünya kötü cevap verir.
6. **Şablon yüzdeleri** (`02 §4`) ve **vuruş bankasından** blok başına ≥1 kalıp (`03 §B`) → özgün konuya aktar.
7. **Kurulum→ödeme haritası** (7 dk'da ≥4, 3 dk'da ≥2 çift; 60–240 sn arayla) + gizlenen şey (%80–96'da ≤5 sn insert).
8. **Metin bütçesi** (dünya-içi metin ≤12 kelime/öğe, 4–8 öğe) ve **diyalog** (cümle medyanı 5–8 kelime; protagonist ≤%35 kelime; iç ses ≤3).
9. **Shot list** (`# | t | plaka | karakter durumu | aksiyon | insert/metin | müzik işareti`) + **valans eğrisi** (≥8 anahtar kare) + **müzik haritası**.
10. **Bitiş:** maddi durum aynı; hope (erişim) **veya** açık/döngü (tartışma) — seç ve yaz; valans −3'e değiyorsa ≥2 sn eylem gücü ipucu (`08 §6.5`).
11. **Mute testi + 09-qa-checklist K1/K2/K6.**
Çıktıyı kullanıcıya **Türkçe** ver (diyalog/ekran metni kullanıcının hedef diline göre), tablolar halinde; ham transkript/örnek diyalog kopyalama.

## S-PRODUCE kısa akışı
1. **Özgün cast** (`06 §5.3`): protagonist, yüzsüz kalabalık, "daha yüksek ortamda" rakip, mentor/iç ses, sistem sesi, destek. Nob/Blanks/Vance/Ora *örnek*; kullanıcı kendi tasarımını seçer. Benzerlik kontrolleri **zorunlu**.
2. **Karakter sayfası** `06 §5.4` (18 gövde, 16 yüz, 8 bindirme, 6 el); plaka prompt şablonu `06 §5.5` (gerçek marka/yazı/insan yok, lisans kaydı).
3. **Shot list → `shots.json` → Remotion** (`06 §5.9`): `Shot` bileşeni, presetler (PUSH 1,6 %/sn, SWISH 10 kare, EXPR_SWAP 1 kare, CYCLE_2 5 kare…), vinyet, grade (`06 §5.6`), filigran bizim ad.
4. **Ses:** TTS rol başına ayrı ses, 150–205 WPM, 0,4–0,6 sn boşluk, kuru; müzik 2–4 cue (komedi → idil → karanlık) ya da tek duygusal enstrümantal (sözsüz); **−14 ±1 LUFS** (`07 §9`).
5. **QA:** `python scripts/rhythm_qa.py VIDEO.mp4 --transcript words.json --mode voiced --out qa_out --target-lufs -14 --montage` → exit 0 + `09`.

## PACKAGE kısa akışı
Başlık: 3–6 kelime, 12–32 karakter, konu ismiyle biter, aile şablonu T1–T18 (`05 §2`); thumbnail Düzen A/B/C (`05 §3`); açıklama iskeleti + sabit yorum + 2–3 dikey klip (`05 §4, §6`). **Hit klonlama yok.**

## Dosya haritası
| Dosya | İçerik |
|---|---|
| `references/01-why-it-won.md` | beyin: makine, başarı hiyerarşisi, zayıflıklar, çelişki kararları, hızlı başlangıç |
| `references/02-script-engine.md` | **senaryo motoru:** 12 değişmez, aile şablonları (% süre), merdiven, karşıtlık/callback/gizleme, gag süreleri, pantomim, diyalog zanaatı, yazar analizi, konu testi, anti-kalıplar |
| `references/03-beat-bank.md` | **sözsüz senaryo yazma yöntemi (10 adım)** + 70 vuruş kalıbı + mikro örnek |
| `references/05-packaging.md` | kanal rakamları, başlık anatomisi + 22 şablon, thumbnail ölçümleri + spec, açıklama iskeleti, seri/devam, dağıtım |
| `references/06-visual-build.md` | görsel sistem tabloları, karakter anatomisi, kompozit kuralları, pipeline/maliyet, **yeniden kurma spec'i** (katman yığını, özgün cast, grade, preset'ler, Remotion) |
| `references/07-audio-edit-rhythm.md` | kalibre kesme ritmi, plan dağılımı, ses gramer, SFX envanteri, TTS, **ritim + ses spec'i**, QA script'i |
| `references/08-audience-retention-ethics.md` | yorum madenciliği, tekrar-izleme psikolojisi, duygu yayı, seri stratejisi, **risk/etik/IP**, tutma rehberi, duygusal QA |
| `references/09-qa-checklist.md` | birleşik yayın öncesi kapı (K1–K6) |
| `references/10-reverse-engineering-method.md` | **yöntem:** kanıt paketi, 5 analist ayrımı, birleştirme kuralları, çözülmüş çelişkiler, pratik dersler |
| `scripts/rhythm_qa.py` | kesme-ritmi + ses QA (22 metrik, korpus normları, `--target-lufs`, `--montage`) |
| `scripts/thumbnail_qa.py` | thumbnail piksel QA: parlaklık, sıcak/soğuk payı, koyu-monokrom, amber/coral payı, sağ-alt boş alan, A düzeni parlaklık farkı (exit 1 = FAIL) |
| `scripts/contact_sheets.py` | saniye damgalı 3×3 (1 fps) ve 4×4 (4 fps, ilk 60 sn) kontak sayfaları — frame-by-frame analiz aleti |
| `scripts/transcribe_gpu.py` | faster-whisper GPU toplu transkript (kelime zamanlı) |
| `deep-research/` | ham raporlar: v01–v10 teardown + L1–L5 mercekleri (İngilizce) — çelişkide `README.md` önceliği |

## Altın kurallar (kısa)
1. **Önce aile, sonra şablon, sonra vuruş bankası.** Boş sayfadan yazma.
2. **Ödeme kurulumdan önce planlanır:** kurulum→ödeme haritası ve gizlenen şey yazılmadan sahne yazılmaz.
3. **Sözsüz = tasarlanır:** durum-işaretleri, merdiven, EER planlar, dünya-içi metin; mute testi geçmeden onay yok.
4. **Ölç:** `rhythm_qa.py` + 09 olmadan yayın yok; WARN'ı gerekçelendir.
5. **Özgün + etik:** özgün cast, uydurma marka, kendi/lisanslı müzik, davranış şakası (beden/etnisite değil), can simidi kuralı, destek satırı (`08 §6.5`).
6. **Klonlama, motoru çalıştır:** başarı 2023 zamanlamasına da bağlıydı; hit'in şablonunu 6+ ay sonra klonlama.
7. **Ölçüm > kare kanıtı > yorum.** Güven düşükse "düşük güven" yaz. n=10 korelasyonu nedensellik gibi sunma.
