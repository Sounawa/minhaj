#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — calibration empirique des chiffres de l'impression : rendu ASCII de
# chiffres CONNUS (double-confirmés cmap+tesseract) pour identifier les 3
# chiffres de la date العيني (X=9840px ; Y=Y=7680/7712px).
from html.parser import HTMLParser
from PIL import Image
import numpy as np
from scipy import ndimage

SRC = '/home/z/my-project/scripts-ia2/tmp/h5-29/bbox-159-166.html'
D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S = 1200 / 72.0

class B(HTMLParser):
    def __init__(self):
        super().__init__()
        self.words=[]; self.cur=None; self.page=158; self.inw=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='page': self.page+=1
        elif tag=='word':
            self.inw=True
            self.cur=[self.page,float(a['xmin']),float(a['ymin']),float(a['xmax']),float(a['ymax']),'']
    def handle_endtag(self, tag):
        if tag=='word' and self.cur: self.words.append(tuple(self.cur)); self.cur=None; self.inw=False
    def handle_data(self,d):
        if self.inw: self.cur[5]+=d
b=B(); b.feed(open(SRC,encoding='utf-8').read())

def art(pg, xa, ya, xb, yb, label, cols=22):
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    a = np.asarray(im, dtype=np.uint8)
    z = (a[int(ya*S):int(yb*S), int(xa*S):int(xb*S)] < 128)
    if z.sum() < 40:
        print(f'  {label}: (vide)'); return
    lab, n = ndimage.label(z)
    # garder le plus gros composant
    best, bestn = None, 0
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if len(ys) > bestn: bestn, best = len(ys), (xs.min(), xs.max(), ys.min(), ys.max(), lab==i)
    cx0, cx1, cy0, cy1, mask = best
    sub = mask[cy0:cy1+1, cx0:cx1+1]
    h, wd = sub.shape
    rows = max(7, int(cols * h / wd / 2))
    print(f'  {label}  (x {xa+cx0/S:.1f}-{xa+cx1/S:.1f}, l={(cx1-cx0)/S:.1f}pt, px={bestn})')
    for r in range(rows):
        line = ''
        for c in range(cols):
            yy0, yy1 = int(r*h/rows), int((r+1)*h/rows)
            xx0, xx1 = int(c*wd/cols), int((c+1)*wd/cols)
            d = sub[yy0:yy1, xx0:xx1].mean()
            line += '█' if d > 0.42 else ('▒' if d > 0.18 else ' ')
        print('    ' + line)

# trouver le mot-chiffre (page, chiffre, y ±4)
def find_digit(pg, ch, yline):
    cands = [w for w in b.words if w[0]==pg and w[5]==ch and abs(w[2]-yline)<5]
    if not cands:
        print(f'  p{pg} chiffre {ch} y≈{yline}: INTROUVABLE'); return
    w = cands[0]
    pad = 1.2
    art(pg, w[1]-pad, w[2]-pad, w[3]+pad, w[4]+pad, f'«{ch}» p{pg} y{yline}')

print("========== CALIBRATION CHIFFRES CONNUS ==========")
# 256 (p159 y385.6) ; 261 (p159 y518.1) ; 273 (p160 y180.8) ; 458 (p160 y278.9)
# 303 (p160 y~333?) ; 275 (p160 y~360?) ; 354 (p160 y~410?)
# 795 (p163 y437.4) ; 449 (p163 y535.3) ; 827 (p165 y496.0) ; 849/911 (p164 y504.8)
for pg, ch, y in [(159,'2',385.6),(159,'5',385.6),(159,'6',385.6),
                  (159,'2',518.1),(159,'6',518.1),(159,'1',518.1),
                  (160,'2',180.8),(160,'7',180.8),(160,'3',180.8),
                  (160,'4',278.9),(160,'5',278.9),(160,'8',278.9),
                  (163,'7',437.4),(163,'9',437.4),(163,'5',437.4),
                  (163,'4',535.3),(163,'4',535.3),(163,'9',535.3),
                  (165,'8',496.0),(165,'2',496.0),(165,'7',496.0),
                  (164,'8',504.8),(164,'4',504.8),(164,'9',504.8),(164,'1',504.8)]:
    find_digit(pg, ch, y)
