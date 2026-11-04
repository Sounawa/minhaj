# -*- coding: utf-8 -*-
"""R560 — calibration des positions par les chiffres ASCII du calque texte."""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
doc = fitz.open(PDF)

targets = {
    112: ["104", "103", "674"],
    113: ["675", "677", "681"],
    114: ["672"],
    115: ["673", "676", "678"],
    116: ["679", "680", "684", "104", "103"],
    117: [],
}
for pg, needles in targets.items():
    page = doc[pg - 1]
    for nd in needles:
        rects = page.search_for(nd)
        if rects:
            print(
                f"p{pg} «{nd}»: "
                + ", ".join(f"({round(r.x0)},{round(r.y0)})-({round(r.x1)},{round(r.y1)})" for r in rects[:4])
            )
        else:
            print(f"p{pg} «{nd}»: ABSENT")
