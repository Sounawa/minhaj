#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 v3 — recadrages 600 dpi (T600) + profils d'encre (comptage de lignes des citations).
import subprocess, os
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S6 = 600 / 72.0
Image.MAX_IMAGE_PIXELS = None

ZONES = [
    (12, 148, 172, 'urf600'),
    (12, 205, 228, 'wafat600'),
    (13, 158, 192, 'muddathir600'),
    (13, 228, 280, 'baqara600'),
    (13, 575, 628, 'muminun600'),
    (15, 398, 432, 'tawba600'),
    (16, 265, 320, 'fussilat600'),
    (16, 410, 480, 'sulukat-head600'),
]

def tess(png, psm):
    base = png[:-4] + f'-psm{psm}'
    subprocess.run(['tesseract', png, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True, text=True)
    try:
        return open(base + '.txt', encoding='utf-8').read()
    except FileNotFoundError:
        return ''

for p, y1, y2, nom in ZONES:
    img = Image.open(f'{DIR}/r600/p{p}.png')
    crop = img.crop((0, int(y1 * S6), img.width, int(y2 * S6)))
    png = f'{DIR}/v3-p{p}-{nom}.png'
    crop.save(png)
    for psm in (6, 7, 11):
        txt = tess(png, psm)
        txt = ' ‖ '.join(l.strip() for l in txt.split('\n') if l.strip())
        if txt:
            print(f'p{p} {nom} psm{psm}: {txt[:250]}')
    print()

# ——— profils d'encre : comptage de lignes des citations coraniques ———
def ink_profile(pno, y1, y2, label):
    img = Image.open(f'{DIR}/r600/p{pno}.png').convert('L')
    a = np.array(img)
    zone = a[int(y1 * S6):int(y2 * S6), :]
    dark = (zone < 128).sum(axis=1)
    # lignes = segments continus où densité > seuil
    th = max(3, dark.max() * 0.08)
    inline = dark > th
    lines = []
    start = None
    for i, v in enumerate(inline):
        if v and start is None: start = i
        if not v and start is not None:
            if i - start > 8: lines.append((start, i))
            start = None
    if start is not None and len(inline) - start > 8:
        lines.append((start, len(inline)))
    print(f'{label}: {len(lines)} lignes détectées:', end=' ')
    for s, e in lines:
        print(f'[{y1 + s/S6:.0f}-{y1 + e/S6:.0f}pt]', end=' ')
    print()

ink_profile(13, 165, 200, 'muddathir-zone')
ink_profile(13, 575, 625, 'muminun-zone')
ink_profile(16, 268, 315, 'fussilat-zone')
ink_profile(15, 398, 428, 'tawba-zone')
ink_profile(16, 415, 630, 'table-zone')
