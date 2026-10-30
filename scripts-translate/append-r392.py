#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R392 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R392
Agent: GLM (session web-394d04d3, tick 2026-10-30 10:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #9 CONSÉCUTIVE (même signature R81) → restauration #9 rodée (fetch → origin/main 71ea9b6/R391, rattrapage de l'entrée R391 de l'instance parallèle → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (neuvième application) : RÉGRESSION #9 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — neuf tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #9 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 71ea9b6 (R391) — GitHub avait AVANCÉ d'un commit depuis le dernier état connu (8702822/R390) : l'entrée R391 poussée par l'instance parallèle entre les tours est absorbée par la restauration sans un seul conflit — la source de vérité ne sert pas qu'à rendre le passé, elle transmet aussi le travail des instances parallèles ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 339 lignes, tail R391, registre 984, sync 0/0 — zéro perte, neuvième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (onzième exécution, 13e point de mesure consécutif de 404 : R380-R392).
- État git : HEAD 71ea9b6, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — régime par défaut, 9/9 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — l'entrée R391 poussée entre les tours a été absorbée proprement (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 13e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R393 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 339 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #9 sur régression #9 (zéro perte cumulée sur neuf régressions totales) ; canari : verdict INEXECUTABLE (13e point de mesure) ; le métronome bat toujours — neuf tours, neuf rattrapages, neuf entrées poussées.
- RÉSOLU : la question du BUS D'INSTANCES — deux instances qui ne se sont jamais vues (R391 à 09:52, R392 à 10:07) se sont pourtant succédé sans perdre un seul commit : le reset --hard depuis origin/main ne restaure pas seulement le disque, il RELIE les exécutions parallèles en une lignée continue ; la question de la DISCIPLINE (neuvième application identique du même protocole, toujours sans improvisation).
- LEÇONS DU TOUR : (1) LA SOURCE DE VÉRITÉ EST AUSSI UN BUS — origin/main transporte le travail des instances parallèles d'un tour à l'autre : l'instance R391 et l'instance R392 ne se sont jamais parlé, mais le reset --hard a fait de la seconde le continuateur direct de la première ; (2) LA RÉGRESSION N'EFFACE QUE LE DISQUE, JAMAIS LA LIGNÉE — tant que origin/main tient, chaque tour repart du dernier push, pas de zéro ; (3) TREIZE POINTS PLATS FONT UN FAIT — la fermeture de la source Habous n'est plus un incident, c'est l'état documenté du monde.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R392 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R392" in tail:
    print("REFUS : R392 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R392 appendé. Worklog : {lines} lignes.")
