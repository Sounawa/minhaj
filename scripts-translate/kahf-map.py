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
(objectifs « مناظر النبي ﷺ » visibles) — les STARTS suivants se tranchent passe
après passe par sondage des objectifs, jamais devinés.

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
STARTS = [10, 17]
# bornes des annexes (à trancher par sondage quand la leçon 26 sera atteinte)
ACTIVITES = None   # slot 765
FIHRIS = None      # slot 766
SOURCES = None     # slot 767

# slots tafsir-5ep dans l'ordre (739..764 = leçons 1..26, 765 activités,
# 766 fihris, 767 sources)
SLOTS = {i: 738 + i for i in range(1, 27)}   # leçon i -> docId slot
VERSE_RANGE = {
    1: "v1-5", 2: "v6-9", 3: "v10-12", 4: "v13-16", 5: "v17-18", 6: "v19-20",
    7: "v21-24", 8: "v25-27", 9: "v28-29", 10: "v30-31", 11: "v32-35",
    12: "v36-43", 13: "v44-45", 14: "v46-48", 15: "v49-52", 16: "v53-55",
    17: "v56-58", 18: "v59-64", 19: "v65-72", 20: "v73-77", 21: "v78-81",
    22: "v82-84", 23: "v85-91", 24: "v92-97", 25: "v98-101", 26: "v102-105",
}


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
