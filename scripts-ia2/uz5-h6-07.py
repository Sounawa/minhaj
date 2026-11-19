#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 6 : anatomie des CHIFFRES des références (crops exacts bbox) +
# dernières lignes (تمهيد L1, حتى-لو, وX-وسعادة, بدعة fin, آل عمران fin, التوبة آية,
# étape3, أعدّ/بعنوان, شرح gloses, نزل فيهم).
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/uz5', exist_ok=True)

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
    fp = f'{DIR}/uz5/_t.png'
    img.save(fp)
    base = f'{DIR}/uz5/_t'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

def crop_gray(pg, x0, y0, x1, y1):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    return np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))

# ── A) CHIFFRES des références : description morphologique + OCR isolé ──
DIGITS = [
    ('nur-d1', 44, 149, 63, 158, 90),   # 1er chiffre [النور: ?9] (cmap lit 4)
    ('nur-d2', 44, 143, 63, 152, 90),   # 2e chiffre (cmap lit 9)
    ('nisa-d1', 44, 247, 136, 256, 160),# [النساء: 6?] (cmap lit 6)
    ('nisa-d2', 44, 242, 136, 251, 160),# (cmap lit 4)
    ('tawba-d1', 42, 288, 228, 299, 254), # [التوبة: 9?]
    ('tawba-d2', 42, 282, 228, 293, 254), # (cmap lit 3)
    ('imran-d2', 44, 240, 378, 252, 404), # [آل عمران: 10?]
    ('imran-d3', 44, 232, 378, 244, 404), # (cmap lit 3)
]
for tag, pg, x0, y0, x1, y1 in DIGITS:
    g = crop_gray(pg, x0, y0, x1, y1)
    b = otsu_bin(g)
    ink = b == 0
    n = int(ink.sum())
    ys, xs = np.where(ink) if n else (np.array([0]), np.array([0]))
    desc = ''
    if n:
        h, w = ys.max()-ys.min()+1, xs.max()-xs.min()+1
        # trous verticaux (le 4 occidental a un trou, le 5 a une boucle en bas, etc.)
        from collections import deque
        lab = np.zeros(b.shape, dtype=int); cur = 0
        for i in range(b.shape[0]):
            for j in range(b.shape[1]):
                if ink[i, j] and lab[i, j] == 0:
                    cur += 1; q = deque([(i, j)]); lab[i, j] = cur
                    while q:
                        y, x = q.popleft()
                        for dy in (-1,0,1):
                            for dx in (-1,0,1):
                                ny, nx = y+dy, x+dx
                                if 0<=ny<b.shape[0] and 0<=nx<b.shape[1] and ink[ny,nx] and lab[ny,nx]==0:
                                    lab[ny,nx]=cur; q.append((ny,nx))
        sizes = sorted([int((lab==c).sum()) for c in range(1, cur+1)], reverse=True)[:3]
        desc = f'ink={n} bbox={h}x{w} CCs={cur} top3={sizes}'
    img = Image.fromarray(b).resize((b.shape[1]*6, b.shape[0]*6), Image.LANCZOS)
    t = ocr(img, 10) or ocr(img, 8)
    print(f'{tag}: {desc} → OCR «{t.strip()[:20]}»')

# ── B) lignes restantes ──
LINES = [
    ('tamhid-L1',  41, 60, 352, 570, 380),
    ('hatta-L2',   43, 70, 702, 565, 742),
    ('wX-saida',   43, 430, 410, 565, 432),
    ('bida-f1',    44, 70, 486, 565, 512),
    ('bida-f2',    44, 70, 510, 565, 540),
    ('imran-end',  44, 70, 380, 565, 404),
    ('tawba-aya1', 42, 70, 148, 565, 176),
    ('tawba-aya3', 42, 70, 200, 565, 232),
    ('etape3',     45, 70, 696, 565, 722),
    ('aad-bonwan', 45, 420, 586, 565, 616),
    ('glose1',     42, 380, 324, 565, 356),
    ('glose2',     42, 200, 356, 565, 398),
    ('nazel-fihim',42, 300, 150, 565, 178),
]
for tag, pg, x0, y0, x1, y1 in LINES:
    g = crop_gray(pg, x0, y0, x1, y1)
    print(f'── {tag}')
    seen = set()
    for low, high in ((90, 190), (110, 210)):
        g2 = np.clip((g.astype(int)-low)*255/(high-low), 0, 255).astype(np.uint8)
        b = otsu_bin(g2)
        img = Image.fromarray(b).resize((b.shape[1]*2, b.shape[0]*2), Image.LANCZOS)
        for psm in (7, 6):
            t = ocr(img, psm).replace('\n', ' ')
            if t.strip() and t.strip()[:40] not in seen:
                seen.add(t.strip()[:40])
                print(f'   [{psm}] {t.strip()[:150]}')
