# -*- coding: utf-8 -*-
"""Minhāj — Rond d'adjudication 3 (R673-c) leçon 406 hadith-3es : 5 zones en
conflit entre couches, tranchées sur image 900 dpi (preuve image, jamais devinées).
  a) p.116 questions de l'iʿdād (terme 1 de Q1)
  b) p.117 bloc calligraphique āya du tamhīd
  c) p.120 queue de page (phrase « وكل شيء… »)
  d) p.121 bloc « والشعائر… عروة… يا بني »
  e) p.121 citation « لقوله تعالى… » + renvoi سورة/آية
Sortie : tr-tmp/qa-crops-r673/ (crops z2-*.png + lectures _r673c-read-*.json)."""
import fitz
import json
import os
import subprocess

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r673"
os.makedirs(OUT, exist_ok=True)

CROPS = [
    (116, 0.04, 0.12, 0.96, 0.42, "z2-p116-questions"),
    (117, 0.04, 0.45, 0.96, 0.92, "z2-p117-aya"),
    (120, 0.04, 0.80, 0.96, 0.995, "z2-p120-queue"),
    (121, 0.04, 0.22, 0.96, 0.56, "z2-p121-shaair"),
    (121, 0.04, 0.54, 0.96, 0.82, "z2-p121-islam"),
]

PROMPTS = {
    "z2-p116-questions": (
        "Zoom 900 dpi, the preparation page (الإعداد القبلي) of an Arabic schoolbook. "
        "Transcribe EXACTLY right-to-left: the rubric أحفظ أحاديث الدرس المقبل وأجيب عن الآتي, "
        "then EVERY numbered question letter by letter. For question 1 (أشرح: ...), transcribe "
        "the FIRST term after أشرح letter by letter with its diacritics — candidates: النُّثْفِيَّة? "
        "التَّنْفِيَة? النُّثْرِيَّة? النَّحْر? التَّقْدِيَة? — resolve from the image, do NOT guess. "
        "Then the 2nd and 3rd terms (التقليد? الإشعار?) and question 2 (أبحث عن معنى المستيسر من "
        "الهدي?). Mark illegible as [؟]. Short French notes."
    ),
    "z2-p117-aya": (
        "Zoom 900 dpi, the Quranic calligraphic block of an Arabic schoolbook page (tamhīd of "
        "lesson أحكام الهدي 1). Transcribe the WHOLE block letter by letter in order: which verse "
        "passages exactly? Candidates seen: (a) وَلِلَّهِ عَلَى النَّاسِ حِجُّ الْبَيْتِ مَنِ "
        "اسْتَطَاعَ إِلَيْهِ سَبِيلًا وَمَنْ كَفَرَ فَإِنَّ اللَّهَ غَنِيٌّ عَنِ الْعَالَمِينَ; "
        "(b) قُلْ إِنَّ صَلَاتِي وَنُسُكِي وَمَحْيَايَ وَمَمَاتِي لِلَّهِ رَبِّ الْعَالَمِينَ + لَا "
        "شَرِيكَ لَهُ وَبِذَلِكَ أُمِرْتُ وَأَنَا أَوَّلُ الْمُسْلِمِينَ; (c) passages about الْبُدْنِ "
        "/ شَعَائِرِ اللَّهِ / وَلَكِنْ لِيَظْهَرُوا / فَمِنْ. State EXACTLY which of these appear in "
        "the block and in which order, and transcribe any words I did not list. Then the blue "
        "reference bracket [سورة الحج الآيتان: 34-35] — read every digit. Mark illegible as [؟]. "
        "Short French notes."
    ),
    "z2-p120-queue": (
        "Zoom 900 dpi, the LAST lines at the bottom of an Arabic schoolbook page (lesson أحكام "
        "الهدي). Transcribe EXACTLY the final sentence of the page, letter by letter: after « وكيف "
        "يشك أحد في ذلك؟ » comes « وكل شيء ... » — transcribe ALL remaining words exactly: is it "
        "« وكل شيء يجبر أن يحكم فيه ببديعٍ »? « وكل شيء لا يبلغ أن يحكم فيه بغير ... » (then WHAT "
        "word follows بغير?)? Resolve from the image, do NOT guess. Mark illegible as [؟]. Short "
        "French notes."
    ),
    "z2-p121-shaair": (
        "Zoom 900 dpi, middle band of an Arabic schoolbook page (lesson أحكام الهدي). Transcribe "
        "EXACTLY right-to-left the whole commentary block: 1) والشعائر: الهدي والأنعام المشعرة — "
        "then the following words (تعظيمها وتسمينها والمغالاة بها? وتعظيمها تسليمها? ...) letter by "
        "letter; 2) the NAME quoted (عروة? عمر? زيد?) and HOW the sentence introduces the quote "
        "(وكان يقول? وقال?); 3) the quoted words يا بني ... COMPLETE letter by letter (expected "
        "something like يا بني إنّ لا يهدِينَ أن يهدِيَهُ اللهُ فليكن من كريمه أكْرَمُ اختير له — "
        "resolve every word from the image); 4) the blue bracket [الموطأ رقم: NNN] DIGIT BY DIGIT "
        "(1120?). Mark illegible as [؟]. Short French notes."
    ),
    "z2-p121-islam": (
        "Zoom 900 dpi, lower-middle band of an Arabic schoolbook page (lesson أحكام الهدي). "
        "Transcribe EXACTLY: 1) the sentence امتثالا لقوله تعالى: «...» — the quoted verse TEXT "
        "letter by letter (candidates: لِتُكَبِّرُوا اللهَ عَلَى مَا هَدَاكُمْ / وَلْيَتَكَبِّرُوا "
        "اللهَ عَلَى مَا هَدَاكُمْ / other); 2) the blue bracket — SURAH NAME letter by letter "
        "(البقرة? الحج?) and verse number DIGIT BY DIGIT (184? 37? other?); 3) the green rubric "
        "ثالثا: ... and sub-line 1- ركوب الهدي if visible; 4) the quote عن أبي هريرة ... اركبها "
        "ويلك — transcribe exactly, and whether a blue bracket follows it. Mark illegible as [؟]. "
        "Short French notes."
    ),
}


def crop():
    doc = fitz.open(PDF)
    for page_no, x0, y0, x1, y1, name in CROPS:
        pg = doc[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        pix = pg.get_pixmap(matrix=fitz.Matrix(900 / 72, 900 / 72), clip=clip, alpha=False)
        out = os.path.join(OUT, f"{name}.png")
        pix.save(out)
        print(f"CROP {out} — {pix.width}x{pix.height}")


def read(name):
    out = os.path.join(OUT, f"_r673c-read-{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    img = os.path.join(OUT, f"{name}.png")
    cmd = ["z-ai", "vision", "-p", PROMPTS[name], "-i", img, "-o", out]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if res.returncode != 0:
        print(f"ERR {name}: {res.stderr[:200]}")
        return
    d = json.load(open(out, encoding="utf-8"))
    body = d["choices"][0]["message"]["content"]
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["crop"]:
        crop()
    else:
        crop()
        for _n, _x0, _y0, _x1, _y1, _r in CROPS:
            read(_r)
