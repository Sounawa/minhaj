#!/usr/bin/env python3
# Z2-5 — micro-crops ×300% des 11 zones litigieuses de la leçon 5 → composite unique
from PIL import Image, ImageDraw, ImageFont

D = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-05'
ZONES = [
    ('p-037.png', (0.10, 0.74, 0.95, 0.90), 'A p37 : fin cadre hadith + ref (متفق عليه ?)'),
    ('p-038.png', (0.10, 0.56, 0.95, 0.68), 'B p38 : الشرح مفردات الحديث و…'),
    ('p-039.png', (0.05, 0.00, 0.98, 0.10), 'C p39 : وأنّما بعدهما من بقية الأركان'),
    ('p-039.png', (0.05, 0.11, 0.98, 0.24), 'D p39 : والمعانيّة كالإخلاص…'),
    ('p-039.png', (0.05, 0.30, 0.98, 0.42), 'E p39 : في أموره ونهواهه + [سنن الترمذي]'),
    ('p-039.png', (0.05, 0.52, 0.98, 0.66), 'F p39 : fin إيتاء الزكاة (والسخاء ?)'),
    ('p-040.png', (0.05, 0.08, 0.98, 0.32), 'G p40 : صوم رمضان + بنية + verset [البقرة: 183]'),
    ('p-040.png', (0.05, 0.33, 0.98, 0.44), 'H p40 : ومن أهمية الصوم (اكتساب ?)'),
    ('p-040.png', (0.05, 0.58, 0.98, 0.84), 'I p40 : أهمية الحج (بداء? مهط الوحي? الجمعة العظيم?)'),
    ('p-041.png', (0.10, 0.26, 0.95, 0.44), 'J p41 : lettre Umar b. Abd al-Aziz (فسألتها ?)'),
    ('p-041.png', (0.10, 0.44, 0.95, 0.54), 'K p41 : أستنتج مكوّناتي/…'),
]
crops = []
for fn, (l, t, r, b), label in ZONES:
    im = Image.open(f'{D}/{fn}')
    W, H = im.size
    c = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
    c = c.resize((int(c.width * 3.0), int(c.height * 3.0)), Image.LANCZOS)
    crops.append((c, label))
pad = 26
W = max(c.width for c, _ in crops) + 2 * pad
Ht = sum(c.height + pad * 2 + 62 for c, _ in crops)
out = Image.new('RGB', (W, Ht), 'white')
draw = ImageDraw.Draw(out)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)
except Exception:
    font = ImageFont.load_default()
y = 0
for c, label in crops:
    draw.rectangle([0, y, W, y + 62], fill=(235, 245, 255))
    draw.text((pad, y + 8), label, fill=(0, 0, 0), font=font)
    y += 62
    out.paste(c, (pad, y + pad))
    y += c.height + pad * 2
    draw.line([(0, y - pad // 2), (W, y - pad // 2)], fill=(150, 150, 150), width=5)
out.save(f'{D}/s5-crops-composite.png')
print(f'composite: {W}x{Ht}')
