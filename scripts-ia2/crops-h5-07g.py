#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-7 — zoom 1200 dpi : réf. de la dernière āya du cadre (p47)
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

OUT = '/home/z/my-project/scripts-ia2/tmp/h5-07/plates'
im = Image.open(f'{OUT}/p47-1200.png')
w, h = im.size
c = im.crop((int(0.01*w), int(0.855*h), int(0.55*w), int(0.925*h)))
if c.width > 1600:
    c = c.resize((1600, int(c.height*1600/c.width)), Image.LANCZOS)
c.save(f'{OUT}/p47-ref-tawba.png')
print('OK', c.size)
