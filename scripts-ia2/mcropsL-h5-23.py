#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — recadrages LIGNE NATIVE (série L) pour tesseract, leçon 23 (pp.125-130)
import os, subprocess
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-translate/tessdata'

# (page, y0, y1, x0, x1, tag, invert)
CROPS = [
    # ── p.125 : bandeau titre (NUMÉRO exact !) + أهداف + تمهيد + hadith
    (125, 0.030, 0.155, 0.00, 1.00, 'L01', False),  # الدرس + numéro + titre
    (125, 0.060, 0.130, 0.30, 0.75, 'L01b', False),  # bandeau numéro seul (étroit)
    (125, 0.245, 0.370, 0.00, 1.00, 'L02', False),  # أهداف 3 lignes
    (125, 0.440, 0.600, 0.00, 1.00, 'L03', False),  # تمهيد + [الموطأ] + question
    (125, 0.610, 0.905, 0.00, 1.00, 'L04', True),   # cadre hadith INVERSÉ
    (125, 0.610, 0.905, 0.00, 1.00, 'L04r', False), # cadre hadith brut (contrôle)
    # ── p.126 : rāwī ×2 + فهم/شرح + استنتاج
    (126, 0.085, 0.300, 0.00, 1.00, 'L05', False),  # Abū Ḏarr + hadith éloge + الربذة
    (126, 0.310, 0.500, 0.00, 1.00, 'L06', False),  # Muʿāḏ + أسلم وسنه
    (126, 0.500, 0.760, 0.00, 1.00, 'L07', False),  # الفهم + شرح 3 gloses
    (126, 0.760, 0.910, 0.00, 1.00, 'L08', False),  # استنتاج Q1 Q2
    # ── p.127 : تحليل intro + أولاً (سبب الورود) + ثانياً
    (127, 0.100, 0.200, 0.00, 1.00, 'L09', False),  # intro + titre أولاً
    (127, 0.200, 0.420, 0.00, 1.00, 'L10', False),  # سبب الورود : récit Abū Ḏarr
    (127, 0.420, 0.610, 0.00, 1.00, 'L11', False),  # الأمر موجه لكل مسلم + فالمسلم
    (127, 0.610, 0.910, 0.00, 1.00, 'L12', False),  # ثانياً + وصى + قد يخل + فالمطلوب
    # ── p.128 : zone VLM hallucinée + ثالثاً + أهمية/فضل
    (128, 0.120, 0.390, 0.00, 1.00, 'L13', False),  # المراد بالحسنة + hadith أبي هريرة + ref
    (128, 0.385, 0.620, 0.00, 1.00, 'L14', False),  # ثالثاً + 1. أهمية حسن الخلق
    (128, 0.600, 0.910, 0.00, 1.00, 'L15', False),  # ومن حسن الخلق + 2. فضل
    # ── p.129 : محمدة + hadiths + يستفاد + تقويم
    (129, 0.090, 0.310, 0.00, 1.00, 'L16', False),  # محمدة وعبادة + ما شيء أثقل + ref
    (129, 0.300, 0.430, 0.00, 1.00, 'L17', False),  # وصاحب + إن من أحبكم + ref
    (129, 0.420, 0.760, 0.00, 1.00, 'L18', False),  # ومما يستفاد (tirets)
    (129, 0.750, 0.910, 0.00, 1.00, 'L19', False),  # التقويم + Q1 Q2
    # ── p.130 : Q3 + آية + activités + إعداد قبلي
    (130, 0.060, 0.180, 0.00, 1.00, 'L20', False),  # Q3 تقويم
    (130, 0.130, 0.470, 0.00, 1.00, 'L21', False),  # استثمار + آية [آل عمران]
    (130, 0.460, 0.640, 0.00, 1.00, 'L22', False),  # 3 activités
    (130, 0.620, 0.910, 0.00, 1.00, 'L23', False),  # إعداد قبلي + items
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, inv in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if inv:
        c = ImageOps.invert(c.convert('L'))
    p = f'{OUT}/z23-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', '6'],
                       capture_output=True, text=True, env=env)
    txt = ' ¶ '.join(l.strip() for l in r.stdout.splitlines() if l.strip())
    mark = ' INV' if inv else ''
    print(f'── {tag} p{page} y[{y0:.3f}-{y1:.3f}]{mark}:')
    print(f'   {txt if txt else "(vide)"}')
