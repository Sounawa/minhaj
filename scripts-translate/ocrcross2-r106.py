#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R106 — deuxième passe : OCR 600 dpi zones corrigées + micro-crops 2400 dpi
des mots exacts (تعظيم المقام/القائم, كالنخلة/كال..., مهما قضي, يخزي, غلاظ)."""
import os
import subprocess

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
TESSDIR = "/home/z/my-project/scripts-translate/tessdata"

OCR_ZONES = [
    ("p147-glosses-2", 147, 14, 32),
    ("p152-glosses-2", 152, 22, 36),
    ("p153-faraid-2", 153, 34, 46),
    ("p154-nur-2", 154, 20, 30),
]

pdf = fitz.open(PDF)
os.makedirs("/tmp/ocr106", exist_ok=True)
for name, page_no, top, bottom in OCR_ZONES:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    png = f"/tmp/ocr106/{name}.png"
    pg.get_pixmap(dpi=600, clip=clip).save(png)
    out = subprocess.run(
        ["tesseract", png, "stdout", "-l", "ara", "--tessdata-dir", TESSDIR, "--psm", "6"],
        capture_output=True, text=True)
    print(f"===== OCR {name} (p{page_no} {top}-{bottom}%) =====")
    print(out.stdout.strip()[:1400])
    print()

# Micro-crops 2400 dpi (bandes fines horizontales autour des mots clés)
MICRO = [
    ("micro-maqam", 153, 66.4, 69.8),    # وتعظيم المقام/القائم
    ("micro-kalla", 154, 21.5, 25.0),    # كالنخلة/كالنشأة/كالخلة
    ("micro-qudiya", 153, 36.0, 40.0),   # مهما قضي/قصى
    ("micro-yakhzi", 152, 26.0, 33.0),   # glosse يخزي
    ("micro-ghilaz", 147, 17.0, 27.0),   # glosses غلاظ/شداد/تعتذروا
]
for name, page_no, top, bottom in MICRO:
    pg = pdf[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
    png = f"/tmp/ocr106/{name}.png"
    pg.get_pixmap(dpi=2400, clip=clip).save(png)
    out = subprocess.run(
        ["tesseract", png, "stdout", "-l", "ara", "--tessdata-dir", TESSDIR, "--psm", "6"],
        capture_output=True, text=True)
    print(f"===== MICRO {name} (p{page_no} {top}-{bottom}%) 2400dpi =====")
    print(out.stdout.strip()[:800])
    print()
pdf.close()
