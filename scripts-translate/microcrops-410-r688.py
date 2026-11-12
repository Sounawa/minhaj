# -*- coding: utf-8 -*-
"""Minhāj — micro-crops leçon 410 hadith-3es (R688, canal principal).
Recette R685/R687 : calibrations pleine page 300 dpi PUIS micro-crops 600 dpi.
Plan validé sur les calibrations lues au tour : une bande pleine page
600 dpi par page (p.141-146) — lisible à l'échelle composite 0.30 ;
re-cadrages zoomés possibles en passe seconde sur les zones litigieuses."""
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

# Bandes pleines pages (fenêtre p.141-146 de la leçon 21)
composite("m410-p141", [(141, 0.00, 1.00)])
composite("m410-p142", [(142, 0.00, 1.00)])
composite("m410-p143", [(143, 0.00, 1.00)])
composite("m410-p144", [(144, 0.00, 1.00)])
composite("m410-p145", [(145, 0.00, 1.00)])
composite("m410-p146", [(146, 0.00, 1.00)])
