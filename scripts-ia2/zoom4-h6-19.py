#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom4-h6-19 : micro-recadrages 4800 dpi (couleur) pour les points
# résiduels : يرويه/عن ربه, » après كثيرة (écarté), الهمُّ, تفضُّل, همّه,
# تركها شاكراً لله, أزكى/أرقى + استُصلحت, تنعيم→تبشير, istithmar L3/L5/L7/L9.
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

# p105 : fin l1 (يرويه — confirmé psm7) ; début l2 (عن ربه — confirmé psm7) ;
# début l5 (pas de » après كثيرة — VLM) ; l6 (سيئةً واحدةً. puis » — VLM)
crop_pdf("z4-p105-l1end",   105, 4625, 4840, 4800, fx0=0.00, fx1=0.50)
crop_pdf("z4-p105-l2start", 105, 4825, 5050, 4800, fx0=0.55, fx1=1.00)
crop_pdf("z4-p105-l5start", 105, 5508, 5680, 3600, fx0=0.42, fx1=1.00)
crop_pdf("z4-p105-l6",      105, 5765, 5985, 3600)
# p106 : glose همّ (الهمُّ — VLM lettre à lettre) ; ligne مقدار تفضُّل الله (VLM) ;
# l3/l3b (وجعل همَّه بالسيئة — psm8 4800)
crop_pdf("z4-p106-hamm",     106, 2835, 3075, 4800)
crop_pdf("z4-p106-tafaddul", 106, 5190, 5400, 4800)
crop_pdf("z4-p106-l3",       106, 5425, 5665, 4800)
# p107 : ligne تركها [شاكراً لله] (VLM ×3 + tesseract ش ×2)
crop_pdf("z4-p107-tarak",  107, 4500, 4705, 4800)
# p108 : ligne أزكى أرض + استُصلحت (VLM ×2 épelé) ; ligne تبشير الفائزين (VLM ×2)
crop_pdf("z4-p108-azka",   108, 930, 1135, 4800)
crop_pdf("z4-p108-yust3",  108, 5285, 5510, 4800)
# p109 : istithmar L3 (ويعلم...بحقه) ; L5 (فهو بنيته) ; L7 (ولا يعلم...حقه) ; L9 (هي نيته + réf)
crop_pdf("z4-p109-istL3",  109, 3285, 3505, 4800)
crop_pdf("z4-p109-istL5",  109, 3793, 4010, 4800)
crop_pdf("z4-p109-istL7",  109, 4298, 4505, 4800)
crop_pdf("z4-p109-istL9",  109, 4810, 5010, 4800)
# --- zoom5 : micro-crops ciblés supplémentaires (ronde 4-5) ---
crop_pdf("z6-p106-hamm3",    106, 2835, 3070, 4800, fx0=0.55, fx1=0.92)
crop_pdf("z6-p106-l3b",      106, 5695, 5885, 4800, fx0=0.25, fx1=0.72)
crop_pdf("z7-p107-tarak3",   107, 4495, 4705, 4800, fx0=0.46, fx1=0.78)
crop_pdf("z7-p109-L3verb",   109, 3290, 3500, 4800, fx0=0.62, fx1=0.90)
crop_pdf("z7-p109-L3haq",    109, 3290, 3500, 4800, fx0=0.44, fx1=0.68)
crop_pdf("z7-p109-L7verb",   109, 4300, 4505, 4800, fx0=0.55, fx1=0.85)
crop_pdf("z7-p109-L9niyya",  109, 4810, 5010, 4800, fx0=0.46, fx1=0.74)
crop_pdf("z8-p109-L3haq2",   109, 3290, 3500, 4800, fx0=0.20, fx1=0.48)
crop_pdf("z8-p109-L9niyya",  109, 4810, 5010, 4800, fx0=0.66, fx1=0.96)
crop_pdf("z9-p106-isth-vlm", 106, 3480, 3820, 2400)
# --- ronde 3-4 : micro-crops z5 (4800, pleines largeurs de lignes) ---
crop_pdf("z5-p105-sayyi",   105, 5765, 5985, 4800, fx0=0.40, fx1=1.00)
crop_pdf("z5-p106-hamm2",   106, 2835, 3070, 4800, fx0=0.50, fx1=1.00)
crop_pdf("z5-p106-l3mid",   106, 5450, 5660, 4800, fx0=0.25, fx1=0.70)
crop_pdf("z5-p107-tarak",   107, 4500, 4705, 4800, fx0=0.15, fx1=0.65)
crop_pdf("z5-p109-L3tail",  109, 3285, 3505, 4800, fx0=0.05, fx1=0.55)
crop_pdf("z5-p109-L7tail",  109, 4295, 4505, 4800, fx0=0.10, fx1=0.60)
crop_pdf("z5-p109-L9mid",   109, 4810, 5010, 4800, fx0=0.30, fx1=0.85)
# bloc istithmar complet @2400 couleur (pour la carte des guillemets) et @1200 (VLM)
crop_pdf("z5-p109-istfull", 109, 2780, 5070, 2400)
crop_pdf("z6-p109-istfull", 109, 2780, 5070, 1200)
print("OK zoom4-h6-19")
