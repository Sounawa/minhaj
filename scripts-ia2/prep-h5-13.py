#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-15 — prépa leçon 13 hadith-5ep : rendus 150 dpi pp.74-80 + couche texte
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-13'
os.makedirs(OUT, exist_ok=True)

# rendus 150 dpi p74..p80
subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '74', '-l', '80', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

# couche texte p74..p80
subprocess.run(['pdftotext', '-f', '74', '-l', '80', '-layout', SRC, f'{OUT}/textlayer-74-80.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-74-80.txt'), 'octets')
