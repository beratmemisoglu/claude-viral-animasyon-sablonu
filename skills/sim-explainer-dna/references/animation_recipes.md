# Animasyon Reçeteleri

Reçeteler yazılımdan bağımsızdır; parantezde Remotion (React + SVG) ve After Effects karşılığı. Değerler referansın 1–10 fps ölçümünden **yaklaşık** başlangıç değerleridir.

Her reçete paketin 7. bölümüne şu yapıyla yazılır:
`ELEMENT · PURPOSE · STARTING STATE · TIMELINE · MOVEMENT · TRANSFORMATIONS · LAYER ORDER · EASING · SECONDARY EFFECTS · ENDING STATE · TRANSITION · SIMPLIFIED IMPLEMENTATION`

## İçindekiler
0. Simülasyon çekirdeği (her konu için)
1. Sinyal glow
2. Döngü deneyi (T-LOOP)
3. Zincir çubukları
4. Zaman-uzay diyagramı
5. Akış/yoğunluk eğrisi + reframe
6. Panel, bar, sayaç, zamanlayıcı
7. Vurgu halkası / kontur / ok / yay
8. Kural kartları + kural kaldırma
9. Checklist
10. Geçiş ve başlık
11. Remotion iskeleti

---

## 0. Simülasyon çekirdeği
Her konunun "aktörü" için tek bir basit kural yaz, deterministik (sabit seed) çalıştır, kare başına durum kaydet; tüm UI bu kayıttan okunur.

Şablon kurallar:
- **Takip eden ajanlar (trafik, kuyruk yürüyüşü):** Her ajan `i`: hedef hız `v0`; öndekine mesafe `gap`; tepki gecikmesi `τ≈1 s`; `a = k·(min(v0, f(gap)) − v)` ve gecikmeli gözlem. Rastgele yavaşlama olasılığı `p` (Nagel–Schreckenberg kural 3) dalgayı kendiliğinden üretir.
- **Hücresel otomat (NaSch):** 1) v<vmax → v+1; 2) v>gap → v=gap; 3) olasılık p ile v−1; 4) x+=v. Zaman ızgarası çizimi için ideal.
- **Kuyruk (servis):** varış λ, servis μ; bekleme süresi sayaçları.
- **Kümelenme (otobüs vb.):** durakta bekleme = taban + k·(son araçtan beri geçen süre).
- **Yayılma:** ağ düğümleri, komşuya geçiş olasılığı β, iyileşme γ.

Çıktı formatı: `frames[f] = { agents: [{id, x, y, angle, v, brake, state}], metrics: {...} }` → JSON. Remotion'da `useCurrentFrame()` ile indekslenir.

Sim yazmak istemeyen hızlı iş akışı: aktörün "kötü bölgesini" elle tanımla (`θ_jam(t) = θ0 − ω·t` gibi), bölgeye giren ajanların hızını düşür. Görsel olarak aynı sonucu verir.

## 1. Sinyal glow
- Opaklık = smoothstep(brake) (veya `1 − v/v0`); yükselme ~0,15 sn, sönme ~0,5 sn.
- Çekirdek: nesnenin arka kenarında 2 parlak nokta; dış: blur yarıçapı ≈ 3–4 nesne boyu; blend screen/add; nesnelerin **üstünde**, vurgu şekillerinin altında.
- (Remotion: `<circle filter="url(#blur)" style={{mixBlendMode:'screen'}} opacity={g}/>` · AE: kırmızı solid + Fast Box Blur + Add, opaklık expression'la slider'a bağlı.)

## 2. Döngü deneyi (T-LOOP)
Zaman çizelgesi (bölüm ~29 sn):
| t | Olay |
|---|---|
| 0,0 | Dip-in (0,3 sn); döngü + ajanlar tam görünür, akış başlamış |
| 0,4 | H1 başlık fade 0,3 sn; ~6 sn sonra söner |
| 5 | H0 dev sayı ("N AGENTS") |
| 7 / 11 | Düzenek satırları (ölçü, kural) — VO'yla birebir |
| 14 | İç yön oku + "ALL GOING ROUND"-tipi etiket |
| 17 | "NO X YET" durum satırı |
| 19–21 | Sinyal doğar; durum satırı söner |
| 21–28 | Dış veri yayı sinyalin kapsadığı açıyı takip eder, akışın **tersine** uzar; sayaç "N STOPPED" ~1 sn adım |
| 27 | Yay ucuna ok başı (dalganın yönü = punchline) |
Geometri: döngü çapı ≈ %70–78H, yol kalınlığı ≈ %4,5H, dış yay = dış yarıçap + %4H, yay kalınlığı ≈ %0,7H yuvarlak uç. Merkez metin satır aralığı ≈ %5H.
Özgünleştirme: halka yerine oval pist, köşeli devre, düz çizgi + "sarma" (soldan çıkan sağdan girer) veya spiral.

## 3. Zincir çubukları (nedensellik zinciri)
- Ajan i olay yaşayınca üstünde dikey çubuk 0→h_i (0,4 sn ease-out); h_i bir öncekinden büyük (ör. 0,15 · 0,35 · 0,55 · 0,75 · 1,0 · 1,0).
- i ile i+1 arasında tepki zamanlayıcısı (pasta, saat yönünde 1 sn doğrusal dolar).
- Çubuk tepelerini kesik polyline birleştirir; zincir sonunda "STOPPED"-tipi etiket.
- Bitişte zoom-out (ölçek 1 → 0,6, 1 sn ease-in-out) → "bu her yerde oluyor".

## 4. Zaman-uzay diyagramı
| t | Olay |
|---|---|
| 0 | Dip; kaynak şeridi (sistemin dikey ince hali) kenarda |
| 1 | "SEEN FROM ABOVE"-tipi yöntem etiketi |
| 5 | Örnekleme çerçevesi + "ONE PICTURE A SECOND"-tipi etiket |
| 8 | Panel fade 0,3 sn |
| 8–10,5 | Nokta sütunları soldan sağa (~0,15 sn/sütun); durmuş noktalar sinyal renginde |
| 10,5 | Noktalar tek adımda çizgilere dönüşür |
| 11–23 | Çizgilerin sağ ucu sim zamanıyla uzar; bir ajan vurgu renginde |
| 16 / 19 | Lejant satır 1 / satır 2 |
| 24 | Dalga cephesi düz çizgi line-draw 1 sn |
| 27 | Cephe etiketi |
Eksenler: dikey "DISTANCE …" (90° döndürülmüş), yatay "TIME →". Kaynak şeridi ile panel arasında ince kesik kılavuz çizgiler.

## 5. Akış/yoğunluk eğrisi + reframe
- Döngüde ajan sayısı adım adım artar (sayaç 12→15→18→21→23, ~1 sn).
- Reframe: döngü x %50 → %28, 0,5 sn ease-in-out; sağda panel fade (0,3 sn, 0,1 sn gecikmeli).
- Vurgu rengi veri noktası eğri boyunca ilerler, arkasında iz (5 sn); tepe sonrası iniş gürültülü; tepeye dikey kesik çizgi + "THE MOST IT CAN …" etiketi.

## 6. Panel, bar, sayaç, zamanlayıcı
- **Panel:** fade 0,3 sn ease-out; konum tipik alt-orta (x %35–77, y %62–90) veya sağ (x %52–98).
- **Bar:** koyu ray + yuvarlak uçlu dolgu; dolgu genişliği veriye bağlı; sağında sayısal değer ("2.8 S", "+10%").
- **Karşılaştırma çifti:** iki bar sırayla; ikinci barın daha uzun/kısa olması punchline.
- **Sayaç:** night-map'te tween'siz anlık (veri hissi), transit-ink'te 0,6 sn tween.
- **Pasta zamanlayıcı:** dilim saat yönünde doğrusal; dolunca söner.
- **Gösterge (gauge):** yarım daire, ibre "MORE"dan hedefe 3 sn ease-in-out.

## 7. Vurgu halkası / kontur / ok / yay
- Halka pulse: çap %4H → %15H, opaklık 1→0, 0,8–1 sn ease-out.
- Kontur: yuvarlatılmış dikdörtgen, hedef kümeyi %10 payla sarar, kümeyle birlikte hareket eder (takip). "Eski yer" için kesik çizgili hayalet kontur.
- Yön oku: ince çizgi + küçük ok başı, etiketli; sistem yönü beyaz, sinyal yönü sinyal renginde.
- Yay: dairesel, `trim`/arc açıları veriden.

## 8. Kural kartları + kaldırma
- Kartlar soldan sağa VO'daki "One / Two / Three / Four" ile stagger.
- Konuşulan kart: kenarlık + rakam vurgu rengine (<0,2 sn).
- Kaldırma: kartın üzerine sinyal renginde çapraz çizgi line-draw 0,3 sn; sim parametresi aynı karede değişir (ör. p=0) ve zaman ızgarasında dalgalar kaybolur → "NO JAMS"-tipi etiket.

## 9. Checklist
Satırlar baştan soluk (%35); VO özet cümlesine göre sırayla ✓ (stroke draw 0,3 sn) + satır %100; her satırın sağında o bölümün mini canlı simülasyonu (döngüde).

## 10. Geçiş ve başlık
- **Dip:** tam ekran panel rengi; 0,00–0,12 sn 0→1 · 0,12–0,20 tam · 0,20–0,50 1→0. (Resolve/Premiere: Dip to Color, 15 kare @30 fps.)
- **H1:** dip bitişi +0,3–0,5 sn; fade 0,3 sn; 5–10 sn; fade-out 0,3 sn. Kanal imzası (dikey çubuk / bölüm numarası) metinle aynı anda.

## 11. Remotion iskeleti
```
src/
  tokens.ts            // renkler, fontlar, süreler (FADE=9, DIP=15 kare)
  sim/<konu>.ts        // simulate(params, seed) -> frames[]
  components/
    World.tsx          // zemin + doku
    Agent.tsx Glow.tsx Track.tsx (Loop, Strip, Curve)
    Panel.tsx Bar.tsx Counter.tsx PieTimer.tsx Gauge.tsx
    Label.tsx SectionTitle.tsx HighlightRing.tsx Outline.tsx Arrow.tsx ArcArrow.tsx
    RuleCards.tsx Checklist.tsx Dip.tsx
  scenes/V01_Hook.tsx … V18_Close.tsx   // her vuruş bir <Sequence>
  timing/vo_alignment.json             // ElevenLabs kelime zamanları → Label inAt
```
Kural: `Label` bileşeni `inAt`'i elle değil `wordStart("keyword")` ile alır; böylece VO değişince etiketler otomatik kayar.
