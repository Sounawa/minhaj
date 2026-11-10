# -*- coding: utf-8 -*-
"""Minhāj — Crops COMPLÉMENT leçon 407 hadith-3es (R675, ouvrier C trace
1a1a172f41684dc9-cron-agent-loop-202611101441) : zones JAMAIS lues par r674/r674c
— p.124 haut (médaillon 18 + objectifs + tamhīd) et bas (hadith 1121), p.125 bas
(notice savant + gloses + résumé + taqwīm), p.126 milieu (règle الواجب + 1142),
p.127 haut (règle فوات الحج continuation), p.128 milieu (athar Ibn ʿAbbās 1138/1139
suite + استفادة + taqwīm). Mécanique hadith3-crops-407-r674c.py."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r675c"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

ZONES = [
    # (page, y0, y1, zoom, tag)
    (124, 0, 200, 5, "c-p124-top"),       # médaillon 18 + bannière + objectifs
    (124, 200, 340, 7, "c-p124-tamhid"),  # tamhīd avant l'āya
    (124, 435, 620, 8, "c-p124-h1121"),   # hadith 1121 (isnad + texte)
    (124, 620, 765, 7, "c-p124-bottom"),  # fin de page 124
    (125, 255, 420, 7, "c-p125-notice"),  # notice savant après 1135
    (125, 420, 765, 6, "c-p125-taqwim"),  # gloses + résumé + taqwīm
    (126, 390, 475, 9, "c-p126-wajib"),   # règle الهدي الواجب + citation 1142?
    (127, 0, 85, 8, "c-p127-top"),        # règle فوات الحج continuation (هلال/شغل)
    (128, 255, 430, 8, "c-p128-abbas"),   # athar 2 Ibn ʿAbbās (لا أظنه إلا...)
    (128, 430, 590, 7, "c-p128-istifada"),# استفادة + taqwīm questions
]


def crop(page_no, y0, y1, zoom, tag):
    page = doc[page_no - 1]
    w = page.rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(0, y0, w, y1))
    pix.save(f"{OUT}/{tag}.png")
    print(f"OK {tag} — {pix.width}×{pix.height}px")


for pg, y0, y1, zoom, tag in ZONES:
    crop(pg, y0, y1, zoom, tag)
print("crops r675c terminés")
