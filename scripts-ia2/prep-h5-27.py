#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-32 — prépa leçon 27 hadith-5ep (pp.150-155, «مما يدخل الجنة» hadith 22 Arbaʿūn,
# Jābir : أَرَأَيْتَ إِذَا صَلَّيْتُ الْمَكْتُوبَاتِ... فَأَدْخُلُ الْجَنَّةَ؟ قَالَ: نَعَمْ [صحيح مسلم])
# L28 «دعم وتطبيق» démarre p.156 → bornage L27 = pp.150-155 EXACTEMENT.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-27'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(150, 156))

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

subprocess.run(['pdftotext', '-f', '150', '-l', '155', SRC, f'{OUT}/textlayer-150-155.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '150', '-l', '155', SRC, f'{OUT}/bbox-150-155.html'], check=True)
print('couche texte OK')
