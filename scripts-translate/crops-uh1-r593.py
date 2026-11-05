#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R593 — crops d'adjudication image, leçon 16 ulum-hadith-tanawi-1
(pdf-mut23h2q-127, الحديث المنقطع والحديث المعضل, p.80-84 de
ulum-hadith-1-thanawi.pdf). Zones calligraphiques/citations muettes ou
dégradées à l'OCR 300 dpi → composites 600 dpi pour lecture image.
Sortie : tr-tmp/qa-crops-r593/comp-<X>.png
Usage : python3 scripts-translate/crops-uh1-r593.py [comp ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r593"
DPI = 600

# (page, y0, y1, x0, x1) en fractions de page — zones ajustées larges
ZONES = {
    # A — p.80 : bandeau des deux bayts du nāẓim (munqaṭiʿ + muʿḍal)
    "A-p80-bayt":  [(80, 0.46, 0.72, 0.06, 0.94)],
    # B — p.81 : glose المعضّل/الساقط + bayt inline «لم يتصل بحال»
    "B-p81-glose": [(81, 0.02, 0.17, 0.06, 0.94)],
    "B-p81-bayt":  [(81, 0.52, 0.74, 0.06, 0.94)],
    # C — p.82 : exemple Tirmiḏī (roḫa/rewṯa) + bandeau ثانيا + quote nāẓim
    "C-p82-tirm":  [(82, 0.04, 0.40, 0.06, 0.94)],
    "C-p82-tanya": [(82, 0.36, 0.62, 0.06, 0.94)],
    # D — p.82 bas + p.83 haut : hadith al-Ḥākim (برئت منكن...)
    "D-p82-bas":   [(82, 0.76, 0.98, 0.06, 0.94)],
    "D-p83-haut":  [(83, 0.02, 0.20, 0.06, 0.94)],
    # E — p.83 : تقويم + استثمار (quote Ibn al-Ṣalāḥ) + أتأمل
    "E-p83-taqwim": [(83, 0.38, 0.60, 0.06, 0.94)],
    "E-p83-istimar": [(83, 0.56, 0.99, 0.06, 0.94)],
    # F — p.84 : الإعداد القبلي complet
    "F-p84-prep":  [(84, 0.02, 0.45, 0.06, 0.94)],
}


def crop(doc, page, y0, y1, x0, x1) -> Image.Image:
    pg = doc[page - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(DPI / 72, DPI / 72), clip=clip)
    img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples)
    return img


def half_split(img):
    """coupe verticale en 2 moitiés (hémistiches droite/gauche) empilées"""
    w, h = img.size
    right = img.crop((w // 2, 0, w, h))
    left = img.crop((0, 0, w // 2, h))
    return [right, left]


def compose(name, parts):
    """empile les images ; largeur cible 1560 max (lisible sans downscale fort)"""
    pieces = []
    for img in parts:
        w, h = img.size
        if w > 1560:
            nh = int(h * 1560 / w)
            img = img.resize((1560, nh), Image.LANCZOS)
        pieces.append(img)
    W = max(p.size[0] for p in pieces)
    H = sum(p.size[1] for p in pieces) + 8 * (len(pieces) - 1)
    canvas = Image.new("RGB", (W, H), (255, 230, 230))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y))
        y += p.size[1] + 8
    path = f"{OUT}/{name}.png"
    canvas.save(path)
    print(f"{path} {canvas.size[0]}x{canvas.size[1]}")


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    want = set(sys.argv[1:]) or set(ZONES)
    doc = fitz.open(PDF)
    for name, zones in ZONES.items():
        if not any(name.startswith(w) or w in name for w in want):
            continue
        imgs = []
        for (page, y0, y1, x0, x1) in zones:
            img = crop(doc, page, y0, y1, x0, x1)
            if "bayt" in name:  # hémistiches en 2 colonnes → moitiés empilées
                imgs += half_split(img)
            else:
                imgs.append(img)
        compose(name, imgs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
