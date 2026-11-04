# -*- coding: utf-8 -*-
"""R570 — ciblage search_for (texte interne LOGIQUE) + crops 1152/1440 dpi."""
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)

def find(pno, needle):
    page = doc[pno - 1]
    rects = page.search_for(needle)
    print(f"p.{pno} '{needle}': {len(rects)} hits → {[str(r) for r in rects]}")
    return page, rects

def save(page, rect, pad_up, pad_dn, zoom, name):
    clip = fitz.Rect(max(0, rect.x0 - 120), max(0, rect.y0 - pad_up),
                     min(page.rect.x1, rect.x1 + 120), min(page.rect.y1, rect.y1 + pad_dn))
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    with open(f"{OUT}/{name}.png", "wb") as f:
        f.write(pix.tobytes("png"))
    print(f"  {name}: {pix.width}x{pix.height} @y{rect.y0:.0f}-{rect.y1:.0f}pt")

# 1) p.165 : citation ʿĀʾiša (ligne «وأيكم ملك لنفسه من رسول الله»)
p, rs = find(165, "لنفسه")
for i, r in enumerate(rs):
    save(p, r, 45, 20, 16, f"q4-p165-aicha-{i}")
# 2) p.166 : réaction de l'époux («وقال: لسنا/أنا مثل رسول الله...»)
p, rs = find(166, "يحل")
for i, r in enumerate(rs):
    save(p, r, 30, 30, 12, f"q4-p166-yahul-{i}")
# 3) p.166 : hadith Ḥamza (chaîne + question + réponse)
p, rs = find(166, "حمزة")
for i, r in enumerate(rs):
    save(p, r, 10, 110, 8, f"q4-p166-hamza-{i}")
p, rs = find(166, "شئت")
for i, r in enumerate(rs):
    save(p, r, 28, 18, 16, f"q4-p166-shit-{i}")
# 4) p.169 : āya (fragment après لقوله تعالى)
p, rs = find(169, "تعالى")
for i, r in enumerate(rs):
    save(p, r, 8, 70, 12, f"q4-p169-taala-{i}")
# 5) p.170 : fin du passage 829
p, rs = find(170, "سمعت")
for i, r in enumerate(rs):
    save(p, r, 45, 15, 16, f"q4-p170-samic-{i}")
print("DONE")
