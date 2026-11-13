#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — zooms demi-largeur 600 dpi (résolution maximale) — points fins leçon 10
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-10/zooms6'
os.makedirs(OUT, exist_ok=True)
_cache = {}

def page600(pg):
    if pg not in _cache:
        png = f'{OUT}/p600-{pg}.png'
        src = f'/home/z/my-project/minhaj/scripts-ia2/tmp/h5-10/zooms4/p600-{pg}.png'
        if os.path.exists(src):
            png = src
        else:
            if not os.path.exists(png):
                subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(pg), '-l', str(pg),
                                SRC, f'{OUT}/tmp600-{pg}'], check=True)
                os.replace(f'{OUT}/tmp600-{pg}-{pg:03d}.png', png)
        _cache[pg] = Image.open(png)
    return _cache[pg]

def crop(pg, y0, y1, x0, x1):
    im = page600(pg); w, h = im.size
    c = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    if c.size[0] > 1556:
        c = c.resize((1556, int(c.size[1]*1556/c.size[0])), Image.LANCZOS)
    return c

def composite(name, crops):
    W = max(c.size[0] for c in crops)
    H = sum(c.size[1] for c in crops) + 8 * (len(crops) - 1)
    canvas = Image.new('RGB', (W, H), (200, 60, 60))
    y = 0
    for c in crops:
        canvas.paste(c, (0, y)); y += c.size[1] + 8
    canvas.save(f'{OUT}/{name}.png'); print(name, canvas.size)

# t1 — p63 : ligne «قارَبَ ... خالَطَهُ غالِباً» + āya (moitiés droite puis gauche)
composite('t1', [
    crop(63, 0.628, 0.700, 0.50, 1.00),
    crop(63, 0.628, 0.700, 0.00, 0.50),
])
# t2 — p63 : «فهي/فتنهى عن الاقتراب من الوقوع في الحرام» (moitiés)
composite('t2', [
    crop(63, 0.700, 0.775, 0.50, 1.00),
    crop(63, 0.700, 0.775, 0.00, 0.50),
])
# t3 — p62 : item 2 — āyāt lignes (moitiés)
composite('t3', [
    crop(62, 0.540, 0.648, 0.50, 1.00),
    crop(62, 0.540, 0.648, 0.00, 0.50),
])
# t4 — p64 : ibn Rajab «فأما/فلما من كان عالما بها واتبَعَ ما دَلَّهُ عليها» (moitiés)
composite('t4', [
    crop(64, 0.450, 0.535, 0.50, 1.00),
    crop(64, 0.450, 0.535, 0.00, 0.50),
])
print('OK zooms6')
