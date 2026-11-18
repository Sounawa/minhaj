#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-38 — Round 3c : derniers recadrages serrés + tesseract ×4/×5 sur les zones récalcitrantes
import subprocess, os
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (nom, page, x0, y0, x1, y1, zoom, psms)
ZONES = [
    ('aydha3',    24, 215, 558, 400, 612, 5, [7, 6]),
    ('faqala',    24, 50, 645, 120, 670, 5, [7, 8]),
    ('dathur-dal',25, 400, 412, 490, 442, 5, [7, 8]),
    ('diag-centre2',27,195, 392, 442, 442, 4, [6]),
    ('diag-bleug2',27,110, 473, 310, 512, 5, [7, 6]),
    ('diag-sousd2',27,330, 508, 545, 585, 4, [6, 7]),
    ('diag-sousg2',27,100, 508, 315, 585, 4, [6, 7]),
    ('diag-lastr3',27,385, 660, 525, 745, 4, [6, 4]),
    ('t1-fin2',   28, 50, 108, 280, 150, 4, [7, 6]),
    ('cit-hadi2', 28, 55, 396, 570, 438, 4, [7, 6]),
    ('cit-ref4',  28, 170, 436, 570, 470, 4, [7, 6]),
]

os.makedirs(f'{DIR}/tcrops', exist_ok=True)
for nom, pg, x0, y0, x1, y1, z, psms in ZONES:
    S = 600/72.0
    im = Image.open(f'{DIR}/r600/p{pg}.png')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = c.resize((c.width*z, c.height*z), Image.LANCZOS)
    c.save(f'{DIR}/tcrops/t-{nom}.png')
    print(f'===== {nom} =====')
    for psm in psms:
        out = f'{DIR}/tcrops/t-{nom}-psm{psm}'
        subprocess.run(['tesseract', f'{DIR}/tcrops/t-{nom}.png', out, '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        txt = open(out + '.txt').read().strip().replace('\n', ' ⏎ ')
        print(f'  psm{psm}: {txt if txt else "(vide)"}')
    print()
