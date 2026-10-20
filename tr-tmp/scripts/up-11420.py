#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection savante : leçon 11420 (fiqh-1es, leçon imprimée 6 — صفة الوضوء ومستحباته).

Le wuḍūʾ : sa description et ses actes recommandés — la suite du matn (masḥ de la
tête, des oreilles, lavage des pieds) + les mustaḥabbāt et le dire du sorti d'ablutions.

Hadiths VÉRIFIÉS sunnah.com :
- Bukhārī 165 (bāb غسل الأعقاب EXACT) — « Malheur aux talons, de par le Feu ! »
- Tirmidhī 55 (bāb فيما يقال بعد الوضوء EXACT) — les huit portes du Paradis
- Muslim 482 (bāb ما يقال في الركوع والسجود EXACT) — le plus proche en prosternation
- Muslim 226a (bāb صفة الوضوء وكماله EXACT) — ʿUthmān via Ḥumrān

QA : guillemets appariés, 0 apostrophe droite, 0 arabe résiduel hors <em>.
"""

import json

BOOK = "/home/z/my-project/content/books/fiqh-1es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
DOC = "11420"

HTML_FR = open("/home/z/my-project/tr-tmp/11420.fr.html", encoding="utf-8").read()


def main() -> None:
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    lesson = None
    for l in d["lessons"]:
        if str(l.get("docId")) == DOC:
            lesson = l
            break
    if lesson is None:
        raise SystemExit(f"ERREUR: leçon {DOC} introuvable dans fiqh-1es")
    old = lesson.get("htmlFr") or ""
    lesson["htmlFr"] = HTML_FR
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon {DOC} ({lesson.get('titleFr')}) : FR {len(old)} -> {len(HTML_FR)} car")

    with open(REG, "r", encoding="utf-8") as fh:
        r = json.load(fh)
    if DOC not in r["hand"]:
        r["hand"].append(DOC)
        with open(REG, "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=2)
        print(f"OK — registre : {len(r['hand'])} entrées ({DOC} ajouté)")
    else:
        print("Registre : déjà présent")


if __name__ == "__main__":
    main()
