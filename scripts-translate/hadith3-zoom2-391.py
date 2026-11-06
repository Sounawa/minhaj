# -*- coding: utf-8 -*-
"""R631 — zooms ciblés 900 dpi pour trancher les lignes garblées de la leçon 2
(p.17-24 hadith-3es). Chaque zone est repérée par une aiguille dans la couche
brute (mots en miroir), recadrée ±(avant/après) lignes, empilée en piles
zoom-r631-N.png pour lecture VLM fidèle. Sortie : tr-tmp/qa-crops-r631/."""
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUTDIR = "/home/z/my-project/tr-tmp/qa-crops-r631"
doc = fitz.open(PDF)


def line_span(p, needle):
    """(y0, y1) de la 1re ligne contenant l'aiguille (couche brute)."""
    d = doc[p - 1].get_text("dict")
    for blk in d["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            t = "".join(s["text"] for s in ln["spans"])
            if needle in t:
                return ln["bbox"][1], ln["bbox"][3]
    return None


def crop(p, y0, y1, name, dpi=900):
    pg = doc[p - 1]
    pw = pg.rect.width
    pix = pg.get_pixmap(dpi=dpi, clip=fitz.Rect(0, max(0, y0), pw, min(pg.rect.height, y1)))
    path = f"{OUTDIR}/{name}.png"
    pix.save(path)
    print(f"{name}: p.{p} y{round(y0)}-{round(y1)}")
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


# zones : (page, aiguille, marge avant pt, marge après pt, nom)
zones = [
    (19, "ةياور", 30, 130, "z-ruwaya-p19"),        # وفي رواية … لا يلبس بالرفع
    (19, "دارملا", 60, 60, "z-murad-p19"),          # والمراد تحريم المخيط…
    (19, "فظاحلا", 20, 130, "z-hafiz-p19"),         # قال الحافظ … ابن المنذر
    (20, "رازإ", 60, 150, "z-izar-p20"),            # قدر عضو … إزار … يحيى … 910
    (20, "بروغلج", 40, 60, "z-jawarib-p20"),        # كل ما يستر الرجل كالجورب
    (21, "يبعرلا نب", 60, 70, "z-ibn-arabi-p21"),   # ليس الورس بطيب … ملاءمة الشمّ
    (21, "ةحلط", 60, 170, "z-talha-p21"),           # dialogue ʿUmar/Ṭalḥa 912
    (21, "دالوبا نب", 40, 120, "z-asma-p21"),       # أسماء بنت أبي بكر 913 + suite
    (22, "ةراهك", 30, 160, "z-kiraha-p22"),         # القول بالكراهة … سيورة 916
    (22, "ةصفارفلا", 40, 90, "z-farafisa-p22"),     # الفرافصة … 917
    (22, "داقو", 40, 70, "z-waqid-p22"),            # كفن ابنه واقد … لولا أني محرم 919
    (22, "نيحصلا", 60, 80, "z-sahihayn-p22"),       # واقعة عين … إنّ من ألفاظ النص
    (23, "فقيد", 40, 60, "z-tail-p23"),             # ولماذا لم يكن التحريم … لقال
    (23, "229", 60, 40, "z-hafsa-p23"),             # نص 922 حفضصة … الصديق
]

crops = []
for p, needle, up, dn, name in zones:
    sp = line_span(p, needle)
    if sp is None:
        print(f"!! aiguille absente p.{p}: {needle}")
        continue
    y0, y1 = sp
    crops.append(crop(p, y0 - up, y1 + dn, name))

# piles de 2 (ordre des aiguilles) pour limiter les appels VLM
for i in range(0, len(crops), 2):
    pile(crops[i:i + 2], f"zoom-r631-{i // 2 + 1}")

# bannière p.17 : re-crop serré 600 dpi
crop(17, 25, 205, "banniere-p17-serr", dpi=600)
print("OK")
