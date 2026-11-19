#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — prépa leçon 5 du tirage hadith-6ep «الْبِرُّ حُسْنُ الْخُلُقِ» (entry #6 du JSON,
# docId pdf-mut23h3b-685, titleFr «La bonté pieuse, c'est la beauté du caractère»).
# Bornage ÉTABLI au textlayer : L5 = pp.36-40 (p.35 = fin L4 : الإعداد القبلي «أحفظ حديث
# الدرس الموالي وأستخرج منه علامة البر والإثم» — prépare exactement L5 ; p.41 = أهداف L6
# «لزوم السنة» + hadith العُرْبَاض بن سارية). Rendus élargis pp.35-41 pour vérifier les deux bornes.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-06'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(35, 42))

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

# textlayer élargi (bornage) + bbox mot-à-mot de la leçon
subprocess.run(['pdftotext', '-f', '34', '-l', '42', SRC, f'{OUT}/textlayer-34-42.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '36', '-l', '41', SRC, f'{OUT}/bbox-36-41.html'], check=True)
print('couche texte OK')
