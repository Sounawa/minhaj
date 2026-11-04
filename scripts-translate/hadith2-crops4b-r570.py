# -*- coding: utf-8 -*-
"""R570 — ciblage par tokens INVERSÉS (couche visuelle) + crops."""
import fitz
PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)

def locate(pno, token):
    page = doc[pno - 1]
    words = page.get_text("words")
    hits = [w for w in words if token in w[4]]
    for w in hits:
        print(f"p.{pno} '{token}' ∈ '{w[4]}' rect=({w[0]:.1f},{w[1]:.1f},{w[2]:.1f},{w[3]:.1f})")
    return page, hits

def save(page, w, pad_up, pad_dn, zoom, name):
    clip = fitz.Rect(max(0, w[0] - 60), max(0, w[1] - pad_up),
                     min(page.rect.x1, w[2] + 160), min(page.rect.y1, w[3] + pad_dn))
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    with open(f"{OUT}/{name}.png", "wb") as f:
        f.write(pix.tobytes("png"))
    print(f"  → {name}: {pix.width}x{pix.height}")

locate(165, "هسفتل") or locate(165, "هتسفل")   # لنفسه inversé
p, hits = None, []
for tok in ("هسفتل", "هتسفل", "لتفسه"):
    p, hits = locate(165, tok)
    if hits: break
if hits: save(p, hits[0], 48, 22, 16, "q4-p165-aicha")
p, hits = None, []
for tok in ("لثم", "انس", "لوسر"):              # مثل / سنا inversés (p166)
    p, hits = locate(166, tok)
    if hits: break
if hits: save(p, hits[0], 34, 34, 12, "q4-p166-mithl")
p, hits = None, []
for tok in ("ةزمح", "ةمزح", "تئش"):              # حمزة / شئت inversés (p166)
    p, hits = locate(166, tok)
    if hits: break
if hits: save(p, hits[0], 8, 115, 8, "q4-p166-hamza")
p, hits = None, []
for tok in ("ىلاعت", "تالا"):                    # تعالى inversé (p169)
    p, hits = locate(169, tok)
    if hits: break
if hits: save(p, hits[0], 10, 72, 12, "q4-p169-taala")
p, hits = None, []
for tok in ("تعمس", "تامس"):                     # سمعت inversé (p170)
    p, hits = locate(170, tok)
    if hits: break
if hits: save(p, hits[0], 48, 18, 16, "q4-p170-samic")
print("DONE")
