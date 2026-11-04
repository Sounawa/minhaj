# -*- coding: utf-8 -*-
"""R573 — hadith-2es pdf-28 (leçon 27, القضاء والفدية في الصيام, p.184-191).
OCR tesseract ara 300 dpi ×8 pages + TSV (localisation lignes à suspect
numérique : الموطأ, 3 chiffres, سورة/الآية) — tranchage ensuite à l'image."""
import subprocess, os, re
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r573"
os.makedirs(OUT, exist_ok=True)
TESS = "scripts-translate/tessdata" if os.path.isdir("scripts-translate/tessdata") else "/usr/share/tesseract-ocr/4.00/tessdata"
doc = fitz.open(PDF)
PAGES = list(range(184, 192))

def ocr(png, psm="3"):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", psm,
                        "--tessdata-dir", TESS, "-c", "preserve_interword_spaces=1"],
                       capture_output=True, text=True)
    return r.stdout

info = {}
for pno in PAGES:
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
    png = f"{OUT}/p{pno}-300.png"
    pix.save(png)
    txt = ocr(png)
    open(f"{OUT}/p{pno}-ocr.txt", "w").write(txt)
    tsv = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "3",
                          "--tessdata-dir", TESS, "tsv"], capture_output=True, text=True).stdout
    lines = {}
    for row in tsv.splitlines()[1:]:
        c = row.split("\t")
        if len(c) < 12 or not c[11].strip():
            continue
        key = (c[2], c[3], c[4])
        top = int(c[7]); h = int(c[9])
        e = lines.setdefault(key, {"top": top, "bot": top + h, "words": []})
        e["top"] = min(e["top"], top); e["bot"] = max(e["bot"], top + h)
        e["words"].append(c[11])
    info[pno] = list(lines.values())
    print(f"p{pno}: {len(txt)} car OCR, {len(lines)} lignes TSV")

print("\n=== LIGNES SUSPECTES (numériques/āya/Muwaṭṭaʾ) ===")
for pno, ls in info.items():
    for i, e in enumerate(ls):
        joined = " ".join(e["words"])
        if (re.search(r"[0-9\u0660-\u0669]{2,}", joined) or "الموط" in joined
                or "سورة" in joined or "الآية" in joined or "الآ" in joined):
            print(f"p{pno} L{i} y={e['top']}-{e['bot']}: {joined[:110]!r}")

print("\nDONE — rendus 300 dpi dans", OUT)
