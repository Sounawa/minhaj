#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R108 — Composites 450 dpi demi-pages p167-169 (فهرس الأعلام, leçon 621).

Rend chaque page en 450 dpi, la coupe en deux moitiés verticales (haut/bas) et
écrit 6 PNG (une demi-page par fichier) pour lecture visuelle (Read) : le
indice des figures est en petit corps, les demi-pages conservent la
résolution utile au tranchement des noms propres.
"""
import os
import sys

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r108"
PAGES = [167, 168, 169]
SPLIT = 0.52  # coupe légèrement sous la moitié pour ne pas trancher une ligne

os.makedirs(OUT, exist_ok=True)
pdf = fitz.open(PDF)

for p in PAGES:
    pix = pdf[p - 1].get_pixmap(dpi=450)
    png = f"{OUT}/full450-p{p}.png"
    pix.save(png)
    img = Image.open(png)
    w, h = img.size
    cut = int(h * SPLIT)
    img.crop((0, 0, w, cut)).save(f"{OUT}/half-{p}-haut.png", optimize=True)
    img.crop((0, cut, w, h)).save(f"{OUT}/half-{p}-bas.png", optimize=True)
    os.remove(png)
    print(f"p{p} : {w}x{h} -> haut {w}x{cut}, bas {w}x{h-cut}", file=sys.stderr)

pdf.close()
print("zoom-r108 terminé : 6 demi-pages 450 dpi")
