#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — ultra-zooms 2400 dpi (pdftoppm -x -y -W -H) + binarisation + psm 7/6/8.
import subprocess, os
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
TESS = '/home/z/my-project/scripts-translate/tessdata'
R = 2400 / 72.0
os.makedirs(f'{DIR}/uz', exist_ok=True)

# (tag, page, x0, y0, x1, y1) en pt
ZONES = [
    ('u41-tamhid1',    41, 60, 355, 570, 384),
    ('u41-ahdaf2',     41, 70, 240, 570, 266),
    ('u41-cartouche',  41, 70,  66, 565, 140),
    ('u42-awwalan1',   42, 330, 582, 565, 612),
    ('u42-tawba-ref',  42, 240, 226, 470, 254),
    ('u42-aya-start',  42, 70, 148, 565, 178),
    ('u42-sharh2',     42, 380, 330, 565, 400),
    ('u43-taqwa-blk',  43, 70, 356, 565, 430),
    ('u43-hatta',      43, 70, 678, 565, 716),
    ('u43-maqasid2',   43, 70, 528, 565, 560),
    ('u44-imran-ref',  44, 70, 351, 565, 400),
    ('u44-bida-last',  44, 70, 494, 565, 532),
    ('u44-nur-ref',    44, 370, 62, 565, 94),
    ('u44-nisa-ref',   44, 370, 124, 565, 160),
    ('u44-bida-mid',   44, 70, 448, 565, 478),
    ('u45-tq1',        45, 70, 112, 565, 140),
    ('u45-tq2',        45, 70, 138, 565, 166),
    ('u45-tq4',        45, 70, 182, 565, 212),
    ('u45-tq5',        45, 70, 208, 565, 234),
    ('u45-nass-a',     45, 70, 405, 565, 434),
    ('u45-nass-b',     45, 70, 432, 565, 462),
    ('u45-nass-d',     45, 70, 478, 565, 512),
    ('u45-ist1',       45, 70, 543, 565, 576),
    ('u45-ist3',       45, 70, 686, 565, 720),
    ('u45-ban2',       45, 200, 224, 440, 264),
]

def binarize(g):
    h, _ = np.histogram(g, bins=32, range=(0, 255))
    cum = np.cumsum(h); total = cum[-1]
    best, bthr = -1, 128
    for i in range(31):
        w0 = cum[i]; w1 = total - w0
        if w0 == 0 or w1 == 0: continue
        m0 = (np.arange(32)[:i+1] * h[:i+1]).sum() / w0
        m1 = (np.arange(32)[i+1:] * h[i+1:]).sum() / w1
        v = w0 * w1 * (m0 - m1) ** 2
        if v > best: best, bthr = v, (i + .5) * 8
    return np.where(g < bthr, 0, 255).astype(np.uint8)

for tag, pg, x0, y0, x1, y1 in ZONES:
    png = f'{DIR}/uz/{tag}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '2400',
                        '-x', str(int(x0*R)), '-y', str(int(y0*R)),
                        '-W', str(int((x1-x0)*R)), '-H', str(int((y1-y0)*R)),
                        '-f', str(pg), '-l', str(pg), SRC, f'{DIR}/uz/q{tag}'], check=True)
        got = [f for f in os.listdir(f'{DIR}/uz') if f.startswith(f'q{tag}-')]
        os.rename(f'{DIR}/uz/{got[0]}', png)
    c = np.array(Image.open(png).convert('RGB')).astype(int)
    g = c.mean(axis=2)
    outs = [(f'{tag}-bin', binarize(g))]
    sat = c.max(axis=2) - c.min(axis=2)
    m = sat > 35
    if m.sum() > 400:
        lum = g[m]; med = np.median(lum)
        if med > 140:
            outs.append((f'{tag}-colD', np.where(m & (g < med - 40), 0, 255).astype(np.uint8)))
        else:
            outs.append((f'{tag}-colL', np.where(m & (g > med + 40), 0, 255).astype(np.uint8)))
    print(f'────── {tag}')
    seen = set()
    for name, arr in outs:
        fp = f'{DIR}/uz/{name}.png'
        img = Image.fromarray(arr)
        if img.width > 9000:
            img = img.resize((img.width//2, img.height//2), Image.LANCZOS)
        img.save(fp)
        for psm in (7, 6, 8):
            base = f'{DIR}/uz/{name}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip().replace('\n', ' ⏎ ')
            if len(txt) > 2 and txt[:50] not in seen:
                seen.add(txt[:50])
                print(f'  [{psm}/{name.split("-")[-1]}] {txt[:170]}')
