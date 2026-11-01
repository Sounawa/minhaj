#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R107 — micro-crops 2400 dpi pour trancher 6 zones ambiguës (méthode R106).
Empilés en 2 composites (économie de lecture)."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r107"
os.makedirs(OUT, exist_ok=True)

CROPS = [
    ("mc1-p158-abdin.png",   158, 18.0, 30.0),  # glosse تحت عبدين : عصمتها/عصمتهما
    ("mc2-p159-ladina.png",  159, 26.0, 40.0),  # « منها ما نصه صفحة اللدنة » ?
    ("mc3-p160-kana.png",    160, 7.0, 22.0),   # أي : كانا/كانتا تحت عصمة نبيين كريمين
]

CROPS2 = [
    ("mc4-p162-i3dad.png",   162, 28.0, 46.0),  # expressions الإعداد (calligraphie)
    ("mc5-p163-question.png", 163, 34.0, 50.0), # question finale du تمهيد
    ("mc6-p164-dua.png",     164, 70.0, 90.0),  # فدعت بهذا الدعاء + أي : + دعاء
]

pdf = fitz.open(PDF)
for name, jobs in (("comp-micro-r107-1.png", CROPS), ("comp-micro-r107-2.png", CROPS2)):
    imgs = []
    for _n, page_no, top, bottom in jobs:
        pg = pdf[page_no - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        png = f"/tmp/m107-{page_no}-{top}.png"
        pg.get_pixmap(dpi=2400, clip=clip).save(png)
        im = Image.open(png)
        if im.width > 1500:
            nh = int(im.height * 1500 / im.width)
            im = im.resize((1500, nh), Image.LANCZOS)
        imgs.append(im)
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
