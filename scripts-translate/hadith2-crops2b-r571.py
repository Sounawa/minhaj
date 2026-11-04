# -*- coding: utf-8 -*-
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
doc = fitz.open(PDF)
def crop(pno, y0, y1, zoom, name):
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(80, y0, 520, y1))
    with open(f"{OUT}/{name}.png", "wb") as f:
        f.write(pix.tobytes("png"))
    print(f"{name}: {pix.width}x{pix.height}")
crop(181, 105, 240, 10, "q2-p181-ayat-nisa-mujadala")   # les deux fragments coraniques
crop(178, 648, 816, 8, "q2-p178-tarjama")                # notice biographique
crop(182, 200, 300, 12, "q2-p182-fin-malade")            # fin de la fatwa sur le malade
crop(177, 160, 305, 10, "q2-p177-intro-ziyad")           # hadith d'intro Ziyād b. Jubayr
print("DONE")
