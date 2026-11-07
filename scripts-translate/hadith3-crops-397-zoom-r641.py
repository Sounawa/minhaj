# -*- coding: utf-8 -*-
"""Minhāj — Recadrages ciblés R641-bis (leçon 8 hadith-3es 397, tick 11:07).
Trois zones à trancher en haute résolution avant rédaction :
  z1  p.59  queue du texte 1025 (« وقد نهى الله عن... » + « والأمر عندنا »)
  z2  p.59  liste des cinq animaux du hadith 1028 (ordre + « جناح »)
  z3  p.64  « شق المحرم دُمَّله / كلفه » (conflit couches vs image)
Sortie : tr-tmp/qa-crops-r641/*.png"""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r641"

CROPS = [
    (59, 0.385, 0.475, 900, "z1-p59-1025fin", None, None),
    (59, 0.465, 0.575, 900, "z2-p59-1028liste", None, None),
    (64, 0.535, 0.645, 900, "z3-p64-shaq-dummala", None, None),
]

doc = fitz.open(PDF)
for pg, f0, f1, dpi, name, x0, x1 in CROPS:
    page = doc[pg - 1]
    r = page.rect
    xa = x0 if x0 is not None else 0
    xb = x1 if x1 is not None else r.width
    clip = fitz.Rect(xa, r.height * f0, xb, r.height * f1)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    p = f"{OUT}/{name}.png"
    pix.save(p)
    print(f"OK {p} {pix.width}x{pix.height}")
