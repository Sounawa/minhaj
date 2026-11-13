#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — préparation hadith-5ep pdf-10 (leçon 10 « الحلال والحرام والمشتبهات », pp. 60-63) :
# rendus 150 dpi (lectures directes), planches 300 dpi en moitiés (adjudication directe),
# couche texte pdftotext (arbitre des āyas — leçon Z2-7).
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-10'
os.makedirs(OUT + '/plates', exist_ok=True)

PAGES = (60, 61, 62, 63)

# 1) rendus 150 dpi pleine page
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

# 3) couche texte pdftotext (pp. 60-63), avec séparateurs de page
txt = subprocess.run(['pdftotext', '-f', '60', '-l', '63', SRC, '-'],
                     capture_output=True, text=True).stdout
open(f'{OUT}/textlayer-60-63.txt', 'w', encoding='utf-8').write(txt)
print('textlayer:', len(txt), 'car')
print('OK prep h5-10')
