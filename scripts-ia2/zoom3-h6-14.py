#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-14 : micro-zooms 1800 dpi + upscale LANCZOS ×2 + seuils multiples
# pour les zones résiduelles (gloses الشرح, item 1 استخلاص, mots disputés…).
import subprocess, os
from PIL import Image, ImageOps

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/zoom3"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(OUT, exist_ok=True)

# (label, page, y0, y1 @600, psm, x0, x1 @600)  — x en px @600 (largeur 5309)
TARGETS = [
    ("gloses-sharh-p77",   77, 3260, 3700, 6,  300, 5000),
    ("istikhlal-item1-p77",77, 4100, 4470, 7,  300, 5000),
    ("liuali-mot-p78",     78, 1890, 2180, 7,  300, 5000),
    ("lahiqqi-mot-p78",    78, 3710, 4010, 7,  300, 5000),
    ("malam-taqum-p78",    78, 4770, 5030, 7,  300, 5000),
    ("yatabayyan-p78",     78, 5370, 5670, 7,  300, 5000),
    ("thalithan-head-p79", 79,  920, 1100, 7,  300, 5000),
    ("istithmar-lead-p79", 79, 4540, 4830, 7,  300, 5000),
    ("objectif3-p76",      76, 2270, 2400, 7,  300, 5000),
    ("falayahkum-p79",     79, 2110, 2330, 7,  300, 5000),
]

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return " ".join(r.stdout.split())

for label, page, y0, y1, psm, x0, x1 in TARGETS:
    base = f"{OUT}/{label}"
    y3, h3 = 3 * y0, 3 * (y1 - y0)
    x3, w3 = 3 * x0, 3 * (x1 - x0)
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "1800",
                        "-gray", "-png", "-singlefile",
                        "-x", str(x3), "-y", str(y3), "-W", str(w3), "-H", str(h3),
                        PDF, base], check=True)
    img = Image.open(base + ".png")
    big = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)
    auto = ImageOps.autocontrast(big, cutoff=1)
    seen = []
    print(f"\n████ {label} (p.{page}, y{y0}-{y1}, psm{psm}) ████")
    variants = [("auto", auto)]
    for th in (130, 150, 170, 190):
        variants.append((f"bw{th}", auto.point(lambda v, t=th: 255 if v > t else 0)))
    for name, im in variants:
        p = f"{base}-{name}.png"
        im.save(p)
        t = ocr(p, psm)
        if t and t not in seen:
            seen.append(t)
            print(f"  [{name}] {t}")
