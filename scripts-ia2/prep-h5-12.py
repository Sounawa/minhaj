#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-13 — prépa leçon 12 hadith-5ep : rendus 150 dpi pp.69-74 + couches texte
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-12'
os.makedirs(OUT, exist_ok=True)

# rendus 150 dpi p69..p74
subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '69', '-l', '74', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

# couches texte p69..p74
subprocess.run(['pdftotext', '-f', '69', '-l', '74', '-layout', SRC, f'{OUT}/textlayer-69-74.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-69-74.txt'), 'octets')
