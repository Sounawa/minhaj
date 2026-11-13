#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-8 — micro-crops FINALES (zoom ×2+) — 5 mots décisifs leçon 8.
import subprocess, os
from PIL import Image, ImageDraw

SRC = '/home/z/my-project/minhaj/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-08/crops'
os.makedirs(OUT, exist_ok=True)

def render(pg):
    png = f'{OUT}/hi-{pg}.png'
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(pg), '-l', str(pg),
                        SRC, f'{OUT}/hi-tmp-{pg}'], check=True)
        os.replace(f'{OUT}/hi-tmp-{pg}-{pg:03d}.png', png)
    return Image.open(png)

ZOOMS = [
    # (page, y0, y1, x0, x1, zoom, label)
    (50, 0.660, 0.730, 0.03, 0.97, 1.6, 'p.50 - entre « وبينه » et « فيسبق » : الإلزاء / إلا ذراعًا ؟'),
    (51, 0.105, 0.165, 0.03, 0.97, 1.6, 'p.51 - فيدخلهها (1) + أحَدكم (shadda ?)'),
    (52, 0.180, 0.235, 0.03, 0.97, 1.6, 'p.52 - آية : لا يسأل عما يفعل وهُم يسألون + ref'),
    (52, 0.495, 0.545, 0.03, 0.97, 1.6, 'p.52 - فلـ... نبي مرسل ولا ملك مقرب'),
    (53, 0.590, 0.650, 0.03, 0.97, 1.6, 'p.53 - أن تبدل/يُبَدِّل الحال'),
    (53, 0.630, 0.730, 0.03, 0.97, 1.6, 'p.53 - فساد أو ارتياب أو ...؟ + كما نبهت/ينهى الرواية'),
]

parts = []
for pg, y0, y1, x0, x1, z, label in ZOOMS:
    im = render(pg)
    w, h = im.size
    crop = im.crop((int(w * x0), int(h * y0), int(w * x1), int(h * y1)))
    crop = crop.resize((int(crop.width * z), int(crop.height * z)), Image.LANCZOS)
    lab = Image.new('RGB', (crop.width, 70), (200, 225, 255))
    d = ImageDraw.Draw(lab)
    d.text((20, 20), label, fill=(0, 0, 0))
    parts.append(lab)
    parts.append(crop)

W = max(p.width for p in parts)
H = sum(p.height for p in parts) + 12 * len(parts)
sheet = Image.new('RGB', (W, H), (255, 255, 255))
y = 0
for p in parts:
    sheet.paste(p, (0, y))
    y += p.height + 12
sheet.save(f'{OUT}/comp-E-zoomfinal.png')
print('comp-E', sheet.size)
