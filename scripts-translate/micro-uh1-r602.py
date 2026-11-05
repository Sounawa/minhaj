#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R602 — recadrages serrés (mots ambigus) + feuilles de contrôle."""
import os
import fitz
from PIL import Image

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r602"
os.makedirs(OUT, exist_ok=True)

# nom -> (page, fx0, fy0, fx1, fy1, dpi)
S = [
    # p122 : يشمل/يشتمل — ligne entière
    ("f-p122-yachmal",   122, 0.30, 0.235, 0.99, 0.290, 1200),
    # p122 : انتلاف/ائتلاف — début de ligne
    ("f-p122-ittilaf",   122, 0.45, 0.395, 0.99, 0.455, 1200),
    # p122 : دفع معرّة التصحيف + citation البيقوني (2 lignes)
    ("f-p122-bayquni",   122, 0.03, 0.610, 0.99, 0.720, 900),
    # p123 : trio حبان/حيان/جيان
    ("f-p123-trio",      123, 0.25, 0.145, 0.99, 0.210, 1200),
    # p123 : ينضبط لثقته
    ("f-p123-thiqata",   123, 0.28, 0.205, 0.99, 0.260, 1200),
    # p123 : التعصيم/التعميم (mot)
    ("f-p123-tasim",     123, 0.55, 0.245, 0.90, 0.300, 2400),
    # p123 : كله مـ… (mot)
    ("f-p123-kullahu",   123, 0.30, 0.285, 0.75, 0.345, 2400),
    # p124 : فن جليل يققعهل به — début de la citation
    ("f-p124-fann",      124, 0.40, 0.320, 0.99, 0.385, 2400),
    # p124 : مصنفات … وأكملها الإكمال
    ("f-p124-musannafat",124, 0.03, 0.400, 0.60, 0.470, 2400),
    # p124 : وأتمه الفنك
    ("f-p124-funak",     124, 0.03, 0.455, 0.55, 0.525, 2400),
]

doc = fitz.open(PDF)
groups = {}
for name, pno, fx0, fy0, fx1, fy1, dpi in S:
    page = doc[pno - 1]
    r = page.rect
    clip = fitz.Rect(r.width * fx0, r.height * fy0, r.width * fx1, r.height * fy1)
    png = f"{OUT}/{name}.png"
    page.get_pixmap(dpi=dpi, clip=clip).save(png)
    groups.setdefault(pno, []).append(png)
    print(png, os.path.getsize(png))

for pno, parts in groups.items():
    ims = [Image.open(p) for p in parts]
    W = max(im.width for im in ims)
    PAD = 30
    H = sum(im.height for im in ims) + PAD * (len(ims) + 1)
    sheet = Image.new("RGB", (W + 2 * PAD, H), "white")
    y = PAD
    for im in ims:
        sheet.paste(im, (PAD, y))
        y += im.height + PAD
    sp = f"{OUT}/fix-sheet-p{pno}.png"
    sheet.save(sp)
    print(sp, sheet.size)
