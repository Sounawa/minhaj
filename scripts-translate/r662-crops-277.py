# -*- coding: utf-8 -*-
# R662 — crops haute résolution des zones EN CONFLIT de la leçon 23 uh2
# (pdf-mut23h2u-277, المصحف والمحرف, p.120-124). Conflits recensés après
# relecture des 15 lectures R659 (5 pages pleines + 10 zooms) et des 15 bandes
# R658 : قول القرار بالصورة فقط. Sortie : tr-tmp/qa-crops-r662/
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r662"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (page, y0_pt, y1_pt, x0_pt, x1_pt, dpi, nom) — 0 = pleine largeur
ZONES = [
    # p.120 — titre + objectifs 1-2 (المصحف والمحرف vs التحرف)
    (120, 28, 150, 0, 0, 1500, "hi-p120-title-obj12"),
    # p.120 — objectifs 3-4 + début tamhīd (المخالفة vs الخلافَة, وبينوا vs وميزوا)
    (120, 140, 360, 0, 0, 1200, "hi-p120-obj34-tamhid"),
    # p.120 — متن complet (بقاء السياق vs السُّباق)
    (120, 400, 530, 0, 0, 1500, "hi-p120-matn"),
    # p.121 — première phrase de أهمية معرفة المصحف (كان في المتون vs كائن في المتن)
    (121, 240, 310, 0, 0, 1500, "hi-p121-ahamiyya-l1"),
    # p.121 — chaîne de l'exemple isnad + hadith عثمان
    (121, 340, 470, 0, 0, 1500, "hi-p121-isnad-chain"),
    # p.121 — correction يحيى بن معين (ابن مزاحم / فرد عليه / فردّه)
    (121, 440, 520, 0, 0, 1800, "hi-p121-correction"),
    # p.121 — intro تصحيف في المتن (أنه بإسناده عن زيد بن ثابت)
    (121, 505, 580, 0, 0, 1500, "hi-p121-matan-intro"),
    # p.121 — citation مسلم + bracket source (حجرة/حجيرة بخصفة, المسافر وقصرها)
    (121, 560, 700, 0, 0, 1500, "hi-p121-muslim-quote"),
    # p.122 — bloc تصحيف السمع (واضل الأحذب vs واصل الأحدب)
    (122, 225, 350, 0, 0, 1800, "hi-p122-sam-block"),
    # p.122 — bloc تصحيف في المعنى + ref المسند 18761
    (122, 420, 510, 0, 0, 1500, "hi-p122-maani-musnad"),
    # p.122 — organigramme أقسام المصحف (structure + titre)
    (122, 480, 670, 0, 0, 700, "hi-p122-diagram"),
    # p.122 — bracket مقاييس اللغة (2/43 vs 2/34)
    (122, 700, 765, 0, 0, 1800, "hi-p122-luga-bracket"),
    # p.123 — définition المحرف + le «53» flottant de la couche texte
    (123, 28, 130, 0, 0, 1800, "hi-p123-def53"),
    # p.123 — hadith جابر (رمي أبي... فكواه) mot à mot
    (123, 115, 235, 0, 0, 1800, "hi-p123-jabir-matn"),
    # p.123 — note غندر + ref 385 + glose الأكحل
    (123, 210, 330, 0, 0, 1800, "hi-p123-ghundar"),
    # p.123 — fin حكم التصحيف (والقدر الصحف أو المحرف مردود)
    (123, 415, 500, 0, 0, 1800, "hi-p123-hukm-clause"),
    # p.123 — التقويم items 2-3 (تصحيف السمع/الاسم + item 3)
    (123, 640, 765, 0, 0, 1500, "hi-p123-taqwim"),
    # p.124 — rubrique verte (الاستثمار vs الاستتمار)
    (124, 45, 115, 0, 0, 1800, "hi-p124-rubric"),
    # p.124 — quote complète ابن الصلاح (بطون الكتب) + ref 218
    (124, 100, 320, 0, 0, 1200, "hi-p124-quote"),
]
for p, y0, y1, x0, x1, dpi, name in ZONES:
    page = doc[p - 1]
    rect = fitz.Rect(x0 or 0, y0, x1 or page.rect.width, min(y1, page.rect.height))
    pix = page.get_pixmap(dpi=dpi, clip=rect)
    out = f"{OUT}/{name}.png"
    pix.save(out)
    print(out, pix.width, "x", pix.height)
