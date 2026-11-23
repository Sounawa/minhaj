#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom5-h6-17 : 2e vague — cartouche p.95 (triangulation pixel du numéro
# contre p.90 = ١٥ et p.100 = ١٧?) + recadrages serrés pour re-scrutins VLM :
# matn-l1 (يكذبه), kayy (أحسن تقويم), ligne mystère p.98 y1200-1380,
# yashwush @2400, tête du tableau en couleur, تتمة délimiteurs.
import subprocess, os
import numpy as np
from PIL import Image, ImageOps

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"   # copie survivante
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

# ---------- A. triangulation pixel du numéro de cartouche ----------
# couche bleue @1200 : texte blanc → noir. Zone numéro sous الدرس (Z2-52 : x8550-8850).
def cart_bleu(name, page, y0, y1):
    png = crop_pdf(name, page, y0, y1, 1200, color=True)
    a = np.array(Image.open(png).convert("RGB"))
    R, G, B = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
    mask_text = (R > 160) & (G > 150)   # texte blanc → noir
    out = np.where(mask_text, 0, 255).astype(np.uint8)
    p = f"{DIR}/zoom/{name}-bleu.png"
    Image.fromarray(out).save(p)
    return p

for nm, pg in (("z5-cart-bleu-p95", 95), ("z5-cart-bleu-p90", 90), ("z5-cart-bleu-p100", 100)):
    p = cart_bleu(nm, pg, 300, 1100)
    with open(f"{DIR}/zoom/{nm}-psm6.txt", "w") as fh:
        fh.write(ocr(p, 6))
    print(nm, "OK")

# comparaison pixel : découpe fine de la zone numéro (bande y du numéro) et diff
def zone_num(img_path, tag):
    im = Image.open(img_path).convert("L")
    a = np.array(im)
    ink = (a < 120)
    rows = ink.sum(axis=1)
    # bande occupée du bas du cartouche (le numéro est sous الدرس, moitié droite)
    H, W = a.shape
    right = ink[:, int(0.60 * W):int(0.95 * W)]
    rows_r = right.sum(axis=1)
    # affiche le profil horizontal sommé par colonnes de la moitié droite
    cols = right[int(0.30 * H):int(0.75 * H), :].sum(axis=0)
    nz = np.nonzero(cols > 0)[0]
    if len(nz):
        x0, x1 = nz.min(), nz.max()
        crop = Image.fromarray(((1 - right.astype(np.uint8)) * 255)[int(0.30*H):int(0.75*H), max(0,x0-30):x1+30])
        crop.save(f"{DIR}/zoom/{tag}-numzone.png")
        print(f"{tag}: zone numéro x[{x0}-{x1}] sur W={W}")
    return

zone_num(f"{DIR}/zoom/z5-cart-bleu-p95-bleu.png", "z5-cart-p95")
zone_num(f"{DIR}/zoom/z5-cart-bleu-p90-bleu.png", "z5-cart-p90")
zone_num(f"{DIR}/zoom/z5-cart-bleu-p100-bleu.png", "z5-cart-p100")

# ---------- B. recadrages serrés pour re-scrutins ----------
Z = [
    ("z5-p95-matn-l1",      95, 4840, 5075, 2400, False),  # pour VLM redo يكذبه
    ("z5-p97-ahsana",       97, 2905, 3150, 3600, False),  # ثم أحسن ... خلقه وسخر
    ("z5-p98-myst",         98, 1180, 1400, 2400, False),  # ligne mystère (couleur claire ?)
    ("z5-p98-myst-col",     98, 1180, 1400, 1200, True),   # idem en couleur
    ("z5-p99-yash",         99, 1860, 2320, 2400, False),  # يشوش القلب + تضييع
    ("z5-p98-thead",        98, 5140, 5370, 1200, True),   # tête du tableau (couleur)
    ("z5-p95-tatimma",      95,  300, 1100, 1200, True),   # zone تتمة du cartouche
    ("z5-p98-raqaba2",      98, 2860, 3100, 3600, False),  # رقابة الله وشهوده (3600)
    ("z5-p97-item5-mil",    97, 4110, 4460, 3600, False),  # بالإتلاف أو الإيذاء (3600)
]
for name, page, y0, y1, dpi, color in Z:
    png = crop_pdf(name, page, y0, y1, dpi, color=color)
    for psm in (6, 7):
        with open(f"{DIR}/zoom/{name}-psm{psm}.txt", "w") as fh:
            fh.write(ocr(png, psm))
    print(f"{name}: OK ({os.path.getsize(png)//1024} Ko)")

# ligne mystère : binarisation douce si couleur claire
img = Image.open(f"{DIR}/zoom/z5-p98-myst-col.png").convert("RGB")
g = ImageOps.autocontrast(img.convert("L"))
for t in (130, 160, 190):
    bw = g.point(lambda v, th=t: 0 if v < th else 255)
    out = f"{DIR}/zoom/z5-p98-myst-col-bw{t}.png"
    bw.save(out)
    with open(f"{DIR}/zoom/z5-p98-myst-col-bw{t}-psm6.txt", "w") as fh:
        fh.write(ocr(out, 6))
print("myst binarisation OK")

# tête du tableau : binarisation
img = Image.open(f"{DIR}/zoom/z5-p98-thead.png").convert("RGB")
g = ImageOps.autocontrast(img.convert("L"))
for t in (120, 150, 180):
    bw = g.point(lambda v, th=t: 0 if v < th else 255)
    out = f"{DIR}/zoom/z5-p98-thead-bw{t}.png"
    bw.save(out)
    with open(f"{DIR}/zoom/z5-p98-thead-bw{t}-psm6.txt", "w") as fh:
        fh.write(ocr(out, 6))
print("thead binarisation OK")
print("OK zoom5-h6-17")
