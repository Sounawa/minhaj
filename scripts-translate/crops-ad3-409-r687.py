# -*- coding: utf-8 -*-
"""Minhāj — adjudication AD3 leçon 409 (R687) — bandes larges 600 dpi."""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r687"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0, r.x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


bands = [
    (136, 0.025, 0.15),   # médaillon 20 + titre
    (137, 0.095, 0.205),  # 1178 : يحلّ … يوم النحر + āya
    (137, 0.755, 0.84),   # bannière استخلاص …
    (137, 0.925, 1.00),   # glose : ويسمى العطف …
    (138, 0.145, 0.245),  # bannière فقه … + أولا
    (140, 0.125, 0.21),   # 1180 : لطولهما … من أول شوال
    (140, 0.485, 0.645),  # 1175 : وأكته … + عن السعي
    (139, 0.83, 0.975),   # وفعله هذا … وكأن سالمًا …
]

imgs = []
for p, a, b in bands:
    im = zone(p, a, b)
    r = 1500 / im.width
    imgs.append(im.resize((1500, int(im.height * r)), Image.LANCZOS))

sep = 12
H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
sheet = Image.new("RGB", (1500, H), (255, 230, 170))
y = 0
for im in imgs:
    sheet.paste(im, (0, y))
    y += im.height + sep
path = f"{OUT}/ad3-adjudications.png"
sheet.save(path)
print("OK", path, sheet.size)
