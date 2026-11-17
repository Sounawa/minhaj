#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-24 — recadrages LIGNE NATIVE (série L) pour tesseract, résolution 600dpi brute.
import os, subprocess, sys
from PIL import Image

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-21'
R600 = f'{OUT}/r600'
TESS = '/home/z/my-project/scripts-ia2/tmp/tessdata'

# (page, y0, y1, x0, x1, tag, invert)
CROPS = [
    (114, 0.515, 0.565, 0.00, 1.00, 'L01', False),  # تمهيد ligne 3 complète
    (114, 0.595, 0.660, 0.00, 1.00, 'L02', False),  # questions
    (115, 0.268, 0.312, 0.00, 1.00, 'L03', False),  # شرح item1
    (115, 0.355, 0.400, 0.00, 1.00, 'L04', False),  # شرح item3 (لا تغضب)
    (115, 0.500, 0.540, 0.00, 1.00, 'L05', False),  # استخلاص Q2
    (115, 0.575, 0.650, 0.00, 1.00, 'L06', False),  # تحليل intro (لخص عدة مضامين)
    (115, 0.845, 0.890, 0.00, 1.00, 'L07', False),  # الظاهرة لسمو بلاغته
    (116, 0.082, 0.122, 0.00, 1.00, 'L08', False),  # ففيها ligne 1
    (116, 0.120, 0.158, 0.00, 1.00, 'L09', False),  # ففيها ligne 2
    (116, 0.155, 0.190, 0.00, 1.00, 'L10', False),  # ففيها ligne 3 (وعلى سبيلهم)
    (116, 0.262, 0.300, 0.00, 1.00, 'L11', False),  # معنى قوله... أى لا تستحب
    (116, 0.395, 0.435, 0.00, 1.00, 'L12', False),  # ولأنه من طبائعه قلّ...
    (116, 0.500, 0.540, 0.00, 1.00, 'L13', False),  # وساوس الشيطان وانفعالات
    (116, 0.755, 0.800, 0.00, 1.00, 'L14', False),  # فالشيطان زين لـ...
    (116, 0.830, 0.865, 0.00, 1.00, 'L15', False),  # من أقوى الحيل لدفع كيده
    (117, 0.125, 0.200, 0.00, 1.00, 'L16', False),  # ثانيا intro
    (117, 0.680, 0.725, 0.00, 1.00, 'L17', False),  # ثمرة 4 opener
    (118, 0.445, 0.492, 0.00, 1.00, 'L18', False),  # كلمتين أو ثلاث ligne
    (118, 0.598, 0.632, 0.00, 1.00, 'L19', False),  # تقويم Q1 opener
    (118, 0.715, 0.755, 0.00, 1.00, 'L20', False),  # تقويم Q3
    (119, 0.630, 0.720, 0.00, 1.00, 'L21', False),  # إعداد قبلي items
]

env = dict(os.environ, TESSDATA_PREFIX=TESS)
for page, y0, y1, x0, x1, tag, inv in CROPS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if inv:
        from PIL import ImageOps
        c = ImageOps.invert(c.convert('L'))
    p = f'{OUT}/z21-{tag}.png'
    c.save(p)
    r = subprocess.run(['tesseract', p, '-', '-l', 'ara', '--psm', '7'],
                       capture_output=True, text=True, env=env)
    txt = r.stdout.strip()
    print(f'── L{tag[1:]} p{page} y[{y0:.3f}-{y1:.3f}]:')
    print(f'   {txt if txt else "(vide)"}')
