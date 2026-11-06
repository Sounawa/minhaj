#!/usr/bin/env python3
"""R635 — crops uh2 leçon 13 : pleines pages 900 dpi + zones ciblées 1200-1500 dpi."""
import fitz

PDF = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r635"
doc = fitz.open(PDF)

def full(p, dpi=900):
    pg = doc[p - 1]
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
    f = f"{OUT}/p{p:03d}-full{dpi}.png"
    pm.save(f)
    return f

def zone(p, y0, y1, dpi=1500, tag="", x0=0.0, x1=1.0):
    pg = doc[p - 1]
    W, H = pg.rect.width, pg.rect.height
    clip = fitz.Rect(W * x0, H * y0, W * x1, H * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    f = f"{OUT}/p{p:03d}-{tag}-{dpi}.png"
    pm.save(f)
    return f

jobs = [
    # p.71 : bas = i3dad (fin leçon 12) — contrôle
    ("p071-bas-900",    lambda: zone(71, 0.55, 1.00, 900, "bas")),
    # p.72 : bannière leçon 13 + objectifs + tableau
    ("p072-top-1500",   lambda: zone(72, 0.00, 0.20, 1500, "top")),
    ("p072-banniere-900", lambda: zone(72, 0.00, 0.14, 900, "banniere")),
    ("p072-tableau-1200", lambda: zone(72, 0.30, 0.75, 1200, "tableau")),
    ("p072-bas-900",    lambda: zone(72, 0.75, 1.00, 900, "bas")),
    # p.73 : ancha al-ard + istidadat qibliya
    ("p073-top-1500",   lambda: zone(73, 0.00, 0.45, 1500, "top")),
    ("p073-bas-1500",   lambda: zone(73, 0.45, 1.00, 1500, "bas")),
    ("p073-full900",    lambda: full(73)),
    # p.74 : bannière leçon 14 ?
    ("p074-top-1500",   lambda: zone(74, 0.00, 0.22, 1500, "top")),
    ("p074-full900",    lambda: full(74)),
    # p.75-78 : sondage hauts de page (bannières éventuelles)
    ("p075-top-900",    lambda: zone(75, 0.00, 0.20, 900, "top")),
    ("p076-top-900",    lambda: zone(76, 0.00, 0.20, 900, "top")),
    ("p077-top-900",    lambda: zone(77, 0.00, 0.20, 900, "top")),
    ("p078-top-900",    lambda: zone(78, 0.00, 0.20, 900, "top")),
    ("p079-top-900",    lambda: zone(79, 0.00, 0.20, 900, "top")),
]
for name, fn in jobs:
    print(fn())
for p in (72, 74):
    print(full(p))
