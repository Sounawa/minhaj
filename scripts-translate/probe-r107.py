#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R107 — Sondes de bandeaux p157-172 (bornage 619 = v.9-10, 620 = v.11-12).

Rend chaque page du manuel tafsir-3es en 400 dpi, recadre le bandeau supérieur
(haut ~22 % de la page) et empile 3 bandeaux par composite PNG pour lecture
visuelle (Read). Les bandeaux portent « الدرس : <n> — سورة التحريم «الآية(s) : X »
et permettent de borner 619/620 exactement.
"""
import os
import sys
import fitz
from PIL import Image

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
OUT = "/home/z/my-project/tr-tmp/probe-r107"
PAGES = list(range(157, 173))
PER = 3  # bandeaux par composite

os.makedirs(OUT, exist_ok=True)
pdf = fitz.open(PDF)

bands = []
for p in PAGES:
    pix = pdf[p - 1].get_pixmap(dpi=400)
    png = f"{OUT}/full-p{p}.png"
    pix.save(png)
    img = Image.open(png)
    w, h = img.size
    crop = img.crop((0, 0, w, int(h * 0.22)))
    bands.append((p, crop))
    os.remove(png)
    print(f"bande p{p} : {crop.size}", file=sys.stderr)

# empilement 3 par 3, largeur max unifiée
W = max(c.size[0] for _, c in bands)
for gi in range(0, len(bands), PER):
    grp = bands[gi:gi + PER]
    H = sum(c.size[1] for _, c in grp) + 30 * (len(grp) - 1)
    comp = Image.new("L", (W, H), 255)
    y = 0
    for p, c in grp:
        comp.paste(c, (0, y))
        y += c.size[1] + 30
    out = f"{OUT}/bands-{grp[0][0]}-{grp[-1][0]}.png"
    comp.save(out, optimize=True)
    print(f"composite : {out} ({comp.size})")
pdf.close()
