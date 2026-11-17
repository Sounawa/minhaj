#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-26 — bandes pleine largeur 600 dpi pour adjudication VLM finale (leçon 22)
import os
from PIL import Image, ImageOps

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-22'
R600 = f'{OUT}/r600'

# (page, y0, y1, tag, invert)
BANDS = [
    (120, 0.230, 0.315, 'b01', False),  # objectifs 1-3 (verbes)
    (120, 0.415, 0.565, 'b02', False),  # تمهيد complet (فشرع/الإتقان/الجنان)
    (120, 0.640, 0.885, 'b03', True),   # cadre hadith INVERSÉ
    (122, 0.055, 0.150, 'b04', False),  # في العبادات opener + ref البخاري ومسلم
    (122, 0.300, 0.375, 'b05', False),  # آية العنكبوت + الحوار والجدال
    (122, 0.515, 0.585, 'b06', False),  # ثانيا opener (حث الإسلام على...)
    (122, 0.655, 0.775, 'b07', False),  # hadith تصبير + sanad + ref + gloss
    (122, 0.780, 0.875, 'b08', False),  # hadith الهرة fin + ref
    (123, 0.085, 0.300, 'b09', False),  # règles du ذبح complètes
    (123, 0.300, 0.485, 'b10', False),  # transition أفاعي + header + item 1
    (123, 0.545, 0.725, 'b11', False),  # items جار + والدين
    (123, 0.740, 0.815, 'b12', False),  # آية + ref الرحمن
    (124, 0.130, 0.285, 'b13', False),  # تقويم Q1-Q3
    (124, 0.565, 0.625, 'b14', False),  # gloss 2 opener
    (124, 0.635, 0.760, 'b15', False),  # إعداد قبلي header + items
]

for page, y0, y1, tag, inv in BANDS:
    im = Image.open(f'{R600}/p{page}.png')
    W, H = im.size
    c = im.crop((0, int(y0 * H), W, int(y1 * H)))
    if inv:
        c = ImageOps.invert(c.convert('L'))
    c.save(f'{OUT}/z22-{tag}.png')
    print(f'{tag}: p{page} y[{y0:.3f}-{y1:.3f}] {c.size}{" INV" if inv else ""}')
