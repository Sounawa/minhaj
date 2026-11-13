#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-16 — planche d'adjudication leçon 14 (600 dpi ×2.2)
from PIL import Image, ImageDraw
import subprocess, os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-14'
Z = f'{BASE}/zooms'
os.makedirs(Z, exist_ok=True)
SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'

for p in [80, 81, 82]:
    subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(p), '-l', str(p), SRC, f'{Z}/big-{p}'], check=True)

def zone(pg, y0, y1, x0, x1, label, scale=2.2):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1780:
        tw = 1780
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

CROPS = [
    zone(80, 0.135, 0.205, 0.03, 0.99, 'Z1. p80 obj.3 (an a-stathmira? uawaffifa muktasabati fi wad-iyyatin jadida)'),
    zone(80, 0.255, 0.565, 0.03, 0.99, 'Z2. p80 NASS l.1-7 (khalaqahu min turab... ayat ar-Rum ? ... sana l-taklifi... al-inaya bi-qalbihi)'),
    zone(80, 0.535, 0.765, 0.03, 0.99, 'Z3. p80 NASS l.7-10 (ayat ash-Shuara 88-89... harrama r-riba... raggbahu fi l-wara... an-nasiha... at-tarahum... hadith aliyyakum bi-sunnati)'),
    zone(80, 0.720, 0.90, 0.03, 0.99, 'Z4. p80 NASS fin (jaala mutaqqalabahu bi-yadihi + ayat [?: 20?] + hadith law + sahih muslim)'),
    zone(81, 0.395, 0.60, 0.03, 0.99, 'Z5. p81 tahlil item 4 sous-items (khilafa? bi-yadi llah / ahimmiyatu l-qalbi / TROISIEME sous-item exact)'),
    zone(82, 0.055, 0.22, 0.03, 0.99, 'Z6. p82 tatbiq item 2 (uqaddimu nasa-iha li-akhin li?...)'),
    zone(82, 0.28, 0.52, 0.03, 0.99, 'Z7. p82 i-dad qabli (ahfazu... 1. abhathu an ahammiyati d-duai fi l-islami WA ? / 2. ? al-alaqata...)'),
]

imgs = CROPS
total_h = sum(c.height + 50 for _, c in imgs)
comp = Image.new('RGB', (1800, total_h), 'white')
d = ImageDraw.Draw(comp)
y = 0
for label, c in imgs:
    d.rectangle([0, y, 1799, y+44], fill=(225, 235, 225))
    d.text((14, y+12), label, fill=(20, 20, 20))
    y += 48
    comp.paste(c, ((1800-c.width)//2, y))
    y += c.height + 4

comp.save(f'{Z}/comp-Z14.png')
print('OK', f'{Z}/comp-Z14.png', comp.size, os.path.getsize(f'{Z}/comp-Z14.png')//1024, 'Ko')
