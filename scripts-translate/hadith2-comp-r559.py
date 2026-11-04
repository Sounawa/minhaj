# -*- coding: utf-8 -*-
"""R559 — composites verticaux (3 bandes par image) pour contourner le quota
d'appels vision (HTTP 429 constaté 08:47-08:59Z) : 7 composites au lieu de
21 lectures. Méthode R550 (lectures groupées). Sorties tr-tmp/qa-comp-r559/."""
from PIL import Image
import os

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r559"
OUT = f"{HOME}/tr-tmp/qa-comp-r559"
os.makedirs(OUT, exist_ok=True)

GROUPS = [
    ("comp-A-p80", ["p80-hadith2", "p80-sharh"]),
    ("comp-B-p81p82", ["p81-tahlil-1", "p81-suite", "p82-top"]),
    ("comp-C-p81p82", ["p81-aya-fatwa", "p82-malika", "p82-hifz"]),
    ("comp-D-p83", ["p83-awqat", "p83-thaniya", "p83-dua1"]),
    ("comp-E-p83p84", ["p83-dua2-3", "p84-dua3-fin", "p84-tamata"]),
    ("comp-F-p84", ["p84-thulth", "p84-bid", "p84-iftitah"]),
    ("comp-G-p85p86", ["p85-istidlal-1", "p85-hadith", "p85-taqwim", "p86-borne"]),
]

W = 1900
for name, bands in GROUPS:
    path = f"{OUT}/{name}.png"
    if os.path.exists(path):
        print("•", name, "existe")
        continue
    ims = []
    for b in bands:
        im = Image.open(f"{CROPS}/{b}.png").convert("RGB")
        r = W / im.width
        im = im.resize((W, int(im.height * r)), Image.LANCZOS)
        ims.append(im)
    sep = 26
    H = sum(i.height for i in ims) + sep * (len(ims) - 1)
    canvas = Image.new("RGB", (W, H), (255, 230, 230))  # séparation rosée
    y = 0
    for i in ims:
        canvas.paste(i, (0, y))
        y += i.height + sep
    canvas.save(path)
    print(f"{name}: {canvas.size} ← {' + '.join(bands)}")
print("COMPOSITES OK")
