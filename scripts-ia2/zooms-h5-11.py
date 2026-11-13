#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-12 — zooms 600 dpi leçon 11 (points fins)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-11/zooms'
os.makedirs(OUT, exist_ok=True)
_cache = {}

def page600(pg):
    if pg not in _cache:
        png = f'{OUT}/p600-{pg}.png'
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

# a1 — p66 : «فلما علمت عظيمته إذا صلح وشديدته إذا فسد [جامع العلوم والحكم بتصرف]»
composite('a1', [
    crop(66, 0.635, 0.720, 0.38, 0.76),
    crop(66, 0.635, 0.720, 0.02, 0.40),
])
# a2 — p66 : āya al-Ḥaǧǧ + ref (2 lignes, moitiés)
composite('a2', [
    crop(66, 0.840, 0.905, 0.50, 0.98),
    crop(66, 0.840, 0.905, 0.02, 0.50),
    crop(66, 0.900, 0.965, 0.50, 0.98),
    crop(66, 0.900, 0.965, 0.02, 0.50),
])
# a3 — p67 : «فساده أعظم المقاصد/المقادع» + «وأعظم ذلك كله ... كل حلال» + «والعقلة/الغفلة»
composite('a3', [
    crop(67, 0.125, 0.190, 0.28, 0.66),
    crop(67, 0.575, 0.645, 0.40, 0.80),
    crop(67, 0.640, 0.715, 0.40, 0.80),
])
# a4 — p67 : hadīth Tirmiḏī (2 bandes × moitiés) + ﴿كلا بل ران﴾ + refs
composite('a4', [
    crop(67, 0.730, 0.810, 0.50, 0.98),
    crop(67, 0.730, 0.810, 0.02, 0.50),
    crop(67, 0.805, 0.885, 0.50, 0.98),
    crop(67, 0.805, 0.885, 0.02, 0.50),
    crop(67, 0.880, 0.955, 0.50, 0.98),
    crop(67, 0.880, 0.955, 0.02, 0.50),
])
print('OK zooms h5-11')
