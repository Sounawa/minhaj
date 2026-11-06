#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R617 — recadrages d'arbitrage leçon 5 ulum-hadith-tanawi-2 (p.30-34).
Chaque zone ambiguë est rendue en PNG 600-900 dpi pour lecture image
(précepte R613-R616 : tout nombre/nom équivoque tranché par image, jamais deviné).
Couches : pdftotext = miroir des nombres ; PyMuPDF = logique fidèle (R615).
Usage : python3 scripts-translate/r617-crops.py"""
import os
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r617"

# (nom, page, ancre de recherche (None = bandes), étendue y relative)
CROPS = [
    ("r01-p30-banniere-haut", 30, None, (0.0, 0.30)),      # bannière leçon 5 + objectifs
    ("r02-p30-matn-ibnhagar", 30, "والرابع", (None, None)),
    ("r03-p31-maqayis", 31, "مقاييس", (None, None)),       # nombre Ibn Fāris
    ("r04-p31-hakim", 31, "الجهالة", (None, None)),        # citation al-Ḥākim
    ("r05-p31-ibnarabi", 31, "المنبر", (None, None)),      # réponse Ibn al-ʿArabī
    ("r06-p32-lisan", 32, "لسان", (None, None)),           # nombre Lisān
    ("r07-p32-isa", 32, "عيسى", (None, None)),             # chaîne + nisba
    ("r08-p32-tabarani", 32, "الكرم", (None, None)),       # nombre Maʿǧam al-Awsaṭ
    ("r09-p33-haut", 33, None, (0.0, 0.34)),               # الغنجار + كتب أمهات + أنواع
    ("r10-p33-faqih", 33, "الفقيه", (None, None)),         # nombre al-Faqīh
    ("r11-p34-taqyim", 34, None, (0.0, 0.26)),             # items التقويم 1-3
    ("r12-p34-ibnalsalah", 34, "الصلاح", (None, None)),    # citation
    ("r13-p34-muqaddima", 34, "مقدمة", (None, None)),      # nombre ص
    ("r14-p34-iidad", 34, None, (0.74, 1.0)),              # الإعداد القبلي
]


def band(page, y0f, y1f, dpi, path):
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0f, r.x1, r.y0 + r.height * y1f)
    page.get_pixmap(dpi=dpi, clip=clip).save(path)


def anchor(page, needle, dpi, path, pad_above=0.030, pad_below=0.030):
    hits = page.search_for(needle)
    if not hits:
        return False
    r = page.rect
    top = min(h.y0 for h in hits) / r.height
    bot = max(h.y1 for h in hits) / r.height
    band(page, max(0.0, top - pad_above), min(1.0, bot + pad_below), dpi, path)
    return True


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    dpi = 600
    for name, pno, needle, frac in CROPS:
        page = doc[pno - 1]
        path = f"{OUT}/{name}.png"
        if needle is None:
            band(page, frac[0], frac[1], dpi, path)
        else:
            if not anchor(page, needle, dpi, path):
                print(f"ANCRE INTROUVABLE p{pno} : {needle!r} → bande 1/3")
                band(page, 0.33, 0.66, dpi, path)
        print(name, os.path.getsize(path))
    doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
