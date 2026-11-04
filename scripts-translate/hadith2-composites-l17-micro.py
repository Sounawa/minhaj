# -*- coding: utf-8 -*-
"""Minhāj — Composite final (comp7) leçon 17 (pdf-18, R562) : micro-zones
1 200 dpi des mots restant non tranchés après les 6 composites (jamais devinées)."""
from PIL import Image, ImageDraw
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r562"
DPI = 900
TARGET_W = 1900

# (label, page, y0, y1, x0, x1) — fractions de page
ZONES = [
    ("118-tamhid-w1", 118, 0.445, 0.492, 0.50, 0.95),
    ("118-nafth-thuluth", 118, 0.783, 0.872, 0.36, 0.96),
    ("120-thuluth-jawaz", 120, 0.742, 0.828, 0.06, 0.58),
    ("119-an-nazara", 119, 0.426, 0.482, 0.40, 0.96),
    ("119-aktib-693", 119, 0.626, 0.682, 0.06, 0.66),
    ("121-mithl-ahlih", 121, 0.488, 0.548, 0.06, 0.66),
    ("121-qabil-dayn", 121, 0.538, 0.602, 0.28, 0.94),
    ("121-madan", 121, 0.606, 0.662, 0.06, 0.66),
    ("121-mutanawwia", 121, 0.650, 0.702, 0.06, 0.56),
    ("121-falyazd", 121, 0.683, 0.738, 0.06, 0.50),
    ("121-risala-fin", 121, 0.768, 0.868, 0.06, 0.96),
    ("122-yanha", 122, 0.268, 0.322, 0.06, 0.60),
    ("122-an-unzur", 122, 0.842, 0.902, 0.06, 0.58),
    ("123-naqala-madin", 123, 0.228, 0.282, 0.06, 0.60),
    ("123-tamanha", 123, 0.278, 0.342, 0.06, 0.64),
    ("123-hurth-man-mudir", 123, 0.446, 0.542, 0.06, 0.64),
    ("123-fayaqum-nasab", 123, 0.538, 0.632, 0.06, 0.64),
    ("123-wafratha", 123, 0.738, 0.798, 0.06, 0.66),
    ("123-muhtakir-firka", 123, 0.786, 0.838, 0.06, 0.54),
    ("124-baatha-yawm", 124, 0.312, 0.362, 0.06, 0.94),
    ("124-aqall-buyu", 124, 0.356, 0.448, 0.06, 0.94),
    ("124-source-naji", 124, 0.442, 0.488, 0.06, 0.94),
]

import gc

doc = fitz.open(PDF)

# grouper par page pour ne garder qu'un rendu 1200 dpi en mémoire à la fois
zones_by_page = {}
for z in ZONES:
    zones_by_page.setdefault(z[1], []).append(z)

tiles_by_label = {}
for page_no in sorted(zones_by_page):
    pix = doc[page_no - 1].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
    img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
    h, w = img.height, img.width
    for label, _, y0, y1, x0, x1 in zones_by_page[page_no]:
        tile = img.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
        scale = TARGET_W / tile.width
        tile = tile.resize((TARGET_W, int(tile.height * scale)), Image.LANCZOS)
        tiles_by_label[label] = tile
    del img, pix
    gc.collect()

tiles = [(label, tiles_by_label[label]) for label, *_ in ZONES]

total_h = sum(t.height + 44 for _, t in tiles) + 10
comp = Image.new("L", (TARGET_W, total_h), 255)
d = ImageDraw.Draw(comp)
y = 5
for label, tile in tiles:
    d.rectangle([0, y, TARGET_W, y + 32], fill=205)
    d.text((10, y + 7), label, fill=0)
    y += 44
    comp.paste(tile, (0, y))
    y += tile.height + 8
path = os.path.join(OUT, "comp7-micro.png")
comp.save(path)
print(f"OK {path} — {TARGET_W}x{total_h}")
