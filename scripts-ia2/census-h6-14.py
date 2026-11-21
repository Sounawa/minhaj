#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — census-h6-14 : recensement des couleurs par bande horizontale (p.77,
# y2400-3800) pour comprendre la structure (bandeaux, cellules, encadrés).
import subprocess, os
from collections import Counter
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14"
page, y0, y1 = 77, 2400, 3800
base = f"{OUT}/census-p77"
if not os.path.exists(base + ".png"):
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "300",
                    "-png", "-singlefile", "-x", "75", "-y", str(y0 // 2),
                    "-W", "2500", "-H", str((y1 - y0) // 2), PDF, base], check=True)
img = Image.open(base + ".png").convert("RGB")
px = img.load()
w, h = img.size

def classe(R, G, B):
    mx, mn = max(R, G, B), min(R, G, B)
    sat = mx - mn
    lum = (R + G + B) // 3
    if sat < 35:
        if lum > 225: return "blanc"
        if lum > 140: return "grisclair"
        return "noir"
    if R > 150 and G > 120 and B < 130: return "jaune"
    if R > 150 and G < 130 and B < 130: return "rouge"
    if B > 130 and B > R + 25 and B > G + 10: return "bleu"
    if G > 130 and G > R + 20 and G > B + 20: return "vert"
    if R > 140 and G > 100 and B > 100: return "or/beige"
    return "autre"

# census par bandes de 40 px (300dpi → y600 = y*2)
print("bande y@600 | classes dominantes (%, part)")
for j0 in range(0, h, 20):  # 20px @300 = 40px @600
    c = Counter()
    for j in range(j0, min(j0 + 20, h)):
        for i in range(0, w, 3):
            c[classe(*px[i, j])] += 1
    tot = sum(c.values())
    top = ", ".join(f"{k} {v * 100 // tot}%" for k, v in c.most_common(4) if v * 100 // tot >= 3)
    print(f"y{y0 + j0 * 2:4d} | {top}")
