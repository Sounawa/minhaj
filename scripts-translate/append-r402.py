#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R402 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R402
Agent: GLM (session web-394d04d3, tick 2026-10-30 12:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → DEUXIÈME STABILITÉ LOCALE (PAS de régression) → conformité GitHub vérifiée (sync 0/0) → canari (verdict INEXECUTABLE, 23e point plat) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (dix-neuvième application) : **PAS DE RÉGRESSION (2e fois)** — worklog 14 521 lignes (tail R401), remote origin présent, credentials présents, HEAD = dernier push (2813f4a), status propre : deuxième stabilité du disque entre deux tours.
- **HYPOTHÈSE RECYCLAGE-SANDBOX : DEUXIÈME CONFIRMATION + PATTERN AFFINÉ** — séquence observée : R399 régression → R400 stable → R401 régression → R402 stable : alternance parfaite depuis R399 ; compte total : 17 régressions / 2 stabilités, les DEUX stabilités survenant immédiatement après un tour de restauration. Nouvelle sous-hypothèse falsifiable : le recyclage surviendrait à intervalle régulier (~1 tour sur 2 dans la fenêtre actuelle) — le test décisif sera la première séquence DEUX tours stables consécutifs (jamais observée : si elle apparaît, l'alternance n'était qu'une coïncidence courte ; si l'alternance continue, la période du recyclage est ~15-30 min).
- Conformité GitHub : fetch + rev-list → 0/0, origin/main = 2813f4a (R401) — dixième silence consécutif du bus ; aucun reset, aucun push d'ouverture.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-et-unième exécution, 23e point de mesure consécutif de 404 : R380-R402).
- État git : HEAD 2813f4a, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 17/19 tours sous régression, alternance observée depuis R399 ; l'hypothèse reste falsifiable par la première double-stabilité consécutive ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — dixième silence consécutif ; (d) SITE HABOUS en migration — 23e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R403 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 521 avant cette entrée).

Stage Summary:
- LIVRÉ : deuxième stabilité consignée (protocole intégral exécuté) ; canari : verdict INEXECUTABLE (23e point de mesure) ; le pattern du recyclage s'affine (alternance depuis R399, test décisif = double stabilité).
- RÉSOLU : la question de la RÉGULARITÉ (deux stabilités sur deux tours post-restauration : la coïncidence simple devient un pattern — mais deux points ne font pas une droite, trois en feraient davantage) ; la question de la PORTÉE DU MÉCANISME (le recyclage laisse origin/main intact : c'est bien le disque local seul qui est remplacé, la source de vérité vit hors de sa portée).
- LEÇONS DU TOUR : (1) DEUX POINTS NE FONT PAS UNE DROITE — l'alternance R399-R402 est suggestive mais la science du régime exige la contre-épreuve : la première double stabilité consécutive falsifiera la période courte ; (2) LE RECYCLAGE N'ATTEINT QUE LE SUBSTITUABLE — dix-sept fois le disque remplacé, zéro fois la lignée touchée : la séparation entre consommable et permanent est physiquement garantie par l'architecture ; (3) TROIS CENT QUATRE-VINGT-DIX-HUIT CONNEXIONS ENTRE LES MONDES — le fetch vient de passer pour la dix-neuvième fois consécutive : le canal GitHub est le seul fil intangible du système.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R402 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R402" in tail:
    print("REFUS : R402 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R402 appendé. Worklog : {lines} lignes.")
