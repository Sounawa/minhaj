#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom1-h6-19 : recadrages blocs @2400 (gris) des sections de L19
# «فضل الله في الجزاء عن الأعمال» pp.105-109 + OCR psm 6/7.
# Bandes calibrées par ink-h6-19.py (600 dpi).
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

# --- p105 : matn (2 blocs) ---
zone("z1-p105-matn1", 105, 4590, 5320)   # عن ابن عباس... عن ربه تبارك وتعالى... ذلك: فمن همّ
zone("z1-p105-matn2", 105, 5290, 6120)   # فعملها... [رواه البخاري ومسلم في صحيحيهما بهذه الحروف]
# --- p106 : الشرح gloses + استخلاص + التحليل ---
zone("z1-p106-sharh", 106, 2300, 3450)   # الشرح: + gloses (كتب/حسنة/سيئة/همّ/ضعف)
zone("z1-p106-istikhl", 106, 3620, 4300) # استخلاص المضامين + items ×2
zone("z1-p106-tahlil", 106, 4550, 6160)  # التحليل + أولاً + intro (jusqu'au bas de page)
# --- p107 : lignes 1-3 + لطف passage + ثانياً + items 1-2 ---
zone("z1-p107-l1", 107, 650, 1400)       # إلى أضعاف كثيرة... مجرد فضل.
zone("z1-p107-lataf", 107, 1400, 2650)   # وإذا تأملنا ألفاظ الحديث...
zone("z1-p107-thani", 107, 2740, 3260)   # ثانياً: سر المضاعفة في ثواب الأعمال + intro
zone("z1-p107-item1", 107, 3280, 5000)   # item 1 complet (يخزي→ويعصي adjudiqué)
zone("z1-p107-item2", 107, 5000, 6000)   # item 2 complet (وإيقاعها adjudiqué)
# --- p108 : items 3-5 + مما يستفاد ---
zone("z1-p108-item3", 108, 650, 1650)
zone("z1-p108-item4", 108, 1680, 2900)   # آية + [النحل: ٩٧]
zone("z1-p108-item5", 108, 2920, 4360)
zone("z1-p108-yustafad", 108, 4440, 5850)
# --- p109 : تقويم + استثمار + إعداد قبلي ---
zone("z1-p109-taqwim", 109, 1050, 2400)
zone("z1-p109-istithmar", 109, 2780, 5060)
zone("z1-p109-idad", 109, 5580, 6120)
print("OK zoom1-h6-19")
