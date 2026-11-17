#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — zooms pixel-précis (série Z) d'après cartographie TSV, leçon 22
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0px, y1px, x0px, x1px, tag, scale)
ZONES = [
    (120, 1600, 1800, 1200, 4300, 'Z01', 3),  # obj1 verbe [أعرف/أتعرف]
    (120, 1780, 1960, 1200, 4300, 'Z02', 3),  # obj2 أذكر فضل الإحسان إلى الحيوان
    (120, 5370, 5580, 700, 4300, 'Z03', 2),   # cadre L3: القتلة... فأحسنوا [الذبح/الذبحة]
    (123, 640, 980, 600, 4300, 'Z04', 2),     # re-quote p123 + من الإحسان في ذبح البهائم
    (121, 2400, 3150, 600, 4400, 'Z05', 2),   # zone الفهم: sous-en-tête? + gloss + استخلاص header
    (123, 5330, 5580, 3250, 3720, 'Z06', 5),  # ref [الرحمن: ٥٩/٦٠]
    (124, 3040, 3500, 3480, 3920, 'Z07', 5),  # ref [النساء: ٣٦]
    (124, 3950, 4250, 2800, 4400, 'Z08', 4),  # gloss 2 opener
    (124, 1540, 1720, 1470, 2900, 'Z09', 4),  # Q3 opener أبين بعض فوائد
    (122, 4810, 5120, 2700, 4300, 'Z10', 4),  # نهى أن [تصبر البهيمة/البهائم]
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
        for psm in ('7', '6'):
            r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', psm],
                               capture_output=True, text=True, env=env)
            t = r.stdout.strip().replace('\n', ' / ')
            if len(t) > len(best):
                best = t
        outs.append(f'{variant}: {best if best else "(vide)"}')
    print(f'◆ {tag} p{page} px y[{y0}-{y1}] x[{x0}-{x1}] ×{scale}')
    for o in outs:
        print(f'   {o}')
