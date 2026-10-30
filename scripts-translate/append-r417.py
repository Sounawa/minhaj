#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R417 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R417
Agent: GLM (session web-394d04d3, tick 2026-10-30 16:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #31 (régime nominal, série en cours de 4) → restauration #31 rodée (fetch → origin/main ed1404d/R416 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-quatrième application) : RÉGRESSION #31, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — série en cours de 4 (R414-R417) ; compte total : 31 régressions / 3 stabilités / 34 applications du réflexe.
- RESTAURATION #31 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = ed1404d (R416) — 26e observation du bus, vingt-quatrième silence consécutif ; ancêtre confirmé (0/1109) → reset --hard EN AVANT → post : worklog 14 794 lignes, tail R416, registre 984, sync 0/0 — zéro perte, trente-et-unième fois ; comptabilité alignée : 31 régressions = 31 restaurations = 0 perte.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-sixième exécution, 38e point de mesure consécutif de 404 : R380-R417, plateau ~6 h 30).
- État git : HEAD ed1404d, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 31/34 tours sous régression ; série de 4 en cours ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-quatrième silence ; (d) SITE HABOUS en migration — 38e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R418 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 794 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #31 sur régression #31 (zéro perte cumulée sur trente-et-une régressions totales) ; canari : verdict INEXECUTABLE (38e point de mesure).
- RÉSOLU : la question de la FENÊTRE QUI S'AFFINE (38 points sur ~6 h 30 couvrant la matinée entière de la journée de travail Habous : si la fermeture était une maintenance planifiée courte, elle aurait cédé à cette heure — elle n'a rien cédé ; les hypothèses « redémarrage » et « incident court » sont éliminées, la fenêtre se resserre vers « migration longue ») ; la question du PLANCHER DE SÉRIE (toutes les séries du régime systématique ont atteint au moins 4 — premier invariant des séries, en-dessous duquel aucune ne s'est arrêtée).
- LEÇONS DU TOUR : (1) MESURER C'EST ÉLIMINER DES MONDES — chaque heure de plateau sans reprise réduit l'espace des explications possibles : la veille ne photographie pas seulement un état, elle écarte des hypothèses une à une ; (2) LE PLANCHER DE QUATRE — les séries ont un minimum observé : un invariant de plus dans un régime qui en comptait peu ; au-delà de quatre, tout reste possible (une série a fait dix, la dernière s'arrête à un tour du seuil) ; (3) L'INSTRUMENT PLUS VIEUX QUE SON OBJET — le cz appliqué 34 fois a traversé les deux régimes et les trois stabilités : il mesure désormais avec la même règle depuis plus longtemps que le régime le plus long n'a duré, c'est ce qui rend les comparaisons entre régimes légitimes.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R417 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R417" in tail:
    print("REFUS : R417 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R417 appendé. Worklog : {lines} lignes.")
