#!/usr/bin/env python3
"""R595 — OCR 300 dpi p.93-95 de ulum-hadith-1-thanawi.pdf (chaîne R594/C → R595/B).
Leçon 18 ulum-hadith-tanawi-1 (pdf-mut23h2q-129, الحديث الشاذ):
bornes p.91-? (sondage : الإعداد القبلي p.90 annonce le šāḏḏ ; bannière p.91 confirmée OCR).
Objectif : trancher la borne supérieure (bannière leçon 19 = الحديث المقلوب / الإعداد القبلي L18).
PDF = content/textbooks-src/ulum-hadith-1-thanawi.pdf — chaîne R578+ (zéro vision API)."""
import os, sys
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/r592-uh1"
os.makedirs(OUT, exist_ok=True)

def ocr_page(doc, pno, psm):
    tp = f"{OUT}/p{pno}-300.txt"
    if os.path.exists(tp):
        base = open(tp, encoding="utf-8").read()
    else:
        base = ""
    if f"[psm{psm}]" in base:
        return base
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=300)
    img = f"/tmp/uh1-r595-p{pno}.png"
    pix.save(img)
    os.system(f"TESSDATA_PREFIX={HOME}/scripts-translate/tessdata tesseract {img} {img}.out -l ara --psm {psm} 2>/dev/null")
    txt = open(f"{img}.out.txt", encoding="utf-8").read()
    os.remove(img); os.remove(f"{img}.out.txt")
    marker = f"\n[psm{psm}]\n"
    if base and f"[psm{psm}]" not in base:
        base = base + marker + txt
    else:
        base = txt + marker
    open(tp, "w", encoding="utf-8").write(base)
    return base

doc = fitz.open(PDF)
for p in (93, 94, 95):
    t6 = ocr_page(doc, p, 6)
    t4 = ocr_page(doc, p, 4)
    print(f"===== p{p} (psm6) =====")
    print(t6[:1800])
    print(f"----- p{p} (psm4) -----")
    print(t4[:1200])
doc.close()
print("R595 OCR p.93-95 terminé")
