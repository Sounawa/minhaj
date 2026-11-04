# -*- coding: utf-8 -*-
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)
def crop(pno, y0, y1, zoom, name):
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(80, y0, 520, y1))
    with open(f"{OUT}/{name}.png", "wb") as f:
        f.write(pix.tobytes("png"))
    print(f"{name}: {pix.width}x{pix.height}")
crop(166, 330, 585, 5, "q4-p166-hamza-full")   # hadith Ḥamza complet
crop(170, 300, 392, 12, "q4-p170-fin-829")       # ligne «وذلك أحب ما سمعت...» + crochet
print("DONE")
