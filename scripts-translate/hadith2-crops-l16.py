# -*- coding: utf-8 -*-
"""R560 — Images de preuve leçon 16 (pdf-17, p.112-117).
Pages entières 300 dpi + micro-crops numéros Muwaṭṭaʾ 1200 dpi (méthode R553/R559)."""
import fitz
import os

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r560"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0, y0, x1, y1, dpi, name):
    pg = doc[page_no - 1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


# pages entières 300 dpi
for p in range(112, 118):
    crop(p, 0, 0, 640, 810, 300, f"full-p{p}")

print("--- micro-crops (seront ajustés après lecture des pages entières) ---")
