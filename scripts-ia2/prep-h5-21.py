#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-24 — prépa leçon 21 hadith-5ep (pp.114-119, «لا تغضب» hadith 16 Arbaʿūn, Abū Hurayra)
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-21'
R150 = f'{OUT}/r150'
R600 = f'{OUT}/r600'
os.makedirs(R150, exist_ok=True)
os.makedirs(R600, exist_ok=True)

PAGES = list(range(114, 120))  # leçon 21 = pp.114-119 (leçon 22 «الإحسان» démarre p.120)

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

subprocess.run(['pdftotext', '-f', '114', '-l', '119', SRC, f'{OUT}/textlayer-114-119.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '114', '-l', '119', SRC, f'{OUT}/bbox-114-119.html'], check=True)
print('couche texte OK')

from PIL import Image
for p in PAGES:
    im = Image.open(f'{R150}/p{p}.png')
    print(f'p{p}: 150dpi={im.size}')
