# -*- coding: utf-8 -*-
"""R573 — composite G : 10 re-crops 2400 dpi pour les mots résiduels."""
import os

import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r573-crops"
doc = fitz.open(PDF)
WIDTH = 1400

BANDS = [
    (193, 0.50, 0.195, 0.95, 0.245, 2400),  # g1 «إنما يدع شهوته»
    (195, 0.30, 0.112, 0.60, 0.168, 2400),  # g2 «كتخمّ»
    (195, 0.05, 0.195, 0.60, 0.255, 2400),  # g3 «التشريف والتعتيم»
    (195, 0.20, 0.262, 0.70, 0.325, 2400),  # g4 «بعشرة أمثالها»
    (195, 0.60, 0.262, 0.95, 0.325, 2400),  # g10 «تعالي + كل حسنة»
    (195, 0.35, 0.745, 0.75, 0.805, 2400),  # g5 «فإن أمِرَّ قاتله»
    (196, 0.40, 0.288, 0.90, 0.345, 2400),  # g6 «ولم رأيته»
    (196, 0.05, 0.605, 0.95, 0.695, 900),   # g7 phrase «بينها وبينه فرائض»
    (197, 0.30, 0.145, 0.70, 0.215, 2400),  # g8 «أين/أبين المراد»
    (197, 0.15, 0.435, 0.65, 0.500, 2400),  # g9 «خير حصال الصائم السواك»
]

pieces = []
for i, (pno, x0, y0, x1, y1, dpi) in enumerate(BANDS, 1):
    page = doc[pno - 1]
    r = page.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    tmp = f"/tmp/g_{i}.png"
    pix.save(tmp)
    im = Image.open(tmp)
    if im.width > WIDTH:
        h = int(im.height * WIDTH / im.width)
        im = im.resize((WIDTH, h), Image.LANCZOS)
    lab = Image.new("RGB", (WIDTH, 30), (230, 230, 230))
    d = ImageDraw.Draw(lab)
    d.text((6, 6), f"g{i}: p.{pno} ({x0:.2f}-{x1:.2f} x {y0:.2f}-{y1:.2f}) {dpi}dpi", fill=(0, 0, 0))
    pieces.append(lab)
    pieces.append(im)

total_h = sum(p.height for p in pieces) + 4 * len(pieces)
comp = Image.new("RGB", (WIDTH, total_h), (255, 255, 255))
y = 0
for p in pieces:
    comp.paste(p, (0, y))
    y += p.height + 4
path = f"{OUT}/G-re-crops.png"
comp.save(path)
print(path, comp.size)
