#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-19 : recadrages couleur @3600 pour scrutins VLM (points douteux).
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"

def crop_pdf(name, page, y0, y1, dpi, color=True, fx0=0.0, fx1=1.0):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        X0, X1 = int(W * fx0), int(W * fx1)
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", str(X0), "-y", str(int(y0 * f)), "-W", str(X1 - X0), "-H", str(int((y1 - y0) * f)),
                PDF, out]
        subprocess.run(args, check=True)
    print(name, os.path.getsize(out + ".png") // 1024, "Ko")

# p105 : cartouche @1200 couleur ; matn l1-l2 (يرويه + قال: + إن الله كتب) ; l6 (سيئةً واحدةً + réf)
crop_pdf("z1-p105-cart-vlm", 105, 300, 2000, 1200)
crop_pdf("z3-p105-matn12-vlm", 105, 4600, 5080, 3600)
crop_pdf("z3-p105-matn6-vlm", 105, 5740, 5995, 3600)
# p106 : glose همّ ; tahlil lignes همّ العبد
crop_pdf("z3-p106-hamm-vlm", 106, 2830, 3080, 3600)
crop_pdf("z3-p106-tahlil-vlm", 106, 5180, 5670, 3600)
# p107 : lataf l2 (عنده?) ; item1 l1-l2 (بالقلب.) ; item1 l6 (شاكراً لله) ; item2 l4 (وإيقاعها)
crop_pdf("z3-p107-lataf-vlm", 107, 1915, 2140, 3600)
crop_pdf("z3-p107-item1a-vlm", 107, 3300, 3780, 3600)
crop_pdf("z3-p107-item1c-vlm", 107, 4490, 4710, 3600)
crop_pdf("z3-p107-item2-vlm", 107, 5770, 5950, 3600)
# p108 : item3 l2 (استُصلحت?) ; item4 l3-l4 (آية+réf) ; item4 l5 (يحصره) ; item5 l4-l5 (وللأول ألفاً) ; yust l3-l4
crop_pdf("z3-p108-item3-vlm", 108, 930, 1130, 3600)
crop_pdf("z3-p108-item4-vlm", 108, 2165, 2660, 3600)
crop_pdf("z3-p108-item4b-vlm", 108, 2650, 2860, 3600)
crop_pdf("z3-p108-item5-vlm", 108, 3670, 4125, 3600)
crop_pdf("z3-p108-yust-vlm", 108, 5280, 5800, 3600)
# p109 : istithmar L3/L5/L7/L9 (يعمل/بحقه/بنيته/هي نيته) ; réf chiffres
crop_pdf("z3-p109-ist1-vlm", 109, 3540, 3760, 3600)
crop_pdf("z3-p109-ist2-vlm", 109, 4300, 4510, 3600)
crop_pdf("z3-p109-ist4-vlm", 109, 4900, 5065, 3600)
print("OK zoom3-h6-19")
