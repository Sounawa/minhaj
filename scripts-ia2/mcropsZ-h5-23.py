#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — zooms étroits (série Z) pour tesseract psm 7/6, leçon 23 — points litigieux restants
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, psm)
Z = [
    (125, 0.040, 0.100, 0.30, 0.72, 'Z01', 7),   # numéro du bandeau الدرس
    (125, 0.095, 0.165, 0.20, 0.85, 'Z02', 7),   # titre du bandeau
    (125, 0.248, 0.285, 0.00, 1.00, 'Z03', 7),   # objectif 1
    (125, 0.330, 0.370, 0.00, 1.00, 'Z04', 7),   # objectif 3
    (125, 0.570, 0.600, 0.00, 1.00, 'Z05', 7),   # question نحافظ/نخالط
    (126, 0.655, 0.690, 0.00, 1.00, 'Z06', 7),   # glose 2 تمحها
    (126, 0.825, 0.860, 0.00, 1.00, 'Z07', 7),   # استنتاج Q2 (مخالقة)
    (127, 0.875, 0.910, 0.00, 1.00, 'Z08', 7),   # fin p127 (ويحافظ الإنسان بذلك...)
    (128, 0.120, 0.175, 0.00, 1.00, 'Z09', 6),   # cadre آية هود 114 ligne 1
    (128, 0.170, 0.215, 0.00, 1.00, 'Z10', 6),   # cadre آية ligne 2
    (128, 0.295, 0.335, 0.00, 1.00, 'Z11', 7),   # مكفرات + ref hadith أبي هريرة
    (128, 0.675, 0.712, 0.00, 1.00, 'Z12', 7),   # وكف الأذى / عدم الكذب
    (129, 0.100, 0.135, 0.00, 1.00, 'Z13', 7),   # محمدة وعبادة وتحصيل
    (129, 0.285, 0.320, 0.00, 1.00, 'Z14', 7),   # أحاسنكم أخلاقا
    (129, 0.540, 0.575, 0.00, 1.00, 'Z15', 7),   # يستفاد item 2 (يحقق فعاله?)
    (129, 0.585, 0.620, 0.00, 1.00, 'Z16', 7),   # يستفاد item 3 ligne 1
    (130, 0.215, 0.270, 0.05, 0.95, 'Z17', 6),   # آية آل عمران l.1
    (130, 0.265, 0.320, 0.05, 0.95, 'Z18', 6),   # آية l.2
    (130, 0.315, 0.405, 0.05, 0.95, 'Z19', 6),   # آية l.3-4
    (130, 0.555, 0.590, 0.00, 1.00, 'Z20', 7),   # activité 3
    (130, 0.705, 0.740, 0.00, 1.00, 'Z21', 7),   # إعداد قبلي item 1 suite (أخطاك...)
    (130, 0.755, 0.800, 0.00, 1.00, 'Z22', 7),   # إعداد قبلي a (تحدث عن معنى حفظ الله)
    (130, 0.835, 0.875, 0.00, 1.00, 'Z23', 7),   # إعداد قبلي 2-3
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, psm in Z:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    # upscale ×2 pour les bandes très fines
    if (y1 - y0) < 0.06:
        c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    p = f'{OUT}/z23-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', str(psm)],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}] psm{psm}:')
    print(f'   {txt if txt else "(vide)"}')
