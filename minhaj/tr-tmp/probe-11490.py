#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe QA: check that key scholarly phrases render in the lesson page."""
import subprocess
import sys

doc = sys.argv[1] if len(sys.argv) > 1 else "11490"
probes = [
    # hadith verification
    "1109b",
    "VÉRIFIÉ MOT À MOT",
    "Ḥarmala b. Yaḥyā",
    "Ibn Wahb",
    "Ibn Shihāb",
    "ʿUrwa b. az-Zubayr",
    "Umm Salama",
    "yuṣbiḥu",
    # Bukhari N.d.T.
    "1991-1992",
    "Mūsā b. Ismāʿīl",
    "Wuhayb",
    "Abū Saʿīd al-Khudrī",
    "ṣammāʾ",
    # verse chips
    "légende imprimée : 183",
    "quiconque d’entre vous est malade ou en voyage",
    "une rançon : la nourriture d’un pauvre",
    "le mois de Ramaḍān au cours duquel le Coran a été descendu",
    "le fil blanc de l’aube du fil noir",
    "décalage de −1 verset",
    "CALIBRATION Baqara",
    "sonde VLM lettre à lettre",
    # matn content
    "soixante pauvres",
    "mudd",
    "quatre relais",
    "mutamattiʿ",
    "liquide prostatique",
    "l’affranchissement d’un esclave",
    "deux mois consécutifs",
    "s’évanouit de nuit",
    # sharh lexique
    "trois lieues",
    "tamattuʿ",
    "hady",
    "manī",
    # analysis
    "avis proche",
    "avis éloigné",
    "croissant de Ramaḍān",
    "sans divergence",
    "particularités de Ramaḍān",
    "la plus grande des afflictions",
    "station nocturne",
    "corrigé (",
    "repentant, le pardon est le choix",
    # istithmār
    "al-Lakhmī",
    "tome 1, page 460",
    "continuation",
    # preparation
    "retraite (",
    "iʿtikāf",
    # structure
    "L’évaluation (",
    "L’exploitation (",
    "La préparation préalable (",
    "La compréhension (",
    "L’extraction des contenus",
]

out = subprocess.run(
    ["agent-browser", "read", "http://localhost:3000/#/livre/fiqh-1es/" + doc],
    capture_output=True,
    text=True,
    timeout=60,
).stdout

ok = 0
miss = []
for p in probes:
    if p in out:
        ok += 1
    else:
        miss.append(p)
print(f"PROBES: {ok}/{len(probes)} OK")
if miss:
    print("MISSES:")
    for m in miss:
        print("  -", m)
