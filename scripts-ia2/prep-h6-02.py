#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 — prépa leçon 1 du tirage hadith-6ep «المسارعة في الخيرات» (entry #2 du JSON,
# docId pdf-mut23h3b-681, fichier habours 1_.المسارعة_في_الخيرات.pdf).
# Bornage ÉTABLI au texte-layer : leçon 1 = pp.11-16 du manuel local
# (p.10 = fin du tableau التوزيع ; p.17 = objectifs de la leçon 2 تحريم الظلم).
# pp.5-8 = pages « méthode » avec extraits annotés (NE PAS confondre avec la leçon).
# Rendus élargis pp.10-17 pour vérifier le bornage des deux côtés.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-02'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(10, 18))

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
subprocess.run(['pdftotext', '-f', '9', '-l', '18', SRC, f'{OUT}/textlayer-9-18.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '11', '-l', '16', SRC, f'{OUT}/bbox-11-16.html'], check=True)
print('couche texte OK')
