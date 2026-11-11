#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection savante : leçon 11421 (fiqh-1es, leçon imprimée 7 — الغسل وأحكامه).

Le ghusl et ses règles — motif, farāʾiḍ (5), sunan (5), faḍāʾil (7), description en 5 temps.

Hadiths VÉRIFIÉS sunnah.com :
- Bukhārī 168 (bāb التيمن في الوضوء والغسل EXACT) — ʿĀʾisha via Masrūq (chaîne imprimée EXACTE)
- Muslim 317a (bāb صفة غسل الجنابة EXACT) — Maymūna via Ibn ʿAbbās

FIX titleFr : « Le ġusl et ses règles » → « Le ghusl et ses règles » (arti-fact ġ du
corpus, même série que istiñǧāʾ→istinjāʾ de R129 — le corps du corpus emploie gh).

QA : guillemets appariés, 0 apostrophe droite, 0 arabe résiduel hors <em>.
"""

import json

BOOK = "/home/z/my-project/content/books/fiqh-1es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
DOC = "11421"

HTML_FR = open("/home/z/my-project/tr-tmp/11421.fr.html", encoding="utf-8").read()


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
    # FIX arti-fact de translittération dans le titleFr officiel
    if "ġusl" in (lesson.get("titleFr") or ""):
        lesson["titleFr"] = lesson["titleFr"].replace("ġusl", "ghusl")
        print(f"FIX titleFr : ġusl → ghusl ({lesson['titleFr']})")
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
