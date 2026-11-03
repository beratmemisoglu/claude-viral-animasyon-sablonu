# Toon Studio: penceresiz animasyon stüdyosu

Bu klasör animasyon motorunun ana kodunu (`appcore/main/index.js`, `python setup_from_app.py` ile senin
kurulumundan kopyalanır) bir kütüphane olarak çalıştırır: proje kurulumu, CLAUDE.md yazıcısı, seslendirme, temizleme ve
zamanlama, ses tasarımı, miks, dışa aktarma, Claude görev çalıştırıcısı (istemler, ekip ajanları, hook'lar, araçlar) ve
tüm Claude araçları. Sadece uygulamanın penceresi değiştirildi: gizli render pencereleri headless Chrome sayfalarıdır
(`appcore/load.cjs`). Yani burada yapılan video, her stilde, uygulamadakiyle birebir aynı şekilde yapılır.

`appcore/main/index.js` ya da `templates/` yoksa önce `python setup_from_app.py` çalıştır.

## Video yapmak (uygulamanın akışı, adım adım)

Tüm komutlar bu klasörden: `python studio.py ...` (`python studio.py help` listeler). Uzun olanlar (run, export, voice)
dakikalar–saatler sürer: arka planda çalıştır.

1. `python studio.py new <ad> --style <id> [--length 60] [--format vertical|landscape] [--lang en] [--look <önayar>]
   [--topic "..."] [--brief "..."]` - stiller: `python studio.py styles`; görünümler: `python studio.py looks <stil>`.
2. Senaryo: `python studio.py run <ad> script --notes "<konu, açı, notlar>"` (uygulamanın "Write the script" adımı:
   araştırma, research.md, script.txt) ya da `script.txt`'yi kendin yaz (## bölümler, [notlar] kendi satırında).
3. `python studio.py voice <ad>` - ElevenLabs, sahibinin ses ayarlarıyla (appdata/config.json "voice"); hemen ardından
   kelimeleri temizler ve zamanlar (autoTime). Kendi kaydın: `--provider file --file <yol>`. Sadece yeniden zamanlama:
   `python studio.py audio <ad>`.
4. Build: `python studio.py run <ad> build --level <standard|props|polish|scenes|ultra|ultraplus> [--notes "..."]`
   (stilin seviyeleri: `python studio.py levels <ad>`). Bu, uygulamanın Build'idir: aynı istek metni, aynı model ve efor
   kuralları (Ultraedit'te Opus), ekip ajanları, kare bütçesi, araçlar.
5. Değişiklik: `python studio.py run <ad> edit --notes "<neyi, nerede değiştir (zaman / plan)>"`; sorular:
   `run <ad> ask`. Bitmiş videoya Ultraedit geçişi: `run <ad> ultra`.
6. `python studio.py sound <ad>` (müzik ve efektler; export gerekirse kendisi de çalıştırır), sonra
   `python studio.py export <ad> [--stems]` -> projenin `out/<ad>.mp4` dosyası.

Sessiz video (ses ve müzik yok): `voice`'u atla; planların ipucu satırları ve zamanlarıyla `audio/timeline.json` +
`audio/script_timed.txt`, uzunlukta sessiz bir `audio/clean.wav` yaz ve project.json'a `end` ekle; sonra `run <ad> build`
(satırların sadece zamanlama ipucu olduğunu söyle) ve `export <ad> --silent`.

## Özel stiller (uygulamanın Style Kit'i) ve dmscales

- `python studio.py kit [klasör]` uygulamanın Style Kit'ini yazar; stilleri orada kendi CLAUDE.md'si ve `cz` ile kur
  (`./cz check|stills|export|package <stil>`). `python studio.py import-style <zip>` uygulamanın içe aktarma
  kontrollerini çalıştırıp stili ekler; `styles` listeler, `new --style custom-<ad>` kullanır.
- **dmscales** (`custom-dmscales`): @dmscales'ten tersine mühendislikle çıkarılmış whiteboard açıklayıcıları (araştırma:
  `research/dmscales`). Stilin kendi parçaları `styles/dmscales` içinde (models, scenes, looks, skill); Style Kit'e nasıl
  konacağı README'de. Görünümler: Clean ve Hit (kalın italik, #fcfcfc); kontrol: `era`.
- Bir dmscales videosu: `new <ad> --style custom-dmscales [--look custom-dmscales-hit]`, ses
  `voice <ad> --provider file --file v.wav` (+ `script.txt`), ekran görüntüleri ve klipler
  `node <proje>\.claude\skills\style-custom-dmscales\scripts\add_media.mjs <proje> <dosyalar...>`, sonra `run <ad> build`.

## Bu oturumda bir proje üzerinde kendin çalışmak

`python studio.py use <ad>`, sonra `suite` MCP sunucusunu yeniden bağla (/mcp): araçları uygulamanın o projenin stili
için olan kendi araçlarıdır (render_frames, check_preview, check_layout, list_shots, narration, make_image, make_sprites,
web_image, lowpoly_asset, enrich_frame, library_* ...). Önce projenin kendi CLAUDE.md'sini ve skill'ini
(`<proje>/.claude/skills/<skill>/SKILL.md`) oku ve onlara uy. Tam build'ler için `run`'ı tercih et.

## Neler nerede

- Çalışma alanı (projeler, suite.db, kütüphane, STYLE.md): `studio.json` "workspace" (varsayılan `~/ToonStudio-Projects`;
  bilerek bu klasörün dışında: projelerin üstündeki bir CLAUDE.md uygulamanın kendi Claude çalışmalarına sızar).
- `appcore/`: uygulamanın kodu (kurulumdan) + `load.cjs` (Electron'un yerine geçen) + `cli.cjs` + `mcp.cjs` + `fixes.cjs`
  (her cli komutunun projenin engine.js'ine uyguladığı düzeltmeler: export'ta "OperationError: Encoding error" için
  stickstory/toon encoder yedeği); `appdata/` uygulamanın veri klasörü (config.json: ses, müzik, Claude, araç yolları);
  `templates/` stil motorları ve skill'ler (kurulumdan).
- Google Flow (ücretsiz görseller): uygulamanın Flow Chrome profili, appdata/flow-chrome'a bağlı. Giriş ya da robot
  kontrolü gerekirse sahibi `python studio.py flow-open` çalıştırıp o pencerede kendisi tamamlar (asla onun yerine yapma).
- Anahtarlar dosyadan değil, ortam değişkenlerinden gelir: ELEVENLABS_API_KEY, HIGGSFIELD_API_KEY, FAL_KEY,
  FISH_AUDIO_API_KEY.

`appcore/main/index.js` ve `templates/` dosyalarını asla düzenleme: onlar uygulamanındır.
