# -*- coding: utf-8 -*-
"""Minhāj — Zooms étroits 600 dpi (compE) leçon 23 (pdf-24, R569).
5 zones douteuses : p.159 « إنك لست... », p.158 āya warš az-Zumar,
p.161 suite ʿĀʾiša/Darquṭnī, p.162 « عمدا...عند مالك », p.163 « فأجابه بالفعل ».
"""
from PIL import Image

CROPS = "/home/z/my-project/tr-tmp/qa-crops-r569"

# (page, x1, y1, x2, y2) en coordonnées 300 dpi → ×2 pour 600 dpi
ZONES = [
    (159, 1100, 1090, 2480, 1330, "z-fin796"),
    (158, 480, 1850, 2200, 2340, "z-aya-zumar"),
    (161, 260, 1740, 2480, 2170, "z-aischa-darqutni"),
    (162, 230, 2320, 2480, 2570, "z-umda-malik"),
    (163, 230, 1950, 2480, 2130, "z-ajaba-bilfil"),
]

imgs = []
for n, x1, y1, x2, y2, label in ZONES:
    im = Image.open(f"{CROPS}/page-{n}-600.png")
    crop = im.crop((x1 * 2, y1 * 2, x2 * 2, y2 * 2))
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
canvas.save(f"{CROPS}/compE.jpg", quality=85)
print(f"COMPOSITE compE: {canvas.width}x{canvas.height}")
