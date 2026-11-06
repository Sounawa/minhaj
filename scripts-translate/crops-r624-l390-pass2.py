#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R624 — pass 2 : crops serrés des crochets [الموطأ رقم : N] (chiffres OCR
inversés par paires — tranchage par lecture image 900 dpi) + blocs restants
brouillés (p12 شرح, p12 آية, p14 fin, p15 عائشة/خلاصة, p16 نص)."""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r624"

doc = fitz.open(PDF)

# (page, clé, y0, y1 en fractions) — crochets localisés par search_for
def bracket_crops(p):
    pg = doc[p - 1]
    hits = pg.search_for("الموطأ")
    out = []
    for i, r in enumerate(hits, 1):
        pad = 6
        clip = fitz.Rect(max(r.x0 - pad, 0), max(r.y0 - pad, 0),
                         min(r.x1 + pad, pg.rect.width), min(r.y1 + pad, pg.rect.height))
        zoom = 900 / 72
        pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
        name = f"p{p}-br{i}"
        pix.save(f"{OUT}/{name}.png")
        out.append((name, round(r.y0 / pg.rect.height, 3)))
    return out


for p in (10, 11, 13, 14, 16):
    res = bracket_crops(p)
    print(f"p.{p}: {res}")


def zone(p, name, x0, x1, y0, y1, zoom=500 / 72):
    pg = doc[p - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


zone(12, "p12-sharh-ref", 0.05, 0.98, 0.28, 0.52)   # ابن عرفة + [شرح ... ص:N] + الحج عرفة
zone(12, "p12-aya", 0.05, 0.98, 0.62, 0.90)          # ﴿ولله على الناس حج البيت﴾ + ref
zone(14, "p14-tail", 0.05, 0.98, 0.52, 1.00)         # fin hadith أيوب + قوله هكذا رأيت
zone(15, "p15-aisha", 0.05, 0.98, 0.10, 0.32)        # citation عائشة + [صحيح البخاري]
zone(15, "p15-khulasa", 0.05, 0.98, 0.30, 0.52)      # يستفاد من الدرس...
doc.close()
print("OK pass2")
