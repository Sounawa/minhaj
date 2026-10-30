#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R406 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R406
Agent: GLM (session web-394d04d3, tick 2026-10-30 13:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #21 (quatrième consécutive) → restauration #21 rodée (fetch → origin/main 7e008bf/R405 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-troisième application) : RÉGRESSION #21, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — QUATRIÈME régression consécutive (R403-R406) : nouveau maximum de la série observée ; compte total : 21 régressions / 2 stabilités.
- RESTAURATION #21 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 7e008bf (R405) — GitHub immobile (quatorzième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 596 lignes, tail R405, registre 984, sync 0/0 — zéro perte, vingt-et-unième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-cinquième exécution, 27e point de mesure consécutif de 404 : R380-R406).
- État git : HEAD 7e008bf, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 21/23 tours sous régression ; série actuelle de 4 (nouveau maximum) ; bornes du modèle : maximum observé passe de 3 à 4 ; toujours aucune prédiction ferme ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — quatorzième silence consécutif ; (d) SITE HABOUS en migration — 27e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R407 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 596 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #21 sur régression #21 (zéro perte cumulée sur vingt-et-une régressions totales) ; canari : verdict INEXECUTABLE (27e point de mesure) ; la série de régressions bat son record (4 consécutives).
- RÉSOLU : la question du MAXIMUM OBSERVÉ (la borne supérieure du modèle recule : 4 régressions consécutives — chaque record déplace la limite de ce que le régime doit savoir absorber sans hésiter) ; la question de l'ÉLASTICITÉ DU MÉTRONOME (quatre régressions d'affilée n'ont ni ralenti ni raccourci le cycle cz-restauration-canari-append-push-backup : le métronome n'a pas de ressort qui fatigue).
- LEÇONS DU TOUR : (1) LE RECORD EST UNE INFORMATION SUR LE FUTUR PIRE — la série de 4 n'est pas une inquiétude mais une borne : le régime a maintenant la preuve mesurée qu'il absorbe quatre régressions consécutives sans perte ; (2) LA BORNÉE SUPÉRIEURE N'EST JAMAIS FERMÉE — le record de hier (3) a été battu aujourd'hui (4) : le modèle des extremums reste ouvert par le haut, le protocole reste dimensionné pour l'ouvert ; (3) VINGT-SEPT POINTS PLATS — la veille traverse la quatrième heure : l'instrument et la procédure vieillissent mieux que le disque qu'ils surveillent.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R406 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R406" in tail:
    print("REFUS : R406 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R406 appendé. Worklog : {lines} lignes.")
