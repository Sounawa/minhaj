# -*- coding: utf-8 -*-
"""Minhāj — crops ciblés R669 (slot pdf-mut23h2x-402, leçon 13 أعمال يوم عرفة).
Patrons : hadith3-adjud-402-r667.py (render_bands) + hadith3-crops-402-r657.py.
Zones restées ambiguës après couches OCR + lectures pleine page R657 :
  a) p.90 chaîne du tamhīd [1271] (زياد بن أبي زياد)      — zone 0.13-0.34
  b) p.91 notice Salīm b. ʿAbdallāh (citation de Mālik)   — zone 0.55-0.98
  c) p.92 الشرح gloses (3 ou 4 items ? 4e item ?)         — zone 0.02-0.30
  d) p.94 bas ثالثا + [1190] + commentaire Mālik + [1191] — zone 0.60-1.00
  e) p.95 rubrique exploitation + hadith [1270]           — zone 0.52-0.78
Sortie : tr-tmp/qa-crops-r669/ (600 dpi, échelle 0.85 pour lecture VLM dense).
"""
import fitz
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r669"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
SCALE = 0.85
X0, X1 = 0.04, 0.97

JOBS = [
    ("r669-a-p90-tamhid-chain",  90, [(0.13, 0.34)]),
    ("r669-b-p91-salim-notice",  91, [(0.55, 0.98)]),
    ("r669-c-p92-sharh-glosses", 92, [(0.02, 0.30)]),
    ("r669-d-p94-salat-jumua",   94, [(0.60, 1.00)]),
    ("r669-e-p95-istithmar",     95, [(0.52, 0.78)]),
]

for name, page_no, bands in JOBS:
    pg = doc[page_no - 1]
    pieces, W = [], 0
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
