#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — zooms complémentaires leçon 10 (600 dpi natif, bandes pleine largeur)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-10/zooms5'
os.makedirs(OUT, exist_ok=True)
_cache = {}

def page600(pg):
    if pg not in _cache:
        png = f'{OUT}/p600-{pg}.png'
        if not os.path.exists(png):
            # réutiliser les rendus existants de zooms4 si présents
            src = f'/home/z/my-project/minhaj/scripts-ia2/tmp/h5-10/zooms4/p600-{pg}.png'
            if os.path.exists(src):
                png = src
            else:
                subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(pg), '-l', str(pg),
                                SRC, f'{OUT}/tmp600-{pg}'], check=True)
                os.replace(f'{OUT}/tmp600-{pg}-{pg:03d}.png', png)
        _cache[pg] = Image.open(png)
    return _cache[pg]

def crop(pg, y0, y1, x0, x1):
    im = page600(pg); w, h = im.size
    c = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    if c.size[0] > 1560:
        c = c.resize((1560, int(c.size[1]*1560/c.size[0])), Image.LANCZOS)
    return c

def composite(name, crops):
    W = max(c.size[0] for c in crops)
    H = sum(c.size[1] for c in crops) + 8 * (len(crops) - 1)
    canvas = Image.new('RGB', (W, H), (200, 60, 60))
    y = 0
    for c in crops:
        canvas.paste(c, (0, y)); y += c.size[1] + 8
    canvas.save(f'{OUT}/{name}.png'); print(name, canvas.size)

# S1 — p60 : encadré du hadith (9 lignes, 4 bandes pleine largeur)
composite('s1', [
    crop(60, 0.660, 0.735, 0.06, 0.94),
    crop(60, 0.735, 0.810, 0.06, 0.94),
    crop(60, 0.810, 0.885, 0.06, 0.94),
    crop(60, 0.885, 0.950, 0.06, 0.94),
])

# S2 — p61 : biographie an-Nu'man (3 bandes pleine largeur)
composite('s2', [
    crop(61, 0.170, 0.270, 0.04, 0.96),
    crop(61, 0.270, 0.370, 0.04, 0.96),
    crop(61, 0.370, 0.470, 0.04, 0.96),
])

# S3 — p62 : titre أولا + intro + item 1 + āyāt + item 2 + āyāt (5 bandes)
composite('s3', [
    crop(62, 0.220, 0.300, 0.04, 0.96),   # ligne الأشياء... ثلاثة أقسام
    crop(62, 0.300, 0.380, 0.04, 0.96),   # item 1 : فما نص الله على تحليله...
    crop(62, 0.380, 0.460, 0.04, 0.96),   # āyāt item 1 + refs + ونحو ذلك
    crop(62, 0.460, 0.540, 0.04, 0.96),   # item 2 : وما نص الله على تحريمه...
    crop(62, 0.540, 0.620, 0.04, 0.96),   # āyāt item 2 + refs + وقوله
])

# S4 — p63 : fushak + qarib + āya + fahiya (3 bandes pleine largeur)
composite('s4', [
    crop(63, 0.560, 0.640, 0.04, 0.96),
    crop(63, 0.640, 0.720, 0.04, 0.96),
    crop(63, 0.720, 0.800, 0.04, 0.96),
])

print('OK zooms5')
