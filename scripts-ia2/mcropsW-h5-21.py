#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-24 — recadrages MOT-NIVEAU natifs (série W) pour tesseract, zones pendantes.
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-21'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-ia2/tmp/tessdata'

# (page, y0, y1, x0, x1, tag)
ZONES = [
    (114, 0.528, 0.575, 0.36, 1.00, 'W01'),  # والشر بمثله. ودفعا لذلك فللشرع موقفًا (droite)
    (114, 0.528, 0.575, 0.00, 0.40, 'W02'),  # من الغضب يدفع به [X] الوخيمة في (gauche)
    (115, 0.262, 0.312, 0.00, 1.00, 'W03'),  # شرح item1 mot + début déf
    (115, 0.352, 0.402, 0.00, 1.00, 'W04'),  # شرح item3 (لا تغضب: ...)
    (115, 0.840, 0.885, 0.42, 0.85, 'W05'),  # [الظاهرة/المظهرة] لسمو بلاغته
    (116, 0.082, 0.122, 0.28, 0.75, 'W06'),  # ...بضبط [النفس/اللسان] وكظم
    (116, 0.152, 0.192, 0.00, 0.60, 'W07'),  # وعلى سبيلهم (ligne 3)
    (116, 0.750, 0.795, 0.35, 0.95, 'W08'),  # يزين [X] مع الغضب
    (116, 0.825, 0.865, 0.00, 0.70, 'W09'),  # من أقوى الحيل لدفع كيده
    (117, 0.122, 0.165, 0.30, 0.95, 'W10'),  # لا يخفى أن في كظم الغيظ [الثائر؟] عند
    (117, 0.155, 0.200, 0.00, 0.45, 'W11'),  # ...الغضب جماع الخير والفضل و[زكاة] الثمرات
    (117, 0.678, 0.722, 0.42, 1.00, 'W12'),  # ثمرة 4 opener (droite)
    (118, 0.443, 0.495, 0.25, 0.95, 'W13'),  # ...لهذا الصحابي [X] كلمتين أو ثلاث
    (119, 0.628, 0.678, 0.05, 0.95, 'W14'),  # إعداد قبلي item 2
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag in ZONES:
    im = Image.open(f'{R600}/p{page}.png').convert('L')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    for variant, img in (('raw', c), ('bin', c.point(lambda p: 255 if p > 150 else 0))):
        p = f'{OUT}/z21-{tag}-{variant}.png'
        img.save(p)
        best = ''
        for psm in ('7', '6'):
            r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', psm],
                               capture_output=True, text=True, env=env)
            t = r.stdout.strip().replace('\n', ' / ')
            if len(t) > len(best):
                best = t
        print(f'{tag}-{variant}: {best if best else "(vide)"}')
