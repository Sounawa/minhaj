# -*- coding: utf-8 -*-
"""Minhāj — Crops ciblés R673 (leçon 406, p.120-123) pour adjudication fine
des citations coraniques, numéros et isnād ambigus. Sortie tr-tmp/qa-crops-r673/."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r673"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

JOBS = [
    (120, 600, 0.04, 0.48, 0.96, 0.92, "z-p120-bas"),
    (121, 600, 0.04, 0.02, 0.96, 0.34, "z-p121-haut"),
    (121, 600, 0.04, 0.30, 0.96, 0.66, "z-p121-mil"),
    (121, 600, 0.04, 0.62, 0.96, 0.97, "z-p121-bas"),
    (122, 600, 0.04, 0.02, 0.96, 0.36, "z-p122-haut"),
    (122, 600, 0.22, 0.28, 0.96, 0.62, "z-p122-mil"),
    (122, 600, 0.04, 0.56, 0.96, 0.97, "z-p122-bas"),
    (123, 600, 0.04, 0.02, 0.96, 0.42, "z-p123-haut"),
    (123, 600, 0.04, 0.38, 0.96, 0.90, "z-p123-bas"),
]
for page_no, dpi, x0, y0, x1, y1, name in JOBS:
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
    out = os.path.join(OUT, f"{name}.png")
    pix.save(out)
    print(f"OK {out} — {pix.width}x{pix.height}")
