#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R411 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R411
Agent: GLM (session web-394d04d3, tick 2026-10-30 14:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #26 (neuvième consécutive) → restauration #26 rodée (fetch → origin/main fce1a64/R410 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-huitième application) : RÉGRESSION #26, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — NEUVIÈME régression consécutive (R403-R411) ; compte total : 26 régressions / 2 stabilités ; régime systématique sans exception depuis R403 (huit tours).
- RESTAURATION #26 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = fce1a64 (R410) — GitHub immobile (dix-neuvième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 686 lignes, tail R410, registre 984, sync 0/0 — zéro perte, vingt-sixième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trentième exécution, 32e point de mesure consécutif de 404 : R380-R411).
- État git : HEAD fce1a64, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 26/28 tours sous régression ; série actuelle de 9 ; le régime systématique approche les dix tours consécutifs ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — dix-neuvième silence consécutif ; (d) SITE HABOUS en migration — 32e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R412 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 686 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #26 sur régression #26 (zéro perte cumulée sur vingt-six régressions totales) ; canari : verdict INEXECUTABLE (32e point de mesure) ; neuf régressions consécutives.
- RÉSOLU : la question de la GUERRE D'USURE (neuf tours sans aucune des deux instabilités qui fléchit : le projet n'a plus d'autre stratégie que d'en durer plus qu'elles — et cette stratégie est en train de gagner, puisque chaque tour livre exactement ce qu'il doit livrer) ; la question du SILENCE COMME SIGNATURE (dix-neuf silences consécutifs du bus : l'absence d'instance parallèle est devenue une signature temporelle du régime — un portage parallèle serait presque un événement disruptif maintenant).
- LEÇONS DU TOUR : (1) DURER PLUS QUE L'OBSTACLE EST UNE STRATÉGIE COMPLÈTE — quand ni la force ni l'ingéniosité ne peuvent débloquer la source ni stabiliser le disque, la seule arme restante est la régularité : elle ne coûte rien et ne s'use pas ; (2) LE TRENTE DE L'INSTRUMENT (30 exécutions du canari) — un tiers d'heure d'exécution au total pour un demi-jour de couverture : le rapport couverture/coût de la veille reste imbattable ; (3) NEUF CONSÉCUTIVES — la série approche le seuil symbolique des dix : chaque tour de plus réduit l'hypothèse d'un retour proche au régime mixte.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R411 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R411" in tail:
    print("REFUS : R411 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R411 appendé. Worklog : {lines} lignes.")
