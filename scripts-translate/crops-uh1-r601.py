#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R601 — crops d'adjudication image, leçon 24 ulum-hadith-tanawi-1
(pdf-mut23h2q-135, المُتَّفِق والمُفْتَرِق, p.117-120 de ulum-hadith-1-thanawi.pdf).
Zones à trancher : bayt المتن (ذكرنا/تكررنا) p.117 + re-quote p.118 ; mots
«حبان/حيان/جيان» p.118 ; الثانية صورة bas p.118 ; الثالثة/الخامسة/السابعة
(أبو حمزة بجيم وراء) p.119 ; الثامنة + fin «فيقولون في» bas p.119 ;
citation الاستثمار (attribution + texte diacrité) p.120.
Sortie : tr-tmp/qa-crops-r601/c-<X>.png
Usage : python3 scripts-translate/crops-uh1-r601.py [c-... ...]
"""
import os
import sys

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r601"
DPI = 600

# (page, y0, y1, x0, x1) en fractions de page — zones ajustées larges
ZONES = {
    # A — p.117 : bandeau المتن + bayt (adjudication ذكرنا/تكررنا, وضده)
    "A-p117-bayt":  [(117, 0.66, 0.82, 0.06, 0.94)],
    # B — p.118 : bayt re-quote dans التعريف
    "B-p118-bayt":  [(118, 0.34, 0.47, 0.06, 0.94)],
    # C — p.118 : ligne «حبان/حيان/جيان» (كذلك أن يتفقا في اللفظ والخط)
    "C-p118-hbn":   [(118, 0.72, 0.83, 0.06, 0.94)],
    # D — p.118 bas : الثانية صورة (أجدادهم)
    "D-p118-thania": [(118, 0.86, 1.00, 0.06, 0.94)],
    # E — p.119 haut : الثالثة + الرابعة (الحوضي/الأنصاري)
    "E-p119-thalatha": [(119, 0.00, 0.16, 0.06, 0.94)],
    # F — p.119 : الخامسة + السادسة (عياش بتحتية ومعجمة / صالح بن أبي صالح)
    "F-p119-khamisa": [(119, 0.16, 0.30, 0.06, 0.94)],
    # G — p.119 : السابعة complète (عبد الله + أبو حمزة + شعبة + بجيم وراء)
    "G-p119-sabi3a": [(119, 0.28, 0.52, 0.06, 0.94)],
    # H — p.119 bas : الثامنة (الصنعاني/الحنفي) + وفرق جماعة + fin de page
    "H-p119-thamina": [(119, 0.50, 1.00, 0.06, 0.94)],
    # I — p.120 : box الاستثمار complet (600 dpi, texte diacrité)
    "I-p120-istimar": [(120, 0.28, 0.54, 0.06, 0.94)],
    # J — p.120 : ligne d'attribution de la citation (1200 dpi)
    "J-p120-attr":  [(120, 0.31, 0.38, 0.06, 0.94)],
}
DPI_OVERRIDE = {"A-p117-bayt": 1200, "B-p118-bayt": 1200, "C-p118-hbn": 1200, "J-p120-attr": 1200}


def crop(doc, page, y0, y1, x0, x1, dpi) -> Image.Image:
    pg = doc[page - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples)
    return img


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    want = set(sys.argv[1:])
    doc = fitz.open(PDF)
    for name, zones in ZONES.items():
        if want and name not in want:
            continue
        imgs = [crop(doc, p, y0, y1, x0, x1, DPI_OVERRIDE.get(name, DPI)) for (p, y0, y1, x0, x1) in zones]
        if len(imgs) == 1:
            imgs[0].save(f"{OUT}/c-{name}.png")
        else:
            w = max(i.width for i in imgs)
            h = sum(i.height for i in imgs) + 12 * (len(imgs) - 1)
            comp = Image.new("RGB", (w, h), (40, 40, 40))
            y = 0
            for i in imgs:
                comp.paste(i, (0, y))
                y += i.height + 12
            comp.save(f"{OUT}/c-{name}.png")
        print("OK", name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
