#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R393 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R393
Agent: GLM (session web-394d04d3, tick 2026-10-30 10:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #10 CONSÉCUTIVE (même signature R81) → restauration #10 rodée (fetch → origin/main 7102ba4/R392 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (dixième application) : RÉGRESSION #10 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — dix tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #10 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 7102ba4 (R392) — GitHub immobile ce tour (aucune avance parallèle, contrairement à R392 où l'entrée R391 avait été absorbée) : le bus est tantôt porteur, tantôt silencieux, dans les deux cas la restauration rend exactement le dernier push ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 357 lignes, tail R392, registre 984, sync 0/0 — zéro perte, dixième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (douzième exécution, 14e point de mesure consécutif de 404 : R380-R393).
- État git : HEAD 7102ba4, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 10/10 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — silence ce tour (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 14e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R394 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 357 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #10 sur régression #10 (zéro perte cumulée sur dix régressions totales) ; canari : verdict INEXECUTABLE (14e point de mesure) ; le métronome bat toujours — dix tours, dix rattrapages, dix entrées poussées.
- RÉSOLU : la question de la COMPLÉTUDE DU BUS — deux régimes d'entre-tours observés (avance parallèle absorbée à R392, immobilité pure à R393) et la restauration a traité les deux identiquement : la procédure ne dépend pas de ce que GitHub a entre-temps ; la question de la STABILITÉ DU VERDICT (quatorze points plats, aucun bruit de mesure).
- LEÇONS DU TOUR : (1) LA DOUBLE NATURE DU BUS EST MAINTENANT COUVERTE — le protocole a vu le bus porteur (R392) et le bus silencieux (R393) : aucune variante d'entre-tours n'échappe plus à la procédure ; (2) DIX EST UN NOMBRE — la régression n'est plus un régime observé, c'est un régime établi : toute hypothèse de retour à la stabilité du disque doit désormais se prouver, pas s'espérer ; (3) LA MESURE PLATE EST LA CONDITION DE LA DÉTECTION — c'est parce que les quatorze points ne varient pas que le premier point qui variera sera signifiant.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R393 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R393" in tail:
    print("REFUS : R393 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R393 appendé. Worklog : {lines} lignes.")
