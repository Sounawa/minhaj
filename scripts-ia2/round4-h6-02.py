#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 v4 — lignes 1200 dpi pour relecture VLM (versets muminun/baqara, cellule
# sulukat L1, cartouche أحاديث) + analyse CC des chiffres de références.
import re, subprocess, os
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02'
S12 = 1200 / 72.0
Image.MAX_IMAGE_PIXELS = None

# ——— 1. recadrages fins 1200 dpi ———
CROPS = [
    ('muminun-l1', 13, 576, 604, None, None),
    ('muminun-l2', 13, 604, 630, None, None),
    ('baqara-l1', 13, 228, 256, None, None),
    ('baqara-l2', 13, 253, 284, None, None),
    ('sulukat-r1', 16, 492, 528, None, None),
    ('ahadith-cart', 11, 138, 175, None, None),
    ('tawba-l2', 15, 407, 432, None, None),
]
for nom, p, y1, y2, x1, x2 in CROPS:
    img = Image.open(f'{DIR}/r1200/p{p}.png')
    W = img.width
    crop = img.crop((int((x1 or 0) * S12), int(y1 * S12), int((x2 or W / S12) * S12), int(y2 * S12)))
    crop.save(f'{DIR}/v4-{nom}.png')
    print(f'{nom}: {crop.size[0]}x{crop.size[1]}px')

# ——— 2. CC des chiffres de références ———
html = open(f'{DIR}/bbox-11-16.html', encoding='utf-8').read()
pages = re.findall(r'<page width="[\d.]+" height="[\d.]+">(.*?)</page>', html, re.S)

def digit_words(pno, ymin, ymax):
    body = pages[pno - 11]
    out = []
    for a, b, c, d, t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', body):
        if ymin <= float(b) <= ymax and re.fullmatch(r'[0-9٠-٩]+', t.strip()):
            out.append((float(a), float(b), float(c), float(d), t.strip()))
    out.sort(key=lambda w: -w[0])  # droite→gauche
    return out

REFS = [
    ('baqara-ref', 13, 262, 278),
    ('muminun-ref', 13, 610, 626),
    ('fussilat-ref', 16, 305, 318),
]
for nom, pno, y1, y2 in REFS:
    dws = digit_words(pno, y1, y2)
    print(f'--- {nom}: {[(w[4], round(w[0])) for w in dws]}')
    img = Image.open(f'{DIR}/r1200/p{pno}.png').convert('L')
    for x1, yy1, x2, yy2, t in dws:
        a = np.array(img.crop((int(x1 * S12) - 6, int(yy1 * S12) - 6,
                               int(x2 * S12) + 6, int(yy2 * S12) + 6)))
        dark = a < 140
        # ascii art 40 col
        h, w = dark.shape
        rows = []
        for r in range(0, h, max(1, h // 18)):
            line = ''
            for c in range(0, w, max(1, w // 44)):
                blk = dark[r:r + max(1, h // 18), c:c + max(1, w // 44)]
                line += '#' if blk.mean() > 0.35 else ('.' if blk.mean() > 0.1 else ' ')
            rows.append(line)
        print(f'  cmap="{t}" x={x1:.0f}-{x2:.0f}pt')
        for r in rows:
            print('   |' + r + '|')

# tawba ref : pas dans cmap → zone complète autour de la fin de verset
img = Image.open(f'{DIR}/r1200/p15.png').convert('L')
zone = (int(180 * S12), int(414 * S12), int(460 * S12), int(432 * S12))
a = np.array(img.crop(zone))
dark = a < 140
h, w = dark.shape
print('--- tawba-ref zone x180-460 y414-432')
for r in range(0, h, max(1, h // 22)):
    line = ''
    for c in range(0, w, max(1, w // 110)):
        blk = dark[r:r + max(1, h // 22), c:c + max(1, w // 110)]
        line += '#' if blk.mean() > 0.35 else ('.' if blk.mean() > 0.1 else ' ')
    print('   |' + line + '|')
