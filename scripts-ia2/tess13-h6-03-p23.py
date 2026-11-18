#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-37 — tesseract psm 7/13 sur recadrages 1200 dpi des lignes LA-LD de p.23 (الاستثمار)
# (méthode Z2-34 : psm13 brut sur lignes moucharabieh — les identités cmap sont en défaut,
#  seule la convergence multi-outils tranche)
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03'
TESS = '/home/z/my-project/scripts-translate/tessdata'

LINES = {
    'LA': (40, 125, 610, 152),
    'LB': (40, 146, 610, 178),
    'LC': (40, 177, 610, 205),
    'LD': (40, 195, 610, 226),
}
S = 1200 / 72.0
from PIL import Image
im = Image.open(f'{DIR}/r1200/p23.png')
for nom, (x0, y0, x1, y1) in LINES.items():
    fp = f'{DIR}/crops/t13-p23-{nom}.png'
    im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))).save(fp)
    for psm in (7, 13):
        out = f'{DIR}/t13-p23-{nom}-psm{psm}'
        if os.path.exists(out + '.txt'):
            continue
        subprocess.run(['tesseract', fp, out, '-l', 'ara', '--tessdata-dir', TESS,
                        '--psm', str(psm)], check=True, capture_output=True)
        print(f'== {nom} psm{psm} ==')
        print(open(out + '.txt').read().strip()[:400])
        print()
