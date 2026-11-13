#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-12 — zooms razor leçon 11 (3 lignes restantes)
import os
from PIL import Image

BASE = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-11'
OUT = f'{BASE}/zooms2'
os.makedirs(OUT, exist_ok=True)
_im = {}

def page600(pg):
    if pg not in _im:
        _im[pg] = Image.open(f'{BASE}/zooms/p600-{pg}.png')
    return _im[pg]

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

composite('b1', [
    crop(67, 0.180, 0.235, 0.24, 0.74),   # فصلاح القلب أعظم المصالح وفساده أعظم المقا...
    crop(67, 0.580, 0.640, 0.04, 0.64),   # وأعظم ذلك كله ... كل حلال
    crop(67, 0.635, 0.700, 0.36, 0.98),   # ومما يفسده: هجر القرآن الكريم، وال... عن ذكر الله
    crop(67, 0.690, 0.760, 0.04, 0.64),   # وترك الصلاة والجهل بالدين وفصول الكلام...
])
print('OK b1')
