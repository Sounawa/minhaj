#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-20 — prépa leçon 18 hadith-5ep « محبة الخير للناس » : rendus 150 dpi pp.98-104 + couche texte
# (Z2-19 a livré leçon 17 = pp.93-97 ; leçon 18 démarre p.98 ; leçon 19 « من صفات المؤمنين ? » attendue ~p.103+)
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-18'
os.makedirs(OUT, exist_ok=True)

subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '98', '-l', '104', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

subprocess.run(['pdftotext', '-f', '98', '-l', '104', '-layout', SRC, f'{OUT}/textlayer-98-104.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-98-104.txt'), 'octets')
