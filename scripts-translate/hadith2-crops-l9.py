#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Preuve image leçon 9 hadith-2es (slot pdf-10, p.67-72).
Crops fitz : pages entières 160 dpi (contexte) + zones serrées 400-600 dpi
pour trancher numéros Muwaṭṭa (mécanique inversion R535-R542), isnāds,
matns, āya d'ouverture, biographies Abū Ayyūb/Abū Hurayra, glossaire,
rapport Ibn ʿUmar, āya du changement de qibla, hadiths du Musnad Aḥmad,
التوسع + الإعداد القبلي (méthode R538/R541/R542). Sortie : tr-tmp/qa-crops-r543/"""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r543"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


for p in range(67, 73):
    pg = doc[p - 1]
    pix = pg.get_pixmap(matrix=fitz.Matrix(160 / 72, 160 / 72))
    pix.save(f"{OUT}/p{p}-full.png")
    print(f"p{p}-full: {pix.width}x{pix.height}")

crop(67, 0.05, 0.03, 0.95, 0.50, 400, "p67-objectifs-intro-aya")
crop(67, 0.05, 0.44, 0.95, 0.98, 450, "p67-hadith1-isnad")
crop(68, 0.05, 0.02, 0.95, 0.28, 500, "p68-hadith1-matn-num")
crop(68, 0.05, 0.24, 0.95, 0.62, 450, "p68-hadith3-said")
crop(68, 0.05, 0.55, 0.95, 1.00, 450, "p68-hadith4-rawda")
crop(69, 0.05, 0.02, 0.95, 0.26, 500, "p69-bio-hurayra-dates")
crop(69, 0.05, 0.22, 0.95, 0.62, 500, "p69-glossaire-karais")
crop(70, 0.05, 0.02, 0.95, 0.34, 450, "p70-ibnumar-report")
crop(70, 0.05, 0.30, 0.95, 0.68, 450, "p70-basaq-kama")
crop(70, 0.05, 0.62, 0.95, 1.00, 450, "p70-tahwil-isnad")
crop(71, 0.05, 0.02, 0.95, 0.38, 450, "p71-aya-tahwil")
crop(71, 0.05, 0.30, 0.95, 0.68, 450, "p71-fadl-muwatta-ahmad")
crop(71, 0.05, 0.60, 0.95, 1.00, 450, "p71-taqwim")
crop(72, 0.05, 0.02, 0.95, 0.50, 450, "p72-istinass-hadiths")
crop(72, 0.05, 0.42, 0.95, 1.00, 450, "p72-maqasid-idad")
