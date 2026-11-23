#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-20 : recadrages ligne-à-ligne @2400 des points douteux L20 :
# تمهيد l1 (القرب غاية؟ تنيله؟), آية يونس box + réf, hadith عمر réf,
# ثالثاً (كناية/كفاية عن قربه؟), ثانياً القدر الواجب من التزكية؟, آية المائدة
# box + réf + فمن أحبهم, يستفاد item 3, تقويم exemple 3?, p114 آية 1 + réf.
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

def crop_pdf(name, page, y0, y1, dpi, color=False):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", "0", "-y", str(int(y0 * f)), "-W", str(W), "-H", str(int((y1 - y0) * f)),
                PDF, out]
        if not color:
            args.insert(-2, "-gray")
        subprocess.run(args, check=True)
    return out + ".png"

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return r.stdout

def zone(name, page, y0, y1, psms=(6, 7)):
    png = crop_pdf(name, page, y0, y1, 2400)
    for psm in psms:
        t = ocr(png, psm)
        with open(f"{DIR}/zoom/{name}-psm{psm}.txt", "w") as fh:
            fh.write(t)
        print(f"=== {name} psm{psm} ===\n{t}")

# p110 : تمهيد l1 (premier mot) + questions (تنيله؟)
zone("z2-p110-tam-l1", 110, 3000, 3260)     # القربُ غايةٌ يرجو العبد...
zone("z2-p110-tam-l3", 110, 3550, 4030)     # فما هي العبادة التي تنيله القرب...؟
# p111 : آية يونس (boîte) + réf
zone("z2-p111-aya", 111, 4680, 5400)        # box آية يونس + [يونس: ...]
# p112 : réf hadith عمر + ثالثاً (كناية/كفاية)
zone("z2-p112-umaref", 112, 1300, 1660)     # ثم تلا... [يونس: 62]». [سنن أبي داود ...]
zone("z2-p112-thalitha", 112, 5390, 6120)   # دل قوله حتى أحبه... كناية/كفاية عن قربه
# p112 : القدر الواجب من التزكية ؟
zone("z2-p112-wasail", 112, 3750, 4000)     # ووسائل التقرب... لتحقيق القدر الواجب...
# p113 : آية المائدة box + فمن أحبهم
zone("z2-p113-maida", 113, 900, 1620)       # box آية المائدة 55-56 + فمن أحبهم...
# p113 : يستفاد item 3 + تقويم zone basse
zone("z2-p113-yust3", 113, 3830, 4340)      # item 3 (ودوام مودتهم؟)
zone("z2-p113-taqw3", 113, 5350, 6140)      # item 3 + exemples (3e ?)
# p114 : آية 1 + réf + l2
zone("z2-p114-aya1", 114, 1120, 1920)       # قال الله تعالى: (...) [réf ?]
print("OK zoom2-h6-20")
