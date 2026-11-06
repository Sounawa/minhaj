#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R616 — crops de QA localisés (méthode locate R553-R615) pour la leçon 4
ulum-hadith-tanawi-2 (pdf-mut23h2u-258, p.26-29). Chaque nombre de la leçon
est tranché par image, JAMAIS deviné (doctrine R613-R615 : couche pdftotext
inversée EN MIROIR, couche PyMuPDF FIDÈLE à l'imprimé).
Needles numériques cherchés dans la COUCHE (positions exactes), fallback
bandes fractionnaires ; sorties : tr-tmp/qa-crops-r616/*.png
Usage : python3 scripts-translate/r616-crops.py"""
import os

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r616"

# (nom, page, mode, données)
#  mode "needle" : (needles, marge_x, marge_y, dpi, bande_fallback(y0f,y1f))
#  mode "bande"  : (y0f, y1f, dpi)
#  mode "rect"   : (x0, y0, x1, y1, dpi)
CIBLES = [
    # bannière leçon 4 (preuve de la borne inférieure, calligraphie muette)
    ("c14-p26-banniere-l4", 26, "bande", (0.0, 0.20, 600)),
    # référence Maqāyīs p.26 + pied de page « 26 »
    ("c1-p26-bas-maqayis", 26, "bande", (0.895, 0.985, 900)),
    ("c1b-p26-maqayis-tail", 26, "rect", (20, 692, 260, 724, 1200)),
    # les deux pavés-flèches des conditions du mašhūr p.27
    ("c2-p27-paves-conditions", 27, "bande", (0.165, 0.30, 900)),
    # graphie douteuse « فاض الماء يفيض فيضاء / منهم من غاير » p.27
    ("c3-p27-lisantsha", 27, "bande", (0.075, 0.145, 900)),
    # les quatre dates hégériennes de la liste des مصنفات p.28
    ("c4-p28-zarkashi-794", 28, "needle", (("794",), 140, 16, 900, (0.335, 0.375))),
    ("c5-p28-ibnhajar-852", 28, "needle", (("852",), 140, 16, 900, (0.39, 0.435))),
    ("c6-p28-sakhawi-902", 28, "needle", (("902",), 140, 16, 900, (0.44, 0.485))),
    ("c7-p28-suyuti-911", 28, "needle", (("911",), 140, 16, 900, (0.475, 0.52))),
    # date العجلوني (pavé compacté — la couche ne porte que « 2 »)
    ("c8-p28-ajluni-date", 28, "bande", (0.545, 0.615, 1200)),
    # la liste des مصنفات en contexte
    ("c15-p28-liste-masnafat", 28, "bande", (0.25, 0.56, 600)),
    # citation عياض : lignes اهتبالهم/اهتمامهم et تنخيلهم (graphies douteuses)
    ("c10-p28-iyad-quote-lines", 28, "bande", (0.725, 0.855, 600)),
    # référence الإلماع « ص: 7 »
    ("c9-p28-iyad-ref", 28, "bande", (0.855, 0.905, 900)),
    # référence السخاوي « 11/4 » (استتمار) p.29
    ("c11-p29-sakhawi-ref", 29, "needle", (("11/4", "4/11"), 200, 16, 900, (0.42, 0.475))),
    # الإعداد القبلي p.29 (أعد درس العزيز — preuve de la borne supérieure)
    ("c12-p29-idad-qabli", 29, "bande", (0.55, 0.83, 600)),
    # bannière leçon 5 p.30 (preuve de la borne supérieure, calligraphie muette)
    ("c13-p30-banniere-l5", 30, "bande", (0.0, 0.30, 600)),
    # --- compléments R616 (relance) : graphies et pavés à trancher ---
    # objectifs de la leçon 4 (sous la bannière p.26)
    ("c19-p26-objectifs", 26, "bande", (0.0, 0.13, 600)),
    # tamhīd + متن ابن حجر p.26 (muṭūn — preuve image)
    ("c20-p26-tamhid-mutun", 26, "bande", (0.30, 0.52, 600)),
    # glose marginale المستفيض p.26 (marge droite)
    ("c21-p26-glose-margin", 26, "rect", (490, 300, 545, 480, 900)),
    # ligne ب- اصطلاحا p.27 (جماعة من أئمة الفقهاء ? — graphie à trancher)
    ("c16-p27-istilahan-line", 27, "bande", (0.035, 0.105, 900)),
    # glose marginale p.27 (fragments couche « أئمة/جماعة »)
    ("c17-p27-margin-gloss", 27, "rect", (480, 55, 545, 220, 900)),
    # titre ثالثا p.28 : le « ب 2 » des couches (في ?) — graphie à trancher
    ("c22-p28-fi-word", 28, "rect", (330, 168, 530, 205, 1200)),
    # question marginale p.29 (لماذا لم يُعتبر المستفيض والمتواتر…)
    ("c18-p29-margin-q", 29, "rect", (480, 290, 545, 430, 900)),
    # التهذيب p.29 (section complète, preuve image)
    ("c23-p29-tahdhib", 29, "bande", (0.0, 0.28, 600)),
    # raffinements de la 1re passe (crops serrés sur graphies douteuses)
    ("c1c-p26-maqayis-1200", 26, "rect", (40, 690, 280, 726, 1200)),
    ("c4b-p28-zarkashi-tight", 28, "needle", (("794",), 90, 12, 1200, (0.335, 0.375))),
    ("c8b-p28-ajluni-date-tight", 28, "bande", (0.545, 0.615, 1200)),
    ("c10b-p28-ihtibal-tight", 28, "rect", (330, 590, 540, 622, 1200)),
    ("c10c-p28-tankhil-tight", 28, "rect", (300, 612, 540, 646, 1200)),
    ("c3b-p27-ghayara-tight", 27, "bande", (0.36, 0.46, 1200)),
]


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    for nom, pnum, mode, data in CIBLES:
        page = doc[pnum - 1]
        pw, ph = page.rect.width, page.rect.height
        if mode == "bande":
            y0f, y1f, dpi = data
            clip = fitz.Rect(0, ph * y0f, pw, ph * y1f)
            png = f"{OUT}/{nom}.png"
            page.get_pixmap(dpi=dpi, clip=clip).save(png)
            print(f"OK {os.path.basename(png)} bande={y0f}-{y1f} dpi={dpi}")
        elif mode == "rect":
            x0, y0, x1, y1, dpi = data
            clip = fitz.Rect(x0, y0, x1, y1)
            png = f"{OUT}/{nom}.png"
            page.get_pixmap(dpi=dpi, clip=clip).save(png)
            print(f"OK {os.path.basename(png)} rect={clip} dpi={dpi}")
        else:  # needle
            needles, mx, my, dpi, bande = data
            rects = []
            for needle in needles:
                for r in page.search_for(needle):
                    rects.append(fitz.Rect(max(0, r.x0 - mx), max(0, r.y0 - my),
                                           min(pw, r.x1 + mx), min(ph, r.y1 + my)))
            if not rects:
                y0f, y1f = bande
                clip = fitz.Rect(0, ph * y0f, pw, ph * y1f)
                page.get_pixmap(dpi=dpi, clip=clip).save(f"{OUT}/{nom}.png")
                print(f"FALLBACK-BANDE {nom} bande={y0f}-{y1f} dpi={dpi}")
                continue
            rects.sort(key=lambda r: (r.y0, r.x0))
            fusion = [fitz.Rect(rects[0])]
            for r in rects[1:]:
                if r.y0 <= fusion[-1].y1 + 6:
                    fusion[-1] |= r
                else:
                    fusion.append(r)
            clips = fusion[:3]
            for i, clip in enumerate(clips, 1):
                png = f"{OUT}/{nom}.png" if len(clips) == 1 else f"{OUT}/{nom}-{i}.png"
                page.get_pixmap(dpi=dpi, clip=clip).save(png)
                print(f"OK {os.path.basename(png)} clip={clip} dpi={dpi}")


if __name__ == "__main__":
    main()
