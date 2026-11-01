#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — micro-crops 2400 dpi sur les mots exacts restés ambigus (5 bandes fines)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"

ZONES = [
    (147, 2400, 13, 22),   # glosses (غلاظة/شداد/تعتذروا)
    (152, 2400, 8, 20),    # glosses يخزي
    (153, 2400, 28, 36),   # فرائض fin + آداب début
    (153, 2400, 62, 70),   # بواعث ligne entière
    (154, 2400, 14, 20),   # نور كالنخلة/كال...
]

pdf = fitz.open(PDF)
imgs = []
for page_no, dpi, top, bottom in ZONES:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    png = f"/tmp/z106m-{page_no}-{top}.png"
    pg.get_pixmap(dpi=dpi, clip=clip).save(png)
    imgs.append(Image.open(png))
W = max(i.width for i in imgs)
H = sum(i.height for i in imgs) + 20 * (len(imgs) - 1)
canvas = Image.new("RGB", (W, H), (255, 250, 250))
y = 0
for i in imgs:
    canvas.paste(i, (0, y))
    y += i.height + 20
canvas.save(os.path.join(OUT, "fix-D-r106.png"))
print("fix-D-r106.png", canvas.size)
pdf.close()
