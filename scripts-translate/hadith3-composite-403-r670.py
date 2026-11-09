# -*- coding: utf-8 -*-
"""Minhāj — Composites de lecture leçon 14 hadith-3es (R670, slot pdf-mut23h2x-403,
أحكام مزدلفة, p.97-103). Mécanique économie R103 (hadith3-composite-401-r666.py) :
bandes pertinentes 600 dpi empilées en UNE image PIL par zone pivot, réduites à
55 % pour lecture directe par l'agent (Read tool). Sortie : tr-tmp/qa-crops-r670/."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r670"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
SCALE = 0.55
X0, X1 = 0.04, 0.96

JOBS = [
    ("r670-a-p97-intro-hadith", 97, [(0.38, 0.57), (0.57, 0.93)]),
    ("r670-b-p98-hadith2-tarjama", 98, [(0.05, 0.46), (0.55, 0.73)]),
    ("r670-c-p99-glosses-box", 99, [(0.05, 0.36)]),
    ("r670-d-p99-comment-athar", 99, [(0.50, 0.92)]),
    ("r670-e-p100-wuquf", 100, [(0.05, 0.31)]),
    ("r670-f-p100-salat", 100, [(0.31, 0.60)]),
    ("r670-g-p101-taabbudi-adhan", 101, [(0.10, 0.40)]),
    ("r670-h-p101-nuzul", 101, [(0.41, 0.62)]),
    ("r670-i-p101-rukhsa-athars", 101, [(0.62, 0.95)]),
    ("r670-j-p102-taqwim", 102, [(0.10, 0.40)]),
    ("r670-k-p102-malik-aya1", 102, [(0.44, 0.68)]),
    ("r670-l-p102-aya2-tafsir", 102, [(0.68, 0.92)]),
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
