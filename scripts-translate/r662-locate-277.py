# -*- coding: utf-8 -*-
# R662 — localisation mot à mot (rects) des tokens en conflit sur p.120-124
# La couche texte est inversée char à char : on cherche les formes RENVERSÉES.
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
doc = fitz.open(PDF)

TARGETS = {
    120: ["ساق", "فرحم", "ةفلاخ", "وينوب", "اوزيمو", "يصحتل"],
    121: ["هدانسا", "هداتسا", "مجارم", "محازم", "دراف", "ةدرف"],
    122: ["بذح", "18761", "16781", "43/2", "34/2", "نازعلا"],
    123: ["53", "واركف", "يواركف", "بارخلا", "لاحكلا", "ردنوغ", "ردنج"],
    124: ["رامتسا", "نوتب", "812", "218"],
}
for p, toks in TARGETS.items():
    page = doc[p - 1]
    words = page.get_text("words")
    print(f"===== PAGE {p} =====")
    for w in words:
        x0, y0, x1, y1, txt = w[0], w[1], w[2], w[3], w[4]
        rev = txt[::-1]
        for t in toks:
            if t in txt or t in rev:
                print(f"  token={txt!r} rev={rev!r} rect=({x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f})")
                break
