#!/usr/bin/env python3
"""R632 — crops uh2 leçon 12 : pleines pages 900 dpi + zones ciblées 1500 dpi."""
import fitz

PDF = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "tr-tmp/r632"
doc = fitz.open(PDF)

def full(p, dpi=900):
    pg = doc[p - 1]
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
    f = f"{OUT}/p{p:03d}-full{dpi}.png"
    pm.save(f)
    return f

def zone(p, y0, y1, dpi=1500, tag=""):
    pg = doc[p - 1]
    W, H = pg.rect.width, pg.rect.height
    clip = fitz.Rect(0, H * y0, W, H * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    f = f"{OUT}/p{p:03d}-{tag}-{dpi}.png"
    pm.save(f)
    return f

jobs = [
    ("p068-banner-1500", lambda: zone(68, 0.00, 0.22, 1500, "banner")),
    ("p068-matn-1500",   lambda: zone(68, 0.25, 0.58, 1500, "matn")),
    ("p068-bas-900",     lambda: zone(68, 0.55, 1.00, 900, "bas")),
    ("p069-ref1-1500",   lambda: zone(69, 0.10, 0.22, 1500, "ref1")),
    ("p069-ref2-1500",   lambda: zone(69, 0.36, 0.54, 1500, "ref2")),
    ("p069-ref3-1200",   lambda: zone(69, 0.54, 0.88, 1200, "ref3")),
    ("p070-top-1500",    lambda: zone(70, 0.00, 0.14, 1500, "top")),
    ("p070-para-1200",   lambda: zone(70, 0.18, 0.45, 1200, "para")),
    ("p070-diag-1500",   lambda: zone(70, 0.70, 1.00, 1500, "diag")),
    ("p071-ref-1500",    lambda: zone(71, 0.48, 0.70, 1500, "ref")),
]
for name, fn in jobs:
    print(fn())
for p in (68, 69, 70, 71):
    print(full(p))
