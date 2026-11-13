#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-12 — prépa leçon 11 hadith-5ep : rendus 150 dpi pp.65-70 + couches texte
import subprocess, os

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-11'
os.makedirs(OUT, exist_ok=True)

# rendus 150 dpi p65..p70
subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '65', '-l', '70', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

# couches texte p65..p70
subprocess.run(['pdftotext', '-f', '65', '-l', '70', '-layout', SRC, f'{OUT}/textlayer-65-70.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-65-70.txt'), 'octets')
