#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-20 : recadrages couleur @3600 pour scrutins VLM L20.
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"

def crop_pdf(name, page, y0, y1, dpi, color=True):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", "0", "-y", str(int(y0 * f)), "-W", str(W), "-H", str(int((y1 - y0) * f)),
                PDF, out]
        subprocess.run(args, check=True)
    print(name, os.path.getsize(out + ".png") // 1024, "Ko")

crop_pdf("z3-p110-tam1-vlm", 110, 2990, 3270, 3600)   # premier mot du تمهيد (الولاية؟)
crop_pdf("z3-p110-tam3-vlm", 110, 3550, 4030, 3600)   # تنيله القرب...
crop_pdf("z3-p110-matn2-vlm", 110, 4640, 5350, 3600)  # ولا/وما يزال + افترضته + ... + [رواه البخاري]
crop_pdf("z3-p111-aya-vlm", 111, 4650, 5400, 3600)    # آية يونس box + réf
crop_pdf("z3-p112-umaref-vlm", 112, 1290, 1670, 3600) # ثم تلا... + refs
crop_pdf("z3-p112-thalitha-vlm", 112, 5380, 6130, 3600) # كناية/كفاية عن قربه
crop_pdf("z3-p112-wasail-vlm", 112, 3755, 3990, 3600) # القدر الواجب من التزكية؟
crop_pdf("z3-p113-maida-vlm", 113, 890, 1620, 3600)   # آية المائدة box + refs
crop_pdf("z3-p113-yust3-vlm", 113, 3830, 4340, 3600)  # يستفاد item 3
crop_pdf("z3-p114-aya1-vlm", 114, 1120, 1930, 3600)   # آية البقرة + réf
print("OK zoom3-h6-20")
