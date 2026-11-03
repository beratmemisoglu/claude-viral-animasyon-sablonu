"""Paketin senaryosundan (bölüm 5) YouTube'a yüklenebilir SRT altyazı üretir.

Kullanım:  python make_srt.py <paket.md> [-o altyazi_en.srt] [--wpm 150] [--chars 42]

time_beats.py'den SONRA çalıştır: her vuruş kendi "## [mm:ss] Vn" başlığından başlar, cümleler
kelime sayısı / wpm ile zamanlanır. Kart başına en çok 2 satır, satır başına en çok --chars karakter;
bölme önce noktalamada, sonra kelime sınırında yapılır. Gerçek ses gelince --wpm ile yeniden üret
(veya YouTube Studio'da "otomatik senkronizasyon" için düz metni kullan: --plain).
"""
import re
import sys

SCENE = re.compile(r"^##\s*\[(\d{1,2}):(\d{2})\]\s*V\d+")
SECTION = re.compile(r"^##\s*(\d+)\.")


def ts(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def beats(path):
    out, inside, cur = [], False, None
    for line in open(path, encoding="utf-8").read().splitlines():
        sec = SECTION.match(line)
        if sec:
            inside = sec.group(1) == "5"
            continue
        if not inside:
            continue
        m = SCENE.match(line)
        if m:
            cur = {"start": int(m.group(1)) * 60 + int(m.group(2)), "text": []}
            out.append(cur)
        elif cur is not None and line.strip() and not line.lstrip().startswith((">", "#", "|")):
            cur["text"].append(line.strip())
    return out


def chunks(sentence, limit):
    """Cümleyi ≤2*limit karakterlik kartlara böl; virgülde bölmeyi tercih et."""
    words, cards, cur = sentence.split(), [], []
    for w in words:
        trial = " ".join(cur + [w])
        if len(trial) > 2 * limit and cur:
            cards.append(cur)
            cur = [w]
        else:
            cur.append(w)
            if w.endswith((",", ";", ":")) and len(trial) > limit:
                cards.append(cur)
                cur = []
    if cur:
        cards.append(cur)
    return cards


def two_lines(words, limit):
    text = " ".join(words)
    if len(text) <= limit:
        return text
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if len(a) <= limit and len(b) <= limit:
            score = abs(len(a) - len(b))
            if best is None or score < best[0]:
                best = (score, a + "\n" + b)
    return best[1] if best else text


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    path = args[0]
    out = args[args.index("-o") + 1] if "-o" in args else re.sub(r"\.md$", "", path) + "_altyazi_en.srt"
    wpm = float(args[args.index("--wpm") + 1]) if "--wpm" in args else 150.0
    limit = int(args[args.index("--chars") + 1]) if "--chars" in args else 42
    sps = 60.0 / wpm
    bs = beats(path)
    if not bs:
        sys.exit("Bölüm 5'te zamanlı '## [mm:ss] Vn' başlığı yok — önce time_beats.py çalıştır.")
    if "--plain" in args:
        open(out, "w", encoding="utf-8").write("\n\n".join(" ".join(b["text"]) for b in bs) + "\n")
        print("düz metin ->", out)
        return
    cues = []
    for k, b in enumerate(bs):
        t = float(b["start"])
        end_limit = bs[k + 1]["start"] - 0.1 if k + 1 < len(bs) else None
        sentences = re.split(r"(?<=[.!?])\s+", " ".join(b["text"]))
        for sent in sentences:
            for words in chunks(sent, limit):
                dur = max(len(words) * sps, 1.0)
                end = t + dur
                if end_limit is not None:
                    end = min(end, end_limit)
                cues.append((t, max(end, t + 0.5), two_lines(words, limit)))
                t = end + 0.05
    with open(out, "w", encoding="utf-8") as f:
        for i, (a, b, text) in enumerate(cues, 1):
            f.write(f"{i}\n{ts(a)} --> {ts(b)}\n{text}\n\n")
    print(f"{len(cues)} altyazı kartı · son {ts(cues[-1][1])} -> {out}")


if __name__ == "__main__":
    main()
