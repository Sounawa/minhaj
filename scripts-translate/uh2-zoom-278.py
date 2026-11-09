# -*- coding: utf-8 -*-
# R658 — zooms 900 dpi des zones conflictuelles de la leçon 24 uh2 (p.125-128)
# (1) matn Ibn Ḥaǧar p.125 : « يجوز ترك اللفظ » (couche) vs « يحوز التغيير » (VLM)
# (2) source استثناء p.126 : « البخاري » (VLM) vs « مسلم » (couche)
# (3) bas p.127 : citation matn répétée + مفتاح/مفوت + الإلماع/الإملاء
# (4) p.125 panneau الشرح + استخلاص item 2
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r658"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    (125, 340, 520, "z900-p125-matn"),
    (125, 520, 765, "z900-p125-sharh"),
    (126, 430, 560, "z900-p126-istithna-src"),
    (127, 560, 765, "z900-p127-bottom"),
    (128, 620, 765, "z900-p128-idad"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, min(y1, page.rect.height))
    pix = page.get_pixmap(dpi=900, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
