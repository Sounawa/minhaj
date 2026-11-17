#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — R715 : inscription au registre savant des documents traduits
faits main dont l'inscription avait été omise (pose par édition du slot,
R693-R712, sans hand-set.py).

Repère les docIds dotés d'un htmlFr non vide mais absents du registre
« hand ∪ llm » de scripts-translate/savant-registry.json, les inscrit au
registre « hand » (même protocole que hand-set.py : verrou mkdir atomique,
purge > 90 s, relecture-fusion, écriture tmp + os.replace, dédoublonnage),
puis revérifie la couverture. NE MODIFIE AUCUN content/books/*.json —
les traductions sont déjà posées dans les JSON ; seul le registre est
complété. Synchronise ensuite le miroir racine savant-registry.json.

Usage : python3 scripts-translate/r715-inscription-manquants.py
"""

import glob
import json
import os
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(BASE, "scripts-translate", "savant-registry.json")
MIROIR = os.path.join(BASE, "savant-registry.json")
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


def registry_ids(reg: dict) -> set:
    ids = {str(x) for x in reg.get("hand", [])}
    llm = reg.get("llm", {})
    if isinstance(llm, dict):
        ids |= {str(k) for k in llm}
    elif isinstance(llm, list):
        ids |= {str(x) for x in llm}
    return ids


def docs_traduits() -> list:
    """[(docId, livre, titre)] des documents dotés d'un htmlFr non vide."""
    out = []
    for p in sorted(glob.glob(os.path.join(BASE, "content", "books", "*.json"))):
        with open(p, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        slug = os.path.basename(p)[:-5]
        intro = data.get("intro") or {}
        if str(intro.get("htmlFr") or "").strip():
            out.append((str(intro.get("docId") or "").strip(), slug,
                        str(intro.get("titleFr") or "")[:60]))
        for l in data.get("lessons", []):
            if str(l.get("htmlFr") or "").strip():
                out.append((str(l.get("docId") or "").strip(), slug,
                            str(l.get("titleFr") or l.get("titleAr") or "")[:60]))
    return out


def main() -> int:
    with open(REGISTRY, "r", encoding="utf-8") as fh:
        reg = json.load(fh)
    ids_avant = registry_ids(reg)
    docs = docs_traduits()
    manquants = []
    vus = set()
    for did, slug, titre in docs:
        if not did:
            print(f"✗ document sans docId : {slug} « {titre} »")
            continue
        if did in vus:
            continue  # docId partagé (intros muqaddima, pdf-2..19, …)
        vus.add(did)
        if did not in ids_avant:
            manquants.append((did, slug, titre))
    print(f"documents traduits (docId unique) : {len(vus)} | "
          f"inscrits au registre : {len(ids_avant)} | "
          f"manquants : {len(manquants)}")
    for did, slug, titre in manquants:
        print(f"  - {did} ({slug}) « {titre} »")

    if not manquants:
        print("registre déjà complet — rien à inscrire.")
    else:
        acquire_lock()
        try:
            with open(REGISTRY, "r", encoding="utf-8") as fh:
                reg = json.load(fh)
            reg.setdefault("hand", [])
            reg.setdefault("llm", {})
            for did, _, _ in manquants:
                if did not in reg["hand"] and did not in reg["llm"]:
                    reg["hand"].append(did)  # ordre d'insertion conservé (convention hand-set.py)
            tmp = REGISTRY + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(reg, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
            os.replace(tmp, REGISTRY)
        finally:
            try:
                os.rmdir(LOCK)
            except OSError:
                pass

    # revérification complète
    with open(REGISTRY, "r", encoding="utf-8") as fh:
        reg2 = json.load(fh)
    ids = registry_ids(reg2)
    encore = [d for d, _, _ in docs if d and d not in ids]
    print(f"registre : hand={len(reg2['hand'])} llm={len(reg2['llm'])} "
          f"union={len(ids)} | documents savants couverts : "
          f"{sum(1 for d, _, _ in docs if d and d in ids)}/{len(docs)}")
    if encore:
        print(f"✗ ENCORE ABSENTS : {encore}")
        return 1
    print("✓ 100 % des documents traduits sont inscrits comme savants.")

    # miroir racine (copie exacte, même octet)
    with open(REGISTRY, "rb") as a, open(MIROIR, "wb") as b:
        b.write(a.read())
    print("miroir racine savant-registry.json synchronisé.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
