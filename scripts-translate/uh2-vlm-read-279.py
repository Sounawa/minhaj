# -*- coding: utf-8 -*-
"""Minhāj — Lectures VLM pleine page R659 (slot pdf-mut23h2u-279, leçon 25
أنشطة تطبيقية, p.129-130). Mécanique uh2-vlm-read-278.py (R658) : couche texte
recoupée par rendus 300 dpi (tr-tmp/qa-crops-r659-uh2/), chaque lecture =
cache tr-tmp/qa-crops-r659-uh2/_r659-read-<name>.json — toute récusation de la
couche texte est documentée (nom d'image, ce qui a été lu), jamais devinée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r659-uh2"

PROMPTS = {
    "r659-p129-full": (
        "Full Arabic schoolbook page (300 dpi), lesson 25 opening (practical activities lesson). "
        "Transcribe ALL Arabic lines EXACTLY, right-to-left, in reading order, from the top: "
        "1) any green banner + medallion at the very top — read the lesson number digit-by-digit "
        "(expected ٢٥) and transcribe the printed title exactly (expected الدرس 25 : أنشطة تطبيقية); "
        "if there is NO banner, say so explicitly; "
        "2) the rubric أهداف الأنشطة with EVERY numbered objective — the text layer suggests four "
        "items each beginning with أن (item 1 mentions النظريات المفاهيم السابقة, item 2 mentions "
        "العمل التطبيقي البحث في النظريات والمهارات, item 3 mentions ضبط الغاية وأهمية الحديث "
        "والتطبيقات في مجال, item 4 mentions دراسة النظريات العملية على أحاديث) — transcribe EACH "
        "objective completely and exactly as printed, from أن to its final word; "
        "3) the rubric أقرأ with its full paragraph (the text layer suggests: تكتسب جملاً وتستبطن ... "
        "الحديث بالمعلقات المرتبطة النظريات الجوانب من الكثير فصل فيما عرفت ... معارف مرتبطة "
        "بالمعلقات ... التوصيل على الحديث طالب تعني والتي ...) — transcribe the WHOLE paragraph "
        "exactly, word by word; "
        "4) the rubric أطبق with its full paragraph (the text layer suggests: التوصيل على الحديث "
        "طالب تعني والتي الحديث ... les objectifs de l'étude ... التمييز بين التقييم الخاص ببحثه "
        "الضعيف والصحيح ... بشر من هذا غرض ومهم ... ضروري على الاقتباس فيها ومراعي المقدس ... "
        "التوسع بالتطبيقات العانية مرتجلة مفتوح التجربة ... وأن العلم له التجربة مفتوحة) — "
        "transcribe the WHOLE paragraph exactly to its final word; "
        "5) any page footer number, read digit-by-digit. Mark [؟] where unclear. "
        "Short French notes at the end."
    ),
    "r659-p130-full": (
        "Full Arabic schoolbook page (300 dpi), continuation of lesson 25. Transcribe ALL Arabic "
        "lines EXACTLY, right-to-left, in reading order, from the top: "
        "1) the rubric تخريج المطلوب: الحديث — transcribe exactly; "
        "2) THE COMPLETE TRANSMISSION CHAIN (isnaad) printed below it — the text layer suggests "
        "حدثنا أبو هشام الرفاعي ... حدثنا ابن يحيى بن ... ابن ... عن ... الزهري ... عن ... "
        "دباب? أبي ... الرحمن بن عبد ... عن طلحة بن عبيد الله «لكل نبي رفيق» قال النبي ... "
        "[هنع] ... الله رضي نافع بن ... ثمانية بن ثمانية في المناقب باب أبواب الترمذي سنن - "
        "يعني عثمان — transcribe the isnaad WORD BY WORD exactly as printed, line by line, "
        "including the blue bracketed source reference (which recueil, which chapter, and any "
        "hadith number — read digits DIGIT BY DIGIT); mark [؟] where unclear; "
        "3) the numbered items that follow (the text layer suggests items numbered 2,3,4,5,6: "
        "3 - as the hadith is (بك أقبك؟) بالحروف وفظها؟ بلسانه / 2 - أبحث عن ... المأذون فيه / "
        "4 - أسند الدرس هذا الحديث إلى مبتدئ؟ المسند أصلي ... رواته - وخريجي الحديث أسند "
        "بتبشير أقوم إلي / 5 - ولك درجة وأبين وجدت ( ) إن وشواه الحديث طرق أدرس ... درجة أصلي "
        "الحديث / 6 - وشواهده طرق عن البحث تم بعدد أصلي الحديث) — transcribe EVERY item "
        "completely and exactly, with its real number, from first word to last; pay special "
        "attention to the EXACT wording of item 4 (what the student does: أسند? استخرج? الحديث "
        "ورواته) and item 6 (ما تم بعد إحصاء الطرق؟) ; "
        "4) the section that starts at the BOTTOM of the page (the text layer suggests "
        "التطبيق والدعم ورشات أنشطة / والاوراش أنشطة لإنجاز عمل فريق تكونيون? مع أتواعن على "
        "أصدقائي and الأعداد القبلية) — transcribe these bottom lines exactly; state "
        "whether this bottom section has its own heading/banner separated from the takhrij "
        "exercise above (i.e., is it the opening of a NEW section/workshops?). "
        "5) any page footer number, read digit-by-digit. Mark [؟] where unclear. "
        "Short French notes at the end."
    ),
}

IMG = {
    "r659-p129-full": "p129-full-300.png",
    "r659-p130-full": "p130-full-300.png",
}


def run(name):
    out = os.path.join(DIR, f"_r659-read-{name}.json")
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
