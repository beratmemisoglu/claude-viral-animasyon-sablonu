"""Senaryo taslağına zaman damgası basar: vuruş başlıklarını ve ekran olaylarını kelime sayısından zamanlar.

Kullanım:  python time_beats.py <paket.md> [--wpm 150] [--pause 0.6] [-o çıktı.md]
(-o verilmezse dosya yerinde güncellenir.)

Taslak biçimi ("## 5. Senaryo" bölümünde):
    ## V1 · HOOK                       (veya önceden zamanlanmış: ## [00:00] V1 · HOOK)
    You've waited twenty minutes for a bus.
    > EKRAN: @twenty SAYAÇ "20 MIN" pill
    > EKRAN: @+2.5 SİM otobüs kayar      (önceki olaydan 2,5 sn sonra)
"@kelime" → olay, o kelimenin vuruştaki İLK geçişinin konuşulduğu ana (+0,2 sn) yerleşir.
"@+N" → önceki olaydan N sn sonra. "@" yoksa mevcut [mm:ss] korunur.
Vuruşlar arası --pause saniye paragraf durağı eklenir (geçiş yeri).
"""
import re
import sys

SCENE = re.compile(r"^##\s*(?:\[\d{1,2}:\d{2}\]\s*)?(V\d+.*)$")
EVENT = re.compile(r"^(>\s*EKRAN:\s*)(?:\[\d{1,2}:\d{2}\]\s*)?(@(\+?[\w'’.-]+)\s+)?(.*)$")
SECTION = re.compile(r"^##\s*(\d+)\.")
WORD = re.compile(r"[\w'’-]+")


def fmt(t):
    t = int(round(t))
    return f"[{t // 60:02d}:{t % 60:02d}]"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    path = args[0]
    wpm = float(args[args.index("--wpm") + 1]) if "--wpm" in args else 150.0
    pause = float(args[args.index("--pause") + 1]) if "--pause" in args else 0.6
    out = args[args.index("-o") + 1] if "-o" in args else path
    sps = 60.0 / wpm

    lines = open(path, encoding="utf-8").read().splitlines()
    # 1. geçiş: vuruşları ve VO kelimelerini topla
    beats, inside, cur = [], False, None
    for i, line in enumerate(lines):
        sec = SECTION.match(line)
        if sec:
            inside = sec.group(1) == "5"
            continue
        if not inside:
            continue
        sc = SCENE.match(line)
        if sc:
            cur = {"line": i, "name": sc.group(1).strip(), "words": [], "events": []}
            beats.append(cur)
        elif cur is not None:
            if EVENT.match(line):
                cur["events"].append(i)
            elif line.strip() and not line.lstrip().startswith((">", "#", "|")):
                cur["words"] += WORD.findall(line)

    # 2. geçiş: zamanla ve yeniden yaz
    t = 0.0
    for b in beats:
        start = t
        lines[b["line"]] = f"## {fmt(start)} {b['name']}"
        lower = [w.lower() for w in b["words"]]
        last = start
        for i in b["events"]:
            m = EVENT.match(lines[i])
            prefix, anchor, rest = m.group(1), m.group(3), m.group(4)
            if anchor is None:
                old = re.search(r"\[(\d{1,2}):(\d{2})\]", lines[i])
                et = int(old.group(1)) * 60 + int(old.group(2)) if old else last
            elif anchor.startswith("+"):
                et = last + float(anchor[1:])
            else:
                key = anchor.lower()
                idx = next((k for k, w in enumerate(lower) if w.startswith(key)), None)
                if idx is None:
                    print(f"Uyarı: '{anchor}' kelimesi {b['name']} içinde yok; önceki olay +2 sn kullanıldı")
                    et = last + 2
                else:
                    et = start + idx * sps + 0.2
            last = et
            lines[i] = f"{prefix}{fmt(et)} {rest}"
        t = start + len(b["words"]) * sps + pause

    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{len(beats)} vuruş zamanlandı · toplam {t / 60:.1f} dk · {out}")


if __name__ == "__main__":
    main()
