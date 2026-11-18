#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-33 — prépa leçon 28 hadith-5ep «دعم وتطبيق» (pp.156-158, leçon de SYNTHÈSE,
# sans encadré de hadith — cf. L7/L14/L20 ; titleFr registre «Consolidation et application»).
# L29 «لائحة المصادر والمراجع» démarre p.159 → bornage L28 = pp.156-158 EXACTEMENT
# (textlayer pp.154-161 extrait pour re-vérifier le bornage des deux côtés).
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-28'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(156, 159))

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

subprocess.run(['pdftotext', '-f', '154', '-l', '161', SRC, f'{OUT}/textlayer-154-161.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '156', '-l', '158', SRC, f'{OUT}/bbox-156-158.html'], check=True)
print('couche texte OK')
