#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-31 — rendus 1200 dpi natifs pp.144-149 + bandes pleine largeur (leçon 26)
# Bandes JAMAIS coupées verticalement (leçon Z2-30 : le VLM complète les lignes coupées).
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26'
R12 = f'{DIR}/r1200'
os.makedirs(R12, exist_ok=True)
os.makedirs(f'{DIR}/bands', exist_ok=True)

for p in range(144, 150):
    png = f'{R12}/p{p}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '1200', '-f', str(p), '-l', str(p), SRC, f'{R12}/q{p}'], check=True)
        got = [f for f in os.listdir(R12) if f.startswith(f'q{p}-')]
        os.rename(f'{R12}/{got[0]}', png)
        print(f'1200dpi p{p} OK')

# (id, page, y0, y1) en px 1200 dpi (page ~10620 x 13452 ; échelle 16.667 px/point)
BANDS = [
    ('b01', 144, 830, 5000),    # bandeau الدرس ٢٦ + أهداف 1-3
    ('b02', 144, 6170, 8500),   # تمهيد (4 lignes + questions)
    ('b03', 144, 8150, 12000),  # encadré hadith (orné)
    ('b04', 145, 1000, 3080),   # ترجمة الراوي
    ('b05', 145, 3080, 6420),   # الفهم/الشرح + gloses
    ('b06', 145, 6750, 11670),  # استخلاص + التحليل intro + أولاً + لغة/شرعا
    ('b07', 146, 670, 2080),    # suite لزوم الطاعة + عَلِّمْنِي...
    ('b08', 146, 2080, 5830),   # جوامع الكلم + إذ لا تتأتى
    ('b09', 146, 5830, 8250),   # آية فصلت + قول عمر
    ('b10', 146, 8170, 11670),  # وهذا معنى قوله + هود + ابن عباس
    ('b11', 147, 1170, 4830),   # 2. علاقة الاستقامة بالإيمان
    ('b12', 147, 4920, 7750),   # ثانياً + القشيري
    ('b13', 147, 7750, 10250),  # وقال/وقيل + الموطأ
    ('b14', 147, 10170, 12080), # الواسطي + ومن فضائل + item 1
    ('b15', 148, 1170, 2830),   # suite item 1 + items 2-3
    ('b16', 148, 2830, 5080),   # يقول الله + آية [فصلت: ٢٩-٣١]
    ('b17', 148, 5000, 8750),   # ومما يستفاد (3 items)
    ('b18', 148, 8750, 12080),  # التقويم
    ('b19', 149, 1830, 3580),   # استثمار encadré أنس
    ('b20', 149, 4420, 6250),   # activités 1-3
    ('b21', 149, 6250, 9250),   # الإعداد القبلي
]

for cid, p, y0, y1 in BANDS:
    out = f'{DIR}/bands/{cid}-p{p}.png'
    if os.path.exists(out):
        continue
    im = Image.open(f'{R12}/p{p}.png')
    im.crop((250, y0, 10370, y1)).save(out)
    print(cid, im.crop((250, y0, 10370, y1)).size, 'OK')
print('done')
