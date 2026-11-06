#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R615 — crops de QA localisés (méthode locate R553-R575) pour la leçon 3
ulum-hadith-tanawi-2 (pdf-mut23h2u-257, p.20-25). Chaque nombre en conflit
couche/OCR est tranché par image, JAMAIS deviné (doctrine R613-R614).
Needles cherchés dans la COUCHE (positions exactes) puis crop élargi rendu
à 900 dpi (600 si bande). Sortie : tr-tmp/qa-crops-r615/*.png
Usage : python3 scripts-translate/r615-crops.py"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r615"

# (nom, page, needles ou bande (y0f, y1f), marge_x, marge_y)
CIBLES = [
    ("c1-p20-objectifs", 20, ("أدرك", "أتبين"), 40, 14),
    ("c2-p21-maqayis", 21, ("48",), 130, 12),
    ("c3-p22-kitab-ilm", 22, ("61", "كذب على النبي"), 120, 12),
    ("c4-p23-lisan", 23, ("892", "298"), 130, 12),
    ("c4b-p23-alqama", 23, ("علقمة",), 150, 12),
    ("c5-p23-bas-conditions", 23, (0.62, 1.0)),
    ("c5b-p24-haut-conditions", 24, (0.0, 0.22)),
    ("c6-p24-kifaya-malik", 24, ("951", "159", "الكفاية"), 130, 12),
    ("c7-p25-titre-taqyim", 25, (0.0, 0.30)),
    ("c8-p25-kifaya", 25, ("31",), 150, 12),
    ("c9-p25-idad-qabli", 25, (0.60, 1.0)),
]


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    for nom, pnum, *rest in CIBLES:
        page = doc[pnum - 1]
        pw, ph = page.rect.width, page.rect.height
        if len(rest) == 3:
            needles, mx, my = rest
            rects = []
            for needle in needles:
                for r in page.search_for(needle):
                    rects.append(fitz.Rect(max(0, r.x0 - mx), max(0, r.y0 - my),
                                           min(pw, r.x1 + mx), min(ph, r.y1 + my)))
            if not rects:
                print(f"!! {nom} : needle introuvable")
                continue
            # fusion des rects qui se chevauchent ou proches verticalement
            rects.sort(key=lambda r: (r.y0, r.x0))
            fusion = [fitz.Rect(rects[0])]
            for r in rects[1:]:
                if r.y0 <= fusion[-1].y1 + 6:
                    fusion[-1] |= r
                else:
                    fusion.append(r)
            clips = fusion[:3]  # au plus 3 zones par cible
            for i, clip in enumerate(clips, 1):
                dpi = 900 if clip.height < 70 else 600
                png = f"{OUT}/{nom}.png" if len(clips) == 1 else f"{OUT}/{nom}-{i}.png"
                page.get_pixmap(dpi=dpi, clip=clip).save(png)
                print(f"OK {os.path.basename(png)} clip={clip} dpi={dpi}")
        else:  # bande fractionnaire pleine largeur
            y0f, y1f = rest[0]
            clip = fitz.Rect(0, ph * y0f, pw, ph * y1f)
            png = f"{OUT}/{nom}.png"
            page.get_pixmap(dpi=600, clip=clip).save(png)
            print(f"OK {os.path.basename(png)} bande={y0f}-{y1f} dpi=600")


if __name__ == "__main__":
    main()
