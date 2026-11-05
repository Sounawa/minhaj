#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R601 — overview 150 dpi p.117-120 (leçon 24 ulum-hadith-tanawi-1, المتفق والمفترق).
Bornes fixées au double sondage : p.117 bannière أهداف الدرس 24 ; p.121 = bannière cours 25.
Sortie : tr-tmp/qa-crops-r601/ov-p<N>.png
"""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r601"

import os
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
for n in (117, 118, 119, 120):
    doc[n - 1].get_pixmap(dpi=150).save(f"{OUT}/ov-p{n}.png")
    print("OK", n)
