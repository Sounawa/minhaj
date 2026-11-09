# -*- coding: utf-8 -*-
# R656 — zooms 900 dpi des zones résiduelles leçon 21 uh2 (p.107-114)
# Doctrine : toute récusation par preuve image, jamais deviné.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r656"
import os
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    (108, 690, 760, "z1-p108-bukhari-kitab"),
    (110, 90, 145, "z2-p110-abu-qatan"),
    (111, 205, 255, "z3-p111-ruwaya-mufassala"),
    (111, 375, 500, "z4-p111-ibn-masud-nada"),
    (113, 40, 130, "z5-p113-fath-bab-sadaqa"),
    (113, 285, 385, "z6-p113-tarikh-baghdad-line"),
    (114, 325, 445, "z7-p114-alfiyya-verse"),
    (112, 175, 220, "z8-p112-suyuti-word"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, y1)
    pix = page.get_pixmap(dpi=900, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
