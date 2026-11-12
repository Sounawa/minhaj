# -*- coding: utf-8 -*-
"""Microcrops d'adjudication leçon 411 (R689-c) — zones contestées."""
import fitz
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r689c"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
X0, X1 = 0.04, 0.96


def band(name, pageno, y0, y1, dpi=900, x0=X0, x1=X1):
    page = doc[pageno - 1]
    r = page.rect
    clip = fitz.Rect(r.x0 + r.width * x0, r.y0 + r.height * y0,
                     r.x0 + r.width * x1, r.y0 + r.height * y1)
    pix = page.get_pixmap(dpi=dpi, clip=clip)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    scale = 1800 / img.width
    img = img.resize((1800, int(img.height * scale)), Image.LANCZOS)
    img.save(f"{OUT}/{name}.png")
    print(name, img.size)


# a) p.148 — hadith 1263 : la ligne « فتكون كفارة ذلك عنق رقبة »
band("a411-1263-anaq", 148, 0.10, 0.22)
# b) p.147 — hadith 1252 : la première phrase du Prophète (لعلک أذاک هوامک)
band("b411-1252-lalaka", 147, 0.62, 0.80)
# c) p.148 — les deux gloses (أنسك بشاة / قبضة) + استخلاص items
band("c411-gloses-istihlas", 148, 0.48, 0.72)
# d) p.149 haut — fin du hadith 1255 (كما مر الله به / كما أمره الله تعالى)
band("d411-1255-fin", 149, 0.04, 0.13)
# e) p.149 — «مدين مدين» + التكرير (عموم النية) + نزلت الآية خاضة + لأصح قولي مالك
band("e411-madin-nazalat", 149, 0.28, 0.52)
# f) p.149 bas — «فعليه ذم» après غير ضرورة
band("f411-dhimm", 149, 0.88, 0.98)
# g) p.150 haut — hadith 1256 (من تفل شعرا / بنورة / قفاه لموضع الصائم)
band("g411-1256-tafl", 150, 0.06, 0.34)
# h) p.151 — المائدة : numéro d'āya + le dialogue d'Omar (هل تحفظ/تقرأ...)
band("h411-maida", 151, 0.26, 0.62)
