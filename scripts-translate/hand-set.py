#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Injection d'une traduction FAITE MAIN dans le JSON du livre + registre.

Usage: python3 scripts-translate/hand-set.py <bookId> <docId> <fichier.html>

- Met à jour lesson.htmlFr (ou intro.htmlFr) pour TOUS les lessons portant ce
  docId (le corpus contient des docId dupliqués par endroits).
- Verrou registre identique à hand-register.py / llm-translate.ts (mkdir
  atomique, purge > 90 s), relecture-fusion de l'état disque le plus récent.
- Écriture livre : read-fresh → set → tmp + os.replace (atomique).
- Inscription au registre « hand » dans la même section critique.
"""

import json
import os
import sys
import time

HOME = "/home/z/my-project"
REGISTRY = f"{HOME}/scripts-translate/savant-registry.json"
LOCK = REGISTRY + ".lock"


def purge_stale_lock() -> None:
    try:
        age = time.time() - os.path.getmtime(LOCK)
        if age > 90:
            os.rmdir(LOCK)
            print(f"⚠︎ verrou périmé ({age:.0f} s) purgé")
    except OSError:
        pass


def acquire_lock() -> None:
    purge_stale_lock()
    for _ in range(40):
        try:
            os.mkdir(LOCK)
            return
        except OSError:
            time.sleep(0.25)
    raise RuntimeError("verrou registre occupé après 10 s")


def set_book_doc(book_id: str, doc_id: str, html_fr: str, force: bool = False) -> int:
    """Écrit htmlFr pour intro et/ou lessons portant docId. Retourne le nb d'écrits.

    GARDE-DOUBLON (R622-correctif) : si une htmlFr NON VIDE existe déjà pour ce
    docId et diffère de la nouvelle, REFUS (leçon déjà livrie par un autre
    ouvrier) sauf --force (reprise explicite) ou contenu identique
    (re-pose idempotente). Prévient l'écrasement d'une livraison commise."""
    path = f"{HOME}/content/books/{book_id}.json"
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    n = 0
    intro = data.get("intro") or {}
    if str(intro.get("docId")) == doc_id:
        old = str(intro.get("htmlFr") or "").strip()
        if old and old != html_fr and not force:
            raise SystemExit(
                f"✗ GARDE-DOUBLON : {book_id}/{doc_id} possède déjà une htmlFr "
                f"livrée ({len(old)} car) différente de la nouvelle "
                f"({len(html_fr)} car) — livrie par un autre ouvrier. "
                f"Passe --force uniquement en reprise documentée.")
        intro["htmlFr"] = html_fr
        data["intro"] = intro
        n += 1
    for l in data.get("lessons", []):
        if str(l.get("docId")) == doc_id:
            old = str(l.get("htmlFr") or "").strip()
            if old and old != html_fr and not force:
                raise SystemExit(
                    f"✗ GARDE-DOUBLON : {book_id}/{doc_id} possède déjà une "
                    f"htmlFr livrée ({len(old)} car) différente de la nouvelle "
                    f"({len(html_fr)} car) — livrie par un autre ouvrier. "
                    f"Passe --force uniquement en reprise documentée.")
            l["htmlFr"] = html_fr
            n += 1
    if n == 0:
        raise SystemExit(f"✗ docId {doc_id} introuvable dans {book_id}")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, path)
    return n


def register_hand(doc_id: str, title: str) -> int:
    with open(REGISTRY, "r", encoding="utf-8") as fh:
        reg = json.load(fh)
    reg.setdefault("hand", [])
    reg.setdefault("llm", {})
    if doc_id not in reg["hand"] and doc_id not in reg["llm"]:
        reg["hand"].append(doc_id)
    tmp = REGISTRY + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(reg, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, REGISTRY)
    return len(reg["hand"]) + len(reg["llm"])


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--force"]
    force = "--force" in sys.argv
    if len(args) != 3:
        print("Usage: hand-set.py <bookId> <docId> <fichier.html> [--force]")
        sys.exit(1)
    book_id, doc_id, src = args
    with open(src, "r", encoding="utf-8") as fh:
        html_fr = fh.read().strip()

    n = set_book_doc(book_id, doc_id, html_fr, force=force)
    acquire_lock()
    try:
        total = register_hand(doc_id, book_id)
    finally:
        try:
            os.rmdir(LOCK)
        except OSError:
            pass
    print(f"✓ {book_id}/{doc_id} : {n} emplacement(s) htmlFr écrit(s), "
          f"{len(html_fr)} car FR — registre → {total} savants")


if __name__ == "__main__":
    main()
