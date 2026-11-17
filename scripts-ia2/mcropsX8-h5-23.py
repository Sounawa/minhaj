#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — X8/X9/X10 : trois derniers points, zooms maximaux
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm, upscale)
Z = [
    (128, 0.105, 0.150, 0.02, 0.98, 'X08a', 7, 2),   # cadre هود : ligne intro/verset 1
    (128, 0.145, 0.185, 0.02, 0.98, 'X08b', 7, 2),   # cadre هود : ligne verset 2 + ref
    (130, 0.700, 0.758, 0.00, 1.00, 'X09', 6, 2),    # item1 sous-item (extrait hadith)
    (130, 0.208, 0.258, 0.38, 0.82, 'X10', 7, 3),    # آية 133 premier mot ×3
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, psm, up in Z:
    im = Image.open(f'{R600}/p{page}.png')
    IW, IH = im.size
    c = im.crop((int(x0 * IW), int(y0 * IH), int(x1 * IW), int(y1 * IH)))
    c = c.resize((c.width * up, c.height * up), Image.LANCZOS)
    p = f'{OUT}/z23-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}] psm{psm} ×{up}:')
    print(f'   {txt if txt else "(vide)"}')
