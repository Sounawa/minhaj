# -*- coding: utf-8 -*-
"""Minhāj — Preuve image leçon 15 hadith-2es (slot pdf-16, R553).
Composites 300 dpi (6 bandes/page) p.104-112 — bornes + structure + numéros.
Sortie : tr-tmp/qa-crops-r553/."""
import os
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r553"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

def page_mat(page_no, dpi=300, n_bands=6):
    pg = doc[page_no - 1]
    pix = pg.get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    W, H = img.size
    band_h = H // n_bands
    comp = Image.new("RGB", (W, band_h * n_bands + 8 * (n_bands - 1)), "white")
    d = ImageDraw.Draw(comp)
    y = 0
    for i in range(n_bands):
        band = img.crop((0, i * band_h, W, min((i + 1) * band_h, H)))
        comp.paste(band, (0, y))
        if y:
            d.line([(0, y - 4), (W, y - 4)], fill="red", width=3)
        d.text((6, y + 4), f"p{page_no} b{i + 1}/{n_bands}", fill="red")
        y += band_h + 8
    path = f"{OUT}/p{page_no:02d}-comp.png"
    comp.save(path)
    print(path, comp.size)

for p in range(104, 113):
    page_mat(p)
print("DONE")
