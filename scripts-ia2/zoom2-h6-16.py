#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-16 : zooms ciblés 2400/3600 dpi pp.90-94 de L16 «الأخوة الإسلامية» (1)
# + cartouche p.90 : extraction couche bleue (texte blanc sur fond bleu → noir/blanc).
import subprocess, os
import numpy as np
from PIL import Image

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

ZOOMS = [
    # (nom, page, y0, y1, dpi)
    ("z2-p90-matn",        90, 3750, 5400, 2400),  # أسئلة + encadré hadith complet
    ("z2-p91-gloses",      91,  260, 1550, 2400),  # الشرح : gloses ×3
    ("z2-p91-istikhlas",   91, 1450, 3150, 2400),  # استخلاص + يشتمل + أولاً heading
    ("z2-p91-vers",        91, 3400, 4050, 2400),  # قال الله تعالى + verset + réf
    ("z2-p91-vers3600",    91, 3550, 3980, 3600),  # verset ligne unique très haute rés
    ("z2-p91-mana",        91, 4300, 5750, 2400),  # ومعنى قوله ﷺ وكونوا عباد الله إخوانا
    ("z2-p92-thani",       92, 2050, 2500, 2400),  # ثانيا heading + ligne d'intro
    ("z2-p92-item1",       92, 2380, 2980, 2400),  # item 1 الالتزام كل ما تتحقق
    ("z2-p92-item2",       92, 2900, 3520, 2400),  # item 2 اجتناب + جاء عن النبي
    ("z2-p92-hasad",       92, 3480, 4280, 2400),  # الحسد + حديث إياكم والحسد
    ("z2-p92-ghibta",      92, 4150, 4980, 2400),  # الحسد بمعنى الغبطة + لا حسد إلا في اثنين
    ("z2-p92-najsh",       92, 4880, 5950, 2400),  # النجش + من غشنا
    ("z2-p93-tabaghd",     93,  240,  980, 2400),  # التباغض
    ("z2-p93-tadabur",     93,  880, 1980, 2400),  # التدابر + لا يحل لمسلم
    ("z2-p93-bay",         93, 1900, 2820, 2400),  # البيع على بيع أخيه + الطبراني
    ("z2-p93-yustafad",    93, 2720, 3980, 2400),  # مما يستفاد ×3
    ("z2-p93-taqwim",      93, 3900, 6650, 2400),  # التقويم + Q1-Q3 + cas 1
    ("z2-p94-case2",       94,  220,  980, 2400),  # cas 2 اتفق شخص
    ("z2-p94-verses",      94,  800, 2300, 2400),  # الحجرات 10-11 + référence
    ("z2-p94-tamal",       94, 2200, 3500, 2400),  # أتأمل ×2
    ("z2-p94-idad",        94, 3350, 5100, 2400),  # الإعداد القبلي ×2
]

for name, page, y0, y1, dpi in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    with open(f"{DIR}/zoom/{name}-psm6.txt", "w") as fh:
        fh.write(ocr(png, 6))
    print(f"{name}: {os.path.getsize(png)//1024} Ko → psm6 {os.path.getsize(f'{DIR}/zoom/{name}-psm6.txt')} o")

# --- cartouche p.90 : couche bleue (texte blanc → noir sur blanc) ---
col = Image.open(crop_pdf("z16-p90-cartouche-col", 90, 450, 1050, 1200, color=True)).convert("RGB")
a = np.array(col)
R, G, B = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
# texte blanc/or clair : R et G élevés ; fond bleu : R,G faibles
mask_text = (R > 160) & (G > 150)
out = np.where(mask_text, 0, 255).astype(np.uint8)
Image.fromarray(out).save(f"{DIR}/zoom/z2-p90-cartouche-bleu.png")
with open(f"{DIR}/zoom/z2-p90-cartouche-bleu-psm6.txt", "w") as fh:
    fh.write(ocr(f"{DIR}/zoom/z2-p90-cartouche-bleu.png", 6))
# variante : binarisation douce (texte = luminance haute) pour comparaison
lum = (R + G + B) // 3
out2 = np.where(lum > 170, 0, 255).astype(np.uint8)
Image.fromarray(out2).save(f"{DIR}/zoom/z2-p90-cartouche-lum.png")
with open(f"{DIR}/zoom/z2-p90-cartouche-lum-psm6.txt", "w") as fh:
    fh.write(ocr(f"{DIR}/zoom/z2-p90-cartouche-lum.png", 6))
print("cartouche bleu OK")
print("OK zoom2-h6-16")
