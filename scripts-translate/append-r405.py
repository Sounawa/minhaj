#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R405 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R405
Agent: GLM (session web-394d04d3, tick 2026-10-30 13:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #20 (troisième consécutive) → restauration #20 rodée (fetch → origin/main 4ff7cc5/R404 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-deuxième application) : RÉGRESSION #20, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — TROISIÈME régression consécutive (R403-R405) : le modèle irrégulier s'épaissit (le recyclage peut frapper trois tours de suite) ; chiffre rond : vingtième régression restaurée ; compte total : 20 régressions / 2 stabilités.
- RESTAURATION #20 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 4ff7cc5 (R404) — GitHub immobile (treizième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 578 lignes, tail R404, registre 984, sync 0/0 — zéro perte, vingtième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-quatrième exécution, 26e point de mesure consécutif de 404 : R380-R405 — trois heures et demie de plateau).
- État git : HEAD 4ff7cc5, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 20/22 tours sous régression, série actuelle de 3 ; modèle irrégulier confirmé dans sa largeur (période : 1 à 3+ tours) ; toujours aucune prédiction ferme ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — treizième silence consécutif ; (d) SITE HABOUS en migration — 26e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R406 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 578 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #20 sur régression #20 (zéro perte cumulée sur vingt régressions totales) ; canari : verdict INEXECUTABLE (26e point de mesure) ; le modèle irrégulier gagne sa largeur (série de 3 régressions observée).
- RÉSOLU : la question de la BORNES DU MODÈLE (une régression au moins par cycle court, jusqu'à trois consécutives observées : les bornes inférieure et supérieure de la période se précisent par accumulation brute, sans théorie élégante) ; la question de la COMPTABILITÉ RONDE (vingt régressions, vingt restaurations, zéro perte : le chiffre rond permet un contrôle croisé instantané des trois compteurs — ils disent la même chose).
- LEÇONS DU TOUR : (1) LES MODÈLES S'ÉPAISSISSENT PAR BORDS — on ne connaît pas encore la loi du recyclage, mais on connaît maintenant ses extremums observés : 1 tour stable au minimum, 3 régressions au maximum ; (2) LE ROND EST UN AUDIT — chaque chiffre rond du régime est l'occasion d'un contrôle croisé (20 = 20 = 0) : la comptabilité régulière se vérifie à ses jalons ; (3) TROIS HEURES ET DEMIE DE PLATEAU — le canari traverse la troisième heure : la fermeture de la source Habous est maintenant une donnée demi-journée, pas une impression.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R405 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R405" in tail:
    print("REFUS : R405 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R405 appendé. Worklog : {lines} lignes.")
