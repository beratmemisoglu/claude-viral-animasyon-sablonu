# 05 — Görsel dil, animasyon ve kurgu ritmi

Kaynak: `deep-research/C-visual-animation-rhythm.md` (11 video, kontak sayfaları, scdet kesme ölçümü, 1 fps luma/doygunluk). Bileşenler: `templates/remotion/`.

## 1. Asıl bulgu: görsel kalite gerekli ama yeterli değil

Aynı kanalın flop'u görsel olarak hit'iyle birebir aynı (aynı rig, set, palet). Ölçülebilir farklar başka yerde:
- ConChaser flop'u: konuşma boşlukları sürenin %19'u (343 duraklama, hit'te 1), süre +%38, güç etiketi kutusuz küçük bir "1".
- Miko flop'u: güç kişide değil nesnede (uçan araba), kurgu aşırı hızlı (32 kesme/dk, medyan plan 1,2 sn).
- Iflord flop'u: hook'ta somut olay yok, arka planlar boş.

## 2. Kurgu ritmi: iki profil

Hit'ler tek sihirli sayıya değil, iki profile ayrılıyor. Video başında birini seç (`shots.json` → `profile`) ve video boyunca koru.

| Parametre | Profil A "hızlı hikâye" | Profil B "anlatı" |
|---|---|---|
| Örnek | Future Wealth 28/dk, Lie Count 24,8/dk, Heart 19,5/dk | Immortal 8,4/dk, Snail 6,8/dk, Breathe 9,5/dk |
| Kesme/dk | 18–26 (hedef 22) | 8–13 (hedef 10) |
| İlk 15 sn | 5–8 kesme | 3–6 kesme |
| Medyan plan | 1,7–3,0 sn | 3,9–5,5 sn |
| Maksimum tutuş | ≤10–18 sn | Uzun tutuş yalnız duygusal zirvede (30–55 sn) |
| Son 60 sn | %15–30 yavaşla | %30–60 yavaşla |
| Ne zaman | Sosyal sayı ailesi, çok karakterli günlük hayat | DUAL beden, zaman/ölçek, felsefi |

**Sert sınırlar** (doğrulayıcı reddeder):
- >30 kesme/dk ya da medyan plan <1,5 sn (Tesla flop).
- İlk 15 sn'de >10 kesme.
- 10 sn'den uzun planda kamera hareketi + etiket/overlay/poz değişimi yoksa (Electricity flop: 17 boş uzun plan).

**Reaction döngüsü (A):** geniş 2 sn → yakın reaction 1–2 sn (ifade 1 karede değişir) → insert 1–2 sn → geniş ya da kart. Her 2–4 kesmede bir reaction.

## 3. Açılış standardı (11/11 videoda)

1. Kahraman **0. saniyede**, kadrajın ≥%15'i. Logo, intro, kanal kartı yok.
2. Güç ilk **10 sn** içinde görselleştirilir (hedef ≤5 sn) ve **kişiye bağlıdır** (etiket, aura, sayaç).
3. Başlık kartı cold open'dan sonra **25–35 sn** arasında ve ≤4 sn, ya da hiç yok.

## 4. Güç görselleştirme kataloğu (12 teknik)

| # | Teknik | Uyduğu premise | Bileşen |
|---|---|---|---|
| 1 | **Kafa üstü sayı etiketi** (koyu kutu, beyaz rakam, pop) | Herkesin X'ini görmek | `HeadLabel` number |
| 2 | **Damga sayaç + son hane flip** | Birikimli sayı (yalan, günah) | `HeadLabel` (flip eksik) |
| 3 | **Renk aurası** | Duygu/niyet okuma | eksik (`aura` varyantı) |
| 4 | **Kalıcı HUD sayacı** | Kovalamaca, mesafe, geri sayım | overlay `counter` |
| 5 | **Köşe zaman rozeti** ("GÜN 1", "10. YIL") | Zaman atlayan anlatı | overlay `counter` |
| 6 | **Sayı kartı dolumu** (0→N, glow) | Ölçek şoku | `SceneInfoCard` counter |
| 7 | **"Normal vs SEN" karşılaştırma** | Fiziksel süper yetenek | `SceneInfoCard` bars |
| 8 | **Cihaz arayüzü** (saat, monitör) | Biyolojik yetenek | sahne içi prop (elle) |
| 9 | **Hareket izi / yay** | Kusursuz isabet | elle |
| 10 | **İlerleme ızgarası** (N kişiden k'sı) | "Her seferinde", oran | `SceneInfoCard` grid |
| 11 | **Kronometre / gösterge** | Süre limiti | elle |
| 12 | **Sayı değişimi = plot twist** | Gelecek değişebilir | `HeadLabel` from→value |

Kural: teknik 1–3 (kişiye bağlı, sürekli görünür) en çok izlenen dört videonun üçünde var. Flop'larda güç ya nesnede ya soyut ya da küçük ve kontrastsız.

**Lacivert infografik kart:** 8/8 hit'te var. Her 60–120 sn'de bir, videoda 6–15 kart. Başlık (sarı caps) + grafik + kaynak satırı. `scene: "infocard"` + `card` alanı.

## 5. Renk ve ton

- Hit kareleri **orta-koyu**: luma 60–119 (medyan ~85), doygunluk 65–145 (medyan ~117).
- Palet (`theme.ts`, özgün, hiçbir kanalla aynı değil): alacakaranlık mürdüm → amber gökyüzü, mürdüm binalar, mürekkep laciverti gece, krem kafa, tek sinyal rengi nane-turkuaz `#2EE6C5`, tehlike `#FF4D5E`, vurgu sarısı `#F6C445`, infografik `#141B33 → #0B1022`.
- **Ölçüldü (smoke test, sokak sahnesi):** luma 89, doygunluk 99. Hedef luma 70–105, doygunluk 95–135. İlk palet denemesi (kum-gri) luma 113, doygunluk 33 çıkmıştı; düzeltildi.
- Kadrajda bir anda tek sinyal rengi.

## 6. Metin ve altyazı

- **Kelime-kelime karaoke altyazı hiçbir hit'te yok.** Uzun formda `captions: off` (varsayılan). `word` yalnız Shorts kesimlerinde.
- Metin etiket olarak kullanılır: sayaç, köşe rozeti, pill, sarı vurgu kelimesi, konuşma balonu. Yoğunluk 6–12 metin olayı/dk, her biri ≥1 sn.
- Türkçe caps metin İngilizceden %25–40 uzun. 96–120 px'te 1080p genişliğe ~16–18 karakter sığar; uzunsa iki satır ya da 80 px.
- Onomatope: "GÜM!", "VIIN!", "PAT!". Tabelalar: FIRIN, ECZANE, BAKKAL, BANKA; marka yok.
- Büyük harf için `toLocaleUpperCase('tr-TR')`.

## 7. Kamera ve geçiş

| Preset | Değer | Durum |
|---|---|---|
| push (yavaş) | %1–1,5/sn | var |
| push (drama) | %3–5/sn, 2–4 sn | var (rate) |
| snapZoom | 0,25–0,4 sn'de 1,0→1,8× sayıya | eksik |
| blurIn | 6 kare, blur 18→0 | eksik |
| whip | 6 kare yatay + motion blur | eksik |
| shake | 4–6 px, 8 kare | eksik |

Geçişler: ≥%85 sert kesme; mekân değişimi 0,5 sn çapraz geçiş ya da kesme + köşe rozeti; güç tetiklenmesinde 1–2 kare beyaz flaş (video başına ≤6); zaman atlamasında `dip`. Wipe, 3D küp, glitch yok.

## 8. "Tekrar izlenebilir kare"

Heatmap verisi yoktu; yorum zaman damgalarından çıkarıldı (düşük güven). En çok anılan üç an türü:
1. Güç kuralını kıran ya da ters çeviren gag (kırmızı auralı kedi bardağı deviriyor).
2. Sayı/ölçek şoku (etiket 64,8 milyardan düşüyor; sayaç tırmanıyor).
3. Duygusal kırılma (kendi sayını aynada görmek).

Kural: her 60–90 sn'de bir sayı/etiket değişim anı planla; ekranın merkezinde, 2–4 sn, snapZoom ya da flaş ile.

## 9. Ses

- Entegre ses −14 LUFS ±1. VO boşlukları sürenin <%3'ü; ilk 60 sn'de ≥0,35 sn sessizlik ≤1 (ConChaser flop'unda 24 vardı).
- Kasıtlı sessizlik yalnız zirvede (Immortal 6,2 sn, Snail 7 sn).

## 10. Bileşen durumu (E iskeleti + bu birleştirme)

| Bileşen | Var | Eksik (2. sürüm) |
|---|---|---|
| `StickFigure.tsx` | FK rig, 8 poz, 6 ifade, yürüme, kahraman atkısı | dolgu gövde (7/7 hit), rim light, `meh`/`smug` ifadesi, göz kırpma, ağız flap, `handOnHead`/`reachOut`/`wave`/`lieDown`, yakın plan modu |
| `HeadLabel.tsx` | pill, count-up, TR biçim, tonlar | `stamp`, `aura`, hane flip, üstü çizili, delta rozeti |
| `Crowd.tsx` | seed'li N figür, derinlik, etiket havuzu | silüet uzak sıra, grid dizilimi, sıralı pop, sayım pill'i |
| Sahneler | Street, Office, Home, School, Transit, Wedding, **InfoCard (yeni)** | Cafe, DOF katmanı, dusk varyantı, TR tabelalar |
| Kamera | static, push, pull, pan | snapZoom, blurIn, whip, shake, OTS |
| Overlay | card, title, lower, counter (köşe rozeti stiline çevrildi) | vurgu kelimesi, konuşma balonu, CTA kartı |
| `Caption.tsx` | karaoke | varsayılan artık `off` |
| `theme.ts` | **ölçülmüş palet (yeni)** | — |

İlk video bu eksiklerle çıkabilir; en büyük kalite kazancı sırasıyla dolgu gövde + rim light, `HeadLabel` flip/stamp, snapZoom.

**Özgün karakter kuralı:** kanallarda görülen dört kafa tipini kullanma (siyah daire + beyaz göz; beyaz-leylak daire + kıvrık saç; parlak siyah küre + kapüşon; leylak küre + kalp). Bizimki: krem kafa + turuncu atkı. Hedef: krem "yumurta" kafa + dolgu yelek.

## 11. Maliyet

| İş | İlk video | Şablon oturunca |
|---|---|---|
| Rig + sahneler (tek sefer) | 14–20 sa | 0 |
| Shot list | 3–4 sa | 1,5–2 sa (LLM taslak + düzeltme) |
| İnfografik kartlar | 3–5 sa | 1–2 sa |
| Render + QA | 1–2 sa | 1 sa |
| **Video başına** | **14–22 sa** | **6–10 sa** |
