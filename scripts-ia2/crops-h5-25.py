#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-30 — recadrages 600 dpi ciblés (zones contested) leçon 25, pp.138-144
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25'
CROPS = [
    ('z01', 138, 500, 2400),   # bandeau الدرس ٢٥ + أهداف 1-3
    ('z02', 138, 2900, 4150),  # تمهيد 4 lignes (الجامعة/أكدتها/عرفت)
    ('z03', 138, 4150, 6200),  # encadré hadith (orné)
    ('z04', 139, 950, 2400),   # ترجمة الراوي (lignes manquantes tesseract)
    ('z05', 139, 3700, 4050),  # glose لم تستحي (مضارع…)
    ('z06', 139, 4500, 4850),  # fin glose فعل كل ما يُستقبح/يستكره
    ('z07', 140, 1500, 2000),  # لغة (بالمد الحشمة… الاستبقا)
    ('z08', 140, 4550, 5200),  # [فصلت: ٣٩] + بين لهم ما…
    ('z09', 140, 5200, 5750),  # ثانيهما + ما يُسْتَتْكَرُ
    ('z10', 141, 2900, 3400),  # المحمود/الممدوح والمشروع + البرور بهما
    ('z11', 141, 3400, 3950),  # فحش الفعل + بقية liste
    ('z12', 141, 4050, 4500),  # ليس من الحياء (تكليل المحرمات)
    ('z13', 141, 4550, 5350),  # لا يسمى شرعيا + مذموم + خجل…
    ('z14', 142, 550, 1500),   # يستفاد items
    ('z15', 142, 2300, 2950),  # تقويم Q2/Q3
    ('z16', 142, 3850, 4900),  # استثمار cadre (رأت الماء… وجهها)
    ('z17', 142, 4850, 5800),  # تربت يمينك + activités
    ('z18', 143, 1200, 1600),  # إعداد قبلي item 1 (3 expressions)
    ('z19', 144, 400, 2600),   # bandeau leçon 26 (bornage)
]
os.makedirs(f'{DIR}/crops', exist_ok=True)
for cid, p, y0, y1 in CROPS:
    out = f'{DIR}/crops/{cid}-p{p}.png'
    if not os.path.exists(out):
        subprocess.run(['python3', '-c', f'''
from PIL import Image
im = Image.open("{DIR}/r600/p{p}.png")
im.crop((150, {y0}, 5160, {y1})).save("{out}")
'''], check=True)
    print(cid, 'OK')
print('done')
