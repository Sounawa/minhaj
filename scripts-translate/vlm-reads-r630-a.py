#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# R630 — lectures VLM des adjudications jamais lues (leçon 10 uh2, p.57-62), lot A.
# Réutilise les recadrages 600/900/1200/2400 dpi déjà posés par crops-uh2-r623.py
# dans tr-tmp/r623-crops/ (WIP hérité du tick 23:41, claim expiré 16:36 — takeover légitime).
import subprocess, os, json, sys

VLM = "tr-tmp/vlm-read-r616.mjs"
C = "tr-tmp/r623-crops"
OUTD = "tr-tmp/r630"
os.makedirs(OUTD, exist_ok=True)

READS = [
    # (crop, prompt, sortie)
    (f"{C}/ADJ4-p58-mutaba-lugha-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (définitions de mutābaʿa au sens lugawī et au sens istiṣilāḥī, et tout renvoi entre crochets). Ne devine rien : marque [illisible] ce qui ne se lit pas. Pour le renvoi entre crochets, décris chaque chiffre glyphiquement (avant/après la barre oblique).",
     f"{OUTD}/read-ADJ4.txt"),
    (f"{C}/ADJ6-p58-qasira-ibnkhuzayma-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (bas de page : mutābaʿa qāṣira + exemple Ibn Ḫuzayma) avec son renvoi entre crochets. Décris chaque chiffre du renvoi glyphiquement. Ne devine rien.",
     f"{OUTD}/read-ADJ6.txt"),
    (f"{C}/ADJ7-p59-shahid-lugha-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (définition de šāhid au sens de la langue + renvoi Maqāyīs al-luġa). Pour le renvoi entre crochets, décris chaque chiffre glyphiquement (gauche/droite de la barre oblique). Ne devine rien.",
     f"{OUTD}/read-ADJ7.txt"),
    (f"{C}/ADJ9-p59-shahid-manawi-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (šāhid maʿnawī, exemple Buḫārī, et la phrase de clôture de la section). Ne devine rien : marque [illisible] ce qui ne se lit pas.",
     f"{OUTD}/read-ADJ9.txt"),
    (f"{C}/ADJ10-p60-itibar-lugha-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (définition de iʿtibār au sens de la langue + renvoi Maqāyīs al-luġa). Pour le renvoi, décris chaque chiffre glyphiquement. Ne devine rien.",
     f"{OUTD}/read-ADJ10.txt"),
    (f"{C}/ADJ11-p60-iraqi-cite-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (citation de al-ʿIrāqī, début de page). Ne devine rien : marque [illisible] ce qui ne se lit pas.",
     f"{OUTD}/read-ADJ11.txt"),
]

for img, prompt, out in READS:
    if os.path.exists(out) and os.path.getsize(out) > 40:
        print("SKIP (déjà lu):", out)
        continue
    print("READ:", img, "->", out, flush=True)
    r = subprocess.run(["node", VLM, img, prompt, out],
                       capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        print("  ERR:", r.stderr[:300])
    else:
        print("  OK,", os.path.getsize(out), "octets")
print("LOT A TERMINÉ")
