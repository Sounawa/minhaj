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
crop(181, 228, 330, 10, "q4-p181-ayat-zone")
crop(178, 670, 790, 12, "q4-p178-tarjama-zone")
crop(182, 155, 235, 14, "q4-p182-fin-zone")
print("DONE")
