#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — bande unique cadre p47 (lignes 1-4) 900 dpi
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-07/plates'
im = Image.open(f'{OUT}/p47-900.png')
w, h = im.size
# bande y 0.43-0.62 pleine largeur, coupée en 2 colonnes pour rester lisible
band = im.crop((int(0.02*w), int(0.43*h), int(0.98*w), int(0.62*h)))
bw, bh = band.size
left = band.crop((bw//2, 0, bw, bh))    # moitié gauche (fin des lignes, refs)
right = band.crop((0, 0, bw//2, bh))    # moitié droite (débuts de lignes)
H = max(left.height, right.height)
canvas = Image.new('RGB', (left.width, H*2 + 30), 'white')
canvas.paste(left, (0, 0))
canvas.paste(right, (0, H + 30))
if canvas.width > 1900:
    r = 1900/canvas.width
    canvas = canvas.resize((1900, int(canvas.height*r)), Image.LANCZOS)
canvas.save(f'{OUT}/p47-band1.png')
print('OK', canvas.size)
