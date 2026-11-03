---
name: sim-explainer-dna
description: 12 günde 3,6M izlenen "Why Traffic Stops for No Reason, and How One Driver Can Fix It" (7:28, yüzsüz, kuşbakışı simülasyon + veri-grafiği açıklayıcı) videosunun kare kare tersine mühendisliğinden çıkarılmış ÜRETİM SİSTEMİ. Kullanıcı bir BAŞLIK + KONU AÇIKLAMASI (brif) verir; skill tam bir üretim paketi çıkarır: başlık seçenekleri, 3 hook varyantı, zaman damgalı tam VO senaryosu (18 vuruşluk kanıtlı omurga), sahne sahne storyboard + kurgu planı, simülasyon/animasyon reçeteleri (Remotion/AE), ekran metinleri, geçiş ve ses planı, 3 thumbnail konsepti (PHANTOM JAM formülü) + görsel üretim prompt'u, ritim QA. Kullanıcı "phantom jam tarzı", "trafik videosu gibi", "simülasyonlu açıklayıcı video", "bilim explainer senaryosu", "gündelik bir şey neden böyle oluyor videosu", "Why X happens for no reason", "brif vereyim senaryo/kurgu/animasyon/thumbnail çıkar", "bu sisteme göre video planla", "faceless science video", "mekanizma anlatan animasyonlu video" dediğinde veya bir başlık+konu verip video üretim paketi istediğinde MUTLAKA bu skill'i kullan — skill adı geçmese bile.
---

# Sim-Explainer DNA

Bir başlık + konu açıklamasını, referans videonun (3,6M / 12 gün) kanıtlanmış yapısıyla **çekime hazır üretim paketine** çevirir.

Referansın gücü üç şeyden geliyor; paketin her parçası bunlara hizmet etmeli:
1. **Gizem + güç (agency) vaadi:** "Bu sinir bozucu şey sebepsiz oluyor gibi — aslında bir mekanizma var — ve sen onu durdurabilirsin." Başlık, hook ve kapanış aynı vaadi taşır.
2. **Tek görsel aktör:** Problem tek bir renkle (sinyal rengi) gösterilir ve izleyici onun uzayda/zamanda nasıl hareket ettiğini *izler*. Anlatılan her kavram ekranda ölçülebilir bir şeye dönüşür (sayaç, çubuk, eğri).
3. **Katman ekleyen sakin kurgu:** Sahneler uzun (~25 sn), kamera sabit, ama her 2–4 sn'de bir yeni etiket/ölçüm gelir. Göz hep okuyacak yeni bir şey bulur; kesmeye gerek kalmaz.

## Girdi (brif)

Zorunlu: **başlık** ve **konu açıklaması**. İsteğe bağlı: hedef süre (varsayılan 6–8 dk), dil (varsayılan VO İngilizce, notlar Türkçe), platform (varsayılan YouTube 16:9 + 3 Shorts kesiti), araçlar (varsayılan Remotion + ElevenLabs + Resolve), stil modu (aşağıda).

Brif eksikse sorma, varsayılanı kullan ve paketin başında "Varsayımlar" satırında belirt. Sadece konu gerçekten belirsizse (hangi olgu anlatılıyor anlaşılmıyorsa) tek soru sor.

## İş akışı

1. **Konu uygunluk testi** — `references/topic_fit.md`. Konu "gizli mekanizma + izleyici müdahalesi" kalıbına oturuyor mu? Oturmuyorsa en yakın açıyı öner (ör. "X nasıl çalışır" → "X neden hep bozulur ve sen ne yapabilirsin"). Simüle edilebilir bir "aktör" (dalga, kuyruk, yayılma, birikim, geri besleme) bul — bu videonun görsel omurgası olacak.
2. **Gerçek/kanıt listesi** — Senaryoda kullanılacak 4–7 çalışma/deney/veri. Her biri: yıl, yer/ekip, düzenek, tek cümlelik sonuç. Emin olmadığın rakam ya da atfı **[DOĞRULA]** etiketiyle işaretle; asla uydurma. Web arama aracı varsa kritik iddiaları kontrol et. Kanıtın sınırlı olduğu yerde referanstaki "I'll be straight about the evidence" dürüstlüğünü kullan — bu güven kazandırır.
3. **Başlık + hook** — `references/hook_and_script.md` §1–3. 5 başlık seçeneği (formül etiketiyle), 3 hook varyantı; birini öner.
4. **Senaryo** — Aynı dosya §4–6. 18 vuruşluk omurgayı konuya uyarla (birleştirilebilir/atlanabilir ama sıra mantığı korunur), tam VO metni yaz. 145–155 kelime/dk.
   - **Kelime bütçesi:** hedef kelime = süre(dk) × 150 (7 dk ≈ 1.050). Her vuruşun bütçesi = oran × hedef kelime (`hook_and_script.md` §4 tablosundaki oran). Her vuruşu zorunlu öğeleriyle tam yazınca metin doğal olarak ~%15 uzar; ≤7 dk hedefte baştan V12–V14'ü tek "çözümler" vuruşunda birleştir ya da V8'i kısalt, sonradan kırpmakla uğraşma.
   - **Zamanlama elle hesaplanmaz.** Vuruş başlıklarını zamansız (`## V1 · HOOK`), ekran olaylarını anahtar kelimeye bağlı (`> EKRAN: @twenty SAYAÇ "20 MIN"` veya önceki olaydan N sn sonra `@+2.5`) yaz, sonra çalıştır:
     `python <bu skill klasörü>/scripts/time_beats.py <paket.md>` → tüm `[mm:ss]` damgalarını kelime sayısından basar (150 kel/dk, vuruş arası 0,6 sn durak). Gerçek ses kaydı gelince ölçülen hızla (`--wpm <gerçek kel/dk>`) yeniden çalıştır; kare hassasiyeti Remotion'da kelime hizalama verisiyle (`animation_recipes.md` §11) sağlanır. `@kelime` çapaları dosyada kalmaz — yeniden zamanlama gerekecekse taslağın bir kopyasını sakla.
   - Bölüm 5'te `>`, `#`, `|` ile başlamayan **her satır VO sayılır**. Sahne notu/parantez açıklama yazacaksan `> NOT:` ile başlat, yoksa kelime sayısını şişirir.
5. **Storyboard + kurgu** — `references/visual_system.md`. Her vuruşa bir kompozisyon şablonu, sahne öğeleri, ekran metni ve "ekran olayı" listesi (≥1 olay / 4 sn) ata. Geçiş ve ses planı.
6. **Animasyon reçeteleri** — `references/animation_recipes.md`. Konunun "aktörü" için simülasyon kuralı + videodaki ana 6–10 animasyonun uygulanabilir reçetesi.
6b. **Ses tasarımı** — `references/voice_design.md`. Paketin 9. bölümüne ElevenLabs Voice Design açıklaması (kanalın kayıtlı sesi varsa onu kullan), senaryonun hook'undan preview metni ve TTS ayarlarını ekle.
7. **Thumbnail** — `references/thumbnail.md`. 3 konsept + başlık–thumbnail eşleşmesi + görsel üretim prompt'u. Referans görsel: `assets/reference_thumbnail_phantom_jam.png` (gerekirse aç ve bak).
8. **QA** — Senaryoyu çıktı dosyasına yazdıktan sonra çalıştır:
   `python <bu skill klasörü>/scripts/pace_check.py <paket.md>` → kelime/dk, sahne başına olay yoğunluğu, hook uzunluğu. Uyarıları düzelt, sonucu paketin sonuna ekle.

9. **Altyazı** — `time_beats.py` sonrası:
   `python <bu skill klasörü>/scripts/make_srt.py <paket.md> -o <klasör>/altyazi_en.srt` (≤2 satır, satır ≤42 karakter, noktalamada bölünür) ve seslendirme için düz metin: `... make_srt.py <paket.md> -o <klasör>/vo_metni.txt --plain`. Gerçek ses gelince `--wpm` ile yeniden üret ya da YouTube Studio'da düz metni "otomatik senkronizasyon" ile kullan.

Daha derin ayrıntı gerektiğinde (ör. referanstaki belirli bir sahnenin tam zamanlaması, renk örnekleri, geçiş ölçümleri) `references/source_analysis/01_tersine_muhendislik_raporu.md` ve `02_kare_kare_rekonstruksiyon.md` dosyalarına bak; her seferinde okumak gerekmez.

## Stil modu

- **`night-map` (varsayılan):** Referansın görsel *ilkeleri* (koyu dokulu zemin, tek sinyal rengi + tek vurgu rengi, düz veri paneli, büyük harf teknik grotesk) ama kanala ait palet ve imza ile. Ayrıntı: `visual_system.md` §2.
- **`transit-ink`:** Krem kâğıt, metro haritası estetiği — referanstan belirgin şekilde ayrışmak isteyen kanal için. Ayrıntı: `visual_system.md` §3.

Hangi modda olursa olsun referansın birebir imzalarını (aynı slogan, aynı başlık+alt çizgi düzeni ile aynı renkler, "kusursuz daire pist + merkezde dev 'N CARS' sayacı + dışta kırmızı veri yayı" bileşimi gibi özgün kompozisyonlar) kopyalama. Kapalı döngü *fikri* serbesttir — konunun kendisi bir döngüyse (ring otobüs hattı, pist, devre) döngüyü kullan; sadece geometrisini ve bilgi yerleşimini değiştir (oval/köşeli hat, sayaç döngünün dışında, veri yayı yerine durak üstü çubuklar vb.); ilkeyi al, uygulamayı kanala özgü yap. Sebep: hem telif/marka riski hem de izleyicinin "bunu zaten izledim" hissi CTR'ı düşürür.

## Çıktı

Paketi tek bir Markdown dosyası olarak yaz: kullanıcının çalışma klasöründe `uretim/<slug>/paket.md` (klasör yoksa oluştur). Sohbete yalnız kısa özet + dosya bağlantısı + önerilen başlık/hook/thumbnail'i yaz.

Bu şablonu kullan (bölüm başlıkları sabit, böylece QA script'i ve sonraki adımlar dosyayı okuyabilir):

```markdown
# <Başlık> — Üretim Paketi
Varsayımlar: süre … · dil … · platform … · araçlar … · stil modu …

## 1. Açı ve vaat
- Gizem: … · Mekanizma (tek cümle): … · İzleyici müdahalesi: …
- Görsel aktör (sinyal): … · Simülasyon kuralı (tek cümle): …

## 2. Kanıt listesi
| # | Yıl | Kim/nerede | Düzenek | Sonuç | Durum |
(Durum: ✓ eminim / [DOĞRULA])

## 3. Başlık seçenekleri
1. … (formül: …) ← önerilen
…

## 4. Hook varyantları
### H-A (önerilen) … ### H-B … ### H-C …

## 5. Senaryo (VO)
## [00:00] V1 · HOOK
<VO metni>
> EKRAN: [00:03] … 
> EKRAN: [00:07] …
## [00:24] V2 · <BÖLÜM ADI>
…

## 6. Storyboard / shot list
| Vuruş | Zaman | Şablon | Zemin | Öğeler | Ekran metni | Olaylar | Kamera | Geçiş | Ses |

## 7. Animasyon reçeteleri
### AN-01 …  (ELEMENT / PURPOSE / START / TIMELINE / MOVEMENT / EASING / LAYER / END / SIMPLE)

## 8. Tipografi, renk ve geçiş kuralları (bu video için)

## 9. Ses planı

## 10. Thumbnail konseptleri
### T1 (önerilen) … ### T2 … ### T3 …
Görsel üretim prompt'u: …

## 11. Shorts kesitleri (3)

## 12. QA sonucu
```

`> EKRAN:` satırları önemli: `time_beats.py` sonrası her biri `[mm:ss]` ile başlar; QA script'i olay yoğunluğunu bunlardan ölçer. Script'ler UTF-8 çıktı verir (Windows'ta ek ayar gerekmez).

## Yazım ilkeleri (kısa)

Ayrıntı `hook_and_script.md`'de; en kritikleri:
- İkinci tekil şahıs ("You're on the motorway…"), kısa cümle (ort. 9–12 kelime), jargon yok; terim ancak olgu gösterildikten sonra adlandırılır ("It's a wave.").
- Her bölüm tek soruyu cevaplar ve bir sonrakini açar ("That last one deserves a closer look, because we all do it.").
- Rakamlar birimle ve somut ("ten cars back", "around twenty kilometres an hour").
- Açılıştaki vaat ("you can stop one yourself") sonda izleyiciye görev olarak ödenir; son cümle duygusal bir sonuçla biter (izleyicinin davranışının başkasına faydası).
