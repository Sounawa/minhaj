#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — zooms W ultra-étroits ×3 (points litigieux finaux), leçon 23
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm)
W = [
    (125, 0.322, 0.372, 0.00, 1.00, 'W01', 7),   # objectif 3 complet
    (126, 0.655, 0.705, 0.00, 1.00, 'W02', 7),   # glose تمحها (2 verbes)
    (128, 0.118, 0.180, 0.00, 1.00, 'W03', 6),   # cadre هود ligne(s)
    (129, 0.538, 0.582, 0.00, 1.00, 'W05', 7),   # يستفاد item 2 (تفاعل الناس?)
    (129, 0.280, 0.322, 0.00, 1.00, 'W06', 7),   # أحاسنكم + ref
    (130, 0.468, 0.512, 0.00, 1.00, 'W07', 7),   # activité 1 (متقين/منافقين)
    (130, 0.578, 0.640, 0.00, 1.00, 'W08', 6),   # الأعمال التطبيقية ?
    (130, 0.698, 0.758, 0.00, 1.00, 'W09', 6),   # item1 suite : extrait hadith
    (130, 0.795, 0.880, 0.00, 1.00, 'W10', 6),   # items 2-3 (أشرح/أبين)
    (130, 0.208, 0.252, 0.05, 0.95, 'W11', 7),   # آية 133 : سابقوا/سارعوا
    (130, 0.355, 0.412, 0.05, 0.95, 'W12', 6),   # آية 135-136 fin + ref
    (125, 0.030, 0.098, 0.25, 0.78, 'W13', 7),   # numéro bandeau (2e essai)
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, psm in W:
    im = Image.open(f'{R600}/p{page}.png')
    W_, H_ = im.size
    c = im.crop((int(x0 * W_), int(y0 * H_), int(x1 * W_), int(y1 * H_)))
    c = c.resize((c.width * 3, c.height * 3), Image.LANCZOS)
    p = f'{OUT}/z23-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}] psm{psm}:')
    print(f'   {txt if txt else "(vide)"}')
