#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-25 — recadrages ÉTROITS (série N) ×3-×5, leçon 22 — adjudications lettre-niveau
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, scale, invert)
ZONES = [
    (120, 0.238, 0.270, 0.55, 0.95, 'N01', 4, False),  # obj1 verbe [أعرف/أتعرف]
    (120, 0.280, 0.306, 0.10, 0.60, 'N02', 3, False),  # obj3 أتمثل مقاصد الأمر
    (120, 0.782, 0.822, 0.30, 1.00, 'N03', 3, False),  # cadre L3: القتلة... فأحسنوا [الذبح/الذبحة] INV aussi
    (120, 0.782, 0.822, 0.30, 1.00, 'N03i', 3, True),
    (121, 0.355, 0.398, 0.15, 0.90, 'N04', 3, False),  # en-tête الفهم + sous-en-tête ?
    (121, 0.385, 0.412, 0.30, 1.00, 'N05', 4, False),  # gloss كتب الإحسان: فرض الإتقان وشرعه
    (121, 0.472, 0.502, 0.50, 0.98, 'N06', 3, False),  # Q1 بقول الرسول ﷺ
    (122, 0.676, 0.702, 0.30, 0.80, 'N07', 4, False),  # حديث [أنس؟] رضي الله عنه أن النبي
    (122, 0.826, 0.848, 0.00, 0.55, 'N08', 3, False),  # حتى ماتت + ref [سنن ابن ماجة]
    (123, 0.096, 0.122, 0.55, 0.98, 'N09', 4, False),  # قوله ﷺ: «فإذا قتلتم
    (123, 0.342, 0.368, 0.00, 1.00, 'N10', 3, False),  # أو التي [نزل/ينقل] بها الأمراض يستحيل برؤها
    (123, 0.778, 0.806, 0.00, 0.35, 'N11', 5, False),  # ref [الرحمن: ٥٩/٦٠]
    (124, 0.580, 0.610, 0.05, 0.95, 'N12', 3, False),  # gloss 2 opener الجار
    (124, 0.718, 0.750, 0.10, 0.95, 'N13', 3, False),  # إعداد item1: اتق الله، تمحها، وخالق الناس
    (123, 0.128, 0.155, 0.55, 1.00, 'N14', 4, False),  # بأن [يتقن] الذابح ذلك ويتجنب التعذيب
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, scale, inv in ZONES:
    im = Image.open(f'{R600}/p{page}.png').convert('L')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if inv:
        c = ImageOps.invert(c)
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
    print(f'◆ {tag} p{page} y[{y0:.3f}-{y1:.3f}] x[{x0:.2f}-{x1:.2f}] ×{scale}')
    for o in outs:
        print(f'   {o}')
