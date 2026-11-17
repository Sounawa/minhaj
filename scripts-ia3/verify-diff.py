#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IA-3 (W1) — vérification indépendante du diff typo : chaque différence entre
HEAD et le livre modifié doit être une substitution autorisée :
  ' → ’ / ʿ / ʾ  (apostrophes classées) ;
  (espaces | &nbsp; | \u00a0 | \u202f)* + [;:!?»]  →  \u202f + ponc ;
  « + espaces  →  «\u202f ;
  doubles espaces → simple.
Usage : python3 scripts-ia3/verify-diff.py --book fiqh-tanawi-3 [--ref HEAD]
"""
import argparse, json, re, subprocess

ap = argparse.ArgumentParser()
ap.add_argument("--book", required=True)
ap.add_argument("--ref", default="HEAD")
args = ap.parse_args()

old_raw = subprocess.run(["git", "show", f"{args.ref}:content/books/{args.book}.json"],
                         capture_output=True, text=True, check=True).stdout
old = json.loads(old_raw)
new = json.load(open(f"content/books/{args.book}.json"))

od = {d["docId"]: d for x in ([old["intro"]] if old.get("intro") else []) + old["lessons"] for d in [x]}
nd = {d["docId"]: d for x in ([new["intro"]] if new.get("intro") else []) + new["lessons"] for d in [x]}
changed = [k for k in od if od[k] != nd[k]]
print("docs modifiés:", changed)

ALLOWED = set("\u2019\u02bf\u02be")
NAR = "\u202f"
bad = 0
for k in changed:
    a, b = od[k]["htmlFr"], nd[k]["htmlFr"]
    stats = {"apos": 0, "narrow": 0, "dbl": 0}
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == "«" and b[j] == "«" and j + 1 < len(b) and b[j + 1] == NAR:
            m = re.match(r"«((?:[ \u00a0\u202f]|&nbsp;)+)", a[i:])
            if m:                                                   # course après « : l'espace fine
                units = re.findall(r"(?:[ \u00a0\u202f]|&nbsp;)", m.group(1))   # passe DEVANT les entités
                rest = "".join(units[1:])                           # (équivalent qa-lesson, entités protégées)
                if b[j + 2:j + 2 + len(rest)] == rest:
                    stats["narrow"] += 1; i += m.end(); j += 2 + len(rest); continue
        if a[i] == b[j]:
            i += 1; j += 1; continue
        if a[i] == "'" and j < len(b) and b[j] in ALLOWED:          # apostrophe classée
            stats["apos"] += 1; i += 1; j += 1; continue
        if (a[i] == "'" and j < len(b) and b[j] == "t"              # bat'an → battan (باتًّا, tāʾ géminé — consigné R714/W17)
                and a[i-3:i] == "bat" and a[i+1:i+3] == "an"):
            stats["apos"] += 1; i += 1; j += 1; continue
        # course d'espaces/entité dans a → \u202f dans b (avant ponc, après «, partout) :
        # b[j]==NNBSP et b[j+1] == le caractère qui suit la course dans a
        if b[j] == NAR:
            m = re.match(r"(?:[ \u00a0\u202f]|&nbsp;)+", a[i:])
            if m and j + 1 < len(b) and b[j + 1] == a[i + m.end()]:
                stats["narrow"] += 1; i += m.end() + 1; j += 2; continue
        if a[i] == " " and i + 1 < len(a) and a[i + 1] == " " and b[j] not in " \u00a0\u202f":
            while i < len(a) and a[i] == " ":                       # doubles espaces → simple
                i += 1
            stats["dbl"] += 1; continue
        bad += 1
        print(f"  DIFF NON AUTORISÉE @{k} i={i}: {a[max(0,i-25):i+25]!r} → {b[max(0,j-25):j+25]!r}")
        i += 1; j += 1
        if bad > 3:
            break
    print(f"  {k}: {stats} | résidu a={len(a)-i} b={len(b)-j}")
print("diffs non autorisées:", bad)
