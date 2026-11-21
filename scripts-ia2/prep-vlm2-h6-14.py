#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — prep-vlm2-h6-14 : recadrages serrés COULEUR pour la 2e salve VLM.
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/vlm"
os.makedirs(OUT, exist_ok=True)

# (label, page, x0, x1, y0, y1 @600, largeur cible)
ZONES = [
    ("u1-glosse1-p77",  77,  150, 5000, 3240, 3400, 2400),
    ("u2-glosse2-p77",  77,  150, 5000, 3550, 3720, 2400),
    ("u3-fahim-p77",    77,  150, 5000, 2570, 2920, 2400),
    ("u4-lead-p79",     79,  150, 5000, 4530, 4810, 2400),
    ("u5-objectif3-p76",76,  150, 5000, 2255, 2415, 2400),
    ("u6-ouv-p78",      78, 2850, 5160, 5350, 5690, 2000),
    ("u7-taqum-p78",    78,  150, 2850, 4750, 5060, 2000),
    ("u8-lahiqqi-p78",  78,  900, 3750, 3700, 4030, 2200),
]

for label, page, x0, x1, y0, y1, tw in ZONES:
    base = f"{OUT}/{label}"
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "600",
                        "-png", "-singlefile", "-x", str(x0), "-y", str(y0),
                        "-W", str(x1 - x0), "-H", str(y1 - y0), PDF, base], check=True)
    img = Image.open(base + ".png")
    if img.width > tw:
        r = tw / img.width
        img = img.resize((tw, int(img.height * r)), Image.LANCZOS)
        img.save(base + ".png")
    print(f"{label} : {img.width}x{img.height}")
print("OK prep-vlm2")
