#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-28 — bandes W pleine largeur 600 dpi, leçon 24 (pp.131-137) + tesseract psm6
import os, subprocess
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-24'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm)
W = [
    (131, 0.225, 0.335, 0.02, 0.98, 'W01', 6),   # أهداف 3 lignes (verbe obj1)
    (131, 0.430, 0.565, 0.02, 0.98, 'W02', 6),   # تمهيد + question transition
    (131, 0.640, 0.870, 0.02, 0.98, 'W03', 6),   # cadre hadith complet + réf
    (132, 0.025, 0.310, 0.02, 0.98, 'W04', 6),   # cadre suite (رواية غير الترمذي + réf)
    (132, 0.330, 0.645, 0.02, 0.98, 'W05', 6),   # ترجمة الراوي
    (132, 0.715, 0.880, 0.02, 0.98, 'W06', 6),   # الفهم + الشرح 3 gloses
    (133, 0.065, 0.300, 0.02, 0.98, 'W07', 6),   # الشرح suite 5 gloses
    (133, 0.300, 0.535, 0.02, 0.98, 'W08', 6),   # استخلاص المضامين + 3 questions
    (133, 0.535, 0.665, 0.02, 0.98, 'W09', 6),   # bannière ? + يشتمل
    (133, 0.725, 0.905, 0.02, 0.98, 'W10', 6),   # أولاً + معناه + ولا يرك
    (134, 0.085, 0.365, 0.02, 0.98, 'W11', 6),   # ثمرات + الغار + فمن كان
    (134, 0.390, 0.685, 0.02, 0.98, 'W12', 6),   # ثانياً + الطلاق + فلا يلتجئ
    (134, 0.700, 0.885, 0.02, 0.98, 'W13', 6),   # فلا يكون همه + غافر
    (135, 0.070, 0.265, 0.02, 0.98, 'W14', 6),   # ثالثاً + واعلم أن الأمة
    (135, 0.250, 0.475, 0.02, 0.98, 'W15', 6),   # فيه تأكيد + يمنع تعلق
    (135, 0.470, 0.670, 0.02, 0.98, 'W16', 6),   # هذا ما أكده + ماتدم + رابعاً
    (135, 0.670, 0.885, 0.02, 0.98, 'W17', 6),   # قوله فيه + لنبلونكم
    (136, 0.035, 0.235, 0.02, 0.98, 'W18', 6),   # bloc coranique البقرة/الزمر + réfs
    (136, 0.230, 0.615, 0.02, 0.98, 'W19', 6),   # يستفاد items (لقمان)
    (136, 0.615, 0.885, 0.02, 0.98, 'W20', 6),   # تقويم Q1-Q3
    (137, 0.055, 0.465, 0.02, 0.98, 'W21', 6),   # cadre الأنعام + réf
    (137, 0.460, 0.900, 0.02, 0.98, 'W22', 6),   # activités + إعداد قبلي
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, psm in W:
    im = Image.open(f'{R600}/p{page}.png')
    W_, H_ = im.size
    c = im.crop((int(x0 * W_), int(y0 * H_), int(x1 * W_), int(y1 * H_)))
    p = f'{OUT}/z24-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}] psm{psm}:')
    print(f'   {txt if txt else "(vide)"}')
    print()
