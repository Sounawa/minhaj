# -*- coding: utf-8 -*-
# R655 — crops 300 dpi des bandes de la leçon 20 uh2 (p.102-106) + bannière leçon 21 (p.107)
# Doctrine R651-R654 : toute récusation par preuve image, jamais deviné.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r655"
import os
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, page 595x765, rendu 300 dpi
ZONES = [
    (102, 20, 250, "p102-banner-objectifs"),
    (102, 250, 495, "p102-tamhid-matn"),
    (102, 495, 690, "p102-gloses"),
    (103, 95, 430, "p103-def-lugha-istilah"),
    (103, 425, 700, "p103-turuq"),
    (104, 40, 150, "p104-ihtilaq"),
    (104, 148, 335, "p104-ahammiya"),
    (104, 335, 700, "p104-mithal"),
    (105, 40, 198, "p105-b-cont"),
    (105, 193, 420, "p105-hukm-ahtadi"),
    (105, 420, 695, "p105-taqwim-istithmar"),
    (106, 40, 200, "p106-idad"),
    (107, 30, 295, "p107-banner-l21"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, y1)
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
