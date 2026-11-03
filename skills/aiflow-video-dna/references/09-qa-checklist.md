# 09 — Yayın öncesi QA kontrol listesi

Her madde geçmeden yayın yok. Ölçülebilir olanlar `scripts/edit_rhythm_qa.py` ile otomatik.

## A. Paketleme
- [ ] Başlık iskelete uyuyor (Mod T: `How To Make Videos Like {X} With AI ({para} {niş} Niche)`; Mod F: ≤ 60 karakter tek merak kalıbı).
- [ ] ≤ 75 karakter, tek parantez, "|" kuyruğu yok, varlık ≤ 40. karakter; "Full Course" başlıkta değil thumbnail'de.
- [ ] Thumbnail 168×94 testi: başlık + 1 kart başlığı + para bandı okunuyor; gri tonlamada başlık en parlak; hale kontrastı ≥ 7:1; ≤ 7 metin bloğu.
- [ ] Thumbnail'deki her sayı doğru ve doğrulanabilir; geri dönüştürülmüş sayı yok.
- [ ] 3 thumbnail varyantı + 5 başlık → Test & Compare.
- [ ] Açıklama şablonu: satır 1 başlık, düzyazı, **canlı kaynak paketi linki**, araçlar (affiliate açıkça belirtilmiş), topluluk, bölümler, watch-next, "questions people ask", 5 hashtag.
- [ ] İlk bölüm adı "Important"; 9–12 tek kelimelik adım bölümü; bölüm işareti en çok istenen adımdan 0–3 sn önce.
- [ ] Sabit yorum: paket linki + aynı serinin en yeni 3 videosu.
- [ ] Collab partnerleri eklendi (mümkünse); otomatik dublaj açık.

## B. Senaryo (Mod T)
- [ ] 0:02'den önce izleyiciye soru; ≤ 0:08'de niş cevabı ekranda kinetik yazı.
- [ ] ≥ 2 kanıt kanalı × 5 gerçek (video sayısı, abone, ilk yükleme yaşı, en iyi video izlenmesi, viral tazeliği) — hepsi kayıt anında ekranda doğrulanabilir.
- [ ] Para aritmetiği sadece kamuya açık sayılardan, "tahmini" ile; garanti gelir cümlesi yok.
- [ ] Vaat cümlesi + "stres yapma" + ≤ 10 sn kendi bitmiş ürün teaser'ı ilk adımdan önce; ilk adım ≤ %14 sürede.
- [ ] Koşan örnek konu 5/5 adımda taşındı ve finalde oynuyor.
- [ ] Her adım T→N→E→P→C→Z→K→(W)→R→X→V→T′ döngüsünde; R ≥ 3 sn, X her adımda var.
- [ ] Kotalar: güvence ≥ 18 · açık döngü ≥ 8 (≥ 2'si sonra kapanan uyarı) · mizah ≥ 5 · abone ≤ 4 (hiçbiri 2:45'ten önce değil) · ≥ 1 hata→düzeltme ilk üçte birde · ≥ 7 prompt + ≥ 12 ayar/hile.
- [ ] Bekleme anları CTA/motivasyonla dolu (≤ 3, her biri ≤ 12 sn).
- [ ] %80–87'de fırsat hatırlatması (3. kanıt kanalı).
- [ ] Final videodan sonra konuşma yok; tam cümlede bitiyor + end screen.

## C. Senaryo (Mod F)
- [ ] Hook ilk 45–60 kelime, selamlama yok, ilk 15 sn'de 1 somut sayı, açık döngü son üçte birde kapanıyor.
- [ ] Her 60–90 sn'de yeniden kanca; cümle ≤ 18 kelime; tüm istatistikler `[SRC?]` → doğrulandı.
- [ ] Kelime sayısı = dakika × 155 (±%5); `||` vuruş işaretleri her 12–18 kelimede.
- [ ] "not financial advice"; hisse önerisi/garanti yok; rakip adı/ifadesi/karakteri yok.

## D. Edit (otomatik: `edit_rhythm_qa.py`)
**Mod T (`--profile tutorial`):** değişim/dk 20–45 · çekim değişimi/dk 6–18 · medyan çekim 1,5–5 sn · maks statik ≤ 15 sn (sadece okunur kopya ekranı) · > 8 sn statik ≤ 6/10 dk.
**Mod F (`--profile animated`):** değişim/dk 15–40 · çekim değişimi/dk 5–12 · medyan çekim 3–9 sn · maks statik ≤ 10 sn · > 8 sn statik ≤ 3/10 dk.
- [ ] Hook: ilk 10 sn'de 5–7 değişim, ≥ 3 kaynak türü.
- [ ] Kanıt bölümü: 25–35 değişim/dk; söylenen her sayıya 1,5–1,67× animasyonlu zoom (0,3–0,7 sn S-eğrisi, 3–4 sn tut).
- [ ] Gövde 1:1; native seçim + tıklama halkası; editörün çizdiği ok/kutu/emoji yok.
- [ ] Kopyalanacak metin mobilde okunur (≥ %2 H veya 1,5–1,7× punch-in, ≥ 3 sn).
- [ ] AI beklemeleri ≤ 1 sn'ye kırpıldı ya da 4–10× hızlandırıldı; hiçbir bekleme ekranı > 8 sn değil.
- [ ] Her sonuç açılışında sting (+6…+10 dB), "şimdi bak", sonuç ≥ 3 sn.
- [ ] Tek "vay" anı (görsel→video tam ekran, kendi sesiyle) videonun %55–70'inde.
- [ ] Mod F: ilk 20–30 sn animasyon klipleri; hiçbir durağan > 12 sn; dakikada ≤ 2 stilize geçiş; altyazı rakamları düzeltildi.

## E. Ses
- [ ] Anlatım 170–190 wpm (TR 150–170; Mod F 155–165), ≥ %90 kaplama, nefes temiz, ≤ 1 duraklama/dk (ön-reveal hariç).
- [ ] Mix −14…−16 LUFS, true peak ≤ −1,5 dBTP, LRA ≤ 4.
- [ ] TTS parçaları ≤ 2.500 karakter, her parçada > 1 sn sessiz boşluk kontrolü yapıldı (referans içerik kaybetti).
- [ ] Müzik yatağı yok ya da −30…−35 dB altta; kesmelerde SFX yok.

## F. Etik / IP / gizlilik
- [ ] Maskot özgün; tanınmış karakterlere benzerlik kontrolü yapıldı; prompt'larda kanal/karakter/gerçek kişi adı yok.
- [ ] Rakip videolarından klip/ses kullanılmadı (kanal sayfası kaydı kanıt amaçlı; klipler kısa ve sessiz). Teaser ve final = kendi ürünümüz.
- [ ] Meme/B-roll lisanslı veya özgün; silah/şiddet yok.
- [ ] Ekran kaydında e-posta, kullanıcı adı, dosya yolu, API anahtarı, hesap avatarı görünmüyor (gerekirse yumuşak blur).
- [ ] Kaynak paketi linki yüklemede canlı; "söz ver, tutma" yok.
- [ ] Format çeşitliliği: son videoyla aynı yapı ve aynı açılış cümlesi değil (inauthentic-content savunması).
