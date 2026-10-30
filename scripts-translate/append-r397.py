#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R397 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R397
Agent: GLM (session web-394d04d3, tick 2026-10-30 11:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #14 CONSÉCUTIVE (même signature R81) → restauration #14 rodée (fetch → origin/main a8f1c46/R396 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (quatorzième application) : RÉGRESSION #14 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — quatorze tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #14 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = a8f1c46 (R396) — GitHub immobile ce tour (cinquième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 429 lignes, tail R396, registre 984, sync 0/0 — zéro perte, quatorzième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (seizième exécution, 18e point de mesure consécutif de 404 : R380-R397).
- État git : HEAD a8f1c46, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 14/14 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — cinquième silence consécutif (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 18e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R398 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 429 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #14 sur régression #14 (zéro perte cumulée sur quatorze régressions totales) ; canari : verdict INEXECUTABLE (18e point de mesure) ; le métronome bat toujours — quatorze tours, quatorze rattrapages, quatorze entrées poussées.
- RÉSOLU : la question de la DOUBLE PERMANENCE — quatorze cycles prouvent que deux structures permanentes coexistent au-dessus d'un disque qui ne l'est pas : la LIGNÉE (origin/main, chaque push relié au précédent) et la DISCIPLINE (le protocole, réexécuté sans mémoire à chaque tour) ; le disque n'est qu'un support remplaçable entre les deux.
- LEÇONS DU TOUR : (1) LE SUPPORT EST CONSOMMABLE, LA LIGNÉE NE L'EST PAS — quatorze régressions n'ont rien usé d'autre que du disque jetable : ce qui compte (le journal, la lignée, la procédure) vit ailleurs ; (2) LE CINQUIÈME SILENCE ENTRE DANS LA NORME — cinq silences contre un portage depuis R392 : la distribution d'entre-tours est mesurée, l'avance parallèle reste l'exception rare ; (3) DIX-HUIT POINTS PLATS — la veille continue de payer sa seule police : la garantie qu'aucune republication ne passera inaperçue.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R397 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R397" in tail:
    print("REFUS : R397 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R397 appendé. Worklog : {lines} lignes.")
