#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom4-h6-17 : derniers recadrages fins (bandes unitaires) L17 :
# p97 ligne «عليه السلام إذا بدأ» + amorce item 5 ; p98 suite ثانياً lignes 2-3
# + item رقابة seul ; p98 tableau complet pour VLM ; p97 ligne بحسب امرئ + تحذير.
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(f"{DIR}/zoom", exist_ok=True)

def crop_pdf(name, page, y0, y1, dpi, color=False, fx0=0.0, fx1=1.0):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        X0, X1 = int(W * fx0), int(W * fx1)
        Y0, Y1 = int(y0 * f), int(y1 * f)
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", str(X0), "-y", str(Y0), "-W", str(X1 - X0), "-H", str(Y1 - Y0),
                PDF, out]
        if not color:
            args.insert(-2, "-gray")
        subprocess.run(args, check=True)
    return out + ".png"

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return r.stdout

def ocr_save(png, name, psms=(6, 7)):
    for psm in psms:
        with open(f"{DIR}/zoom/{name}-psm{psm}.txt", "w") as fh:
            fh.write(ocr(png, psm))
    print(f"{name}: OK ({os.path.getsize(png)//1024} Ko)")

ZOOMS = [
    ("z4-p97-salam",     97, 3930, 4100, 2400, (7, 6)),   # عليه السلام إذا بدأ.
    ("z4-p97-item5-l1",  97, 4100, 4480, 2400, (6, 7)),   # 5- التعرض أو التسبب...
    ("z4-p98-taql-l23",  98,  920, 1420, 2400, (6, 7)),   # الله تعالى وخشيته... + ligne 3 mystère
    ("z4-p98-raqaba",    98, 2860, 3100, 2400, (6, 7)),   # رقابة الله وشهوده... (une ligne)
    ("z4-p97-bahasab",   97, 2700, 2925, 2400, (6, 7)),   # بحسب امرئ... + تحذير/تحدير عظيم
    ("z4-p98-table-full",98, 5050, 5960, 1200, (6,)),      # tableau complet (gris, pour OCR+VLM)
]
for name, page, y0, y1, dpi, psms in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    ocr_save(png, name, psms)

# tableau en couleur @1200 (pour VLM — inversion texte clair/fond coloré)
png = crop_pdf("z4-p98-table-vlm", 98, 5050, 5960, 1200, color=True)
print("tableau couleur OK:", os.path.getsize(png)//1024, "Ko")

# p95 cartouche entier @1200 couleur (pour VLM numéro)
png = crop_pdf("z4-p95-cart-vlm", 95, 300, 2150, 1200, color=True)
print("cartouche couleur OK:", os.path.getsize(png)//1024, "Ko")

# p99 yashwush @3600 (mots يشوش/تضييع — pour VLM)
png = crop_pdf("z4-p99-yash-vlm", 99, 1860, 2320, 3600)
print("yashwush 3600 OK:", os.path.getsize(png)//1024, "Ko")

# p97 kayy bloc 2 lignes @3600 (لم يحقره إذ خلقه... — pour VLM)
png = crop_pdf("z4-p97-kayy-vlm", 97, 2700, 3160, 3600)
print("kayy 3600 OK:", os.path.getsize(png)//1024, "Ko")

# p98 taql lignes @3600 (pour VLM)
png = crop_pdf("z4-p98-taql-vlm", 98, 640, 1420, 3600)
print("taql 3600 OK:", os.path.getsize(png)//1024, "Ko")

# p95 matn-l1 @3600 (ولا يكذبه — pour VLM)
png = crop_pdf("z4-p95-matn-vlm", 95, 4830, 5090, 3600)
print("matn 3600 OK:", os.path.getsize(png)//1024, "Ko")

# p99 ahwal @3600 (الأحوال/الأهوال — pour VLM)
png = crop_pdf("z4-p99-ahwal-vlm", 99, 2600, 2830, 3600)
print("ahwal 3600 OK:", os.path.getsize(png)//1024, "Ko")
print("OK zoom4-h6-17")
