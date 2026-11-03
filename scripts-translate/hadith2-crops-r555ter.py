# -*- coding: utf-8 -*-
"""Minhāj — R555 ter : zones de suivi (isnāds, lexies, objectifs, bio, renvoi 45)."""
import fitz, os
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r555"
doc = fitz.open(PDF)

def zone(pno, rect, dpi):
    page = doc[pno - 1]
    pm = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(*rect))
    f = f"{OUT}/_z.png"
    pm.save(f)
    return Image.open(f)

# composite 1 : zones matn 500 dpi
C1 = [(79, (40, 140, 600, 370), 500), (80, (40, 158, 600, 218), 500),
      (80, (40, 340, 600, 510), 500), (84, (40, 200, 600, 320), 500),
      (84, (40, 420, 600, 550), 500)]
imgs = [zone(*t) for t in C1]
tw = 1700
sc = tw / max(i.width for i in imgs)
imgs = [i.resize((int(i.width * sc), int(i.height * sc)), Image.LANCZOS) for i in imgs]
H = sum(i.height + 12 for i in imgs)
comp = Image.new("RGB", (tw, H), "white")
y = 0
for i in imgs:
    comp.paste(i, (0, y)); y += i.height + 12
comp.save(f"{OUT}/composite-suivi-1.png")
print(f"suivi-1 : {tw}x{H}")

# composite 2 : lexies
C2 = [(81, (40, 52, 600, 140), 500), (83, (40, 380, 600, 465), 500),
      (83, (40, 500, 600, 570), 500), (83, (40, 635, 600, 740), 500),
      (81, (330, 460, 600, 510), 900), (82, (40, 136, 600, 208), 600),
      (82, (200, 592, 520, 655), 900)]
imgs = [zone(*t) for t in C2]
tw = 1700
sc = tw / max(i.width for i in imgs)
imgs = [i.resize((int(i.width * sc), int(i.height * sc)), Image.LANCZOS) for i in imgs]
H = sum(i.height + 12 for i in imgs)
comp = Image.new("RGB", (tw, H), "white")
y = 0
for i in imgs:
    comp.paste(i, (0, y)); y += i.height + 12
comp.save(f"{OUT}/composite-suivi-2.png")
print(f"suivi-2 : {tw}x{H}")
os.remove(f"{OUT}/_z.png")
