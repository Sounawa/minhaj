# -*- coding: utf-8 -*-
"""Minhāj — adjudication AD4 leçon 409 (R687) — 4 bandes 900 dpi droite."""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r687"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, x0=0.20, x1=1.0, dpi=900):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0 + r.width * x0, r.y0 + r.height * y0,
                     r.x0 + r.width * x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


bands = [
    (137, 0.835, 0.925),  # bannière استخلاص المضامين
    (138, 0.155, 0.245),  # bannière فقه الحديث + أولا
    (140, 0.487, 0.55),   # 1175 : قال: وأكته …
    (137, 0.79, 0.86),    # glose : ويسمى العطف الثقفي
]

imgs = []
for p, a, b in bands:
    im = zone(p, a, b)
    r = 1400 / im.width
    imgs.append(im.resize((1400, int(im.height * r)), Image.LANCZOS))

sep = 12
H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
sheet = Image.new("RGB", (1400, H), (180, 220, 255))
y = 0
for im in imgs:
    sheet.paste(im, (0, y))
    y += im.height + sep
path = f"{OUT}/ad4-900dpi.png"
sheet.save(path)
print("OK", path, sheet.size)
