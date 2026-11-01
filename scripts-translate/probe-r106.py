#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — sondes de bandeaux pour borner 617 (v.6-7) et 618 (v.8).
2 composites : p149/p150/p151/p152 et p153/p154/p155/p156 (hauts de page, 400 dpi)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"
os.makedirs(OUT, exist_ok=True)

SONDES = {
    "probe-A-r106.png": [(149, 400, 0, 17), (150, 400, 0, 17), (151, 400, 0, 17), (152, 400, 0, 17)],
    "probe-B-r106.png": [(153, 400, 0, 17), (154, 400, 0, 17), (155, 400, 0, 17), (156, 400, 0, 17)],
}

pdf = fitz.open(PDF)
for name, jobs in SONDES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/probe106-{page_no}.png"
        pg.get_pixmap(dpi=dpi, clip=clip).save(png)
        imgs.append(Image.open(png))
    W = max(i.width for i in imgs)
    H = sum(i.height for i in imgs) + 24 * (len(imgs) - 1)
    canvas = Image.new("RGB", (W, H), (255, 250, 250))
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + 24
    canvas.save(os.path.join(OUT, name))
    print(name, canvas.size)
pdf.close()
