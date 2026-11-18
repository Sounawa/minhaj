#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-31 — prépa leçon 26 hadith-5ep (pp.144+, «الاستقامة» hadith Sufyān ibn ʿAbd Allāh
# ath-Thaqafī «قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ» [صحيح مسلم attendu])
# leçon 25 = pp.138-143 (6 p.) ; leçon 26 démarre p.144 (bandeau الدرس ٢٦) ; bornage jusqu'à p.153.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-26'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)

PAGES = list(range(144, 154))

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

subprocess.run(['pdftotext', '-f', '144', '-l', '153', SRC, f'{OUT}/textlayer-144-153.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '144', '-l', '153', SRC, f'{OUT}/bbox-144-153.html'], check=True)
print('couche texte OK')
