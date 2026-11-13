#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-8 — micro-crops d'adjudication leçon 8 hadith-5ep (pp. 50-55), composites 600 dpi.
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

# composites : liste de (page, y0, y1) en fractions de page
COMPOSITES = {
    'comp-A-hadith': [  # 1re occurrence بينه وبينها (الإلزاء/إلا ذراع) + فيدخلها + أحَدكم
        (50, 0.585, 0.735),
        (51, 0.065, 0.235),
    ],
    'comp-B-samani': [  # السمعاني : ضلّ وتاه / بحار الحيرة / شفاء العيّ / أبصار / فلم يغلبه + آية الأنبياء
        (52, 0.150, 0.240),
        (52, 0.330, 0.560),
    ],
    'comp-C-khawatim': [  # مع الإنسان خائف وجل / الآية المؤمنون / يبدل/تبدل + لقائله / رائغ + نبهت
        (53, 0.400, 0.545),
        (53, 0.520, 0.635),
        (53, 0.600, 0.730),
    ],
    'comp-D-istifad': [  # التعويل/التوكل على كرم الله + يعتدّ بظهور الحال
        (54, 0.125, 0.230),
        (54, 0.285, 0.400),
    ],
}

for name, zones in COMPOSITES.items():
    parts = []
    for pg, y0, y1 in zones:
        im = render(pg)
        w, h = im.size
        crop = im.crop((0, int(h * y0), w, int(h * y1)))
        label = Image.new('RGB', (crop.width, 60), (255, 230, 150))
        d = ImageDraw.Draw(label)
        d.text((20, 15), f'p.{pg}  y={y0:.3f}-{y1:.3f}', fill=(0, 0, 0))
        parts.append(label)
        parts.append(crop)
    W = max(p.width for p in parts)
    H = sum(p.height for p in parts) + 10 * len(parts)
    sheet = Image.new('RGB', (W, H), (255, 255, 255))
    y = 0
    for p in parts:
        sheet.paste(p, (0, y))
        y += p.height + 10
    sheet.save(f'{OUT}/{name}.png')
    print(name, sheet.size)
print('OK')
