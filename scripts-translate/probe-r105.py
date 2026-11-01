#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R105 — sondes de bandeaux pour borner 615/616 (tafsir-3es).
2 composites : p135/p141/p143/p144 et p145/p146/p147/p148 (hauts de page, 400 dpi)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r105"
os.makedirs(OUT, exist_ok=True)

SONDES = {
    "probe-A-r105.png": [(135, 400, 0, 17), (141, 400, 0, 17), (143, 400, 0, 17), (144, 400, 0, 17)],
    "probe-B-r105.png": [(145, 400, 0, 17), (146, 400, 0, 17), (147, 400, 0, 17), (148, 400, 0, 17)],
}

pdf = fitz.open(PDF)
for name, jobs in SONDES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/probe105-{page_no}.png"
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
