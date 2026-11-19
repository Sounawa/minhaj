#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — prépa leçon 7 du tirage hadith-6ep «دَعْمٌ وَتَطْبِيقٌ» (entry #8 du JSON,
# docId pdf-mut23h3b-687, titleFr «Consolidation et application»).
# Bornage ÉTABLI en Z2-41 : L7 = pp.46-48 (p.45 = fin L6 : إعداد قبلي projet ;
# p.46 = cartouche + أهداف 687 + أنجز في دفتري 1-5 ; p.47-48 = نصوص/أسئلة/projet ;
# p.49 attendu = cartouche L8 pour borne droite). Rendus pp.45-49.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-08'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(45, 50))   # 45-49

for res in (150, 600, 1200):
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

# textlayer élargi (bornage droit L8) + bbox mot-à-mot de la leçon
subprocess.run(['pdftotext', '-f', '44', '-l', '50', SRC, f'{OUT}/textlayer-44-50.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '46', '-l', '49', SRC, f'{OUT}/bbox-46-49.html'], check=True)
print('couche texte OK')
