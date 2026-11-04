# -*- coding: utf-8 -*-
"""Minhāj — Micro-crops 600 dpi + composites leçon 23 (pdf-24, R569).
Zones sensibles : āya warš az-Zumar (p.158), fin 796 + 791 (p.159),
المريم/vers (p.160), النفل-Darquṭnī + 785 (p.161), 786 + ʿUṯmān 787 +
šubha (p.162), 789/794/799 (p.163), 790 (p.164).
Coordonnées TSV (300 dpi) ×2 → 600 dpi. Composites empilés pour lecture.
"""
import os
import subprocess

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r569"
doc = fitz.open(PDF)

# (page, y1_300, y2_300, étiquette)
ZONES = {
    "compA": [
        (158, 1830, 2360, "p158-aya-zumar"),
        (160, 1690, 2660, "p160-maryam-vers"),
        (161, 1340, 1810, "p161-nadfl-darqutni"),
    ],
    "compB": [
        (159, 1090, 1560, "p159-fin-796"),
        (159, 1490, 1960, "p159-791"),
        (161, 2140, 3260, "p161-waq-wujub-785"),
    ],
    "compC": [
        (162, 690, 1160, "p162-fin-786"),
        (162, 1940, 2460, "p162-uthman-787"),
        (162, 2540, 3060, "p162-shubha-789"),
    ],
    "compD": [
        (163, 140, 660, "p163-haut-789"),
        (163, 940, 1760, "p163-794"),
        (163, 1890, 2460, "p163-799"),
        (164, 240, 1210, "p164-790"),
    ],
}

pages_needed = sorted({z[0] for zs in ZONES.values() for z in zs})
for n in pages_needed:
    p600 = f"{CROPS}/page-{n}-600.png"
    if not os.path.exists(p600):
        pix = doc[n - 1].get_pixmap(dpi=600)
        pix.save(p600)
        print(f"RENDU {p600}")

for comp, zones in ZONES.items():
    imgs = []
    for n, y1, y2, label in zones:
        im = Image.open(f"{CROPS}/page-{n}-600.png")
        w = im.width
        crop = im.crop((0, y1 * 2, w, y2 * 2))
        imgs.append(crop)
        crop.save(f"{CROPS}/c-{label}.png")
        print(f"CROP {label}: {crop.width}x{crop.height}")
    total_h = sum(i.height for i in imgs) + 12 * (len(imgs) - 1)
    max_w = max(i.width for i in imgs)
    canvas = Image.new("RGB", (max_w, total_h), (255, 210, 210))
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + 12
    canvas.convert("RGB").save(f"{CROPS}/{comp}.jpg", quality=82)
    print(f"COMPOSITE {comp}: {canvas.width}x{canvas.height}")
print("DONE")
