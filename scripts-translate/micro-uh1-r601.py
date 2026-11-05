#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R601-bis — micro-crops 2400 dpi pour mots litigieux :
1. bayt p.117 : «تَكَرَّنَا/ذَكَرْنَا» (x 0.22-0.40, y 0.70-0.80)
2. quote p.120 : «فيتَّفَق/فيُحسَب» (x 0.30-0.65, y 0.325-0.365)
3. p.118 : ligne «حبان/حيان/جيان» (x 0.06-0.94, y 0.655-0.745) 1200 dpi
Sortie : tr-tmp/qa-crops-r601/m-<X>.png
"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r601"

JOBS = [
    ("m1-bayt-word", 117, 0.70, 0.80, 0.22, 0.42, 2400),
    ("m2-quote-word", 120, 0.325, 0.365, 0.28, 0.66, 2400),
    ("m3-hbn-line", 118, 0.655, 0.745, 0.06, 0.94, 1200),
]

doc = fitz.open(PDF)
os.makedirs(OUT, exist_ok=True)
for name, page, y0, y1, x0, x1, dpi in JOBS:
    pg = doc[page - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pm.save(f"{OUT}/{name}.png")
    print("OK", name, pm.width, "x", pm.height)
