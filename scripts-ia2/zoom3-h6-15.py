#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-15 : micro-recadrages 2400 dpi (pdftoppm -x -y -W -H) sur les
# zones encore incertaines de L14 (pp.81-84 du tirage hadith-6ep) + OCR psm 7/6/13.
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(f"{DIR}/micro", exist_ok=True)

# (nom, page, y0, y1, dpi, x0frac, x1frac) — y en coordonnées 600 dpi
ZONES = [
    ("m081-ahdaf-head",   81, 1300, 1500, 2400, 0.0, 1.0),  # أهداف الأنشطة
    ("m081-ahdaf-item3",  81, 2260, 2450, 2400, 0.0, 1.0),  # أُوَظِّفَ مكتسباتي
    ("m081-inallah",      81, 3390, 3620, 2400, 0.0, 1.0),  # إن الله فرض … (blancs)
    ("m082-shirk",        82,  940, 1120, 2400, 0.0, 1.0),  # من هجر الشرك واجتنبه
    ("m082-hadith2-l3",   82, 1900, 2110, 2400, 0.0, 1.0),  # … الجنة لا يأمن جاره بوائقه
    ("m082-raqm",         82, 2930, 3090, 2400, 0.0, 0.5),  # رقم المستدرك (fin de ligne RTL = gauche)
    ("m082-raqm-full",    82, 2930, 3090, 2400, 0.0, 1.0),  # ligne citation complète
    ("m082-q-head",       82, 3160, 3360, 2400, 0.0, 1.0),  # أتأمل الأحاديث أعلاه
    ("m082-q3",           82, 3960, 4100, 2400, 0.0, 1.0),  # أبيّن كيف يستقيم إيمان العبد
    ("m082-q5-table",     82, 4880, 5420, 1800, 0.0, 1.0),  # tableau Q5
    ("m083-item1",        83, 1050, 1260, 2400, 0.0, 1.0),  # أستثمر مكتسباتي من الدروس
    ("m083-item2-head",   83, 2900, 3160, 2400, 0.0, 1.0),  # تضمّ أحاديث الدروس السابقة
    ("m083-table1-head",  83, 1600, 1980, 1800, 0.0, 1.0),  # en-tête tableau 1 + ligne أحرص
    ("m083-table2-head",  83, 3360, 3850, 1800, 0.0, 1.0),  # الحديث | القيمة المناسبة | …
    ("m084-idad",         84, 3130, 3540, 2400, 0.0, 1.0),  # أحفظ حديث الدرس الموالي
]

for (name, p, y0, y1, dpi, fx0, fx1) in ZONES:
    out = f"{DIR}/micro/{name}"
    if not os.path.exists(out + ".png"):
        # page 637x807 pt → px @600 : 5308x6725 ; facteur dpi/600
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        X0, X1 = int(W * fx0), int(W * fx1)
        Y0, Y1 = int(y0 * f), int(y1 * f)
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi),
                        "-gray", "-png", "-singlefile",
                        "-x", str(X0), "-y", str(Y0), "-W", str(X1 - X0), "-H", str(Y1 - Y0),
                        PDF, out], check=True)
    for psm in (7, 6, 13):
        r = subprocess.run(["tesseract", out + ".png", "stdout", "-l", "ara", "--psm", str(psm)],
                           env=env, capture_output=True, text=True)
        txt = " ".join(r.stdout.split())
        if txt.strip():
            print(f"── {name} psm{psm}: {txt}")
print("OK zoom3-h6-15")
