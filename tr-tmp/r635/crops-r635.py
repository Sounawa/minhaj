#!/usr/bin/env python3
"""R635 — crops uh2 leçon 13 : sondage bornes 150 dpi + zones ciblées 1500 dpi."""
import fitz

PDF = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r635"
doc = fitz.open(PDF)

def full(p, dpi=150, tag=""):
    pg = doc[p - 1]
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
    f = f"{OUT}/p{p:03d}-survey{tag}-{dpi}.png"
    pm.save(f)
    return f

def zone(p, x0, y0, x1, y1, dpi=1500, tag=""):
    pg = doc[p - 1]
    W, H = pg.rect.width, pg.rect.height
    clip = fitz.Rect(W * x0, H * y0, W * x1, H * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    f = f"{OUT}/p{p:03d}-{tag}-{dpi}.png"
    pm.save(f)
    return f

jobs = [
    # sondage bornes (150 dpi, léger)
    ("survey-p72", lambda: full(72)),
    ("survey-p73", lambda: full(73)),
    ("survey-p74", lambda: full(74)),
    # p.72 : bande verte verticale « تطبيقات في ... » (bord droit, zone مجال الأنشطة)
    ("p72-band",   lambda: zone(72, 0.55, 0.10, 1.00, 0.42, 1500, "band")),
    # p.72 : objectifs (haut de page)
    ("p72-objectifs", lambda: zone(72, 0.0, 0.02, 1.0, 0.16, 1500, "obj")),
    # p.72 : أنشطة الإعداد (4 puces, zones corrompues)
    ("p72-i3dad",  lambda: zone(72, 0.0, 0.42, 1.0, 0.72, 1500, "i3dad")),
    # p.72 : أنشطة الإنجاز (2 puces, liste des termes + bas de page)
    ("p72-injaz",  lambda: zone(72, 0.0, 0.72, 1.0, 1.00, 1500, "injaz")),
    # p.73 : أنشطة العرض + bande rotée
    ("p73-3ard",   lambda: zone(73, 0.0, 0.02, 1.0, 0.50, 1500, "3ard")),
    # p.73 : الإعداد القبلي (ligne corrompue)
    ("p73-i3dad-q", lambda: zone(73, 0.0, 0.50, 1.0, 0.95, 1500, "i3dqd")),
    # p.74 : bannière leçon 14 (borne sup)
    ("p74-banner", lambda: zone(74, 0.0, 0.0, 1.0, 0.35, 1200, "banner")),
]
for name, fn in jobs:
    print(fn())
