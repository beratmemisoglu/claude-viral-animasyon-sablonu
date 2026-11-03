# Thumbnail Sistemi ("PHANTOM JAM" formülü)

Referans görsel: `assets/reference_thumbnail_phantom_jam.png` (3,6M / 12 gün).

## 1. Referansın çözümlemesi
| Öğe | Gözlem |
|---|---|
| Metin | 2 kelime, iki satır: **PHANTOM** (kehribar ≈#F0A848) / **JAM** (beyaz), kalın dar grotesk, BÜYÜK HARF; altında kehribar kısa alt çizgi. Metin sol üst ~%45 genişlik, toplam yüksekliğin ~%45'i |
| Metin içeriği | Başlığı tekrar etmiyor; olguya **uydurulmuş/az bilinen bir ad** veriyor ("phantom jam" = hayalet sıkışıklık). Merak: "bu ne?" |
| Zemin | Üst yarı düz lacivert gradyan (≈#1B2848–#223158) — videonun koyu yeşilinden **daha parlak ve doygun** |
| Görsel | Alt yarıda sol alttan sağ üste çapraz yükselen geniş yol, kenarlarda yeşil çim şeridi; asfalt videodakinden açık (≈#6A6F7B) |
| Hikâye | **Sol yarı:** kırmızı fren ışıklı yoğun araç kümesi. **Sağ yarı:** boş yol + tek araç. Tek karede "sıkışma var ama sebep yok" — gizem kanıtı görsel |
| Kontrast | En parlak öğeler: kehribar kelime + kırmızı glow; ikisi farklı köşelerde → göz Z deseniyle gezer (metin → küme → boş yol) |
| Videoyla bağ | Aynı araç ikonları, aynı glow, aynı tipografi ailesi → tıklayan beklediğini bulur |
| Ne YOK | Yüz, ok, emoji, kırmızı daire, şok ifadesi. Sakin, "bilgi grafiği" ciddiyeti |

## 2. Formül
`[2 kelimelik olgu adı: renkli kelime + beyaz kelime]` + `[sistemin tek karede "problem | sebepsizlik" ikiliği]` + `[videodaki görsel dil, %20–30 daha parlak/doygun]`

Kurallar:
1. Metin ≤3 kelime, ideal 2; başlıktaki kelimeleri tekrar etme. Olgunun **adı** (bilimsel ya da merak uyandıran takma ad): "PHANTOM JAM", "BUS BUNCHING", "THE BULLWHIP", "QUEUE TRAP".
2. Görselin yarısı problem (sinyal rengi), yarısı "sebepsizlik"/boşluk. Bu karşıtlık başlıktaki "for no reason" sözünü kanıtlar.
3. Çapraz kompozisyon (sol alt → sağ üst) — hareket ve yükseliş hissi; metin karşı köşede.
4. Arka plan videodan bir ton parlak; küçük ekranda (mobil ~160 px genişlik) metin okunur olmalı: harf yüksekliği ≥ görüntü yüksekliğinin %18'i.
5. Tek sıcak sinyal rengi + tek vurgu rengi (metin kelimesi). Üçüncü parlak renk yok.
6. Yüz/emoji/ok yok — formatın güven duygusu ciddiyetten geliyor. (Kanal A/B testiyle aksini kanıtlarsa değiştir.)

## 3. Konsept üretimi (her pakette 3)
| Konsept | Yaklaşım |
|---|---|
| T1 Karşıtlık (önerilen) | Referans formülü: sistem çapraz, yarısı sinyal kümesi, yarısı boş; 2 kelimelik ad |
| T2 Tek ajan | Uzun bir sinyal dizisinin önünde/arkasında vurgu renginde tek ajan + boşluk ("ONE CAR" / "ONE BUS") — videonun güç vaadini satar |
| T3 Grafik | Sadeleştirilmiş tek grafik (ör. tepe yapıp çöken eğri, geriye giden çizgi) + 2 kelime — meraklı/inek kitle için |

Her konsept için yaz: metin (satır satır, renkleriyle) · kompozisyon (öğe konumları %) · renkler · neden tıklanır (tek cümle) · başlık eşleşmesi (hangi başlık seçeneğiyle).

## 4. Görsel üretim
- **Tercih:** Thumbnail'ı video ile aynı Remotion bileşenleriyle render et (`<Still>` 1280×720): tutarlılık + sıfır maliyet. Metni AI'a bırakma; metin katmanını kodla/editörle ekle.
- **AI görsel (opsiyonel, metinsiz arka plan için) prompt şablonu:**
  `Top-down flat vector infographic illustration, [sistem tanımı] running diagonally from bottom-left to top-right, [sinyal öğesi] glowing [renk] clustered on the left half, empty [sistem] with a single [ajan] on the right half, clean dark [zemin rengi] background with subtle gradient, minimal, crisp, no text, no people, 16:9, high contrast, YouTube thumbnail composition with empty space top-left for title`
- **QA:** 1280×720'i 168×94'e küçült ve kontrol et: metin okunuyor mu, küme seçiliyor mu, iki yarı ayırt ediliyor mu.
