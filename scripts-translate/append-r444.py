#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — append worklog R444 (garde renforcée GARDE-DOUBLON.md) :
balayer le FICHIER ENTIER pour le dernier `Task ID: R<N>`, refuser si
le dernier ID >= 444 ; append atomique (tmp + os.replace)."""
import os
import re
import sys

HOME = "/home/z/my-project"
WL = f"{HOME}/worklog.md"
ENTRY = f"{HOME}/scripts-translate/tr-tmp/entry-r444.md"
N = 444

content = open(WL, encoding="utf-8").read()
ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    print(f"REFUS : une entrée >= R{N} existe déjà (dernier = R{ids[-1]}).")
    sys.exit(1)

entry = open(ENTRY, encoding="utf-8").read()
if not entry.startswith("\n---\n"):
    entry = "\n---\n" + entry.lstrip("\n")

new = content.rstrip("\n") + "\n" + entry
if not new.endswith("\n"):
    new += "\n"

tmp = WL + ".tmp"
with open(tmp, "w", encoding="utf-8") as fh:
    fh.write(new)
os.replace(tmp, WL)

# mesure post-append
fresh = open(WL, encoding="utf-8").read()
ids2 = re.findall(r"Task ID: R(\d+)", fresh)
lines = fresh.count("\n") + 1
print(f"OK : entrée R{N} apposée (dernier ID = R{ids2[-1]}) ; worklog = {lines} lignes, {len(fresh)} caractères.")
