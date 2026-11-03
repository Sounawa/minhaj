# -*- coding: utf-8 -*-
"""Minhāj — R555 bis : bandes pour les renvois répétés (hits indexés).
p83 «569» hits[1] et hits[2] ; p84 «572» hits[1]."""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r555"
doc = fitz.open(PDF)

TASKS = [(83, "569", 1), (83, "569", 2), (84, "572", 1)]
strips = []
for pno, tok, idx in TASKS:
    page = doc[pno - 1]
    hits = page.search_for(tok)
    r = hits[idx]
    clip = fitz.Rect(max(0, r.x0 - 15), max(0, r.y0 - 7),
                     min(page.rect.width, r.x1 + 120), min(page.rect.height, r.y1 + 7))
    pm = page.get_pixmap(matrix=fitz.Matrix(900 / 72, 900 / 72), clip=clip)
    pm.save(f"{OUT}/_s.png")
    strips.append(Image.open(f"{OUT}/_s.png"))
w = max(i.width for i in strips)
h = sum(i.height + 8 for i in strips)
comp = Image.new("RGB", (w, h), "white")
y = 0
for i in strips:
    comp.paste(i, (0, y))
    y += i.height + 8
comp.save(f"{OUT}/composite-numbers-bis.png")
print(f"composite-numbers-bis.png : {w}x{h}")
import os
os.remove(f"{OUT}/_s.png")
