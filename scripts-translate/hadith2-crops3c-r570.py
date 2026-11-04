# -*- coding: utf-8 -*-
import fitz
from PIL import Image
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)
def crop(pno, y0, y1, x0, x1, zoom, name, maxw=3600):
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(x0, y0, x1, y1))
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    if img.width > maxw:
        r = maxw / img.width
        img = img.resize((maxw, int(img.height * r)), Image.LANCZOS)
    img.save(f"{OUT}/{name}.png")
    print(f"{name}: {img.width}x{img.height}")
crop(166, 840, 1230, 80, 520, 6, "q3-p166-hamza")
crop(166, 1120, 1200, 80, 520, 16, "q3-p166-hamza-bracket")
crop(169, 400, 600, 80, 520, 6, "q3-p169-aya")
crop(169, 470, 560, 80, 520, 16, "q3-p169-aya-1152")
crop(170, 520, 660, 80, 520, 12, "q3-p170-829-864")
print("DONE")
