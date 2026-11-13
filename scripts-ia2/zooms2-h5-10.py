#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — ultra-zooms 600 dpi natif, demi-bandes empilées (leçon 10 hadith-5ep)
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-10/zooms2'
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

def halves_band(pg, y0, y1, x0=0.0, x1=1.0):
    """A band cut in two overlapping halves, stacked vertically (keeps native 600dpi)."""
    im = page600(pg); w, h = im.size
    band = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    bw, bh = band.size
    mid = int(bw * 0.56)
    right = band.crop((0, 0, mid, bh))       # right half (start of Arabic line)
    left = band.crop((bw - mid, 0, bw, bh))  # left half
    canvas = Image.new('RGB', (mid, bh*2 + 10), (180, 180, 180))
    canvas.paste(right, (0, 0)); canvas.paste(left, (0, bh + 10))
    return canvas

def composite(name, pieces):
    W = max(p.size[0] for p in pieces)
    H = sum(p.size[1] for p in pieces) + 10 * (len(pieces) - 1)
    canvas = Image.new('RGB', (W, H), (120, 120, 120))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y)); y += p.size[1] + 10
    canvas.save(f'{OUT}/{name}.png'); print(name, canvas.size)

# W1 — tamhīd L1 (أذن) + rāwī L4 (معالية) + rāwī L5-6 (حمص + date)
composite('w1', [
    halves_band(60, 0.395, 0.475, 0.30, 1.0),
    halves_band(61, 0.240, 0.295, 0.30, 1.0),
    halves_band(61, 0.293, 0.352, 0.25, 1.0),
])

# W2 — p62 : āyas item 1 (2 lignes) + āyas item 2 haut p62-B (2 lignes)
composite('w2', [
    halves_band(62, 0.310, 0.352, 0.05, 1.0),
    halves_band(62, 0.348, 0.398, 0.05, 1.0),
    halves_band(62, 0.545, 0.595, 0.05, 1.0),
    halves_band(62, 0.590, 0.645, 0.05, 1.0),
])

# W3 — p62 item 3 + p63 qila 3 + bullet 2
composite('w3', [
    halves_band(62, 0.690, 0.830, 0.20, 1.0),
    halves_band(63, 0.272, 0.338, 0.25, 1.0),
    halves_band(63, 0.430, 0.505, 0.25, 1.0),
])

# W4 — p63 milieu (المرعى المنعو + āya + فهي عن الاقتراب) + التزينة + p64 Ibn Raǧab
composite('w4', [
    halves_band(63, 0.545, 0.755, 0.10, 1.0),
    halves_band(63, 0.890, 0.980, 0.25, 1.0),
    halves_band(64, 0.455, 0.610, 0.15, 1.0),
])

print('OK zooms2')
