#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R690 — localisation des renvois et citations pour microcrops leçon 412.
Cherche dans le calque brut (ordres visuels possibles) les ancres : الموطأ، سورة الحج،
وال citations clés. Sort les rects PDF pour crops."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)

ANCRE = ["الموطأ", "سورة", "الحج", "الآية", "رمضان", "أشهر", "شوال", "القعدة",
         "التنعيم", "الجعرانة", "مرارا", "بينهما", "تركها", "استخلاص", "مات",
         "الإعداد", "افترق", "افصل", "تجوزت", "نذر", "تجهزت", "أعرّف", "أبين",
         "أستخرج", "استئذن", "سعيد:", "الكعبة", "زيارة"]

for pno in range(152, 159):
    page = doc[pno - 1]
    words = page.get_text("words")  # x0,y0,x1,y1,word,block,line,word_no
    print(f"===== PAGE {pno} ({len(words)} mots) =====")
    for w in words:
        x0, y0, x1, y1, t = w[0], w[1], w[2], w[3], w[4]
        if any(a in t for a in ANCRE):
            print(f"  [{x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}] {t[:50]}")
