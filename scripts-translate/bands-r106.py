#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — trois bandes fines 1100 dpi pour lecture visuelle finale (mots clés)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"

BANDS = [
    ("band-glosses-147.png", 147, 15, 31),
    ("band-maqam-153.png", 153, 65.5, 70.5),
    ("band-nur-154.png", 154, 21.0, 26.5),
]

pdf = fitz.open(PDF)
for name, page_no, top, bottom in BANDS:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    pg.get_pixmap(dpi=1100, clip=clip).save(os.path.join(OUT, name))
    print(name)
pdf.close()
