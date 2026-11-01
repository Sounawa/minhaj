#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R95 — rendus zoomés du manuel tafsir-2es pour relecture visuelle :
pages 86-97 (leçons 12 = pdf-mut23h33-567 Fāṭir 38-40, et 13 = pdf-mut23h33-568 Fāṭir 41-44)."""
import fitz

PDF = "/tmp/tafsir2es-manual.pdf"
doc = fitz.open(PDF)
for p in range(86, 98):
    pix = doc[p - 1].get_pixmap(dpi=220)
    out = f"/tmp/r95-p{p}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
doc.close()
