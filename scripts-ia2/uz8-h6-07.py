#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 9 : rendus 1800 dpi par pdftoppm -x -y -W -H (crops sûrs en mémoire)
# pour l'étape 3 + les chiffres de [النور].
import subprocess, os
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
SRC = '/home/z/my-project/content/textbooks-src/hadith-6-ibtidai_text.pdf'
TESS = '/home/z/my-project/scripts-translate/tessdata'
R = 1800 / 72.0
os.makedirs(f'{DIR}/uz8', exist_ok=True)

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

def ocr(img, psm):
    fp = f'{DIR}/uz8/_t.png'
    img.save(fp)
    base = f'{DIR}/uz8/_t'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

ZONES = [
    ('e3',   45, 75, 692, 560, 722),
    ('e3b',  45, 75, 698, 560, 716),
    ('nur',  44, 132, 58, 196, 96),
    ('nur2', 44, 138, 60, 190, 94),
]
for tag, pg, x0, y0, x1, y1 in ZONES:
    png = f'{DIR}/uz8/{tag}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '1800',
                        '-x', str(int(x0*R)), '-y', str(int(y0*R)),
                        '-W', str(int((x1-x0)*R)), '-H', str(int((y1-y0)*R)),
                        '-f', str(pg), '-l', str(pg), SRC, f'{DIR}/uz8/q{tag}'], check=True)
        got = [f for f in os.listdir(f'{DIR}/uz8') if f.startswith(f'q{tag}-')]
        os.rename(f'{DIR}/uz8/{got[0]}', png)
    g = np.array(Image.open(png).convert('L'))
    print(f'── {tag} ({g.shape[1]}x{g.shape[0]})')
    seen = set()
    for low, high in ((90, 195), (115, 210), (100, 205)):
        g2 = np.clip((g.astype(int)-low)*255/(high-low), 0, 255).astype(np.uint8)
        b = otsu_bin(g2)
        for scale in (1, 2):
            img = Image.fromarray(b)
            if scale > 1:
                img = img.resize((b.shape[1]*scale, b.shape[0]*scale), Image.LANCZOS)
            for psm in (6, 7, 13):
                t = ocr(img, psm).replace('\n', ' ')
                if t.strip() and len(t.strip()) > 3 and t.strip()[:45] not in seen:
                    seen.add(t.strip()[:45])
                    print(f'   [c{low}/s{scale}/{psm}] {t.strip()[:160]}')
