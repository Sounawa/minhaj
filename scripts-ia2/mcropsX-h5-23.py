#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — zooms X natifs 600 dpi (pas de downsample) : arbitrages finaux
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm)
X = [
    (125, 0.025, 0.170, 0.05, 0.95, 'X01', 6),   # bandeau complet : numéro + titre
    (125, 0.318, 0.375, 0.00, 1.00, 'X02', 7),   # objectif 3
    (126, 0.650, 0.710, 0.00, 1.00, 'X03', 7),   # glose تمحها
    (128, 0.100, 0.240, 0.00, 1.00, 'X04', 6),   # cadre هود complet
    (130, 0.460, 0.520, 0.00, 1.00, 'X05', 7),   # activité 1 fin (متقين?)
    (130, 0.695, 0.760, 0.00, 1.00, 'X06', 6),   # item1 suite : extrait hadith
    (130, 0.205, 0.258, 0.30, 0.85, 'X07', 7),   # آية 133 premier mot
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, psm in X:
    im = Image.open(f'{R600}/p{page}.png')
    IW, IH = im.size
    c = im.crop((int(x0 * IW), int(y0 * IH), int(x1 * IW), int(y1 * IH)))
    p = f'{OUT}/z23-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}] psm{psm} {c.width}x{c.height}:')
    print(f'   {txt if txt else "(vide)"}')
