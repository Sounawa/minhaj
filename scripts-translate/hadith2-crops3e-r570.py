# -*- coding: utf-8 -*-
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)
def crop(pno, y0, y1, x0, x1, zoom, name):
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(x0, y0, x1, y1))
    assert pix.height > 0, f"{name}: hauteur nulle !"
    with open(f"{OUT}/{name}.png", "wb") as f:
        f.write(pix.tobytes("png"))
    print(f"{name}: {pix.width}x{pix.height}")
# p.165 intro-b band = pt 444-552 : citation ʿĀʾiša + crochet 805
crop(165, 468, 556, 80, 520, 16, "q3-p165-kilta")
# p.166 bande b = pt 216-336 : «وقال: لسنا/أنا مثل رسول الله»
crop(166, 216, 340, 80, 520, 8, "q3-p166-mithl")
# p.166 Ḥamza : chaîne en fin de bande c + hadith entier bande 812 = pt 456-576
crop(166, 400, 480, 80, 520, 8, "q3-p166-hamza-chain")
crop(166, 456, 580, 80, 520, 8, "q3-p166-hamza")
crop(166, 540, 578, 80, 520, 16, "q3-p166-hamza-bracket")
# p.169 āya + crochet 184 : bande 816b = pt 444-564 ; āya en tête de bande
crop(169, 436, 500, 80, 520, 16, "q3-p169-aya-1152")
crop(169, 436, 570, 80, 520, 6, "q3-p169-aya")
# p.170 passage 829 = pt 252-384
crop(170, 248, 390, 80, 520, 10, "q3-p170-829-864")
print("DONE")
