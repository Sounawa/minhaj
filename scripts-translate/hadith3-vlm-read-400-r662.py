# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM ciblées R662 (slot pdf-mut23h2x-400, leçon 11 أحكام الطواف (2)).
Complète le corpus R660 (21 lectures) sur quatre zones restées ambiguës :
gloses p.80, dialogue Şafiyya + citation ʿUrwa p.81, jugement de Mâlik + hadith
d'Ibn ʿUmar p.82 (haut), items 2-3 p.82 (bas : verbe final + doublon de réf).
Patron hadith3-vlm-read-400-r660.py ; SDK isolé /tmp/vlm-r660 HORS arbre git
(patron incident wiper R651). Crops 600 dpi dans tr-tmp/qa-crops-r660/r662-*.
Cache _r662-read-<name>.json — toute récusation documentée, jamais devinée."""
import json
import os
import subprocess
import sys

import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
DIR = "/home/z/my-project/tr-tmp/qa-crops-r660"
READ = "/tmp/vlm-r660/read.mjs"

CROPS = [
    # (page, dpi, x0, y0, x1, y1, nom)
    (80, 600, 0.03, 0.14, 0.97, 0.33, "r662-p80-glosses"),
    (81, 600, 0.03, 0.08, 0.97, 0.46, "r662-p81-safiyya-urwa"),
    (82, 600, 0.03, 0.02, 0.97, 0.46, "r662-p82-top"),
    (82, 600, 0.03, 0.44, 0.97, 0.97, "r662-p82-bottom"),
]

PROMPTS = {
    "r662-p80-glosses": (
        "600 dpi crop of the GLOSSARY band at the top of an Arabic schoolbook page (rubric الشرح, "
        "glosses of lesson 11 on the ṭawāf). Transcribe EVERY gloss entry EXACTLY, in order: the "
        "glossed word, then a dash, then its printed definition. Expected entries: لا يَصَدَّرَنَّ ، "
        "مُحَلِّها ، مُرَاهِقًا. Read each definition letter by letter; distinguish carefully ع/غ، ظ/ض، ف/ق. "
        "For مُرَاهِقًا note the pronunciation remark in parentheses (بكسر الها وفتحها?) exactly. "
        "Mark anything illegible as [؟]. Short French notes at the end."
    ),
    "r662-p81-safiyya-urwa": (
        "600 dpi crop of the upper band of an Arabic schoolbook page (fiqh section 2 of lesson 11: "
        "الرجوع لطواف الوداع بعد مغادرة البيت). Transcribe EXACTLY, in order: (1) the section title; "
        "(2) the ruling line (الرجوع لطواف الوداع... مستحب مندوب إليه عند مالك إن لم تلحق الراجع مشقة); "
        "(3) the hadith of ʿĀʾiša on Şafiyya bint Ḥuyayy — transcribe the WHOLE dialogue; give the "
        "EXACT reply word(s) after فقيل: letter by letter (candidates: إنها قد قاضت / إنها قد طافت / "
        "something else — read what is printed, do not guess); then فقال: «فلا إذا»; (4) the blue "
        "[الموطأ رقم: NNNN] digit by digit; (5) the words بعد ذلك (فلم يلزمها بدم ولا أمرها بالمقام) "
        "and ويدل للاستحباب أيضا; (6) the quote of ʿUrwa starting «من ...» — give its FIRST word "
        "letter by letter (candidates: قضى / أفاض / قاضى) and transcribe the whole quote word by "
        "word; (7) its blue [الموطأ رقم: NNNN] digit by digit; (8) the green rubric ثانيا: طواف "
        "القدوم للمراهق. Mark [؟] if uncertain. Short French notes at the end."
    ),
    "r662-p82-top": (
        "600 dpi crop of the top of an Arabic schoolbook page (continuation of ثالثا: طواف الحائض, "
        "lesson 11). Transcribe EXACTLY, in order: (1) the opening words of the page (the reason of "
        "the prohibition, وعلة النهي عند الجمهور...) with the exact LIST of persons concerned "
        "(candidates: الحائض والنفساء والمحدث / الحائض والجنب والمحدث — read what is printed); "
        "(2) the attribution words BEFORE قال مالك: «لا يطوف أحد بالبيت ولا بين الصفا والمروة إلا وهو "
        "طاهر» — is there a phrase like ما روي عن ابن عمر before or after? transcribe letter by "
        "letter the exact connector; (3) the blue [الموطأ رقم: NNNN] of that quote digit by digit; "
        "(4) the bold hadith of the woman consulting Ibn ʿUmar («جاءته امرأة تستفتيه فقالت: إني أريد "
        "أن أطوف بالبيت...») — transcribe it fully, COUNT the repeated clauses about هرقت الدماء "
        "and transcribe each; (5) the words of Ibn ʿUmar's answer — letter by letter the instruction "
        "between فاغتسلي and طوفي (candidates: ثم استثفري / ثم استنفري / بثوب?); (6) its blue "
        "[الموطأ رقم: NNNN] digit by digit. Mark [؟] if uncertain. Short French notes at the end."
    ),
    "r662-p82-bottom": (
        "600 dpi crop of the lower band of an Arabic schoolbook page (lesson 11, fiqh of طواف "
        "الحائض). Transcribe EXACTLY, in order: (1) the commentary lines (they mention a fatwa "
        "أفتاها, a variant wording of جماعة من رواة الموطأ possibly «أن عجوزا استفتته», the "
        "الاستحاضة, the principle إنما يحل الطواف لمن تحل له الصلاة, and the gloss of فاغتسلي as "
        "nadb for the ṭawāf not for the ḥayḍ) — transcribe as printed, letter by letter where "
        "degraded; (2) the green numbered heading 2 - المتمتعة إذا حاضت وخشيت فوات الحج وأفعال "
        "العمرة, its paragraph, and Mālik's quote (أهلت بالحج وأهديت... طواف واحد) with the blue "
        "[الموطأ رقم: NNNN] digit by digit; (3) the green numbered heading 3 - إذا حاضت المرأة بعد "
        "ركعتي الطواف and Mālik's quote — transcribe it fully and give its FINAL verb letter by "
        "letter (candidates: تفيض / تطوف / تقيم — read what is printed) and its blue [الموطأ رقم: "
        "NNNN] digit by digit; (4) state EXPLICITLY whether the blue numbers of headings 2 and 3 "
        "are identical. Mark [؟] if uncertain. Short French notes at the end."
    ),
}


def make_crops():
    doc = fitz.open(PDF)
    for page_no, dpi, x0, y0, x1, y1, name in CROPS:
        page = doc[page_no - 1]
        r = page.rect
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
        out = os.path.join(DIR, f"{name}.png")
        pix.save(out)
        print(f"CROP {out} — {pix.width}x{pix.height}")


def run(name):
    out = os.path.join(DIR, f"_r662-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, f"{name}.png")
    cmd = ["node", READ, img, PROMPTS[name], out + ".raw"]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=420)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:300]}")
        return
    body = open(out + ".raw", encoding="utf-8").read().strip()
    json.dump({"name": name, "image": img, "body": body}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    os.path.exists(out + ".raw") and os.remove(out + ".raw")
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    if "--crops-only" in sys.argv:
        make_crops()
    else:
        make_crops()
        for n in sys.argv[1:] or list(PROMPTS):
            run(n)
