#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R86 — Finalisation : injection des rendus savants dans hadith-1es.json
+ correction des titleFr GT-ismes + inscription au registre hand."""
import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"
REG = "/home/z/my-project/scripts-translate/savant-registry.json"
TMP = "/home/z/my-project/tr-tmp"

IDS = ["12986", "12987", "12995", "12998"]
TITLES = {
    "12986": "Les dispositions du sahwe dans la prière (1)",
    "12987": "Les dispositions du sahwe dans la prière — suite",
    "12995": "Les dispositions du vendredi et son étiquette (1)",
    "12998": "Les dispositions du vendredi et son étiquette — suite",
}

book = json.load(open(BOOK, encoding="utf-8"))
done = []
for les in book["lessons"]:
    did = str(les.get("docId"))
    if did not in IDS:
        continue
    html = open(f"{TMP}/{did}.html", encoding="utf-8").read().strip()
    old_gt = len(les.get("htmlFr") or "")
    les["htmlFr"] = html
    old_title = les.get("titleFr")
    les["titleFr"] = TITLES[did]
    done.append(did)
    print(f"✓ {did} : htmlFr {old_gt} → {len(html)} car | titleFr «{old_title}» → «{TITLES[did]}»")

assert set(done) == set(IDS), f"absents du livre : {sorted(set(IDS) - set(done))}"
with open(BOOK, "w", encoding="utf-8") as f:
    json.dump(book, f, ensure_ascii=False, indent=2)
print("book mis à jour")

reg = json.load(open(REG, encoding="utf-8"))
hand = reg["hand"]
added = 0
for did in IDS:
    if did not in hand:
        hand.append(did)
        added += 1
with open(REG, "w", encoding="utf-8") as f:
    json.dump(reg, f, ensure_ascii=False, indent=2)
print(f"registre hand : +{added} → {len(hand)} entrées")
