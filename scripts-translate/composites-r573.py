# -*- coding: utf-8 -*-
"""R573 — composites d'adjudication : bandes 900 dpi empilées.
Méthode R572 « lectures groupées » : un composite = plusieurs bandes étiquetées."""
import os

import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/r573-crops"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

WIDTH = 1400

BANDS = {
    "A-p193-critique": [
        (193, 0.05, 0.165, 0.95, 0.215),   # 1 «إنما يدع شهوته وطعامه وشرابه»
        (193, 0.05, 0.235, 0.95, 0.290),   # 2 «كل حسنة...» + [864]
        (193, 0.05, 0.420, 0.95, 0.485),   # 3 «الجفاء، لو رأوا/زاووا...» + [887]
        (193, 0.05, 0.475, 0.95, 0.585),   # 4 «وقال يحيى وسمعت...ينهى/يبغي» + [887]
        (193, 0.03, 0.615, 0.97, 0.930),   # 5 ترجمة الراوي + الشرح قَسَم + الخلاف
    ],
    "B-p195-critique": [
        (195, 0.05, 0.110, 0.95, 0.205),   # 6 الزين بن المنير «التشريف والتعتيم/التعميم»
        (195, 0.05, 0.275, 0.95, 0.375),   # 7 «كل حسنة بعشر/بعشرة أمثالها»
        (195, 0.05, 0.735, 0.95, 0.875),   # 8 «فإن أمر قاتله...إني صائم» + [863]
    ],
    "C-p196-critique": [
        (196, 0.05, 0.360, 0.95, 0.485),   # 9 حديث ابن مسعود + [السنن الكبرى للنسائي]
        (196, 0.05, 0.465, 0.95, 0.560),   # 10 «لرواية ابن القاسم كراهة صوم يوم مؤقت»
        (196, 0.05, 0.640, 0.95, 0.735),   # 11 «بينهما وبينه فيعتقدوها فرائض»
    ],
    "D-p197-critique": [
        (197, 0.05, 0.175, 0.95, 0.255),   # 12 «أبين/أين المراد بقول النبي»
        (197, 0.05, 0.315, 0.95, 0.535),   # 13 الاستثمار مالك + [866] + الزرقاني + sources
    ],
}

for name, bands in BANDS.items():
    pieces = []
    for i, (pno, x0, y0, x1, y1) in enumerate(bands, 1):
        page = doc[pno - 1]
        r = page.rect
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        pix = page.get_pixmap(dpi=900, clip=clip)
        tmp = f"/tmp/band_{pno}_{i}.png"
        pix.save(tmp)
        im = Image.open(tmp)
        if im.width > WIDTH:
            h = int(im.height * WIDTH / im.width)
            im = im.resize((WIDTH, h), Image.LANCZOS)
        # étiquette
        lab = Image.new("RGB", (WIDTH, 34), (230, 230, 230))
        d = ImageDraw.Draw(lab)
        d.text((6, 8), f"p.{pno} - bande {i}  ({x0:.2f}-{x1:.2f} x {y0:.2f}-{y1:.2f})", fill=(0, 0, 0))
        pieces.append(lab)
        pieces.append(im)
    total_h = sum(p.height for p in pieces) + 4 * len(pieces)
    comp = Image.new("RGB", (WIDTH, total_h), (255, 255, 255))
    y = 0
    for p in pieces:
        comp.paste(p, (0, y))
        y += p.height + 4
    path = f"{OUT}/{name}.png"
    comp.save(path)
    print(path, comp.size)

# p.198 complet à 600 dpi (contenu inconnu, couche texte vide)
page = doc[197]
pix = page.get_pixmap(dpi=600)
pix.save("/tmp/p198.png")
im = Image.open("/tmp/p198.png")
if im.width > WIDTH:
    h = int(im.height * WIDTH / im.width)
    im = im.resize((WIDTH, h), Image.LANCZOS)
lab = Image.new("RGB", (WIDTH, 34), (230, 230, 230))
d = ImageDraw.Draw(lab)
d.text((6, 8), "p.198 - page entiere 600 dpi", fill=(0, 0, 0))
comp = Image.new("RGB", (WIDTH, im.height + 38), (255, 255, 255))
comp.paste(lab, (0, 0))
comp.paste(im, (0, 38))
path = f"{OUT}/E-p198-check.png"
comp.save(path)
print(path, comp.size)
