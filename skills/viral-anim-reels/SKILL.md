---
name: viral-anim-reels
description: Yüzsüz animasyonlu "gizli kural / loophole / gizli mekanizma" Reels ve Shorts fabrikası. Instagram'da 0'dan 100K takipçiye, sonra YouTube'a. Akış FİKİR → SENARYO → KURGU/PLAN LİSTESİ → HIGGSFIELD GÖRSEL+HAREKET → ELEVENLABS SES → ALTYAZI → MONTAJ → QA → IG BAŞLIK/AÇIKLAMA/KAPAK → YAYIN PLANI → KPI. Ricks Clips (14 ayda 315M, top short 28M) ve 5 rakip kanalın (Low Poly Shorts, Loaded Dice, Circle Toon History, The Why Side, i think it's george) 41 viral shorts'unun NexLev + kare kare tersine mühendisliğinden çıkarıldı (2026-10-29). Ölçülenler: hook taksonomisi, başlık aileleri, 11 vuruşluk beat-sheet, "You see" menteşesi, twist %65, 3,8 sn plan / %0 statik kamera, literal isim kuralı, tek kelimelik altyazı spec'i, −14 LUFS dolu duraklamalar, IG algoritması ve 90 günlük plan. Varsayılan marka: Backdoor Bureau / rakun müfettiş Clause. Kullanıcı "Ricks Clips gibi", "animasyonlu shorts/reels", "viral reels fikri", "instagram animasyon hesabı", "loophole videosu", "gizli kural videosu", "Backdoor Bureau", "Clause", "senaryo yaz", "reels kurgusu", "instagram açıklaması/başlığı yaz", "kapak yap", "reels yayın planı", "100K takipçi planı", "KPI/metrik analizi", "bu videoyu Ricks gibi analiz et" dediğinde ya da bir konu verip kısa animasyonlu video istediğinde MUTLAKA bu skill'i kullan — skill adı geçmese bile.
---

# Viral Anim Reels — "gizli kural" animasyon fabrikası

**Kaynak:** 41 video kare kare incelendi (2 fps kare, 1 fps kontak sayfası, kelime zamanlı transkript, ses ölçümü). Ayrıca 147 yorum, NexLev outlier verisi ve IG algoritma araştırması kullanıldı.
- 6 analist raporu: `deep-research/` (00, A–F).
- Ham veri: `deep-research/dataset.csv`.
- Birleştirilmiş kurallar: `references/`. Çalışan kod: `scripts/`.

**Kopyalanan:** yapı, zamanlama, ölçüler, karar mantığı. **Kopyalanmayan:** rakip karakteri (Ricks'in beyaz yuvarlak kafası), hikâyeleri, cümleleri, sesi.

## Tek cümlelik DNA
> **Gerçek** bir nesne/kurum + onun **kuralını bozan** bir insan + alay/itiraz + en sona saklanmış **gerçek mekanizma**. 0. saniyede konuşan ve hiç durmayan kamera, tek kelimelik altyazı. Kapanışta Clause'un damgası ve bedelli bir soru.

## Viralliği ne belirliyor (`references/01`)
- **Premise, başlık ve arketip belirliyor.**
  - 12 hit'in 12'si gerçek bir kuralı bozan, failli bir cümleyle ~4 sn'de açılıyor.
  - "The [Nesne] That [Anomali]" başlıkları ort. 12,9M, okul tarzı başlıklar 0,46M.
  - Aynı konuda (kumar) çerçeveye göre 130 kat fark var.
- **Kurgu hızı, wpm, altyazı ve LUFS belirlemiyor**; hit'te de flop'ta da aynı. Bunlar hijyen.
- **Sonuç:** Emeğin %70'i fikir, premise ve başlığa gider. Üretim şablonu birebir uygulanır.

## Modlar
| Mod | Tetik | Yap |
|---|---|---|
| **IDEA** | "fikir", "konu öner", "ne yapalım" | `02`: banka (`deep-research/E` §5, `B` §5b) + NexLev taze outlier → 3 aday, rubrik tablosu (≥7/10), seçim |
| **SCRIPT** | "senaryo yaz" | `03`: `script.json` (beat'ler, plan alanları, kaynaklar) → `validate.py` |
| **PRODUCE** | "videoyu yap", "baştan sona" | Aşağıdaki akışın tamamı |
| **PACKAGE** | "başlık", "açıklama", "kapak", "caption" | `02` §5–6 + `06` §3 → `package.json` → `validate.py` |
| **PUBLISH-PLAN** | "yayın planı", "takvim", "100K planı" | `06` §4 faz tablosu + seri dağılımı + saatler |
| **KPI** | "metrikler", "hangi video tuttu", "pop oldu" | `metrics.csv` → `kpi_report.py` → `06` §5 protokolü |
| **RESEARCH** | "rakip ne yapıyor", "bu videoyu analiz et" | NexLev + `scripts/fetch_and_frame.py` (kare kare kanıt paketi) → `deep-research` yöntemi |
| **BRAND** | "isim / karakter değiştir" | Yalnızca `references/00-brand.md` güncellenir |

## PRODUCE — uçtan uca akış
```powershell
$S = "$env:USERPROFILE\.claude\skills\viral-anim-reels\scripts"
python -I "$S\new_project.py" airline-seat-twice --series "Small Print"   # C:\dev\viral-reels\<slug> (env VIRAL_REELS_ROOT)
python -I "$S\validate.py"   airline-seat-twice      # script + package kuralları; FAIL = düzelt
python -I "$S\tts.py"        airline-seat-twice      # ElevenLabs kelime zamanlı VO (plan aşamasında --dry)
python -I "$S\shotlist.py"   airline-seat-twice      # zamanlı plan listesi + shots/PROMPTS.md
#   → Higgsfield: her plan için anahtar kare (shots/sNN.png) + I2V (shots/sNN.mp4)
python -I "$S\captions.py"   airline-seat-twice      # build/captions.ass (y=1060, tek kelime kart)
python -I "$S\assemble.py"   airline-seat-twice --draft   # hızlı önizleme; sonra --draft olmadan final
python -I "$S\qa.py"         airline-seat-twice      # LUFS/TP/sessizlik/süre + qa/ kontak sayfaları
```
1. **Fikir:** Rubrik ≥7. Fikri `ideas_log.csv` ile karşılaştır; son 30 günde aynı seriden ≤3 video olsun.
2. **Araştırma:** Her olgusal iddia için **2 bağımsız kaynak** bul (WebSearch) ve `brief.md` ile `script.json.sources`'a yaz. Kaynağı bulunamayan iddia senaryoya girmez (`03` §6).
3. **Senaryo:** `script.json` beat-sheet'e göre yazılır, her satıra `shot` alanı eklenir. `validate.py` FAIL vermeyene kadar düzeltilir. Senaryoyu kullanıcıya Türkçe özet + İngilizce VO metni olarak göster.
4. **Ses:** `tts.py`. `voice-narrator.json`'da `voice_id` = CHOOSE_ME ise dur. `--list-voices` ile 3–5 aday sun, **sesi kullanıcı seçer**. Plan ve zamanlama için `--dry` yeterli.
5. **Görsel:** `shotlist.py` → `shots/PROMPTS.md`. Higgsfield akışı (`04` §3):
   - İlk kez: Clause referans sayfasını üret, `manage_reference_elements` ile "CLAUSE" elementi olarak kaydet.
   - Önce `balance` ve tahmini maliyet; bütçe verilmediyse ilk videoda kullanıcıya sor.
   - `generate_image_batch` (anahtar kareler) → **kareleri aç ve bak**: karakter tutarlılığı, isim görünür mü, altyazı bandı boş mu → beğenilmeyenleri yeniden üret.
   - `generate_video_batch` (I2V) → `jobs_wait` → dosyaları `shots/sNN.png|mp4` olarak indir.
   - Klip yoksa `assemble.py` anahtar kareye Ken Burns uygular; o da yoksa yer tutucu kart koyar (animatik).
6. **Montaj ve QA:** `captions.py` → `assemble.py --draft` → `qa/hook.jpg` ve `qa/sheet_*.jpg`'ye bak → düzelt → final → `qa.py` FAIL 0. `music/` klasörüne telifsiz ya da kendi üretimimiz bir yatak koy (yoksa yer tutucu pad kullanılır; yayına uygun değil).
7. **Paket:** `package.json` (`06` §3) → `validate.py`. `build/cover.jpg`, `build/ig_caption.txt`, `build/pinned_comment.txt` ve `build/yt.txt` hazır.
8. **Yayın:** Ajan hesap açmaz ve kendi başına paylaşım yapmaz. Final dosyayı, kapağı, caption'ı ve önerilen saati kullanıcıya göster; yayını kullanıcı yapar (ya da açık onayıyla bir araçla yapılır). 72. saatte `metrics.csv` kaydı hatırlatılır.

## Elle mod — kısa kurallar
- **Hook:** 10–17 kelime, fail + somut geçmiş zaman fiil + stake kelimesi. Soru değil, "Look/Imagine" ile başlamaz. Tipler H1/H2 (%60), H6 (%20, rakipte 24M ortalamalı boş şerit), H3/H4 (%20).
- **Başlık:** 5–7 kelime, somut isim + anomali fiili + ölçek. Mekanizmayı vermez. Science/Behind/Actually/Explained/Works kelimeleri ve "This …" açılışı yok.
- **Yapı:**
  - Twist %60–72'de, mekanizma twist'ten sonra.
  - "You see," 2 kez, pivot ≥6/dk, 1 "Wait, X?" ve 1–2 diyalog satırı.
  - ≥2 yorum cihazı + 1 send cihazı + 1 meme kelimesi.
  - Kapanış: Clause damgası + bedelli soru ya da sonraki dava teaser'ı.
- **Görsel:**
  - 14–16 plan (~3,8 sn), sert kesme yok, ≥1 sn statik an yok.
  - Söylenen somut isim ±0,3 sn içinde ekranda.
  - Videoda en az birer cutaway, overhead, iris ve damga planı.
  - S %40–48; gerçekçi insan yüzü yok.
- **Altyazı/ses:**
  - Montserrat ExtraBold 80 px, beyaz, 3 px kontur, gölge, **merkez y=1060**, 1–2 kelime/kart.
  - VO 0,00 sn'de başlar, 205–220 wpm, 6–10 duraklama ve hepsi SFX ya da müzikle dolu.
  - Master −14 LUFS / −1 dBTP.
- **IG:**
  - Kapak = imkânsız an + 2–4 kelime (3:4 bant).
  - Caption'ın ilk satırı ≤80 karakter, VO'nun kopyası değil.
  - 3–5 hashtag; kaynaklar sabitlenmiş yorumda.
  - Trial Reels ile hook testi; pop olunca 24–72 sa protokolü.
- Kullanıcıya çıktı **Türkçe**, VO ve IG metinleri **İngilizce**.

## Korkuluklar
- Rakip hikâyesi, cümlesi, karakteri ya da sesi kopyalanmaz. Ricks/Loaded Dice'ın işlediği hikâyeler listesi: `deep-research/E` §4.
- **Uydurulmuş tarihsel sonuç ve "always/never" yalanı yok.** Fabl ilk 5 sn'de işaretlenir.
- Kumar ayda ≤2 video ve "kasa neden kazanır" tonunda; bahis sponsoru yok.
- Gore, intihar, cinsellik ve gerçek kişiye karalama yok. Ülkeye bağlı yasal iddialarda kapsam belirtilir.
- Müzik telifsiz ya da kendi üretimimiz; her platforma filigransız master.
- Ses seçimi, marka adı, bütçe ve yayın kullanıcı kararıdır: bilgiyi hazırla, onay iste.
- `inner-voice-film/voice.json` başka bir kanalın kilitli sesi; ona dokunma.

## Dosya haritası
| Dosya | İçerik |
|---|---|
| `references/00-brand.md` | Backdoor Bureau, Clause karakter spec'i, 6 seri, bio, alternatifler |
| `references/01-why-it-works.md` | Hit/flop kanıtları, izleyici psikolojisi, flop teşhisleri |
| `references/02-ideas-titles.md` | Fikir kaynakları, ısı haritası, rubrik, hook taksonomisi, başlık kuralları, IG paketleme |
| `references/03-script.md` | 11 vuruşluk beat-sheet, anlatıcı kuralları, şablonlar, cihazlar, `script.json` formatı, doğruluk kuralı |
| `references/04-visual-edit.md` | Kurgu grameri, kamera sözlüğü, Higgsfield tarifi ve prompt şablonları, montaj |
| `references/05-captions-audio.md` | Altyazı spec'i, ElevenLabs ayarları, müzik/SFX/master |
| `references/06-instagram-publish.md` | Algoritma, kurulum, paket alanları, 90 günlük plan ve KPI'lar, pop protokolü, YouTube geçişi, riskler |
| `references/07-qa-checklist.md` | Yayın öncesi kontrol listesi |
| `scripts/` | new_project, validate, tts, shotlist, captions, assemble, qa, kpi_report, fetch_and_frame (araştırma) |
| `templates/` | script/package şablonları, metrics.csv başlığı |
| `examples/` | Örnek dolu proje (`case-001-pudding-guy`) |
| `deep-research/` | Ham analist raporları (00, A–F), BRIEF, dataset.csv, analiz script'leri |
| `voice-narrator.json` | Anlatıcı ses config'i (voice_id kullanıcı seçimini bekliyor) |
