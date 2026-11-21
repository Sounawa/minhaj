#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — col-h6-14 : extraction par couches colorées des zones résistantes.
# Le tirage imprime : texte blanc sur bandeaux bleus, texte bleu/foncé sur cellules
# jaunes, sous-titres rouges, encadré jaune du texte-source. En gris, tesseract
# s'effondre ; on sépare par canaux/masques puis OCR psm 6/7/13.
import subprocess, os
from PIL import Image, ImageOps

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/col"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(OUT, exist_ok=True)

# (label, page, y0, y1 @600)
ZONES = [
    ("c1-gloses-p77",     77, 3200, 3760),
    ("c2-rat-line-p77",   77, 2560, 2900),
    ("c3-lead-p79",       79, 4520, 4860),
    ("c4-objectifs-p76",  76, 1640, 2430),
    ("c5-cartouche-p76",  76,  600, 1050),
    ("c6-bayyina-p78",    78, 1070, 1690),
    ("c7-yubayyin-p78",   78, 5350, 5700),
    ("c8-liali-p78",      78, 1880, 2200),
]

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return " ".join(r.stdout.split())

for label, page, y0, y1 in ZONES:
    base = f"{OUT}/{label}"
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "600",
                        "-png", "-singlefile", "-x", "150", "-y", str(y0),
                        "-W", "5000", "-H", str(y1 - y0), PDF, base], check=True)
    img = Image.open(base + ".png").convert("RGB")
    px = img.load()
    w, h = img.size
    # variantes : sombre (tout ce qui n'est pas fond clair), texte-coloré (non-gris),
    # rouge seul, bleu seul, jaune-absorbé (noir sur jaune)
    dark = Image.new("L", (w, h), 255)
    colored = Image.new("L", (w, h), 255)
    red = Image.new("L", (w, h), 255)
    blue = Image.new("L", (w, h), 255)
    onyellow = Image.new("L", (w, h), 255)
    d, c, r_, b, y_ = dark.load(), colored.load(), red.load(), blue.load(), onyellow.load()
    for j in range(h):
        for i in range(w):
            R, G, B = px[i, j]
            mx, mn = max(R, G, B), min(R, G, B)
            lum = (R + G + B) // 3
            if lum < 150:
                d[i, j] = lum
            if mx - mn > 40:  # pixel franchement coloré
                c[i, j] = 255 - lum
                if R > G + 30 and R > B + 30:
                    r_[i, j] = 255 - lum
                if B > R + 30 and B > G + 10:
                    b[i, j] = 255 - lum
            if R > 170 and G > 150 and B < 140:  # fond jaune → texte = le reste
                y_[i, j] = 255
    print(f"\n████ {label} (p.{page}) ████")
    for name, im in (("dark", dark), ("colored", colored), ("red", red),
                     ("blue", blue), ("onyellow", onyellow)):
        p = f"{base}-{name}.png"
        im.save(p)
        for psm in (6, 7):
            t = ocr(p, psm)
            if t and len(t) > 3:
                print(f"  [{name}/psm{psm}] {t[:340]}")
                break
