# -*- coding: utf-8 -*-
"""Minhāj — Rendu images annexe 29 hadith-2es (slot pdf-30, R574).
300 dpi in extenso (pages 198-203) dans tr-tmp/r574-pages/."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUTDIR = "/home/z/my-project/tr-tmp/r574-pages"
import os
os.makedirs(OUTDIR, exist_ok=True)

doc = fitz.open(PDF)
for p in range(197, 203):  # pages 198-203
    pix = doc[p].get_pixmap(dpi=300)
    fp = f"{OUTDIR}/p{p + 1:03d}-300dpi.png"
    pix.save(fp)
    print(fp, pix.width, "x", pix.height)
print("OK")
