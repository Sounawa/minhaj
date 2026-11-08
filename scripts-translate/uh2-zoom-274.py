# -*- coding: utf-8 -*-
# R655 — zooms 600 dpi NEUTRES (sans candidats amorcés) des zones fragiles de la leçon 20 uh2
# Adjudication par preuve image des références numériques et des mots suspects.
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r655"
doc = fitz.open(PDF)

ZONES = [
    (103, 250, 545, 148, 174, "z1-lisan-ref"),      # ref لسان العرب (471/11 couche)
    (103, 0, 545, 176, 202, "z2-definition"),       # définition Ibn aṣ-Ṣalāḥ + ref ص
    (103, 0, 545, 244, 298, "z3-mardud"),           # مرذول/مردود + بالمعلول
    (103, 300, 545, 316, 346, "z4-qari-p103"),      # ref القاري (549/945 couche)
    (103, 0, 545, 370, 422, "z5-adtila"),           # clause finale شرطان (اضطلاعا ?)
    (104, 300, 545, 120, 146, "z6-qari-p104"),      # ref القاري (164/461 couche)
    (104, 0, 545, 586, 616, "z7-ans"),              # حديث أنس المصرح به ?
    (105, 250, 545, 166, 194, "z8-muqaddima-92"),   # ref مقدمة ابن الصلاح (29/92 couche)
    (105, 0, 545, 428, 528, "z9-taqwim"),           # التقويم q1 (illisible couche) + q2
    (105, 180, 545, 654, 684, "z10-muqaddima-93"),  # ref مقدمة ابن الصلاح (39/93 couche)
]
for p, x0, x1, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(dpi=600, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
