#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R97 — rendus haute résolution pour la relecture visuelle des pages 98-110
(manuel tafsir-2es : leçon 14 = Fāṭir 44-45 [569], leçon 15 = Ḥadīd 1-4 [570])."""
import os
import sys

import fitz

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 2 إعدادي.pdf"
OUT = "/tmp/r97"
os.makedirs(OUT, exist_ok=True)

# (page 1-based, dpi, mode, top%, bottom%) — mode full → page entière
JOBS = [
    (99, 300, "full", 0, 100),   # bracket leçon 14 + الشرح + versets
    (100, 300, "full", 0, 100),  # Ibn Kathīr + parallèle + bracket
    (102, 300, "full", 0, 100),  # Rāzī istithmār
    (104, 300, "full", 0, 100),  # objectifs + intro Ḥadīd + v.1
    (105, 300, "full", 0, 100),  # versets + bracket + الشرح + extraction
    (106, 300, "full", 0, 100),  # commentaire v.2-v.3 + brackets
    (108, 300, "full", 0, 100),  # v.4 + Rāzī + maqāṣid
    (109, 300, "full", 0, 100),  # évaluation + hadith istithmār
    # crops ciblés
    (99, 500, "crop", 20, 52),   # bracket [سورة فاطر: 4X-4X] + الشرح
    (103, 450, "crop", 0, 30),   # التحضير leçon 15 : expressions
    (108, 450, "crop", 55, 95),  # bracket Rāzī + maqāṣid
    (109, 500, "crop", 25, 75),  # hadith al-Faḍarī
    (110, 450, "crop", 0, 42),   # التحضير leçon 16 : expressions
]

pdf = fitz.open(PDF)
for page_no, dpi, mode, top, bottom in JOBS:
    pg = pdf[page_no - 1]
    r = pg.rect
    if mode == "full":
        clip = fitz.Rect(r.x0, r.y0, r.x1, r.y1)
        name = f"p{page_no}-full-{dpi}.png"
    else:
        clip = fitz.Rect(r.x0, r.y0 + r.height * top / 100, r.x1, r.y0 + r.height * bottom / 100)
        name = f"p{page_no}-crop{top}-{bottom}-{dpi}.png"
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    path = os.path.join(OUT, name)
    pix.save(path)
    print(f"{name}: {pix.width}x{pix.height}")
pdf.close()
