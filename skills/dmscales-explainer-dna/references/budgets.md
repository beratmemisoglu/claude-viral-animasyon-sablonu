# Süre ve kelime bütçeleri + doldurulabilir iskeletler

Kaynak: `SISTEM.md` §11 (çözülen çelişki: 180 sn için 480–540 TR kelime; son uzunluk ElevenLabs çıktısının gerçek süresine göre kesilir), `01_shorts_algo_180s` §10 (14 vuruşluk şablon), `02_longform_algo_300s` §10 (19 vuruşluk şablon).

Hız varsayımı: Türkçe ~170 kel/dk (QC varsayılanı `--wpm 170`). Gerçek ses gelince ölçülen hızla yeniden çalıştır. **Başlıktaki N = gerçek süre**; ses N'den uzunsa metni kıs, kısaysa bir teşhis maddesi/rakam ekle (hızlandırma ile uydurma, ±%3'ten fazla).

## 1. Beat bütçesi

| Beat | 120 sn (~330–360 kel.) | 180 sn (~480–540 kel.) | 300 sn (~800–880 kel.) |
|---|---|---|---|
| A0 kapı + mekanizma + isim + taktik | 0–20 | 0–25 | 0–30 |
| Aksiyom + gizli sayaç | 20–30 | 25–35 | 30–60 |
| A1 test (isim, grafik, teşhis) | 30–60 | 35–80 | 60–145 |
| Yeniden çerçeve | A1 içinde | 65–80 | 130–145 |
| Ana kural + metrik + eşik | 60–75 | 85–110 | 145–220 (+ ~%55'te 10 sn orta-CTA) |
| A2 birikim | — | 110–127 | 220–245 |
| A3–A4 kırılma + doruk | 75–100 | 127–148 | 245–275 |
| Uyarı | A4 içinde | 148–160 | 275–285 |
| Köprü + CTA | 100–120 | 160–180 | 285–300 |
| Ünite sayısı | 3–4 | 5 | 6–7 |

Kelime ≈ saniye × 2,85 (170 kel/dk). Örn. 180 sn'de A0 (25 sn) ≈ 70 kelime.

## 2. İskelet — 180 sn (ana format)

```
### A0 · Giriş kapısı
[KAPI] Yeni bir [HESAP/BAŞVURU] açtığında olan ilk şey şu: [SİSTEM], [GİZLİ KONTROL].
[MEKANİZMA] Eğer [OLUMLU KOŞUL], seni yaklaşık [RAKAM-1] kişiye/birime gösterir.
[TEŞHİS] Ama [OLUMSUZ KOŞUL]sa, [CEZA SONUCU].
[İSİM] Buna [MEKÂN METAFORU-1] deniyor.
[TAKTİK] Bundan kaçınmak için [TAKTİK-1a], [TAKTİK-1b], ama en önemlisi [TAKTİK-1c].
(EKRAN: NASIL DÜZELİR: başlığı + maddeler)
[AKSİYOM] Çünkü [SİSTEM]in umursadığı tek bir şey var: [GÜDÜ]. Daha çok A, daha çok B demek.
[SAYAÇ] Bunların hepsi [GİZLİ SAYAÇ] denen gizli bir ölçüye gidiyor. Kısacası, [TEK CÜMLE TANIM]. Düşükse [SİSTEM] riske girmek yerine başkasını öne çıkarır.

### A1 · Test aşaması
[KAPI] [İLK EYLEM]i yaptığın anda …
[MEKANİZMA] … her seferinde farklı bir [RAKAM-2]'lik gruba …
[İSİM] İnsanlar buna [RAKAMLI MEKÂN METAFORU-2] diyor.
[MEKANİZMA] Yeni [hesap]ların grafiği hep aynıdır: yavaş bir başlangıç, bir sıçrama, sonra düz bir çizgi.
(EKRAN: grafik)
[TEŞHİS] [X] [BANT-A]'da takılıyorsa sebep şunlardan biri.
(EKRAN: 3 madde — seslendirilmez)
[TEŞHİS] Ama [BANT-B]'deysen sebep şunlardan biri.
(EKRAN: 3 madde — seslendirilmez)
[ÇERÇEVE] Herkes [METAFOR-2]'ye söylenir ama aslında bu iyi bir yer, çünkü [SİSTEM]in sadece daha fazla veriye ihtiyacı var.
[TAKTİK] [Herkese hitap eden içerik / geniş kitle taktiği] + somut örnek.
[KURAL] [SİSTEM] her şeyden çok [ANA METRİK]e bakar. Bu grafiği olabildiğince düz, olabildiğince yüksek tutman lazım.
(EKRAN: metrik kartı + eşik rakamları)
[UYARI] Ama [YASAK DAVRANIŞ] yapma; [kural/politika]ya aykırı ve [SAYAÇ]ını düşürür.

### A2 · Birikim
[KAPI] [EYLEM]ledikçe …
[MEKANİZMA] … [KÜMÜLATİF SİNYAL] … [SAYAÇ] en çok bununla artar.
[TAKTİK] Yani olabildiğince hızlı [HEDEF] için [RİTİM/SIKLIK] gerekiyor.

### A3 · Kırılma
[KAPI] İlk [BAŞARI]ndan sonra bir tür [EVRE METAFORU]na girersin.
[MEKANİZMA] [SİSTEM] sonraki [şey]lerini daha hızlı [ödül], çünkü güvenilebileceğini kanıtladın.
[UYARI] Arada yine [CEZA-METAFORU]na düşebilirsin, ama [koşul]sa daha hızlı çıkarsın.

### A4 · Yüksek durum
[KAPI] [SAYAÇ] yeterince yükseldiğinde [SİSTEM] seni [CEZA]lamayı bırakır.
[MEKANİZMA] Oradan sonrası sadece [EYLEM] meselesi; [BÜYÜK RAKAM / NİHAİ ÖDÜL].
[UYARI] Ama bu noktaya geldiğinde her zamankinden çok çalış. Şimdi tembelleşirsen [KAYIP / baştan başlarsın].

### Köprü + CTA
[KÖPRÜ] Ama en önemli şey [ASIL ÖN KOŞUL]. Aynı şeyi yapan on kişi varken [HEDEF] zor; o durumda [SİSTEM] en güvendiğini öne koyar.
[CTA] Bu konuda yardım için [VARLIK] hazırladım, sürekli güncelliyorum. Kendim de kullanıyorum.
[CTA] Ücretsiz [inceleme/yol haritası] istersen [TOPLULUK]a katıl.
```

## 3. İskelet — 120 sn (dikey; 3–4 ünite)
A0 (kapı+isim+taktik, 0–20) → Aksiyom+sayaç (20–30) → A1 tek bantlı teşhis + çerçeve 1 cümle (30–60) → Kural+eşik (60–75) → A3–A4 tek blok + uyarı (75–100) → Köprü+CTA (100–120). Çerçeve A1 içinde 1 cümle. Kavram ≥8.

## 4. İskelet — 300 sn (6–7 ünite, Longform şablonundan)
180 sn iskeletine ek olarak:
- A0'dan sonra **"yükleme anı taraması"** aşaması (üçlü fiil: "yazıya döker, tarar, sınıflandırır") ve **"ilk 24–48 saat"** profil aşaması.
- A1 içinde **metrik bloğu** (145–220): "[SİSTEM]in bakacağı 3 şey var, ilki [M1]… Şöyle düşün: [metafor]… Ortalama [X–Y], [Z]'nin altıysa [SİSTEM] kesinlikle itmez." → "Sıradaki [M2]; bu [M1]'den çok daha önemli…" → **önem merdiveni**: "en önemli" → "çok daha önemli" → "en güçlü sinyal" (en güçlüsü sona).
- ~%55'te 10 sn **orta-CTA** (aynı varlık, içerikten çıkan köprüyle: "en iyi öne çıkma yolu bir niş seçmek; bunun için …").
- Liste bombardımanı: "Bunun ötesinde [SİSTEM] bir sürü şey izler: a, b, c, d, e…" (tek cümle, ekranda 2 sütun).
- Önceki videoya ≥2 köprü ("Tıpkı [X]'teki gibi…", "[X]'e göre çok daha affedici").
- Kişisel kanıt yalnız varsa (kullanıcının gerçek sonucu); yoksa atla — uydurma.
