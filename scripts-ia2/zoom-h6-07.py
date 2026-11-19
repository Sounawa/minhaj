#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — round 2 : tranches fines 1200 dpi + variantes + psm 6/7/8/13.
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/strips', exist_ok=True)

ZONES = [
    ('w41-cartouche',  41, 70,  68, 565, 138),   # cartouche blanc sur bleu
    ('w41-ahdaf2',     41, 75, 243, 560, 268),   # objectif 2
    ('w41-tamhid1a',   41, 70, 358, 565, 380),
    ('w41-tamhid1b',   41, 70, 378, 565, 402),
    ('w42-tarjama1a',  42, 70, 120, 565, 148),   # هو: ... السلمي أبو نجيح
    ('w42-tarjama2a',  42, 70, 150, 565, 178),   # verset التوبة 92 l.1
    ('w42-tarjama2b',  42, 70, 176, 565, 205),   # verset l.2
    ('w42-tarjama3a',  42, 70, 205, 565, 232),   # verset l.3 + ref
    ('w42-tarjama3b',  42, 70, 230, 565, 258),   # توفي سنة 75
    ('w42-awwalanR',   42, 70, 583, 565, 612),   # أولاً (rouge)
    ('w42-awwalanL',   42, 70, 608, 565, 632),   # وصف العرباض...
    ('w43-thaniyanR',  43, 70, 296, 565, 322),   # ثانياً (rouge)
    ('w43-taqwa0',     43, 70, 357, 565, 382),   # 1- تقوى الله تعالى؛ وهي:
    ('w43-taqwa1',     43, 70, 380, 565, 405),   # أن يجعل الإنسان...
    ('w43-taqwa2',     43, 70, 403, 565, 428),   # باتباع الأوامر... سبب كل خير
    ('w43-aya2a',      43, 70, 428, 565, 455),   # وقال عز وجل: ...
    ('w43-aya2b',      43, 70, 453, 565, 480),   # ...فرقانا [ref]
    ('w43-maqasid',    43, 70, 502, 565, 532),   # من مقاصد الإسلام
    ('w43-nass-59a',   43, 70, 578, 565, 608),   # آية النساء 59 (1)
    ('w43-nass-59b',   43, 70, 606, 565, 636),   # آية النساء 59 (2)
    ('w43-samnaa',     43, 70, 668, 565, 712),   # سمعنا وأطعنا حتى لو...
    ('w44-nur-ref',    44, 70,  64, 565,  92),   # [النور: 51?]
    ('w44-nisa-ref',   44, 70, 126, 565, 158),   # [النساء: 65?]
    ('w44-wasaaad',    44, 70, 205, 565, 245),   # أوصى الأمّة بما يقيها
    ('w44-imran1',     44, 70, 328, 565, 355),   # ويساعد على غرس قيم...
    ('w44-imran2',     44, 70, 353, 565, 398),   # آية آل عمران + ref
    ('w44-bida-a',     44, 70, 428, 565, 452),   # وفي قوله ﷺ...
    ('w44-bida-b',     44, 70, 450, 565, 476),   # نهي عن إحداث شيء...
    ('w44-bida-c',     44, 70, 474, 565, 500),   # والبدعة: إحداث...
    ('w44-bida-d',     44, 70, 498, 565, 542),   # أي مقطوع... فلا يدخل
    ('w45-ban2',       45, 208, 226, 432, 262),  # bandeau 2 (blanc/bleu)
    ('w45-ban3',       45, 208, 511, 432, 547),  # bandeau 3
    ('w45-ban1',       45, 208,  75, 432, 111),  # bandeau 1
    ('w45-tq1',        45, 70, 114, 565, 140),   # تقويم item 1
    ('w45-tq2',        45, 70, 138, 565, 163),
    ('w45-tq3',        45, 70, 161, 565, 186),
    ('w45-tq4',        45, 70, 184, 565, 210),
    ('w45-tq5',        45, 70, 208, 565, 232),
    ('w45-nass-a',     45, 70, 407, 565, 432),   # أتأمل النص...
    ('w45-nass-b',     45, 70, 430, 565, 456),   # 1- تعريفا للبدعة
    ('w45-nass-c',     45, 70, 454, 565, 482),   # 2- ?
    ('w45-nass-d',     45, 70, 480, 565, 510),
    ('w45-ist1',       45, 70, 545, 565, 572),   # تحت إشراف...
    ('w45-ist2',       45, 70, 570, 565, 598),
    ('w45-ist5',       45, 70, 692, 565, 718),   # étape 3
]

def variants(c, tag):
    out = []
    g = c.mean(axis=2)
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
    out.append((f'{tag}-bin', np.where(g < bthr, 0, 255).astype(np.uint8)))
    sat = c.max(axis=2) - c.min(axis=2)
    m = sat > 35
    if m.sum() > 400:
        lum = g[m]; med = np.median(lum)
        if med > 140:
            out.append((f'{tag}-colD', np.where(m & (g < med - 40), 0, 255).astype(np.uint8)))
        else:
            out.append((f'{tag}-colL', np.where(m & (g > med + 40), 0, 255).astype(np.uint8)))
    return out

_cache = {}
import os as _os
_chunk = int(_os.environ.get('CHUNK', '0'))
if _chunk:
    ZONES = [z for z in ZONES if (ZONES.index(z) // 24) == (_chunk - 1)]
for tag, pg, x0, y0, x1, y1 in ZONES:
    if pg not in _cache:
        _cache.clear()
        _cache[pg] = np.array(Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB'))
    full = _cache[pg]
    c = full[int(y0*S):int(y1*S), int(x0*S):int(x1*S), :].astype(int)
    results = {}
    for name, arr in variants(c, tag):
        fp = f'{DIR}/strips/{name}.png'
        img = Image.fromarray(arr).resize((int(arr.shape[1]*1.6), int(arr.shape[0]*1.6)), Image.LANCZOS)
        img.save(fp)
        for psm in (7, 6):
            base = f'{DIR}/strips/{name}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip().replace('\n', ' ⏎ ')
            if len(txt) > 3 and txt.count('ض') + txt.count('ص') < len(txt):  # anti-garbage
                results.setdefault(psm, []).append((name.split('-')[-1], txt))
    print(f'────── {tag}')
    seen = set()
    for psm, lst in results.items():
        for v, txt in lst[:2]:
            if txt[:60] in seen: continue
            seen.add(txt[:60])
            print(f'  [{psm}/{v}] {txt[:180]}')
