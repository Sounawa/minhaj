#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R90 — Injection du rendu savant dans hadith-1es.json (13014).

Usage: python3 finalize-r90.py 13014

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
    "13014": "La présentation du livre",
}


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in TITLES:
        sys.exit("Usage: finalize-r90.py 13014")
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
    print(f"✓ {did} injecté (leçon) — titleFr : « {old_title} » → « {TITLES[did]} » ; htmlFr {old_len} → {len(htmlFr)} car")

    # Jumeaux (même docId sur intro + leçons — constat R90, getDoc résout
    # l'intro d'abord : sans synchronisation, le lecteur afficherait encore
    # l'ancienne version R81 de l'intro, titre GT-isme compris).
    intro = book.get("intro")
    if intro is not None and str(intro.get("docId")) == did:
        old_i_title = intro.get("titleFr")
        old_i_len = len(intro.get("htmlFr") or "")
        intro["titleFr"] = TITLES[did]
        intro["htmlFr"] = htmlFr
        print(f"✓ {did} jumeau intro synchronisé — titleFr : « {old_i_title} » → « {TITLES[did]} » ; htmlFr {old_i_len} → {len(htmlFr)} car")

    with open(BOOK, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
        f.write("\n")

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
