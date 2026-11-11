# -*- coding: utf-8 -*-
"""Minhāj — micro-crops ciblés leçon 409 hadith-3es (R686) — adjudications fines.
Trois composites empilés, zones 600 dpi p.136-141."""
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r686"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, dpi=600):
    """Retourne l'image du rectangle pleine largeur (fractions y de la page)."""
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0, r.x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, zones, width=1600):
    imgs = []
    for label, (p, a, b) in zones:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append((label, im.resize((width, int(im.height * r)), Image.LANCZOS)))
    sep, lab_h = 10, 44
    H = sum(im.height + lab_h for _, im in imgs) + sep * (len(imgs) + 1)
    sheet = Image.new("RGB", (width, H), (210, 235, 210))
    y = sep
    d = ImageDraw.Draw(sheet)
    for label, im in imgs:
        d.text((12, y + 8), label, fill=(0, 0, 160))
        y += lab_h
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print("OK", path, sheet.size)


# 1) zones p.136-138 : référence āya tamhīd p.136, notice p.137, glose المقصرين
composite("fine-1-p136-137-138", [
    ("p136 ref āya tamhīd (fin)", (136, 0.42, 0.62)),
    ("p136 ligne+début hadith 1174", (136, 0.55, 0.75)),
    ("p137 notice Ibn 'Umar", (137, 0.62, 0.78)),
    ("p137 glose المقصرين", (137, 0.74, 0.90)),
    ("p138 zone ليس على النساء/ويجزئ الرجل", (138, 0.13, 0.34)),
])

# 2) zones p.139 : troisième citation, خذوا عني, dernières lignes, لطولهما p.140
composite("fine-2-p139-140", [
    ("p139 3e citation + commentaire", (139, 0.17, 0.42)),
    ("p139 خذوا عني مناسككم", (139, 0.08, 0.22)),
    ("p139 fin de page (كأن سالمًا…)", (139, 0.82, 1.0)),
    ("p140 zone لطولهما 1180", (140, 0.06, 0.20)),
])

# 3) p.140 bas + p.141 haut : encadré الاشتغال, i'dād, médaillon leçon 21
composite("fine-3-p140-141", [
    ("p140 encadré 1175 + الزرقاني", (140, 0.30, 0.62)),
    ("p140 i'dād أحفظ أحاديث الدرس المقبل", (140, 0.60, 0.86)),
    ("p141 haut : médaillon 21 (leçon 410 fidya)", (141, 0.0, 0.30)),
])
