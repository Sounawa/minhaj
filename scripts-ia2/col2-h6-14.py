#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — col2-h6-14 : extraction TEXTE BLANC sur bandeau coloré (inversion)
# pour les gloses du الشرح et la ligne bleue p.77.
import subprocess, os
from PIL import Image, ImageOps

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/col2"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(OUT, exist_ok=True)

ZONES = [
    ("g1-ligne1-p77", 77, 3250, 3400),
    ("g2-ligne2-p77", 77, 3550, 3710),
    ("f1-fahim-p77",  77, 2560, 2920),
]

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return " ".join(r.stdout.split())

for label, page, y0, y1 in ZONES:
    base = f"{OUT}/{label}"
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "900",
                        "-png", "-singlefile", "-x", "150", "-y", str(y0),
                        "-W", "5000", "-H", str(y1 - y0), PDF, base], check=True)
    img = Image.open(base + ".png").convert("RGB")
    px = img.load()
    w, h = img.size
    # 1) blanc → noir, le reste → blanc (texte blanc sur bandeau)
    wht = Image.new("L", (w, h), 255)
    # 2) clair-non-coloré → noir (texte clair quelconque)
    lgt = Image.new("L", (w, h), 255)
    p1, p2 = wht.load(), lgt.load()
    for j in range(h):
        for i in range(w):
            R, G, B = px[i, j]
            mx, mn = max(R, G, B), min(R, G, B)
            sat = mx - mn
            lum = (R + G + B) // 3
            if lum > 195 and sat < 45:
                p1[i, j] = 0
            if lum > 165:
                p2[i, j] = 255 - min(255, (255 - lum) * 3)
    print(f"\n████ {label} ████")
    seen = []
    for name, im in (("blanc", wht), ("clair", lgt)):
        for th in (None, 128, 100):
            out = im if th is None else im.point(lambda v: 255 if v > th else 0)
            big = out.resize((out.width * 2, out.height * 2), Image.LANCZOS)
            p = f"{base}-{name}{th or ''}.png"
            big.save(p)
            for psm in (7, 6, 13):
                t = ocr(p, psm)
                if t and len(t) > 4 and t not in seen:
                    seen.append(f"[{name}/{th}/psm{psm}] {t}")
    for s in seen[:5]:
        print("  " + s)
