#!/usr/bin/env python3
# Z2-1 — crops 300 dpi (moitiés de pages 13-17, rendu 150 dpi upsclalé ×2)
from PIL import Image
import os
SRC = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01'
for pg in ['013','014','015','016','017']:
    im = Image.open(f'{SRC}/p-{pg}.png')
    w, h = im.size
    top = im.crop((0, 0, w, h//2 + 60))
    bot = im.crop((0, h//2 - 60, w, h))
    for name, part in [(f'{pg}-top', top), (f'{pg}-bot', bot)]:
        up = part.resize((part.width*2, part.height*2), Image.LANCZOS)
        up.save(f'{SRC}/z-{name}.png')
        print(name, up.size, os.path.getsize(f'{SRC}/z-{name}.png'))
