#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 4 : binarisation ADAPTATIVE (moyenne locale) + segmentation ligne/mot
# pour les zones récalcitrantes restantes.
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/uz3', exist_ok=True)

def adapt_bin(g, win=81, k=0.12):
    """Sauvola simplifié via image intégrale."""
    g = g.astype(np.float64)
    ii = np.pad(g, ((1,0),(1,0)), mode='constant').cumsum(0).cumsum(1)
    r = win // 2
    H, W = g.shape
    y0 = np.arange(H)[:,None] - r; y1 = np.arange(H)[:,None] + r + 1
    x0 = np.arange(W)[None,:] - r; x1 = np.arange(W)[None,:] + r + 1
    y0c, y1c = np.clip(y0,0,H), np.clip(y1,0,H)
    x0c, x1c = np.clip(x0,0,W), np.clip(x1,0,W)
    n = (y1c-y0c) * (x1c-x0c)
    s = ii[y1c,x1c] - ii[y0c,x1c] - ii[y1c,x0c] + ii[y0c,x0c]
    m = s / np.maximum(n, 1)
    var = np.maximum((g - m)**2, 0)
    iiv = np.pad(var, ((1,0),(1,0)), mode='constant').cumsum(0).cumsum(1)
    sv = iiv[y1c,x1c] - iiv[y0c,x1c] - iiv[y1c,x0c] + iiv[y0c,x0c]
    sd = np.sqrt(np.maximum(sv / np.maximum(n,1), 0))
    thr = m * (1 + k * (sd / 128 - 1))
    return np.where(g < thr, 0, 255).astype(np.uint8)

def ocr(img, psm):
    fp = f'{DIR}/uz3/_t.png'
    img.save(fp)
    base = f'{DIR}/uz3/_t'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

def get_bin(pg, x0, y0, x1, y1):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    g = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))
    return adapt_bin(g)

def lines_of(b, min_ink=30):
    """segments horizontaux = lignes"""
    rs = (b == 0).sum(axis=1)
    segs, s = [], None
    for i, v in enumerate(rs):
        if v > min_ink:
            if s is None: s = i
        else:
            if s is not None and i - s > 20:
                segs.append((s, i)); s = None
    if s is not None: segs.append((s, len(rs)))
    return segs

def words_of(b):
    cs = (b == 0).sum(axis=0)
    segs, s, last = [], None, 0
    for i, v in enumerate(cs):
        if v > 0:
            if s is None: s = i
            last = i
        else:
            if s is not None and i - last >= 16:
                segs.append((s, last+1)); s = None
    if s is not None: segs.append((s, len(cs)))
    return segs

def read_line_words(b, tag):
    out = []
    for a, e in reversed(words_of(b)):
        if e - a < 20: continue
        wc = b[:, max(0,a-8):e+8]
        img = Image.fromarray(wc).resize((wc.shape[1]*3, wc.shape[0]*3), Image.LANCZOS)
        best = ''
        for psm in (8, 7):
            t = ocr(img, psm)
            if len(t) > len(best): best = t
        out.append(best.strip())
    print(f'   {tag}: ' + ' | '.join(out))

def read_line(b, tag, psms=(7, 6)):
    img = Image.fromarray(b).resize((b.shape[1]*2, b.shape[0]*2), Image.LANCZOS)
    seen = set()
    for psm in psms:
        t = ocr(img, psm).replace('\n', ' ')
        if t and t[:40] not in seen:
            seen.add(t[:40])
            print(f'   {tag}[{psm}] {t[:150]}')

# 1) تمهيد ligne 1 — adaptatif + mots
b = get_bin(41, 60, 354, 570, 386)
print('── p41 تمهيد L1 (adaptatif)')
read_line(b, 'L1')
read_line_words(b, 'L1-mots')

# 2) cartouche : zone chiffre (gauche du titre ?) — scan des 2 côtés
for tag, x0, x1 in (('cart-G', 70, 200), ('cart-D', 430, 565), ('cart-C', 200, 440)):
    b = get_bin(41, x0, 66, x1, 140)
    print(f'── p41 {tag}')
    read_line(b, tag, psms=(6, 7, 8))

# 3) تقوى block — lignes
b = get_bin(43, 70, 354, 565, 432)
print('── p43 تقوى block')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'tq{i}')

# 4) hatta ligne 2 (حتى لو حكم...)
b = get_bin(43, 70, 676, 565, 716)
print('── p43 حتى-لوحكم')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'ht{i}')
    read_line_words(b[a:e], f'ht{i}-mots')

# 5) bida dernière ligne
b = get_bin(44, 70, 490, 565, 534)
print('── p44 bida-last')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'bd{i}')
    read_line_words(b[a:e], f'bd{i}-mots')

# 6) imran fin de verset + ref
b = get_bin(44, 70, 380, 565, 404)
print('── p44 imran end+ref')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'im{i}')

# 7) refs النور / النساء / التوبة — tight crops
for tag, pg, x0, y0, x1, y1 in (
    ('nur', 44, 68, 60, 215, 94),
    ('nisa', 44, 225, 134, 350, 162),
    ('tawba', 42, 400, 226, 515, 258),
):
    b = get_bin(pg, x0, y0, x1, y1)
    print(f'── ref {tag}')
    read_line(b, tag, psms=(7, 8, 6))

# 8) p45 تقويم items — lignes
b = get_bin(45, 70, 108, 565, 236)
print('── p45 تقويم lignes')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'tqw{i}')
read_line_words(b, 'tqw-all')

# 9) p45 nass intro + items — lignes
b = get_bin(45, 70, 403, 565, 514)
print('── p45 nass lignes')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'ns{i}')
    if i >= 1:
        read_line_words(b[a:e], f'ns{i}-mots')

# 10) p45 استثمار intro
b = get_bin(45, 70, 539, 565, 604)
print('── p45 استثمار/إعداد intro')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'is{i}')

# 11) p45 étape 3
b = get_bin(45, 70, 694, 565, 724)
print('── p45 étape3')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'e3-{i}')

# 12) p42 أولاً head (rouge) — adaptatif
b = get_bin(42, 330, 582, 565, 614)
print('── p42 أولاً head')
read_line(b, 'aw')
read_line_words(b, 'aw-mots')

# 13) p42 شرح glose 2
b = get_bin(42, 70, 352, 565, 400)
print('── p42 شرح glose2')
for i, (a, e) in enumerate(lines_of(b)):
    read_line(b[a:e], f'sh{i}')
