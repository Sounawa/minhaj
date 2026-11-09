# -*- coding: utf-8 -*-
"""Minhāj — Composites de lecture leçon 12 hadith-3es (R666 reprise, slot
pdf-mut23h2x-401, أحكام السعي بين الصفا والمروة, p.84-89). Deux niveaux :
(a) pages entières 84-89 à Matrix 600/72 réduites à 42 % (≈250 dpi effectif,
lecture structure/bornes) ; (b) méga-composite d'adjudication des six chiffres
pivots récusés par l'OCR local (micro-crops 900 dpi existants, étiquettes
latines) ; (c) trois zooms ciblés 55 % (duʿāʾ p.87, āthar p.89, contexte « 28 »
p.88). Sortie : tr-tmp/qa-crops-r666/."""
import os
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r666"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def render(page_no, y0, y1, scale, x0=0.04, x1=0.96):
    pg = doc[page_no - 1]
    clip = fitz.Rect(pg.rect.width * x0, pg.rect.height * y0,
                     pg.rect.width * x1, pg.rect.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    return img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)


# (a) pages entières à 42 %
for p in range(84, 90):
    img = render(p, 0.0, 1.0, 0.42)
    path = f"{OUT}/page-p{p}-r666.png"
    img.save(path)
    print(f"OK {path} — {img.width}x{img.height}")

# (b) méga-composite chiffres pivots récusés (micro-crops 900 dpi existants)
PICKS = [
    ("p86 etiqu 157 (OCR « 7157 »)", "ocr-p86-157.png"),
    ("p87 Muwatta 1091 (OCR « 161091205 »)", "ocr-p87-1091.png"),
    ("p87 Ghafir 60 (OCR « 960 »)", "ocr-p87-60.png"),
    ("p88 Muwatta 1096 (OCR « 61096 »)", "ocr-p88-1096.png"),
    ("p88 Muwatta 28 (OCR « 4 »)", "ocr-p88-28.png"),
    ("p89 Muwatta 1097 (OCR « »)", "ocr-p89-1097.png"),
]
pieces = []
W = 0
for label, fn in PICKS:
    img = Image.open(f"{OUT}/{fn}")
    if img.width > W:
        W = img.width
    pieces.append((label, img))
LBL_H = 34
H = sum(p.height + LBL_H for _, p in pieces) + 10 * (len(pieces) - 1)
canvas = Image.new("RGB", (W + 40, H + 20), (235, 235, 235))
d = ImageDraw.Draw(canvas)
y = 10
for label, p in pieces:
    d.text((20, y + 8), label, fill=(0, 0, 120))
    y += LBL_H
    canvas.paste(p, (20, y))
    y += p.height + 10
path = f"{OUT}/_r666-digits-mega.png"
canvas.save(path)
print(f"OK {path} — {canvas.width}x{canvas.height}")

# (c) zooms ciblés 55 %
ZOOMS = [
    ("z1-p87-dua", 87, [(0.53, 0.90)]),
    ("z2-p89-athar", 89, [(0.40, 0.80)]),
    ("z3-p88-28ctx", 88, [(0.42, 0.66)]),
]
for name, page_no, bands in ZOOMS:
    pieces = []
    W = 0
    for (y0, y1) in bands:
        img = render(page_no, y0, y1, 0.55)
        pieces.append(img)
        W = max(W, img.width)
    sep = 24
    H = sum(p.height for p in pieces) + sep * (len(pieces) - 1)
    canvas = Image.new("RGB", (W, H), (220, 220, 220))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y))
        y += p.height + sep
    path = f"{OUT}/{name}-r666.png"
    canvas.save(path)
    print(f"OK {path} — {canvas.width}x{canvas.height}")
