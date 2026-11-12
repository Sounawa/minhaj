#!/usr/bin/env python3
# Z2-3 — planches d'adjudication : bandes contestées empilées par page (×2 LANCZOS)
from PIL import Image
import os
SRC = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01'

PLATES = [
    ('023', [('T-tamhid', 810, 1140)]),
    ('024', [('B-falith', 610, 815), ('C-gloses', 940, 1410)]),
    ('025', [('D-tahlil', 480, 955), ('E-awla', 955, 1360)]),
    ('026', [('G-iman-billah', 550, 955), ('H-versets', 955, 1230)]),
    ('027', [('I-hafaza', 130, 360), ('J-kutub', 360, 745), ('K-tafarruq', 960, 1360)]),
    ('028', [('L-akhir', 220, 510), ('M-hadid', 900, 1090)]),
    ('029', [('P-sul', 660, 990)]),
    ('030', [('Q-badaa', 310, 510)]),
]

for pg, bands in PLATES:
    im = Image.open(f'{SRC}/p-{pg}.png')
    parts = [im.crop((0, y0, im.width, y1)) for _, y0, y1 in bands]
    h = sum(p.height for p in parts) + 8 * (len(parts) - 1)
    plate = Image.new('RGB', (im.width, h), (200, 200, 200))
    y = 0
    for p in parts:
        plate.paste(p, (0, y))
        y += p.height + 8
    up = plate.resize((plate.width * 2, plate.height * 2), Image.LANCZOS)
    out = f'{SRC}/s3-{pg}.png'
    up.save(out)
    print(f's3-{pg}.png', bands, up.size, os.path.getsize(out))
