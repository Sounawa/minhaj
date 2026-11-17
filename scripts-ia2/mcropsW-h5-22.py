#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — recadrages MOT-NIVEAU (série W) binarisés, leçon 22 — adjudications fines
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, invert)
ZONES = [
    (120, 0.415, 0.470, 0.45, 1.00, 'W01', False),  # جاء الإسلام رحمة لكل المخلوقات من إنسان وحيوان فشُرِّعَ
    (120, 0.565, 0.615, 0.00, 0.55, 'W02', False),  # وكيف [تُحسن/نُحسن] إلى الحيوان؟
    (120, 0.765, 0.800, 0.50, 1.00, 'W03', False),  # القتلة وإذا ذبحتم فأحسنوا [الذبح/الذبحة]
    (120, 0.640, 0.685, 0.30, 0.80, 'W04', False),  # bannière الحديث
    (120, 0.640, 0.685, 0.30, 0.80, 'W04i', True),  # idem inversé
    (121, 0.190, 0.250, 0.00, 1.00, 'W05', False),  # روى عن النبي ﷺ [خمسين حديثا؟]
    (121, 0.380, 0.412, 0.25, 1.00, 'W06', False),  # كتب الإحسان: فرض الإتقان وشرعه
    (121, 0.838, 0.875, 0.00, 0.80, 'W07', False),  # وكلمة شيء من أنكر النكرات لا يخرج عنها أي عمل
    (122, 0.672, 0.700, 0.25, 0.90, 'W08', False),  # [تعذيبها/تغذيها] + حديث [أنس؟]
    (122, 0.712, 0.752, 0.25, 0.95, 'W09', False),  # نهى أن تُصبر البهيمة + ref
    (122, 0.820, 0.845, 0.00, 0.60, 'W10', False),  # خشاش الأرض حتى ماتت + ref ابن ماجة
    (123, 0.330, 0.362, 0.00, 1.00, 'W11', False),  # أو التي [نزل/ينقل] بها بعض الأمراض يستحيل برؤها
    (123, 0.098, 0.148, 0.00, 0.55, 'W12', False),  # قوله ﷺ + من الإحسان في ذبح البهائم
    (123, 0.775, 0.802, 0.50, 0.90, 'W13', False),  # ref [الرحمن: 60/59]
    (123, 0.752, 0.790, 0.15, 0.80, 'W14', False),  # آية هل جزاء الإحسان إلا الإحسان
    (124, 0.222, 0.272, 0.00, 1.00, 'W15', False),  # Q3 تقويم complète
    (124, 0.578, 0.607, 0.00, 1.00, 'W16', False),  # gloss 2 opener (الجار)
    (124, 0.718, 0.745, 0.00, 1.00, 'W17', False),  # إعداد item 1: اتق الله تمحها وخالق الناس
    (123, 0.128, 0.152, 0.50, 1.00, 'W18', False),  # بأن [يتقن/ينقن] الذابح ذلك ويتجنب التعذيب
    (123, 0.165, 0.190, 0.10, 0.65, 'W19', False),  # فلا يصرعها [بغتة] ولا يجرها من موضع إلى موضع
    (122, 0.596, 0.616, 0.35, 0.85, 'W20', False),  # وإن لنا في [البهائم] لأجرا؟
    (120, 0.240, 0.300, 0.10, 1.00, 'W21', False),  # أهداف obj1-2 (أعرف/أذكر)
    (120, 0.278, 0.305, 0.10, 1.00, 'W22', False),  # obj3 أتمثل مقاصد الأمر
    (123, 0.308, 0.335, 0.30, 1.00, 'W23', False),  # وكما يطلب الإحسان في ذبح بهيمة الأنعام
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, inv in ZONES:
    im = Image.open(f'{R600}/p{page}.png').convert('L')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if inv:
        c = ImageOps.invert(c)
    results = []
    for variant, img in (('raw', c), ('b120', c.point(lambda p: 255 if p > 120 else 0)),
                         ('b150', c.point(lambda p: 255 if p > 150 else 0)),
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
        results.append(f'{variant}: {best if best else "(vide)"}')
    print(f'◆ {tag} p{page} y[{y0:.3f}-{y1:.3f}] x[{x0:.2f}-{x1:.2f}]')
    for r in results:
        print(f'   {r}')
