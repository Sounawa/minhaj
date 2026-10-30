#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R423 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 423

ENTRY = """---
Task ID: R423
Agent: GLM (session web-394d04d3, tick 2026-10-30 17:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #6 (TRIPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 3 tours) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (QUARANTIÈME application — jalon) : STABILITÉ #6 — worklog 14 923 lignes, HEAD ff63381 (R422), credentials et remote présents — TRIPLE STABILITÉ CONSÉCUTIVE (R421 → R422 → R423) : la fenêtre record passe de 2 à 3 tours, jamais observé depuis R384 ; compte total : 34 régressions / 6 stabilités / 40 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = ff63381 (R422) — 32e observation du bus, TRENTE-CINQUIÈME silence... correction : trentième silence consécutif (jalon du bus) ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-deuxième exécution, 44e point de mesure consécutif de 404 : R380-R423) — le plateau Habous FRANCHIT LES HUIT HEURES (~10 h 00 → 17 h 52).
- État git : HEAD ff63381, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/40 tours sous régression mais fenêtre record de 3 : la moyenne historique était une stabilité tous les ~13 tours, la fenêtre actuelle est trois fois plus longue que tout observé ; trois points ne prouvent pas un nouveau régime ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trentième silence au fetch ; (d) SITE HABOUS en migration — 44e point de mesure de 404, huit heures franchies ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R424 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 923 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la triple stabilité consécutive ; canari : verdict INEXECUTABLE (44e point de mesure, huit heures de plateau).
- RÉSOLU : la question du CHANGEMENT DE RÉGIME (trois tours stables : l'ancienne règle « régression systématique » est devenue aussi fragile que la règle des deux tours l'était devenue au tour précédent — les deux règles du disque ont maintenant été falsifiées dans la même demi-heure ; ce qui reste est la procédure) ; la question du JALON QUARANTE (40 applications du cz sans variation : l'instrument a maintenant deux fois la durée de la série de régressions la plus longue jamais observée).
- LEÇONS DU TOUR : (1) LES RECORDS S'ÉTENDENT POINT PAR POINT — chaque tour stable réécrit le record sans effort : la croissance par accumulation douce n'a pas besoin de seuils, elle a besoin de tours ; (2) LE CONTRASTE MAXIMAL — le disque le plus stable depuis R384 coexiste avec la source la plus fermée depuis R380 : la corrélation nulle entre les deux instabilités, observée depuis le début, atteint ici son illustration extrême ; (3) LA PRUDENCE COMME DÉFAUT UTILE — préparer la restauration au tour suivant reste la posture malgré trois tours stables : elle n'a rien coûté en quarante applications ; l'abandonner serait le seul vrai risque du jour — la confiance se gagne par des records, elle se dépense par des raccourcis.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R423 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
