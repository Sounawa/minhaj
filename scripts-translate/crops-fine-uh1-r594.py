#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R594 — crops FINS d'adjudication, leçon 17 ulum-hadith-tanawi-1
(pdf-mut23h2q-128, الحديث المدلس, p.85-90). Mots/vers contestés entre
OCR 300 dpi et VLM 600 dpi → bandes étroites 1200-2400 dpi, pleine largeur.
Sortie : tr-tmp/qa-crops-r594/fin-<N>.png
Usage : python3 scripts-translate/crops-fine-uh1-r594.py [fin ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r594"

# nom → (page, y0, y1, x0, x1, dpi, largeur cible)
ZONES = {
    # p.85 matn : bandeau + 3 lignes de bayts (bandes horizontales pleine largeur)
    "fin1-p85-matn-a": (85, 0.46, 0.64, 0.06, 0.94, 1200, 2400),
    "fin2-p85-matn-b": (85, 0.62, 0.80, 0.06, 0.94, 1200, 2400),
    "fin3-p85-matn-c": (85, 0.78, 0.97, 0.06, 0.94, 1200, 2400),
    # p.86 : citation des bayts dans le sharḥ (après «بقوله:»)
    "fin4-p86-verse": (86, 0.48, 0.78, 0.06, 0.94, 1200, 2400),
    # p.86 haut : définition الشرح (المشتري…)
    "fin5-p86-top": (86, 0.00, 0.14, 0.06, 0.94, 1200, 2400),
    # p.88 : bayt «والثاني لا يسقطه لكن يصف» à 2400 dpi
    "fin6-p88-bayt": (88, 0.40, 0.56, 0.06, 0.94, 2400, 2600),
    # p.88 : titre النوع الثاني تدليس الشيوخ/الشيخ
    "fin7-p88-titre": (88, 0.26, 0.42, 0.06, 0.94, 1200, 2400),
    # p.89 : cause صغر سنه (queue «أو أكبر …») + إيهام كثرة الشيوخ
    "fin8-p89-causes": (89, 0.02, 0.20, 0.06, 0.94, 1200, 2400),
    # p.89 : حكم تدليس الشيوخ (مدلس الشيوخ تقبل روايته…)
    "fin9-p89-shuyukh": (89, 0.44, 0.60, 0.06, 0.94, 1200, 2400),
    # p.90 : citation Ibn aṣ-Ṣalāḥ complète à 1200 dpi
    "fin10-p90-quote": (90, 0.04, 0.42, 0.06, 0.94, 1200, 2400),
}


def crop(doc, page, y0, y1, x0, x1, dpi) -> Image.Image:
    pg = doc[page - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    return Image.frombytes("RGB", (pm.width, pm.height), pm.samples)


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    want = set(sys.argv[1:]) or set(ZONES)
    doc = fitz.open(PDF)
    for name, (page, y0, y1, x0, x1, dpi, tw) in ZONES.items():
        if want != set(ZONES) and not any(name.startswith(w) for w in want):
            continue
        img = crop(doc, page, y0, y1, x0, x1, dpi)
        w, h = img.size
        if w > tw:
            nh = int(h * tw / w)
            img = img.resize((tw, nh), Image.LANCZOS)
        path = f"{OUT}/{name}.png"
        img.save(path)
        print(f"{path} {img.size[0]}x{img.size[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
