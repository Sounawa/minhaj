#!/usr/bin/env python3
"""R596 — OCR 300 dpi p.96-99 de ulum-hadith-1-thanawi.pdf (chaîne R595/B → R596/D).
Leçon 19 ulum-hadith-tanawi-1 (pdf-mut23h2q-130, الحديث المقلوب):
bornes p.95-? (sondage : bannière p.95 confirmée OCR R595 ; objectifs pdf-131 p.>95).
Objectif : trancher la borne supérieure (bannière leçon 20 / الإعداد القبلي L19).
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
    img = f"/tmp/uh1-r596-p{pno}.png"
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

pages = [int(x) for x in sys.argv[1:]] or [96, 97, 98, 99]
doc = fitz.open(PDF)
for p in pages:
    t6 = ocr_page(doc, p, 6)
    t4 = ocr_page(doc, p, 4)
    print(f"===== p{p} (psm6) =====")
    print(t6[:1800])
    print(f"----- p{p} (psm4) -----")
    print(t4[:1200])
doc.close()
print(f"R596 OCR {pages} terminé")
