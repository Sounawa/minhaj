#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — 2e vague de recadrages : zones serrées (une ligne), r600 ET r1200,
# pour les points où la 1re vague a échoué (B/C/E/F) + header complet entrée 37.
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S1200 = 1200 / 72.0
S600 = 600 / 72.0

zones = [
    # (page, nom, x0,y0,x1,y1, [ressources])
    (159, 'B2-abudawud',     30, 641, 340, 671, [600, 1200]),
    (160, 'C2-sunankubra',   40, 241, 600, 267, [600, 1200]),
    (163, 'E2-ayni',        380, 687, 600, 715, [600, 1200]),
    (163, 'E3-ayni-large',  340, 660, 600, 715, [600, 1200]),
    (163, 'F2-haytami',     40,  74, 600, 104, [600, 1200]),
    (165, 'G2-entree37hdr', 40, 596, 600, 648, [600, 1200]),
]

for p, nom, x0, y0, x1, y1, ress in zones:
    for res in ress:
        im = Image.open(f'{D}/r{res}/p{p}.png')
        S = S1200 if res == 1200 else S600
        box = (int(x0*S), int(y0*S), int(x1*S), int(y1*S))
        crop = im.crop(box)
        # pour r600 : agrandir ×2 pour aider tesseract sur les petits fragments
        if res == 600:
            crop = crop.resize((crop.width*2, crop.height*2), Image.LANCZOS)
        out = f'{D}/crops/{nom}-r{res}.png'
        os.makedirs(f'{D}/crops', exist_ok=True)
        crop.save(out)
        print(nom, f'r{res}', crop.size)
