#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 — recadrages ciblés 1200 dpi + tesseract psm 7/13 (méthode Z2-34/35).
# Zones en points cmap (pdftotext -bbox) → px = pt × 1200/72 (×16.6667).
import subprocess, os
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0

# (page, y1, y2, x1, x2, nom, psm, upscale)
# x=None → pleine largeur
ZONES = [
    (11,  55, 170, None, None, 'titre-bande', 13),
    (11, 165, 205, None, None, 'ahdaf', 13),
    (11, 300, 400, None, None, 'tamhid-bande', 13),
    (11, 465, 548, None, None, 'hadith-bande', 13),
    (12,  55, 120, None, None, 'tarjama-bande', 13),
    (12, 148, 172, None, None, 'urf-gharf', 7),
    (12, 203, 228, None, None, 'wafat-18', 13),
    (12, 232, 372, None, None, 'fahm-sharh-shatr', 13),
    (12, 550, 645, None, None, 'tahlil-bande', 13),
    (13, 155, 190, None, None, 'muddathir', 13),
    (13, 224, 278, None, None, 'baqara', 13),
    (13, 565, 630, None, None, 'muminun', 13),
    (14, 410, 455, None, None, 'sabr-header', 13),
    (15, 310, 365, None, None, 'yaghdu-cite', 13),
    (15, 395, 435, None, None, 'tawba', 13),
    (16,  55, 132, None, None, 'taqwim-bande', 13),
    (16, 262, 318, None, None, 'fussilat', 13),
    (16, 412, 475, None, None, 'sulukat-head', 13),
    (16, 470, 635, None, None, 'sulukat-rows', 6),
]

def run(png, out, psm):
    r = subprocess.run(['tesseract', png, out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       capture_output=True, text=True)
    return open(out, encoding='utf-8').read()

for p, y1, y2, x1, x2, nom, psm in ZONES:
    src = f'{DIR}/r1200/p{p}.png'
    img = Image.open(src)
    W, H = img.size
    box = (int((x1 or 0) * S), int(y1 * S), int((x2 or W / S) * S), int(y2 * S))
    crop = img.crop(box)
    # upscale ×1.6 pour les petites zones (psm13)
    if psm == 13:
        crop = crop.resize((int(crop.width * 1.6), int(crop.height * 1.6)), Image.LANCZOS)
    png = f'{DIR}/c-p{p}-{nom}.png'
    crop.save(png)
    out = f'{DIR}/c-p{p}-{nom}.txt'
    txt = run(png, out, psm)
    print(f'===== p{p} {nom} (y{y1}-{y2}) =====')
    for ln in [l for l in txt.split('\n') if l.strip()]:
        print('  ', ln.strip()[:150])
    print()
