#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — CARTE HADITH-2-IADADI : manuel « al-Ḥadīth min Muwaṭṭaʾ al-imām
Mālik bi-Šarḥ az-Zarqānī » pour la 2ᵉ année de l'enseignement collégial
traditionnel (208 pages, PDF miroir content/textbooks-src/hadith-2-iadadi_text.pdf)
↔ livre portail hadith-2es (slots pdf-2..pdf-31, 30 leçons pdfOnly).

Livraison inaugurale de la carte : R534 (2026-11-03, passe 0640 ouvrier A).
Mécanique identique à kahf-map.py (R458/R487) : fix_line décode les mots
(caractères inversés), readable() ré-inverse la SÉQUENCE des mots par ligne.

MÉTHODE DES BORNES (jamais devinées) : chaque STARTS[i] = page d'ouverture de
la leçon i, sondée par le bloc « أهداف الدرس » (en-tête parfois muet à l'OCR —
les pages 79, 97, 111, 151, 183 portent « الإعداد القبلي » qui CLOT la leçon
précédente, convergence double) ; la borne supérieure d'une leçon = la leçon
suivante moins un. Leçons 26 et 28 : les noms de fichier du portail sont
illisibles (2682F41.PDF / 28673C1.PDF) — le titre se tranche PAR LE CONTENU à
la livraison (sondage p.177 : « صور الصيام الواجب والمنهي والمكروه » ;
sondage p.192 : « فضل الصيام والنزلة عند الصائم » — candidats sonnés, jamais
assertés). Annexes : فهرس الأعلام ouvre p.199 (p.198 vide, sondé) ; لائحة
المصادر ouvre p.203 (sondé) ; fin du manuel p.207/208.

COMPTEUR : 28 leçons + 2 annexes = 30 slots pdfOnly (pdf-2..pdf-31) ; l'intro
du livre (slot 10960, pdfUrl null) est déjà couverte par une livraison CMS.
"""
import fitz  # PyMuPDF

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"

# STARTS : pages d'ouverture sondées (objectifs) — preuve dans les commentaires.
STARTS = [
    8,    # l1  أحكام القصر والجمع — أهداف الدرس p.8
    14,   # l2  النافلة والمرور — أهداف الدرس p.14 (l1 clôturée par الإعداد القبلي p.13)
    21,   # l3  مستحبات الصلاة — أهداف الدرس p.21
    34,   # l4  الالتفات والتصفيق — أهداف الدرس p.34
    40,   # l5  ما يطلب فعله أو تركه — أهداف الدرس p.40
    46,   # l6  أحكام العيدين — أهداف الدرس p.46
    53,   # l7  صلاة الخوف والكسوف والخسوف — أهداف الدرس p.53
    60,   # l8  صلاة الاستسقاء — أهداف الدرس p.60
    67,   # l9  القِبلة وفضل المسجد النبوي — أهداف الدرس p.67 (« أن أتعرف آداب القبلة »)
    73,   # l10 الطهارة لمس المصحف وسجود التلاوة — أهداف الدرس p.73
    80,   # l11 فضل الذكر والدعاء — أهداف p.80 (en-tête muet, objectifs « أبين فضل الذكر ») ; الإعداد القبلي p.79
    86,   # l12 حكم الصلاة بعد الصبح والعصر — أهداف الدرس p.86
    91,   # l13 الجنائز 1 (غسل الميت) — أهداف الدرس p.91 ; الإعداد القبلي p.97
    98,   # l14 الجنائز 2 (القبر والدفن) — أهداف p.98 (en-tête muet « الدرس HE قادما », « أن أتعرف أحكام الدفن »)
    105,  # l15 مفهوم الزكاة وشروطها — أهداف الدرس p.105 ; الإعداد القبلي p.104
    112,  # l16 زكاة المعادن والحلي — أهداف p.112 (en-tête muet, « أن أتعرف زكاة المعدن والركاز ») ; الإعداد القبلي p.111
    118,  # l17 زكاة الميراث والدين والعروض — أهداف الدرس p.118 ; الإعداد القبلي p.117
    125,  # l18 زكاة الماشية — أهداف الدرس p.125 (إعداد p.124)
    132,  # l19 زكاة خلطاء الماشية — أهداف الدرس p.132
    139,  # l20 زكاة الثمار والحبوب — أهداف الدرس p.139
    146,  # l21 ما لا زكاة فيه والمستحقون — أهداف الدرس p.146 ; الإعداد القبلي p.151
    152,  # l22 زكاة الفطر — أهداف p.152 (en-tête muet « الدرس HE قادها ») ; الإعداد القبلي p.151
    158,  # l23 أحكام الصيام 1 — أهداف الدرس p.158 ; الإعداد القبلي p.157
    165,  # l24 أحكام الصيام 2 — أهداف الدرس p.165
    171,  # l25 أحكام الصيام 3 — أهداف الدرس p.171
    177,  # l26 slot pdf-27 (nom illisible 2682F41.PDF) — أهداف الدرس p.177 (« صور الصيام الواجب والمنهي والمكروه » ; titre = أحكام الصيام 4 à confirmer par le contenu)
    184,  # l27 القضاء والفدية في الصيام — أهداف p.184 (en-tête muet, « أن أتعرف أحكام قضاء الصيام والفدية ») ; الإعداد القبلي p.183
    192,  # l28 slot pdf-29 (nom illisible 28673C1.PDF) — أهداف الدرس p.192 (« فضل الصيام والنزلة عند الصائم » ; titre à confirmer par le contenu)
]
FIHRIS = 199   # slot pdf-30 فهرس الأعلام المترجم لهم — p.198 VIDE (sondée), index ouvre p.199
SOURCES = 203  # slot pdf-31 لائحة المصادر والمراجع — ouvre p.203 (sondée), fin p.207/208

# slots portail dans l'ordre : leçon i -> docId « pdf-{i+1} » (pdf-2..pdf-29)
SLOTS = {i: i + 1 for i in range(1, 29)}
ANNEX_SLOTS = {29: 30, 30: 31}  # fihris -> pdf-30, sources -> pdf-31

# étiquettes du portail (segments pdfUrl) — l26/l28 illisibles, titres à trancher
LABELS = {
    1: "أحكام القصر والجمع بين الصلاتين في السفر والحضر",
    2: "أحكام صلاة النافلة والمرور بين يدي المصلي",
    3: "من مستحبات الصلاة وآدابها",
    4: "الالتفات والتصفيق والكلام في الصلاة",
    5: "ما يطلب فعله أو تركه في الصلاة فرضا ونفلا",
    6: "أحكام العيدين",
    7: "صلاة الخوف والكسوف والخسوف",
    8: "صلاة الاستسقاء",
    9: "أحكام القِبلة وفضل المسجد النبوي",
    10: "الطهارة لمس المصحف وسجود التلاوة",
    11: "فضل الذكر والدعاء",
    12: "حكم الصلاة بعد الصبح والعصر",
    13: "أحكام الجنائز - غسل الميت وكفنه والصلاة عليه",
    14: "أحكام الجنائز - القبر والدفن وآداب الجنازة",
    15: "مفهوم الزكاة وشروطها",
    16: "زكاة المعادن والحلي وأموال اليتامى",
    17: "زكاة الميراث والدين والعروض",
    18: "زكاة الماشية",
    19: "زكاة خلطاء الماشية",
    20: "زكاةُ الثمار والحبوب",
    21: "ما لا زكاة فيه والمستحقون للزكاة",
    22: "زكاة الفطر",
    23: "أحكام الصيام 1",
    24: "أحكام الصيام 2",
    25: "أحكام الصيام 3",
    26: "(nom de fichier portail illisible 2682F41.PDF — leçon 26 par ordre ; sondage p.177 : أحكام الصيام 4)",
    27: "القضاء والفدية في الصيام",
    28: "(nom de fichier portail illisible 28673C1.PDF — leçon 28 par ordre ; sondage p.192 : فضل الصيام)",
}


def fix_line(s: str) -> str:
    """Décode une ligne OCR : chaque mot a ses caractères inversés."""
    return " ".join(w[::-1] for w in s.split())


def readable(fixed: str) -> str:
    """Ré-inverse la séquence des mots de chaque ligne déjà décodée mot à mot."""
    out = []
    for line in fixed.split("\n"):
        words = line.split()
        out.append(" ".join(reversed(words)) if len(words) > 1 else line)
    return "\n".join(out)


def _pages(lo: int, hi: int) -> dict:
    doc = fitz.open(PDF)
    pages = {}
    for p in range(lo, hi + 1):
        raw = doc[p - 1].get_text()
        pages[p] = {"raw": raw, "fixed": "\n".join(fix_line(l) for l in raw.split("\n"))}
    return pages


def extract(lesson: int) -> dict:
    lo = STARTS[lesson - 1]
    hi = STARTS[lesson] - 1 if lesson < len(STARTS) else FIHRIS - 1
    if lesson == len(STARTS):  # l28 = p.192..197 (p.198 vide, sondée)
        hi = FIHRIS - 1
    return {"lesson": lesson, "slot": f"pdf-{SLOTS[lesson]}",
            "label": LABELS[lesson], "pages": (lo, hi), "content": _pages(lo, hi)}


def extract_annex(docid: int) -> dict:
    """29 = فهرس الأعلام (pdf-30, p.199..202) ; 30 = لائحة المصادر (pdf-31, p.203..208).
    Bornes intérieures tranchées par sondage (p.198 vide, p.199 فهرس, p.203 sources)."""
    lo, hi = {29: (FIHRIS, SOURCES - 1), 30: (SOURCES, 208)}[docid]
    return {"docid": docid, "slot": f"pdf-{ANNEX_SLOTS[docid]}",
            "pages": (lo, hi), "content": _pages(lo, hi)}


def main() -> None:
    n = len(STARTS)
    print(f"CARTE HADITH-2-IADADI — {n} leçons + 2 annexes (manuel miroir Muwaṭṭaʾ/Zarqānī 2ᵉ collégial, 208 p.)")
    print(f"livre portail : hadith-2es (slots pdf-2..pdf-31, 30 pdfOnly, 0 htmlFr)")
    for i in range(1, n + 1):
        lo = STARTS[i - 1]
        hi = (STARTS[i] - 1) if i < n else (FIHRIS - 1)
        print(f"  leçon {i:2d} — slot pdf-{SLOTS[i]:<3d} — p.{lo}-{hi} — {LABELS[i][:60]}")
    print(f"  annexe 29 — slot pdf-30 — p.{FIHRIS}-{SOURCES-1} — فهرس الأعلام المترجم لهم")
    print(f"  annexe 30 — slot pdf-31 — p.{SOURCES}-208 — لائحة المصادر والمراجع")


if __name__ == "__main__":
    main()
