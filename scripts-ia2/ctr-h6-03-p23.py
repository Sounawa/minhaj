#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-37 — tesseract sur recadrages CONTRASTÉS des lignes p.23 الاستثمار (méthode Z2-35 :
# contraste ×2.5 + psm 7/13 tranche là où tout le reste échoue). Bin fork: 3 seuils.
from PIL import Image, ImageOps
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0

im = Image.open(f'{DIR}/r1200/p23.png').convert('L')

# lignes (marges généreuses, diacritiques inclus)
LINES = {
    'A': (40, 122, 610, 152),
    'B': (40, 148, 610, 178),
    'C': (40, 178, 610, 206),
    'D': (40, 198, 610, 226),
}

os.makedirs(f'{DIR}/crops/ctr', exist_ok=True)
for nom, (x0, y0, x1, y1) in LINES.items():
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    # contraste x2.5 (méthode Z2-35) puis 3 binarisations
    lo, hi = c.getextrema()
    ctr = c.point(lambda v: max(0, min(255, int((v - 127.5) * 2.5 + 127.5))))
    big = ctr.resize((ctr.width, ctr.height * 2), Image.LANCZOS)  # étirement vertical x2
    for tag, img in (('ctr', ctr), ('big', big)):
        fp = f'{DIR}/crops/ctr/p23-{nom}-{tag}.png'
        img.save(fp)
        for psm in (7, 13):
            out = f'{DIR}/ctr-p23-{nom}-{tag}-psm{psm}'
            if os.path.exists(out + '.txt'):
                continue
            subprocess.run(['tesseract', fp, out, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], check=True, capture_output=True)
            t = open(out + '.txt').read().strip()
            if t:
                print(f'== {nom}/{tag} psm{psm}: {t[:220]}')
print('done')
