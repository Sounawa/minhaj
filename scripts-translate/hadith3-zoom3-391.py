# -*- coding: utf-8 -*-
"""R631 — zooms complémentaires (600 dpi, piles de 2) pour la leçon 2 hadith-3es.
Zones repérées à la main sur la carte des lignes (couche dict). Sortie :
tr-tmp/qa-crops-r631/zoom2-r631-*.png"""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUTDIR = "/home/z/my-project/tr-tmp/qa-crops-r631"
doc = fitz.open(PDF)


def crop(p, y0, y1, name, dpi=600):
    pg = doc[p - 1]
    pw = pg.rect.width
    pix = pg.get_pixmap(dpi=dpi, clip=fitz.Rect(0, max(0, y0), pw, min(pg.rect.height, y1)))
    path = f"{OUTDIR}/{name}.png"
    pix.save(path)
    print(name, f"p.{p} y{round(y0)}-{round(y1)}")
    return path


def pile(paths, name):
    ims = [Image.open(f) for f in paths]
    w = max(im.width for im in ims)
    h = sum(im.height for im in ims) + 12 * (len(ims) - 1)
    c = Image.new("RGB", (w, h), (255, 255, 255))
    y = 0
    for im in ims:
        c.paste(im, (0, y))
        y += im.height + 12
    c.save(f"{OUTDIR}/{name}.png")
    print("pile", name)


crops = [
    crop(18, 55, 175, "z2-boxes-p18"),        # boîtes 915 + 918
    crop(19, 570, 765, "z2-hafiz-p19"),       # الخطابي + الحافظ + ابن المنذر
    crop(20, 60, 310, "z2-sarawil-p20"),      # قدر عضو … 910 … البخاري ومسلم
    crop(20, 440, 580, "z2-jawarib-p20"),     # كل ما يستر … الجورب
    crop(21, 110, 205, "z2-ibnarabi-p21"),    # ابن العربي … ملاءمة الشمّ
    crop(21, 240, 445, "z2-talha-p21"),       # dialogue 912
    crop(21, 440, 565, "z2-asma-p21"),        # أسماء 913 … نفض
    crop(22, 100, 300, "z2-kiraha-p22"),      # الكراهة … سيورة 916 … ابن عبد البر
    crop(22, 320, 450, "z2-farafisa-p22"),    # القاسم … الفرافصة 917
    crop(22, 450, 570, "z2-waqid-p22"),       # كفن واقد … 919 … مالك 920
    crop(22, 560, 765, "z2-sahihayn-p22"),    # الصحيحين … واقعة عين
    crop(23, 40, 115, "z2-tail-p23"),         # ولماذا لم يكن … لقال
    crop(23, 490, 665, "z2-hafsa-p23"),       # نص 921 + نص 922
]
pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for i, (a, b) in enumerate(pairs):
    pile([crops[a], crops[b]], f"zoom2-r631-{i + 1}")
pile([crops[12], f"{OUTDIR}/banniere-p17-serr.png"], "zoom2-r631-7")
print("OK")
