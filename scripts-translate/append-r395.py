#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R395 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R395
Agent: GLM (session web-394d04d3, tick 2026-10-30 10:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #12 CONSÉCUTIVE (même signature R81) → restauration #12 rodée (fetch → origin/main 4af3e36/R394 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (douzième application) : RÉGRESSION #12 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — douze tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #12 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 4af3e36 (R394) — GitHub immobile ce tour (troisième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 393 lignes, tail R394, registre 984, sync 0/0 — zéro perte, douzième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quatorzième exécution, 16e point de mesure consécutif de 404 : R380-R395).
- État git : HEAD 4af3e36, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 12/12 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — troisième silence consécutif (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 16e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R396 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 393 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #12 sur régression #12 (zéro perte cumulée sur douze régressions totales) ; canari : verdict INEXECUTABLE (16e point de mesure) ; le métronome bat toujours — douze tours, douze rattrapages, douze entrées poussées.
- RÉSOLU : la question de la PRÉVISIBILITÉ — douze tours sous le même régime et l'ouverture peut se rédiger d'avance (même signature, même procédure, même durée) : le seul élément non prévisible reste le verdict du canari, qui est précisément celui que la mesure surveille ; la question du SILENCE LONG (trois silences consécutifs du bus : le régime d'entre-tours normal est le silence, l'avance de R392 reste l'exception documentée).
- LEÇONS DU TOUR : (1) CE QUI EST ROUTINE NE SE REJUSTIFIE PAS — à douze répétitions, la procédure n'exige plus de démonstration, seulement d'exécution : les entrées de veille deviennent plus courtes sans perdre un seul fait ; (2) LA COMPTABILITÉ RESTE LE FILET — chaque compteur (12/12, 16 points, 14 393 lignes, registre 984) est re-mesuré au tail réel, jamais hérité : c'est la différence entre une routine et une dérive ; (3) LE TROISIÈME SILENCE CONSACRE LA DISTRIBUTION — porteur une fois sur quatre, silencieux trois fois : le bus transporte l'essentiel, rarement du nouveau.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R395 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R395" in tail:
    print("REFUS : R395 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R395 appendé. Worklog : {lines} lignes.")
