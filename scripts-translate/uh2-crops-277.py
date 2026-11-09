# -*- coding: utf-8 -*-
# R658 — crops 300 dpi des bandes de la leçon 23 uh2 (p.120-125)
# Doctrine R651-R657 : toute récusation par preuve image, jamais deviné.
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r658"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, page 595x765, rendu 300 dpi
ZONES = [
    (120, 30, 260, "p120-banner-objectifs"),
    (120, 260, 520, "p120-tamhid-matn"),
    (120, 520, 760, "p120-fahm"),
    (121, 30, 250, "p121-def-musahhaf"),
    (121, 250, 440, "p121-ahamiyya-aqsam"),
    (121, 440, 760, "p121-isnad-tasahhif-matan"),
    (122, 30, 240, "p122-basr-soli"),
    (122, 240, 430, "p122-sam-asma"),
    (122, 430, 760, "p122-maani-thaniya-lugha"),
    (123, 30, 260, "p123-muharraf-jabir"),
    (123, 260, 450, "p123-farq"),
    (123, 450, 760, "p123-hukm-ahtadi-taqwim"),
    (124, 30, 320, "p124-istithmar"),
    (124, 320, 760, "p124-istikhlas-idad"),
    (125, 30, 330, "p125-banner-l24"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, y1)
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
