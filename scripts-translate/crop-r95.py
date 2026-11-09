#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R95 — recadrages zoomés des zones douteuses (OCR défaillant sur fonte ornée)
pour relecture visuelle : p86 (objectifs+tête), p90 (Âlūsī), p91 (إعداد قبلي 38-40),
p93 (verset parallèle), p94 (Nasafī ḥalīm/ghafūr), p96 (Ibn Abī Ḥātim), p97 (إعداد قبلي 45-46)."""
from PIL import Image

JOBS = [
    (86, 0, 1300),      # objectifs + tamhīd + début versets
    (90, 150, 2100),    # citation Âlūsī presque toute la page
    (91, 150, 1000),    # إعداد قبلي : expressions + questions
    (93, 1400, 2467),   # bas de page : verset parallèle
    (94, 950, 1950),    # milieu : Nasafī ḥalīm/ghafūr + verset parallèle
    (96, 1300, 2400),   # bas : citation Ibn Abī Ḥātim
    (97, 400, 1500),    # milieu haut : expressions v45-46
]
for p, y0, y1 in JOBS:
    im = Image.open(f"/tmp/r95-p{p}.png")
    crop = im.crop((0, y0, im.width, min(y1, im.height)))
    out = f"/tmp/r95-crop-p{p}.jpg"
    crop.convert("RGB").save(out, quality=72)
    print(out, crop.size)
