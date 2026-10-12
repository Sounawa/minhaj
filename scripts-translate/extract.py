#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Extraction du document source AR pour traduction manuelle.

Usage: python3 tr-tmp/extract.py <bookId> <docId>

Produit :
  tr-tmp/<docId>.src.html  — source ARABE (le texte à traduire, autorité)
  tr-tmp/<docId>.gt.html   — baseline GT (AIDE AU DÉCODAGE SEULEMENT,
                             jamais copier : GT-ismes interdits)
Affiche : titres AR/FR officiels, tailles, et le titleFr à reprendre tel quel.
"""
import json
import os
import sys

HOME = "/home/z/my-project"
OUT = f"{HOME}/tr-tmp"


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: extract.py <bookId> <docId>")
        sys.exit(1)
    book_id, doc_id = sys.argv[1], sys.argv[2]
    os.makedirs(OUT, exist_ok=True)
    path = f"{HOME}/content/books/{book_id}.json"
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    found = []
    intro = data.get("intro") or {}
    if str(intro.get("docId")) == doc_id:
        found.append(("intro", intro))
    for l in data.get("lessons", []):
        if str(l.get("docId")) == doc_id:
            found.append(("lesson", l))
    if not found:
        raise SystemExit(f"✗ docId {doc_id} introuvable dans {book_id}")

    doc = found[0][1]
    ar = doc.get("html") or ""
    gt = doc.get("htmlFr") or ""
    with open(f"{OUT}/{doc_id}.src.html", "w", encoding="utf-8") as fh:
        fh.write(ar)
    with open(f"{OUT}/{doc_id}.gt.html", "w", encoding="utf-8") as fh:
        fh.write(gt)
    print(f"OK {book_id}/{doc_id} — {len(found)} emplacement(s)")
    print(f"  titleAr : {doc.get('titleAr')}")
    print(f"  titleFr : {doc.get('titleFr')}  <- reprendre tel quel")
    print(f"  source AR : {len(ar)} car -> tr-tmp/{doc_id}.src.html")
    print(f"  baseline GT : {len(gt)} car -> tr-tmp/{doc_id}.gt.html (decodage seulement)")
    # Aide : index aʿlām du livre (généalogies à sourcer dedans)
    try:
        reg = json.load(open(f"{HOME}/scripts-translate/savant-registry.json"))
    except Exception:
        reg = {}
    for l in data.get("lessons", []):
        t = (l.get("titleFr") or "")
        if "aʿlām" in t and str(l.get("docId")) != doc_id:
            did = str(l.get("docId"))
            done = did in reg.get("hand", []) or did in reg.get("llm", {})
            print(f"  index aʿlām : {did} (traduit : {done}) — sourcer les généalogies dedans")
            break


if __name__ == "__main__":
    main()
