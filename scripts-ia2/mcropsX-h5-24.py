#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-28 — zooms X étroits multi-seuils (points litigieux restants), leçon 24 — tesseract ×3 variantes
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-24'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm)
X = [
    (131, 0.230, 0.272, 0.10, 0.95, 'X01', 6),   # verbe objectif 1
    (131, 0.524, 0.558, 0.05, 0.98, 'X02', 7),   # fin question transition
    (131, 0.822, 0.855, 0.05, 0.98, 'X03', 7),   # réf [سنن الترمذي] + جفت الصحف
    (131, 0.648, 0.705, 0.05, 0.98, 'X04', 6),   # sanad كنت خلف + يوما فقال
    (132, 0.385, 0.428, 0.05, 0.98, 'X05', 6),   # أحد العلماء/العبادلة + مناقبه أكثر
    (133, 0.082, 0.115, 0.05, 0.98, 'X06', 7),   # جفت الصحف gloss (قدر/قدره الله)
    (133, 0.198, 0.232, 0.05, 0.98, 'X06b', 7),  # لن/أن يصيبك أبدا
    (133, 0.815, 0.850, 0.05, 0.98, 'X08', 7),   # ولا يرك في مخالفته
    (134, 0.202, 0.258, 0.05, 0.98, 'X09', 6),   # ينجيكم؟ + فذكر كل واحد + فانفرجت
    (134, 0.318, 0.360, 0.05, 0.98, 'X10', 7),   # دنياه بإصلاح البال + إثابة
    (134, 0.522, 0.578, 0.05, 0.98, 'X11', 6),   # وأن لا يعزل؟ + ما قل منها
    (134, 0.636, 0.672, 0.05, 0.98, 'X13', 7),   # والتجأ إلى من لا ...
    (134, 0.703, 0.752, 0.05, 0.98, 'X14', 6),   # فلا تكن/تتوجه رجاء ورغبة
    (135, 0.278, 0.322, 0.05, 0.98, 'X17', 6),   # التي تثمر أن لا يخاف + متيقن
    (135, 0.358, 0.400, 0.05, 0.98, 'X18', 6),   # فلو اجتمعت... ما قدرت
    (135, 0.422, 0.470, 0.05, 0.98, 'X19', 6),   # يثمر عدم تعلق + الفاعل
    (135, 0.808, 0.852, 0.05, 0.98, 'X20', 6),   # معرضون/يكلفون للمصائب
    (136, 0.262, 0.335, 0.05, 0.98, 'X22', 6),   # item1 يقين + لقمان début
    (136, 0.398, 0.438, 0.05, 0.98, 'X23', 7),   # [لقمان: 15/16] digit
    (136, 0.752, 0.842, 0.05, 0.98, 'X24', 6),   # تقويم Q3 fin
    (137, 0.738, 0.885, 0.05, 0.98, 'X28', 6),   # إعداد قبلي items
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
def tess(path, psm):
    r = subprocess.run(['tesseract', path, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    return ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())

for page, y0, y1, x0, x1, tag, psm in X:
    im = Image.open(f'{R600}/p{page}.png').convert('L')
    W_, H_ = im.size
    c = im.crop((int(x0 * W_), int(y0 * H_), int(x1 * W_), int(y1 * H_)))
    p0 = f'{OUT}/z24-{tag}.png'
    c.save(p0)
    # variante 2 : contraste dur
    p2 = f'{OUT}/z24-{tag}-t.png'
    c.point(lambda v: 255 if v > 150 else 0).save(p2)
    # variante 3 : ×2
    p3 = f'{OUT}/z24-{tag}-x2.png'
    c.resize((c.width * 2, c.height * 2), Image.LANCZOS).save(p3)
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}]:')
    for lab, pp in (('nat', p0), ('thr', p2), ('x2', p3)):
        t = tess(pp, psm)
        print(f'   [{lab}] {t if t else "(vide)"}')
    print()
