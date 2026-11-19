#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — micro-anatomie finale : 3 zones lettre-à-lettre.
# A: mot disputé du header questions p.47 (أغلاه? / وأحللها?)
# B: «كل سلامى من الناس [عليه?] ...» l.1 p.46
# C: ligne médiane du hadith de l'item 2 p.46
# D: «فانثروا» — points du ن p.47
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/micro', exist_ok=True)

ZONES = [
    ('A-qword',   47, 325, 490, 410, 520),
    ('B-salami1', 46, 240, 424, 520, 452),
    ('C-midline', 46,  60, 436, 560, 464),
    ('D-fanthru', 47, 320, 390, 470, 416),
]

def dilate(a, k=2):
    b = a.copy()
    for _ in range(k):
        b = np.minimum.reduce([b, np.roll(b, 1, 0), np.roll(b, -1, 0),
                               np.roll(b, 1, 1), np.roll(b, -1, 1)])
    return b

for tag, pg, x0, y0, x1, y1 in ZONES:
    im = np.array(Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB'))
    c = im[int(y0*S):int(y1*S), int(x0*S):int(x1*S), :].astype(int)
    g = c.mean(axis=2)
    outs = []
    # otsu bin
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
    b = np.where(g < bthr, 0, 255).astype(np.uint8)
    outs.append(('bin', b))
    outs.append(('dil', dilate(b)))
    outs.append(('thr110', np.where(g < 110, 0, 255).astype(np.uint8)))
    outs.append(('thr150', np.where(g < 150, 0, 255).astype(np.uint8)))
    print(f'══════ {tag} (p{pg} x={x0}-{x1} y={y0}-{y1})')
    for name, arr in outs:
        fp = f'{DIR}/micro/{tag}-{name}.png'
        img = Image.fromarray(arr).resize((int(arr.shape[1]*2.2), int(arr.shape[0]*2.2)), Image.LANCZOS)
        img.save(fp)
        for psm in (7, 6, 8):
            base = f'{DIR}/micro/{tag}-{name}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip().replace('\n', ' | ')
            if len(txt) > 1:
                print(f'  [{name}/psm{psm}] {txt[:130]}')
