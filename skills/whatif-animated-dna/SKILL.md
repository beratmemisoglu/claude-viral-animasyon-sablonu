---
name: whatif-animated-dna
description: Türkçe "Ya ___ olsaydı?" / "Ya herkesin ___ görebilseydin?" animasyonlu hipotetik senaryo videoları (2. tekil şahıs, 8–10 dk, çöp adam animasyon, kafa üstü sayı etiketleri) için FİKİR → BAŞLIK/THUMBNAIL → SENARYO → SESLENDİRME → SHOT LIST → REMOTION RENDER → METADATA → YOUTUBE tam otomatik üretim sistemi. Ekim 2026'da 2 haftada 5–10 videoyla 100K–650K izlenen 10 yeni İngilizce "What If" kanalının 100 videosundan (27 hit) 5 paralel analist ajanla çıkarıldı: neden tıklandı (başlık kalıp aileleri, 13 mutasyon kuralı, 0–10 rubrik, thumbnail "ikinci soru" + çelişki ilkesi), neden izlendi (≤15 sn kural ihlali, ≤30 sn tek cümle kural, 10 vuruşluk şablon, tırmanma merdiveni, iki adımlı lanet dönüşü), görsel dil (iki ritim profili, 12 güç görselleştirme tekniği, infografik kart, ölçülmüş palet), izleyici psikolojisi, risk korkulukları ve Türkiye pazarı (RPM, rakip boşluğu, 40 puanlı Türkçe premise). Kullanıcı "ya olsaydı videosu", "what if videosu", "what if kanalı", "herkesin kafasının üstünde sayı", "hipotetik senaryo animasyonu", "Iflord / ConChaser / Miko / Jeremy Bearimy / Hour Seven gibi", "faceless what if", "çöp adam animasyon kanalı", "bu nişte video üret", "fikir bul / başlık yaz / thumbnail yap / senaryo yaz / shot list çıkar / render et / yükle" dediğinde, ya da bir premise verip video istediğinde MUTLAKA bu skill'i kullan — skill adı geçmese bile.
---

# What If DNA — Türkçe "Ya … olsaydı?" video fabrikası

Kaynak: 10 kanal, 100 video (27 hit ≥100K), 11 videonun kare kare kanıt paketi, 20 transkript, 1.308 yorum, NexLev RPM/rakip verisi; 5 paralel analist + orkestra şefi birleştirmesi (2026-10-28). Ham raporlar `deep-research/` (her ajanın kendi README'si ve raporu), birleştirilmiş kurallar `references/`, çalışan kod `scripts/` + `templates/`.

**Kopyalanan:** yapı, zamanlama, ölçüler, karar mantığı, başlık kalıpları. **Kopyalanmayan:** rakip karakterleri, renkleri, cümleleri, thumbnail'leri, birebir başlık çevirisi.

## Tek cümlelik DNA
> İzleyiciye gündelik hayatında 5 sn'de hayal edebileceği, **bir sayı + bir yasakla** tanımlı, hediye gibi görünen bir **lanet** ver; kuralı ilk 15 sn'de bir sahnede kır, 30 sn'de tek cümleyle söyle; bedeli önce kahramana sonra en yakın kişiye döndür; sayıyı kişinin kafasının üstünde göster ve her dakika bir kez değiştir; iki seçenekli soruyla bitir.

## Neden kazandı (kısa) — ayrıntı `references/01-why-it-won.md`
1. **Simülasyon, güç değil:** "ben olsam?" oyununu başlatan başlık tıklanıyor. Klasik süper güç (uç, ışınlan) %6 hit; DUAL (ölümsüz, kalp 10 kat) %75; sosyal + somut + tabu %71.
2. **Bilgi yönü sana:** "Crush on You" 179K, aynı gün "Partners Everyone Has Had" 23K. "Herkes seni görüyor" 3/3 flop. Ölüm sayacı keder doğuruyor (12K), servet sayacı hırs (482K).
3. **Thumbnail ikinci soru:** görsel çelişki %56 hit; başlığı tekrar eden metin %22.
4. **Hook:** hit'lerin 10/10'unda kural ihlali ≤15 sn; kural tek cümle ~30 sn. Flop'larda iki katı.
5. **Tartışma motoru:** hit yorumlarında kural/boşluk tartışması %30,6, flop'ta %0.
6. **Dağıtım:** kanalın ilk videosu %60 hit; günde >1 video oranı düşürüyor; hit'ten sonra 24–72 saatte aynı aileden eskalasyon taşınıyor.
7. **Zamanlama:** İngilizce niş Ekim 2026'da doyuyor; Türkçe'de bu aile boş (0 tam eşleşme), format kanıtlı. TR RPM ~1,4–1,8 $; önerilen: TR ana kanal + EN ses parçası.

## Modlar
| Mod | Tetik | Ne yap |
|---|---|---|
| **IDEA** | "fikir bul", "konu öner", "premise", "seri planı" | `02` §2, §6–7 + rubrik; 3 aday, puan tablosu, seçim |
| **PACKAGE** | "başlık", "thumbnail", "kapak" | `02` §3–5 + `03`; `package.json` + `make_thumbnail.py` |
| **SCRIPT** | "senaryo yaz", "seslendirme metni" | `04`; `script.md` + `script.json`; QA rubriği tablosu |
| **SHOTS** | "shot list", "sahne planı", "storyboard" | `05`; `shots.json` (profil seç) |
| **PRODUCE** | "videoyu yap", "render", "full otomatik", "baştan sona" | `07`; `pipeline.py` tüm aşamalar |
| **QA** | "kontrol et", "yayına hazır mı" | `08` checklist + doğrulayıcılar + `qa_render.ps1` |
| **RESEARCH** | "nişte ne oluyor", "yeni hit'ler", "rakipler" | NexLev MCP: `search_viral_videos_small_channels` (query "what if"), `faceless_outliers_videos`, kanal listesi `youtube_channel_videos`; `deep-research/dataset.csv` ile karşılaştır |

## PRODUCE — tam otomatik akış
```powershell
$S = "$env:USERPROFILE\.claude\skills\whatif-animated-dna\scripts"
python "$S\pipeline.py" <slug> --idea "Ya herkesin maaşını görebilseydin?"   # girdi boş da olabilir
```
Sıra: `idea → package → script → tts → shots → render → thumb → meta → upload`.
1. LLM aşamasında (idea/package/script/shots/meta) çıktı yoksa pipeline `prompts/<stage>.prompt.md` yazıp **exit 3** verir. Promptu oku, ilgili `references/` dosyasını uygula, çıktı dosyasını proje klasörüne yaz, `--from <stage>` ile devam et.
2. Doğrulayıcılar kuralları zorunlu tutar: başlık ≤55 karakter / ≤8 kelime / "?" / rubrik ≥5; thumbnail metni başlığı tekrar edemez (Türkçe uyumlu karşılaştırma), çelişki zorunlu; senaryo tahmini ≤11 dk; TTS toplamı ≤11 dk (aşarsa durur) ve gerçek kelime/dk'yı loglar; shots şema + bitişiklik + profil ritmi + sert sınırlar (>30 kesme/dk, medyan <1,5 sn, ilk 15 sn >10 kesme, boş uzun plan) + infografik kart sayısı.
3. **render** önce draft (0,5 ölçek) + her shot'tan kare üretir. **Kareleri aç ve bak** (etiket-yüz çakışması, güvenli alan, Türkçe karakter, yürüme yönü); düzeltmeyi `shots.json`'da yap, sonra final.
4. **thumb** A/B/C üretir; `03` QA kapılarıyla birini seç (`package.thumb.pick`). İsteğe bağlı Higgsfield polish.
5. **upload** private + `publish_at`. Kullanıcı açıkça istemedikçe yayınlama/zamanlama yapma; yüklemeden önce başlık, thumbnail ve tarihi kullanıcıya göster.

**Bir kez kurulum gerekiyor** (`07` §5): bileşenleri stüdyoya kopyala (`C:\dev\the-other-self\src\lib\whatif\`, `register.ts` talimatı), Türkçe ElevenLabs sesi seç (`tts_segments.py --list-voices` → `whatif_voice.json` içindeki placeholder `voice_id`), YouTube token. Ses seçimi ve kanal adı/karakter rengi kullanıcı kararıdır; sorma yerine kurulum durumunu kontrol et, eksikse söyle.

## IDEA / PACKAGE / SCRIPT — elle mod kısa kuralları
- **Fikir:** 1 sayı + 1 yasak; güç başkası hakkında bilgi verir (sana akar) ya da DUAL bedendir ya da oyun mekaniğidir; izleyiciye hamle bırakır; ölüm sayacı yok. Rubrik ≥5.
- **Başlık:** "Ya … -seydin?" ≤8 kelime ≤55 karakter; sıradan rakam yok; ana somut isim ilk 5 kelimede.
- **Thumbnail:** ikinci soru; ötekinin yüzü sayısıyla çelişir; 1–4 kelime; luma 60–160.
- **Senaryo:** 0–3 sn sıradan an → ≤15 sn ihlal → ≤30 sn tek cümle kural → 20–45 sn "Peki ya …?" → 25–50 sn karanlık vaat → 10 vuruş → %38–48 ilk bedel → %48–70 en yakın kişi → kriz → ders + ödül → ikili soru. 8–10 dk, tavan 11. Rakamlar `spoken`'da yazıyla.
- Çıktıyı kullanıcıya **Türkçe**, tablolarla ver. Rakip transkriptinden cümle kopyalama.

## Korkuluklar (her modda)
Özgün karakter; marka/ünlü yok; gore/cinsel ima/intihar çağrışımı yok; din, siyaset, etnik köken ve askerlik alay konusu olmaz; kumar yok; "çocuklar için değil" elle; bilim iddiası kaynaklı; aynı aileden 30 günde ≤2 video; günde ≤1 video. Ayrıntı `06` §3.

## Dosya haritası
| Dosya | İçerik |
|---|---|
| `references/01-why-it-won.md` | sistemin mantığı: kazanma zinciri, "ne değişince tuttu" tablosu, çelişki kararları, sınırlar |
| `references/02-idea-and-title.md` | aile sıralaması, 13 mutasyon kuralı, 0–10 rubrik (doğrulanmış eşik), 20 şablon EN→TR, premise kuralları, TR premise ilk 10 |
| `references/03-thumbnail.md` | ikinci soru ilkesi, 3 layout (ölçülü), 10 QA kapısı, TR notları |
| `references/04-hook-and-script.md` | hook saniye bütçesi, 10 vuruşluk şablon, merdiven, dil + TTS kuralları, bitiş, 10 kriterli QA, süre kararı |
| `references/05-visual-animation.md` | iki ritim profili, açılış standardı, 12 güç tekniği, infografik kart, palet (ölçülmüş), metin, kamera, bileşen eksikleri |
| `references/06-audience-risk-tr.md` | yorum kanıtı, mekanizma → kural, korkuluklar, TR RPM/rakip/go-no-go, kitle |
| `references/07-pipeline.md` | aşama tablosu, çalıştırma, veri şemaları, bileşenler, kurulum, hata modları, doğrulanmayanlar |
| `references/08-qa-checklist.md` | yayın öncesi K1–K7 |
| `templates/prompts/*.md` | LLM aşamalarının prompt şablonları (referanslara bağlı) |
| `templates/remotion/` | WhatIfFilm, StickFigure, HeadLabel, Crowd, Caption, 6 sahne + SceneInfoCard, theme (ölçülmüş palet), fonts, register |
| `templates/sample-script-tr.md` | tam Türkçe örnek senaryo (1.326 kelime, QA 10/10) |
| `templates/thumbnail.svg` | thumbnail şablonu |
| `scripts/pipeline.py` | aşama koşucu + doğrulayıcılar |
| `scripts/tts_segments.py`, `whatif_voice.json` | segment bazlı ElevenLabs TTS + kelime zamanları |
| `scripts/shots_schema.json` | shot list şeması (profile, infocard, card) |
| `scripts/make_thumbnail.py`, `qa_render.ps1` | thumbnail üretici, render QA |
| `deep-research/` | ham veri (`dataset.csv` 100 video), A–E raporları, video notları, `README.md` |
