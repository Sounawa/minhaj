#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R603 — aperçus 150 dpi p.125-128 (cartographie de structure par l'image).
Sortie : /tmp/my-project/tr-tmp/qa-crops-r603/ov-pN-150.png
Usage : python3 scripts-translate/crops-uh1-r603.py
"""
import os
import fitz

HOME = "/tmp/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r603"

os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
for n in (125, 126, 127, 128):
    pm = doc[n - 1].get_pixmap(dpi=150)
    p = f"{OUT}/ov-p{n}-150.png"
    pm.save(p)
    print(p, pm.width, "x", pm.height)
