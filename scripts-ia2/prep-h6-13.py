#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-48 — prépa L12 «لا ضرر ولا ضرار» (entry #13 du JSON, docId pdf-mut23h3b-692).
# Bornage ATTENDU : L12 commence p.71 (أهداف y216-288 + تمهيد + hadith أبي سعيد الخدري
# y552-588 + takhrij y624-648 — bornage Z2-46) ; L13 «البينة على المدعي» (docId 693)
# commence p.76 d'après textlayer 70-78 (أهداف «أن أتعرف معنى المدعي والمدعى عليه»).
# L11 (691) = pp.66-70. Rendus pp.71-77 (66-71 existaient en h6-12, tmp perdu au reset),
# textlayer 70-78, bbox 71-77, tesseract 600 dpi psm4/6 pp.71-77.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h6-13'
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)
TESS = '/home/z/my-project/tessdata'

for res in (600, 1200):
    d = f'{OUT}/r{res}'
    for p in range(71, 78):
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True, timeout=600)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

if not os.path.exists(f'{OUT}/textlayer-70-78.txt'):
    subprocess.run(['pdftotext', '-f', '70', '-l', '78', SRC, f'{OUT}/textlayer-70-78.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '71', '-l', '77', SRC, f'{OUT}/bbox-71-77.html'], check=True)
print('couche texte OK')

for p in range(71, 78):
    for psm in (4, 6):
        out = f'{OUT}/tess600-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        r = subprocess.run(['tesseract', f'{OUT}/r600/p{p}.png',
                            'stdout', '--psm', str(psm), '-l', 'ara',
                            '--tessdata-dir', TESS],
                           capture_output=True, text=True, timeout=300)
        open(out, 'w', encoding='utf-8').write(r.stdout)
        print(f'tess p{p} psm{psm}: {len(r.stdout)} car')
print('PRÉPA L12 OK')
