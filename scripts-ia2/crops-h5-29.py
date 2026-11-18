#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — recadrages ciblés 1200 dpi natifs (leçon 29, bibliographie pp.159-166) :
#  A: p159 entrée القرآن — que suit «المصحف» ? (gap 79.4 anormal → ligne cachée ?)
#  B: p159 entrée 4 — الأزدي puis date de mort ? (cmap «›» seul)
#  C: p160 entrée 7 — header السنن الكبرى : «الخسروجردي» présent ? (ligne sautée par tesseract)
#  D: p162 gap 94.6 pt entre entrées 19/20 — rubrique décorative invisible (cmap+tess) ?
#  E: p163 entrée 26 — date de mort de العيني («855ه» ? cmap ne voit que «5»)
#  F: p163 entrée 21 — nasab الهيتمي («أحمد بن محمد بن علي بن حجر» ?)
#  G: p165 gap 72.9 pt sous «مراجع أخرى:» — header de l'entrée 37 manquant
# Convention : bbox en points PDF (page 637.2x807.12) ; r1200 => ×1200/72 = 16.6667
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h5-29'
S = 1200 / 72.0

zones = [
    # (page, nom, x0,y0,x1,y1 en points)
    (159, 'A-quran-suite',   40, 198, 600, 292),
    (159, 'B-abudawud-date', 35, 636, 300, 675),
    (160, 'C-sunan-kubra',   40, 238, 600, 270),
    (162, 'D-gap-rubrique',  40, 498, 600, 598),
    (163, 'E-ayni-date',    420, 684, 600, 720),
    (163, 'F-haytami-nasab', 40,  70, 600, 110),
    (165, 'G-entree37',      40, 572, 600, 652),
]

for p, nom, x0, y0, x1, y1 in zones:
    im = Image.open(f'{D}/r1200/p{p}.png')
    box = (int(x0*S), int(y0*S), int(x1*S), int(y1*S))
    crop = im.crop(box)
    out = f'{D}/crops/{nom}.png'
    os.makedirs(f'{D}/crops', exist_ok=True)
    crop.save(out)
    print(nom, crop.size)
