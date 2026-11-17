#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — recadrages LIGNE NATIVE (série L) pour tesseract, leçon 22 (pp.120-124)
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, invert)
CROPS = [
    (120, 0.235, 0.350, 0.00, 1.00, 'L01', False),  # أهداف 3 lignes
    (120, 0.415, 0.565, 0.00, 1.00, 'L02', False),  # تمهيد 4 lignes
    (120, 0.565, 0.615, 0.00, 1.00, 'L03', False),  # question تمهيد (تحسن/نحسن)
    (120, 0.640, 0.880, 0.00, 1.00, 'L04', True),   # cadre hadith INVERSÉ
    (120, 0.640, 0.880, 0.00, 1.00, 'L04r', False), # cadre hadith brut (contrôle)
    (121, 0.085, 0.300, 0.00, 1.00, 'L05', True),   # cadre ترجمة الراوي INVERSÉ
    (121, 0.085, 0.300, 0.00, 1.00, 'L05r', False), # cadre rāwī brut
    (121, 0.380, 0.600, 0.00, 1.00, 'L06', False),  # الفهم + استخلاص Q1 Q2
    (121, 0.650, 0.725, 0.00, 1.00, 'L07', False),  # تحليل intro
    (121, 0.755, 0.925, 0.00, 1.00, 'L08', False),  # أولا + معناه أن الإحسان + وكلمة شيء
    (122, 0.035, 0.140, 0.00, 1.00, 'L09', False),  # في العبادات + جبريل début
    (122, 0.255, 0.300, 0.00, 1.00, 'L10', False),  # رحم الله رجلا سمحا + ref
    (122, 0.590, 0.665, 0.00, 1.00, 'L11', False),  # الصحابة سألوه + ذات كبد + الموطأ
    (122, 0.665, 0.760, 0.00, 1.00, 'L12', False),  # تعذيبها + حديث أنس + تصبر
    (122, 0.780, 0.850, 0.00, 1.00, 'L13', False),  # هرة hadith + ref
    (123, 0.095, 0.290, 0.00, 1.00, 'L14', False),  # قوله ﷺ + ذبح détails
    (123, 0.305, 0.365, 0.00, 1.00, 'L15', False),  # وكما يطلب الإحسان + أفاعي
    (123, 0.360, 0.480, 0.00, 1.00, 'L16', False),  # ZONE : fin sentence + en-tête liste + item 1
    (123, 0.470, 0.560, 0.00, 1.00, 'L17', False),  # item 2 + item 3 début
    (123, 0.555, 0.695, 0.00, 1.00, 'L18', False),  # items 3-4 (جار + والدین)
    (123, 0.695, 0.805, 0.00, 1.00, 'L19', False),  # أن المحسن + هل جزاء + ref الرحمن
    (123, 0.825, 0.890, 0.00, 1.00, 'L20', False),  # أن الإحسان مبدأ
    (124, 0.085, 0.260, 0.00, 1.00, 'L21', False),  # en-tête تقويم? + Q1 Q2 Q3
    (124, 0.285, 0.500, 0.00, 1.00, 'L22', False),  # استثمار header + āya + ref
    (124, 0.545, 0.615, 0.00, 1.00, 'L23', False),  # glosses 1-2
    (124, 0.640, 0.810, 0.00, 1.00, 'L24', False),  # إعداد قبلي + items
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, inv in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if inv:
        c = ImageOps.invert(c.convert('L'))
    p = f'{OUT}/z22-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', '6'],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    mark = ' INV' if inv else ''
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}]{mark}:')
    print(f'   {txt if txt else "(vide)"}')
