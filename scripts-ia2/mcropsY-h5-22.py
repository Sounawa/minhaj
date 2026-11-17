#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — zooms fins Y (dernière vague) : verbes أهداف, openers glosses/Q3, mot الذبح/الذبحة
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0px, y1px, x0px, x1px, tag, scale)
ZONES = [
    (120, 1790, 1950, 3300, 4100, 'Y01', 5),  # obj1 verbe أن [أعرف/أتعرف]
    (120, 2030, 2200, 1400, 4300, 'Y02', 4),  # obj2 أذكر فضل الإحسان إلى الحيوان
    (120, 2280, 2450, 1000, 4300, 'Y03', 4),  # obj3 أتمثل مقاصد الأمر
    (124, 3975, 4150, 3050, 4400, 'Y04', 5),  # gloss2 opener [؟] معنى الجار
    (124, 1530, 1840, 1400, 2100, 'Y05', 5),  # Q3 opener أبين بعض فوائد
    (121, 2350, 2680, 2200, 3400, 'Y06', 4),  # sous-en-tête الفهم ?
    (123, 653, 790, 1500, 2900, 'Y07', 5),    # re-quote: فأحسنوا [الذبح/الذبحة]
    (120, 5390, 5580, 1500, 3000, 'Y08', 4),  # cadre L3 mot [الذبح/الذبحة]
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, scale in ZONES:
    im = Image.open(f'{R600}/p{page}.png').convert('L')
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    outs = []
    for variant, img in (('raw', c), ('b150', c.point(lambda p: 255 if p > 150 else 0)),
                         ('b180', c.point(lambda p: 255 if p > 180 else 0))):
        p = f'{OUT}/z22-{tag}-{variant}.png'
        img.save(p)
        best = ''
        for psm in ('7', '6', '13'):
            r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', psm],
                               capture_output=True, text=True, env=env)
            t = r.stdout.strip().replace('\n', ' / ')
            if len(t) > len(best):
                best = t
        outs.append(f'{variant}: {best if best else "(vide)"}')
    print(f'◆ {tag} p{page} px y[{y0}-{y1}] x[{x0}-{x1}] ×{scale}')
    for o in outs:
        print(f'   {o}')
