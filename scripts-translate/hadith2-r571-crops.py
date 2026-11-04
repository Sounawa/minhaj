# -*- coding: utf-8 -*-
"""R571 — pass 2 : crops des crochets manquants + matns à trancher."""
import subprocess, os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
TESS = "scripts-translate/tessdata" if os.path.isdir("scripts-translate/tessdata") else "/usr/share/tesseract-ocr/4.00/tessdata"
doc = fitz.open(PDF)

def crop_ocr(pno, y0px, y1px, tag, dpi=900, x0=20, x1=490, psm="7"):
    """y0/y1 en pixels 300 dpi → converti en points."""
    page = doc[pno - 1]
    clip = fitz.Rect(x0, y0px * 72 / 300, x1, y1px * 72 / 300)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72), clip=clip)
    png = f"{OUT}/x-{tag}.png"
    pix.save(png)
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", psm,
                        "--tessdata-dir", TESS, "-c", "preserve_interword_spaces=1"],
                       capture_output=True, text=True)
    txt = " ".join(r.stdout.split())
    print(f"[{tag}] {txt!r}")
    return txt

# crochets manquants
crop_ocr(172, 560, 930, "818-tail-821", dpi=1200)          # fin hadith 1 (crochet 818?) + début 821
crop_ocr(172, 1500, 1900, "826-zone", dpi=1200)            # fin hadith معاوية (crochet 826)
crop_ocr(173, 2200, 2520, "wasum-num", dpi=1200)           # «وصم يوما» + son numéro
crop_ocr(174, 2620, 3060, "saad-num", dpi=1200)            # سعد+عبد الله يحتجمان + 822?
crop_ocr(176, 840, 1720, "malik-824", dpi=900, psm="6")    # citation مالك + 824

# matns à re-vérifier en gros
crop_ocr(172, 250, 570, "818-head", dpi=900, psm="6")      # début hadith 818 (chaîne + matn)
crop_ocr(175, 1060, 1600, "aicha-matn", dpi=900, psm="6")  # matn عائشة complet
print("DONE")
