# -*- coding: utf-8 -*-
# R659 (sous-agent de l'ouvrier D tick 11:26, trace r659-ouvrier-d-tick-1126-subagent,
# claim pdf-mut23h2u-277) — crops 300 dpi des bandes de la leçon 23 uh2 (p.120-124)
# + bannière leçon 24 p.125 (sondage de borne sup).
# Patron : scripts-translate/uh2-crops-278.py. Doctrine : toute récusation par
# preuve image, jamais deviné. Sortie : tr-tmp/qa-crops-r659/.
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r659"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, rendu 300 dpi
ZONES = [
    (120, 30, 260, "p120-banner-objectifs"),
    (120, 260, 520, "p120-tamhid-matn"),
    (120, 520, 765, "p120-sharh-istikhlas"),
    (121, 30, 250, "p121-def-luga-importance"),
    (121, 250, 440, "p121-aqsam-isnad"),
    (121, 440, 765, "p121-isnad-matan-finh"),
    (122, 30, 240, "p122-tasahhif-basr"),
    (122, 240, 430, "p122-tasahhif-sam"),
    (122, 430, 765, "p122-lafz-maani-luga"),
    (123, 30, 260, "p123-muharraf-jabir"),
    (123, 260, 450, "p123-farq"),
    (123, 450, 765, "p123-hukm-ahtadi-taqwim"),
    (124, 30, 330, "p124-istithmar-quote"),
    (124, 330, 765, "p124-istikhlas-idad"),
    (125, 30, 330, "p125-banner-l24"),
]
# pages pleines pour lectures VLM ciblées (bornes + contenu)
for p in (120, 121, 122, 123, 124):
    ZONES.append((p, 0, 765, f"p{p}-full"))

for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, min(y1, page.rect.height))
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
