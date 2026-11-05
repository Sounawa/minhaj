#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R596 — crops d'adjudication image, leçon 19 ulum-hadith-tanawi-1
(pdf-mut23h2q-130, الحديث المقلوب, p.95-98 de ulum-hadith-1-thanawi.pdf).
Bornes tranchées OCR : p.95 bannière الدرس 19 + المتن ; p.98 الإعداد القبلي → المعلل ;
p.99 = bannière الدرس 20 الحديث الفرد والحديث المعلل (confirmée OCR R596).
Zones calligraphiques/citations dégradées à l'OCR 300 dpi → composites 600 dpi
pour lecture image directe (zéro vision API).
Sortie : tr-tmp/qa-crops-r596/comp-<X>.png
Usage : python3 scripts-translate/crops-uh1-r596.py [comp ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r596"
DPI = 600

# (page, y0, y1, x0, x1) en fractions de page — zones ajustées larges
ZONES = {
    # A — p.95 : bannière الحديث المقلوب + numéro 19 + أهداف الدرس (3 objectifs)
    "A-p95-banniere": [(95, 0.00, 0.42, 0.04, 0.96)],
    # B — p.95 : تمهيد + bandeau المتن + bayt du nāẓim (hémistiche en points ?)
    "B-p95-matn":     [(95, 0.40, 0.86, 0.04, 0.96)],
    # C — p.96 : الشرح (المقلوب مأخوذ من القلب) + استخلاص (2 questions) + bayt répété
    "C-p96-sharh-bayt": [(96, 0.00, 0.45, 0.04, 0.96)],
    # D — p.96 bas + p.97 haut : définition + القسم الأول مقلوب السند + صور + البخاري بغداد
    "D-p96def-p97pics": [(96, 0.42, 1.00, 0.04, 0.96), (97, 0.00, 0.28, 0.04, 0.96)],
    # E — p.97 : القسم الثاني مقلوب المتن + حديث السبعة + صوابه [صحيح مسلم]
    "E-p97-matnan":   [(97, 0.26, 0.64, 0.04, 0.96)],
    # F — p.97 bas : ثانيا أسباب القلب + العراقي + حرمي/شعبة + مثال السهو + قصة حجاج
    "F-p97-asbab":    [(97, 0.62, 1.00, 0.04, 0.96)],
    # H1 — p.98 haut : التقويم (3 questions) + الاستثمار ابن حجر [نزهة النظر 118]
    "H1-p98-taqwim-istimar": [(98, 0.00, 0.52, 0.04, 0.96)],
    # H2 — p.98 bas : أتأمل (2 questions) + الإعداد القبلي → المعلل
    "H2-p98-atamul-i3dadi": [(98, 0.48, 1.00, 0.04, 0.96)],
    # I — p.99 : bannière الدرس 20 (preuve borne supérieure, contrôle inversion)
    "I-p99-banniere": [(99, 0.00, 0.38, 0.04, 0.96)],
}


def build(name):
    doc = fitz.open(PDF)
    parts = []
    for (pno, y0, y1, x0, x1) in ZONES[name]:
        page = doc[pno - 1]
        r = page.rect
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        pix = page.get_pixmap(dpi=DPI, clip=clip)
        tmp = f"/tmp/uh1-r596-{name}-{pno}.png"
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
