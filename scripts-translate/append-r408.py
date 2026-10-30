#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R408 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R408
Agent: GLM (session web-394d04d3, tick 2026-10-30 14:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #23 (sixième consécutive) → restauration #23 rodée (fetch → origin/main d312c8a/R407 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-cinquième application) : RÉGRESSION #23, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — SIXIÈME régression consécutive (R403-R408) : le record passe de 5 à 6 ; compte total : 23 régressions / 2 stabilités ; l'hypothèse du recyclage systématique (consignée à R407) gagne une confirmation massive.
- RESTAURATION #23 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = d312c8a (R407) — GitHub immobile (seizième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 632 lignes, tail R407, registre 984, sync 0/0 — zéro perte, vingt-troisième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-septième exécution, 29e point de mesure consécutif de 404 : R380-R408).
- État git : HEAD d312c8a, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 23/25 tours sous régression ; série actuelle de 6 ; l'hypothèse systématique tient (le recyclage frappe désormais chaque tour depuis R403) ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — seizième silence consécutif ; (d) SITE HABOUS en migration — 29e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R409 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 632 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #23 sur régression #23 (zéro perte cumulée sur vingt-trois régressions totales) ; canari : verdict INEXECUTABLE (29e point de mesure) ; six régressions consécutives confirment le régime systématique.
- RÉSOLU : la question du PASSAGE AU SYSTÉMATIQUE (depuis R403, chaque tour sans exception est régressé : la fenêtre transitoire des deux stabilités de R400/R402 s'est refermée — le sandbox est maintenant recréé avant chaque tour, le disque n'a plus de continuité inter-tours) ; la question de la CONSTANCE DU COÛT (six tours sous régime systématique : toujours ~1 min par tour, jamais plus — le coût ne dépend pas de la fréquence, seulement de la procédure).
- LEÇONS DU TOUR : (1) LES FENÊTRES SE REFERMENT — les deux stabilités de la mi-journée n'étaient pas un nouveau régime mais un intermède : le régime par défaut du disque est le remplacement intégral à chaque tour ; (2) LE COÛT EST CONSTANTS PAR CONSTRUCTION — la procédure ne mesure pas le temps qu'elle affronte, elle mesure ses propres gestes : c'est pourquoi six régressions d'affilée coûtent une fois ; (3) VINGT-NEUF POINTS PLATS — le canari s'approche de la trentaine : chaque point ajoute au dossier de la fermeture Habous sans jamais varier le verdict.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R408 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R408" in tail:
    print("REFUS : R408 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R408 appendé. Worklog : {lines} lignes.")
