# -*- coding: utf-8 -*-
"""Minhāj — crops leçon 411 hadith-3es (R689-c, leçon 22 le locuste et le rasage,
p.147-152). Six pages plein-cadre à 300 dpi + zooms d'adjudication."""
import fitz
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r689c"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# 1. pages pleines 300 dpi
for pg in range(147, 153):
    pix = doc[pg - 1].get_pixmap(dpi=300)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img.save(f"{OUT}/m411-p{pg}.png")
print("pages pleines OK")

# 2. zooms d'adjudication (bandes empilées, 600 dpi)
X0, X1 = 0.04, 0.96


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(
        r.x0 + r.width * X0,
        r.y0 + r.height * y0,
        r.x0 + r.width * X1,
        r.y0 + r.height * y1,
    )
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, bands, width=1500):
    imgs = []
    for p, a, b in bands:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append(im.resize((width, int(im.height * r)), Image.LANCZOS))
    sep = 12
    H = sum(im.height for im in imgs) + sep * (len(imgs) - 1)
    sheet = Image.new("RGB", (width, H), (255, 210, 210))
    y = 0
    for im in imgs:
        sheet.paste(im, (0, y))
        y += im.height + sep
    sheet.save(f"{OUT}/{name}.png")
    print(name, sheet.size)


# z1 : p.147 — objectifs + tamhīd + texte 1252 (le haut de page)
composite("z411-1-p147-objectifs-tamhid-texte", [(147, 0.06, 0.62)])
# z2 : p.147 bas — suite du texte 1252 + numéro
composite("z411-2-p147-texte1252-fin", [(147, 0.58, 0.98)])
# z3 : p.148 — texte 1263 + notice + gloses
composite("z411-3-p148-texte1263-notice-gloses", [(148, 0.05, 0.55)])
# z4 : p.148 bas — la zone استخلاص المضامين et le début du hadith 1255
composite("z411-4-p148-istihlas-hadith", [(148, 0.50, 0.98)])
# z5 : p.149 — hadith 1255 fin + حلق لعذر + مدين مدين
composite("z411-5-p149-fidya-adhr", [(149, 0.05, 0.60)])
# z6 : p.149 bas — la āya al-Baqara + l'argument
composite("z411-6-p149-aya-argument", [(149, 0.55, 0.98)])
# z7 : p.150 — حلق عمد + من تفل شعرا (1256) + ثانيا اشتراك جماعة
composite("z411-7-p150-amd-istishrak", [(150, 0.05, 0.60)])
# z8 : p.150 bas-151 — عدلان + عمر استعان + l'étonnement (1241 re-cité)
composite("z411-8-p150-151-adlan-umar", [(150, 0.55, 0.98), (151, 0.05, 0.30)])
# z9 : p.151 — المائدة 55 + le dialogue d'Omar + استخلاص + texte suivant
composite("z411-9-p151-maida-istihlas", [(151, 0.25, 0.80)])
# z10 : p.151 bas-152 — exploitation + i'dād (2 questions العمرة)
composite("z411-10-p151-152-istithmar-iadad", [(151, 0.75, 0.98), (152, 0.05, 0.45)])
