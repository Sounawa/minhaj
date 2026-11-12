# -*- coding: utf-8 -*-
"""Minhāj — zooms d'adjudication leçon 410 hadith-3es (R688).
Bands recadrées sur la colonne de texte (x 0.04-0.96), échelle composite
effective 0.329 (lisible sans downscale Read). Piles de bandes empilées."""
import fitz
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r688"
doc = fitz.open(PDF)
X0, X1 = 0.04, 0.96


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(
        r.x0 + r.width * X0,
        r.y0 + r.height * y0,
        r.x0 + r.width * X1,
        r.y0 + r.height * y1,
    )
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, bands, width=1500):
    imgs = []
    for p, a, b in bands:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append(im.resize((width, int(im.height * r)), Image.LANCZOS))
    sep = 12
    H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
    sheet = Image.new("RGB", (width, H), (255, 210, 210))
    y = 0
    for im in imgs:
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print(f"OK {path} — {sheet.width}x{sheet.height}")


os.makedirs(OUT, exist_ok=True)

composite("z410-1-p141-textes", [(141, 0.53, 0.78)])
composite("z410-2-p142-textes-notice", [(142, 0.04, 0.37), (142, 0.37, 0.72)])
composite("z410-3-p143-fiqh1", [(143, 0.28, 0.61), (143, 0.60, 0.94)])
composite("z410-4-p144-types", [(144, 0.00, 0.28), (144, 0.24, 0.62)])
composite("z410-5-p144-145-hunt", [(144, 0.58, 0.95), (145, 0.00, 0.30)])
composite("z410-6-p145-tayr", [(145, 0.28, 0.66), (145, 0.65, 0.95)])
composite("z410-7-p146-fin", [(146, 0.00, 0.62)])
