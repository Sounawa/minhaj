#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-28 — prépa leçon 24 hadith-5ep (pp.131+, «حفظ أوامر الله تعالى» hadith 19 Arbaʿūn, Ibn ʿAbbās
# «يَا غُلَامُ إِنِّي أُعَلِّمُكَ كَلِمَاتٍ: احْفَظِ اللهَ يَحْفَظْكَ...» [سنن الترمذي])
# p.131 déjà rendue par prep-h5-23.py (réutilisée par lien dur) ; on rend p.132-138 pour bornage.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-24'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)

# leçon 24 démarre p.131 ; leçon 23 = 6 pages (125-130) → fin attendue ~p.136 ; p.137-138 pour confirmation du bornage
PAGES = list(range(131, 139))

for res in (150, 600):
    d = f'{OUT}/r{res}'
    for p in PAGES:
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        old = f'/home/z/my-project/scripts-ia2/tmp/h5-23/r{res}/p{p}.png'
        if os.path.exists(old):
            os.link(old, png)
            print(f'{res}dpi p{p} réutilisé depuis h5-23')
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

subprocess.run(['pdftotext', '-f', '131', '-l', '138', SRC, f'{OUT}/textlayer-131-138.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '131', '-l', '138', SRC, f'{OUT}/bbox-131-138.html'], check=True)
print('couche texte OK')
