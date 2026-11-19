#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — zoom : tranches fines 1200 dpi + variantes (bin/colD/colL/ac + dilatation)
# + psm 6/7/13 pour les zones encore en dispute de la leçon 7 (pp.46-49).
import subprocess, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/strips', exist_ok=True)
CHUNK = int(os.environ.get('CHUNK', '1'))

ZONES = [
    # ── CHUNK 1 : p.46 items + p.47 disputes ──
    ('w46-item2a',      46,  60, 400, 580, 428),  # كل سلامى l.1
    ('w46-item2b',      46,  60, 424, 580, 452),  # l.2
    ('w46-item2c',      46,  60, 448, 580, 478),  # l.3 والكلمة الطيبة... وتميط
    ('w46-item3a',      46,  60, 476, 580, 504),  # أستدل للمعاني الآتية
    ('w46-item5a',      46,  60, 645, 580, 674),  # أعرّف بالصحابيين (وابصة?)
    ('w47-bandX',       47, 205,  74, 432, 112),  # bandeau النصوص الشرعية?
    ('w47-qhead2a',     47,  60, 478, 580, 506),  # questions header (bleu)
    ('w47-qhead2b',     47,  60, 502, 580, 524),  # header l.2
    ('w47-nass3-verb',  47, 300, 392, 560, 416),  # فانثروا (zone droite)
    ('w47-nass3-x',     47,  60, 434, 580, 462),  # عن [X] إلا القرآن
    ('w47-nass3-tail',  47,  60, 456, 580, 482),  # fin citation + ref
    ('w47-ref1',        47, 380, 182, 560, 198),  # [النساء: 58] digits
    ('w47-ref2',        47, 400, 340, 560, 360),  # [البقرة: 176] digits
    # ── CHUNK 2 : p.48 tableau/act2 + p.49 bandeaux/étapes ──
    ('w48-bandX',       48, 205,  74, 432, 112),  # bandeau أنشطة?
    ('w48-tabhead2',    48,  60, 166, 580, 196),  # entêtes tableau
    ('w48-tabr1',       48,  60, 198, 580, 232),  # الاهتمام بجمال البيئة
    ('w48-tabr2',       48,  60, 230, 580, 262),  # مساعدة الآخرين
    ('w48-tabr3',       48,  60, 260, 580, 295),  # الطهارة
    ('w48-act2a',       48,  60, 352, 580, 380),  # أميّز الحقوق l.1
    ('w48-act2b',       48,  60, 376, 580, 402),  # l.2
    ('w48-act2c',       48,  60, 400, 580, 428),  # أنواع الحقوق
    ('w49-bandX',       49, 205,  74, 432, 112),  # bandeau مشروع?
    ('w49-step1a',      49,  60, 168, 580, 198),  # أقدم خلاصة
    ('w49-step3a',      49,  60, 262, 580, 292),  # أسهم مع أصدقائي
    ('w46-band2x',      46, 205, 305, 560, 345),  # أنجز في دفتري (fin)
]

def dilate(a, k=3):
    b = a.copy()
    for _ in range(k):
        b = np.minimum.reduce([b, np.roll(b, 1, 0), np.roll(b, -1, 0),
                               np.roll(b, 1, 1), np.roll(b, -1, 1)])
    return b

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
    a_bin = np.where(g < bthr, 0, 255).astype(np.uint8)
    out.append((f'{tag}-bin', a_bin))
    out.append((f'{tag}-dil', dilate(a_bin, 2)))
    sat = c.max(axis=2) - c.min(axis=2)
    m = sat > 35
    if m.sum() > 400:
        lum = g[m]; med = np.median(lum)
        if med > 140:
            out.append((f'{tag}-colD', np.where(m & (g < med - 40), 0, 255).astype(np.uint8)))
        else:
            out.append((f'{tag}-colL', np.where(m & (g > med + 40), 0, 255).astype(np.uint8)))
            out.append((f'{tag}-colLd', dilate(np.where(m & (g > med + 40), 0, 255).astype(np.uint8), 2)))
    rng = int(np.ptp(g))
    out.append((f'{tag}-ac', np.clip((g - g.min()) * 255 / max(1, rng), 0, 255).astype(np.uint8)))
    return out

PSMS = (7, 6, 13)
sel = ZONES if CHUNK == 0 else [z for i, z in enumerate(ZONES) if (i // 13) == (CHUNK - 1)]
_cache = {}
for tag, pg, x0, y0, x1, y1 in sel:
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
        for psm in PSMS:
            base = f'{DIR}/strips/{name}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip().replace('\n', ' ⏎ ')
            if len(txt) > 3:
                results.setdefault(psm, []).append((name.split('-')[-1], txt))
    print(f'────── {tag}')
    seen = set()
    for psm, lst in sorted(results.items()):
        for v, txt in lst[:2]:
            if txt[:60] in seen: continue
            seen.add(txt[:60])
            print(f'  [{psm}/{v}] {txt[:190]}')
