# -*- coding: utf-8 -*-
# R657 — zooms 900 dpi des zones résiduelles leçon 22 uh2 (p.115-116)
# Doctrine : toute récusation par preuve image, jamais deviné.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r657"
import os
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    (115, 400, 530, "z1-p115-matn-ibdil"),
    (116, 430, 590, "z2-p116-abuhatim-quote"),
    (116, 610, 765, "z3-p116-conditions-ab"),
    (116, 230, 460, "z4-p116-hadith-exemple-fin"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, y1)
    pix = page.get_pixmap(dpi=900, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
