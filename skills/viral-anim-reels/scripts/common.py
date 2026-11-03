"""Shared helpers for the viral-anim-reels pipeline (stdlib only + ffmpeg on PATH)."""
import json, os, subprocess, sys

for _st in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252; Turkish text needs UTF-8
    try:
        _st.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

SKILL = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ROOT_DEFAULT = os.environ.get("VIRAL_REELS_ROOT", r"C:\dev\viral-reels")
W, H, FPS = 1080, 1920, 30


def load(path, default=None):
    if not os.path.exists(path):
        if default is not None:
            return default
        sys.exit(f"missing: {path}")
    return json.load(open(path, encoding="utf-8"))


def save(path, obj):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    json.dump(obj, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def project_dir(arg):
    """Accept a slug or a path."""
    if os.path.isdir(arg):
        return os.path.abspath(arg)
    p = os.path.join(ROOT_DEFAULT, arg)
    if not os.path.isdir(p):
        sys.exit(f"project not found: {arg} (looked in {ROOT_DEFAULT})")
    return p


def run(cmd, check=True):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd[:6])} ...\n{r.stderr[-1500:]}")
    return r


def duration(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path])
    return float(r.stdout.strip() or 0)


def font():
    """Return (fontfile, family) for captions/cover: bundled Montserrat ExtraBold, else Arial Black."""
    for fn, fam in [("Montserrat-ExtraBold.ttf", "Montserrat ExtraBold"), ("Montserrat-Black.ttf", "Montserrat Black")]:
        p = os.path.join(SKILL, "fonts", fn)
        if os.path.exists(p):
            return p, fam
    return r"C:/Windows/Fonts/ariblk.ttf", "Arial Black"


def ff_path(p):
    """Escape a Windows path for use inside an ffmpeg filter argument."""
    return p.replace("\\", "/").replace(":", "\\:")


def words_of(text):
    import re
    return re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüÂâÎîÛû0-9$%£€₺][A-Za-zÇĞİÖŞÜçğıöşüÂâÎîÛû0-9'’$%£€₺.,-]*", text)


def lower(text, lang="en"):
    return (text.replace("I", "ı").replace("İ", "i") if lang == "tr" else text).lower()


def upper(text, lang="en"):
    return (text.replace("i", "İ").replace("ı", "I") if lang == "tr" else text).upper()


# Language profiles. EN numbers are measured (deep-research/B, D); TR is derived: Turkish words are
# ~25 % longer (agglutinative), so the same 220-wpm energy lands at ~165 wpm and fewer words per minute.
LANG = {
    "en": dict(
        wpm=215, words=(160, 235), hook_words=(10, 19), title_words=(5, 7),
        school={"science", "behind", "actually", "explained", "facts", "works"}, title_ban_start="this ",
        stake=r"\b(million|billion|thousand|\$\d|illegal|banned|law|alive|die|dead|died|kill|fired|arrest|jail|prison|crime|fortune|free|empire|forever|lifetime|never|nobody|every)\b",
        pivots=r"\b(but|yet|except|instead|wait|you see|so|turns out|then|unless|until)\b",
        hinge=r"\byou see\b", hinge_name="You see,", proxy=r"\bwait\b", proxy_name="Wait, ...?",
        hook_ban=r"\s*(look|imagine|have you|did you know|what if|how|why)\b",
        anomaly=r"\b(that|who|nobody|never|can't|cannot|only|keep|keeps|banned|illegal|legal|really|twice|secret|hidden|why|what|levels|vs|forgot|regretted|broke|fooled|beat|paid|pays)\b",
        title_q=r"(what if|would you|can you|is |legal)",
        legend=r"\b(legend|story goes|imagine|they say)\b", gstar=r"most historians|some say|myth",
        func={"a", "an", "the", "to", "of", "in", "on", "at", "and", "but", "so", "or", "your", "his", "her", "my",
              "it's", "is", "was", "no", "just", "for", "by", "he", "she", "they", "it", "i", "we", "you"}),
    "tr": dict(
        wpm=165, words=(125, 185), hook_words=(8, 16), title_words=(4, 7),
        school={"bilim", "bilimi", "ardındaki", "arkasındaki", "aslında", "açıklandı", "açıklıyoruz", "gerçekler", "bilgiler", "nasıl"},
        title_ban_start="bu ",
        stake=r"(milyon|milyar|bin\b|\$\d|₺|yasak|yasal|kanun|hapis|ceza|öldü|ölüm|idam|servet|bedava|imparatorluk|ömür boyu|asla|hiç kimse|hepsini|tamamını|cia|fbi)",
        pivots=r"\b(ama|fakat|ancak|yine de|bekle|işte|meğer|üstelik|sonra|derken|çünkü|oysa|yani)\b",
        hinge=r"\b(işin sırrı|mesele şu|olay şu|bakın)\b", hinge_name="Mesele şu / İşin sırrı",
        proxy=r"\bbekle\b", proxy_name="Bekle, ...?",
        hook_ban=r"\s*(bak|hayal et|biliyor muydunuz|biliyor musun|ya |nasıl|neden)\b",
        anomaly=r"(kaçılamaz|imkânsız|imkansız|sahte|yasak|yasal|asla|hiç|kimse|sadece|tek|gizli|bütün|hepsini|tamamını|iki kez|ödeyen|alan|yenen|kandıran|bozan|neden|pişman)",
        title_q=r"(ya |yasal mı|alır mıydın|yapar mıydın)",
        legend=r"\b(rivayete göre|efsaneye göre|anlatılır|hayal et)\b", gstar=r"tarihçilerin çoğu|bazıları|efsane|rivayet",
        func={"ve", "bir", "bu", "şu", "o", "da", "de", "ile", "en", "çok", "ki", "mi", "mı", "mu", "mü", "ama", "her",
              "hiç", "daha", "gibi", "için", "ne", "sen", "ben", "onun", "bunu", "şunu"}),
}


def lang_of(script):
    return script.get("lang", "en") if script.get("lang", "en") in LANG else "en"
