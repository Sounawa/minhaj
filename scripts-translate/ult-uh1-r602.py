#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R602 — recadrages ultimes (mots 3600 dpi + citation en 2 moitiés)."""
import os
import fitz
from PIL import Image

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r602"
os.makedirs(OUT, exist_ok=True)

S = [
    ("u-p122-yachmal",  122, 0.50, 0.230, 0.78, 0.290, 3600),
    ("u-p122-ittilaf",  122, 0.55, 0.390, 0.85, 0.460, 3600),
    ("u-p122-daf-bayq", 122, 0.03, 0.710, 0.99, 0.870, 900),
    ("u-p123-tasim",    123, 0.55, 0.240, 0.90, 0.310, 3600),
    ("u-p123-mutqal",   123, 0.28, 0.280, 0.70, 0.355, 3600),
    ("u-p123-thiqata",  123, 0.28, 0.200, 0.70, 0.270, 2400),
    ("u-p124-istith-r", 124, 0.46, 0.315, 0.995, 0.480, 1200),
    ("u-p124-istith-l", 124, 0.015, 0.315, 0.53, 0.480, 1200),
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
    sp = f"{OUT}/ult-sheet-p{pno}.png"
    sheet.save(sp)
    print(sp, sheet.size)
