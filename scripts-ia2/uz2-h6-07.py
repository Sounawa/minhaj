#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — uz v2 : depuis r1200 + upscale ×2 + segmentation mot-à-mot (projections)
# pour les lignes récalcitrantes ; + zones restantes en traitement simple.
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/uz2', exist_ok=True)

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

def ocr(img, psm):
    fp = f'{DIR}/uz2/_tmp.png'
    img.save(fp)
    base = f'{DIR}/uz2/_tmp'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

# A) lignes récalcitrantes : segmentation mot-à-mot (creux verticaux)
WORD_ZONES = [
    ('x41-tamhid1',  41, 60, 356, 570, 384),
    ('x41-cartouche-droite', 41, 380, 66, 565, 140),   # partie droite cartouche
    ('x42-awwalan-mots', 42, 360, 584, 565, 612),
]
for tag, pg, x0, y0, x1, y1 in WORD_ZONES:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    g = c.mean(axis=2)
    b = binarize(g)
    colsum = (b == 0).sum(axis=0)
    # mots = colonnes d'encre séparées par ≥14px blancs
    words, start, blank = [], 0, 0
    for i, v in enumerate(colsum):
        if v > 0:
            if blank >= 14 and i - blank > start:
                words.append((start, i - blank + 2))
            if v > 0 and blank >= 14:
                start = i - 0
            blank = 0
        else:
            blank += 1
    if len(colsum) and colsum[-1] == 0 and len(colsum) - blank > start:
        words.append((start, len(colsum) - blank))
    # re-segmentation propre
    words, seg, inseg = [], None, 0
    for i, v in enumerate(colsum):
        if v > 0:
            if seg is None: seg = i
            inseg = i
        else:
            if seg is not None and i - inseg >= 14:
                words.append((seg, inseg + 1)); seg = None
    if seg is not None: words.append((seg, len(colsum)))
    print(f'────── {tag} : {len(words)} segments (droite→gauche)')
    res = []
    for a, e in reversed(words):   # RTL
        if e - a < 18: continue
        wc = b[:, max(0, a-6):e+6]
        img = Image.fromarray(wc).resize(((e-a+12)*3, wc.shape[0]*3), Image.LANCZOS)
        t8 = ocr(img, 8).replace('\n', ' ')
        t7 = ocr(img, 7).replace('\n', ' ')
        res.append((a, t8 or t7))
    for a, t in res:
        print(f'   x={a:>5} → {t}')

# B) zones restantes en traitement simple (1200 + upscale ×2, bin, psm 7/6/8)
REST = [
    ('r42-tawba-ref',  42, 240, 224, 470, 256),
    ('r42-aya-start',  42, 70, 146, 565, 180),
    ('r42-sharh2',     42, 380, 330, 565, 400),
    ('r43-taqwa-blk',  43, 70, 356, 565, 430),
    ('r43-hatta',      43, 70, 676, 565, 716),
    ('r43-maqasid2',   43, 70, 526, 565, 560),
    ('r44-imran-ref',  44, 70, 351, 565, 400),
    ('r44-bida-last',  44, 70, 492, 565, 534),
    ('r44-nur-ref',    44, 370, 60, 565, 96),
    ('r44-nisa-ref',   44, 370, 122, 565, 162),
    ('r44-bida-mid',   44, 70, 446, 565, 480),
    ('r45-tq1',        45, 70, 110, 565, 142),
    ('r45-tq2',        45, 70, 138, 565, 168),
    ('r45-tq4',        45, 70, 180, 565, 214),
    ('r45-tq5',        45, 70, 206, 565, 236),
    ('r45-nass-a',     45, 70, 403, 565, 436),
    ('r45-nass-b',     45, 70, 430, 565, 464),
    ('r45-nass-d',     45, 70, 476, 565, 514),
    ('r45-ist1',       45, 70, 541, 565, 578),
    ('r45-ist3',       45, 70, 684, 565, 722),
]
for tag, pg, x0, y0, x1, y1 in REST:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    g = c.mean(axis=2)
    b = binarize(g)
    img = Image.fromarray(b).resize((b.shape[1]*2, b.shape[0]*2), Image.LANCZOS)
    print(f'────── {tag}')
    seen = set()
    for psm in (7, 6, 8):
        t = ocr(img, psm).replace('\n', ' ⏎ ')
        if t and t[:50] not in seen:
            seen.add(t[:50])
            print(f'  [{psm}] {t[:180]}')
