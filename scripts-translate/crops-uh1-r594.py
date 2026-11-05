#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R594 — crops d'adjudication image, leçon 17 ulum-hadith-tanawi-1
(pdf-mut23h2q-128, الحديث المدلس, p.85-90 de ulum-hadith-1-thanawi.pdf).
Zones calligraphiques/citations muettes ou dégradées à l'OCR 300 dpi →
composites 600 dpi pour lecture image (VLM skill z-ai vision).
Sortie : tr-tmp/qa-crops-r594/comp-<X>.png
Usage : python3 scripts-translate/crops-uh1-r594.py [comp ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r594"
DPI = 600

# (page, y0, y1, x0, x1) en fractions de page — zones ajustées larges
ZONES = {
    # A — p.85 : bandeau المتن + bayts du nāẓim (mudallas)
    "A-p85-matn":  [(85, 0.46, 0.95, 0.06, 0.94)],
    # B — p.86 : citation des bayts du nāẓim dans le sharḥ (أنواع التدليس)
    "B-p86-bayt":  [(86, 0.32, 0.62, 0.06, 0.94)],
    # C — p.88 : citation « والثاني لا يسقطه لكن يصف » + type shuyūkh
    "C-p88-bayt":  [(88, 0.38, 0.60, 0.06, 0.94)],
    # D — p.89 haut : causes (صغر سنه «أو أكبر» / إيهام كثرة الشيوخ)
    "D-p89-haut":  [(89, 0.02, 0.30, 0.06, 0.94)],
    # E — p.89 milieu : حكم التدليس (isnād/shuyūkh/mutūn + hadith qudsī Bukhārī)
    "E-p89-milieu": [(89, 0.26, 0.76, 0.06, 0.94)],
    # F — p.89 bas : bandeau التقويم + 3 questions
    "F-p89-taqwim": [(89, 0.70, 1.00, 0.06, 0.94)],
    # G — p.90 haut : bandeau الاستثمار + citation Ibn aṣ-Ṣalāḥ [74/1]
    "G-p90-istimar": [(90, 0.02, 0.46, 0.06, 0.94)],
    # H — p.90 milieu : أتأمل (Q1 manquante à l'OCR + Q2)
    "H-p90-atamal": [(90, 0.40, 0.70, 0.06, 0.94)],
    # I — p.90 bas : bandeau الإعداد القبلي + 3 questions
    "I-p90-i3dad": [(90, 0.62, 1.00, 0.06, 0.94)],
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
