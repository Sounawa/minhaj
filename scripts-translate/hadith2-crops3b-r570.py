# -*- coding: utf-8 -*-
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)
def crop(pno, y0, y1, x0, x1, zoom, name, jpg=False):
    page = doc[pno - 1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    out = f"{OUT}/{name}.{'jpg' if jpg else 'png'}"
    pix.save(out, jpg_quality=80) if jpg else pix.save(out)
    print(f"{name}: {pix.width}x{pix.height}")
crop(166, 840, 1230, 80, 520, 6, "q3-p166-hamza-432", jpg=True)
crop(166, 1120, 1200, 80, 520, 16, "q3-p166-hamza-bracket")
crop(169, 400, 600, 80, 520, 6, "q3-p169-aya-432", jpg=True)
crop(169, 470, 560, 80, 520, 16, "q3-p169-aya-1152")
crop(170, 520, 660, 80, 520, 12, "q3-p170-829-864")
print("DONE")
