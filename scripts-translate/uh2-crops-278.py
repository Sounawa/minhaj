# -*- coding: utf-8 -*-
# R658 (ouvrier D tick 11:26) — crops 300 dpi des bandes de la leçon 24 uh2 (p.125-128)
# Doctrine R651-R657 : toute récusation par preuve image, jamais deviné.
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r658"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, rendu 300 dpi
ZONES = [
    (125, 30, 260, "p125-banner-objectifs"),
    (125, 260, 520, "p125-tamhid-matn"),
    (125, 520, 760, "p125-fahm-gharib"),
    (126, 30, 250, "p126-analyse-qawal"),
    (126, 250, 450, "p126-tafsil-hukm"),
    (126, 450, 620, "p126-istithna-muslim"),
    (126, 620, 760, "p126-taqtip-ainimma"),
    (127, 30, 260, "p127-mana-hukm"),
    (127, 260, 460, "p127-ibnsumayna-malik"),
    (127, 460, 620, "p127-fasl-abc"),
    (127, 620, 760, "p127-bottom-matn-amal"),
    (128, 30, 220, "p128-ahtadi-ibnsalah"),
    (128, 220, 420, "p128-taqwim"),
    (128, 420, 620, "p128-istithmar-iyad"),
    (128, 620, 760, "p128-idad-l25"),
    # pages pleines pour lectures VLM ciblées
]
for p in (125, 126, 127, 128):
    ZONES.append((p, 0, 765, f"p{p}-full"))

for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, min(y1, page.rect.height))
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
