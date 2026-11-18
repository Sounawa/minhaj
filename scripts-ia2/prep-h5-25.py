#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-30 — prépa leçon 25 hadith-5ep (pp.138+, «الحياء» hadith 20 Arbaʿūn
# «إِنَّمَا الْحَيَاءُ شُعْبَةٌ مِنَ الْإِيمَانِ» + «إِذَا لَمْ تَسْتَحْيِ فَاصْنَعْ مَا شِئْتَ»)
# tmp/h5-24 perdu au 8e recyclage → on rend tout depuis p.138 ; bornage jusqu'à p.146.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-25'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)

# leçon 25 démarre p.138 ; leçon 24 = 7 pages (131-137) → fin attendue ~p.144 ; p.145-146 pour confirmation du bornage
PAGES = list(range(138, 147))

for res in (150, 600):
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

subprocess.run(['pdftotext', '-f', '138', '-l', '146', SRC, f'{OUT}/textlayer-138-146.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '138', '-l', '146', SRC, f'{OUT}/bbox-138-146.html'], check=True)
print('couche texte OK')
