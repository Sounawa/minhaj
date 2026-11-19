#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 7 : anatomie mot-à-mot sur les 8 dernières zones litigieuses.
import subprocess, os
import numpy as np
from PIL import Image
from collections import deque

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/uz6', exist_ok=True)

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
    fp = f'{DIR}/uz6/_t.png'
    img.save(fp)
    base = f'{DIR}/uz6/_t'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

def ccs_of(ink):
    H, W = ink.shape
    lab = np.zeros((H, W), dtype=int); cur = 0
    for i in range(H):
        for j in range(W):
            if ink[i, j] and lab[i, j] == 0:
                cur += 1; q = deque([(i, j)]); lab[i, j] = cur
                while q:
                    y, x = q.popleft()
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = y+dy, x+dx
                            if 0 <= ny < H and 0 <= nx < W and ink[ny, nx] and lab[ny, nx] == 0:
                                lab[ny, nx] = cur; q.append((ny, nx))
    out = []
    for c in range(1, cur+1):
        ys, xs = np.where(lab == c)
        if len(ys) < 3: continue
        out.append((len(ys), ys.min(), ys.max(), xs.min(), xs.max()))
    return out

def zone(pg, x0, y0, x1, y1, tag):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    g = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))
    b = otsu_bin(g)
    cs = (b == 0).sum(axis=0)
    segs, s, last = [], None, 0
    for i, v in enumerate(cs):
        if v > 0:
            if s is None: s = i
            last = i
        else:
            if s is not None and i - last >= 15:
                segs.append((s, last+1)); s = None
    if s is not None: segs.append((s, len(cs)))
    print(f'──── {tag}')
    for a, e in reversed(segs):
        if e - a < 22: continue
        wc = b[:, max(0,a-6):e+6]
        ink = wc == 0
        if ink.sum() < 35: continue
        ccs = sorted(ccs_of(ink), reverse=True)
        body = ccs[0]
        bh = body[2] - body[1]
        up = dn = 0
        for sz, ymin, ymax, xmin, xmax in ccs[1:]:
            if sz > 600: continue
            if ymax < body[1] + bh*0.22: up += 1
            elif ymin > body[2] - bh*0.22: dn += 1
        img = Image.fromarray(wc).resize((wc.shape[1]*3, wc.shape[0]*3), Image.LANCZOS)
        t = ocr(img, 8) or ocr(img, 7)
        print(f'   x={a:>5} h={wc.shape[0]:>3} ↑{up} ↓{dn} nCC={len(ccs)} → «{t.strip()[:38]}»')

zone(41, 60, 350, 570, 380, 'تمهيد L1 (mots)')
zone(43, 400, 702, 565, 736, 'حتى-لو début L2 (mots)')
zone(44, 130, 58, 190, 95, 'ref النور (mots/chiffres)')
zone(44, 70, 496, 565, 536, 'بدعة fin (mots)')
zone(44, 70, 376, 565, 404, 'آل عمران queue (mots)')
zone(45, 70, 694, 565, 724, 'étape3 (mots)')
zone(45, 420, 586, 565, 618, 'أعدّ-عرضا début (mots)')
zone(43, 440, 408, 565, 434, 'وX وسعادة (mot)')
zone(42, 300, 150, 565, 180, 'نزل فيهم (mots)')
