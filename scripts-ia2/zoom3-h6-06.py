#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — 3 dernières vérifications : (1) ز de خزيمة, (2) ayah الفرقان p40, (3) cartouche (texte jaune).
import subprocess
import numpy as np
from PIL import Image, ImageOps

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0

# (1) خزيمة : le cluster خ+ز — crop ultra-serré, multiples variantes
im = Image.open(f'{DIR}/r1200/p37.png').convert('L')
c = im.crop((int(424*S), int(226*S), int(452*S), int(252*S)))
c = ImageOps.autocontrast(c)
print('===== khuzayma cluster =====')
for scale in (6, 10):
    for thr in (None, 140):
        img = c.resize((c.width*scale, c.height*scale), Image.LANCZOS)
        if thr:
            a = np.array(img)
            img = Image.fromarray(np.where(a < thr, 0, 255).astype(np.uint8))
        fp = f'{DIR}/zooms/khz-s{scale}-t{thr}.png'
        img.save(fp)
        for psm in (8, 10, 13):
            base = f'{DIR}/zooms/khz-s{scale}-t{thr}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip()
            if txt and len(txt) > 0:
                print(f'  [x{scale} thr{thr} psm{psm}] {txt[:60]}')

# (2) ayah الفرقان p40 (y406-450) — contraste + binarisation douce
im = Image.open(f'{DIR}/r1200/p40.png').convert('L')
c = im.crop((int(95*S), int(404*S), int(560*S), int(452*S)))
c = ImageOps.autocontrast(c)
c = c.resize((c.width*3, c.height*3), Image.LANCZOS)
fp = f'{DIR}/zooms/furqan-aya.png'
c.save(fp)
print('===== ayah al-Furqan =====')
for psm in (7, 6, 13):
    base = f'{DIR}/zooms/furqan-aya'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    txt = open(base + '.txt', encoding='utf-8').read().strip()
    if txt: print(f'  [psm{psm}] {txt[:250]}')

# (3) cartouche : texte JAUNE sur fond bleu (garde les pixels R≈G>>B, rejette bleu/blanc)
im = Image.open(f'{DIR}/r1200/p36.png').convert('RGB')
a = np.array(im.crop((int(85*S), int(50*S), int(555*S), int(155*S)))).astype(int)
R, G, B = a[:,:,0], a[:,:,1], a[:,:,2]
is_yellow = (R > 150) & (G > 130) & (B < 160) & ((R - B) > 40) & ((G - B) > 30)
out = np.full(R.shape, 255, np.uint8)
out[is_yellow] = 0
img = Image.fromarray(out)
img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
fp = f'{DIR}/zooms/cartouche-yellow.png'
img.save(fp)
print('===== cartouche (jaune) =====')
for psm in (6, 7, 4):
    base = f'{DIR}/zooms/cartouche-yellow'
    subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    txt = open(base + '.txt', encoding='utf-8').read().strip()
    if txt: print(f'  [psm{psm}] {txt[:250]}')
# variante : texte BLEU FONCÉ dans le cartouche
is_dark = (a.mean(axis=2) < 100)
out2 = np.full(R.shape, 255, np.uint8)
out2[is_dark] = 0
img2 = Image.fromarray(out2)
img2 = img2.resize((img2.width*2, img2.height*2), Image.LANCZOS)
fp2 = f'{DIR}/zooms/cartouche-dark.png'
img2.save(fp2)
for psm in (6, 4):
    base = f'{DIR}/zooms/cartouche-dark'
    subprocess.run(['tesseract', fp2, base, '-l', 'ara', '--tessdata-dir', TESS,
                    '--psm', str(psm)], capture_output=True)
    txt = open(base + '.txt', encoding='utf-8').read().strip()
    if txt: print(f'  [dark psm{psm}] {txt[:250]}')
