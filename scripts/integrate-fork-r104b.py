#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R499 bis — Ré-intégration des 12 leçons tafsir-3es du fork R104 (branche fork-r104-sauvegarde2)
vers la ligne avancée d24406e. Méthode R499 éprouvée : union sans écrasement,
titleFr du portail côté main PRÉSERVÉ, registre hand étendu des docId uniques.
Fork ids : 599-602, 607-614 (603-606 jamais livrées au fork)."""
import json, subprocess, re, sys

FORK = "fork-r104-sauvegarde2"
IDS = ["pdf-mut23h36-%d" % n for n in (599, 600, 601, 602, 607, 608, 609, 610, 611, 612, 613, 614)]
AR = re.compile(r"[\u0600-\u06FF]")

def show(path):
    r = subprocess.run(["git", "show", "%s:%s" % (FORK, path)], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8")

fork_t3 = json.loads(show("content/books/tafsir-3es.json"))
main_t3 = json.load(open("content/books/tafsir-3es.json"))
reg = json.load(open("scripts-translate/savant-registry.json"))
hand = reg["hand"] if isinstance(reg["hand"], list) else list(reg["hand"].keys())

fork_idx = {l["docId"]: l for l in fork_t3["lessons"]}
main_idx = {l["docId"]: l for l in main_t3["lessons"]}

integres, sautes = [], []
for did in IDS:
    fl = fork_idx.get(did)
    ml = main_idx.get(did)
    if not fl or not ml:
        sautes.append((did, "absent fork/main")); continue
    fh = (fl.get("htmlFr") or "").strip()
    mh = (ml.get("htmlFr") or "").strip()
    if not fh:
        sautes.append((did, "fork vide")); continue
    if mh:
        sautes.append((did, "main déjà rempli — préservé")); continue
    ml["htmlFr"] = fh  # titleFr portail main conservé tel quel
    integres.append(did)

# Caches OCR du fork absents de main (défense anti-rebuild)
caches = 0
for did in integres:
    n = did.rsplit("-", 1)[1]
    p = "content/ocr-cache/pdf-mut23h36-%s.json" % n
    r = subprocess.run(["git", "cat-file", "-e", "HEAD:%s" % p], capture_output=True)
    if r.returncode != 0:
        txt = show(p)
        if txt:
            open(p, "w").write(txt)
            caches += 1

# Registre : hand étendu (ordre numérique) des docIds intégrés
added = 0
for did in integres:
    if did not in hand:
        hand.append(did); added += 1
def key(d):
    m = re.search(r"(\d+)$", d)
    return int(m.group(1)) if m else 0
hand.sort(key=key)
reg["hand"] = hand
json.dump(reg, open("scripts-translate/savant-registry.json", "w"), ensure_ascii=False, indent=1)
json.dump(main_t3, open("content/books/tafsir-3es.json", "w"), ensure_ascii=False, indent=1)

# QA éclair : 0 arabe, 0 apostrophe droite, guillemets appariés sur les 12
fails = []
for did in integres:
    h = main_idx[did]["htmlFr"]
    if AR.search(h): fails.append((did, "arabe"))
    if "'" in h: fails.append((did, "apostrophe droite"))
    if h.count("«") != h.count("»"): fails.append((did, "guillemets"))

json.dump({"fork-only-ids": integres}, open("tr-tmp/fork-only-ids.json", "w"))
print("INTÉGRÉS:", len(integres), integres)
print("SAUTÉS:", sautes)
print("CACHES OCR copiés:", caches)
print("REGISTRE hand:", len(hand), "ajoutés:", added, "llm:", len(reg["llm"]))
print("QA éclair:", "PASS" if not fails else fails)
chars = sum(len(main_idx[d]["htmlFr"]) for d in integres)
print("TOTAL htmlFr intégrés:", chars, "car")
sys.exit(0 if not fails else 1)
