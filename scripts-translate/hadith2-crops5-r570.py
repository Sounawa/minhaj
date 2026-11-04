# -*- coding: utf-8 -*-
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
doc = fitz.open(PDF)
page = doc[168]  # p.169
pix = page.get_pixmap(matrix=fitz.Matrix(16, 16), clip=fitz.Rect(80, 404, 520, 460))
with open("/home/z/my-project/tr-tmp/qa-crops-r570/q5-p169-aya-line.png", "wb") as f:
    f.write(pix.tobytes("png"))
print(f"q5-p169-aya-line: {pix.width}x{pix.height}")
