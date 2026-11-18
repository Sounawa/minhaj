#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-38 — prépa leçon 3 du tirage hadith-6ep «التنافس في الخير» (entry #4 du JSON,
# docId pdf-mut23h3b-683, fichier habours 3_.التنافس_في_الخير.pdf).
# Bornage ATTENDU : pp.24-29 du manuel local (p.24 = أهداف L3 repérés en Z2-37 ;
# p.23 = الاستثمار/الإعداد القبلي fin de L2). Rendus élargis pp.23-30 pour vérifier les deux bornes.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-04'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(23, 31))

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
subprocess.run(['pdftotext', '-f', '22', '-l', '31', SRC, f'{OUT}/textlayer-22-31.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '24', '-l', '29', SRC, f'{OUT}/bbox-24-29.html'], check=True)
print('couche texte OK')
