# -*- coding: utf-8 -*-
"""Minhāj — SONDE DE BORNES leçon 13 hadith-3es (R667, slot pdf-mut23h2x-402,
أعمال يوم عرفة). Rends p.89 bas, p.90, p.91, p.96 bas et p.97 haut en bands
verticales 600 dpi réduites ×0.55 (mécanique économie R103) pour lecture
DIRECTE par l'agent multimodal (Read tool — SDK VLM 429 documenté R664,
ne pas l'appeler). Bornes à trancher PAR IMAGE, jamais devinées :
inf = bannière الدرس الثالث عشر (médaillon 13), sup = bannière الدرس
الرابع عشر (médaillon 14) ou fin du bloc. Sortie : tr-tmp/qa-crops-r667/."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r667"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
SCALE = 0.55
X0, X1 = 0.04, 0.96

JOBS = [
    ("probe-p89-lower",  89, [(0.35, 1.00)]),
    ("probe-p90-upper",  90, [(0.00, 0.50)]),
    ("probe-p90-lower",  90, [(0.50, 1.00)]),
    ("probe-p91-upper",  91, [(0.00, 0.50)]),
    ("probe-p96-lower",  96, [(0.45, 1.00)]),
    ("probe-p97-upper",  97, [(0.00, 0.40)]),
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
