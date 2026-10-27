#!/usr/bin/env python3
"""Recomptage de couverture d'un livre : registre savant (hand ∪ llm) vs JSON du livre.
Règle (u) : la priorité du prochain tour se détermine TOUJOURS par ce recomptage,
JAMAIS par recopie d'une liste dactylographiée du worklog.
Risque (h) : docIds chaînes au JSON du livre, entrées pdfOnly non numériques au
registre → convertir les DEUX côtés en int.
Usage : python3 scripts-translate/comptage-registre.py [bookKey]
"""
import json, sys

BASE = "/home/z/my-project"
BOOK = sys.argv[1] if len(sys.argv) > 1 else "tafsir-tanawi-1"

reg = json.load(open(f"{BASE}/scripts-translate/savant-registry.json"))
book = json.load(open(f"{BASE}/content/books/{BOOK}.json"))

def to_ints(seq):
    out = set()
    for x in seq:
        try:
            out.add(int(x))
        except (TypeError, ValueError):
            pass  # pdfOnly / non numérique → ignoré
    return out

hand = to_ints(reg.get("hand", []))
llm = to_ints(reg.get("llm", []))
covered = hand | llm

docs = book.get("docs", [book.get("intro", {})] + book.get("lessons", []))
lessons = book.get("lessons", [])
intro = book.get("intro", {})

print(f"Livre {BOOK} : {len(lessons)} leçons (+ intro)")
if intro:
    iid = intro.get("docId")
    try:
        tag = "✓" if (iid is not None and int(iid) in covered) else "✗"
    except (TypeError, ValueError):
        tag = "(non num.)"
    print(f"  intro docId={iid} [{tag}]")

todo, done = [], []
for i, les in enumerate(lessons):
    did = les.get("docId")
    try:
        n = int(did)
    except (TypeError, ValueError):
        print(f"  lessons[{i}] docId ILLISIBLE: {did!r}")
        continue
    status = "✓ hand" if n in hand else ("✓ llm" if n in llm else "✗")
    title = les.get("titleFr") or les.get("titleAr", "")
    line = f"  lessons[{i}] {n} [{status}] {title}"
    (done if n in covered else todo).append(line)

print(f"Couverts : {len(done)}/{len(lessons)}  (hand {sum(1 for d in done if 'hand' in d)} + llm {sum(1 for d in done if 'llm' in d)})")
print("\n-- NON COUVERTS (ordre du livre) --")
for line in todo:
    print(line)
if todo:
    nxt = int(todo[0].split("]")[0].strip().split()[-1]) if False else None
    first = todo[0]
    print(f"\n>>> PROCHAINE LEÇON = {first}")
