# -*- coding: utf-8 -*-
# R654 — crops ciblés des zones altérées de la leçon 19 uh2 (p.97-101)
# Doctrine R651-R653 : toute récusation par preuve image, jamais deviné.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r654"
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, nom) — y en points, page H=765, rendu 300 dpi
ZONES = [
    (97, 315, 465, "p97-matn"),       # matn Ibn Ḥaǧar (الطلث... garbled)
    (97, 560, 765, "p97-istikhlas"),  # استخلاص المضامين (garbles fin de page)
    (99, 235, 330, "p99-asbab-wadh"), # أسباب وضع الحديث (الإغراب ?)
    (99, 350, 470, "p99-hadith"),     # citation « من كذب علي متعمدا... » + attribution
    (100, 85, 185, "p100-tuham-a"),   # أسباب اتهام الراوي بالكذب (أ) — très garbled
    (100, 515, 700, "p100-istithmar"),# الاستثمار citation السخاوي + question
    (101, 40, 175, "p101-idad"),      # الإعداد القبلي items 1-2 (garbled)
]
SCALE = 300 / 72.0
for p, y0, y1, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(30, y0, page.rect.width - 30, y1)
    pix = page.get_pixmap(dpi=300, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
