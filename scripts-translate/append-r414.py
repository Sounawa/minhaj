#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R414 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R414
Agent: GLM (session web-394d04d3, tick 2026-10-30 15:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #28 (retour au régime nominal, la stabilité #3 n'a pas duré deux tours) → restauration #28 rodée (fetch → origin/main f86a4fb/R413 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-et-unième application) : RÉGRESSION #28, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — retour au régime nominal au tour qui suit la stabilité #3 : la règle empirique « la stabilité n'a jamais duré deux tours » reçoit sa TROISIÈME confirmation (R400 → régression à R401 ; R402 → régression à R403 ; R413 → régression à R414) ; compte total : 28 régressions / 3 stabilités / 31 applications.
- RESTAURATION #28 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = f86a4fb (R413) — 23e observation du bus, vingt-et-unième silence consécutif ; ancêtre confirmé (0/1106) → reset --hard EN AVANT → post : worklog 14 740 lignes, tail R413, registre 984, sync 0/0 — zéro perte, vingt-huitième fois ; comptabilité alignée : 28 régressions = 28 restaurations.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-troisième exécution, 35e point de mesure consécutif de 404 : R380-R414, plateau ~5 h 45).
- État git : HEAD f86a4fb, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 28/31 tours sous régression ; nouvelle série ouverte (1 en cours) depuis la rompure de la série des dix ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-et-unième silence ; (d) SITE HABOUS en migration — 35e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R415 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 740 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #28 sur régression #28 (zéro perte cumulée sur vingt-huit régressions totales) ; canari : verdict INEXECUTABLE (35e point de mesure).
- RÉSOLU : la question de la RÈGLE DES DEUX TOURS (la stabilité #3 n'a pas survécu à son tour : trois stabilités observées, zéro qui ait duré — la régularité négative devient assez forte pour servir de référence opérationnelle : après tout tour stable, préparer la restauration au suivant) ; la question du RÉGIME NOMINAL (une seule fenêtre stable sur onze tours depuis R403 : la régression reste l'état par défaut du disque, la stabilité une singularité).
- LEÇONS DU TOUR : (1) APRÈS UNE STABILITÉ, PRÉPARER LA RESTAURATION — lire le régime nominal n'est pas pessimisme mais opérationnalisation : une prédiction fiable transformée en préparation permanente ne coûte rien au tour où elle se vérifie ; (2) LES TROIS STABILITÉS N'ONT QU'UN POINT COMMUN : LEUR DURÉE — R400, R402, R413 : une fenêtre chacune, jamais deux ; une régularité de l'absence est aussi une donnée mesurable ; (3) LE CYCLE COMPLET EN UNE MINUTE — la restauration #28 s'exécute à la vitesse d'une routine : la procédure a absorbé l'instabilité au point qu'elle ne coûte plus qu'une fraction du tour, c'est la vraie victoire sur le régime.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R414 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R414" in tail:
    print("REFUS : R414 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R414 appendé. Worklog : {lines} lignes.")
