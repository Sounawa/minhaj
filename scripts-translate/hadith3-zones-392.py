# -*- coding: utf-8 -*-
"""Minhāj — pile 600 dpi des 4 zones ambiguës restantes (R625, leçon 3 hadith-3es).
a) p.26 bas  : gloss « شَرَّة » (الفهم)
b) p.27 bas  : citation de Muslim (طيّبت عند إحرام...)
c) p.28 milieu : récit ʿUmar/Muʿāwiya/أم حبيبة + «ولما رواه مالك أيضًا...»
d) p.29 haut : « رأسه وقَبْلَ/وقيل أن يفيض » (hadith 927)
Sortie : tr-tmp/qa-crops-r625/pile-zones-600.png
"""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r625/pile-zones-600.png"

ZONES = [
    (26, 0.68, 0.84),  # الفهم gloss شَرَّة
    (27, 0.83, 1.00),  # citation Muslim (fin p.27)
    (28, 0.22, 0.58),  # récit 925 + «ولما رواه مالك أيضًا»
    (29, 0.07, 0.24),  # fin hadith 927 (وقَبْلَ/وقيل أن يفيض)
]

doc = fitz.open(PDF)
crops = []
for p, f0, f1 in ZONES:
    page = doc[p - 1]
    pw, ph = page.rect.width, page.rect.height
    pix = page.get_pixmap(dpi=600, clip=fitz.Rect(0, ph * f0, pw, ph * f1))
    f = f"/home/z/my-project/tr-tmp/qa-crops-r625/zone-p{p}-{int(f0*100)}.png"
    pix.save(f)
    crops.append(f)

ims = [Image.open(f) for f in crops]
w = max(im.width for im in ims)
h = sum(im.height for im in ims) + 12 * (len(ims) - 1)
canvas = Image.new("RGB", (w, h), (255, 255, 255))
y = 0
for im in ims:
    canvas.paste(im, (0, y))
    y += im.height + 12
canvas.save(OUT)
print(f"OK {OUT} {canvas.size}")
