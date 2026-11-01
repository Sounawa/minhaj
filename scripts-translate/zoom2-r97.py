#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R97 — zooms de précision round 2 (brackets internes, hadith, nombres)."""
import os

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 2 إعدادي.pdf"
OUT = "/tmp/r97"
os.makedirs(OUT, exist_ok=True)

JOBS = [
    (100, 700, 46, 68),   # parallèle + bracket bleu
    (102, 600, 14, 34),   # [الروم: 8] + exemple زيد
    (102, 600, 50, 98),   # citations + brackets + questions
    (103, 600, 6, 26),    # expressions التحضير leçon 15
    (109, 700, 28, 64),   # hadith zone haute précision
    (104, 600, 16, 40),   # آياتها ثمان وعشرون
    (105, 600, 10, 60),   # bracket [الحديد: 1-4] + الشرح
    (110, 600, 20, 40),   # expressions التحضير leçon 16
]

pdf = fitz.open(PDF)
for page_no, dpi, top, bottom in JOBS:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    name = f"p{page_no}-z2-{top}-{bottom}-{dpi}.png"
    pix.save(os.path.join(OUT, name))
    print(f"{name}: {pix.width}x{pix.height}")
pdf.close()
