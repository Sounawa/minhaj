#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-17 : zooms ciblés 2400/3600 dpi pp.95-99 de L17 «الأخوة الإسلامية» (تتمة)
# + cartouche p.95 : extraction couche bleue (texte blanc sur fond bleu → noir/blanc),
# positions tirées du profil d'encre ink-h6-17.py.
import subprocess, os
import numpy as np
from PIL import Image, ImageOps

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
    print(f"{name}: OK")

# ---------- A. zones grises 2400/3600 ----------
ZOOMS = [
    # (nom, page, y0, y1, dpi)
    ("z2-p95-tamhid-l2",  95, 3266, 3499, 2400),  # يحب القيام بها خصوصا
    ("z2-p95-matn-l2",    95, 5080, 5310, 2400),  # هاهنا ويشير إلى صدره ثلاث مرات بحسب
    ("z2-p95-matn-l3",    95, 5311, 5595, 2400),  # أخاه المسلم كل المسلم + رواه مسلم
    ("z2-p95-foot",       95, 5560, 6300, 2400),  # note de bas de page éventuelle
    ("z2-p96-gloses",     96, 1960, 2560, 2400),  # الشرح : 2 gloses ?
    ("z2-p96-item1-l2",   96, 4950, 5230, 2400),  # أو عرضه أو ماله لأن ذلك ينافي
    ("z2-p96-foot",       96, 5720, 5960, 1200),  # bande mystère bas de p.96
    ("z2-p97-kayy",       97, 2880, 3160, 3600),  # لم يحقره إذ خلقه ورزقه... وسخر له
    ("z2-p97-ahzar",      97, 3392, 3650, 2400),  # وأرسل / إليه محمدا فمن حقر مسلما
    ("z2-p97-aya-ref",    97, 2180, 2440, 3600),  # الصادقين + [التوبة: NNN]
    ("z2-p97-thani",      97, 5820, 6060, 2400),  # كما قال ﷺ التقوى ها هنا ويشير
    ("z2-p98-l3",         98, 1130, 1400, 2400),  # ligne après رؤية الله تعالى
    ("z2-p98-yustafad1",  98, 1720, 1990, 2400),  # حرمة تحقير الناس... الكافي
    ("z2-p98-taqwim3",   98, 4180, 4420, 2400),  # ماذا أستفيد... التقوى هاهنا
    ("z2-p99-ahwal",      99, 2840, 3100, 3600),  # وقوة في الأحوال / الأهوال
    ("z2-p99-salaf1",     99, 3080, 3340, 2400),  # فقد قال السلف استكثروا من الإخوان
    ("z2-p99-salaf2",     99, 3490, 3760, 2400),  # شفاعة فلعلك... + [إحياء 2/171]
    ("z2-p99-khattata",   99, 4160, 4420, 2400),  # أستجمع في خطاطة
    ("z2-p99-sadr",       99, 2340, 2600, 2400),  # القلب ويصد عن العبادة + تحصنا
    ("z2-p99-top",        99,  600, 1300, 1200),  # heading الاستثمار ?
]
for name, page, y0, y1, dpi in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    ocr_save(png, name, psms=(6,) if dpi == 1200 else (6, 7))

# ---------- B. zones colorées : rendu couleur 1200 + binarisation PIL ----------
def binarize_variants(png_in, base, thresholds=(120, 160, 190)):
    img = Image.open(png_in).convert("RGB")
    g = ImageOps.autocontrast(img.convert("L"))
    for t in thresholds:
        bw = g.point(lambda v, th=t: 0 if v < th else 255)
        out = f"{DIR}/zoom/{base}-bw{t}.png"
        bw.save(out)
        with open(f"{DIR}/zoom/{base}-bw{t}-psm6.txt", "w") as fh:
            fh.write(ocr(out, 6))
    print(f"{base}: binarisation ×{len(thresholds)}")

ZONES = [
    ("z2-p96-item1-col", 96, 4600, 4940),   # الظلم ligne 1 (bande colorée)
    ("z2-p98-table-col", 98, 5100, 6050),   # tableau استثمار
    ("z2-p95-cart-col",  95,  300, 2100),   # cartouche + titre (couleur)
]
for base, page, y0, y1 in ZONES:
    png = crop_pdf(base, page, y0, y1, 1200, color=True)
    binarize_variants(png, base)

# ---------- C. cartouche p.95 : couche bleue (texte blanc → noir sur blanc) ----------
col = Image.open(crop_pdf("z2-p95-cart-bleu-src", 95, 300, 2100, 1200, color=True)).convert("RGB")
a = np.array(col)
R, G, B = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
mask_text = (R > 160) & (G > 150)
out = np.where(mask_text, 0, 255).astype(np.uint8)
Image.fromarray(out).save(f"{DIR}/zoom/z2-p95-cartouche-bleu.png")
with open(f"{DIR}/zoom/z2-p95-cartouche-bleu-psm6.txt", "w") as fh:
    fh.write(ocr(f"{DIR}/zoom/z2-p95-cartouche-bleu.png", 6))
lum = (R + G + B) // 3
out2 = np.where(lum > 170, 0, 255).astype(np.uint8)
Image.fromarray(out2).save(f"{DIR}/zoom/z2-p95-cartouche-lum.png")
with open(f"{DIR}/zoom/z2-p95-cartouche-lum-psm6.txt", "w") as fh:
    fh.write(ocr(f"{DIR}/zoom/z2-p95-cartouche-lum.png", 6))
# moitiés du lum pour psm 7/11
cart = Image.open(f"{DIR}/zoom/z2-p95-cartouche-lum.png")
w, h = cart.size
for half, box in [("R", (w // 2, 0, w, h)), ("L", (0, 0, w // 2, h))]:
    out3 = f"{DIR}/zoom/z2-p95-cart-{half}.png"
    cart.crop(box).save(out3)
    for psm in (7, 11, 6):
        with open(f"{DIR}/zoom/z2-p95-cart-{half}-psm{psm}.txt", "w") as fh:
            fh.write(ocr(out3, psm))
print("cartouche bleu OK")
print("OK zoom2-h6-17")
