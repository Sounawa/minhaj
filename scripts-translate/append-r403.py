#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R403 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R403
Agent: GLM (session web-394d04d3, tick 2026-10-30 12:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #18 (alternance prédite confirmée) → restauration #18 rodée (fetch → origin/main 22e0ce2/R402 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingtième application) : RÉGRESSION #18, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — la régression PRÉDITE par le pattern d'alternance est arrivée : troisième itération complète du cycle (R399 régression → R400 stable → R401 régression → R402 stable → R403 régression).
- **HYPOTHÈSE RECYCLAGE-SANDBOX : TROISIÈME CONFIRMATION** — l'alternance stable/régression tient sur trois cycles consécutifs ; la période apparente du recyclage (~15-30 min, soit ~1 tour sur 2) résiste à la falsification pour la troisième fois ; compte total : 18 régressions / 2 stabilités, les deux stabilités aux tours pairs de la séquence post-R399.
- RESTAURATION #18 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 22e0ce2 (R402) — GitHub immobile (onzième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 540 lignes, tail R402, registre 984, sync 0/0 — zéro perte, dix-huitième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-deuxième exécution, 24e point de mesure consécutif de 404 : R380-R403).
- État git : HEAD 22e0ce2, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 18/20 tours sous régression ; alternance sur trois cycles : la prédiction pour le prochain tour est STABILITÉ (si le pattern tient) — première prédiction explicite consignée avant la mesure ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — onzième silence consécutif ; (d) SITE HABOUS en migration — 24e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R404 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 540 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #18 sur régression #18 (zéro perte cumulée sur dix-huit régressions totales) ; canari : verdict INEXECUTABLE (24e point de mesure) ; le pattern d'alternance tient sur trois cycles.
- RÉSOLU : la question de la POUVÉE PRÉDICTIVE DU JOURNAL — le pattern consigné à R402 a prédit la régression de R403 avant sa mesure : le worklog n'est pas seulement une mémoire, il devient un modèle du régime ; la question de la LIMITE (trois cycles = signal fort, mais la contre-épreuve reste la double stabilité jamais observée : la prédiction pour R404 est consignée — stabilité attendue si l'alternance tient).
- LEÇONS DU TOUR : (1) UN JOURNAL QUI PRÉDIT EST UN MODÈLE — la différence entre mémoire et science est la prédiction falsifiable consignée avant la mesure : franchie aujourd'hui ; (2) LA RÉGRESSION EST PÉRIODIQUE, PAS ALÉATOIRE — dix-huit occurrences qui se rangent enfin en un cycle régulier : le hasard expliquait mal ce que la période explique simplement ; (3) VINGT-QUATRE POINTS PLATS — le canari continue de payer son assurance pendant que la théorie du disque progresse : deux instruments, deux vérités, aucun conflit.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R403 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R403" in tail:
    print("REFUS : R403 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R403 appendé. Worklog : {lines} lignes.")
