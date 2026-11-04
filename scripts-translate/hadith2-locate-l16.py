# -*- coding: utf-8 -*-
"""R560 — Crops guidés par le calque texte (search_for → bbox ± marge).
Cible: āya Tawba p112/p116, Muwaṭṭaʾ 680/684 p116, citation 678 + عمشر p115,
glossaire p113 (المعدن→اللؤلؤ), citations p113, Bukhārī p117, objectifs p112."""
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r560"
doc = fitz.open(PDF)


def show_hits(page_no, needle, label):
    pg = doc[page_no - 1]
    rects = pg.search_for(needle)
    print(f"p{page_no} «{label}»: {[(round(r.x0), round(r.y0), round(r.x1), round(r.y1)) for r in rects[:6]]}")
    return rects


# diagnostic: où sont les chaînes clés ?
show_hits(112, "التوبة", "التوبة p112")
show_hits(112, "أتعرف", "objectif1 p112")
show_hits(112, "المعادن", "المعادن p112")
show_hits(113, "عنبر", "عنبر p113")
show_hits(113, "نافع", "نافع p113")
show_hits(113, "طلي", "طلي p113")
show_hits(115, "حصد", "حصد p115")
show_hits(115, "الزكاة", "زكاة p115")
show_hits(116, "680", "680 p116")
show_hits(116, "684", "684 p116")
show_hits(116, "التوبة", "التوبة p116")
show_hits(117, "البخاري", "البخاري p117")
show_hits(117, "يصنع", "يصنع p117")
