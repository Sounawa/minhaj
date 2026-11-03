#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crops 600 dpi ciblés p.77 (leçon 10 hadith-2es / pdf-11) :
bande A = ligne 1 de la liste des sūras (suite de الأعراف) ;
bande B = « ووجه هذه الرواية… » (lexie floue فُضِعَت/فُمِعَت)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-pdf11"
doc = fitz.open(PDF)
pg = doc[76]  # page 77 (index 0-based)
r = pg.rect

def band(y0, y1, name):
    clip = fitz.Rect(0.02 * r.width, y0 * r.height, 0.98 * r.width, y1 * r.height)
    pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")

band(0.085, 0.175, "p77-liste-zoom600")
band(0.45, 0.60, "p77-wajh-zoom600")
