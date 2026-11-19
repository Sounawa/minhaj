#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — prépa leçon 6 du tirage hadith-6ep «لُزُومُ السُّنَّةِ» (entry #7 du JSON,
# docId pdf-mut23h3b-686, titleFr «L'attachement à la Sunna»).
# Bornage ATTENDU : L6 commence p.41 (أهداف L6 aperçues en Z2-40) ; fin à cartographier
# (leçon suivante = 687 «دعم وتطبيق», consolidation). Rendus élargis pp.40-48 pour
# établir les deux bornes au textlayer.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-07'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(40, 49))

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
subprocess.run(['pdftotext', '-f', '39', '-l', '49', SRC, f'{OUT}/textlayer-39-49.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '41', '-l', '48', SRC, f'{OUT}/bbox-41-48.html'], check=True)
print('couche texte OK')
