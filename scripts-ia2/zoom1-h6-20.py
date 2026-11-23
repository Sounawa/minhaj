#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom1-h6-20 : recadrages blocs @2400 (gris) des sections de L20
# «العبادة وسيلة القرب والمحبة» pp.110-114 + OCR psm 6/7.
# Bandes calibrées par ink-h6-20.py (600 dpi).
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

# --- p110 ---
zone("z1-p110-tamhid", 110, 2990, 4110)     # تمهيد 3 lignes + questions
zone("z1-p110-matn",   110, 4400, 5370)     # matn 3-4 lignes + [رواه البخاري]
zone("z1-p110-tarjama",110, 5880, 6130)     # ترجمة الراوي (renvoi الدرس الرابع)
# --- p111 ---
zone("z1-p111-sharh",   111, 1250, 2000)    # الشرح + gloses ×3
zone("z1-p111-istikh",  111, 2370, 2900)    # استخلاص المضامين + items ×2
zone("z1-p111-tahlil1", 111, 3300, 4350)    # التحليل + قال العلماء + أولاً heading + l1
zone("z1-p111-aya",     111, 4650, 5400)    # آية يونس (boîte) + ref
zone("z1-p111-fiqh",    111, 5380, 6130)    # وفي هذا الحديث من الفقه + عمر hadith l1
# --- p112 ---
zone("z1-p112-umarend", 112, 650, 1660)     # fin hadith عمر + refs + ثانياً heading
zone("z1-p112-thania1", 112, 1750, 3760)    # دلّ قوله (citation) + أفضل ما يتقرب...
zone("z1-p112-thania2", 112, 3750, 5020)    # وسائل التقرب + الفرائض/النوافل + عبداً ربانياً
zone("z1-p112-thalitha",112, 5140, 6150)    # ثالثاً + دل قوله حتى أحبه + محبة الله لأوليائه
# --- p113 ---
zone("z1-p113-muqtaqa", 113, 650, 1600)     # وبمقتضى + آية المائدة (boîte) + فمن أحبهم
zone("z1-p113-rabian",  113, 1740, 2960)    # رابعاً + جزاء من عادى
zone("z1-p113-yustafad",113, 3000, 4330)    # مما يستفاد ×4
zone("z1-p113-taqwim",  113, 4760, 6140)    # تقويم ×3 + exemples
# --- p114 ---
zone("z1-p114-istithmar",114, 1090, 2700)   # الاستثمار + آيتان + questions ×2
zone("z1-p114-idad",    114, 3100, 5060)    # الإعداد القبلي + items + bullets
print("OK zoom1-h6-20")
