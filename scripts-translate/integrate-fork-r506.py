#!/usr/bin/env python3
"""R506-a : ré-intégration fork R499ter — tafsir-3es 599-602, 607-614 htmlFr fork→main si vide.
titleFr du portail PRÉSERVÉ (jamais écrasé). Registre hand 1010→1022."""
import json, subprocess, sys

FORK_REF = "fork-r505-sauvegarde"
SLOTS = ["599", "600", "601", "602", "607", "608", "609", "610", "611", "612", "613", "614"]

def load_fork_json(path):
    blob = subprocess.run(["git", "show", f"{FORK_REF}:{path}"], capture_output=True, text=True, check=True).stdout
    return json.loads(blob)

def match(docId):
    for s in SLOTS:
        if docId.endswith("-" + s):
            return s
    return None

# 1. tafsir-3es.json : copier htmlFr fork→main si vide
cur = json.load(open("content/books/tafsir-3es.json"))
fork = load_fork_json("content/books/tafsir-3es.json")
fork_by_id = {l["docId"]: l for l in fork.get("lessons", [])}
copied, total_chars = [], 0
for l in cur.get("lessons", []):
    s = match(l.get("docId", ""))
    if not s:
        continue
    hf = str(l.get("htmlFr", "") or "")
    if hf:
        print(f"  {l['docId']}: déjà rempli ({len(hf)} car) — inchangé")
        continue
    src = fork_by_id.get(l["docId"])
    if not src or not str(src.get("htmlFr", "") or "").strip():
        print(f"  ⚠️ {l['docId']}: ABSENT ou vide dans le fork — NON copié")
        continue
    l["htmlFr"] = src["htmlFr"]
    copied.append(l["docId"])
    total_chars += len(src["htmlFr"])
    print(f"  {l['docId']}: copié {len(src['htmlFr'])} car (titleFr portail préservé : {str(l.get('titleFr',''))[:40]})")

json.dump(cur, open("content/books/tafsir-3es.json", "w"), ensure_ascii=False, indent=2)
print(f"tafsir-3es.json : {len(copied)} leçons copiées, {total_chars} caractères")

# 2. registre : ajouter les slots manquants
reg = json.load(open("scripts-translate/savant-registry.json"))
hand = reg.setdefault("hand", [])
existing = set()
for x in hand:
    existing.update(str(x).split("|") if isinstance(x, str) else [str(x)])
added = []
for s in SLOTS:
    slot = f"pdf-mut23h36-{s}"
    present = any(slot in str(x) for x in hand)
    if present:
        print(f"  registre {slot}: déjà présent")
        continue
    hand.append(slot)
    added.append(slot)
json.dump(reg, open("scripts-translate/savant-registry.json", "w"), ensure_ascii=False, indent=2)
print(f"registre : +{len(added)} slots → hand total {len(hand)} (+llm {len(reg.get('llm', {}))})")

# 3. vérification finale
final = json.load(open("content/books/tafsir-3es.json"))
n_ok = sum(1 for l in final.get("lessons", []) if str(l.get("htmlFr", "") or "").strip())
print(f"VÉRIF : tafsir-3es {n_ok}/{len(final.get('lessons', []))} leçons avec htmlFr")
missing = [l["docId"] for l in final.get("lessons", []) if match(l.get("docId", "")) and not str(l.get("htmlFr", "") or "").strip()]
if missing:
    print("⚠️ ENCORE VIDES :", missing)
    sys.exit(1)
print("OK — intégration fork complète")
