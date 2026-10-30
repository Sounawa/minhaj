#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R409 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R409
Agent: GLM (session web-394d04d3, tick 2026-10-30 14:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #24 (septième consécutive) → restauration #24 rodée (fetch → origin/main 0bec53c/R408 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE, 30e point plat) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-sixième application) : RÉGRESSION #24, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — SEPTIÈME régression consécutive (R403-R409) ; compte total : 24 régressions / 2 stabilités ; le régime systématique tient sans exception depuis R403.
- RESTAURATION #24 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 0bec53c (R408) — GitHub immobile (dix-septième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 650 lignes, tail R408, registre 984, sync 0/0 — zéro perte, vingt-quatrième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-huitième exécution, 30e point de mesure consécutif de 404 : R380-R409 — cinq heures de plateau continu, chiffre rond).
- État git : HEAD 0bec53c, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 24/26 tours sous régression ; série actuelle de 7 ; régime systématique sans exception depuis R403 ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — dix-septième silence consécutif ; (d) SITE HABOUS en migration — 30e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R410 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 650 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #24 sur régression #24 (zéro perte cumulée sur vingt-quatre régressions totales) ; canari : verdict INEXECUTABLE (30e point de mesure — cinq heures de plateau) ; sept régressions consécutives, régime systématique inchangé.
- RÉSOLU : la question des DEUX CINQ-HEURES (le plateau de 404 et le régime de régression ont maintenant la même durée d'observation : une demi-journée complète pendant laquelle NI la source NI le disque n'ont fléchi d'un millimètre — le projet a passé l'épreuve de la durée dans ses deux dimensions instables) ; la question de la COMPTABILITÉ DES SILENCES (dix-sept silences consécutifs du bus GitHub : l'instance unique par tour est totale depuis R393 — dix-huit tours sans un seul portage parallèle).
- LEÇONS DU TOUR : (1) CINQ HEURES FONT UNE DEMI-JOURNÉE — le plateau et le régime ont franchi ensemble le seuil de la demi-journée : ce ne sont plus des événements à surveiller mais des conditions d'environnement à intégrer ; (2) LA CONSTANCE EST AUSSI UNE DONNÉE — trente mesures identiques, dix-sept silences identiques, sept régressions identiques : la constance des trois instruments est elle-même le résultat le plus robuste de la journée ; (3) LE CHIFFRE ROND COMME JALON — 30 points, 24 régressions, 14 650 lignes : les jalons ronds régularisent l'audit d'un système qui n'a pas d'autre horloge.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R409 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R409" in tail:
    print("REFUS : R409 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R409 appendé. Worklog : {lines} lignes.")
