#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Preuve image leçon 8 hadith-2es (slot pdf-9, p.60-66).
Crops fitz : pages entières 160 dpi (contexte) + zones serrées 400-600 dpi
pour trancher numéros Muwaṭṭa (mécanique inversion R535-R541), isnāds,
matns, duʿāʾs, Malīk quotes (méthode R538/R541). Sortie : tr-tmp/qa-crops-r542/"""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r542"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


for p in range(60, 67):
    pg = doc[p - 1]
    pix = pg.get_pixmap(matrix=fitz.Matrix(160 / 72, 160 / 72))
    pix.save(f"{OUT}/p{p}-full.png")
    print(f"p{p}-full: {pix.width}x{pix.height}")

crop(60, 0.05, 0.04, 0.95, 0.52, 400, "p60-objectifs-tamhid")
crop(60, 0.05, 0.46, 0.95, 0.92, 450, "p60-matn1-num")
crop(60, 0.05, 0.86, 0.95, 1.00, 450, "p60-matn2-start")
crop(61, 0.05, 0.02, 0.95, 0.30, 450, "p61-malik-quote")
crop(61, 0.05, 0.26, 0.95, 0.62, 450, "p61-matn3-rain")
crop(62, 0.05, 0.55, 0.95, 1.00, 450, "p62-anas-hadith")
crop(63, 0.05, 0.02, 0.95, 0.42, 450, "p63-hukm-malik")
crop(63, 0.05, 0.68, 0.95, 1.00, 450, "p63-khutba-malik")
crop(64, 0.05, 0.02, 0.95, 0.20, 500, "p64-dua-anas")
crop(64, 0.05, 0.84, 0.95, 1.00, 500, "p64-adab4-umar")
crop(65, 0.05, 0.02, 0.95, 0.22, 500, "p65-abbas-dua")
crop(65, 0.05, 0.20, 0.95, 0.34, 500, "p65-taqwim")
crop(65, 0.05, 0.32, 0.95, 0.78, 400, "p65-istithmar")
crop(65, 0.05, 0.72, 0.95, 1.00, 450, "p65-exercice")
crop(66, 0.05, 0.25, 0.95, 0.75, 400, "p66-iqdad")
doc.close()
print("OK r542")
