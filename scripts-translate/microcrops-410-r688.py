# -*- coding: utf-8 -*-
"""Minhāj — micro-crops ajustés leçon 410 hadith-3es (R688, canal principal).
Bandes cadrées sur les calibrations 300 dpi lues au tour."""
import fitz
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r688"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0, r.x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, bands, width=1500):
    imgs = []
    for p, a, b in bands:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append(im.resize((width, int(im.height * r)), Image.LANCZOS))
    sep = 14
    H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
    sheet = Image.new("RGB", (width, H), (255, 215, 215))
    y = 0
    for im in imgs:
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print(f"OK {path} — {sheet.width}x{sheet.height}")


os.makedirs(OUT, exist_ok=True)

composite("m410-A-p141-haut", [(141, 0.00, 0.45)])
composite("m410-B-p141-cadre", [(141, 0.40, 0.85)])
composite("m410-C-p142-cadre", [(142, 0.00, 0.50)])
composite("m410-D-p142-notice-gloses", [(142, 0.45, 1.00)])
composite("m410-E-p143-fiqh1", [(143, 0.00, 0.55)])
composite("m410-F-p143-fiqh2", [(143, 0.50, 1.00)])
composite("m410-G-p144-fiqh", [(144, 0.00, 0.60)])
composite("m410-H-p144-145", [(144, 0.55, 1.00), (145, 0.00, 0.45)])
composite("m410-I-p145-146", [(145, 0.40, 1.00), (146, 0.00, 0.90)])
