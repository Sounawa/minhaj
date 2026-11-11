# -*- coding: utf-8 -*-
"""Minhāj — adjudications 600 dpi serrées leçon 409 (R686) — batch 2.
Zones mono-ligne/tri-ligne pour trancher les mots litigieux."""
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r686"
doc = fitz.open(PDF)


def zone(pageno, y0, y1, dpi=600):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0, r.y0 + r.height * y0, r.x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def composite(name, zones, width=1450):
    imgs = []
    for label, (p, a, b) in zones:
        im = zone(p, a, b)
        r = width / im.width
        imgs.append((label, im.resize((width, int(im.height * r)), Image.LANCZOS)))
    sep, lab_h = 10, 40
    H = sum(im.height + lab_h for _, im in imgs) + sep * (len(imgs) + 1)
    sheet = Image.new("RGB", (width, H), (215, 240, 215))
    y = sep
    d = ImageDraw.Draw(sheet)
    for label, im in imgs:
        d.text((10, y + 6), label, fill=(0, 0, 160))
        y += lab_h
        sheet.paste(im, (0, y))
        y += im.height + sep
    path = f"{OUT}/{name}.png"
    sheet.save(path)
    print("OK", path, sheet.size)


composite("fine-4-p136-137", [
    ("p136 hadith 1174 encadre complet", (136, 0.58, 0.97)),
    ("p137 fin 1178 : مبشيا يوم النحر + āya + 1178", (137, 0.02, 0.21)),
    ("p137 texte 1184 + 1177 : يُهل/محرم + بمنى", (137, 0.19, 0.36)),
    ("p137 glose المقصرين fin : ويسمى العطف الـ…", (137, 0.855, 0.99)),
])

composite("fine-5-p138-139", [
    ("p138 ليس على النساء + ويجزئ الرجل عن الحلاق", (138, 0.075, 0.30)),
    ("p138 ومحله حين يحل نحره أو ذبحه + مكان الحلاق بمنى", (138, 0.47, 0.65)),
    ("p139 commentaire 3e citation : ففي المرة الثالثة…", (139, 0.235, 0.47)),
])

composite("fine-6-p139-140", [
    ("p139 توفير الشعر : روى…/حتى يُحرم 1179/وليس ذلك على الناس 1179/المشقة", (139, 0.50, 0.80)),
    ("p139 fin : سالم 1184 + يُهل محرما + وكأن سالمًا يرى", (139, 0.78, 0.99)),
    ("p140 لطولهما بتَرك الأخذ منهما 1180", (140, 0.05, 0.21)),
    ("p140 الزرقاني + الإعداد التمهيدي + أحفظ أحاديث الدرس المقبل", (140, 0.55, 0.90)),
])
