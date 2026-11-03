#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Preuve image leçon 10 hadith-2es (slot pdf-11, p.73-79).
Crops fitz : pages entières 160 dpi (contexte) + zones serrées 400-600 dpi
pour trancher numéros Muwaṭṭa (mécanique inversion R535-R544), isnāds,
matns, āyāt intro (al-Ḥiǧr/al-Wāqiʿa), bio ʿAmr b. Ḥazm, glossaire,
liste des onze sujūdāt (ʿAbd ar-Razzāq), روايتان وقت السجود,
الاستئناس (āya + hadith ʿĀʾiša), التقويم + الإعداد القبلي
(méthode R538/R541/R542/R544). Sortie : tr-tmp/qa-crops-pdf11/"""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-pdf11"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


for p in range(73, 80):
    pg = doc[p - 1]
    pix = pg.get_pixmap(matrix=fitz.Matrix(160 / 72, 160 / 72))
    pix.save(f"{OUT}/p{p}-full.png")
    print(f"p{p}-full: {pix.width}x{pix.height}")

crop(73, 0.05, 0.03, 0.95, 0.42, 400, "p73-objectifs-intro")
crop(73, 0.05, 0.30, 0.95, 0.60, 500, "p73-aya-hijr")
crop(73, 0.05, 0.52, 0.95, 1.00, 500, "p73-hadith1-num")
crop(74, 0.05, 0.02, 0.95, 0.30, 500, "p74-hadith2-umar")
crop(74, 0.05, 0.24, 0.95, 0.52, 500, "p74-hadith3-malik")
crop(74, 0.05, 0.44, 0.95, 0.74, 500, "p74-bio-amr-hazm")
crop(74, 0.05, 0.66, 0.95, 1.00, 500, "p74-glossaire-extraction")
crop(75, 0.05, 0.02, 0.95, 0.34, 450, "p75-analyse-mushaf")
crop(75, 0.05, 0.28, 0.95, 0.58, 500, "p75-aya-waqia")
crop(75, 0.05, 0.50, 0.95, 0.78, 450, "p75-exceptions")
crop(75, 0.05, 0.68, 0.95, 1.00, 500, "p75-lecture-ibnabbas")
crop(76, 0.05, 0.02, 0.95, 0.30, 500, "p76-ibnabbas-suite")
crop(76, 0.05, 0.24, 0.95, 0.62, 450, "p76-hukm-sajdah")
crop(76, 0.05, 0.56, 0.95, 1.00, 500, "p76-adad-mawadi")
crop(77, 0.05, 0.02, 0.95, 0.28, 500, "p77-liste-sujud")
crop(77, 0.05, 0.22, 0.95, 0.72, 450, "p77-waqt-ruwayatan")
crop(77, 0.05, 0.66, 0.95, 1.00, 500, "p77-taqwim")
crop(78, 0.05, 0.02, 0.95, 0.52, 500, "p78-istinass-hadith")
crop(78, 0.05, 0.44, 0.95, 1.00, 500, "p78-questions-idad")
