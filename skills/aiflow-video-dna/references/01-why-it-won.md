# 01 — Neden kazandı? (kanıt + sıralı başarı faktörleri)

Referans: AI Flow (@AIFlowOfficial) — "How To Make Videos Like Nick Invests With AI (High RPM Finance Niche)"
(SRjm9tvMHhs · 9 Mart 2026 · 22:52 · 144.518 izlenme · 4.498 beğeni (%3,1) · 133 yorum · Hintçe/Urduca anlatım + YouTube otomatik İngilizce dublaj).
Kaynak raporlar: `deep-research/01`, `03`, `04`, `06`.

## 1. Rakamlar (ölçüldü)

| Metrik | Değer | Not |
|---|---|---|
| Kanal medyanı | 14.000 izlenme (n=108) | video kanalın 8. en iyi videosu |
| Outlier katsayısı | **10,3×** kanal medyanı · 6,6× son 12 ay · 4,8× ±10 komşu video | #1 değil (#1 = 278K "AI Survival ASMR") |
| Abone | 50,9K (metadata'daki "509" parse hatası); çekim anında ~31K | |
| Dağıtım | **YouTube Collaboration: 4 yaratıcı** (AI Flow, Oriva AI, AI Man, Ai Dadaji) | collab medyanı 47K vs solo 8K (aynı dönem, 5,9×) — korelasyon, nedensellik değil |
| Konu serisi | Finans = kanalın en iyi konusu (medyan 45K) | önceki finans hitleri: 146K ve 230K |
| Süre etkisi (kanal içi) | <8 dk 2,95K · 8–12 dk 6,65K · 12–18 dk 25K · 18–25 dk 35,5K · >25 dk 38K | uzun "full course" kazanıyor |
| Başlık kalıbı | "…Videos Like {X}" medyanı 27K; "\|" kuyruksuz olanlar 52,5K vs kuyruklu 17K | |
| Yorumların %33'ü | PDF / prompt istiyor | izleyici videoyu **kılavuz** olarak kullanıyor |

## 2. "En çok tekrar izlenen" grafiği ne söylüyor

Grafik **tutma (retention) değil**, geri-sarma yoğunluğudur. Yine de çok net bir desen var:

| Zaman | Değer | Ekranda |
|---|---|---|
| 11:26–11:40 | **1,00 (zirve)** | bitmiş senaryo Google Docs'ta (bölüm başlıkları görünür) → "Voice" bölümü başlıyor |
| 11:40–12:35 | 0,45–0,70 | ücretsiz TTS ayarları (Single speaker, style instruction, ses "Charon") |
| 15:19–15:47 | 0,70–0,85 | Grok ile durağan karakter → konuşan klip (tek "vay" anı) |
| 18:04–18:18 | 0,53 | CapCut'ta zoom animasyonu + otomatik altyazı tıklama yolu |
| 07:05–07:19 | 0,45 | konu prompt'undaki başlık kalıpları okunur halde |
| 16:55–17:50 | **0,03–0,06 (dip)** | sadece konuşma, kopyalanacak bir şey yok |
| 0:00–3:12 | ~0,10 | giriş (bir kez izleniyor — normal) |

**Kural:** tekrar izlemeyi *kesme hızı değil, ekrandaki kopyalanabilir eser* belirliyor (prompt, ayar, tıklama yolu, üretilen sonuç).
Görsel değişim yoğunluğu ile tekrar izleme korelasyonu **zayıf negatif** (ρ −0,11 / −0,18; bölüm bazında r −0,05). Statik saniye
oranı arttıkça tekrar izleme düşüyor ama sadece "konuşma + kopyalanacak bir şey yok" ekranlarında (r −0,41, 03:12–09:25).

## 3. Başarı faktörleri — sıralı (kanıtla)

1. **Çok kanallı dağıtım (Collaboration, 4 yaratıcı).** En büyük yapısal etki; ilk hızı partner kanalların akışı sağlar.
2. **Kanıtlanmış para konusu + seri ivmesi.** Finans serisinin 3. büyük videosu; thumbnail etiketi 230K'lık hitle birebir aynı ("FINANCE NICHE / FULL COURSE").
3. **İsimli-varlık başlığı.** Zirvede olan bir kanalın adı ("Nick Invests": 184 video, 155K abone, 5 ayda ~1M izlenme) → arama + önerilenlerde komşuluk + "zaten kanıtlanmış" güveni.
4. **Açık para vaadi.** Başlıkta "High RPM", thumbnail'de para yığını, 1. dakikada RPM hesabı ($5–15 RPM × 668K izlenme ≈ $3.340), "uzun video = daha çok reklam" argümanı.
5. **Thumbnail sunucuyu değil ÇIKTIYI satıyor.** 4 örnek mini-thumbnail ("bunu yapacaksın"), "FULL COURSE", araç logoları + yükselen izlenme kartı.
6. **Video = kopyalanabilir kılavuz.** 7 prompt + ~14 ayar/hile → her ~53 sn'de bir kopyalanabilir öğe; 11 tek-kelimelik adım bölümü; her adım ücretsiz araçla.
7. **İzleyicinin her engelini sırayla kaldırıyor.** Fikir yok → prompt · İngilizce yok → "kolay İngilizce" + AI ses · beceri yok → "çocuk bile yapar" · bütçe yok → ücretsiz araçlar · başarısızlık korkusu → kamerada hata→düzeltme.
8. **Kaynak paketi + beğeni hedefi.** PDF 7 kez anılıyor, nasıl alınacağı son 60 sn'de ("200 Likes" kartı). Beğeni %3,1. Bedeli: teslim edilmeyen link → yorumların üçte biri şikâyet.
9. **Otomatik İngilizce dublaj.** Yorumların %42'si İngilizce → kitle Hintçe/Urduca konuşanların dışına taşıyor.
10. **Zamanlama + evergreen sorgu.** "…Invests" finans-animasyon dalgası zirvede; "how to make videos like {büyüyen kanal}" sorgusu model kanal büyüdükçe yaşıyor (hâlâ günde ~640 izlenme).

## 4. Edit başarının nedeni DEĞİL — ama işini yapıyor

- Edit iki hızlı: **giriş (0:00–3:12) yoğun** (31,6 değişim/dk, 12 zoom, her 17 sn'de bir ek), **gövde (3:12–21:50) çıplak ekran kaydı** (zoom yok, süs yok, uygulama değiştirerek doğal çeşitlilik).
- Giriş, ilk kez izleyenin "kalayım mı" kararını veriyor; gövde "gerçek, takip edilebilir, ben de yaparım" hissini veriyor.
- Kopyalanacak ekranları hızlı kesmek muhtemelen **zarar verir** (tekrar izlenen bölümler daha statik: %41 vs %27).
- Ses metronomdur: ~200 kelime/dk, %94 konuşma kaplaması, 21:50'de sadece 11 duraklama.

## 5. Kopyalamaya DEĞMEYEN zayıflıklar (iyileştir)

| Zayıflık | Kanıt | Bizim düzeltme |
|---|---|---|
| Prompt'lar telefonda okunmuyor (yükseklik %1,2–1,5) | 29–44 yorum "PDF nerede" | kopyalanacak blokta 1,5–1,7× punch-in veya paket linkini yüklemede ver |
| PDF söz verilip teslim edilmedi | şikâyet yorumları | link yüklemede açıklama + sabit yorumda; asla "söz ver, tut" yok |
| 17–32 sn statik bekleme/okuma ekranları | o kovalar 0,20–0,21 | bekleme ≤ 8 sn (hızlandır/kes) |
| 112 sn kesintisiz tek çekim | bölgenin en zayıf kısmı | tek çekim ≤ 45 sn |
| Thumbnail'de geri dönüştürülmüş "189K VIEWS" | 3 thumbnail'de aynı sayı | sadece doğrulanabilir sayı |
| Rakip kanalın gerçek thumbnail'leri + tanınmış çizgi film karakterine benzeyen maskot | IP riski | özgün maskot, kendi örneklerimiz |
| Silahlı meme | 10:53 | zararsız özgün meme |
| Gizlilik sızıntısı (dosya seçici, indirme paneli) | 15:30–15:31, 14:46 | yayın öncesi blur kontrolü |
| Ses dosyası sessiz hata verdi, içerik kaybı | 10:56 WAV → 6:44 export | TTS parça ≤ 2.500 karakter + boşluk kontrolü |
