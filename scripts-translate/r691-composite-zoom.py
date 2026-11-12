#!/usr/bin/env python3
"""R691 — zoom composite des points à adjudiquer (leçon 24 hadith-3es, docId 413)."""
from PIL import Image

SRC = '/home/z/my-project/tr-tmp/m413-r691/'
OUT = '/home/z/my-project/tr-tmp/m413-r691/composite-zoom-r691.png'

# (fichier, (x0%,y0%,x1%,y1%), zoom) — bandes cibles
strips = [
    ('p160-b.png', (0.00, 0.72, 1.00, 1.00), 1.5),   # A1 glossaire : Sharih + ligne 1
    ('p160-c.png', (0.00, 0.00, 1.00, 0.22), 1.5),   # A2 glossaire : ligne 2
    ('p160-a.png', (0.00, 0.28, 1.00, 0.62), 1.6),   # B hadith abu burda (ffadda ?)
    ('p161-c.png', (0.00, 0.50, 1.00, 0.72), 1.8),   # C numero de la aya al-Hujj
    ('p162-a.png', (0.00, 0.38, 1.00, 0.72), 1.6),   # D al-Baqara 201/203 + ref al-Masalik
    ('p162-c.png', (0.00, 0.18, 1.00, 0.42), 1.7),   # E bibaqarin akhara ?
    ('p163-b.png', (0.00, 0.22, 1.00, 0.44), 1.6),   # F debut de l'athar istithmar
]

imgs = []
for fn, (x0, y0, x1, y1), z in strips:
    im = Image.open(SRC + fn)
    w, h = im.size
    box = (int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))
    crop = im.crop(box)
    crop = crop.resize((int(crop.width * z), int(crop.height * z)), Image.LANCZOS)
    imgs.append((fn, crop))

# disposition 2 colonnes x 4 lignes
colw = max(c.width for _, c in imgs)
pad = 24
left = [imgs[0], imgs[2], imgs[4], imgs[6]]
right = [imgs[1], imgs[3], imgs[5]]
lh = sum(c.height for _, c in left) + pad * (len(left) + 1)
rh = sum(c.height for _, c in right) + pad * (len(right) + 1)
H = max(lh, rh)
W = colw * 2 + pad * 3
canvas = Image.new('RGB', (W, H), 'white')
x1c = pad
y = pad
for fn, c in left:
    canvas.paste(c, (x1c, y))
    y += c.height + pad
x2c = pad + colw + pad
y = pad
for fn, c in right:
    canvas.paste(c, (x2c, y))
    y += c.height + pad
canvas.save(OUT)
print('composite:', OUT, canvas.size)
