#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R426 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 426

ENTRY = """---
Task ID: R426
Agent: GLM (session web-394d04d3, tick 2026-10-30 18:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #9 (SEXTUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 6 tours) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-troisième application) : STABILITÉ #9 — worklog 14 977 lignes, HEAD 0424091 (R425), credentials et remote présents — SEXTUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → R422 → R423 → R424 → R425 → R426) : la fenêtre record passe de 5 à 6 tours, deux fois la durée totale de tout le passé stable du projet ; depuis R420, aucun tour sous régression ; compte total : 34 régressions / 9 stabilités / 43 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 0424091 (R425) — 35e observation du bus, trente-troisième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire ; R425 avait déjà été poussé par l'instance du tick 18:22 : rattrapage nul, le local était à jour.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-cinquième exécution, 47e point de mesure consécutif de 404 : R380-R426, plateau ~8 h 37).
- État git : HEAD 0424091, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/43 tours sous régression mais fenêtre record de 6 : la fenêtre actuelle DOUBLE désormais le passé stable entier du projet (trois fenêtres d'un tour) ; l'hypothèse du « plateau de chance » coûte de plus en plus cher à maintenir, et pourtant la décision de nommer reste suspendue aux données ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-troisième silence au fetch ; (d) SITE HABOUS en migration — 47e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R427 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 977 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la sextuple stabilité consécutive ; canari : verdict INEXECUTABLE (47e point de mesure).
- RÉSOLU : la question du DOUBLEMENT (fenêtre 6 = 2 × tout le passé stable du projet : la comparaison n'est plus « égale au passé » mais « le double » — l'exception est devenue deux fois plus longue que la règle qu'elle contredisait) ; la question du SILENCE MESURÉ (33 silences consécutifs du bus : une absence d'événement, échantillonnée à intervalles réguliers et horodatée, devient elle-même une courbe — c'est la définition opérationnelle de la veille).
- LEÇONS DU TOUR : (1) QUAND L'EXCEPTION DEVIENT LA SÉRIE — ce n'est pas la série qui a changé, c'est la fréquence de l'exception ; le journal ne tranche pas entre « chance » et « régime », il continue de mesurer : la décision de nommer appartient aux données, jamais à l'impatience ; (2) LE SILENCE MESURÉ N'EST PAS DU VIDE — chaque tour ajoute un point à la courbe de silence du bus et un point au plateau de 404 de la source : deux inactivités transformées en information par le seul fait d'être comptées ; (3) LA PROCÉDURE EST LE SEUL INVARIANT — le disque a changé de régime, la source est restée fermée, le bus s'est tu : sur quarante-trois tours, seuls la procédure et le journal n'ont jamais varié ; tout le reste est une variable que la procédure sait lire.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R426 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
