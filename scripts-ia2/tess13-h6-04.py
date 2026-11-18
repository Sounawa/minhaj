#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-38 — tesseract sur recadrages grossis ×3 (zones dures : diagramme p27, glose دثور p25,
# mot disputé وتجنب/وتحذير p26, cela أنّه/أنّهم p26, أيضاً p24, fin hadith p24)
import subprocess, os
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04'
TESS = '/home/z/my-project/scripts-translate/tessdata'

ZONES = [
    # (nom, page, x0, y0, x1, y1, psm)
    ('dathur',   25, 140, 405, 570, 450, 6),
    ('dathur-w', 25, 300, 408, 500, 445, 7),
    ('irshad-w', 26, 55, 655, 300, 690, 7),
    ('dhalika-w',26, 380, 392, 565, 422, 7),
    ('aydha',    24, 360, 565, 570, 605, 7),
    ('hadith-l3',24, 55, 660, 605, 700, 6),
    ('diag-title',27, 55, 370, 605, 465, 6),
    ('diag-bleus',27, 55, 455, 605, 590, 6),
    ('diag-jaunes',27,55, 545, 605, 645, 6),
    ('diag-lastr',27, 300, 655, 605, 750, 6),
    ('diag-lastl',27, 55, 655, 320, 750, 6),
    ('tamhid-l2',24, 55, 370, 605, 420, 6),
]

os.makedirs(f'{DIR}/tcrops', exist_ok=True)
for nom, pg, x0, y0, x1, y1, psm in ZONES:
    S = 600/72.0
    im = Image.open(f'{DIR}/r600/p{pg}.png')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = c.resize((c.width*3, c.height*3), Image.LANCZOS)
    fp = f'{DIR}/tcrops/t-{nom}.png'
    c.save(fp)
    out = f'{DIR}/tcrops/t-{nom}-psm{psm}'
    subprocess.run(['tesseract', fp, out, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], check=True, capture_output=True)
    txt = open(out + '.txt').read().strip()
    print(f'===== {nom} (psm{psm}) =====')
    print(txt if txt else '(vide)')
    print()
