#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — identification pixel-level (CC + ASCII) des 3 dernières dates :
#  d8  : p160 x470-590 y395-435  — entrée 8 النسائي «(المتوفى: 303ه)» attendu
#  d13 : p161 x470-590 y420-458  — entrée 13 «1994م.» attendu
#  d14 : p161 x470-590 y490-530  — entrée 14 المعجم الأوسط «360ه)» attendu
# Bibliothèque de formes (calibration même impression) :
#  1=flag+diagonale ; 2=crochet haut+zigzag+bande basse ; 3=deux courbes+centre ;
#  4=diagonale+verticale+2 bandes ; 5=bande haut+bande médiane+descente droite+crochet
#  bas-gauche ; 6=courbe haut-droite balayant bas-gauche ; 7=bande haut+descente
#  gauche ; 8=DEUX BOUCLES empilées ; 9=BOUCLE creuse+queue bas-gauche ; 0=ovale creux
from PIL import Image
import numpy as np
from scipy import ndimage

D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S = 1200 / 72.0

def art(pg, xa, ya, xb, yb, label):
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    a = np.asarray(im, dtype=np.uint8)
    z = (a[int(ya*S):int(yb*S), int(xa*S):int(xb*S)] < 128)
    lab, n = ndimage.label(z)
    comps = []
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if len(ys) < 60:
            continue
        comps.append((xs.min(), xs.max(), ys.min(), ys.max(), len(ys), (lab == i)))
    comps.sort()
    print(f'===== {label} (p{pg} x{xa}-{xb} y{ya}-{yb}) : {len(comps)} glyphes LTR =====')
    for k, (cx0, cx1, cy0, cy1, px, mask) in enumerate(comps):
        sub = mask[cy0:cy1+1, cx0:cx1+1]
        h, wd = sub.shape
        if h < 25 or wd < 15:   # trop petit : point/diacritique
            continue
        cols = 20
        rows = max(7, int(cols * h / wd / 2))
        print(f'  --- g{k} x {xa+cx0/S:.1f}-{xa+cx1/S:.1f}pt l={(cx1-cx0)/S:.1f} h={h/S:.1f}pt px={px} ---')
        for r in range(rows):
            line = ''
            for c in range(cols):
                yy0, yy1 = int(r*h/rows), int((r+1)*h/rows)
                xx0, xx1 = int(c*wd/cols), int((c+1)*wd/cols)
                d = sub[yy0:yy1, xx0:xx1].mean()
                line += '█' if d > 0.42 else ('▒' if d > 0.18 else ' ')
            print('    ' + line)

art(160, 470, 395, 590, 435, 'd8 — النسائي (المتوفى: …)')
art(161, 470, 420, 590, 458, 'd13 — 1994م. attendu')
art(161, 470, 490, 590, 530, 'd14 — المعجم الأوسط (المتوفى: …)')
