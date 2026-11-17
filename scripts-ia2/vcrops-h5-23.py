#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — recadrages VLM (série V) 600 dpi : zones où tesseract échoue (bandeaux décorés, cadres)
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
R600 = f'{OUT}/r600'

# (page, y0, y1, x0, x1, tag)
V = [
    (125, 0.025, 0.175, 0.00, 1.00, 'V01'),  # bandeau الدرس + numéro + titre
    (125, 0.235, 0.380, 0.00, 1.00, 'V02'),  # أهداف 3 lignes
    (125, 0.555, 0.610, 0.00, 1.00, 'V03'),  # question نحافظ/نخالط
    (126, 0.615, 0.730, 0.00, 1.00, 'V04'),  # الشرح 3 gloses
    (128, 0.110, 0.225, 0.00, 1.00, 'V05'),  # cadre آية [هود: 114]
    (128, 0.650, 0.735, 0.00, 1.00, 'V06'),  # وكف الأذى / عدم الكذب
    (129, 0.415, 0.770, 0.00, 1.00, 'V07'),  # ومما يستفاد complet (items + numéros)
    (130, 0.125, 0.475, 0.00, 1.00, 'V08'),  # cadre آية [آل عمران: 133-136]
    (130, 0.455, 0.655, 0.00, 1.00, 'V09'),  # 3 activités numérotées
    (130, 0.615, 0.915, 0.00, 1.00, 'V10'),  # الإعداد القبلي complet
]

for page, y0, y1, x0, x1, tag in V:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    # downsample si trop large (limite VLM) : max 1600px de large
    if c.width > 1600:
        r = 1600 / c.width
        c = c.resize((1600, int(c.height * r)), Image.LANCZOS)
    c.save(f'{OUT}/z23-{tag}.png')
    print(f'{tag} p{page} {c.width}x{c.height} OK')
