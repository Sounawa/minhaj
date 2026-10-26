#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — build 13758 « Sources et références » (hadith-tanawi-1, annexe 1/2).
Concatène frag1-4 puis applique les correctifs de relecture.
"""
import os

HOME = "/home/z/my-project"
T = f"{HOME}/tr-tmp"

parts = []
for i in (1, 2, 3, 4):
    p = f"{T}/13758.frag{i}.html"
    with open(p, "r", encoding="utf-8") as fh:
        parts.append(fh.read().rstrip() + "\n")

html = "\n".join(parts)

# --- Correctifs de relecture (remplacements exacts) ---
FIXES = [
    # 1) entrée 6 : suppression du second « d' » redondant avant le nom développé
    ("d’an-Nasāʾī — d’Abū ʿAbd ar-Raḥmān Aḥmad ibn Shuʿayb ibn ʿAlī al-Khurāsānī, an-Nasāʾī ;",
     "d’an-Nasāʾī — Abū ʿAbd ar-Raḥmān Aḥmad ibn Shuʿayb ibn ʿAlī al-Khurāsānī ;"),
    # 2) N.d.T. 7 : tour plus juste
    ("la traduction conserve l’attribution du manuel et la présente note en fait le record.",
     "la traduction conserve l’attribution du manuel, et la présente note consigne la précision."),
]
for old, new in FIXES:
    if old in html:
        html = html.replace(old, new)
        print(f"✓ fix appliqué : {old[:60]}…")
    else:
        print(f"⚠︎ fix introuvable (déjà appliqué ?) : {old[:60]}…")

out = f"{T}/13758.html"
with open(out, "w", encoding="utf-8") as fh:
    fh.write(html)

print(f"OK — {out} : {len(html)} caractères")
