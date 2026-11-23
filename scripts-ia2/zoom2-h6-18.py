#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-18 : zooms ciblés 2400 dpi pp.100-104 de L18 «من الأعمال الفاضلة وثوابها»
# positions tirées de ink-h6-18.py + constats zoom1-h6-18.py.
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

ZOOMS = [
    # ---- p.100 ----
    ("z2-p100-tamhid-l3", 100, 3270, 3490, 2400),  # عسى أن ينال بها بغيته
    ("z2-p100-hadith-head", 100, 3740, 4240, 1200),  # الحديث header + espace
    ("z2-p100-sanad", 100, 4230, 4700, 2400),     # عن أبي هريرة... عن النبي ﷺ قال
    ("z2-p100-matn-awn", 100, 5100, 5340, 2400),  # عون أخيه »؟ + ومن سلك
    ("z2-p100-matn-end", 100, 5740, 6060, 2400),  # ومن بطأ به عمله... [رواه مسلم بهذا اللفظ]
    # ---- p.101 ----
    ("z2-p101-gloses", 101, 1880, 2350, 2400),    # الشرح : toutes les gloses
    ("z2-p101-istikhlas", 101, 2350, 2900, 2400), # bande mystère y2396-2866
    ("z2-p101-intro-l1", 101, 4320, 4570, 2400),  # مجموعة من الأعمال الفاضلة يليق للمسلم
    ("z2-p101-intro-l2", 101, 4650, 4890, 2400),  # فضلها والقيام بها لما فيه من فضل وثواب عظيمين
    ("z2-p101-ragabba", 101, 5140, 5340, 2400),   # رغب النبي ﷺ في الإكثار من الإحسان إلى الناس
    ("z2-p101-item1-l2", 101, 5580, 5840, 2400),  # ونفعهم بما يتيسر من علم أو مال
    # ---- p.102 ----
    ("z2-p102-item2-l3", 102, 930, 1190, 2400),   # أو ينظر إلى ساعة X بتأجيل الأجل له
    ("z2-p102-aya-baqara", 102, 1150, 1420, 2400),  # وإن كان ذو عسرة... [البقرة: NNN]
    ("z2-p102-item3-l2", 102, 2360, 2570, 2400),  # جزاء ستر المسلم في الدنيا ستر الله
    ("z2-p102-item4-l1", 102, 2840, 3080, 2400),  # بأن يعينه بما يمكن من المساعدة إذا احتاج
    ("z2-p102-zumar", 102, 4180, 4460, 2400),     # قل هل يستوي... [الزمر: N]
    # ---- p.103 ----
    ("z2-p103-halaq", 103, 1300, 1490, 2400),     # حلق العلم والتعليم (حلقات ?)
    ("z2-p103-tadarsa", 103, 2270, 2510, 2400),   # التلاوة والتدبر والتدارسة يدخل
    ("z2-p103-sakinah-l2", 103, 3030, 3240, 2400),  # فلا تشعر بضيق أو غيره / كرب
    ("z2-p103-hafoof", 103, 3820, 4340, 2400),    # حفوف الملائكة + ذكر الله لهم في الملأ الأعلى
    ("z2-p103-manas-l2", 103, 4380, 4640, 2400),  # أن من أخر عمله تسويفا أو تفريطا
    ("z2-p103-aya-hujurat", 103, 4610, 5120, 2400),  # المسارعة بالأعمال + [الحجرات: 13]
    # ---- p.104 ----
    ("z2-p104-yustafad3", 104, 680, 940, 2400),   # طلب العلم الخالص لوجه الله لما له من نفع عميم
    ("z2-p104-taqwim1", 104, 1610, 1850, 2400),   # أصنف في خطاطة الأعمال الواردة في الحديث
    ("z2-p104-istithmar", 104, 3550, 3770, 2400),  # فيستهين بـ ...
    ("z2-p104-idad", 104, 5640, 6110, 2400),      # أحفظ حديث الدرس الموالي + سبعمائة
]

for name, page, y0, y1, dpi in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    ocr_save(png, name)
print("OK zoom2-h6-18")
