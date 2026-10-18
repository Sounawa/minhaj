#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Promotion LLM→main au registre savant (pour les upgrades LLM→main).

Usage: python3 scripts-translate/promote-llm.py <docId> [docId2 ...]

- Déplace chaque docId de reg["llm"] vers reg["hand"] (même discipline de
  verrou que hand-register.py : mkdir atomique + purge > 90 s).
- Idempotent : un docId déjà en main est ignoré ; absent des deux → ajouté
  à main (cas d'une leçon jamais LLM).
"""

import json
import os
import sys
import time

REGISTRY = "/home/z/my-project/scripts-translate/savant-registry.json"
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


def main() -> None:
    doc_ids = [a for a in sys.argv[1:] if a.strip()]
    if not doc_ids:
        print("Usage: promote-llm.py <docId> [docId2 ...]")
        sys.exit(1)

    acquire_lock()
    try:
        with open(REGISTRY, "r", encoding="utf-8") as fh:
            reg = json.load(fh)
        reg.setdefault("hand", [])
        reg.setdefault("llm", {})
        promoted, added = [], []
        for doc_id in doc_ids:
            if doc_id in reg["llm"]:
                del reg["llm"][doc_id]
                if doc_id not in reg["hand"]:
                    reg["hand"].append(doc_id)
                promoted.append(doc_id)
            elif doc_id not in reg["hand"]:
                reg["hand"].append(doc_id)
                added.append(doc_id)
        tmp = REGISTRY + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(reg, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        os.replace(tmp, REGISTRY)
        total = len(reg["hand"]) + len(reg["llm"])
        print(f"✓ promotion LLM→main : {promoted} (ajouts purs : {added}) → "
              f"{total} savants ({len(reg['hand'])} main + {len(reg['llm'])} LLM)")
    finally:
        try:
            os.rmdir(LOCK)
        except OSError:
            pass


if __name__ == "__main__":
    main()
