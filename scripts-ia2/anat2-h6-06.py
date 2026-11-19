#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — anatomie ciblée : point au-dessus de la boucle ṣād/ḍād dans إصلاح (p39),
# point au-dessus du dāl dans البذل/البدل (p38), et première lettre de ن/ذفرة (p38).
# Témoins de contrôle : صفات (ص, p38), اتضح (ض, p36).
import numpy as np
from PIL import Image, ImageOps
from scipy import ndimage

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
S = 1200 / 72.0

def word_anatomy(pg, y0, y1, x0, x1, tag, loop_hint=None):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = ImageOps.autocontrast(c)
    a = np.array(c)
    H, W = a.shape
    ink = a < max(a.mean() - 1.2*a.std(), 110)
    lab, n = ndimage.label(ink)
    comps = []
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if len(ys) < 3:
            continue
        comps.append({'n': len(ys), 'x0': int(xs.min()), 'x1': int(xs.max()),
                      'y0': int(ys.min()), 'y1': int(ys.max())})
    print(f'===== {tag} ({W}x{H}px) =====')
    # corps principal = plus grande composante
    comps.sort(key=lambda z: -z['n'])
    body = comps[0]
    bh = body['y1'] - body['y0']
    print(f"  CORPS principal: x[{body['x0']}-{body['x1']}] y[{body['y0']}-{body['y1']}] h={bh}px n={body['n']}")
    # petites composantes = points/voyelles ; classer DESSUS/DESSOUS par rapport au corps
    for cc in comps[1:14]:
        rel = 'AU-DESSUS du corps' if cc['y1'] < body['y0'] + 0.25*bh else (
              'DESSOUS' if cc['y0'] > body['y1'] - 0.2*bh else 'dans/contre le corps')
        posx = 'droite' if cc['x0'] > body['x0'] + 0.66*(body['x1']-body['x0']) else (
               'gauche' if cc['x1'] < body['x0'] + 0.33*(body['x1']-body['x0']) else 'centre')
        print(f"  x[{cc['x0']:>4}-{cc['x1']:>4}] y[{cc['y0']:>3}-{cc['y1']:>3}] {cc['n']:>4}px {rel:<20} {posx}")

# إصلاح occurrences p39 (ligne y446-472) : mots ~x330-410 (1er) et x100-180 (2e)
# cible serrée sur le mot seul
word_anatomy(39, 449, 471, 340, 400, 'islah-1 (premier إصلاح)')
word_anatomy(39, 449, 471, 95, 165, 'islah-2 (second لإصلاح)')
# témoin ص : صفات p38 y405-432 (mot ~ x150-230)
word_anatomy(38, 407, 433, 145, 235, 'TEMOIN صفات (ص)')
# témoin ض : اتضح p36 y363-390 (mot ~ x200-260)
word_anatomy(36, 364, 391, 195, 265, 'TEMOIN اتضح (ض)')
# البذل/البدل p38 y409-436 : mot ~ x345-415
word_anatomy(38, 410, 436, 340, 420, 'badl (البذل/البدل)')
# ن/ذفرة p38 y622-650 : mot ~ x296-348
word_anatomy(38, 622, 652, 292, 352, 'nafra (ن/ذ/زفرة)')
# قابل X بينهما p38 y705-735 : mot ~ x432-470
word_anatomy(38, 706, 736, 428, 474, 'qabil-X')
# محاولة/محاورة : lettre entre و-ا et ة (r ou l) p38 y383-408
word_anatomy(38, 383, 409, 255, 340, 'muhawara-mot')
