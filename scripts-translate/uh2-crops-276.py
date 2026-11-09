# -*- coding: utf-8 -*-
# R657 (ouvrier C tick 09:49) — crops 300 dpi des bandes de la leçon 22 uh2 (p.115-119)
# Doctrine R651-R656 : toute récusation par preuve image, jamais deviné.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r657"
import os
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, page 595x765, rendu 300 dpi
ZONES = [
    (115, 30, 260, "p115-banner-objectifs"),
    (115, 260, 520, "p115-tamhid-matn"),
    (115, 520, 760, "p115-fahm"),
    (116, 30, 250, "p116-def-mazid"),
    (116, 250, 450, "p116-hadith-exemple"),
    (116, 450, 620, "p116-commentaire-abuzura"),
    (116, 620, 760, "p116-conditions-ab"),
    (117, 30, 260, "p117-cases-majii"),
    (117, 260, 440, "p117-hukm-thaniya"),
    (117, 440, 620, "p117-mudtarib-def"),
    (117, 620, 760, "p117-mudtarib-shartan"),
    (118, 30, 220, "p118-anwa-sund-exemple"),
    (118, 220, 420, "p118-shahr-daraqutni"),
    (118, 420, 580, "p118-matan-fatima"),
    (118, 580, 760, "p118-masdar-hukm-tahdhib"),
    (119, 30, 260, "p119-taqwim"),
    (119, 260, 560, "p119-istithmar-sakhawi"),
    (119, 560, 760, "p119-idad-l23"),
]
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(0, y0, page.rect.width, y1)
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
