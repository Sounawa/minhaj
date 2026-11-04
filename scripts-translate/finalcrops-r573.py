# -*- coding: utf-8 -*-
"""R573 — composite H : 7 re-crops 2400 dpi, adjudication terminale."""
import os

import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r573-crops"
doc = fitz.open(PDF)
WIDTH = 1400

BANDS = [
    (193, 0.03, 0.150, 0.35, 0.200, 2400),  # h1 «يَدْأُ/يَدَعُ» fin de ligne
    (195, 0.55, 0.105, 0.90, 0.155, 2400),  # h2 «كتخمّ»
    (195, 0.03, 0.262, 0.30, 0.325, 2400),  # h3 «بعشرة أمثالها»
    (196, 0.35, 0.355, 0.70, 0.415, 2400),  # h4 «ولم رأيته»
    (196, 0.45, 0.648, 0.95, 0.695, 2400),  # h5 «بينهما وبينه فيعتقدوها فرائض»
    (197, 0.55, 0.195, 0.95, 0.250, 2400),  # h6 «أين/أبين المراد»
    (197, 0.55, 0.395, 0.95, 0.460, 2400),  # h7 «خير حصال الصائم السواك»
]

pieces = []
for i, (pno, x0, y0, x1, y1, dpi) in enumerate(BANDS, 1):
    page = doc[pno - 1]
    r = page.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    tmp = f"/tmp/h_{i}.png"
    pix.save(tmp)
    im = Image.open(tmp)
    if im.width > WIDTH:
        h = int(im.height * WIDTH / im.width)
        im = im.resize((WIDTH, h), Image.LANCZOS)
    lab = Image.new("RGB", (WIDTH, 30), (230, 230, 230))
    d = ImageDraw.Draw(lab)
    d.text((6, 6), f"h{i}: p.{pno} ({x0:.2f}-{x1:.2f} x {y0:.2f}-{y1:.2f}) {dpi}dpi", fill=(0, 0, 0))
    pieces.append(lab)
    pieces.append(im)

total_h = sum(p.height for p in pieces) + 4 * len(pieces)
comp = Image.new("RGB", (WIDTH, total_h), (255, 255, 255))
y = 0
for p in pieces:
    comp.paste(p, (0, y))
    y += p.height + 4
path = f"{OUT}/H-final-crops.png"
comp.save(path)
print(path, comp.size)
