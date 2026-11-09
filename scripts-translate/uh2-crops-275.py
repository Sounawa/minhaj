# -*- coding: utf-8 -*-
# R656 — crops 300 dpi des bandes de la leçon 21 uh2 (p.107-114) + sondages bornes
# Doctrine R651-R655 : toute récusation par preuve image, jamais deviné.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r656"
import os
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, page 595x765, rendu 300 dpi
ZONES = [
    (107, 30, 260, "p107-banner-objectifs"),
    (107, 260, 500, "p107-tamhid-matn"),
    (107, 500, 760, "p107-gloses"),
    (108, 40, 430, "p108-def-anatypes"),
    (108, 430, 760, "p108-mudraj-isnad-awwal"),
    (109, 40, 260, "p109-thalith-exemple"),
    (109, 260, 530, "p109-salat-haja"),
    (109, 530, 760, "p109-thalith-rabi"),
    (110, 40, 300, "p110-iklil-mudraj-matan"),
    (110, 300, 560, "p110-awwaluhu-khatib"),
    (110, 560, 760, "p110-khatib-quote"),
    (111, 40, 300, "p111-athnaihi-daraqutni"),
    (111, 300, 560, "p111-akhiruhu-abu-khaythama"),
    (111, 560, 760, "p111-asbab-idraj"),
    (112, 40, 280, "p112-istihala-tirmidhi"),
    (112, 280, 500, "p112-suyuti-maqlub-def"),
    (112, 500, 760, "p112-maqlub-anwa"),
    (113, 40, 280, "p113-maqlub-sund-mithal"),
    (113, 280, 560, "p113-maqlub-matan-bukhari"),
    (113, 560, 760, "p113-fath-mughith-tarikh"),
    (114, 40, 300, "p114-hukm-ali-darmi"),
    (114, 300, 500, "p114-istithmar"),
    (114, 500, 760, "p114-taqwim-idad"),
    (115, 30, 260, "p115-banner-l22"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, y1)
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
