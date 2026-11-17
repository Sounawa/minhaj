#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — zooms ultimes ×6 COULEUR (série V) : الذبحة, gloss2 opener, Q3 opener
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0px, y1px, x0px, x1px, tag, scale)
ZONES = [
    (123, 680, 900, 1500, 2500, 'V01', 6),   # re-quote: فأحسنوا [الذبح/الذبحة]
    (124, 3960, 4160, 3950, 4460, 'V02', 6), # gloss2 opener (couleur)
    (124, 1560, 1800, 3200, 4200, 'V03', 6), # Q3 opener (couleur)
    (120, 5390, 5570, 2000, 2800, 'V04', 6), # cadre L3 mot [الذبح/الذبحة] (couleur)
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, scale in ZONES:
    im = Image.open(f'{R600}/p{page}.png')  # couleur
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    g = c.convert('L')
    outs = []
    for variant, img in (('raw', g), ('b120', g.point(lambda p: 255 if p > 120 else 0)),
                         ('b150', g.point(lambda p: 255 if p > 150 else 0))):
        p = f'{OUT}/z22-{tag}-{variant}.png'
        img.save(p)
        best = ''
        for psm in ('7', '8', '13'):
            r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', psm],
                               capture_output=True, text=True, env=env)
            t = r.stdout.strip().replace('\n', ' / ')
            if len(t) > len(best):
                best = t
        outs.append(f'{variant}: {best if best else "(vide)"}')
    print(f'◆ {tag} p{page} px y[{y0}-{y1}] x[{x0}-{x1}] ×{scale}')
    for o in outs:
        print(f'   {o}')
