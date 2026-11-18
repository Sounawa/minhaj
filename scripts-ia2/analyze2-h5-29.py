#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — analyse sans-VLM round 3 :
#  (a) X-extent des bandes A1 (p159 y237-257), D2 (p162 y557-576), G1 (p165 y625-648)
#      → longueur/largeur des lignes cachées (centrée ? pleine largeur ?)
#  (b) composantes connexes : B (p159 x25-115 y645-680 après الأزدي),
#      E (p163 x490-570 y690-720 date العيني) → nombre de glyphes, largeurs
#  (c) tesseract multi-variantes (échelle ×2, binarisation, psm 6/7/13) sur les strips
from PIL import Image, ImageOps
import numpy as np, subprocess, os
from scipy import ndimage

D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S = 1200 / 72.0
TESS = '/home/z/my-project/scripts-translate/tessdata'

def strip(pg, xa, ya, xb, yb, scale=1, binar=False):
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    c = im.crop((int(xa*S), int(ya*S), int(xb*S), int(yb*S)))
    if scale != 1:
        c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
    if binar:
        c = c.point(lambda v: 0 if v < 150 else 255)
    return c

def tess(img, psm, tag):
    fp = f'{D}/crops/r3-{tag}.png'
    img.save(fp)
    r = subprocess.run(['tesseract', fp, 'stdout', '-l', 'ara', '--tessdata-dir', TESS,
                        '--psm', str(psm)], capture_output=True, text=True)
    return r.stdout.strip().replace('\n', ' ⏎ ')[:200]

# (a) X-extent : profil horizontal d'encre
print('===== (a) X-EXTENT DES BANDES CACHÉES =====')
for nom, pg, ya, yb in [('A1', 159, 236, 258), ('D2', 162, 556, 578), ('G1', 165, 624, 649)]:
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    a = np.asarray(im, dtype=np.uint8)
    z = (a[int(ya*S):int(yb*S), :] < 128)
    prof = z.mean(axis=0)
    cols = np.where(prof > 0.01)[0]
    if len(cols):
        x0_pt, x1_pt = cols.min()/S, cols.max()/S
        # segmentation en mots (gaps > 12 pt)
        gaps, words, cur = [], [], [cols[0]]
        for i in range(1, len(cols)):
            if cols[i] - cols[i-1] > 12*S/1:
                words.append(cur); cur = [cols[i]]
            else:
                cur.append(cols[i])
        words.append(cur)
        segs = [(w[0]/S, w[-1]/S) for w in words]
        print(f'{nom} p{pg} y{ya}-{yb}: x {x0_pt:.0f}→{x1_pt:.0f} pt '
              f'(largeur {x1_pt-x0_pt:.0f} pt, page 637 pt) — {len(segs)} îlots:')
        print('   îlots (x pt):', ' '.join(f'{s:.0f}-{e:.0f}' for s, e in segs[:40]))
    else:
        print(f'{nom} p{pg}: VIDE')

# (b) composantes connexes
print()
print('===== (b) COMPOSANTES CONNEXES =====')
for nom, pg, xa, ya, xb, yb in [('B-après-Azdi', 159, 30, 644, 118, 680),
                                  ('E-date-ayni', 163, 488, 690, 572, 718)]:
    im = Image.open(f'{D}/r1200/p{pg}.png').convert('L')
    a = np.asarray(im, dtype=np.uint8)
    z = (a[int(ya*S):int(yb*S), int(xa*S):int(xb*S)] < 128)
    lab, n = ndimage.label(z)
    print(f'--- {nom} (p{pg} x{xa}-{xb} y{ya}-{yb}) : {n} composantes ---')
    comps = []
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if len(ys) < 6:
            continue
        comps.append((xs.min()/S+xa, xs.max()/S+xa, ys.min()/S+ya, ys.max()/S+ya, len(ys)))
    comps.sort()
    for c in comps:
        print(f'   x {c[0]:6.1f}→{c[1]:6.1f} (l={c[1]-c[0]:5.1f}pt) y {c[2]:6.1f}→{c[3]:6.1f} (h={c[3]-c[2]:4.1f}pt) px={c[4]}')

# (c) tesseract multi-variantes sur strips
print()
print('===== (c) TESSERACT MULTI-VARIANTES =====')
for nom, pg, xa, ya, xb, yb in [('A1', 159, 40, 232, 600, 260),
                                 ('D2', 162, 40, 552, 600, 580),
                                 ('G1', 165, 40, 621, 600, 651)]:
    for scale in (1.0, 2.0):
        for binar in (False, True):
            img = strip(pg, xa, ya, xb, yb, scale, binar)
            for psm in (6, 13):
                r = tess(img, psm, f'{nom}-s{scale}-b{int(binar)}-p{psm}')
                if r:
                    print(f'{nom} ×{scale} bin={int(binar)} psm{psm}: {r}')
                else:
                    print(f'{nom} ×{scale} bin={int(binar)} psm{psm}: (vide)')
