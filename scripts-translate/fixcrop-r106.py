#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — composites ciblés 900 dpi pour trancher les formes imprimées restées
ambiguës après les composites A/B et re-crops (11 zones, 2 images)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r106"
os.makedirs(OUT, exist_ok=True)

FIXES = {
    "fix-A-r106.png": [
        (146, 900, 26, 36),   # tamhīd fin + question (قاية أنفسهم وأهلهم)
        (147, 900, 3, 17),    # glosses 3-4 (غلاظة/شداد + تعتذروا)
        (150, 900, 28, 46),   # الإعداد : expressions ×3 (توبة نصوحا - ... - يغفر)
        (152, 900, 2, 15),    # glosses p152 (يخزي + la suite)
        (153, 900, 22, 32),   # فرائض fin (مهما قضي/قصى)
    ],
    "fix-B-r106.png": [
        (153, 900, 30, 40),   # آداب ×3 (الحسنات لمحو)
        (153, 900, 62, 74),   # بواعث ×7 fin (الحبيب/الجبيب, القائم/القادر)
        (154, 900, 0, 7),     # glosse head للذين تابوا
        (154, 900, 13, 21),   # نور كالنخلة/كال...
        (154, 900, 30, 42),   # يقولون (ضمير عائد)
    ],
}

pdf = fitz.open(PDF)
for name, jobs in FIXES.items():
    imgs = []
    for page_no, dpi, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/fix106-{page_no}-{top}.png"
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
