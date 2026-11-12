#!/usr/bin/env python3
# Z2-5 — planches de lecture directe hadith-5ep leçon 5 (p.37-41)
from PIL import Image, ImageDraw, ImageFont

D = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-05'
PLATES = {
    's5-A.png': [('p-037.png', 2.2), ('p-038.png', 2.2)],
    's5-B.png': [('p-039.png', 2.2), ('p-040.png', 2.2)],
    's5-C.png': [('p-041.png', 2.2)],
}
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)
except Exception:
    font = ImageFont.load_default()

for out, items in PLATES.items():
    crops = []
    for fn, k in items:
        im = Image.open(f'{D}/{fn}')
        crops.append(im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS))
    pad = 40
    W = max(c.width for c in crops) + 2 * pad
    Ht = sum(c.height + pad * 3 for c in crops) + 60 * len(crops)
    plate = Image.new('RGB', (W, Ht), 'white')
    draw = ImageDraw.Draw(plate)
    y = 0
    for c in crops:
        draw.text((pad, y + 10), f'--- {c.height// (2.2 * 3.7795):.0f}mm zone ---', fill=(0, 100, 0), font=font)
        y += 60
        plate.paste(c, (pad, y + pad))
        y += c.height + pad * 2
        draw.line([(0, y - pad // 2), (W, y - pad // 2)], fill=(120, 120, 120), width=8)
    plate.save(f'{D}/{out}')
    print(out, plate.size)
