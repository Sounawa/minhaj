#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — lecture visuelle par ASCII art des glyphes de la date العيني (p163, y 697)
# + digits de calibration tirés de dates KNOWNES de la même page/impression.
# Méthode Z2-33 : composantes connexes + rendu ASCII lisible directement.
from PIL import Image
import numpy as np
from scipy import ndimage

D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S = 1200 / 72.0

def art(pg, xa, ya, xb, yb, w=26):
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    a = np.asarray(im, dtype=np.uint8)
    z = (a[int(ya*S):int(yb*S), int(xa*S):int(xb*S)] < 128)
    lab, n = ndimage.label(z)
    # regrouper tous les gros composants (les chiffres)
    comps = []
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if len(ys) < 40:
            continue
        comps.append((xs.min(), xs.max(), ys.min(), ys.max(), len(ys)))
    comps.sort()
    print(f'  zone p{pg} x{xa}-{xb} y{ya}-{yb} : {len(comps)} gros glyphes (LTR)')
    for (cx0, cx1, cy0, cy1, px) in comps:
        sub = (lab[cy0:cy1+1, cx0:cx1+1] > 0)
        h, wd = sub.shape
        # rendu ASCII : 24 colonnes
        cols = 24
        rows = max(8, int(cols * h / wd / 2))
        out = []
        for r in range(rows):
            line = ''
            for c in range(cols):
                yy0, yy1 = int(r*h/rows), int((r+1)*h/rows)
                xx0, xx1 = int(c*wd/cols), int((c+1)*wd/cols)
                d = sub[yy0:yy1, xx0:xx1].mean()
                line += '█' if d > 0.42 else ('▓' if d > 0.18 else ' ')
            out.append(line)
        x_pt0, x_pt1 = xa + cx0/S, xa + cx1/S
        print(f'  --- glyphe x {x_pt0:.1f}-{x_pt1:.1f}pt (l={x_pt1-x_pt0:.1f}) px={px} ---')
        for l in out:
            print('    ' + l)

print('================ ZONE E : date العيني (p163 y 700-720, x 488-535) ================')
art(163, 488, 700, 536, 720)
print()
print('================ CALIBRATION : «827ه» entrée 36 (p165, ligne y 496) ================')
# ligne y=496 : «بن خلفة الوشتاني الأبِّي المالكي المتوفى سنة: 8 ا 2 7 ل ه ن-اشر دار الكتب»
# digits 8,2,7 après «سنة:» — cherchés x≈? : d'après bbox, '8' à x≈? on prend une fenêtre large
art(165, 380, 493, 520, 516)
print()
print('================ CALIBRATION : «795ه» entrée 24 (p163, ligne y 437) ================')
art(163, 60, 432, 200, 458)
