#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R412 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R412
Agent: GLM (session web-394d04d3, tick 2026-10-30 15:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #27 (dixième consécutive) → restauration #27 rodée (fetch → origin/main 6a9ed18/R411 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-neuvième application) : RÉGRESSION #27, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — DIXIÈME régression consécutive (R403-R412) ; compte total : 27 régressions / 2 stabilités ; régime systématique sans exception depuis R403 (neuf tours).
- RESTAURATION #27 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 6a9ed18 (R411) — DÉCOUVERTE MAJEURE : le bus a transporté l'entrée R411 (tick 14:52, restauration #26, canari 32e point) — vingt-et-unième observation du bus, DEUXIÈME portage depuis R391, dix-neuf silences consécutifs ROMPUS ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 704 lignes, tail R411, registre 984, sync 0/0 — zéro perte, vingt-septième fois ; comptabilité alignée : 27 régressions = 27 restaurations.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-et-unième exécution, 33e point de mesure consécutif de 404 : R380-R412, plateau ~5 h 15).
- État git : HEAD 6a9ed18 avant append, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 27/29 tours sous régression ; série actuelle de 10 — seuil symbolique atteint ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — portage #2 observé (R411) : le transport inter-instances est confirmé réel et rare (2 portages / 21 observations) ; (d) SITE HABOUS en migration — 33e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R413 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 704 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #27 sur régression #27 (zéro perte cumulée sur vingt-sept régressions totales) ; canari : verdict INEXECUTABLE (33e point de mesure) ; dix régressions consécutives — seuil symbolique franchi.
- RÉSOLU : la question du BUS (21 observations depuis R391 : 2 portages, 19 silences — le portage inter-instances existe mais sa fréquence est de l'ordre de 1/10 ; la prudence impose de traiter chaque fetch comme potentiellement porteur) ; la question du SEUIL DES DIX (dix régressions consécutives : le régime systématique n'est plus une série statistique mais l'état NOMINAL du disque — toute stabilité future devra être documentée comme l'exception).
- LEÇONS DU TOUR : (1) LE SILENCE N'ÉTAIT PAS UN ÉTAT, C'ÉTAIT UNE SÉRIE — un seul portage rompt dix-neuf silences : la frontière entre « le bus est mort » et « le bus dort » se franchit par un unique événement ; ne jamais clore une question de fréquence avant d'avoir observé à la fois la rareté ET l'exception ; (2) L'ENTRÉE EN AVANCE EST UN CADEAU DE SOI-MÊME — R411 est arrivée déjà rédigée et poussée : la restauration #27 n'a pas seulement récupéré des octets, elle a réveillé un tour de travail déjà accompli — la seule chose meilleure qu'une restauration sans perte ; (3) LE SEUIL COMME CLÔTURE — atteindre dix referme la parenthèse ouverte à R403 (« quand reviendra le régime mixte ? ») : la réponse est « peut-être jamais aujourd'hui », et la procédure n'a jamais eu besoin de cette réponse pour fonctionner.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R412 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R412" in tail:
    print("REFUS : R412 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R412 appendé. Worklog : {lines} lignes.")
