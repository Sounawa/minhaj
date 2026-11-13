#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-9 — préparation hadith-5ep pdf-9 (leçon 9 « الإحداث والابتداع في الدين », pp. 56-59) :
# rendus 150 dpi (lectures VLM), planches 300 dpi en moitiés (adjudication directe),
# couche texte pdftotext (arbitre des āyas — leçon Z2-7).
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-09'
os.makedirs(OUT + '/plates', exist_ok=True)

PAGES = (56, 57, 58, 59)

# 1) rendus 150 dpi pleine page (VLM)
for pg in PAGES:
    png = f'{OUT}/p-{pg:03d}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', str(pg), '-l', str(pg),
                        SRC, f'{OUT}/tmp150-{pg}'], check=True)
        os.replace(f'{OUT}/tmp150-{pg}-{pg:03d}.png', png)

# 2) planches 300 dpi en moitiés (A = haut 56%, B = bas 44%, recouvrement 12%)
for pg in PAGES:
    png = f'{OUT}/plates/hi-{pg}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '300', '-f', str(pg), '-l', str(pg),
                        SRC, f'{OUT}/plates/tmp300-{pg}'], check=True)
        os.replace(f'{OUT}/plates/tmp300-{pg}-{pg:03d}.png', png)
    im = Image.open(png)
    w, h = im.size
    top = im.crop((0, 0, w, int(h * 0.56)))
    bot = im.crop((0, int(h * 0.44), w, h))
    top.save(f'{OUT}/plates/p{pg}-A.png')
    bot.save(f'{OUT}/plates/p{pg}-B.png')
    print(pg, im.size, '->', top.size, bot.size)

# 3) couche texte pdftotext (pp. 56-59), avec séparateurs de page
txt = subprocess.run(['pdftotext', '-f', '56', '-l', '59', SRC, '-'],
                     capture_output=True, text=True).stdout
open(f'{OUT}/textlayer-56-59.txt', 'w', encoding='utf-8').write(txt)
print('textlayer:', len(txt), 'car')
print('OK prep h5-09')
