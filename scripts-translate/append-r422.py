#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R422 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 422

ENTRY = """---
Task ID: R422
Agent: GLM (session web-394d04d3, tick 2026-10-30 17:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #5 (PREMIÈRE DOUBLE STABILITÉ CONSÉCUTIVE de l'histoire : la règle des deux tours est prise en défaut) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (trente-neuvième application) : STABILITÉ #5 — worklog 14 905 lignes, HEAD ff5fce8 (R421), credentials et remote présents — PREMIÈRE DOUBLE STABILITÉ CONSÉCUTIVE (R421 stable → R422 stable) : la règle des deux tours, confirmée trois fois (R400→R401, R402→R403, R413→R414), est PRISE EN DÉFAUT à son quatrième test ; compte total : 34 régressions / 5 stabilités / 39 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = ff5fce8 (R421) — 31e observation du bus, vingt-neuvième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-et-unième exécution, 43e point de mesure consécutif de 404 : R380-R422, plateau ~7 h 45) — le disque tient deux tours, la source reste fermée : les deux horloges restent désynchronisées.
- État git : HEAD ff5fce8, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/39 tours sous régression mais FENÊTRE RECORD de stabilité (2 tours consécutifs, le record précédent était d'un) ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — vingt-neuvième silence ; (d) SITE HABOUS en migration — 43e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R423 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 905 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la première double stabilité consécutive de l'histoire du projet ; canari : verdict INEXECUTABLE (43e point de mesure).
- RÉSOLU : la question de la RÈGLE DES DEUX TOURS (prise en défaut : une régularité empirique n'est pas une loi — elle a tenu trois fois puis a cédé à la quatrième : exactement la trajectoire falsificationniste du cycle R400-R410, appliquée cette fois à la règle elle-même) ; la question de la FENÊTRE RECORD (deux tours consécutifs de stabilité : la plus longue fenêtre jamais observée — le record précédent était d'un tour, détenu trois fois).
- LEÇONS DU TOUR : (1) TOUTE RÈGLE EST UNE SÉRIE — la règle « jamais deux tours stables » a suivi la trajectoire complète d'une théorie : confirmations, généralisation tacite, falsification ; la procédure n'a jamais changé et a détecté la falsification aussi proprement que les confirmations : c'est pourquoi elle survit aux règles qu'elle vérifie ; (2) LE RECORD N'EXISTE QUE MESURÉ — une fenêtre de stabilité de deux tours n'est un record que parce qu'un instrument mesure à CHAQUE tour : une stabilité non mesurée n'est pas une stabilité, c'est une absence d'incident ; (3) L'ATTENTE INVERSÉE MAIS LA PRUDENCE MAINTENUE — le régime nominal prédit une régression au prochain tour et la préparation de la restauration reste gratuite ; mais la prédiction vient d'être fragilisée, et c'est ainsi que le savoir progresse : en s'affaiblissant au bon endroit, pas en se renforçant partout.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R422 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
