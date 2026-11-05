#!/usr/bin/env python3
"""R610 — crops image 900 dpi des passages incertains de la leçon 28 (p.133-136).
Ancres TSV 300 dpi -> bbox -> crop 900 dpi (échelle ×3), tuiles si trop large.
Jamais deviné : chaque crop sera lu à l'image."""
import os, glob, subprocess, unicodedata
from PIL import Image

BASE = '/home/z/my-project'
os.chdir(BASE)
os.makedirs('tr-tmp/r610/crops', exist_ok=True)
PDF = 'content/textbooks-src/ulum-hadith-1-thanawi.pdf'
PAGES = [133, 134, 135, 136]

DIAC = ''.join(chr(c) for c in range(0x64B, 0x653)) + '\u0670\u0640'

def norm(s):
    return ''.join(ch for ch in s if ch not in DIAC).strip()

# Rendus 300 dpi (TSV) et 900 dpi (crops)
for p in PAGES:
    if not glob.glob(f'tr-tmp/r610/tsv-{p}.png'):
        subprocess.run(['pdftoppm', '-r', '300', '-png', '-f', str(p), '-l', str(p),
                        PDF, f'tr-tmp/r610/tsv-{p}'], check=True)
    if not glob.glob(f'tr-tmp/r610/big-{p}.png'):
        subprocess.run(['pdftoppm', '-r', '900', '-png', '-f', str(p), '-l', str(p),
                        PDF, f'tr-tmp/r610/big-{p}'], check=True)

def page_png(prefix):
    g = sorted(glob.glob(f'tr-tmp/r610/{prefix}-*.png'))
    return g[0] if g else None

def lines_of(page):
    """TSV -> liste de lignes {y0,y1,x0,x1,text} triées par y."""
    png300 = page_png(f'tsv-{page}')
    tsv = png300.replace('.png', '.tsv')
    if not os.path.exists(tsv):
        subprocess.run(['TESSDATA_PREFIX=/tmp/tessdata', 'tesseract', png300, tsv[:-4],
                        '-l', 'ara', '--psm', '6', 'tsv'], check=True,
                       capture_output=True)
    rows = []
    with open(tsv, encoding='utf-8') as f:
        next(f)
        for ln in f:
            c = ln.rstrip('\n').split('\t')
            if len(c) < 12 or c[0] != '5':
                continue
            rows.append(dict(block=c[2], par=c[3], line=c[4],
                             left=int(c[6]), top=int(c[7]),
                             w=int(c[8]), h=int(c[9]), text=c[11]))
    byline = {}
    for r in rows:
        k = (r['block'], r['par'], r['line'])
        d = byline.setdefault(k, dict(x0=r['left'], y0=r['top'],
                                      x1=r['left'] + r['w'], y1=r['top'] + r['h'],
                                      words=[]))
        d['x0'] = min(d['x0'], r['left']); d['y0'] = min(d['y0'], r['top'])
        d['x1'] = max(d['x1'], r['left'] + r['w']); d['y1'] = max(d['y1'], r['top'] + r['h'])
        d['words'].append(r['text'])
    out = [dict(x0=d['x0'], y0=d['y0'], x1=d['x1'], y1=d['y1'], text=' '.join(d['words']))
           for d in byline.values()]
    out.sort(key=lambda L: L['y0'])
    return out

def find_line(ls, anchor):
    for i, L in enumerate(ls):
        if anchor in norm(L['text']):
            return i
    return None

# (page, tag, ancre_normalisée, lignes_avant, lignes_après)
TARGETS = [
    (133, 'bayt-tamhid',   'قصر',     1, 2),
    (133, 'sharh',         'المصنوع', 0, 2),
    (134, 'def-bqle',      'بقوله',   0, 4),
    (134, 'nazar',         'نظر',     1, 2),
    (134, 'khab-dunya',    'الدنيا',  0, 1),
    (134, 'maida',         'المعدة',  0, 1),
    (135, 'qism1',         'الخبيثة', 1, 1),
    (135, 'shaytan',       'الشيطان', 0, 1),
    (135, 'asbab-bullets', 'الاكتساب', 2, 2),
    (136, 'khatima',       'البيقوني', 0, 3),
    (136, 'mughira',       'المغيرة', 0, 4),
    (136, 'muslim',        'الكاذبين', 1, 2),
    (136, 'atamal',        'أتأمل',   0, 4),
]

for page, tag, anchor, bef, aft in TARGETS:
    ls = lines_of(page)
    i = find_line(ls, anchor)
    if i is None:
        print(f'!! ancre introuvable p{page} {tag} ({anchor})')
        continue
    a, b = max(0, i - bef), min(len(ls) - 1, i + aft)
    x0 = min(ls[k]['x0'] for k in range(a, b + 1)) - 40
    y0 = min(ls[k]['y0'] for k in range(a, b + 1)) - 40
    x1 = max(ls[k]['x1'] for k in range(a, b + 1)) + 40
    y1 = max(ls[k]['y1'] for k in range(a, b + 1)) + 40
    big = page_png(f'big-{page}')
    im = Image.open(big)
    W, H = im.size
    sx0 = max(0, x0 * 3); sy0 = max(0, y0 * 3)
    sx1 = min(W, x1 * 3); sy1 = min(H, y1 * 3)
    crop = im.crop((sx0, sy0, sx1, sy1))
    MAXW = 5600
    if crop.size[0] > MAXW:
        n = (crop.size[0] + MAXW - 1) // MAXW
        step = crop.size[0] // n
        for t in range(n):
            tx0 = t * step
            tx1 = min(crop.size[0], tx0 + step + 300)
            crop.crop((tx0, 0, tx1, crop.size[1])).save(
                f'tr-tmp/r610/crops/{tag}-p{page}-t{t}.png')
        print(f'OK p{page} {tag}: {n} tuiles y={y0}-{y1}')
    else:
        crop.save(f'tr-tmp/r610/crops/{tag}-p{page}.png')
        print(f'OK p{page} {tag}: 1 tuile y={y0}-{y1} w={sx1-sx0}')
