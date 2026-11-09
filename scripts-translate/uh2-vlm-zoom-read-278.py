# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM zooms 900 dpi R658 (uh2-278) : trancher les conflits
de couches. Cache tr-tmp/qa-crops-r658/_r658-read-z900-<name>.json."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r658"

PROMPTS = {
    "z900-p125-matn": (
        "High-resolution (900 dpi) Arabic textbook excerpt showing a boxed quote (المتن). Transcribe the ENTIRE "
        "boxed text EXACTLY, letter by letter, with all diacritics you can see. Expected candidate wording: "
        "قال الحافظ ابن حجر رحمه الله: «ولا يجوز تعمد ترك اللفظ والمرادف إلا لعالم بما يحيل المعاني؛ فإن حفي "
        "المعنى حاج إلى شرح الغريب وما المشكل». CAREFULLY verify each contested word: (a) after تعمد — is it "
        "ترك اللفظ والمرادف or التغيير والمرادف or تغيير اللفظ؟ (b) after لعالم — بما يحيل أو به يحيل؟ (c) "
        "then فإن حفي المعنى حاج أو حيف أو احتاج؟ (d) the final words: وما المشكل أو وبيان المشكل أو وما "
        "أشكل؟ Report each choice explicitly. Mark [؟] where print is unclear. Short French notes."
    ),
    "z900-p125-sharh": (
        "High-resolution (900 dpi) Arabic textbook excerpt (panneau الشرح + استخلاص المضامين, page 125). "
        "Transcribe EXACTLY: (1) the الشرح gloss box: الغريب: البعيد عن وطنه، وغريب الحديث: ... (transcribe "
        "the rest letter by letter, expected ما غَمُضَ وخفي معناه or ما ضع معناها؟) then المشكل: المقصود به "
        "في المتن: ما التبس وأشكل معناه بسبب تعارض ظاهر؟ — verify each word; (2) the استخلاص المضامين "
        "numbered items: item 1 أستخلص من المتن حكم اختصار الحديث؟ and item 2 أستخرج من النص حكم رواية "
        "الحديث... — transcribe item 2 COMPLETELY to its last word (expected tail لتغير العالم بالمعنى؟ أو "
        "غير ذلك؟), mark [؟] where unclear. Short French notes."
    ),
    "z900-p126-istithna-src": (
        "High-resolution (900 dpi) Arabic textbook excerpt showing the tail of a paragraph and a blue bracketed "
        "source reference. Transcribe EXACTLY the bracketed line: expected [صحيح البخاري، كتاب البيوع، باب بيع "
        "الذهب بالذهب] OR [صحيح مسلم، كتاب البيوع، باب بيع الذهب بالذهب]. READ THE COLLECTION NAME LETTER BY "
        "LETTER: does it read البخاري or مسلم؟ Also transcribe the words immediately before the bracket "
        "(expected إلا سَواءً بسَواء) and after it (فإنه لا يجوز حذفه). Mark [؟] where unclear. Short French notes."
    ),
    "z900-p127-bottom": (
        "High-resolution (900 dpi) Arabic textbook excerpt (bottom of page 127). Transcribe EVERY line EXACTLY "
        "letter by letter: (1) the paragraph beginning وذلك أنه إن لم يكن — continue to its end; (2) the "
        "repeated quote of الحافظ ابن حجر inside it — transcribe exactly (candidate wordings: ولا يجوز تعمد "
        "ترك اللفظ والمرادف إلا لعالم بما يحيل المعاني OR ولا يجوز تعمد تغيير اللفظ بالنقص والزيادة إلا لعالم "
        "بما يحيل المعاني — decide by image); (3) the line وما سلف من الأقوال هو خلاف في الجواز وعدمه والأولى "
        "إيراد الحديث بألفاظه دون التصرف فيه — verify; (4) the phrase about the practice of scholars والذي جرى "
        "به عمل أهل العلم أن ينقلوا الرواية كما وصلت ولا يغيروها في كتبهم; (5) the quote ونقل الحافظ ابن حجر "
        "عن القاضي عياض رحمهما الله قوله ينبغي سد باب الرواية بالمعنى لئلا يتسلط من لا يحسن ممن يظن أنه يحسن — "
        "verify each word; (6) the clause وقد عقد القاضي عياض في كتابه الإلماع إلى معرفة أصول الرواية وتقييد "
        "السماع بابا عنوانه باب تحري الرواية والمجيء باللفظ ومن رخص للعلماء في المعنى ومن منع — verify the "
        "BOOK TITLE letter by letter: الإلماع or الإملاء؟; (7) the clause وخلص فيه إلى أن المستحب المجيء بنفس "
        "اللفظ ما استطيع with its blue reference — read the page number DIGIT BY DIGIT (expected 179); also "
        "check the earlier clause containing مفتاح أو مفوت للتبرك بألفاظ صاحب الشريعة ومفتح لأبواب الشك — "
        "transcribe it exactly. Mark [؟] where unclear. Short French notes."
    ),
    "z900-p128-idad": (
        "High-resolution (900 dpi) Arabic textbook excerpt (bottom of page 128, rubric الاعداد القبلي). "
        "Transcribe EXACTLY: (1) the lead line يراعى في إنجاز درس الأنشطة التطبيقية ما يلي؟ — verify; (2) "
        "EVERY numbered item with its printed number read DIGIT BY DIGIT — expected: 1. تنجز حصة الأنشطة "
        "التطبيقية داخل المؤسسة / 2. يقسم المتعلمون إلى مجموعات تنجز كل مجموعة عملها تحت إشراف الأستاذ(ة) / "
        "4. تعرض نتائج الأعمال في الفصل قصد مناقشتها — state explicitly: how many items, and what numbers are "
        "printed (is the third really 4 or 3?). Mark [؟] where unclear. Short French notes."
    ),
}

IMG = {
    "z900-p125-matn": "z900-p125-matn.png",
    "z900-p125-sharh": "z900-p125-sharh.png",
    "z900-p126-istithna-src": "z900-p126-istithna-src.png",
    "z900-p127-bottom": "z900-p127-bottom.png",
    "z900-p128-idad": "z900-p128-idad.png",
}


def run(name):
    out = os.path.join(DIR, f"_r658-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(DIR, IMG[name])
    prompt = PROMPTS[name]
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:200]}")
        return
    try:
        d = json.load(open(out, encoding="utf-8"))
        body = d["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"ERR parse {name}: {e}")
        return
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
