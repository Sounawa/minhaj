#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 v2 — recadrages SANS upscale, contraste ×2.5 pour bandes, psm multiples.
import subprocess, os, re
from PIL import Image, ImageEnhance

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
Image.MAX_IMAGE_PIXELS = None

html = open(f'{DIR}/bbox-11-16.html', encoding='utf-8').read()
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S)

def words_of(pno):
    body = pages[pno - 11][2]
    return [(float(a), float(b), float(c), float(d), t) for a, b, c, d, t in
            re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', body)]

def tess(png, psm, contrast=None):
    img = Image.open(png)
    if contrast:
        img = ImageEnhance.Contrast(img).enhance(contrast)
        png2 = png.replace('.png', f'-c{contrast}.png')
        img.save(png2)
        png = png2
    base = png[:-4] + f'-psm{psm}'
    subprocess.run(['tesseract', png, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True, text=True)
    try:
        return open(base + '.txt', encoding='utf-8').read()
    except FileNotFoundError:
        return ''

# ——— 1. bandes décoratives : pleine largeur, contraste ×2.5, psm 13 + 6 ———
BANDES = [
    (11, 55, 170, 'titre'),
    (11, 160, 208, 'ahdaf'),
    (11, 300, 400, 'tamhid'),
    (11, 462, 548, 'hadith'),
    (12, 55, 122, 'tarjama'),
    (12, 548, 645, 'tahlil'),
    (14, 408, 458, 'sabr'),
    (16, 55, 132, 'taqwim'),
    (15, 305, 370, 'yaghdu'),
]
for p, y1, y2, nom in BANDES:
    img = Image.open(f'{DIR}/r1200/p{p}.png')
    crop = img.crop((0, int(y1 * S), img.width, int(y2 * S)))
    png = f'{DIR}/v2-p{p}-{nom}.png'
    crop.save(png)
    for psm in (13, 6):
        for ct in (None, 2.5):
            txt = tess(png, psm, ct)
            txt = ' ‖ '.join(l.strip() for l in txt.split('\n') if l.strip())
            if txt:
                print(f'p{p} {nom} psm{psm} ct{ct}: {txt[:160]}')
    print()

# ——— 2. zones de texte denses (versets) : psm 6 + 4, sans contraste ———
ZONES = [
    (12, 232, 372, 'fahm-sharh'),
    (13, 150, 195, 'muddathir'),
    (13, 220, 282, 'baqara'),
    (13, 560, 635, 'muminun'),
    (15, 390, 440, 'tawba'),
    (16, 258, 322, 'fussilat'),
    (16, 408, 480, 'sulukat-head'),
    (16, 468, 640, 'sulukat-rows'),
    (12, 145, 175, 'urf'),
    (12, 200, 232, 'wafat'),
]
for p, y1, y2, nom in ZONES:
    img = Image.open(f'{DIR}/r1200/p{p}.png')
    crop = img.crop((0, int(y1 * S), img.width, int(y2 * S)))
    png = f'{DIR}/v2-p{p}-{nom}.png'
    crop.save(png)
    for psm in (6, 4):
        txt = tess(png, psm)
        txt = ' ‖ '.join(l.strip() for l in txt.split('\n') if l.strip())
        if txt:
            print(f'p{p} {nom} psm{psm}: {txt[:220]}')
    print()
