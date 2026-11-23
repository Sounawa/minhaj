#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-19 : recadrages ligne-à-ligne @2400 des points douteux L19
# (bandes calibrées ink-h6-19 + zoom1). Points : matn p105 l2/l6, glose همّ,
# أولاً intro (همّ العبد؟), لطف passage, item1 p107 (ويعصي/شاكراً لله), item2
# (وإيقاعها), p108 item3 (استُصلحت/أزكى), item4 (آية+réf+يحصره), item5
# (arithmétique وللأول ألفاً), مما يستفاد 3-4, p109 استثمار + réf.
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

# --- p105 ---
zone("z2-p105-matn-l2", 105, 4820, 5070)   # عن ربه تبارك وتعالى قال: إن الله كتب الحسنات...
zone("z2-p105-matn-l6", 105, 5745, 5990)   # بها فعملها كتبها الله سيئة واحدة». [رواه...]
# --- p106 ---
zone("z2-p106-glose-hamm", 106, 2840, 3070)  # همّ: الهمّ: القصد إلى الفعل
zone("z2-p106-tahlil-l2", 106, 5190, 5400)  # هذا حديث شريف عظيم؛ بيّن فيه النبي ﷺ مقدار تفضّل الله
zone("z2-p106-tahlil-l3", 106, 5430, 5665)  # على خلقه... أن جعل همّ العبد
zone("z2-p106-tahlil-l4", 106, 5690, 6120)  # بالحسنة... وجعل همّه بالسيئة... عشراً إلى سبعمائة ضعف؛
# --- p107 ---
zone("z2-p107-lataf-l3", 107, 2150, 2630)   # كاملة» فجعلها كاملة مع أنه لم يعمل... فقللها
zone("z2-p107-item1-l1", 107, 3295, 3520)   # 1- أن الله تعالى جعل الهمّ بالحسنة حسنة؛ لعقد القلب...
zone("z2-p107-item1-l2", 107, 3530, 3770)   # الخير بالقلب. ولا يلزم في المقابل...
zone("z2-p107-item1-l3", 107, 3770, 4015)   # سيئة؛ أن الكف عن الشر... باعتقاد آخر
zone("z2-p107-item1-l4", 107, 4010, 4250)   # ينوي به الخير؛ ويعصي به هوى الشر... ويدل له
zone("z2-p107-item1-l6", 107, 4495, 4710)   # بأن تارك السيئة... إذا تركها [شاكراً لله]] ولا يدخل
zone("z2-p107-item2-l4", 107, 5750, 5965)   # مضاعفة بمقدار إخلاص النية وإيقاعها في مواضعها.
# --- p108 ---
zone("z2-p108-item3-l2", 108, 930, 1145)    # في أزكى أرض؛ ثم استُصلحت ودرست وبذرت...
zone("z2-p108-item4-l3", 108, 2165, 2415)   # سائر الحسنات... وقد قال جل جلاله: (ولنجزينهم...)
zone("z2-p108-item4-l4", 108, 2395, 2665)   # آية suite + [النحل: ٩٧] + وكل هذه المضاعفة
zone("z2-p108-item4-l5", 108, 2650, 2875)   # العباد لا على مقدار فضل الله... يحصره خلقه
zone("z2-p108-item5-l4", 108, 3670, 3875)   # عشرة؛ فإذا تصدق بها الثاني صارت له عشرة وللأول مائة
zone("z2-p108-item5-l5", 108, 3890, 4125)   # الثالث صارت له عشرة وللثاني مائة وللأول ألفاً
zone("z2-p108-yust-l3", 108, 5280, 5520)    # تبشير الفائزين برضى الله... إلا من أبى
zone("z2-p108-yust-l4", 108, 5570, 5800)    # أهمية إخلاص العمل وقوة الإيمان/اليقين
# --- p109 ---
zone("z2-p109-taqw-1", 109, 1310, 1530)
zone("z2-p109-taqw-2", 109, 1560, 1800)
zone("z2-p109-taqw-3", 109, 1860, 2090)
zone("z2-p109-ist-l3", 109, 3530, 3775)     # ويصل فيه رحمه ويعمل/يعلم لله عز وجل فيه بحقه» قال...
zone("z2-p109-ist-l7", 109, 4800, 5035)     # ولا يصل فيه رحمه؛ ولا يعلم لله فيه حقه؛ ... قال: وعبد
zone("z2-p109-ist-ref", 109, 4900, 5065)    # [مسند الإمام أحمد ٢٩/٥٦٢]
zone("z2-p109-idad-l", 109, 5950, 6065)     # أحفظ حديث الدرس الموالي...
print("OK zoom2-h6-19")
