#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — composite final 1200 dpi pour les 6 formes imprimées restées ambiguës."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"

ZONES = [
    (146, 1200, 44, 56),   # tamhīd fin (قاية أنفسهم وأهله من النار + question)
    (147, 1200, 10, 18),   # glosses 3-4 (غلاظة/شداد)
    (152, 1200, 4, 12),    # glosse يخزي
    (153, 1200, 26, 31),   # فرائض fin (مهما قضي/قصى)
    (153, 1200, 66, 71),   # بواعث : تعظيم القائم/القادر
    (154, 1200, 16, 20),   # نور كالنخلة/كالنشأة/كالخلة
]

pdf = fitz.open(PDF)
imgs = []
for page_no, dpi, top, bottom in ZONES:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    png = f"/tmp/z106f-{page_no}-{top}.png"
    pg.get_pixmap(dpi=dpi, clip=clip).save(png)
    imgs.append(Image.open(png))
W = max(i.width for i in imgs)
H = sum(i.height for i in imgs) + 20 * (len(imgs) - 1)
canvas = Image.new("RGB", (W, H), (255, 250, 250))
y = 0
for i in imgs:
    canvas.paste(i, (0, y))
    y += i.height + 20
canvas.save(os.path.join(OUT, "fix-C-r106.png"))
print("fix-C-r106.png", canvas.size)
pdf.close()
