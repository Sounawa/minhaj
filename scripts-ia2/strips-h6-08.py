#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — strips 1200 dpi multi-variantes (autocontraste / binarisation / extraction
# colorée) + tesseract psm 6/7/8/13 sur les zones en dispute de la leçon 7 (pp.46-49).
# CHUNK=1 : bandeaux + structures ; CHUNK=2 : textes disputés ; CHUNK=3 : diagrammes.
import subprocess, os, sys
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/strips', exist_ok=True)
CHUNK = int(os.environ.get('CHUNK', '1'))

# (tag, page, x0, y0, x1, y1) en pt — pleine largeur des lignes concernées
ZONES = [
    # ── CHUNK 1 : bandeaux + zones structurelles ──
    ('z46-cartouche',   46,  60,  64, 580, 148),
    ('z46-band1',       46, 195, 146, 440, 190),
    ('z46-band2',       46, 200, 303, 560, 347),
    ('z47-band',        47, 195,  70, 440, 115),
    ('z48-band',        48, 195,  70, 440, 115),
    ('z48-top',         48,  60,  35, 580, 135),
    ('z49-band',        49, 195,  70, 440, 115),
    ('z49-i3d-band',    49, 200, 352, 440, 397),
    # ── CHUNK 2 : textes disputés ──
    ('z46-item1',       46,  60, 352, 580, 402),
    ('z46-item2',       46,  60, 400, 580, 472),
    ('z46-item3',       46,  60, 470, 580, 548),
    ('z46-item4',       46,  60, 548, 580, 622),
    ('z46-item5',       46,  60, 640, 580, 700),
    ('z47-nass1',       47,  60, 136, 580, 200),
    ('z47-nass2-head',  47,  60, 208, 580, 250),
    ('z47-nass2-mid',   47,  60, 245, 580, 330),
    ('z47-nass2-tail',  47,  60, 325, 580, 362),
    ('z47-nass3a',      47,  60, 374, 580, 410),
    ('z47-nass3b',      47,  60, 405, 580, 445),
    ('z47-nass3c',      47,  60, 440, 580, 480),
    ('z47-qhead',       47,  60, 492, 580, 518),
    # ── CHUNK 3 : activités + diagrammes + projet ──
    ('z48-act1',        48,  60, 125, 580, 178),
    ('z48-tabhead',     48,  60, 165, 580, 195),
    ('z48-tabrows',     48,  60, 190, 580, 355),
    ('z48-act2',        48,  60, 350, 580, 415),
    ('z48-diagram',     48,  60, 413, 580, 610),
    ('z48-bottom',      48,  60, 605, 580, 748),
    ('z49-intro',       49,  60, 118, 580, 162),
    ('z49-step1',       49,  60, 160, 580, 210),
    ('z49-step2',       49,  60, 205, 580, 260),
    ('z49-step3',       49,  60, 255, 580, 330),
    ('z49-i3d',         49,  60, 397, 580, 432),
]

GROUPS = {1: range(0, 8), 2: range(8, 21), 3: range(21, 32)}

def variants(c, tag):
    """c = RGB int array. Produit des PNG binarisés dans strips/."""
    out = []
    g = c.mean(axis=2)
    h, _ = np.histogram(g, bins=32, range=(0, 255))
    cum = np.cumsum(h)
    total = cum[-1]
    best, bthr = -1, (g.min() + g.max()) / 2
    for i in range(32):
        w0 = cum[i]; w1 = total - w0
        if w0 == 0 or w1 == 0: continue
        m0 = (np.arange(32)[:i+1] * h[:i+1]).sum() / w0
        m1 = (np.arange(32)[i+1:] * h[i+1:]).sum() / w1
        v = w0 * w1 * (m0 - m1) ** 2
        if v > best: best, bthr = v, (i + .5) * 8
    a_bin = np.where(g < bthr, 0, 255).astype(np.uint8)
    out.append((f'{tag}-bin', a_bin))
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
    rng = int(np.ptp(g))
    out.append((f'{tag}-ac', np.clip((g - g.min()) * 255 / max(1, rng), 0, 255).astype(np.uint8)))
    return out

PSMS = (6, 7, 13)
for zi in GROUPS[CHUNK]:
    tag, pg, x0, y0, x1, y1 = ZONES[zi]
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    best_txt = {}
    for name, arr in variants(c, tag):
        fp = f'{DIR}/strips/{name}.png'
        img = Image.fromarray(arr).resize((int(arr.shape[1]*1.6), int(arr.shape[0]*1.6)), Image.LANCZOS)
        img.save(fp)
        for psm in PSMS:
            base = f'{DIR}/strips/{name}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip()
            if txt and len(txt) > len(best_txt.get(psm, '')):
                best_txt[psm] = txt
    print(f'───────── {tag} (p{pg} y={y0}-{y1})')
    for psm, txt in sorted(best_txt.items()):
        print(f'  [psm{psm}] {txt[:220]}')
