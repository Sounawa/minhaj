#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-39 — prépa leçon 4 du tirage hadith-6ep «شكر الله على نعمة الجوارح» (entry #5 du JSON,
# docId pdf-mut23h3b-684, titleFr «La gratitude envers Dieu pour le don des facultés»).
# Bornage ÉTABLI au textlayer : L4 = pp.29-35 (p.28 = fin L3 : استخلاص/تقويم/استثمار/إعداد قبلي ;
# p.29 = أهداف L4 + hadith أبي هريرة «كل سلامى من الناس عليه صدقة» [البخاري ومسلم] ;
# p.35 = الإعداد القبلي L4 (أحفظ حديث الدرس الموالي + أستخرج من علامة البر — prépare L5) ;
# p.36 = أهداف L5 «البر حسن الخلق»). Rendus élargis pp.28-36 pour vérifier les deux bornes.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-05'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(28, 37))

for res in (150, 600, 1200):
    d = f'{OUT}/r{res}'
    for p in PAGES:
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

# textlayer élargi (bornage) + bbox mot-à-mot de la leçon
subprocess.run(['pdftotext', '-f', '27', '-l', '36', SRC, f'{OUT}/textlayer-27-36.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '29', '-l', '36', SRC, f'{OUT}/bbox-29-36.html'], check=True)
print('couche texte OK')
