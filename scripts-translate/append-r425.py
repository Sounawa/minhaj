#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R425 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 425

ENTRY = """---
Task ID: R425
Agent: GLM (session web-394d04d3, tick 2026-10-30 18:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #8 (QUINTUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 5 tours) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-deuxième application) : STABILITÉ #8 — worklog 14 959 lignes, HEAD 446a193 (R424), credentials et remote présents — QUINTUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → R422 → R423 → R424 → R425) : la fenêtre record passe de 4 à 5 tours, premier jalon rond de la fenêtre ; depuis R420, aucun tour sous régression ; compte total : 34 régressions / 8 stabilités / 42 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 446a193 (R424) — 34e observation du bus, trente-deuxième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-quatrième exécution, 46e point de mesure consécutif de 404 : R380-R425, plateau ~8 h 30).
- État git : HEAD 446a193, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/42 tours sous régression mais fenêtre record de 5 : elle dépasse de deux tiers la durée totale du passé stable du projet ; la question « plateau de chance » s'affaiblit avec chaque tour ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-deuxième silence ; (d) SITE HABOUS en migration — 46e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R426 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 959 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la quintuple stabilité consécutive ; canari : verdict INEXECUTABLE (46e point de mesure).
- RÉSOLU : la question de la DURÉE RELATIVE (5 tours : la fenêtre dépasse de deux tiers tout le passé stable du projet — chaque tour supplémentaire rend l'hypothèse du « hasard » plus coûteuse que celle du régime ; le seuil symbolique des cinq est franchi sans cérémonie) ; la question de la PAUSE GÉNÉRALE (stabilité du disque + silence du bus = trente-deux tours sans aucun événement externe : l'état du projet est une pause où le métronome de 15 minutes est le seul battement).
- LEÇONS DU TOUR : (1) LES JALONS ARRIVENT DANS LES DEUX SENS — cinq tours stables comme dix régressions : le journal les enregistre de la même plume, sans emphase et sans dédain ; c'est la symétrie du compte qui fait l'honnêteté de la mesure ; (2) LA QUESTION CHANGE DE FORME — on ne demande plus « quand la régression reviendra-t-elle » mais « quand la fenêtre se fermera-t-elle, et à quel prix » ; la bonne question est celle qui prépare les deux réponses ; (3) LE MÉTRONOME DANS LA PAUSE — disque stable, bus silencieux, source fermée : trois inactivités superposées, et pourtant chaque tour livre une entrée, un push, un backup ; l'activité du projet ne vient plus d'aucun de ses environnements, elle est auto-portée par la procédure.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R425 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R{N} appendé sous garde renforcée. Worklog : {lines} lignes.")
