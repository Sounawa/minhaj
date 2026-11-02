#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Carte leçons↔pages du manuel miroir Tafsīr 3 ثانوي (al-Kahf) + extraction.

ÉTABLI R487 : le manuel complet (224 p., collection archive.org
1_20220304_20220304_2251, couche texte OCR en ordre visuel inversé mot à mot —
le mot الكهف arrive « فهكلا ») porte les leçons de sūrat al-Kahf, même mécanique
que isra-map.py (R458). Source tranchée par la GRILLE DU LIVRE (pdfUrl des
slots pdf-mut23h3c-739+ = dossier التفسير-الثالثة-ثانوي du portail) et par le
contenu : la préface p.5 porte « دروس في تفسير سورة الكهف », la grille de
compétences p.8 « تحصيل معاني سورة الكهف ».

SONDAGE R487 : p.5-8 = préface + compétences ; p.9 = fihris du livre ; la leçon 1
(Kahf v1-5, slot pdf-mut23h3c-739) commence p.10 (objectifs « أن أتعرف سورة
الكهف وفضلها وسبب نزولها ») et s'achève p.16 ; la leçon 2 (v6-9) ouvre p.17
(objectifs « مناظر النبي ﷺ » sondés R487) et s'achève p.22 (استثمار + invocations,
sondés R488) ; la leçon 3 ouvre p.23.

SONDAGE R491 : en-têtes imprimés du livre TRANCHÉS PAR LE CONTENU (précédent de
la leçon 28 d'Isrāʾ, jamais deviné) : p.23 porte « أهداف الدرس (الكهف: الآيات
10-14) » — la leçon 3 couvre donc les āyāt 10 à 14 (contre (10-12) à la grille
du portail, divergence documentée) et s'achève avant p.29 ; p.29 porte « أهداف
الدرس (الكهف: الآيات 15-16) » — la leçon 4 couvre les āyāt 15 à 16 (contre
(13-16) à la grille du portail, divergence documentée) et ouvre p.29 ; sa borne
supérieure à trancher par sondage à l'armement de la leçon 4.

SONDAGE R492 : p.37 porte « أهداف الدرس » — la leçon 5 ouvre p.37, la leçon 4
s'achève donc p.36 ; p.44 porte « أهداف الدرس » — la leçon 6 ouvre p.44, la
leçon 5 s'achève p.43 (p.44 sondant « مشهد استغراب أصحاب الكهف بعد اليقظة »,
conforme à la grille v19-20). Bornes 5+ restant à trancher à chaque armement.

SONDAGE R497 : p.50 porte « أهداف الدرس » — la leçon 7 ouvre p.50, la leçon 6
couvre donc p.44-49 (p.44 NUM « 91-02 » = āyāt 19-20, convergence avec la
grille ; p.51 NUM « 12-42 » = āyāt 21-24, conforme à la grille de la leçon 7).

Usage :
  python3 scripts-translate/kahf-map.py            # imprime la carte
  python3 scripts-translate/kahf-map.py 1          # extrait la leçon 1 (p.10-16)
"""
import sys

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"

# Vrais départs (fixes) : leçon i = pages STARTS[i] .. STARTS[i+1]-1
# p5-9 = matière liminaire (préface, compétences, fihris) — la leçon 1 RÉELLE
# commence p10 ; leçon 2 ouvre p17 (objectifs sondés R487).
STARTS = [10, 17, 23, 29, 37, 44, 50, 58, 65, 73, 79, 87, 96, 102, 110, 118, 125, 132]
# +96 : borne leçon 13 tranchée par sondage R511 (kahf-probe-l12.py + rendu
# image p87 « (الآيات: 36-43) » badge 12 et p96 « (الآيات: 44-45) » badge 13)
# — la leçon 12 couvre p.87-95, JAMAIS devinée.
# +102 : borne leçon 14 tranchée par sondage R512 (kahf-probe-l13.py, texte
# brut : « أهداف الدرس » p.102 — objectifs « مشاهد القيامة / إحصاء الأعمال /
# يوم العرض » conformes au slot -752 v46-48) — la leçon 13 couvre p.96-101.
# +110 : borne leçon 15 tranchée par sondage R512 (sonde textuelle p.105-113 :
# « أهداف الدرس » p.110) — la leçon 14 couvre p.102-109.
# +118 : borne leçon 15 tranchée par sondage R514 (kahf-probe-l15.py :
# « أهداف الدرس » p.118, badge « (الكهف: 55-35…) » inversé = (الكهف: 53-55)
# imprimé = cache 54-56, objectifs « الأمثال / إرسال الرسل / الجدال بالباطل »
# conformes) — la leçon 15 couvre p.110-117, JAMAIS devinée.
# +125 : borne leçon 17 tranchée par sondage R514 (sonde textuelle p.122-128 :
# p.124 porte l'إعداد القبلي de la leçon 16, NUM inversé « 85-65 » = (56-58)
# imprimé = cache 57-59 versets de la leçon 17 ; p.125 ouvre « أهداف الدرس »
# objectifs « صفات الكافرين المعرضين / سعة رحمة الله في تأخير العقوبة »
# conformes au slot -755) — la leçon 16 couvre p.118-124, JAMAIS devinée.
# +132 : borne leçon 18 tranchée par sondage R515 (kahf-probe-l18.py, texte
# brut : p.132 porte « أهداف الدرس (الكهف: الآيات 59-64) » — objectifs « تفاصيل
# قصة موسى والعبد الصالح / أهمية الرحلة في طلب العلم وآدابها » conformes au
# slot -756 ; p.133 commentaire de v60 cache « و موسى وهو موسى بن عمران » ;
# badge p.132 conforme à la grille v59-64 imprimé = cache 60-65, moins un
# depuis leçon 12, et à la continuité v58→v59) — la leçon 17 couvre p.125-131,
# JAMAIS devinée.
# bornes des annexes (à trancher par sondage quand la leçon 26 sera atteinte)
ACTIVITES = None   # slot 765
FIHRIS = None      # slot 766
SOURCES = None     # slot 767

# slots tafsir-5ep dans l'ordre (739..764 = leçons 1..26, 765 activités,
# 766 fihris, 767 sources)
SLOTS = {i: 738 + i for i in range(1, 27)}   # leçon i -> docId slot
VERSE_RANGE = {
    1: "v1-5", 2: "v6-9", 3: "v10-14", 4: "v15-16", 5: "v17-18", 6: "v19-20",
    7: "v21-24", 8: "v25-27", 9: "v28-29", 10: "v30-31", 11: "v32-35",
    12: "v36-43", 13: "v44-45", 14: "v46-48", 15: "v49-52", 16: "v53-55",
    17: "v56-58", 18: "v59-64", 19: "v65-72", 20: "v73-77", 21: "v78-81",
    22: "v82-84", 23: "v85-91", 24: "v92-97", 25: "v98-101", 26: "v102-105",
}
# R491 : plages 3-4 tranchées par les en-têtes imprimés du livre (p.23 : 10-14 ;
# p.29 : 15-16) — la grille du portail (10-12 / 13-16) diverge, documenté ; les
# plages 5+ restent celles de la grille, à trancher par sondage à chaque armement.
# R492 : départs sondés p.37 (leçon 5) et p.44 (leçon 6) — en-têtes أهداف الدرس.
# R497 : départ de la leçon 7 sondé p.50 — la leçon 6 couvre p.44-49 (v19-20).
# R500ter/R508 : départs sondés p.58 (leçon 8), p.65 (leçon 9), p.73 (leçon 10) —
# NUM p.66 «92-82» inversé = 28-29 ; R509 : borne de la leçon 10 tranchée p.78
# (الإعداد القبلي NUM «23-53» inversé = 32-35) — la leçon 11 ouvre p.79
# (أهداف الدرس sondé, NUM p.79).
# R509bis : borne de la leçon 11 tranchée — l'إعداد القبلي de p.86 porte NUM
# «34-63» inversé = 36-43 (verses de la leçon 12) et les objectifs de la
# leçon 12 ouvrent p.87 (أهداف الدرس, p.87 citant « (الكهف: 36-43) » p.88) —
# la leçon 11 couvre donc p.79-86, jamais devinée.


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def extract(lesson: int) -> dict:
    doc = fitz.open(PDF)
    lo = STARTS[lesson - 1]
    hi = STARTS[lesson] - 1 if lesson < len(STARTS) else None
    if hi is None:
        raise SystemExit("STARTS incomplets : borne supérieure de la leçon "
                         f"{lesson} à trancher par sondage avant extraction")
    pages = {}
    for p in range(lo, hi + 1):
        raw = doc[p - 1].get_text()
        pages[p] = {"raw": raw, "fixed": "\n".join(fix_line(l) for l in raw.split("\n"))}
    return {"lesson": lesson, "slot": f"pdf-mut23h3c-{SLOTS[lesson]}",
            "verses": VERSE_RANGE[lesson], "pages": (lo, hi), "content": pages}


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        n = int(sys.argv[1])
        d = extract(n)
        print(f"KAHF LEÇON {n} — slot {d['slot']} — {d['verses']} — pages {d['pages'][0]}-{d['pages'][1]}")
        print("=" * 70)
        for p in range(d["pages"][0], d["pages"][1] + 1):
            print(f"\n===== PAGE {p} (décodé) =====")
            print(d["content"][p]["fixed"])
    else:
        print("CARTE KAHF — 26 leçons + annexes (manuel miroir 3 ثانوي, 224 p.)")
        for i in range(1, 27):
            if i - 1 >= len(STARTS):
                print(f"  leçon {i:2d} | slot pdf-mut23h3c-{SLOTS[i]} | {VERSE_RANGE[i]:8s} | start à trancher")
                continue
            hi = STARTS[i] - 1 if i < len(STARTS) else None
            rng = f"p{STARTS[i-1]}-{hi}" if hi else f"p{STARTS[i-1]}-?"
            print(f"  leçon {i:2d} | slot pdf-mut23h3c-{SLOTS[i]} | {VERSE_RANGE[i]:8s} | {rng}")
        print("  annexes | slots 765 activités / 766 fihris / 767 sources — bornes à trancher")


if __name__ == "__main__":
    main()
