#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 8 : psm13 + dilatation morphologique pour reconnecter les glyphes
# brisés (تمهيد L1 ouverture, بدعة fin, étape3, آل عمران queue, ref النور).
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/uz7', exist_ok=True)

def otsu_bin(g):
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

def dilate(b, k=3):
    pad = k // 2
    out = b.copy()
    H, W = b.shape
    for dy in range(-pad, pad+1):
        for dx in range(-pad, pad+1):
            if dy == 0 and dx == 0: continue
            out = np.minimum(out, np.roll(np.roll(b, dy, 0), dx, 1))
    return out

def ocr(img, psm):
    fp = f'{DIR}/uz7/_t.png'
    img.save(fp)
    base = f'{DIR}/uz7/_t'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

ZONES = [
    ('tamhid-L1',     41, 60, 348, 570, 382),
    ('bida-fin',      44, 70, 494, 565, 534),
    ('etape3',        45, 70, 694, 565, 724),
    ('imran-q',       44, 70, 376, 565, 404),
    ('nur-ref',       44, 132, 58, 195, 96),
    ('tawba-ref',     42, 350, 226, 470, 258),
    ('aad-debut',     45, 380, 586, 565, 620),
]
for tag, pg, x0, y0, x1, y1 in ZONES:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    g = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))
    print(f'── {tag}')
    seen = set()
    for low, high in ((95, 195), (120, 215)):
        g2 = np.clip((g.astype(int)-low)*255/(high-low), 0, 255).astype(np.uint8)
        b = otsu_bin(g2)
        for kd in (0, 2):
            bb = dilate(b, 3) if kd else b
            img = Image.fromarray(bb)
            if img.width < 3000:
                img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
            for psm in (13, 7):
                t = ocr(img, psm).replace('\n', ' ')
                if t.strip() and len(t.strip()) > 4 and t.strip()[:45] not in seen:
                    seen.add(t.strip()[:45])
                    print(f'   [c{low}/d{kd}/{psm}] {t.strip()[:150]}')
