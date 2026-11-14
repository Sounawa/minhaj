#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-17 — prépa leçon 15 hadith-5ep « الدعاء وأثره » : rendus 150 dpi pp.83-89 + couche texte
# (Z2-16 a borné : leçon 15 démarre p.83 ; pdf-16 « التورع عن الشبهات » attendu ~p.89+)
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-15'
os.makedirs(OUT, exist_ok=True)

subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '83', '-l', '89', SRC, f'{OUT}/p'], check=True)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f, os.path.getsize(f'{OUT}/{f}') // 1024, 'Ko')

subprocess.run(['pdftotext', '-f', '83', '-l', '89', '-layout', SRC, f'{OUT}/textlayer-83-89.txt'], check=True)
print('textlayer:', os.path.getsize(f'{OUT}/textlayer-83-89.txt'), 'octets')
