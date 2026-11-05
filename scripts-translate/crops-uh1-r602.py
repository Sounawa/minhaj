#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R602 — recadrages ciblés 1200 dpi + composites par page (leçon 25, p.121-124).
Sortie : tr-tmp/qa-crops-r602/sheet-p<N>.png (empilement vertical, séparateurs)."""
import os
import fitz
from PIL import Image

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r602"
os.makedirs(OUT, exist_ok=True)

# (page, x0, y0, x1, y1) — fractions du rect complet ; dpi par crop
CROPS = {
    121: [
        ("bayt-hemistich2", 0.50, 0.730, 0.98, 0.780, 1200),
    ],
    122: [
        ("ichmal-dars", 0.50, 0.250, 0.98, 0.295, 1200),
        ("ittilaf-rawiyan", 0.55, 0.410, 0.99, 0.460, 1200),
        ("la-yataallaq", 0.03, 0.540, 0.45, 0.585, 1200),
        ("daf-muarrati", 0.55, 0.605, 0.99, 0.655, 1200),
        ("bayquni-quote", 0.50, 0.650, 0.99, 0.700, 1200),
    ],
    123: [
        ("trio-hibban-hayyan-jayyan", 0.28, 0.150, 0.99, 0.200, 1200),
        ("yandabit-lithiqatihi", 0.30, 0.210, 0.99, 0.255, 1200),
        ("lirad-bihi", 0.55, 0.250, 0.99, 0.295, 1200),
        ("sulaym-kullahu", 0.25, 0.290, 0.99, 0.340, 1200),
        ("khazim-fin-droite", 0.45, 0.660, 0.99, 0.725, 1200),
        ("khazim-fin-gauche", 0.02, 0.660, 0.50, 0.725, 1200),
    ],
    124: [
        ("taqwim-q3", 0.35, 0.210, 0.99, 0.250, 1200),
        ("istithmar-l1-droite", 0.48, 0.330, 0.99, 0.375, 1200),
        ("istithmar-l1-gauche", 0.02, 0.330, 0.52, 0.375, 1200),
        ("istithmar-l2-droite", 0.48, 0.370, 0.99, 0.415, 1200),
        ("istithmar-l2-gauche", 0.02, 0.370, 0.52, 0.415, 1200),
        ("istithmar-l3-droite", 0.48, 0.410, 0.99, 0.455, 1200),
        ("istithmar-l3-gauche", 0.02, 0.410, 0.52, 0.455, 1200),
        ("idad-numeros", 0.70, 0.630, 0.99, 0.760, 1200),
    ],
}

doc = fitz.open(PDF)
for pno, specs in CROPS.items():
    page = doc[pno - 1]
    r = page.rect
    parts = []
    for name, fx0, fy0, fx1, fy1, dpi in specs:
        clip = fitz.Rect(r.width * fx0, r.height * fy0, r.width * fx1, r.height * fy1)
        png = f"{OUT}/c-p{pno}-{name}.png"
        page.get_pixmap(dpi=dpi, clip=clip).save(png)
        parts.append(png)
        print(png, os.path.getsize(png))
    # composite : empilement vertical, largeur normalisée
    ims = [Image.open(p) for p in parts]
    W = max(im.width for im in ims)
    PAD = 24
    H = sum(im.height for im in ims) + PAD * (len(ims) + 1)
    sheet = Image.new("RGB", (W + 2 * PAD, H), "white")
    y = PAD
    for im in ims:
        sheet.paste(im, (PAD, y))
        y += im.height + PAD
    sheet.save(f"{OUT}/sheet-p{pno}.png")
    print(f"sheet-p{pno}.png", sheet.size)
