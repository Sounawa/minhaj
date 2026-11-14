#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — prépa leçon 16 hadith-5ep « التورع عن الشبهات » : rendus 150 dpi pp.88-94 + couche texte
# (Z2-17 a borné : leçon 16 démarre p.88 ; leçon 17 « ترك ما لا يعني »? attendue ~p.93+)
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-16'
os.makedirs(OUT, exist_ok=True)

subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '88', '-l', '94', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

subprocess.run(['pdftotext', '-f', '88', '-l', '94', '-layout', SRC, f'{OUT}/textlayer-88-94.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-88-94.txt'), 'octets')
