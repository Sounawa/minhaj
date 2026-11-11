# -*- coding: utf-8 -*-
"""Minhāj — crops ciblés complémentaires leçon 409 hadith-3es (R687, canal principal).
Zones manquantes aux micro-crops r686 : p.136 bas, p.138 haut+bas, p.140 milieux, p.141 haut."""
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r687"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0, r.x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, zones, width=1500):
    imgs = []
    for p, a, b in zones:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append(im.resize((width, int(im.height * r)), Image.LANCZOS))
    sep, lab_h = 12, 40
    H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
    sheet = Image.new("RGB", (width, H), (220, 210, 240))
    y = 0
    for im in imgs:
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print("OK", path, sheet.size)


import os
os.makedirs(OUT, exist_ok=True)

# t1 : p.136 bas — fin du tamhīd, référence de l'āya, question d'ouverture, encadré 1174 complet
composite("t1-p136-bas", [(136, 0.40, 1.00)])

# t2 : p.138 haut (items 2-3 de l'extraction + bannière fiqh) + p.138 bas (محله + مكان الحلاق + 1177 re-cité)
composite("t2-p138", [(138, 0.00, 0.20), (138, 0.66, 1.00)])

# t4 : p.140 — milieu (bannière تقويم + questions) + bas (fin encadré 1175 + istithmār + iʿdād)
composite("t4-p140", [(140, 0.13, 0.31), (140, 0.44, 0.98)])

# t5 : p.141 haut — médaillon 21 + objectifs de la leçon 21 (fidiya) — borne supérieure
composite("t5-p141-haut", [(141, 0.00, 0.32)])
