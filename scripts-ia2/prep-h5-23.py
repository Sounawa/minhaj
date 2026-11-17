#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-27 — prépa leçon 23 hadith-5ep (pp.125+, «التقوى وحسن الخلق» hadith 18 Arbaʿūn, Abū Dharr & Muʿādh)
# p.125-126 déjà rendues par prep-h5-22.py (réutilisées par lien dur) ; on rend p.127-131 pour bornage.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-23'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)

# leçon 23 démarre p.125 (الدرس 24 du livre) ; fin attendue ~p.129 ; p130-131 pour confirmation du bornage
PAGES = list(range(125, 132))

for res in (150, 600):
    d = f'{OUT}/r{res}'
    for p in PAGES:
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        old = f'/home/z/my-project/scripts-ia2/tmp/h5-22/r{res}/p{p}.png'
        if os.path.exists(old):
            os.link(old, png)
            print(f'{res}dpi p{p} réutilisé depuis h5-22')
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

subprocess.run(['pdftotext', '-f', '125', '-l', '131', SRC, f'{OUT}/textlayer-125-131.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '125', '-l', '131', SRC, f'{OUT}/bbox-125-131.html'], check=True)
print('couche texte OK')
