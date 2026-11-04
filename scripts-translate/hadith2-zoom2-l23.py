# -*- coding: utf-8 -*-
"""Minhāj — Dernier zoom 1200 dpi (compF) leçon 23 (pdf-24, R569).
(a) āya warš az-Zumar seule ; (b) p.159 « إنك لست... » ; (c) p.162 clause ʿUmda.
"""
from PIL import Image

CROPS = "/home/z/my-project/tr-tmp/qa-crops-r569"

# rendu 1200 dpi des 3 pages
import fitz
doc = fitz.open("/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf")
for n in (158, 159, 162):
    p = f"{CROPS}/page-{n}-1200.png"
    import os
    if not os.path.exists(p):
        doc[n - 1].get_pixmap(dpi=1200).save(p)
        print(f"RENDU {p}")

# (page, x1, y1, x2, y2) en 300 dpi → ×4
ZONES = [
    (158, 1380, 1900, 2160, 2350, "z2-aya"),
    (159, 1100, 1130, 2480, 1270, "z2-fin796"),
    (162, 230, 2320, 2480, 2460, "z2-umda"),
]

imgs = []
for n, x1, y1, x2, y2, label in ZONES:
    im = Image.open(f"{CROPS}/page-{n}-1200.png")
    crop = im.crop((x1 * 4, y1 * 4, x2 * 4, y2 * 4))
    imgs.append(crop)
    crop.save(f"{CROPS}/c-{label}.png")
    print(f"CROP {label}: {crop.width}x{crop.height}")

total_h = sum(i.height for i in imgs) + 14 * (len(imgs) - 1)
max_w = max(i.width for i in imgs)
canvas = Image.new("RGB", (max_w, total_h), (255, 210, 210))
y = 0
for i in imgs:
    canvas.paste(i, (0, y))
    y += i.height + 14
canvas.save(f"{CROPS}/compF.jpg", quality=85)
print(f"COMPOSITE compF: {canvas.width}x{canvas.height}")
