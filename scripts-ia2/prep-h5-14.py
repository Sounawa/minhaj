#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-16 — prépa leçon 14 hadith-5ep : rendus 150 dpi pp.80-85 + couche texte
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-14'
os.makedirs(OUT, exist_ok=True)

subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '80', '-l', '85', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

subprocess.run(['pdftotext', '-f', '80', '-l', '85', '-layout', SRC, f'{OUT}/textlayer-80-85.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-80-85.txt'), 'octets')
