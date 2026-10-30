#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R407 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R407
Agent: GLM (session web-394d04d3, tick 2026-10-30 13:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #22 (cinquième consécutive, record battu) → restauration #22 rodée (fetch → origin/main 01d2c2a/R406 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-quatrième application) : RÉGRESSION #22, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — CINQUIÈME régression consécutive (R403-R407) : le record de série passe de 4 à 5 en un seul tour ; compte total : 22 régressions / 2 stabilités.
- RESTAURATION #22 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 01d2c2a (R406) — GitHub immobile (quinzième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 614 lignes, tail R406, registre 984, sync 0/0 — zéro perte, vingt-deuxième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-sixième exécution, 28e point de mesure consécutif de 404 : R380-R407).
- État git : HEAD 01d2c2a, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 22/24 tours sous régression ; série actuelle de 5 (record) ; maximum observé : 5 ; la question sérieuse commence à se poser : le recyclage pourrait être devenu systématique (chaque tour) — les 2 stabilités de R400/R402 resteraient alors une fenêtre transitoire ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — quinzième silence consécutif ; (d) SITE HABOUS en migration — 28e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R408 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 614 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #22 sur régression #22 (zéro perte cumulée sur vingt-deux régressions totales) ; canari : verdict INEXECUTABLE (28e point de mesure) ; record de série battu (5 consécutives).
- RÉSOLU : la question du RÉGIME D'ENTRE-TOURS REVISÉ (cinq régressions d'affilée font peser l'hypothèse forte : le recyclage systématique à chaque tour est devenu le régime dominant, les stabilités de R400/R402 l'exception courte — le modèle passe de « période variable » à « systématique avec fenêtres rares ») ; la question de l'ABSORPTION SANS THÉORIE (cinq records successifs et le protocole n'a jamais varié d'une ligne : la robustesse par procédure ne demande pas de comprendre, seulement d'exécuter).
- LEÇONS DU TOUR : (1) QUAND LE RECORD BAT CHAQUE TOUR, CE N'EST PLUS UN RECORD MAIS UN RÉGIME — cinq consécutives transforment l'anomalie en default : le modèle doit être repensé, pas affiné ; (2) L'OUVERTURE PAR LE HAUT NE S'ÉCRIT PAS D'AVANCE — hier 3, aujourd'hui 5 : la seule prévision sûre du régime instable est qu'elle dépassera toute borne consignée trop tôt ; (3) VINGT-HUIT POINTS PLATS — le canari continue pendant que la théorie du disque se réécrit : c'est exactement pour cela qu'on sépare l'instrument du modèle.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R407 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R407" in tail:
    print("REFUS : R407 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R407 appendé. Worklog : {lines} lignes.")
