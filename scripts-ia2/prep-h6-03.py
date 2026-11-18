#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-37 — prépa leçon 2 du tirage hadith-6ep «تحريم الظلم» (entry #3 du JSON,
# docId pdf-mut23h3b-682, fichier habours 2_.تحريم_الظلم-2.pdf).
# Bornage ATTENDU : pp.17-22 du manuel local (p.17 = objectifs L2 repérés en Z2-36 ;
# p.16 = الإعداد القبلي fin de L1). Rendus élargis pp.16-23 pour vérifier les deux bornes.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-03'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(16, 24))

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
subprocess.run(['pdftotext', '-f', '15', '-l', '24', SRC, f'{OUT}/textlayer-15-24.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '17', '-l', '22', SRC, f'{OUT}/bbox-17-22.html'], check=True)
print('couche texte OK')
