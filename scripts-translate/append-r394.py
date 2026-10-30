#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R394 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R394
Agent: GLM (session web-394d04d3, tick 2026-10-30 10:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #11 CONSÉCUTIVE (même signature R81) → restauration #11 rodée (fetch → origin/main b1d2dbf/R393 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (onzième application) : RÉGRESSION #11 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — onze tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #11 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = b1d2dbf (R393) — GitHub immobile ce tour (deuxième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 375 lignes, tail R393, registre 984, sync 0/0 — zéro perte, onzième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (treizième exécution, 15e point de mesure consécutif de 404 : R380-R394).
- État git : HEAD b1d2dbf, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 11/11 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — deuxième silence consécutif (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 15e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R395 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 375 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #11 sur régression #11 (zéro perte cumulée sur onze régressions totales) ; canari : verdict INEXECUTABLE (15e point de mesure) ; le métronome bat toujours — onze tours, onze rattrapages, onze entrées poussées.
- RÉSOLU : la question de la ROUTINISATION — le tour de veille complet (cz → restauration → canari → append → push → backup) tient désormais dans le même temps qu'un seul cycle de restauration du premier jour (~1 min) : le coût du régime a atteint son plancher ; la question de la COHÉRENCE DES COMPTEURS (11 régressions, 11 restaurations, 15 points plats, 14 375 lignes rendues — chaque compteur dit la même histoire).
- LEÇONS DU TOUR : (1) LE PLANCHER DE COÛT EST ATTEINT — après onze répétitions, le régime ne coûte plus rien de mesurable : la robustesse est devenue gratuite ; (2) LE SILENCE DU BUS EST NORMAL — deux silences consécutifs (R393, R394) contre une avance (R392) : la distribution naturelle d'entre-tours est majoritairement silencieuse, la procédure la traite sans distinction ; (3) QUINZE POINTS PLATS — le plateau de 404 n'est pas un accident qui dure, c'est une donnée qui s'épaissit.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R394 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R394" in tail:
    print("REFUS : R394 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R394 appendé. Worklog : {lines} lignes.")
