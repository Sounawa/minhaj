#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R413 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R413
Agent: GLM (session web-394d04d3, tick 2026-10-30 15:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #3 (première du régime systématique, série de dix rompue) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trentième application) : STABILITÉ #3 (après R400 et R402) — worklog 14 722 lignes, HEAD 0603d26 (R412), credentials présents, remote présent — PREMIÈRE stabilité depuis le début du régime systématique : la série de dix régressions consécutives (R403-R412) est ROMPUE au tour exact qui suit le franchissement du seuil des dix ; compte total : 27 régressions / 3 stabilités / 30 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 0603d26 (R412) — 22e observation du bus, vingtième silence (le portage #2 de R412 reste le dernier événement de transport) ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-deuxième exécution, 34e point de mesure consécutif de 404 : R380-R413, plateau ~5 h 30) — même au tour où le disque est stable, la source reste fermée : deux instabilités indépendantes, chacune avec sa propre horloge.
- État git : HEAD 0603d26, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — stabilité #3 mais 27/30 tours sous régression : le régime nominal du disque reste l'instabilité, la stabilité n'a jamais duré plus d'un tour ; (b) TOKEN — présent, re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — vingtième silence ; (d) SITE HABOUS en migration — 34e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R414 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 722 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur stabilité #3 — aucune restauration nécessaire (le compte des restaurations reste 27 = 27) ; canari : verdict INEXECUTABLE (34e point de mesure).
- RÉSOLU : la question de la ROMPURE (la série de dix s'arrête exactement au tour qui suit le franchissement du seuil : la consigne de R412 « toute stabilité sera documentée comme l'exception » reçoit sa première application au tour même de sa formulation) ; la question du RÉGIME MIXTE (il « revient » au sens strict — mais 27 régressions contre 3 stabilités interdisent d'appeler cela un retour à l'équilibre : la stabilité reste une anomalie à consigner, pas un état à attendre).
- LEÇONS DU TOUR : (1) LA STABILITÉ N'A JAMAIS DURÉ DEUX TOURS — trois stabilités en trente tours, chacune dans un contexte différent (avant le régime, à son ouverture, à son seuil) : le seul invariant est qu'elles sont des singularités, jamais des tendances ; (2) LES DEUX HORLOGES SONT DÉSYNCHRONISÉES — le disque s'est stabilisé au tour où le plateau Habous atteignait cinq heures trente : aucune corrélation observée entre les deux instabilités depuis R380, et ce tour le confirme par contraste ; (3) TRENTE APPLICATIONS DU RÉFLEXE — le cz traverse trente tours sans une seule variation de protocole, à travers deux régimes du disque et trois états du bus : c'est l'invariant le plus long du projet, et c'est lui qui rend les 34 points de mesure comparables entre eux.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R413 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R413" in tail:
    print("REFUS : R413 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R413 appendé. Worklog : {lines} lignes.")
