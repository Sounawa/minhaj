#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-18 : zooms complémentaires 2400 dpi (offsets corrigés par zoom2)
# + images VLM couleur 1200/2400 pour les zones rebelles — L18 pp.100-104.
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
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

# ---- A. zones grises 2400 (offsets corrigés) ----
ZOOMS = [
    # p.100 : عسى ligne + matn ponctuation
    ("z3-p100-tamhid-l3", 100, 3250, 3520, 2400),  # عسى أن ينال بها بغيته (bande y3291-3465)
    ("z3-p100-matn-awn2", 100, 4880, 5140, 2400),  # والله في عون العبد...أخيه + ponctuation
    # p.101 : intro l1 + رغب + zone mystère y2396-2866
    ("z3-p101-intro-l1", 101, 4080, 4330, 2400),   # مجموعة من الأعمال الفاضلة يليق للمسلم
    ("z3-p101-ragabba", 101, 5380, 5630, 2400),    # رغب النبي ﷺ في الإكثار من الإحسان إلى الناس
    # p.102 : آية البقرة + يعينه + آية الزمر
    ("z3-p102-aya-baqara", 102, 1395, 1660, 2400),  # وإن كان ذو عسرة... [البقرة: NNN]
    ("z3-p102-item4-l1", 102, 3355, 3580, 2400),   # 4- عون المسلم لأخيه بأن يعينه
    ("z3-p102-zumar-ref", 102, 4415, 4680, 2400),  # قل هل يستوي... [الزمر: N]
    # p.103 : حلقات + كل اجتماع + تسويفا
    ("z3-p103-halaq-l1", 103, 1570, 1810, 2400),   # هو: حلق العلم والتعليم
    ("z3-p103-kull-ijtima", 103, 1990, 2230, 2400),  # وكل اجتماع من أجل التلاوة والتدبر والتدارسة
    # p.104 : إعداد l1
    ("z3-p104-idad-l1", 104, 5640, 5900, 2400),    # أحفظ حديث الدرس الموالي وأبين سبب مضاعفة
]

for name, page, y0, y1, dpi in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    ocr_save(png, name)

# ---- B. images VLM couleur ----
VLMS = [
    # (nom, page, y0, y1, dpi)
    ("z3-p100-tamhid-vlm",   100, 3250, 3760, 2400),  # عسى أن ينال بها بغيته + question
    ("z3-p100-hadith-vlm",   100, 3760, 4720, 2400),  # الحديث header + sanad + matn l1-l2
    ("z3-p100-matn-awn-vlm", 100, 4700, 5400, 2400),  # سلك طريقا... عون أخيه »؟ + ستر
    ("z3-p101-gloses-vlm",   101, 1850, 2950, 1200),  # الشرح gloses + zone mystère y2396-2866
    ("z3-p101-intro-vlm",    101, 4030, 4360, 2400),  # intro l1 مجموعة من الأعمال الفاضلة
    ("z3-p101-ragabba-vlm",  101, 5360, 5660, 2400),  # رغب النبي ﷺ...
    ("z3-p102-saa-vlm",      102, 1140, 1420, 2400),  # أو ينظر إلى ساعة اليسر بتأجيل
    ("z3-p102-aya-vlm",      102, 1395, 1660, 2400),  # آية البقرة + ref chiffres
    ("z3-p102-item4-vlm",    102, 3340, 3590, 2400),  # بأن يعينه بما يمكن من المساعدة
    ("z3-p102-zumar-vlm",    102, 4400, 4700, 2400),  # آية الزمر + ref chiffres
    ("z3-p103-hafoof-vlm",   103, 3810, 4120, 2400),  # حفوف/حف الملائكة
    ("z3-p103-manas-vlm",    103, 4600, 4900, 2400),  # أن من أخر عمله X أو تفريطا
    ("z3-p104-table-vlm",    104, 2740, 3350, 1200),  # الجدول (تقويم 3)
    ("z3-p104-istithmar-vlm",104, 3330, 3820, 2400),  # استثمار : شخص يظن... فيستهين بـ
    ("z3-p104-aya-vlm",      104, 4300, 4980, 2400),  # آية + [الطور: N] + كيف أوفق
    ("z3-p104-idad-vlm",     104, 5620, 6120, 2400),  # الإعداد القبلي complet
]

for name, page, y0, y1, dpi in VLMS:
    crop_pdf(name, page, y0, y1, dpi, color=True)
    print(f"{name}: image OK")
print("OK zoom3-h6-18")
