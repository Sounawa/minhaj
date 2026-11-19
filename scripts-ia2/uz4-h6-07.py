#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 5 : anatomie des points diacritiques (composantes connexes au-dessus/
# sous la ligne) pour les mots litigieux + lectures ciblées otsu/contraste.
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/uz4', exist_ok=True)

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
    fp = f'{DIR}/uz4/_t.png'
    img.save(fp)
    base = f'{DIR}/uz4/_t'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    return open(base + '.txt', encoding='utf-8').read().strip()

def words_of(b, gap=16):
    cs = (b == 0).sum(axis=0)
    segs, s, last = [], None, 0
    for i, v in enumerate(cs):
        if v > 0:
            if s is None: s = i
            last = i
        else:
            if s is not None and i - last >= gap:
                segs.append((s, last+1)); s = None
    if s is not None: segs.append((s, len(cs)))
    return segs

def anatomy(pg, x0, y0, x1, y1, tag, gap=16):
    """Pour chaque mot (RTL) : composantes connexes = points diacritiques vs corps.
    Un point diacritique = CC de surface < 450px² située nettement au-dessus ou en-dessous
    du corps du mot (ligne médiane)."""
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    g = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))
    b = otsu_bin(g)
    print(f'── {tag}')
    ws = words_of(b, gap)
    for a, e in reversed(ws):
        if e - a < 25: continue
        wc = b[:, max(0,a-4):e+4]
        ink = wc == 0
        if ink.sum() < 40: continue
        # composantes connexes (BFS simple sur 8-voisinage, image petite)
        H, W = ink.shape
        lab = np.zeros((H, W), dtype=int); cur = 0
        from collections import deque
        for i in range(H):
            for j in range(W):
                if ink[i, j] and lab[i, j] == 0:
                    cur += 1
                    q = deque([(i, j)]); lab[i, j] = cur
                    while q:
                        y, x = q.popleft()
                        for dy in (-1, 0, 1):
                            for dx in (-1, 0, 1):
                                ny, nx = y+dy, x+dx
                                if 0 <= ny < H and 0 <= nx < W and ink[ny, nx] and lab[ny, nx] == 0:
                                    lab[ny, nx] = cur; q.append((ny, nx))
        ccs = []
        for c in range(1, cur+1):
            ys, xs = np.where(lab == c)
            if len(ys) < 3: continue
            ccs.append((len(ys), ys.min(), ys.max(), xs.min(), xs.max(), c))
        ccs.sort(reverse=True)
        if not ccs: continue
        body = ccs[0]
        bh = body[2] - body[1]
        # points = petites CC séparées verticalement du corps
        dots_up, dots_dn, big = [], [], 0
        for sz, ymin, ymax, xmin, xmax, c in ccs:
            if sz > max(500, 0.35 * body[0]):
                big += 1; continue
            if ymax < body[1] + bh*0.18:
                dots_up.append((ymin, ymax, xmin, xmax, sz))
            elif ymin > body[2] - bh*0.18:
                dots_dn.append((ymin, ymax, xmin, xmax, sz))
        # regrouper les points proches horizontalement (double-point = 2 CC parfois)
        def group(ds):
            ds = sorted(ds, key=lambda d: d[2])
            out = []
            for d in ds:
                if out and d[2] - out[-1][3] < 6:
                    out[-1] = (out[-1][0], out[-1][1], out[-1][2], max(out[-1][3], d[3]), out[-1][4]+d[4])
                else:
                    out.append(list(d))
            return out
        gu, gd = group(dots_up), group(dots_dn)
        img = Image.fromarray(wc).resize((wc.shape[1]*3, wc.shape[0]*3), Image.LANCZOS)
        t = ocr(img, 8) or ocr(img, 7)
        print(f'   w=[{a}-{e}] pts_haut={len(gu)} pts_bas={len(gd)} grosses_CC={big} → «{t.strip()[:40]}»')

# 1) أولاً : premier mot (entre «أولاً:» et «الموعظة»)
anatomy(42, 440, 583, 565, 614, 'أولاً-mot1 (المنطقة du 1er mot)')
anatomy(42, 470, 583, 565, 614, 'أولاً-mot1 serré')

# 2) غضب/عصب dans la définition de تقوى
anatomy(43, 70, 358, 565, 408, 'تقوى-déf (mots avec points)')

# 3) refs : chiffres — anatomie (petites CC = chiffres ?) + OCR serré
for tag, pg, x0, y0, x1, y1 in (
    ('ref-nur',   44, 75, 62, 215, 95),
    ('ref-nisa',  44, 228, 134, 352, 162),
    ('ref-tawba', 42, 248, 228, 460, 256),
    ('ref-imran', 44, 75, 380, 240, 404),
    ('num-tqw2',  45, 475, 158, 565, 190),   # numéro de l'item «أوضح»
    ('num-ns2',   45, 475, 428, 565, 460),   # numéro item 1 nass
):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    g = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))
    b = otsu_bin(g)
    img = Image.fromarray(b).resize((b.shape[1]*3, b.shape[0]*3), Image.LANCZOS)
    print(f'── {tag}')
    for psm in (7, 8, 13):
        t = ocr(img, psm).replace('\n', ' ')
        if t.strip():
            print(f'   [{psm}] {t.strip()[:90]}')

# 4) lectures ciblées otsu ×4 (contrast boost)
def boost_read(pg, x0, y0, x1, y1, tag, low=90, high=190):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    g = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S))))
    g2 = np.clip((g.astype(int) - low) * 255 / (high - low), 0, 255).astype(np.uint8)
    b = otsu_bin(g2)
    img = Image.fromarray(b).resize((b.shape[1]*2, b.shape[0]*2), Image.LANCZOS)
    print(f'── {tag}')
    seen = set()
    for psm in (7, 6, 8):
        t = ocr(img, psm).replace('\n', ' ')
        if t.strip() and t.strip()[:40] not in seen:
            seen.add(t.strip()[:40])
            print(f'   [{psm}] {t.strip()[:160]}')

boost_read(44, 70, 490, 565, 536, 'bida-dernière-ligne', 100, 200)
boost_read(44, 70, 352, 565, 404, 'imran-fin+ref', 100, 200)
boost_read(43, 70, 686, 565, 716, 'hatta-ligne2', 100, 200)
boost_read(43, 70, 410, 565, 430, 'wX-wasaida', 100, 200)
boost_read(42, 70, 350, 565, 400, 'sharh-glose2', 100, 200)
boost_read(45, 70, 586, 565, 620, 'ichtmrah-taht', 100, 200)
boost_read(45, 70, 696, 565, 724, 'etape3', 100, 200)
boost_read(41, 60, 356, 570, 386, 'tamhid-L1', 60, 170)
boost_read(42, 70, 148, 565, 178, 'tawba-aya-L1', 100, 200)
