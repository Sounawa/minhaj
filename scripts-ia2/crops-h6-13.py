#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — crops 1200 dpi des zones litigieuses L12 (docId 692), pp.71-75.
# Zones définies en points bbox (72 dpi) d'après bbox-71-77.html, converties ×(1200/72).
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h6-13/r1200'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-13/crops'
os.makedirs(OUT, exist_ok=True)
S = 1200 / 72.0

# (tag, page, y0_pt, y1_pt, x0_pt, x1_pt) — x pleine zone texte par défaut
ZONES = [
    ('c01-objectifs',   71, 195, 310,  55, 582),   # 3 lignes أهداف + début bandeau
    ('c02-tamhid',      71, 340, 495,  55, 582),   # تمهيد complet + question finale
    ('c03-hadith-takh', 71, 530, 670,  55, 582),   # hadith + takhrij
    ('c04-tarjama',     72, 110, 215,  55, 582),   # notice Abu Sa'id
    ('c05-sharh',       72, 285, 375,  55, 582),   # gloses ضرر/ضرار + bandeau
    ('c06-intro-tahlil',72, 515, 600,  55, 582),   # يتضن/يتشمل + أولا
    ('c07-glose',       72, 598, 770,  55, 582),   # glose Ibn Daqiq + أد الأمانة + وهذا معناه
    ('c08-waqil',       73,  60, 175,  55, 582),   # وقيل + فمعنى + ضررا ×2
    ('c09-ya-ibadi',    73, 175, 300,  55, 582),   # ومن أضر + يا عبادي + دماءكم + réf
    ('c10-thaniya',     73, 305, 410,  55, 582),   # ثانيا + الحديث خبر + إيقاعهما
    ('c11-yadullu',     73, 410, 600,  55, 582),   # والحديث يدل + قاعدة + لفظ عام
    ('c12-yustafad',    73, 600, 770,  55, 582),   # مما يستفاد ×2
    ('c13-tab-haut',    74, 230, 470,  55, 582),   # tableau haut (حق النفس/الغير/البيئة)
    ('c14-items-123',   74, 455, 545,  55, 582),   # items 1-3 تقويم
    ('c15-tab-bas',     74, 540, 770,  55, 582),   # tableau bas (السلوك/صح-خطأ/تعليل)
    ('c16-verset',      75, 115, 215,  55, 582),   # an-Nisa 29
    ('c17-hadiths',     75, 218, 325,  55, 582),   # أد الأمانة + اتقوا الملاعن
    ('c18-item-enr',    75, 330, 405,  55, 582),   # أتأمل النصوص
    ('c19-iidad',       75, 430, 515,  55, 582),   # الإعداد القبلي
]

for tag, p, y0, y1, x0, x1 in ZONES:
    im = Image.open(f'{D}/p{p}.png')
    box = (int(x0 * S), int(y0 * S), int(x1 * S), int(y1 * S))
    crop = im.crop(box)
    crop.save(f'{OUT}/{tag}.png')
    print(f'{tag}: p{p} {crop.size}')
print('CROPS OK')
