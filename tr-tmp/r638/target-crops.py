#!/usr/bin/env python3
"""R638 — crops ciblés 1200 dpi pour adjudication finale leçon 391."""
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)
OUT = "/home/z/my-project/tr-tmp/r638"
zones = [
    ("p17-909-ouverture", 17, 600, 690),   # question + نعلين/إزارا
    ("p20-sarawil-glose", 20, 80, 175),    # كالتبان والقفاز
    ("p21-talha-mudarra", 21, 293, 365),   # إنما هو مدرّع
    ("p21-nafad-rijal", 21, 508, 570),     # فإذا نفض كره للرجال...
    ("p22-kiraha-siyur", 22, 85, 150),     # والقول بالكراهة...
    ("p22-section2-takhmir", 22, 285, 340),# titre section 2
    ("p22-farafisa-917", 22, 378, 445),    # 917 personnage
    ("p22-waqid-919", 22, 448, 535),       # 919 fin Wāqid
    ("p23-fatima-922", 23, 545, 630),      # 922 texte Fāṭima
]
for name, p, y0, y1 in zones:
    pg = doc[p-1]
    pix = pg.get_pixmap(dpi=1200, clip=fitz.Rect(0, y0, pg.rect.width, y1))
    pix.save(f"{OUT}/crop-{name}.png")
    print(name, "->", pix.width, "x", pix.height)
