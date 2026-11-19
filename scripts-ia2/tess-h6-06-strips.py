#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — tesseract ciblé sur bandes 1200 dpi (mode sombre) + extraction couche colorée
# (saturation/hue) pour les bandeaux cmap-aveugles — leçon 5 «البر حسن الخلق».
import subprocess, os, sys
import numpy as np
from PIL import Image, ImageOps, ImageEnhance

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
os.makedirs(f'{DIR}/strips', exist_ok=True)
S = 1200 / 72.0

def run_tess(png, tag, psms=(6, 4)):
    outs = []
    for psm in psms:
        base = f'{DIR}/strips/{tag}-psm{psm}'
        subprocess.run(['tesseract', png, base, '-l', 'ara', '--tessdata-dir', TESS,
                        '--psm', str(psm)], capture_output=True)
        txt = open(base + '.txt', encoding='utf-8').read().strip()
        outs.append((psm, txt))
    return outs

def strip_dark(pg, y0, y1, x0, x1, tag, psms=(6, 4)):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = ImageOps.autocontrast(c)
    c = c.resize((c.width*2, c.height*2), Image.LANCZOS)
    fp = f'{DIR}/strips/{tag}.png'
    c.save(fp)
    return run_tess(fp, tag, psms)

def strip_color(pg, y0, y1, x0, x1, tag, psms=(6, 4)):
    """Extraction couche colorée : garde les pixels saturés (bande), binarise par luminance locale."""
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    a = np.array(c).astype(int)
    sat = a.max(axis=2) - a.min(axis=2)
    lum = a.mean(axis=2)
    variants = {}
    # V1 : pixels saturés = bande (fond), texte = moins saturé/plus sombre → seuil
    m = sat > 45
    if m.sum() > 50:
        # dans la bande colorée, le texte est plus sombre (bleu foncé) ou clair (jaune/blanc)
        v = np.where(m & (lum < 110), 0, 255).astype(np.uint8)  # texte sombre sur bande claire
        variants['v1'] = v
        v2 = np.where(m & (lum > 165), 0, 255).astype(np.uint8)  # texte clair sur bande foncée
        variants['v2'] = v2
    # V3 : autocontraste simple
    g = np.array(ImageOps.autocontrast(c.convert('L')))
    variants['v3'] = g
    res = {}
    for name, arr in variants.items():
        img = Image.fromarray(arr)
        img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
        fp = f'{DIR}/strips/{tag}-{name}.png'
        img.save(fp)
        res[name] = run_tess(fp, f'{tag}-{name}', psms)
    return res

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    ZONES_COLOR = [
        ('s36-cartouche', 36, 50, 155, 85, 555),
        ('s36-ban-ahdaf', 36, 158, 202, 140, 570),
        ('s36-ban-tamhid', 36, 318, 358, 140, 570),
        ('s36-ban-hadith', 36, 490, 548, 140, 570),
        ('s37-ban-tarjama', 37, 82, 116, 140, 570),
        ('s37-ban-sharh', 37, 358, 398, 380, 575),
        ('s37-ban-istikhlas', 37, 425, 465, 380, 575),
        ('s37-ban-tahlil', 37, 538, 570, 380, 575),
        ('s39-sub-thalith', 39, 70, 100, 150, 570),
        ('s39-ban-mustafad', 39, 405, 442, 200, 575),
        ('s39-ban-taqwim', 39, 575, 635, 150, 575),
        ('s40-ban-istithmar', 40, 305, 385, 140, 575),
        ('s40-table-head', 40, 98, 170, 60, 580),
        ('s40-ban-iidad', 40, 592, 628, 140, 575),
    ]
    ZONES_DARK = [
        ('s36-ref-muslim2', 36, 598, 622, 60, 578, (7, 6)),
        ('s36-ahdaf', 36, 203, 305, 230, 565, (6, 4)),
        ('s36-tamhid', 36, 358, 452, 60, 578, (6, 4)),
        ('s36-question', 36, 455, 488, 60, 578, (7, 6)),
        ('s36-hadith', 36, 548, 612, 60, 578, (6, 4)),
        ('s36-wabisa', 36, 636, 700, 60, 578, (6, 4)),
        ('s36-wabisa-ref', 36, 695, 722, 60, 578, (7, 6)),
        ('s37-nawas1', 37, 118, 145, 60, 578, (7, 6)),
        ('s37-nawas2', 37, 143, 175, 60, 578, (7, 6)),
        ('s37-nawas3', 37, 178, 200, 60, 578, (7, 6)),
        ('s37-wabisa1', 37, 208, 236, 60, 578, (7, 6)),
        ('s37-wabisa2', 37, 236, 262, 60, 578, (7, 6)),
        ('s37-wabisa3', 37, 262, 290, 60, 578, (7, 6)),
        ('s37-wabisa4', 37, 289, 318, 60, 578, (7, 6)),
        ('s37-glose', 37, 398, 430, 190, 560, (7, 6)),
        ('s37-istikhl-items', 37, 462, 532, 230, 545, (6, 4)),
        ('s37-tahlil1', 37, 565, 600, 60, 578, (7, 6)),
        ('s37-tahlil-tafsil', 37, 600, 628, 420, 578, (7, 6)),
        ('s37-awwal-sub', 37, 638, 666, 60, 578, (7, 6)),
        ('s37-awwal-p1', 37, 666, 700, 60, 578, (7, 6)),
        ('s37-awwal-p2', 37, 698, 732, 60, 578, (7, 6)),
        ('s38-citation', 38, 78, 112, 120, 572, (7, 6)),
        ('s38-ulama1', 38, 112, 146, 60, 572, (7, 6)),
        ('s38-ulama2', 38, 144, 172, 60, 572, (7, 6)),
        ('s38-aya-baqara', 38, 170, 290, 60, 582, (6, 4)),
        ('s38-fmajami', 38, 283, 314, 350, 572, (7, 6)),
        ('s38-bir-husn', 38, 313, 348, 60, 572, (7, 6)),
        ('s38-hajj', 38, 344, 376, 130, 572, (7, 6)),
        ('s38-murad1', 38, 377, 412, 60, 572, (7, 6)),
        ('s38-murad2', 38, 410, 437, 60, 572, (7, 6)),
        ('s38-aya-anfal', 38, 437, 545, 60, 582, (6, 4)),
        ('s38-sub-thani', 38, 555, 592, 400, 572, (7, 6)),
        ('s38-thani1', 38, 594, 626, 60, 578, (7, 6)),
        ('s38-thani2', 38, 624, 654, 60, 578, (7, 6)),
        ('s38-thani3', 38, 652, 682, 60, 578, (7, 6)),
        ('s38-thani4', 38, 682, 712, 60, 578, (7, 6)),
        ('s38-thani5', 38, 710, 735, 60, 578, (7, 6)),
        ('s39-alamatayn1', 39, 100, 136, 60, 578, (7, 6)),
        ('s39-alamatayn2', 39, 133, 166, 60, 578, (7, 6)),
        ('s39-laysa1', 39, 168, 200, 60, 578, (7, 6)),
        ('s39-laysa2', 39, 198, 230, 60, 578, (7, 6)),
        ('s39-laysa3', 39, 228, 258, 60, 578, (7, 6)),
        ('s39-laysa4', 39, 256, 287, 60, 578, (7, 6)),
        ('s39-laysa5', 39, 285, 317, 60, 578, (7, 6)),
        ('s39-shubuhat1', 39, 317, 346, 60, 578, (7, 6)),
        ('s39-shubuhat2', 39, 344, 378, 60, 578, (7, 6)),
        ('s39-mustafad1', 39, 443, 478, 60, 578, (7, 6)),
        ('s39-mustafad2', 39, 478, 502, 60, 578, (7, 6)),
        ('s39-mustafad3', 39, 508, 538, 60, 578, (7, 6)),
        ('s39-mustafad4', 39, 544, 574, 60, 578, (7, 6)),
        ('s39-taqwim1', 39, 630, 662, 150, 578, (7, 6)),
        ('s39-taqwim2', 39, 664, 700, 150, 578, (7, 6)),
        ('s40-taqwim3', 40, 70, 100, 280, 570, (7, 6)),
        ('s40-row1a', 40, 170, 195, 60, 580, (7, 6)),
        ('s40-row1b', 40, 194, 213, 60, 580, (7, 6)),
        ('s40-row2', 40, 222, 245, 60, 580, (7, 6)),
        ('s40-row3', 40, 254, 278, 60, 580, (7, 6)),
        ('s40-row4', 40, 285, 305, 60, 580, (7, 6)),
        ('s40-furqan1', 40, 381, 412, 60, 570, (7, 6)),
        ('s40-furqan2', 40, 410, 448, 60, 570, (7, 6)),
        ('s40-act1', 40, 477, 506, 80, 545, (7, 6)),
        ('s40-act2', 40, 510, 540, 80, 545, (7, 6)),
        ('s40-act3', 40, 544, 572, 80, 545, (7, 6)),
        ('s40-ahfaz', 40, 625, 658, 240, 545, (7, 6)),
        ('s40-iidad1', 40, 662, 690, 220, 545, (7, 6)),
        ('s40-iidad2', 40, 688, 700, 200, 545, (7, 6)),
        ('s40-iidad3', 40, 697, 712, 200, 545, (7, 6)),
        ('s40-bottom', 40, 700, 735, 130, 530, (7, 6)),
    ]
    if which in ('all', 'color'):
        for tag, pg, y0, y1, x0, x1 in ZONES_COLOR:
            print(f'===== {tag} =====')
            for name, outs in strip_color(pg, y0, y1, x0, x1, tag).items():
                for psm, txt in outs:
                    if txt: print(f'  [{name} psm{psm}] {txt[:170]}')
    if which in ('all', 'p36'):
        for tag, pg, y0, y1, x0, x1, psms in [z for z in ZONES_DARK if z[1] == 36]:
            print(f'===== {tag} =====')
            for psm, txt in strip_dark(pg, y0, y1, x0, x1, tag, psms):
                print(f'  [psm{psm}] {txt[:220]}')
    if which in ('all', 'p37'):
        for tag, pg, y0, y1, x0, x1, psms in [z for z in ZONES_DARK if z[1] == 37]:
            print(f'===== {tag} =====')
            for psm, txt in strip_dark(pg, y0, y1, x0, x1, tag, psms):
                print(f'  [psm{psm}] {txt[:220]}')
    if which in ('all', 'p38'):
        for tag, pg, y0, y1, x0, x1, psms in [z for z in ZONES_DARK if z[1] == 38]:
            print(f'===== {tag} =====')
            for psm, txt in strip_dark(pg, y0, y1, x0, x1, tag, psms):
                print(f'  [psm{psm}] {txt[:220]}')
    if which in ('all', 'p39'):
        for tag, pg, y0, y1, x0, x1, psms in [z for z in ZONES_DARK if z[1] == 39]:
            print(f'===== {tag} =====')
            for psm, txt in strip_dark(pg, y0, y1, x0, x1, tag, psms):
                print(f'  [psm{psm}] {txt[:220]}')
    if which in ('all', 'p40'):
        for tag, pg, y0, y1, x0, x1, psms in [z for z in ZONES_DARK if z[1] == 40]:
            print(f'===== {tag} =====')
            for psm, txt in strip_dark(pg, y0, y1, x0, x1, tag, psms):
                print(f'  [psm{psm}] {txt[:220]}')
