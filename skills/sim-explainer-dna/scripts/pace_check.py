"""Ritim QA: üretim paketindeki senaryonun konuşma hızını ve ekran olayı yoğunluğunu ölçer.

Kullanım:  python pace_check.py <paket.md> [--wpm 150]

Beklenen biçim (paketin "## 5. Senaryo" bölümü):
    ## [00:00] V1 · HOOK
    VO metni...
    > EKRAN: [00:03] SİM ...
Bölüm, bir sonraki "## <sayı>." başlığında biter. Çıktı Markdown'dur; paketin 12. bölümüne yapıştırılabilir.
"""
import re
import sys

SCENE = re.compile(r"^##\s*\[(\d{1,2}):(\d{2})\]\s*(.*)$")
EVENT = re.compile(r"^>\s*EKRAN:\s*\[(\d{1,2}):(\d{2})\]")
SECTION = re.compile(r"^##\s*(\d+)\.")


def secs(m, s):
    return int(m) * 60 + int(s)


def parse(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    inside, scenes = False, []
    for line in lines:
        sec = SECTION.match(line)
        if sec:
            inside = sec.group(1) == "5"
            continue
        if not inside:
            continue
        sc = SCENE.match(line)
        if sc:
            scenes.append({"start": secs(sc.group(1), sc.group(2)), "name": sc.group(3).strip(),
                           "text": [], "events": []})
            continue
        if not scenes:
            continue
        ev = EVENT.match(line)
        if ev:
            scenes[-1]["events"].append(secs(ev.group(1), ev.group(2)))
        elif line.strip() and not line.lstrip().startswith((">", "#", "|")):
            scenes[-1]["text"].append(line.strip())
    return scenes


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    wpm = 150
    if "--wpm" in sys.argv:
        wpm = float(sys.argv[sys.argv.index("--wpm") + 1])
    scenes = parse(sys.argv[1])
    if not scenes:
        print("Senaryo bölümünde '## [mm:ss] V..' başlığı bulunamadı.")
        sys.exit(1)

    warnings, rows, total_words = [], [], 0
    for i, sc in enumerate(scenes):
        text = " ".join(sc["text"])
        words = len(re.findall(r"[\w'’-]+", text))
        total_words += words
        spoken = words / wpm * 60
        end = scenes[i + 1]["start"] if i + 1 < len(scenes) else sc["start"] + spoken
        dur = max(end - sc["start"], 0.1)
        local_wpm = words / dur * 60
        n_ev = len(sc["events"])
        gap = dur / max(n_ev, 1)
        flags = []
        if local_wpm > 170:
            flags.append("VO sığmıyor")
        if local_wpm < 120 and words:
            flags.append("VO seyrek")
        limit = 3 if i == 0 else 4
        if gap > limit:
            flags.append(f"olay seyrek ({gap:.1f} sn/olay)")
        if any(not (sc["start"] <= e <= end + 0.5) for e in sc["events"]):
            flags.append("olay zamanı sahne dışında")
        rows.append((sc["name"], sc["start"], dur, words, local_wpm, n_ev, gap, ", ".join(flags) or "✓"))
        warnings += [f"{sc['name']}: {f}" for f in flags]

    hook = " ".join(scenes[0]["text"])
    hook_words = len(re.findall(r"[\w'’-]+", hook))
    first = re.split(r"(?<=[.!?])\s+", hook.strip())[0] if hook.strip() else ""
    first_words = len(first.split())
    if hook_words > 80:
        warnings.append(f"Hook {hook_words} kelime (hedef ≤80)")
    if first_words > 8:
        warnings.append(f"Hook ilk cümlesi {first_words} kelime (hedef ≤8)")
    total_dur = rows[-1][1] + rows[-1][2]
    overall = total_words / total_dur * 60

    print("| Vuruş | Başlangıç | Süre (sn) | Kelime | Kel/dk | Olay | sn/olay | Durum |")
    print("|---|---|---|---|---|---|---|---|")
    for name, st, dur, w, lw, ne, gap, fl in rows:
        print(f"| {name} | {st//60:02d}:{st%60:02d} | {dur:.0f} | {w} | {lw:.0f} | {ne} | {gap:.1f} | {fl} |")
    print()
    print(f"Toplam: {total_words} kelime · {total_dur/60:.1f} dk · ortalama {overall:.0f} kel/dk (hedef 145–155)")
    print(f"Hook: {hook_words} kelime, ilk cümle {first_words} kelime")
    print("Uyarılar: " + ("; ".join(warnings) if warnings else "yok"))


if __name__ == "__main__":
    main()
