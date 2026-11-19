#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — extraction TEXTE BLEU (B-R>40) sur cellules jaunes / fond blanc, et
# TEXTE BLANC dans bandeaux bleus (B-R>40 & lum élevé) — tesseract psm 6/7.
import subprocess
import numpy as np
from PIL import Image

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0

def blue_text(pg, y0, y1, x0, x1, tag, psms=(6, 7)):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    R, G, B = c[:,:,0], c[:,:,1], c[:,:,2]
    is_blue = (B - R > 40) & (B > 140)
    lum = c.mean(axis=2)
    out = np.full(lum.shape, 255, np.uint8)
    out[is_blue] = 0                      # texte bleu → noir
    img = Image.fromarray(out)
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    fp = f'{DIR}/strips/{tag}-bluetxt.png'
    img.save(fp)
    res = []
    for psm in psms:
        base = f'{DIR}/strips/{tag}-bluetxt'
        subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                        '--psm', str(psm)], capture_output=True)
        txt = open(base + '.txt', encoding='utf-8').read().strip()
        res.append((psm, txt))
    return res

def white_on_blue(pg, y0, y1, x0, x1, tag, psms=(6, 7)):
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('RGB')
    c = np.array(im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))).astype(int)
    R, G, B = c[:,:,0], c[:,:,1], c[:,:,2]
    is_blue = (B - R > 40) & (B > 140)
    lum = c.mean(axis=2)
    out = np.full(lum.shape, 255, np.uint8)
    out[is_blue & (lum > 190)] = 0         # texte blanc/crème dans la bande bleue → noir
    img = Image.fromarray(out)
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    fp = f'{DIR}/strips/{tag}-white.png'
    img.save(fp)
    res = []
    for psm in psms:
        base = f'{DIR}/strips/{tag}-white'
        subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                        '--psm', str(psm)], capture_output=True)
        txt = open(base + '.txt', encoding='utf-8').read().strip()
        res.append((psm, txt))
    return res

ZONES = [
    # table p.40 : en-têtes bleus sur cellules jaunes — par bande horizontale
    ('t40-head-r1', 40, 100, 140, 580, 118, 145),   # ligne 1 droite
    ('t40-head-r1b', 40, 100, 60, 260, 100, 145),   # ligne 1 gauche (التعليل ?)
    ('t40-head-r2', 40, 143, 60, 460, 143, 168),    # ligne 2 (في البر / في الإثم ?)
    ('t40-head-all', 40, 98, 60, 585, 98, 168),
    # bandeaux bleus à texte blanc
    ('b36-cartouche', 36, 52, 90, 550, 52, 152),
    ('b36-tamhid', 36, 320, 150, 565, 320, 356),
    ('b36-hadith', 36, 492, 150, 565, 492, 546),
    ('b37-tarjama', 37, 84, 150, 565, 84, 114),
    ('b37-tahlil', 37, 540, 380, 575, 540, 568),
    ('b39-taqwim', 39, 578, 150, 575, 578, 632),
    ('b40-istithmar', 40, 308, 145, 575, 308, 382),
    ('b40-iidad', 40, 594, 145, 575, 594, 626),
]

for mode, pg, x0, x1, ya, yb, tag in [(m, p, a, b, c, d, t) for (t, p, c, d, a, b, m) in
        [(z[0], z[1], z[4], z[5], z[2], z[3], z[6]) for z in []]]:
    pass

# exécution directe
print('===== TABLE p40 (texte bleu sur jaune) =====')
for tag, pg, y0, y1, x0, x1 in [
    ('t40-head-all', 40, 98, 168, 60, 585),
    ('t40-head-r1', 40, 100, 145, 60, 585),
    ('t40-head-r2', 40, 143, 168, 60, 585),
]:
    print(f'--- {tag} ---')
    for psm, txt in blue_text(pg, y0, y1, x0, x1, tag):
        print(f'  [psm{psm}] {txt[:200]}')

print('===== BANDEAUX (texte blanc sur bleu) =====')
for tag, pg, y0, y1, x0, x1 in [
    ('b36-cartouche', 36, 52, 152, 90, 550),
    ('b36-tamhid', 36, 320, 356, 150, 565),
    ('b36-hadith', 36, 492, 546, 150, 565),
    ('b37-tarjama', 37, 84, 114, 150, 565),
    ('b37-tahlil', 37, 540, 568, 380, 575),
    ('b39-taqwim', 39, 578, 632, 150, 575),
    ('b40-istithmar', 40, 308, 382, 145, 575),
    ('b40-iidad', 40, 594, 626, 145, 575),
]:
    print(f'--- {tag} ---')
    for psm, txt in white_on_blue(pg, y0, y1, x0, x1, tag):
        if txt: print(f'  [psm{psm}] {txt[:200]}')
