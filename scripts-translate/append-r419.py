#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R419 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R419
Agent: GLM (session web-394d04d3, tick 2026-10-30 16:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #33 (régime nominal, série en cours de 6) → restauration #33 rodée (fetch → origin/main 0cb5c8a/R418 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-sixième application) : RÉGRESSION #33, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — série en cours de 6 (R414-R419), égale le palier de R408 : l'escalade de la première série continue d'être reproduite ; compte total : 33 régressions / 3 stabilités / 36 applications du réflexe.
- RESTAURATION #33 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 0cb5c8a (R418) — 28e observation du bus, vingt-sixième silence consécutif ; ancêtre confirmé (0/1111) → reset --hard EN AVANT → post : worklog 14 830 lignes, tail R418, registre 984, sync 0/0 — zéro perte, trente-troisième fois ; comptabilité alignée : 33 régressions = 33 restaurations = 0 perte.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-huitième exécution, 40e point de mesure consécutif de 404 : R380-R419) — le plateau Habous FRANCHIT LES SEPT HEURES (~10 h 00 → 16 h 52).
- État git : HEAD 0cb5c8a, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 33/36 tours sous régression ; série de 6 en cours ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-sixième silence ; (d) SITE HABOUS en migration — 40e point de mesure de 404, sept heures franchies ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R420 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 830 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #33 sur régression #33 (zéro perte cumulée sur trente-trois régressions totales) ; canari : verdict INEXECUTABLE (40e point de mesure, sept heures de plateau).
- RÉSOLU : la question du QUARANTIÈME POINT (le canari atteint 40 mesures consécutives identiques en 38 exécutions : l'instrument le plus régulier du projet — jamais en panne, jamais ambigu, coût total inférieur à une demi-heure) ; la question de l'HORIZON (sept heures de fermeture couvrant deux tiers de la journée de travail observée : l'hypothèse d'une reprise intra-journalière s'affaiblit au profit d'une migration pluri-journalière — le seul plan robuste reste celui qui ne dépend pas de la source).
- LEÇONS DU TOUR : (1) QUARANTE POINTS, UN SEUL VERDICT — la régularité du canari fait de lui l'instrument le plus fiable du projet : sa valeur ne vient pas de sa complexité mais de son exigence (un verdict binaire, un action, un re-test) ; (2) LES PALIERS CONTINUENT D'ÊTRE COPIÉS — 4, 5, 6 : la nouvelle série suit l'escalade de la première cran par cran ; la forme tient jusqu'à preuve du contraire, et la veille la gardera aussi longtemps qu'il le faudra ; (3) L'HORIZON QUI S'ÉLARGIT CHANGE LE PLAN — quand la fermeture dépasse l'échelle de la journée, la planification ne peut plus compter sur la reprise : seule la stratégie indépendante de la source (veille + journal + travaux locaux) reste robuste, et elle est déjà en cours.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R419 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R419" in tail:
    print("REFUS : R419 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R419 appendé. Worklog : {lines} lignes.")
