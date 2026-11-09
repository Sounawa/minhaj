# -*- coding: utf-8 -*-
"""Minhāj — Composites de lecture leçon 12 hadith-3es (R666, slot pdf-mut23h2x-401,
أحكام السعي بين الصفا والمروة, p.84-89). Mécanique économie R103 : bandes pertinentes
600 dpi empilées en UNE image PIL par zone pivot, réduites à 55 % pour lecture directe
par l'agent (Read tool, SDK VLM 429 documenté R664). Sortie : tr-tmp/qa-crops-r666/."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r666"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
SCALE = 0.55
X0, X1 = 0.04, 0.96

JOBS = [
    ("a1-p84-banner",  84, [(0.02, 0.36)]),
    ("a2-p84-quote",   84, [(0.36, 0.58), (0.58, 0.82)]),
    ("b1-p85-hadiths", 85, [(0.02, 0.48)]),
    ("b2-p85-gloss",   85, [(0.48, 0.98)]),
    ("c1-p86-extract", 86, [(0.02, 0.50)]),
    ("c2-p86-comment", 86, [(0.50, 0.95)]),
    ("d1-p87-start",   87, [(0.02, 0.22), (0.34, 0.47)]),
    ("d2-p87-dua",     87, [(0.53, 0.90)]),
    ("e1-p88-refs",    88, [(0.12, 0.26), (0.48, 0.64), (0.80, 0.95)]),
    ("f1-p89-taqwim",  89, [(0.02, 0.30), (0.42, 0.78)]),
    ("f2-p89-idad",    89, [(0.78, 0.98)]),
]

for name, page_no, bands in JOBS:
    pg = doc[page_no - 1]
    pieces = []
    W = 0
    for (y0, y1) in bands:
        clip = fitz.Rect(pg.rect.width * X0, pg.rect.height * y0,
                         pg.rect.width * X1, pg.rect.height * y1)
        pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img = img.resize((int(img.width * SCALE), int(img.height * SCALE)), Image.LANCZOS)
        pieces.append(img)
        W = max(W, img.width)
    sep = 24
    H = sum(p.height for p in pieces) + sep * (len(pieces) - 1)
    canvas = Image.new("RGB", (W, H), (220, 220, 220))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y))
        y += p.height + sep
    path = f"{OUT}/{name}.png"
    canvas.save(path)
    print(f"OK {path} — {canvas.width}x{canvas.height}")
