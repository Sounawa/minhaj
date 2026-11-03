#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — R558 (pdf-14, leçon 13) : micro-crops 900-1200 dpi pour trancher
en-tête, āya, isnāds, numéros rouges et lexies. Sortie : tr-tmp/qa-crops-r558/
  - comp-pNN.png : bandes empilées par page
  - composite-numbers.png : bandes 1200 dpi autour de chaque « الموطأ رقم »
"""
import fitz
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r558"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# --- bandes fractionnelles par page (y0, y1 en fraction de hauteur) ---
BANDS = {
    91: [(0.00, 0.14, 900), (0.14, 0.62, 900), (0.60, 1.00, 900)],
    92: [(0.00, 0.34, 900), (0.32, 0.62, 900), (0.60, 0.80, 900), (0.78, 1.00, 900)],
    93: [(0.00, 0.16, 1200), (0.20, 0.50, 1200)],
    94: [(0.06, 0.34, 900), (0.32, 0.62, 900), (0.58, 0.80, 900)],
    95: [(0.00, 0.26, 900), (0.24, 0.42, 900), (0.40, 0.72, 900), (0.70, 1.00, 900)],
    96: [(0.00, 0.24, 900), (0.22, 0.48, 900), (0.46, 0.72, 900), (0.70, 1.00, 900)],
    97: [(0.00, 0.26, 1000), (0.24, 0.52, 1000), (0.52, 0.88, 1000)],
}

for pno, bands in BANDS.items():
    page = doc[pno - 1]
    H, W = page.rect.height, page.rect.width
    strips = []
    for f0, f1, dpi in bands:
        clip = fitz.Rect(0, H * f0, W, H * f1)
        pm = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
        tmp = f"{OUT}/_strip.png"
        pm.save(tmp)
        strips.append(Image.open(tmp))
    w = max(im.width for im in strips)
    w = min(w, 2400)
    h = sum(min(im.height, 2200) + 10 for im in strips)
    comp = Image.new("RGB", (w, h), "white")
    y = 0
    for im in strips:
        if im.width > w:
            im = im.resize((w, int(im.height * w / im.width)))
        comp.paste(im, (0, y))
        y += im.height + 10
    comp.save(f"{OUT}/comp-p{pno}.png")
    print(f"comp-p{pno}.png : {w}x{comp.height}")

# --- bandes numéros rouges : occurrences de « الموطأ رقم » (couche : أطوملا) ---
NUMBANDS = []
for pno in range(90, 99):
    page = doc[pno - 1]
    for tok in ("أطوملا", "اطوملا", "أاطوملا"):
        for r in page.search_for(tok):
            clip = fitz.Rect(max(0, r.x0 - 210), max(0, r.y0 - 9),
                             min(page.rect.width, r.x1 + 25), min(page.rect.height, r.y1 + 9))
            pm = page.get_pixmap(matrix=fitz.Matrix(1200 / 72, 1200 / 72), clip=clip)
            tmp = f"{OUT}/_num.png"
            pm.save(tmp)
            NUMBANDS.append((pno, Image.open(tmp)))
        if NUMBANDS and NUMBANDS[-1][0] == pno:
            break
strips = NUMBANDS
w = min(max(im.width for _, im in strips), 2400)
h = sum(min(im.height, 300) + 12 for _, im in strips)
comp = Image.new("RGB", (w, h), "white")
y = 0
for pno, im in strips:
    if im.width > w:
        im = im.resize((w, int(im.height * w / im.width)))
    comp.paste(im, (0, y))
    y += im.height + 12
comp.save(f"{OUT}/composite-numbers.png")
print(f"composite-numbers.png : {w}x{comp.height} — {len(strips)} bandes")
