#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — OCR tesseract haute résolution (600/1200 dpi) sur les zones de mots
ambigus, pour recouper les lectures visuelles 450-900 dpi."""
import os
import subprocess

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
TESS = "/home/z/my-project/scripts-translate/tessdata/ara.traineddata"

ZONES = [
    ("p147-glosses", 147, 12, 24),
    ("p152-glosses", 152, 4, 16),
    ("p152-glosses-bas", 152, 14, 24),
    ("p153-faraid", 153, 26, 38),
    ("p153-bawacith", 153, 62, 72),
    ("p154-nur", 154, 13, 21),
]

pdf = fitz.open(PDF)
os.makedirs("/tmp/ocr106", exist_ok=True)
for name, page_no, top, bottom in ZONES:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    png = f"/tmp/ocr106/{name}.png"
    pg.get_pixmap(dpi=600, clip=clip).save(png)
    out = subprocess.run(
        ["tesseract", png, "stdout", "-l", "ara", "--tessdata-dir",
         "/home/z/my-project/scripts-translate/tessdata", "--psm", "6"],
        capture_output=True, text=True)
    print(f"===== {name} (p{page_no} {top}-{bottom}%) =====")
    print(out.stdout.strip()[:1200])
    print()
pdf.close()
