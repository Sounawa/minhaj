#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R595 — crops d'adjudication image, leçon 18 ulum-hadith-tanawi-1
(pdf-mut23h2q-129, الحديث الشاذ, p.91-94 de ulum-hadith-1-thanawi.pdf).
Bornes tranchées OCR : p.91 bannière+objectifs+متن ; p.94 الإعداد القبلي → المقلوب ;
p.95 = bannière الدرس 19 (confirmée). Zones calligraphiques/citations dégradées à
l'OCR 300 dpi → composites 600 dpi pour lecture image directe (zéro vision API).
Sortie : tr-tmp/qa-crops-r595/comp-<X>.png
Usage : python3 scripts-translate/crops-uh1-r595.py [comp ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r595"
DPI = 600

# (page, y0, y1, x0, x1) en fractions de page — zones ajustées larges
ZONES = {
    # A — p.91 : bannière الحديث الشاذ + numéro + أهداف الدرس (3 objectifs)
    "A-p91-banniere": [(91, 0.00, 0.38, 0.04, 0.96)],
    # B — p.91 : تمهيد + bandeau المتن + bayt du nāẓim (شاذ/شاد à trancher)
    "B-p91-matn":     [(91, 0.36, 0.80, 0.04, 0.96)],
    # C — p.91 bas + p.92 haut : الشرح (الملا/الشاذ) + استخلاص (2 questions)
    "C-p91sharh-p92istikhlas": [(91, 0.78, 1.00, 0.04, 0.96), (92, 0.00, 0.20, 0.04, 0.96)],
    # D — p.92 : التحليل — définition معتمدة + المحفوظ + مخالفة سند/متن + الحاكم [119]
    "D-p92-tahlil":   [(92, 0.18, 1.00, 0.04, 0.96)],
    # E — p.93 : الخليلي [176/1] + البخاري إنما الأعمال + chaîne عمر + مسلم الزهري
    "E-p93-ta3rifat": [(93, 0.00, 0.60, 0.04, 0.96)],
    # F — p.93 bas + p.94 haut : ثانيا أقسام + exemple أبو داود + البيهقي
    "F-p93aqsam-p94bayhaqi": [(93, 0.58, 1.00, 0.04, 0.96), (94, 0.00, 0.14, 0.04, 0.96)],
    # G — p.94 : التقويم (3 questions) + الاستثمار ابن دقيق العيد [268] + أتأمل + الإعداد القبلي
    "G-p94-taqwim-istimar": [(94, 0.12, 1.00, 0.04, 0.96)],
}


def build(name):
    doc = fitz.open(PDF)
    parts = []
    for (pno, y0, y1, x0, x1) in ZONES[name]:
        page = doc[pno - 1]
        r = page.rect
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        pix = page.get_pixmap(dpi=DPI, clip=clip)
        tmp = f"/tmp/uh1-r595-{name}-{pno}.png"
        pix.save(tmp)
        parts.append(Image.open(tmp))
    doc.close()
    W = max(im.width for im in parts)
    H = sum(im.height for im in parts) + 24 * (len(parts) - 1)
    comp = Image.new("RGB", (W, H), (255, 0, 0))  # séparateur rouge entre pages
    y = 0
    for im in parts:
        comp.paste(im, (0, y))
        y += im.height + 24
    path = f"{OUT}/comp-{name}.png"
    comp.save(path, optimize=True)
    print(f"{path}  {comp.width}x{comp.height}")
    for im in parts:
        im.close()


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    names = sys.argv[1:] or list(ZONES)
    for n in names:
        build(n)
