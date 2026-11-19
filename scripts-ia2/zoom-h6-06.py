#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — zooms mot-level 1200 dpi sur les mots disputés de la leçon 5 + tesseract psm 7/8/13.
import subprocess
import numpy as np
from PIL import Image, ImageOps

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
import os
os.makedirs(f'{DIR}/zooms', exist_ok=True)

# (tag, page, y0, y1, x0, x1, note)
ZOOMS = [
    ('z-madud',      37, 138, 158, 415, 470, 'المعدود word (بعد ربيعة قبل في الشاميين)'),
    ('z-khuzayma',   37, 228, 250, 415, 475, 'أسد بن خزيمة (ز présent ?)'),
    ('z-kunya',      37, 228, 250, 300, 420, 'يكنى أبا شداد'),
    ('z-sanata',     37, 228, 250, 240, 310, 'سنة تسع'),
    ('z-lahu-ahadith', 37, 256, 275, 380, 500, 'وله ? أحاديث'),
    ('z-bakka',      37, 256, 275, 100, 300, 'وكان قارئا... بكاء'),
    ('z-glose-end',  37, 398, 428, 230, 330, 'ولا/ولم تطمئن إليه'),
    ('z-nuqsim',     36, 350, 380, 420, 560, 'نقسم/تقسم الأعمال'),
    ('z-yatia',      36, 350, 380, 300, 430, 'التي يأتيها'),
    ('z-ruwah-muslim', 36, 602, 622, 380, 560, '[رواه مسلم]'),
    ('z-darami',     36, 697, 720, 150, 330, 'والدارمي/والدرامي'),
    ('z-masnaday',   36, 697, 720, 330, 460, 'مسندي الإمامين'),
    ('z-naam',       36, 630, 652, 380, 470, 'قلت نعم'),
    ('z-cite-head',  38, 74, 108, 380, 565, 'premier mot citation (قال/كالبر...)'),
    ('z-taghdiya',   38, 74, 108, 250, 420, 'تغذية/تعذية البدن'),
    ('z-page-ref',   38, 74, 108, 140, 260, 'ص: 214 digits'),
    ('z-lawahiq',    38, 165, 190, 60, 160, 'بسائر لواحقها/أنواعها'),
    ('z-aya-baq-num',38, 248, 268, 60, 200, '[البقرة: 176/177] digits'),
    ('z-muhawara',   38, 377, 408, 200, 330, 'الرفق في المحاورة/المحاولة'),
    ('z-badl',       38, 405, 435, 330, 470, 'البذل/البدل في الإحسان'),
    ('z-nafra',      38, 618, 646, 400, 520, 'يورث نفرة/ذفرة/زفرة في القلب'),
    ('z-qabil',      38, 705, 732, 330, 480, 'قابل كل بينهما'),
    ('z-fatwa',      39, 192, 220, 400, 560, 'على فتوى/فتاوى النفوس'),
    ('z-aftahu',     39, 255, 282, 380, 520, 'فسأل عنها و? بأنها حلال'),
    ('z-ghayr',      39, 284, 312, 200, 420, 'الذي هو غير مطمئن إليه'),
    ('z-nasai',      39, 368, 390, 380, 560, 'رواه الترمذي والنسائي'),
    ('z-islah1',     39, 443, 470, 330, 530, 'أهمية إصلاح/إضلاح القلب'),
    ('z-islah2',     39, 443, 470, 90, 230, 'لإصلاح حركات الجوارح'),
    ('z-furqan-aya', 40, 405, 448, 100, 560, 'آية وعباد الرحمن... هونا'),
    ('z-muwalī',     40, 625, 652, 240, 400, 'الدرس الموالي/الموالى'),
    ('z-marḍi',      37, 700, 730, 300, 460, 'ولكل فعل مرضي + تزكية النفس'),
    ('z-yulhiq',     37, 663, 690, 150, 340, 'ويلحقه/فيلحق بالأبرار'),
    ('z-yabirru',    37, 663, 690, 340, 470, 'يبر به فاعله'),
]

for tag, pg, y0, y1, x0, x1, note in ZOOMS:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = ImageOps.autocontrast(c)
    variants = {'x2': c.resize((c.width*2, c.height*2), Image.LANCZOS),
                'x3': c.resize((c.width*3, c.height*3), Image.LANCZOS)}
    print(f'===== {tag} — {note} =====')
    for vn, img in variants.items():
        fp = f'{DIR}/zooms/{tag}-{vn}.png'
        img.save(fp)
        for psm in (7, 8):
            base = f'{DIR}/zooms/{tag}-{vn}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip()
            if txt: print(f'  [{vn} psm{psm}] {txt[:120]}')
