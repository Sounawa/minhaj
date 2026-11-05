#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R600 — crops d'adjudication image, leçon 23 ulum-hadith-tanawi-1
(pdf-mut23h2q-134, المُدَبَّج, p.113-116 de ulum-hadith-1-thanawi.pdf).
Zones calligraphiques/citations muettes ou divergentes à l'OCR 300 dpi →
composites 600 dpi pour lecture image (adjudication, jamais devinée).
Divergences OCR constatées : bayt المتن (حَفا/حَقا وانتخه/انتخة) répété p.113
et p.114 (فاعرفه/فأغرفه) ; isnad long p.115 ; citation Ibn Ṣalāḥ p.116 ;
comptage questions الإعداد القبلي p.116.
Sortie : tr-tmp/qa-crops-r600/comp-<X>.png
Usage : python3 scripts-translate/crops-uh1-r600.py [comp ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r600"
DPI = 600

# (page, y0, y1, x0, x1) en fractions de page — zones ajustées larges
ZONES = {
    # A — p.113 : bandeau المتن + bayt du nāẓim (mudabbaǧ) + الشرح (3 gloses)
    "A-p113-matn":  [(113, 0.50, 0.80, 0.06, 0.94)],
    "B-p113-sharh": [(113, 0.68, 0.98, 0.06, 0.94)],
    # C — p.114 : bayt répété dans le taʿrīf + fāʾida/puis-les bullets
    "C-p114-bayt":  [(114, 0.28, 0.58, 0.06, 0.94)],
    # D — p.115 : isnad long (aḥmad … ʿĀʾiša) + référence [al-Musalsalāt]
    "D-p115-isnad": [(115, 0.38, 0.72, 0.06, 0.94)],
    # E — p.115 bas : bandeau التقويم + questions
    "E-p115-taqwim": [(115, 0.68, 1.00, 0.06, 0.94)],
    # F — p.116 haut : bandeau الاستثمار + citation Ibn Ṣalāḥ + question
    "F-p116-istimar": [(116, 0.02, 0.52, 0.06, 0.94)],
    # G — p.116 bas : bandeau الإعداد القبلي + questions (comptage)
    "G-p116-i3dad": [(116, 0.50, 1.00, 0.06, 0.94)],
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
            if "bayt" in name or "matn" in name:  # hémistiches en colonnes
                imgs += half_split(img)
            else:
                imgs.append(img)
        compose(name, imgs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
