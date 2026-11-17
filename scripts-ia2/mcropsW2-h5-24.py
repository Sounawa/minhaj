#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-28 — zooms W30-W43 supplémentaires (×4), tesseract nat+thr — leçon 24
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-24'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm, scale)
Z = [
    (132, 0.392, 0.428, 0.55, 0.98, 'W30', 7, 4),   # أحد الأعلام/العبادلة/العلماء
    (134, 0.215, 0.300, 0.02, 0.98, 'W31', 6, 3),   # فأنجاكم/ينجيكم + سابقة سبقت
    (134, 0.326, 0.360, 0.30, 0.98, 'W32', 7, 4),   # دنياه بإصلاح البال + أخراه بالإثابة
    (134, 0.572, 0.616, 0.02, 0.98, 'W33', 6, 4),   # verset الطلاق + chiffre
    (134, 0.630, 0.674, 0.02, 0.98, 'W34', 7, 4),   # والتجأ إلى من لا ...
    (134, 0.812, 0.866, 0.02, 0.98, 'W35', 6, 4),   # verset غافر + queue + chiffre
    (135, 0.423, 0.468, 0.02, 0.98, 'W36', 6, 4),   # سبحانه ? + يثمر عدم تعلق
    (136, 0.122, 0.158, 0.15, 0.75, 'W37a', 7, 4),  # réf البقرة digits
    (136, 0.158, 0.188, 0.25, 0.95, 'W37b', 7, 4),  # verset الزمر + réf digit
    (136, 0.270, 0.304, 0.30, 0.98, 'W38', 7, 4),   # فليجمل
    (136, 0.750, 0.818, 0.02, 0.98, 'W39', 6, 4),   # Q3 ouverture + queue
    (137, 0.158, 0.270, 0.03, 0.97, 'W40', 6, 2.5), # الأنعام cadre part 1
    (137, 0.255, 0.412, 0.03, 0.97, 'W41', 6, 2.5), # الأنععام cadre part 2
    (137, 0.386, 0.410, 0.15, 0.85, 'W42', 7, 4),   # réf الأنعام digits
    (137, 0.790, 0.835, 0.45, 0.98, 'W43', 7, 4),   # الأولى/الأولي
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
def tess(path, psm):
    r = subprocess.run(['tesseract', path, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    return ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())

for page, y0, y1, x0, x1, tag, psm, scale in Z:
    im = Image.open(f'{R600}/p{page}.png').convert('L')
    W_, H_ = im.size
    c = im.crop((int(x0 * W_), int(y0 * H_), int(x1 * W_), int(y1 * H_)))
    if scale != 1:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    p0 = f'{OUT}/z24-{tag}.png'
    c.save(p0)
    p2 = f'{OUT}/z24-{tag}-t.png'
    c.point(lambda v: 255 if v > 150 else 0).save(p2)
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}] ×{scale}:')
    for lab, pp in (('nat', p0), ('thr', p2)):
        t = tess(pp, psm)
        print(f'   [{lab}] {t if t else "(vide)"}')
    print()
