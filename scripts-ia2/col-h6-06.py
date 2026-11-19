#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — analyse couleurs des bandeaux cmap-aveugles + extraction adaptée + tesseract.
import subprocess, os
import numpy as np
from PIL import Image, ImageOps

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0

ZONES = [
    ('s36-cartouche', 36, 50, 155, 85, 555),
    ('s36-ban-tamhid', 36, 318, 358, 140, 570),
    ('s36-ban-hadith', 36, 490, 548, 140, 570),
    ('s37-ban-tarjama', 37, 82, 116, 140, 570),
    ('s37-ban-tahlil', 37, 538, 570, 380, 575),
    ('s39-ban-taqwim', 39, 575, 635, 150, 575),
    ('s40-ban-istithmar', 40, 305, 385, 140, 575),
    ('s40-ban-iidad', 40, 592, 628, 140, 575),
    ('s40-table-head2', 40, 100, 168, 60, 580),
]

for tag, pg, y0, y1, x0, x1 in ZONES:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    # couleurs dominantes (quantifiées /32)
    q = (c // 32) * 32
    flat = q.reshape(-1, 3)
    from collections import Counter
    cnt = Counter(map(tuple, flat))
    top = cnt.most_common(5)
    print(f'===== {tag} =====')
    for col, n in top:
        print(f'  RGB{col} × {n} ({100*n/len(flat):.1f}%)')
    # histogramme luminance des pixels saturés
    sat = c.max(axis=2) - c.min(axis=2)
    m = sat > 40
    if m.sum() > 100:
        lum = c.mean(axis=2)[m]
        print(f'  pixels saturés: {m.sum()}, lum min/p10/med/p90/max: {lum.min():.0f}/{np.percentile(lum,10):.0f}/{np.median(lum):.0f}/{np.percentile(lum,90):.0f}/{lum.max():.0f}')
        # binarisation : texte = le plus CONTRASTÉ dans la bande (min ou max de luminance)
        med = np.median(lum)
        v_low = np.where(m & (c.mean(axis=2) < med - 45), 0, 255).astype(np.uint8)
        v_high = np.where(m & (c.mean(axis=2) > med + 45), 0, 255).astype(np.uint8)
        for name, v in (('low', v_low), ('high', v_high)):
            img = Image.fromarray(v)
            img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
            fp = f'{DIR}/strips/{tag}-col-{name}.png'
            img.save(fp)
            for psm in (7, 6):
                base = f'{DIR}/strips/{tag}-col-{name}'
                subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                                '--psm', str(psm)], capture_output=True)
                txt = open(base + '.txt', encoding='utf-8').read().strip()
                if txt: print(f'  [{name} psm{psm}] {txt[:130]}')
