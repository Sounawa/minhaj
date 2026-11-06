#!/usr/bin/env python3
"""R635 — recadrages d'adjudication leçon 13 : boutons, liste des aṣṭilāḥāt, note الطالب, iʿdād qablī."""
import fitz
PDF = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r635"
doc = fitz.open(PDF)

def zone(p, y0, y1, dpi=1500, tag="", x0=0.0, x1=1.0):
    pg = doc[p - 1]
    W, H = pg.rect.width, pg.rect.height
    clip = fitz.Rect(W * x0, H * y0, W * x1, H * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    f = f"{OUT}/p{p:03d}-adj-{tag}-{dpi}.png"
    pm.save(f)
    return f

jobs = [
    # p.72 : la note espacée « الطالب… » + bouton أنشطة الإنجاز (y ~0.50-0.68)
    ("p072-note-enjaz",   lambda: zone(72, 0.50, 0.70, 1500, "note-enjaz")),
    # p.72 : la parenthèse des aṣṭilāḥāt (y ~0.62-0.78)
    ("p072-astilahat",    lambda: zone(72, 0.60, 0.80, 1500, "astilahat")),
    # p.72 : bas de page — item إجراء بحث + numéro
    ("p072-bas",          lambda: zone(72, 0.72, 1.00, 1200, "bas")),
    # p.73 : الإعداد القبلي titre + ligne citée (y ~0.55-1.00)
    ("p073-i3dad-qibli",  lambda: zone(73, 0.55, 1.00, 1500, "i3dad-qibli")),
    # p.73 : أنشطة العرض bouton + 2 items (y ~0.05-0.55) pour contrôle
    ("p073-ard",          lambda: zone(73, 0.02, 0.55, 1200, "ard")),
]
for name, fn in jobs:
    print(fn())
