#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R602 — aperçus 150 dpi p.121-124 (leçon 25 المؤتلف والمختلف, pdf-mut23h2r-136).
Chaîne R578→R601. Sortie : tr-tmp/qa-crops-r602/ov-p<N>.png"""
import os
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r602"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
for n in (121, 122, 123, 124):
    doc[n - 1].get_pixmap(dpi=150).save(f"{OUT}/ov-p{n}.png")
    print(f"ov-p{n}.png", os.path.getsize(f"{OUT}/ov-p{n}.png"))
