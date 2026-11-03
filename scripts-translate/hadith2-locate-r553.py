#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — localisation par bboxes de la couche texte (mots inversés) pour
placer les micro-crops de la passe 5-bis au pixel près."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
doc = fitz.open(PDF)

# mots recherchés sous forme INVERSÉE (couche miroir) + libellé
TARGETS = {
    107: [("تيمسف", "فسميت"), ("لوؤي", "يؤول"), ("لوقي", "يقول"),
          ("تشتعل", "وتستعمل")],
    109: [("نوتس", "ستون"), ("ةينامث", "ثمانية"), ("هدلبب", "ببلده"),
          ("نورشع", "عشرون"), ("ةرشع", "عشرة")],
    110: [("ليقتسيف", "فيستقيل?"), ("ميأقلا", "القاسم"),
          ("ةرشع", "عشرة"), ("نيرشع", "عشرين"),
          ("ةكمخ", "خمسة"), ("ضفاء", "فائضة?"), ("ةمكح", "حكمة")],
    105: [("قْسؤأ", "أوسق"), ("قاَوأ", "أواق")],
    108: [("ةينامث", "ثمانية?"), ("اثولم", "ملوثا"), ("نولا", "ملونا?")],
}

for page_no, words in TARGETS.items():
    pg = doc[page_no - 1]
    print(f"===== PAGE {page_no} (rect {pg.rect.width:.1f}x{pg.rect.height:.1f}) =====")
    raw = pg.get_text("dict")
    for blk in raw.get("blocks", []):
        for line in blk.get("lines", []):
            for span in line.get("spans", []):
                for w in span.get("words", []) if "words" in span else []:
                    pass
    # version simple : mots par recherche textuelle
    txt_words = pg.get_text("words")  # (x0,y0,x1,y1,word,...)
    for t, label in words:
        hits = [w for w in txt_words if t in w[4]]
        for w in hits:
            print(f"  {label:14s} {t!r:14s} -> x{w[0]:.0f}-{w[2]:.0f} y{w[1]:.0f}-{w[3]:.0f}")
        if not hits:
            print(f"  {label:14s} {t!r:14s} -> ABSENT de la couche")
