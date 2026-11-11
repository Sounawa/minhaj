# -*- coding: utf-8 -*-
"""Minhāj — adjudications 900 dpi leçon 409 (R687) — mots litigieux, bandes droites."""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r687"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, x0=0.22, x1=1.0, dpi=900):
    """Bande droite (arabe commence à droite) en 900 dpi."""
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0 + r.width * x0, r.y0 + r.height * y0,
                     r.x0 + r.width * x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, bands, width=1400):
    imgs = []
    for p, a, b, x0, x1 in bands:
        im = zone(p, a, b, x0, x1)
        r = width / im.width
        imgs.append(im.resize((width, int(im.height * r)), Image.LANCZOS))
    sep = 14
    H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
    sheet = Image.new("RGB", (width, H), (250, 220, 180))
    y = 0
    for im in imgs:
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print("OK", path, sheet.size)


composite("ad1-p136-137", [
    (136, 0.005, 0.115, 0.15, 1.0),   # médaillon 20 + titre
    (137, 0.085, 0.150, 0.22, 1.0),   # 1178 : حتى يحلّ … يوم النحر
    (137, 0.705, 0.775, 0.30, 1.0),   # bannière استخلاص …
    (137, 0.875, 0.975, 0.22, 1.0),   # glose : ويسمى العطف الـ…
])

composite("ad2-p138-139", [
    (138, 0.095, 0.170, 0.35, 1.0),   # bannière فقه/فتحه الحديث + أولا
    (138, 0.495, 0.665, 0.22, 1.0),   # ومَحَلُّ … / مكان الحلاق بمنى
    (139, 0.540, 0.640, 0.22, 1.0),   # روى عن نافع / أنّ عمر …
    (139, 0.790, 0.975, 0.22, 1.0),   # وفعله هذا … وكأن سالمًا …
    (139, 0.080, 0.155, 0.35, 1.0),   # خذوا عني مناسككم [سنن النسائي الصغرى]
])
