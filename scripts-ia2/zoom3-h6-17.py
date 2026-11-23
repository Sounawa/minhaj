#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-17 : zooms ciblés complémentaires L17 (suite zoom2, positions
# tirées du profil d'encre ink-h6-17.py — bandes exactes par ligne).
# Zones : p95 matn-l1 (ولا يكذبه à vérifier) ; p97 items 2-5 + آية + ثانياً ;
# p98 fin de ثانياً + مما يستفاد 3-4 + تقويم tête + tableau ;
# p99 يشوش/تضييع + الأحوال + fin Ghazali + الإعداد tête.
import subprocess, os

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
    print(f"{name}: OK ({os.path.getsize(png)//1024} Ko)")

ZOOMS = [
    # (nom, page, y0, y1, dpi, psms)
    ("z3-p95-matn-l1",   95, 4830, 5085, 2400, (6, 7)),   # المسلم أخو المسلم... ولا يكذبه ولا يحقره التقوى
    ("z3-p97-item2-l1",  97,  660,  915, 2400, (6, 7)),   # الخذلان وهو ترك إعانة من استعان [لدفع؟ به؟] ظلم
    ("z3-p97-kadb-l23",  97, 1440, 1900, 2400, (6, 7)),   # وخيانة وهو أشد الأشياء ضررا والصدق أشدها نفعا + أمر الله
    ("z3-p97-aya",       97, 2195, 2425, 2400, (6, 7)),   # آية الصادقين (couleur) + [التوبة: NNN]
    ("z3-p97-tahqir",    97, 2455, 2680, 2400, (6, 7)),   # بعد الآية : بحسب امرئ... + amorce item 4
    ("z3-p97-kayy2",     97, 2900, 3165, 2400, (6, 7)),   # لأن الله تعالى خلقه ورزقه ثم أحسن ...
    ("z3-p97-item5",     97, 4480, 5200, 2400, (6, 7)),   # item 5 التعرض للإيذاء (3 lignes)
    ("z3-p97-thani-head",97, 5320, 5520, 2400, (6, 7)),   # ثانيا: التقوى سبيل الأخوة
    ("z3-p97-thani-l1",  97, 5590, 5840, 2400, (6, 7)),   # إنما يعين على الالتزام هذه الحقوق والآداب
    ("z3-p98-taql3",     98,  655, 1400, 2400, (6, 7)),   # التقوى لا تحصل وحدها... رؤية الله تعالى (3 l.)
    ("z3-p98-yustafad3", 98, 2340, 2475, 2400, (6, 7)),   # اعتبار التقوى (bande claire)
    ("z3-p98-yustafad4", 98, 2570, 2800, 2400, (6, 7)),   # رقابة الله وشهوده وإحاطته بما عليه العباد
    ("z3-p98-taqwim-hd", 98, 2870, 3115, 2400, (6, 7)),   # heading التقويم ?
    ("z3-p98-taqwim1",   98, 3600, 3840, 2400, (6, 7)),   # أستخرج... حقوقا [تقتضيها ق/ف] أخوة الإسلام
    ("z3-p98-table",     98, 5160, 5910, 2400, (6, 7)),   # tableau (couleur claire)
    ("z3-p99-yashwush",  99, 1860, 2320, 2400, (6, 7)),   # يشوش القلب ويصد عن العبادة + تضييع الأوقات
    ("z3-p99-ahwal2",    99, 2600, 2830, 2400, (6, 7)),   # وقوة في الأحوال/الأهوال
    ("z3-p99-ghazali-end",99,3155, 3330, 2400, (6, 7)),   # شفاعة فلعلك تدخل + [إحياء 2/171]
    ("z3-p99-idad-head", 99, 3740, 4210, 1200, (6, 7)),   # heading الإعداد القبلي (blanc/couleur)
]
for name, page, y0, y1, dpi, psms in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    ocr_save(png, name, psms)

# p97 آية en couleur @1200 + binarisation douce (le gris 2400 peut manquer le bleu)
png = crop_pdf("z3-p97-aya-col", 97, 2195, 2425, 1200, color=True)
from PIL import Image, ImageOps
img = Image.open(png).convert("RGB")
g = ImageOps.autocontrast(img.convert("L"))
for t in (140, 170, 200):
    bw = g.point(lambda v, th=t: 0 if v < th else 255)
    out = f"{DIR}/zoom/z3-p97-aya-col-bw{t}.png"
    bw.save(out)
    with open(f"{DIR}/zoom/z3-p97-aya-col-bw{t}-psm6.txt", "w") as fh:
        fh.write(ocr(out, 6))
print("aya couleur binarisation OK")

# p98 tableau : couleur @1200 + autocontrast + seuils
png = crop_pdf("z3-p98-table-col", 98, 5160, 5910, 1200, color=True)
img = Image.open(png).convert("RGB")
g = ImageOps.autocontrast(img.convert("L"))
for t in (120, 150, 180):
    bw = g.point(lambda v, th=t: 0 if v < th else 255)
    out = f"{DIR}/zoom/z3-p98-table-col-bw{t}.png"
    bw.save(out)
    with open(f"{DIR}/zoom/z3-p98-table-col-bw{t}-psm6.txt", "w") as fh:
        fh.write(ocr(out, 6))
print("tableau couleur binarisation OK")
print("OK zoom3-h6-17")
