#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R594 — crops ULTRA-FINS (2400-3600 dpi), leçon 17 ulum-hadith-tanawi-1.
Mots encore disputés après les passes 300/600/1200/2400 dpi :
bayt 3 (يُسْقِطُهُ/يَسْقُطْهُ, يَنْعَرِفْ/يَنْصَرِفْ/يَتَعَرَّفْ/يَتَّصِفْ),
bayt 2 (عَمَّنْ/عَنْ, يَنْقِلَ/يَنْقُلُ), queue «صغر سنه», définition الشرح.
Sortie : tr-tmp/qa-crops-r594/uf-<N>.png
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r594"

ZONES = {
    # p.85 bayt 3 complet (والثان لا … يصف ✽ أوصافه بما به لا …)
    "uf1-p85-bayt3": (85, 0.82, 0.96, 0.06, 0.94, 3600, 2800),
    # p.85 bayt 2 hémistiche gauche seul (ينقل عمن فوقه بعن وأن)
    "uf2-p85-bayt2g": (85, 0.71, 0.83, 0.05, 0.50, 3600, 2400),
    # p.88 copie du bayt 3 complète
    "uf3-p88-bayt3": (88, 0.42, 0.54, 0.06, 0.94, 3600, 2800),
    # p.89 ligne صغر سنه (queue «أو أكبر …»)
    "uf4-p89-sighr": (89, 0.02, 0.10, 0.06, 0.94, 2400, 2600),
    # p.86 définition الشرح (السلعة/المشتري…)
    "uf5-p86-sharh": (86, 0.12, 0.32, 0.06, 0.94, 1200, 2400),
    # p.86 phrase «لأن الراوي دلّس ولم يسمّ من حدّثه … لاشتغالهما في الخفاء»
    "uf6-p86-dallas": (86, 0.48, 0.72, 0.06, 0.94, 2400, 2600),
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
