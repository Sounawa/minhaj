#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R84 — Fusion des 4 traductions savantes hadith-1es (12929/12945/12948/12953).

1. content/books/hadith-1es.json : htmlFr ← tr-tmp/<id>.html ; titleFr ← titre savant.
2. scripts-translate/savant-registry.json : hand ← += les 4 docIds (GARDE-DOUBLON).
3. Vérification : seule la leçon visée change (diff ligne par ligne).
"""
import difflib
import json
import sys

BOOK = "/home/z/my-project/content/books/hadith-1es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
TMP = "/home/z/my-project/tr-tmp"

TITLES = {
    "12929": "Les dispositions de l’appel à la prière",
    "12945": "Les dispositions de l’appel à la prière en voyage",
    "12948": "Les dispositions de l’ouverture de la prière",
    "12953": "La récitation dans la prière",
}
IDS = sys.argv[1:] or list(TITLES)


def dump(obj, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main() -> None:
    raw_before = open(BOOK, encoding="utf-8").read()
    book = json.loads(raw_before)
    done = []
    for les in book["lessons"]:
        did = str(les.get("docId"))
        if did in IDS:
            if did in done:
                raise SystemExit(f"✗ GARDE-DOUBLON : {did} apparaît deux fois dans le livre")
            html = open(f"{TMP}/{did}.html", encoding="utf-8").read().strip()
            les["htmlFr"] = html
            les["titleFr"] = TITLES[did]
            done.append(did)
    missing = [i for i in IDS if i not in done]
    if missing:
        raise SystemExit(f"✗ docIds introuvables dans le livre : {missing}")
    dump(book, BOOK)

    reg = json.load(open(REG, encoding="utf-8"))
    for i in IDS:
        if i in reg["hand"]:
            raise SystemExit(f"✗ GARDE-DOUBLON : {i} déjà dans le registre hand")
    reg["hand"] = reg["hand"] + IDS
    dump(reg, REG)
    print(f"✓ registre hand = {len(reg['hand'])} (+4) | llm = {len(reg['llm'])} | total = {len(reg['hand']) + len(reg['llm'])}/950")

    # ——— Vérification diff minimal (livre)
    raw_after = open(BOOK, encoding="utf-8").read()
    diff = list(difflib.unified_diff(raw_before.splitlines(), raw_after.splitlines(), lineterm="", n=0))
    changed = [l for l in diff if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    n_html = sum(1 for l in changed if '"htmlFr"' in l)
    n_title = sum(1 for l in changed if '"titleFr"' in l)
    print(f"✓ diff livre : {len(changed)} lignes changées — htmlFr: {n_html} | titleFr: {n_title}")
    n_attendu = len(IDS)
    if len(changed) != 4 * n_attendu or n_html != 2 * n_attendu or n_title != 2 * n_attendu:
        raise SystemExit(f"✗ diff inattendu ({len(changed)} lignes) — inspecter avant commit")
    print("✓ fusion R84 terminée proprement")


if __name__ == "__main__":
    main()
