#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-8 — planches haute résolution (300 dpi) de hadith-5ep pdf-8 (leçon 8, pp. 50-55),
# coupées en moitiés pour adjudication par lecture directe de l'agent.
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-08/plates'
os.makedirs(OUT, exist_ok=True)

for pg in (50, 51, 52, 53, 54, 55):
    png = f'{OUT}/hi-{pg}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '300', '-f', str(pg), '-l', str(pg),
                        SRC, f'{OUT}/hi-tmp-{pg}'], check=True)
        src = f'{OUT}/hi-tmp-{pg}-{pg:03d}.png'
        os.replace(src, png)

for pg in (50, 51, 52, 53, 54, 55):
    im = Image.open(f'{OUT}/hi-{pg}.png')
    w, h = im.size
    top = im.crop((0, 0, w, int(h * 0.56)))
    bot = im.crop((0, int(h * 0.44), w, h))
    top.save(f'{OUT}/p{pg}-A.png')
    bot.save(f'{OUT}/p{pg}-B.png')
    print(pg, im.size, '->', top.size, bot.size)
print('OK')
