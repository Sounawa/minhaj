#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R101 — zooms de précision pour les leçons 607 (p85-91) + 608 (p92-98).
Cible : blocs de versets ornés, variantes coraniques, noms de lecteurs,
citations d'Ibn ʿĀšūr / al-Qurṭubī, sources de hadiths."""
import os

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/zoom-r101"
os.makedirs(OUT, exist_ok=True)

# (page, dpi, top%, bottom%)
JOBS = [
    (85, 400, 38, 66),    # 607 bloc versets v.1 + الإعداد?
    (86, 500, 30, 62),    # 607 citation ornée «فاتقوا الله» + نداء
    (87, 600, 6, 40),     # 607 variantes قراءة عثمان/ابن عباس/أبي/ابن عمر
    (89, 500, 10, 46),    # 607 «إن أتين بفاحشة» + قراءة أبي بن كعب + 5 أقوال
    (90, 500, 44, 84),    # 607 citation ابن عاشور + [التحرير والتنوير: 728]
    (91, 500, 6, 44),     # 607 fin citation ابن عاشور
    (92, 400, 34, 72),    # 608 bloc versets v.2-3
    (93, 500, 10, 42),    # 608 termes (أوشكت العدة...)
    (94, 500, 22, 78),    # 608 «لئلا يميل» + [النساء 134/135] + ابن الفرس
    (95, 500, 30, 92),    # 608 عوف بن مالك + hadith قرأها فقال
    (96, 500, 6, 52),     # 608 [سنن ابن ماجه] + الرزق نوعان + [هود: 6]
    (97, 500, 44, 82),    # 608 citation القرطبي + [18/158]
]

pdf = fitz.open(PDF)
for page_no, dpi, top, bottom in JOBS:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    name = f"p{page_no}-{dpi}-{top}-{bottom}.png"
    pix.save(os.path.join(OUT, name))
    print(f"{name}: {pix.width}x{pix.height}")
pdf.close()
