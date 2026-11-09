#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R88 — Injection du rendu savant dans hadith-1es.json (13004 ou 13005).

Usage: python3 finalize-r88.py 13004

Pour le docId donné :
  - lessons[].titleFr  = titre corrigé (GT-isme rectifié)
  - lessons[].htmlFr   = contenu de tr-tmp/<id>.html
  - savant-registry.json : docId ajouté à « hand » (si absent)
"""
import json
import sys

BOOK = "/home/z/my-project/content/books/hadith-1es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
TMP = "/home/z/my-project/tr-tmp"

TITLES = {
    "13004": "La vertu de la prière en commun",
    "13005": "Les dispositions propres à l’imam et à ceux qui prient derrière lui",
}


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in TITLES:
        sys.exit("Usage: finalize-r88.py 13004|13005")
    did = sys.argv[1]
    htmlFr = open(f"{TMP}/{did}.html", encoding="utf-8").read().strip()

    book = json.load(open(BOOK, encoding="utf-8"))
    hit = None
    for les in book["lessons"]:
        if str(les.get("docId")) == did:
            hit = les
            break
    if hit is None:
        sys.exit(f"✗ docId {did} introuvable dans {BOOK}")
    old_title = hit.get("titleFr")
    old_len = len(hit.get("htmlFr") or "")
    hit["titleFr"] = TITLES[did]
    hit["htmlFr"] = htmlFr
    with open(BOOK, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"✓ {did} injecté — titleFr : « {old_title} » → « {TITLES[did]} » ; htmlFr {old_len} → {len(htmlFr)} car")

    reg = json.load(open(REG, encoding="utf-8"))
    if did not in reg["hand"]:
        reg["hand"].append(did)
        reg["hand"].sort()
        with open(REG, "w", encoding="utf-8") as f:
            json.dump(reg, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"✓ registre : {did} ajouté à hand ({len(reg['hand'])} docs savants)")
    else:
        print(f"• registre : {did} déjà présent (hand = {len(reg['hand'])})")


if __name__ == "__main__":
    main()
