#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — strips 1200 dpi multi-variantes (autocontraste / binarisation / extraction
# colorée) + tesseract psm 6/7/8 sur les zones en dispute de la leçon 6 (pp.41-45).
import subprocess, os
import numpy as np
from PIL import Image, ImageOps

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/strips', exist_ok=True)

# (tag, page, x0, y0, x1, y1) en pt — pleine largeur des lignes concernées
ZONES = [
    # p.41 : cartouche titre + أهداف + تمهيد
    ('z41-cartouche',   41, 60,  66, 570, 145),
    ('z41-ahdaf1',      41, 60, 158, 570, 200),
    ('z41-ahdaf2',      41, 60, 200, 570, 245),
    ('z41-ahdaf3',      41, 60, 245, 570, 290),
    ('z41-tamhid1',     41, 60, 358, 570, 385),
    ('z41-tamhid2',     41, 60, 385, 570, 412),
    # p.42 : ترجمة (verset + date) + شرح gloses
    ('z42-tarjama1',    42, 60, 118, 570, 150),
    ('z42-tarjama2',    42, 60, 150, 570, 205),
    ('z42-tarjama3',    42, 60, 205, 570, 260),
    ('z42-sharh',       42, 60, 296, 570, 400),
    ('z42-awwalan',     42, 60, 580, 570, 625),
    # p.43 : ثانياً + تقوى + versets + مقاصد
    ('z43-thaniyan',    43, 60, 290, 570, 335),
    ('z43-taqwa1',      43, 60, 355, 570, 390),
    ('z43-taqwa2',      43, 60, 390, 570, 425),
    ('z43-aya2',        43, 60, 428, 570, 480),
    ('z43-maqasid',     43, 60, 500, 570, 545),
    ('z43-nass-1',      43, 60, 645, 570, 725),
    # p.44 : refs النور/النساء + ثالثاً + آل عمران + البدعة
    ('z44-refs',        44, 60,  62, 570, 155),
    ('z44-thalithan',   44, 60, 180, 570, 215),
    ('z44-imran',       44, 60, 325, 570, 400),
    ('z44-bida1',       44, 60, 420, 570, 465),
    ('z44-bida2',       44, 60, 465, 570, 545),
    # p.45 : تقويم items 1-2 + bandeau2 + النص + استثمار
    ('z45-taqwim12',    45, 60, 112, 570, 230),
    ('z45-ban2',        45, 60, 228, 570, 262),
    ('z45-nass-intro',  45, 60, 376, 570, 412),
    ('z45-item-bida',   45, 60, 412, 570, 500),
    ('z45-istithmar3',  45, 60, 690, 570, 735),
    ('z45-istithmar2',  45, 60, 648, 570, 695),
]

def variants(c, tag):
    """c = RGB int array. Produit des PNG binarisés dans strips/."""
    out = []
    g = c.mean(axis=2)
    # (a) otsu simple
    thr = (g.min() + g.max()) / 2
    h, _ = np.histogram(g, bins=32, range=(0, 255))
    cum = np.cumsum(h)
    total = cum[-1]
    best, bthr = -1, thr
    for i in range(32):
        w0 = cum[i]; w1 = total - w0
        if w0 == 0 or w1 == 0: continue
        m0 = (np.arange(32)[:i+1] * h[:i+1]).sum() / w0
        m1 = (np.arange(32)[i+1:] * h[i+1:]).sum() / w1
        v = w0 * w1 * (m0 - m1) ** 2
        if v > best: best, bthr = v, (i + .5) * 8
    a_bin = np.where(g < bthr, 0, 255).astype(np.uint8)
    out.append((f'{tag}-bin', a_bin))
    # (b) extraction colorée : texte clair sur fond coloré OU foncé sur fond coloré
    sat = c.max(axis=2) - c.min(axis=2)
    m = sat > 35
    if m.sum() > 400:
        lum = g[m]
        med = np.median(lum)
        if med > 140:   # fond clair → texte foncé
            b = np.where(m & (g < med - 40), 0, 255).astype(np.uint8)
            out.append((f'{tag}-colD', b))
        else:           # foncé (bleu) → texte clair/blanc
            b = np.where(m & (g > med + 40), 0, 255).astype(np.uint8)
            out.append((f'{tag}-colL', b))
    # (c) autocontraste global
    rng = int(np.ptp(g))
    out.append((f'{tag}-ac', np.clip((g - g.min()) * 255 / max(1, rng), 0, 255).astype(np.uint8)))
    return out

for tag, pg, x0, y0, x1, y1 in ZONES:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    best_txt = {}
    for name, arr in variants(c, tag):
        fp = f'{DIR}/strips/{name}.png'
        # upscale ×1.6 pour tesseract
        img = Image.fromarray(arr).resize((int(arr.shape[1]*1.6), int(arr.shape[0]*1.6)), Image.LANCZOS)
        img.save(fp)
        for psm in (6, 7):
            base = f'{DIR}/strips/{name}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip()
            if txt and len(txt) > len(best_txt.get(psm, '')):
                best_txt[psm] = txt
    print(f'───────── {tag} (p{pg} y={y0}-{y1})')
    for psm, txt in best_txt.items():
        print(f'  [psm{psm}] {txt[:200]}')
