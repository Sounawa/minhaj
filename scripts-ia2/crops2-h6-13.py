#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — crops ronde 2 : bandeaux, mots litigieux, encadrés p.74, zones mal cadrées.
from PIL import Image
import os

D = '/home/z/my-project/scripts-ia2/tmp/h6-13/r1200'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-13/crops'
os.makedirs(OUT, exist_ok=True)
S = 1200 / 72.0

ZONES = [
    # (tag, page, y0, y1, x0, x1) en points
    ('c20-p74-haut',     74,   0, 250,  45, 585),  # structure haut p74
    ('c21-enc1',         74, 265, 470, 470, 585),  # encadré 1 (droite)
    ('c22-enc2',         74, 265, 470, 380, 475),  # encadré 2
    ('c23-enc3',         74, 265, 470, 290, 385),  # encadré 3
    ('c25-enc6',         74, 265, 470,  40, 148),  # encadré 6 (gauche)
    ('c26-items12',      74, 450, 545, 300, 585),  # items 1-2
    ('c27-tab-bas-r14',  74, 630, 775, 300, 585),  # rangées 1+4 tableau bas
    ('c28-band-tamhid',  71, 298, 355,  55, 582),  # bandeau تمهيد
    ('c29-band-hadith',  71, 478, 548,  55, 582),  # bandeau الحديث
    ('c30-band-sharh',   72, 268, 308,  55, 582),  # bandeau الشرح
    ('c31-band-tahlil',  72, 468, 535,  55, 582),  # bandeau التحليل
    ('c32-tamhid-l1',    71, 348, 388,  55, 582),  # ligne 1 تمهيد (mot après ليرفع)
    ('c33-glose2',       72, 330, 372,  55, 582),  # مجاراة/مجازاة
    ('c34-famaana',      73,  92, 142,  55, 582),  # لا يدخل أحد على أحد ضررا
    ('c35-walbuduquf',   73, 443, 478,  55, 582),  # والضرر/الضرار بالوقوف
    ('c36-yashmal',      73, 533, 568,  55, 582),  # لفظ عام يشمل + علاقته
    ('c37-ref-bukhari',  73, 262, 296,  55, 582),  # référence Boukhari
    ('c38-maahu-inda',   72, 693, 775,  55, 582),  # وهذا معناه عند...
    ('c39-band-istithmar',75,  58, 132,  55, 582), # bandeau استثمار + début verset
    ('c40-ittaqu',       75, 258, 294,  55, 582),  # اتقوا الملاعن الثلاث البراز
    ('c41-iidad-mot',    75, 443, 515,  55, 582),  # أحفظ حديث الدرس الموالى وأبين
]

for tag, p, y0, y1, x0, x1 in ZONES:
    im = Image.open(f'{D}/p{p}.png')
    box = (int(x0 * S), int(y0 * S), int(x1 * S), int(y1 * S))
    crop = im.crop(box)
    crop.save(f'{OUT}/{tag}.png')
    print(f'{tag}: p{p} {crop.size}')
print('CROPS R2 OK')
