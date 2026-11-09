# -*- coding: utf-8 -*-
"""Minhāj R664 — composites verticaux de lignes du tableau tarāǧim.
Méthode d'économie de lectures validée R103 (6 lectures groupées pour 11 pages).
Chaque composite = 2-3 lignes 600 dpi empilées, séparées par une barre rouge,
étiquetées en marge. Sortie : tr-tmp/qa-crops-r664/comp-r664-<n>.png"""
from PIL import Image, ImageDraw

DIR = "/home/z/my-project/tr-tmp/qa-crops-r664"
RED = (200, 30, 30)

COMPS = {
    "comp-r664-a": ["row-p132-r0-qari", "row-p132-r3-raz", "row-p132-r5-zark"],
    "comp-r664-b": ["row-p133-r1-abd", "row-p133-r2-hakim"],
    "comp-r664-c": ["row-p133-r4-khatib", "row-p134-r1-sakhawi"],
    "comp-r664-d": ["row-p134-r0-dhahabi", "row-p134-r2-suyuti"],
    "comp-r664-e": ["row-p134-r3-iyad", "row-p133-r0-salah"],
}

for out, names in COMPS.items():
    imgs = [Image.open(f"{DIR}/{n}.png") for n in names]
    w = max(i.width for i in imgs)
    bar = 26
    h = sum(i.height for i in imgs) + bar * len(imgs)
    canvas = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(canvas)
    y = 0
    for n, im in zip(names, imgs):
        d.rectangle([0, y, w, y + bar], fill=RED)
        d.text((10, y + 4), n + " 600dpi", fill=(255, 255, 255))
        y += bar
        canvas.paste(im, (0, y))
        y += im.height
    canvas.save(f"{DIR}/{out}.png")
    print(out, w, "x", h, "←", ", ".join(names))
