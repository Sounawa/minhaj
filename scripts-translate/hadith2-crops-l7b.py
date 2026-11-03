#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — crops ultimes R541 : zones serrées 400-600 dpi."""
import os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r541"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


crop(53, 0.05, 0.32, 0.95, 0.54, 600, "c1-p53-renvoi600")
crop(53, 0.05, 0.75, 0.95, 0.99, 600, "c2-p53-matn1fin600")
crop(54, 0.05, 0.02, 0.95, 0.13, 600, "c3-p54-matn1tail600")
crop(54, 0.05, 0.24, 0.95, 0.44, 600, "c4-p54-matn2deb600")
crop(55, 0.05, 0.12, 0.95, 0.42, 400, "c5-p55-defs400")
crop(55, 0.05, 0.66, 0.95, 0.93, 400, "c6-p55-aya101-400")
crop(57, 0.05, 0.02, 0.95, 0.55, 400, "c7-p57-haut400")
crop(57, 0.05, 0.55, 0.95, 0.80, 400, "c8-p57-khutba400")
crop(58, 0.05, 0.02, 0.95, 0.45, 400, "c9-p58-hikma-taqwim400")
crop(58, 0.05, 0.50, 0.95, 0.88, 400, "c10-p58-istitmar400")
doc.close()
print("OK")
