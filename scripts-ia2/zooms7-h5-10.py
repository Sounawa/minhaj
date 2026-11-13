#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — zooms razor 600 dpi (aucun downscale) — points finaux leçon 10
import os
from PIL import Image

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-10'
OUT = f'{BASE}/zooms7'
os.makedirs(OUT, exist_ok=True)
_im = {}

def page600(pg):
    if pg not in _im:
        _im[pg] = Image.open(f'{BASE}/zooms4/p600-{pg}.png')
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

# w1 — p63 : قارب... / فهي عن الاقتراب... / les deux tirets
composite('w1', [
    crop(63, 0.585, 0.655, 0.40, 0.80),   # لأن من قارب النهي/الشرع خالطه غالبا. قال
    crop(63, 0.655, 0.715, 0.06, 0.46),   # فهي تنهى/عن الاقتراب حدًى/حذرا من
    crop(63, 0.805, 0.900, 0.48, 0.98),   # tiret 1 : التنبيه إلى ترك كل ما يوصل
    crop(63, 0.900, 0.990, 0.48, 0.98),   # tiret 2 : الدعوة إلى التربية/التزية
])
# w2 — p64 : فأما من كان عالما بها / واتبَعَ ما دَلَّهُ عليها
composite('w2', [
    crop(64, 0.445, 0.505, 0.38, 0.80),   # فأما/فلما من كان عالما بها
    crop(64, 0.495, 0.555, 0.08, 0.52),   # واتبَعَ ما دلَّ/دلَّهُ عليها
])
print('OK zooms7')
