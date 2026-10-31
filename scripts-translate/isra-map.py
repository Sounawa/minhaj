#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Carte leçons↔pages du manuel miroir Tafsīr 2 ثانوي (Isrāʾ) + extraction.

ÉTABLI R458 : le manuel complet (221 p., collection archive.org
1_20220304_20220304_2251, couche texte OCR en ordre visuel inversé mot à mot)
porte les 28 leçons d'Isrāʾ dans le MÊME ORDRE que les slots 709-736 de
tafsir-5ep (preuve d'alignement : la leçon n°7 en p51 porte les objectifs
« بَرُّ الوالدين / عبادة الله وحده » = v23-25 = slot 715 ; la leçon n°28 en
p202 porte «الآيتان» = les deux versets 109-110 = slot 736 ; le fihris
p209-214 = slot 737 ; les sources p215-220 = slot 738).

La couche texte est INVERSÉE MOT À MOT (ordre visuel) : le décodage = inverser
chaque mot. Les plages de versets des en-têtes sont corrompues à l'OCR —
l'ORDRE fait foi (garde : vérifier le contenu d'une leçon sur ses objectifs
avant toute livraison).

Usage :
  python3 scripts-translate/isra-map.py            # imprime la carte
  python3 scripts-translate/isra-map.py 1          # extrait la leçon 1 (brut + décodé)
  python3 scripts-translate/isra-map.py 7          # extrait la leçon 7
"""
import sys

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-2-thanawi_text.pdf"

# Vrais départs (fixes) : leçon i = pages STARTS[i] .. STARTS[i+1]-1
# p7-10 = matière liminaire (échantillon méthodologique de leçon + évaluation
# type + compétences + table de répartition de l'année) — la leçon 1 RÉELLE
# commence p11 (mêmes objectifs que l'échantillon p7 + تمهيد + développement).
STARTS = [11, 18, 24, 30, 37, 44, 51, 58, 65, 72, 80, 87, 94, 101, 110, 118,
          125, 131, 139, 146, 154, 161, 168, 175, 182, 188, 195, 202]
# bornes des annexes
FIHRIS = (209, 214)
SOURCES = (215, 220)

# slots tafsir-5ep dans l'ordre (709..736 = leçons 1..28, 737 fihris, 738 sources)
SLOTS = {i: 708 + i for i in range(1, 29)}   # leçon i -> docId slot
VERSE_RANGE = {
    1: "v1", 2: "v2-4", 3: "v5-8", 4: "v9-12", 5: "v13-17", 6: "v18-22",
    7: "v23-25", 8: "v26-30", 9: "v31-33", 10: "v34-36", 11: "v37-40",
    12: "v41-44", 13: "v45-48", 14: "v49-55", 15: "v56-60", 16: "v61-65",
    17: "v66-69", 18: "v70-72", 19: "v73-77", 20: "v78-81", 21: "v82-85",
    22: "v86-89", 23: "v90-93", 24: "v94-98", 25: "v99-100", 26: "v101-104",
    27: "v105-108", 28: "v109-110",
}


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def extract(lesson: int) -> dict:
    doc = fitz.open(PDF)
    lo = STARTS[lesson - 1]
    hi = STARTS[lesson] - 1 if lesson < len(STARTS) else FIHRIS[0] - 1
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
        print(f"LEÇON {n} — slot {d['slot']} — {d['verses']} — pages {d['pages'][0]}-{d['pages'][1]}")
        print("=" * 70)
        for p in range(d["pages"][0], d["pages"][1] + 1):
            print(f"\n===== PAGE {p} (décodé) =====")
            print(d["content"][p]["fixed"])
    else:
        print("CARTE ISRA — 28 leçons + annexes (manuscrit miroir 221 p.)")
        for i in range(1, 29):
            hi = STARTS[i] - 1 if i < len(STARTS) else FIHRIS[0] - 1
            print(f"  leçon {i:2d} | slot pdf-mut23h3c-{SLOTS[i]} | {VERSE_RANGE[i]:8s} | p{STARTS[i-1]}-{hi}")
        print(f"  fihris  | slot pdf-mut23h3c-737 |          | p{FIHRIS[0]}-{FIHRIS[1]}")
        print(f"  sources | slot pdf-mut23h3c-738 |          | p{SOURCES[0]}-{SOURCES[1]}")


if __name__ == "__main__":
    main()
