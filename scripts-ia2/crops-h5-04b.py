#!/usr/bin/env python3
# Z2-4 — second composite : zones restantes p33/p35/p36
from PIL import Image, ImageDraw, ImageFont

D = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-04'
ZONES = [
    ('p-033.png', (0.05, 0.00, 0.98, 0.42), 'F p33 haut : التحليل + أولًا الإحسان (المرتبة الثالثة، اتقان)'),
    ('p-033.png', (0.05, 0.42, 0.98, 0.62), 'G p33 milieu : 2 مراتب الإحسان + الأولى المشاهدة'),
    ('p-035.png', (0.05, 0.50, 0.98, 0.72), 'H p35 : وما يستفاد من الحديث (items)'),
    ('p-036.png', (0.05, 0.52, 0.98, 0.80), 'I p36 : الأعداد القبلية (titre + ligne)'),
]
crops = []
for fn, (l, t, r, b), label in ZONES:
    im = Image.open(f'{D}/{fn}')
    W, H = im.size
    c = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
    c = c.resize((int(c.width * 2.8), int(c.height * 2.8)), Image.LANCZOS)
    crops.append((c, label))

pad = 30
W = max(c.width for c, _ in crops) + 2 * pad
Ht = sum(c.height + pad * 2 + 70 for c, _ in crops)
out = Image.new('RGB', (W, Ht), 'white')
draw = ImageDraw.Draw(out)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)
except Exception:
    font = ImageFont.load_default()
y = 0
for c, label in crops:
    draw.rectangle([0, y, W, y + 70], fill=(255, 235, 205))
    draw.text((pad, y + 12), label, fill=(0, 0, 0), font=font)
    y += 70
    out.paste(c, (pad, y + pad))
    y += c.height + pad * 2
    draw.line([(0, y - pad // 2), (W, y - pad // 2)], fill=(150, 150, 150), width=6)
out.save(f'{D}/s4-crops-composite2.png')
print(f'composite2: {W}x{Ht}')
