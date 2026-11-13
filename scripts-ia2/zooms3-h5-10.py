#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — adjudication finale leçon 10 : bandes 600 dpi en 3 strips verticaux avec recouvrement
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-10/zooms3'
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

def strips3(pg, y0, y1):
    """Full-width band cut in 3 overlapping vertical strips, stacked."""
    im = page600(pg); w, h = im.size
    band = im.crop((0, int(y0*h), w, int(y1*h)))
    bw, bh = band.size
    s = int(bw * 0.42)
    cuts = [(bw - s, 0, bw, bh), (int(bw*0.29), 0, int(bw*0.29)+s, bh), (0, 0, s, bh)]
    canvas = Image.new('RGB', (s, bh*3 + 20), (120, 120, 120))
    for i, c in enumerate(cuts):
        canvas.paste(band.crop(c), (0, i*(bh+10)))
    return canvas

def composite(name, pieces):
    W = max(p.size[0] for p in pieces)
    H = sum(p.size[1] for p in pieces) + 10 * (len(pieces) - 1)
    canvas = Image.new('RGB', (W, H), (200, 60, 60))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y)); y += p.size[1] + 10
    canvas.save(f'{OUT}/{name}.png'); print(name, canvas.size)

# V1 — tamhīd L1-L2 + rāwī L3-L5 + Ibn Raǧab (p64)
composite('v1', [
    strips3(60, 0.388, 0.478),
    strips3(61, 0.232, 0.358),
    strips3(64, 0.400, 0.560),
])

# V2 — p62 āyas item 1 (2 lignes calligraphiées + refs)
composite('v2', [
    strips3(62, 0.312, 0.352),
    strips3(62, 0.348, 0.398),
])

# V3 — p62-B āyas item 2 (2 lignes + refs) + entame item 3
composite('v3', [
    strips3(62, 0.543, 0.592),
    strips3(62, 0.588, 0.648),
    strips3(62, 0.688, 0.760),
])

# V4 — p62 item 3 suite (النمور + quote) + p63 qila 3 + bullet 2
composite('v4', [
    strips3(62, 0.755, 0.838),
    strips3(63, 0.268, 0.348),
    strips3(63, 0.428, 0.508),
])

# V5 — p63 milieu (المرعى المنعو + āya + غالبا + الاقتراب) + التزينة
composite('v5', [
    strips3(63, 0.540, 0.762),
    strips3(63, 0.882, 0.982),
])

print('OK zooms3')
