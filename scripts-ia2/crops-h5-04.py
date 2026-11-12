#!/usr/bin/env python3
# Z2-4 — micro-crops ×280% des zones litigieuses de la leçon 4 hadith-5ep → composite unique
from PIL import Image

D = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-04'
# (fichier, (gauche, haut, droite, bas) en fraction de page, étiquette)
ZONES = [
    ('p-036.png', (0.10, 0.20, 0.95, 0.36), 'A p36 : مقرونًا بـ… الله (معيّة ou محبّة ?) + fsl. 128'),
    ('p-036.png', (0.05, 0.80, 0.98, 1.00), 'B p36 : الأعداد القبلية ligne complète'),
    ('p-034.png', (0.05, 0.10, 0.98, 0.30), 'C p34 : والحاصل… يتتمثل في إخلاص المؤمن…'),
    ('p-032.png', (0.05, 0.30, 0.98, 0.52), 'D p32 : hadith فَعَجِبَنَا لَهُ…'),
    ('p-035.png', (0.05, 0.28, 0.98, 0.50), 'E p35 : تفاسير الأمارات (فساد الأخلاق/العقوق)'),
]

crops = []
for fn, (l, t, r, b), label in ZONES:
    im = Image.open(f'{D}/{fn}')
    W, H = im.size
    box = (int(l * W), int(t * H), int(r * W), int(b * H))
    c = im.crop(box)
    c = c.resize((int(c.width * 2.8), int(c.height * 2.8)), Image.LANCZOS)
    crops.append((c, label))

pad = 30
W = max(c.width for c, _ in crops) + 2 * pad
Ht = sum(c.height + pad * 2 + 70 for c, _ in crops)
out = Image.new('RGB', (W, Ht), 'white')
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(out)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)
except Exception:
    font = ImageFont.load_default()

y = 0
for c, label in crops:
    draw.rectangle([0, y, W, y + 70], fill=(220, 235, 255))
    draw.text((pad, y + 12), label, fill=(0, 0, 0), font=font)
    y += 70
    out.paste(c, (pad, y + pad))
    y += c.height + pad * 2
    draw.line([(0, y - pad // 2), (W, y - pad // 2)], fill=(180, 180, 180), width=6)

out.save(f'{D}/s4-crops-composite.png')
print(f'composite: {W}x{Ht} -> {D}/s4-crops-composite.png')
