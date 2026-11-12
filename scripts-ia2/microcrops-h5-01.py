#!/usr/bin/env python3
# Z2-1 — micro-crops ciblés (bandes de lignes contestées), 150 dpi rendu → ×2.5
from PIL import Image
import os
SRC = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01'
# (page, y0%, y1%, nom)
bands = [
    ('013', 0.06, 0.34, 'obj-tamhid'),      # objectifs + tamhîd
    ('014', 0.02, 0.30, 'fahm-gloses'),     # rubrique + gloses + استخلاص + التحليل intro
    ('014', 0.72, 1.00, 'bio-fin'),         # dernières lignes bio Nawawî
    ('015', 0.00, 0.20, 'maitres'),         # professeurs + élèves
    ('015', 0.55, 0.85, 'daqiq-birth'),     # nisba + naissance Ibn Daqîq
    ('015', 0.80, 1.00, 'daqiq-oeuvres'),   # œuvres + mort
    ('016', 0.00, 0.40, 'bul123'),          # puces 1-3
    ('016', 0.28, 0.62, 'hadith'),          # hadith + riwâyât
    ('016', 0.58, 0.97, 'bul5-stefade'),    # puce 5 + المستفاد
    ('017', 0.22, 0.66, 'box-stithmar'),    # encadré الاستثمار
]
for pg, a, b, name in bands:
    im = Image.open(f'{SRC}/p-{pg}.png')
    w, h = im.size
    part = im.crop((0, int(h*a), w, int(h*b)))
    up = part.resize((int(part.width*2.5), int(part.height*2.5)), Image.LANCZOS)
    up.save(f'{SRC}/m-{name}.png')
    print(name, up.size, os.path.getsize(f'{SRC}/m-{name}.png'))
