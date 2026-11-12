#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrections manuelles des 5 défauts de guillemets non appariés (zone primaire).
Chaque ancre doit apparaître exactement une fois — sinon abort sans écriture."""
import json, sys

FIXES = [
    {
        "book": "fiqh-5ep", "doc": "12011",
        "old": "ou en inclinaison&nbsp;\u202f».&nbsp;\u202f»</li>",
        "new": "ou en inclinaison&nbsp;\u202f».</li>",
        "why": "guillemet fermant doublé (citation du poète déjà fermée)",
    },
    {
        "book": "tafsir-5ep", "doc": "13915",
        "old": "a couvert leurs cœurs.&nbsp;\u202f» (<em>al-Muṭaffifīn</em> <span dir=\"rtl\" lang=\"ar\">(الْمُطَفِّفِينَ)</span>, 14)</p>",
        "new": "a couvert leurs cœurs.&nbsp;\u202f» (<em>al-Muṭaffifīn</em> <span dir=\"rtl\" lang=\"ar\">(الْمُطَفِّفِينَ)</span>, 14)\u202f»</p>",
        "why": "fermeture du hadith englobant (citation du verset imbriquée), après la référence",
    },
    {
        "book": "tafsir-5ep", "doc": "16743",
        "old": "(<em>al-Shūrā</em>, 3 — le manuel imprime «\u202f&nbsp;11&nbsp;\u202f»)</p>",
        "new": "(<em>al-Shūrā</em>, 3 — le manuel imprime «\u202f&nbsp;11&nbsp;\u202f»)\u202f»</p>",
        "why": "fermeture de la citation d'Ibn ʿĀshūr, après le dernier verset cité",
    },
    {
        "book": "tafsir-5ep", "doc": "16757",
        "old": "(’Abasa, 34-37)</p>",
        "new": "(’Abasa, 34-37)\u202f»</p>",
        "why": "fermeture de la citation d'Ibn Kathīr, après la référence du verset",
    },
    {
        "book": "tafsir-5ep", "doc": "16767",
        "old": "d’une datte&nbsp;\u202f!\u202f» [<em>al-Jāmi</em>",
        "new": "d’une datte&nbsp;\u202f!\u202f»\u202f» [<em>al-Jāmi</em>",
        "why": "fermeture de la citation d'al-Jalālayn (elle englobe le hadith), avant le crochet de source",
    },
    {
        "book": "tafsir-5ep", "doc": "16767",
        "old": "(الْإِنْشِقَاقُ)</span>, 1)</p>",
        "new": "(الْإِنْشِقَاقُ)</span>, 1)\u202f»</p>",
        "why": "fermeture du hadith de at-Tirmidhī, après la troisième référence de verset",
    },
]

def main():
    per_book = {}
    for f in FIXES:
        per_book.setdefault(f["book"], []).append(f)
    for book, fixes in per_book.items():
        path = f"content/books/{book}.json"
        raw = open(path).read()
        b = json.loads(raw)
        docs = ([b["intro"]] if b.get("intro") else []) + b["lessons"]
        for f in fixes:
            l = [x for x in docs if x and x.get("docId") == f["doc"]][0]
            fr = l["htmlFr"]
            if f["old"] not in fr and f["new"] in fr:
                continue  # déjà appliqué (idempotent)
            n = fr.count(f["old"])
            if n != 1:
                print(f"ABORT {book} {f['doc']}: ancre trouvée {n}× (attendu 1)")
                sys.exit(1)
        dirty = False
        for f in fixes:
            l = [x for x in docs if x and x.get("docId") == f["doc"]][0]
            if f["old"] in l["htmlFr"]:
                l["htmlFr"] = l["htmlFr"].replace(f["old"], f["new"], 1)
                print(f"  {book}/{f['doc']}: {f['why']}")
                dirty = True
        if not dirty:
            print(f"  {book}: déjà corrigé, rien à écrire")
            continue
        out = json.dumps(b, ensure_ascii=False, indent=2)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(out)
    print("OK — corrections appliquées")

if __name__ == "__main__":
    main()
