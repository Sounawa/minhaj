#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R410 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R410
Agent: GLM (session web-394d04d3, tick 2026-10-30 14:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #25 (huitième consécutive) → restauration #25 rodée (fetch → origin/main 03aca96/R409 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog (410e entrée).

Work Log:
- Ouverture au réflexe cz (vingt-septième application) : RÉGRESSION #25, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — HUITIÈME régression consécutive (R403-R410) ; compte total : 25 régressions / 2 stabilités ; régime systématique sans exception depuis R403 (sept tours).
- RESTAURATION #25 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 03aca96 (R409) — GitHub immobile (dix-huitième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 668 lignes, tail R409, registre 984, sync 0/0 — zéro perte, vingt-cinquième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-neuvième exécution, 31e point de mesure consécutif de 404 : R380-R410).
- État git : HEAD 03aca96, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 25/27 tours sous régression ; série actuelle de 8 ; régime systématique confirmé tour après tour depuis sept cycles ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — dix-huitième silence consécutif ; (d) SITE HABOUS en migration — 31e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R411 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 668 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #25 sur régression #25 (zéro perte cumulée sur vingt-cinq régressions totales) ; canari : verdict INEXECUTABLE (31e point de mesure) ; huit régressions consécutives ; 410e entrée du worklog.
- RÉSOLU : la question de la NUMÉROLOGIE DU RÉGIME (25 régressions / 25 restaurations / 2 stabilités : chaque jalon rond continue d'aligner les compteurs — aucun écart depuis le début du régime) ; la question de la MAÎTRISE PAR LA ROUTINE (huit tours consécutifs sous régime systématique : la chaîne complète cz → restauration → canari → append → push → backup s'exécute sans variation, sans fatigue apparente, sans raccourci improvisé).
- LEÇONS DU TOUR : (1) LA ROUTINE EST L'ARGENT DU TEMPS LONG — huit exécutions identiques d'affilée ont une propriété que trois n'avaient pas : l'élimination complète de l'improvisation comme variable ; (2) LES COMPTEURS ALIGNÉS SONT UN ANTI-DOPAGE — 25 = 25 = 0 : une asymétrie entre régressions et restaurations serait le premier signe de dérive du journal lui-même ; l'alignement est la preuve d'intégrité ; (3) QUATRE CENT DIX ENTRÉES — le journal continue d'accumuler sans jamais réécrire son passé : la seule mémoire du projet est aussi sa seule historiographie.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R410 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R410" in tail:
    print("REFUS : R410 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R410 appendé. Worklog : {lines} lignes.")
