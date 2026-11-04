# -*- coding: utf-8 -*-
"""R570 — micro-crops pass 3 : zones litigieuses à 1440 dpi (zoom 20) / 576 dpi (zoom 8)."""
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)

def crop(pno, y0, y1, x0, x1, zoom, name):
    page = doc[pno - 1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(f"{OUT}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height} (p{pno} y{y0}-{y1} zoom{zoom})")

# 1) p.165 : ligne de la citation de ʿĀʾiša au-dessus du crochet 805
crop(165, 530, 600, 80, 520, 20, "q3-p165-kilta-1440")
# 2) p.166 : ligne «وقال: لسنا/أنا مثل رسول الله» + suite (bande y480-660)
crop(166, 480, 660, 80, 520, 12, "q3-p166-mithl")
# 3) p.166 : hadith Ḥamza complet (chaîne + question + réponse + crochet)
crop(166, 840, 1230, 80, 520, 8, "q3-p166-hamza-576")
# 3b) p.166 : crochet du Ḥamza en très haute résolution
crop(166, 1120, 1200, 80, 520, 20, "q3-p166-hamza-bracket-1440")
# 4) p.169 : fragment coranique + crochet 184 (zone لقوله تعالى)
crop(169, 400, 600, 80, 520, 8, "q3-p169-aya-576")
crop(169, 470, 560, 80, 520, 20, "q3-p169-aya-1440")
# 5) p.170 : passage 829 début haute résolution
crop(170, 520, 660, 80, 520, 12, "q3-p170-829-1440")
print("DONE")
