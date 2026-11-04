# -*- coding: utf-8 -*-
"""R573 — composite F : 13 micro-crops 1200 dpi, adjudication finale des mots."""
import os

import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r573-crops"
doc = fitz.open(PDF)
WIDTH = 1400

BANDS = [
    (193, 0.30, 0.175, 0.78, 0.228),  # 1 «يدأ/يدع شهوته»
    (193, 0.28, 0.498, 0.65, 0.558),  # 2 «يبغي/ينهى عن صيام»
    (193, 0.25, 0.838, 0.68, 0.898),  # 3 «قَسَمْ بالله»
    (193, 0.03, 0.888, 0.70, 0.948),  # 4 «الخلاف: تغير راحة... لخلاء المعدة»
    (195, 0.25, 0.112, 0.68, 0.165),  # 5 «كتخمّ»
    (195, 0.08, 0.158, 0.52, 0.210),  # 6 «التشريف والتعتيم/التعميم»
    (195, 0.22, 0.272, 0.62, 0.328),  # 7 «بعشرة/بعشر أمثالها»
    (195, 0.25, 0.748, 0.65, 0.808),  # 8 «فإن أمرّ قاتله أو شاهده»
    (196, 0.28, 0.290, 0.85, 0.348),  # 9 «ولم رأيته يفطر يوم الجمعة»
    (196, 0.70, 0.358, 0.99, 0.410),  # 10 «[السنن الكبرى للنسائي]»
    (196, 0.28, 0.668, 0.92, 0.728),  # 11 «بينهما وبينه فرائض/فراضا»
    (197, 0.28, 0.182, 0.62, 0.248),  # 12 «أبين/أين المراد»
    (197, 0.10, 0.465, 0.62, 0.518),  # 13 «خير حصال الصائم السواك»
]

pieces = []
for i, (pno, x0, y0, x1, y1) in enumerate(BANDS, 1):
    page = doc[pno - 1]
    r = page.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = page.get_pixmap(dpi=1200, clip=clip)
    tmp = f"/tmp/micro_{i}.png"
    pix.save(tmp)
    im = Image.open(tmp)
    if im.width > WIDTH:
        h = int(im.height * WIDTH / im.width)
        im = im.resize((WIDTH, h), Image.LANCZOS)
    lab = Image.new("RGB", (WIDTH, 30), (230, 230, 230))
    d = ImageDraw.Draw(lab)
    d.text((6, 6), f"p.{pno} - micro {i}  ({x0:.2f}-{x1:.2f} x {y0:.2f}-{y1:.2f}) 1200dpi", fill=(0, 0, 0))
    pieces.append(lab)
    pieces.append(im)

total_h = sum(p.height for p in pieces) + 4 * len(pieces)
comp = Image.new("RGB", (WIDTH, total_h), (255, 255, 255))
y = 0
for p in pieces:
    comp.paste(p, (0, y))
    y += p.height + 4
path = f"{OUT}/F-micro-crops.png"
comp.save(path)
print(path, comp.size)
