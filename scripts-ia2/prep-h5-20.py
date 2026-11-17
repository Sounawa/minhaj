#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-22 — prépa leçon 20 hadith-5ep (pp.111-113, consolidation دعم وتطبيق) : rendus 150 + 600 dpi
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-20'
R150 = f'{OUT}/r150'
R600 = f'{OUT}/r600'
os.makedirs(R150, exist_ok=True)
os.makedirs(R600, exist_ok=True)

PAGES = list(range(111, 114))  # leçon 20 = pp. 111-113

for d, res in ((R150, 150), (R600, 600)):
    for p in PAGES:
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

# couche texte brute + bbox
subprocess.run(['pdftotext', '-f', '111', '-l', '113', SRC, f'{OUT}/textlayer-111-113.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '111', '-l', '113', SRC, f'{OUT}/bbox-111-113.html'], check=True)
print('couche texte OK')

# contrôle tailles
from PIL import Image
for p in PAGES:
    im = Image.open(f'{R150}/p{p}.png')
    im6 = Image.open(f'{R600}/p{p}.png')
    print(f'p{p}: 150dpi={im.size} 600dpi={im6.size}')
