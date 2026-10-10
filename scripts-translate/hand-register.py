#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Inscription d'une traduction FAITE MAIN par l'agent au registre savant.

Usage: python3 scripts-translate/hand-register.py <docId> [docId2 ...]

Même discipline de verrou que llm-translate.ts (saveRegistry) :
mkdir atomique + relecture-fusion de l'état disque le plus récent, purge
des verrous périmés > 90 s. Sans cette inscription, le worker LLM
retraduirait le document et écraserait le travail manuel.
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
        print("Usage: hand-register.py <docId> [docId2 ...]")
        sys.exit(1)

    acquire_lock()
    try:
        with open(REGISTRY, "r", encoding="utf-8") as fh:
            reg = json.load(fh)
        reg.setdefault("hand", [])
        reg.setdefault("llm", {})
        added = []
        for doc_id in doc_ids:
            if doc_id not in reg["hand"] and doc_id not in reg["llm"]:
                reg["hand"].append(doc_id)
                added.append(doc_id)
        tmp = REGISTRY + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(reg, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        os.replace(tmp, REGISTRY)
        total = len(reg["hand"]) + len(reg["llm"])
        print(f"✓ registre : +{len(added)} main {added} → {total} savants "
              f"({len(reg['hand'])} main + {len(reg['llm'])} LLM)")
    finally:
        try:
            os.rmdir(LOCK)
        except OSError:
            pass


if __name__ == "__main__":
    main()
