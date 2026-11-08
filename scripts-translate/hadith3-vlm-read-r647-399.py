# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM R647 (fiable-dégradé) slot pdf-mut23h2x-399, leçon 10.
Cinq lectures image pour trancher les zones où l'OCR couches est dégradé :
p.72 (trois ḥadīṯs + notice Ǧābir + gloses), p.74 (réf. Fatiḥ al-Bārī + 1068 +
Muzāhama), p.75 (1066 + 1064 + rubrique ثالثا), p.77 (istiṯmār + iʿdād qiblī),
composite p.73-duʿā + p.76-isnād. Budget doctrine : ≤6 lectures par sous-passe.
Mécanisme hadith3-vlm-read-399.py (z-ai vision, cache _read-r647-*.json)."""
import json
import os
import subprocess
import sys
import time

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
DIR = "/home/z/my-project/tr-tmp/qa-crops-r647"
os.makedirs(DIR, exist_ok=True)

# Rendus de pages manquants (300 dpi, même format que les r649-*.png)
doc = fitz.open(PDF)


def render(page_no: int, tag: str) -> None:
    path = f"{DIR}/{tag}.png"
    if os.path.exists(path) and os.path.getsize(path) > 100_000:
        print(f"rendu présent : {path}")
        return
    pix = doc[page_no - 1].get_pixmap(dpi=300)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img.save(path)
    print(f"OK rendu {path} — {img.size[0]}x{img.size[1]}")


for pg, tag in [(72, "r647-p72-full"), (74, "r647-p74-full"),
                (75, "r647-p75-full"), (77, "r647-p77-full")]:
    render(pg, tag)


def band(page_no: int, y0: float, y1: float, dpi: int = 450):
    pix = doc[page_no - 1].get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    W, H = img.size
    return img.crop((0, int(H * y0), W, int(H * y1)))


# Composite : bande duʿā p.73 (30-70 %) + bande isnād/istiṯmār p.76 (45-100 %)
comp_path = f"{DIR}/r647-composite-p73dua-p76isnad.png"
if not (os.path.exists(comp_path) and os.path.getsize(comp_path) > 100_000):
    a = band(73, 0.28, 0.72)
    b = band(76, 0.42, 1.00)
    sep = Image.new("RGB", (max(a.width, b.width), 12), (255, 210, 90))
    total_h = a.height + b.height + sep.height
    comp = Image.new("RGB", (max(a.width, b.width), total_h), (255, 255, 255))
    comp.paste(a, (0, 0))
    comp.paste(sep, (0, a.height))
    comp.paste(b, (0, a.height + sep.height))
    comp.save(comp_path)
    print(f"OK composite {comp_path} — {comp.size[0]}x{comp.size[1]}")

PROMPTS = {
    "r647-p72-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY in reading order. "
        "1) First hadith: مالك عن عروة بن هشام عن أبيه أنه قال: قال رسول الله ﷺ لعبد الرحمن بن "
        "عوف: كيف صنعتَ يا أبا محمد في الاستلام من الركن؟ — transcribe EVERY word, the blue "
        "[الموطأ رقم: NNN] digits digit-by-digit. "
        "2) Second hadith: مالك عن هشام بن عروة عن أبيه أن عمر بن الخطاب قال وهو يطوف بالبيت "
        "للركن الأسود: «إنما أنت حجر...» — transcribe the FULL sentence letter by letter: what "
        "follows حجر (لا يحجن؟ لا يضر؟ لا ينفع؟), and the exact ending (ولولا أني رأيت رسول الله "
        "ﷺ قد قبّلَكَ ما قبّلتُك؟ ولولا أن رسول الله ﷺ قبّلَكَ؟) — do NOT normalize, what you SEE; "
        "blue ref digits digit-by-digit. "
        "3) Third hadith about عبد الرحمن بن عبد القاري / عبد الله بن عمر and عمر, الصبح, طوافة, "
        "حنى, فرَكب, بذي طوى — transcribe EVERY word exactly, blue ref digits digit-by-digit. "
        "4) The biography note about جابر بن عبد الله (الأنصاري الخزرجي...) at the bottom: "
        "transcribe FULLY; the digit of the number of his hadiths في الصحيح — read it digit by "
        "digit (is it 87 or 78?), and his death-year digits digit-by-digit. "
        "5) The two gloss lines at the very bottom (الاشتلام: افتعال من... and رَمَلَ: أسرع في...) "
        "EXACTLY. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r647-p74-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY. "
        "1) The very top line(s): a bracketed book-reference — transcribe the bracket content "
        "letter by letter: does it read [فتح الباري لابن حجر]؟ and what words precede the quote "
        "«ليس هو بسنة، من شاء رمَل ومن شاء لم يرمَل» (قال ابن الباري؟ قال ابن حجر؟ عنهم الله؟) "
        "letter by letter — do NOT normalize. "
        "2) The following sentence ويستثنى من ذلك من أحرم من مكة فلا يستحب له الرمل فعن نافع أن "
        "عبد الله... and the blue [الموطأ رقم: NNN] digits digit-by-digit. "
        "3) The green rubric ثانيا: الطواف الاستلام EXACTLY. "
        "4) Item 1- تقبيل الركن الأسود عند الاستلام: transcribe the FULL prose paragraph and the "
        "quote of عمر (إنما أنت حجر...) with its EXACT ending, and the quote of مالك beginning "
        "سمعتُ بعض أهل العلم (about الركن اليماني, the hand, الفم, تقبيل) — EVERY word, blue ref "
        "digits digit-by-digit. "
        "5) Item 2- المزاحمة على استلام الركن: transcribe the FULL prose (المراد باستلام الركن "
        "تقبيله... فإن زُحم عن تقبيله لمسه بيده... فإن لم تصل يده فبعُود...) and the story of عبد "
        "الرحمن بن عوف (إذا أتى الركن فوجدهم يزدحمون عليه... كبر ودفّع؟ قال عروة: قال رسول الله...) "
        "down to the bottom of the page. Mark illegible as [؟]. Short French notes at the end."
    ),
    "r647-p75-full": (
        "Full Arabic schoolbook page. Transcribe ALL Arabic lines EXACTLY in reading order. "
        "1) Top lines ending the previous story (فقال عبد الرحمن بن عوف: لمستُه وتركتُه. فقال له "
        "رسول الله ﷺ: «أصبتَ»؟) EXACTLY. "
        "2) Item 3- استلام الأركان الأربعة: full prose (على الجمهور أنه لا يُستلم إلا الركن "
        "الأسود واليماني ولا يستلم الركنان الشاميان أما...), the passage ثبت من طريق عن هشام بن "
        "عروة, the blue [الموطأ رقم: NNN] digits digit-by-digit, and the reason about عبد الله "
        "بن الزبير (فلأن عبد الله بن الزبير لما عمرّ الكعبة أتمّ البيت على قواعد إسماعيل وبقي "
        "الأمر على هذا حتى قتل عبد الله). "
        "3) Item 4- استلام الركن الأسود بعد الطواف: full prose and quote أن رسول الله ﷺ كان إذا "
        "قضا طوافه صلى الركعتين وأراد أن يخرج إلى الصفا والمروة استلم الركن الأسود قبل أن يخرج, "
        "blue ref digit-by-digit, and the closing sentence (وهذا إن أمكن ذلك دون إذاية للنفس أو "
        "غيره؟). "
        "4) The green rubric ثالثا: ركعتا الطواف EXACTLY and its first item (حكم ركعتَي الطواف "
        "بعد الصبح والعصر؟): the hadith of عمر بن الخطاب / عبد الرحمن بن عبد القاري / عبد الله "
        "بن عمر — EVERY word (صلاة الصبح؟ طوافة؟ نظر؟ حنى؟ فرَكب؟ بذي طوى؟ ركعتين؟ فصلى؟) with "
        "blue ref digits digit-by-digit, and the words of مالك (لا يرى النفل بعد صلاة الصبح حتى "
        "تطلع الشمس؟ وأن يطوف الرجل طافاً واحداً بعد الصبح ثم يصلي الركعتين؟ يزيد على سبعة "
        "واحداً؟ ويؤخر الركعتين حتى تطلع الشمس كما صلى عمر؟) down to the bottom of the page. "
        "Mark illegible as [؟]. Short French notes at the end."
    ),
    "r647-p77-full": (
        "Full Arabic schoolbook page (short page, end of a lesson). Transcribe ALL Arabic lines "
        "EXACTLY in reading order. "
        "1) The first numbered items at top: 1- أستخرج من الحديث الحكمة من امتناع النبي ﷺ عن "
        "بناء الكعبة على قواعد إبراهيم and 2- لماذا لم يكن النبي ﷺ يستلم الركنين الشاميين؟ — "
        "transcribe exactly; is there a green rubric above them (الاستثمار؟ الأسئلة؟) — name it "
        "letter by letter if visible. "
        "2) The rubric الإعداد القبلي (green pill) — exact wording. "
        "3) The line احفظ أحاديث الدرس المقبل وأستعين بالزرقاني للإجابة عن الآتي: EXACTLY. "
        "4) Numbered question 1: it begins أشرح — transcribe THE WORD AFTER أشرح letter by "
        "letter (it may read أَدْرَنَا؟ أَرْنَدَا؟ أَلْدَرَنَا؟ أَدْرَنَا؟) — do NOT normalize, "
        "glyph by glyph, mark uncertain glyphs [؟]. "
        "5) Numbered question 2 (أبحث عن حكم طواف الحائض) EXACTLY. "
        "Short French notes at the end."
    ),
    "r647-composite-p73dua-p76isnad": (
        "Two stacked crops of an Arabic schoolbook (a yellow separator band between them). "
        "TOP CROP (middle of a page): transcribe EXACTLY the bold hadith with its isnad: عن "
        "هشام بن عروة عن أبيه عروة؟ (or عن غروة؟) كان إذا طاف بالبيت يسعى الأشواط الثلاثة وكان "
        "يقول: — then THE DUʿĀ word by word, letter by letter (it may read: لا إله إلا الله، "
        "وأنت بعد ما أمتَ، لا إله إلا أنت، لا يشغل الناس بسماعهم عما هم فيه، ويخفض دُكَّهُ بذلك؟) "
        "— transcribe what you SEE, do NOT normalize; then قال مالك: وذلك الأمر الذي لم يزل على "
        "أهل العلم ببلدنا، فالرمل سنة في الثلاثة... (transcribe to the end of مالك's words incl. "
        "ولم يخالف إلا ابن عباس؟) and the blue [الموطأ رقم: NNN] digits digit-by-digit. "
        "BOTTOM CROP (bottom half of another page): transcribe EXACTLY the bold hadith of the "
        "الاستثمار rubric: مالك عن ابن شهاب عن سالم بن عبد الله بن عبد الله؟ بن عمر؟ بن محمد بن "
        "أبي بكر الصديق؟ — transcribe the FULL isnad word by word (is there a repetition بن عبد "
        "الله بن عبد الله? does it end بن محمد بن أبي بكر الصديق? who says أخبرني?) then عن "
        "عائشة أن النبي ﷺ قال: and the Prophet's opening words glyph by glyph (ألم تري أن قومك "
        "حين بنوا الكعبة أصرّوا على قواعد إبراهيم؟ ألا تري؟ ألا لمرواة؟) — do NOT normalize; "
        "then عائشة's question (فالت؟ فقلت؟ يار رسول الله ألا نردُها على قواعد إبراهيم؟) and the "
        "Prophet's reply (فقال رسول الله ﷺ: لو لا حدثان قومك بالكفر؟), then the closing words "
        "(قال عبد الله بن عمر: لقد كانت عائشة سمعت هذا من رسول الله، ما أرى رسول الله ﷺ ترك "
        "استلام الركنين اللذين يليان الحجر إلا أن البيت لم يتمم على قواعد إبراهيم؟) and the blue "
        "[الموطأ رقم: NNN] digits digit-by-digit. Mark illegible as [؟]. Short French notes."
    ),
}


def read_one(name: str, tries: int = 4) -> str:
    out = f"{DIR}/_read-{name}.json"
    if os.path.exists(out) and os.path.getsize(out) > 200:
        try:
            with open(out, encoding="utf-8") as f:
                d = json.load(f)
            c = d.get("choices", [{}])[0].get("message", {}).get("content")
            if c:
                print(f"[{name}] cache présent")
                return c
        except Exception:
            pass
    prompt = PROMPTS[name]
    img = f"{DIR}/{name}.png"
    for i in range(tries):
        r = subprocess.run(
            ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out],
            capture_output=True, text=True, timeout=300,
        )
        if r.returncode == 0 and os.path.exists(out):
            try:
                with open(out, encoding="utf-8") as f:
                    d = json.load(f)
                c = d.get("choices", [{}])[0].get("message", {}).get("content") or json.dumps(d, ensure_ascii=False)
                return c
            except Exception:
                pass
        wait = 20 * (i + 1)
        print(f"[{name}] tentative {i + 1} échouée, attente {wait}s — {r.stderr[:200]}", flush=True)
        time.sleep(wait)
    raise SystemExit(f"ÉCHEC lectures {name}")


if __name__ == "__main__":
    names = sys.argv[1:] or list(PROMPTS)
    for n in names:
        print(f"===== {n} =====", flush=True)
        print(read_one(n)[:400], flush=True)
