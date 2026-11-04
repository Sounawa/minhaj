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
crop(181, 300, 405, 12, "q3-p181-ayat-bas")          # les deux fragments Nisāʾ/Muǧādala
crop(178, 760, 830, 16, "q3-p178-tarjama-bas")        # notice en bas de page
crop(182, 225, 315, 14, "q3-p182-fin-malade-bas")     # phrase المرض المبيح
crop(177, 295, 470, 12, "q3-p177-ziyad")              # hadith Ziyād b. Jubayr
print("DONE")
