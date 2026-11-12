#!/usr/bin/env python3
"""R691 — zooms serres x3 des points d'adjudication residuels (docId 413)."""
from PIL import Image

SRC = '/home/z/my-project/tr-tmp/m413-r691/'
OUT = '/home/z/my-project/tr-tmp/m413-r691/zoom-final-r691.png'

# (fichier, x0, y0, x1, y1 en fraction) — bandes TRES etroites autour des mots cibles
bands = [
    # B: hadith abu burda — phrase "قبل أن يذبح ... ففَضَّ أن"
    ('p160-a.png', 0.05, 0.30, 0.98, 0.55),
    # A1: glossaire, ligne 1 (bas de p160-b)
    ('p160-b.png', 0.02, 0.80, 0.99, 0.99),
    # A2: glossaire, ligne 2 (haut de p160-c)
    ('p160-c.png', 0.02, 0.00, 0.99, 0.20),
    # C: numero aya al-Hujj (p161-c)
    ('p161-c.png', 0.05, 0.55, 0.98, 0.73),
    # D: al-Baqara + ref al-Masalik (p162-a)
    ('p162-a.png', 0.03, 0.42, 0.98, 0.70),
    # E: "ببقر?" (p162-c)
    ('p162-c.png', 0.05, 0.22, 0.98, 0.42),
    # F: debut de l'athar de l'istithmar (p163-b)
    ('p163-b.png', 0.03, 0.22, 0.98, 0.42),
]

Z = 2.6
imgs = []
for fn, x0, y0, x1, y1 in bands:
    im = Image.open(SRC + fn)
    w, h = im.size
    crop = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    crop = crop.resize((int(crop.width * Z), int(crop.height * Z)), Image.LANCZOS)
    imgs.append(crop)

W = max(c.width for c in imgs)
pad = 30
H = sum(c.height for c in imgs) + pad * (len(imgs) + 1)
canvas = Image.new('RGB', (W, H), 'white')
y = pad
for c in imgs:
    canvas.paste(c, (0, y))
    y += c.height + pad
# resize final pour lecture cible ~1900 px de large
scale = 1900 / W
canvas = canvas.resize((1900, int(H * scale)), Image.LANCZOS)
canvas.save(OUT)
print('zoom final:', OUT, canvas.size)
