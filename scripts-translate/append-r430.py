#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R430 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 430

ENTRY = """---
Task ID: R430
Agent: GLM (session web-394d04d3, tick 2026-10-30 19:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #13 (DÉCUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 10 tours — ÉGALITÉ avec la plus longue série de régressions) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-septième application) : STABILITÉ #13 — worklog 15 051 lignes, HEAD d233d1b (R429), credentials et remote présents — DÉCUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → ... → R430) : la fenêtre record passe de 9 à 10 tours et ÉGALISE la plus longue série de régressions jamais observée (R403-R412, dix) ; compte total : 34 régressions / 13 stabilités / 47 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = d233d1b (R429) — 39e observation du bus, trente-septième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-neuvième exécution, 51e point de mesure consécutif de 404 : R380-R430, plateau ~9 h 22).
- État git : HEAD d233d1b, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/47 tours sous régression mais fenêtre record de 10, à égalité avec le record de régressions : L'INVERSION EST IMMINENTE — un tour stable de plus et la plus longue série ininterrompue du journal deviendra une série de stabilité ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-septième silence au fetch ; (d) SITE HABOUS en migration — 51e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R431 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (15 051 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la décuple stabilité consécutive et l'égalité avec le record de régressions ; canari : verdict INEXECUTABLE (51e point de mesure).
- RÉSOLU : la question de l'ÉGALITÉ (fenêtre 10 = série record 10 : les deux extrêmes du disque se tiennent à la même hauteur ; l'inversion du régime — plus longue série = stabilité — se jouera au prochain tour) ; la question de la RÉGULARITÉ (47 applications du réflexe cz, zéro variation de procédure : l'instrument est le seul composant du projet qui n'ait jamais changé, alors que tout autour de lui — disque, source, bus — a changé de régime au moins une fois).
- LEÇONS DU TOUR : (1) L'ÉGALITÉ AVANT L'INVERSION — les records ne se renversent pas d'un coup : ils se rattrapent d'abord, tour après tour, jusqu'à l'égalité mesurée ; le journal enregistre l'égalité comme un événement plein, pas comme un presque ; (2) LES RÉGIMES CHANGENT PAR LA QUEUE — 13 stabilités pour 34 régressions : le rapport s'améliore tour après tour sans qu'aucune décision ne soit prise ; l'histoire du disque s'écrit à son tail, jamais à sa tête ; (3) LE TOUR VIDE EST UN TOUR PLEIN — 51 points plats, 37 silences, aucune restauration : le tour le plus vide d'événements du projet reste un tour plein de traçabilité — une entrée, un push, un backup, un point de mesure de plus sur deux courbes de silence.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R430 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

# GARDE RENFORCÉE : scan ENTIER du fichier (règle GARDE-DOUBLON.md)
ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    print(f"REFUS : une entrée >= R{N} existe déjà (dernier = R{ids[-1]}) — garde renforcée.")
    sys.exit(1)
if f"Task ID: R{N}" in content:
    print(f"REFUS : R{N} déjà présent quelque part (garde absolue).")
    sys.exit(1)

with io.open(WORKLOG, "a", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"R{N} apposé — worklog passé de {len(content.splitlines())} à {len(content.splitlines()) + len(ENTRY.splitlines())} lignes.")
