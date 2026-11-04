# -*- coding: utf-8 -*-
"""Minhāj — Composites 600 dpi pour les zones ambiguës de la leçon 20 (pdf-21, R565).
Méthode R559-R562 : bandes 600 dpi coupées en deux moitiés verticales, empilées
à l'échelle 1:1 (largeur 2655 px → lecture à ~354 dpi effectifs après downscale Read)."""
from PIL import Image

SRC = "/home/z/my-project/tr-tmp/qa-crops-r565/sd-{}.png"  # 600 dpi
OUT = "/home/z/my-project/tr-tmp/qa-crops-r565/composite-l20-{}.png"

# (composite, [(page, y0, y1), ...]) — bandes en pixels 600 dpi (page 5310×6726)
BANDS = {
    1: [(140, 2220, 2920), (140, 3020, 3360)],   # 727 isnād+matn ; 733 ligne
    2: [(139, 4740, 5300), (140, 3834, 4434)],   # 745 citation ; 735 ouverture
    3: [(142, 1020, 1680), (142, 2690, 3290)],   # 736 matn ; 728-bis
    4: [(142, 4943, 5543), (143, 3665, 4405)],   # 737 liste ; āya Anʿām + 735-bis
    5: [(143, 2421, 3321)],                      # 729 passage khars
    6: [(144, 3100, 3900), (141, 3060, 3360)],   # qoṭṭāniyya ; glossaire yuḫarriṣu
    7: [(144, 4650, 5350), (145, 2555, 3195)],   # liste ب ; box istīthār
}

HALF = 2655  # moitié de 5310

for idx, bands in BANDS.items():
    strips = []
    for page, y0, y1 in bands:
        im = Image.open(SRC.format(page))
        if im.size != (5310, 6726):
            print(f"WARN page {page} dims {im.size}")
        w, h = im.size
        y0c, y1c = max(0, y0), min(h, y1)
        left = im.crop((0, y0c, min(HALF, w), y1c))
        right = im.crop((max(0, w - HALF), y0c, w, y1c))
        strips.extend([left, right])
    total_h = sum(s.height for s in strips) + 6 * (len(strips) - 1)
    comp = Image.new("RGB", (HALF, total_h), (220, 220, 220))
    y = 0
    for s in strips:
        comp.paste(s, (0, y))
        y += s.height + 6
    comp.save(OUT.format(idx))
    print(f"OK composite {idx}: {comp.size[0]}x{comp.size[1]} ({len(strips)} bandes)")

import json
d = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json", encoding="utf-8"))
s6 = d["6"]
print("FR 6:141 COMPLET:", s6["fr"][140][1])
