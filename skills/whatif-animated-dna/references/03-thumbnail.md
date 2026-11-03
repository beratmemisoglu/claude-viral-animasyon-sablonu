# 03 — Thumbnail sistemi

Kaynak: `deep-research/A-packaging-ctr.md` §3–4e (100 thumbnail gözle etiketlendi + PIL ölçümü). Üretici: `scripts/make_thumbnail.py` + `templates/thumbnail.svg`.

## 1. İlke: thumbnail ikinci sorudur

Başlık "ne olurdu?" diye sorar. Thumbnail başlığın resmi olmamalı; mekanizmanın **ilk sonucunu** gösterip **ikinci soruyu** açmalı.

| Thumbnail metni | n | Hit | Medyan |
|---|---|---|---|
| İkinci merak açıyor | 21 | %43 | 44K |
| Başlığa sayı/ölçek ekliyor | 33 | %33 | 17K |
| Başlığı tekrar ediyor | 27 | %22 | 24K |
| Metin yok | 3 | %0 | 10K |

| Görsel çelişki | n | Hit | Medyan |
|---|---|---|---|
| Var (gülen yüz + kötü sayı, evsiz + milyar, sakin sen + boğulan dalgıç) | 16 | **%56** | 134K |
| Yok | 68 | %25 | 19,5K |
| Başlık somut + thumbnail çelişkili | 11 | **%64** | 166K |

En iyi örnekler:
- **Lie Count (460K):** "Seni seviyorum" diyen kız, kafasında "9.317 +1". Başlık yalanı sorar, thumbnail "sevgilin de mi?" diye sorar.
- **Future Wealth (482K):** evsiz adamın üstünde 8,7 milyar dolar. Soru: "nasıl?"
- **Secretly Hates (223K):** "BENDEN KİM NEFRET EDİYOR?" + üç etiketli kişi. İzleyici kendi çevresini düşünür.

Flop örnekleri hep başlık tekrarı: "ERASE ANYTHING", "10X FASTER", "PSYCHIC".

## 2. Üç layout (1280×720)

### Layout 1 — Kafa üstü sayı (sosyal sayı ailesi)
- Sen solda (x %5–40, yüksekliğin %70'i), öteki kişi sağda (x %50–90).
- Ötekinin ifadesi sayısıyla **çelişir**: gülümseyen + büyük yalan sayısı.
- Sayı rozeti: kafanın 10–40 px üstü, yükseklik 60–90 px, doygun kırmızı/yeşil zemin, beyaz kalın rakam, ≤12 karakter.
- Metin: üst bant, y %4–26, 2 kelime (1. satır beyaz, 2. satır sarı), 900 ağırlık, 6–8 px siyah kontur. Alternatif: metin yok, sayılar ≥70 px.
- İsteğe bağlı konuşma balonu ≤3 kelime ("Seni seviyorum").
- `make_thumbnail.py` layout **A**.

### Layout 2 — Sonuç cümlesi + tek nesne (DUAL beden, oyun, yenilmezlik)
- Karakter sağda (x %55–95), yüz izleyiciye, sırıtış ya da gülümseyen-yaralı (DUAL).
- Solda tek nesne: kurşun izi, basket potası, para yığını. Toplam öğe ≤4.
- Metin: sol üst, x %3–48, y %5–45, **2 kelime 2 satır**, kesin kip: "ÖLEMİYORUM." / "ASLA ISKALAMAM." / "RESPAWN".
- İsteğe bağlı küçük kırmızı rozet ≤10 karakter: "GÜN 300", "ACI: %0".
- `make_thumbnail.py` layout **C** (yakın yüz) veya **A**.

### Layout 3 — Önce / sonra bölünmüş (ölçek serisi)
- Dikey zikzak bölme x≈%48. Sol sıcak ve normal ölçek, sağ soğuk ve aykırı ölçek.
- Her panelde 1–3 kelime dev yazı; karakter aynı poz, ifade ve ortam değişir.
- Sayı kontrastı mesajdır: "1 TRİLYON %0" ↔ "GOOGOL %100".
- Seride her bölümde bir öğe değişmeli; Alternate You bu şablonu 12 kez aynen kullandı ve yalnız içerik değişen videolar tuttu.
- `make_thumbnail.py` layout **B** kalabalık versiyonu ya da özel SVG.

## 3. QA kapıları (hepsi geçmeli)

| # | Kapı | Eşik | Kanıt |
|---|---|---|---|
| 1 | Parlaklık | Ortalama luma 60–160; siyah piksel (luma<20) ≤%35; beyaz ≤%30 | Siyah >%50 olan 4 thumbnail'in 4'ü flop |
| 2 | Metin | 1–4 kelime | 9+ kelime yalnız editoryal şablonda |
| 3 | İkinci soru | Metin + başlık yan yana okununca yeni bilgi veriyor | REPEAT %22 vs SECOND_HOOK %43 |
| 4 | Çelişki | Bir yüz ifadesi bir sayı/durumla çelişiyor | Sosyal ve DUAL ailede zorunlu |
| 5 | Sadelik | Öğe ≤4; kenar yoğunluğu ≤0,062 | En kalabalık çeyrek %20 hit |
| 6 | Mobil | 320×180'de metin ve sayı okunuyor; yüz ≥%12 alan | `make_thumbnail.py` önizleme üretir |
| 7 | Tutarlılık | Aynı karakter, aynı hoodie/atkı rengi | ConChaser farklı karakterle 19K |
| 8 | Metinsiz yasak | — | Metinsiz 0/3, Jeremy'de 0/5 |
| 9 | Kırmızı | Şart değil; kullanılırsa ≤%5 alan | En az kırmızılı çeyrek %45 hit |
| 10 | Eşleşme | Başlıktaki somut isim karede var | — |

Renk ve parlaklık bir **kapı**, itici güç değil: kanal içinde hit'i açıklamıyor, kanallar arası tabanı açıklıyor. Karakter stili olarak açık kafa + koyu zemin (beyaz yuvarlak kafa %45 hit) okunabilirlik nedeniyle siyah kafadan (%23) iyi.

## 4. Türkçe notlar

- Örnek metinler: "ÖLEMİYORUM." · "ASLA ISKALAMAM." · "KİM NEFRET EDİYOR?" · "SEVGİLİN DE Mİ?" · "SİMİTÇİ: 2 MİLYAR".
- Büyük harfte İ/ı: metni baştan doğru yaz; Python `upper()` ve JS `toUpperCase()` Türkçe değildir. Fredoka 700 latin-ext ile Türkçe glifler doğru çıkıyor (smoke testte doğrulandı).
- Sayı biçimi: binlik nokta (9.317), ondalık virgül.
- Dini, cinsel, askeri şaka yok (bkz. `06-audience-risk-tr.md`).
- Higgsfield polish isteğe bağlı: `--no-text` ile taban üret, `nano_banana_pro` ile 2 aday (~4 kredi), sonra `--base-image` ile yazıyı bizim şablon basar. Kompozisyon bizde kalır.
