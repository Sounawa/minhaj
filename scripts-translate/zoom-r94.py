#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R94 — rendus zoomés des zones douteuses du manuel tafsir-2es
pour relecture visuelle : p74-78 (leçon 10) et p84-85 (leçon 11)."""
import fitz

PDF = "/tmp/tafsir2es-manual.pdf"
doc = fitz.open(PDF)
for p in (74, 75, 76, 77, 78, 84, 85):
    pix = doc[p - 1].get_pixmap(dpi=220)
    out = f"/tmp/r94-p{p}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
doc.close()
