#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R404 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R404
Agent: GLM (session web-394d04d3, tick 2026-10-30 13:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #19 (PRÉDICTION DE R403 INFIRMÉE) → restauration #19 rodée (fetch → origin/main a8fae1e/R403 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (vingt-et-unième application) : RÉGRESSION #19, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — la stabilité PRÉDITE à R403 n'est PAS venue : deuxième régression consécutive (R403, R404), l'alternance s'est brisée à la quatrième itération.
- **MODÈLE D'ALTERNANCE FALSIFIÉ — CONSIGNÉ TEL QUEL** : trois cycles (R399-R403) n'étaient pas une loi ; le recyclage a frappé deux tours de suite cette fois ; nouveau modèle : le recyclage est IRRÉGULIER (période variable : parfois 1 tour, parfois 2+) — aucune prédiction ferme n'est possible sur la stabilité du prochain tour ; le réflexe cz redevient l'unique détecteur (comme il l'a toujours été en pratique) ; compte total : 19 régressions / 2 stabilités.
- RESTAURATION #19 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = a8fae1e (R403) — GitHub immobile (douzième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 559 lignes, tail R403, registre 984, sync 0/0 — zéro perte, dix-neuvième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingt-troisième exécution, 25e point de mesure consécutif de 404 : R380-R404).
- État git : HEAD a8fae1e, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 19/21 tours sous régression ; modèle irrégulier adopté (période variable) ; AUCUNE prédiction consignée pour R405 (l'humilité post-falsification) ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — douzième silence consécutif ; (d) SITE HABOUS en migration — 25e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R405 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 559 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #19 sur régression #19 (zéro perte cumulée sur dix-neuf régressions totales) ; canari : verdict INEXECUTABLE (25e point de mesure) ; le modèle d'alternance falsifié et remplacé par le modèle irrégulier.
- RÉSOLU : la question de la valeur de la FALSIFICATION (le modèle cassé n'a coûté que trois lignes d'hypothèse et rapporté une information durable : la période est irrégulière — la science du régime a progressé par son échec, pas par sa réussite) ; la question de la SYMÉTRIE DU JOURNAL (l'échec de prédiction est consigné avec la même précision que les réussites : le journal ne garde que les victoires n'est pas un journal, c'est une propagande).
- LEÇONS DU TOUR : (1) TROIS POINTS NE FONT PAS UNE DROITE NON PLUS — la période courte était une coïncidence enrichie : le hasard imite la loi sur quelques échantillons, seule la répétition longue la trahit ou la confirme ; (2) L'HUMILITÉ POST-FALSIFICATION EST UNE MÉTHODE — aucune nouvelle prédiction ferme tant que le modèle n'a pas repris du poids : prédire après un échec sans nouvelle donnée, c'est pari, pas science ; (3) LE RÉFLEXE RESTE ROI — le modèle est tombé, le réflexe cz n'a pas bougé : la procédure ne dépend pas de la théorie, c'est pourquoi elle survit aux théories.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R404 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R404" in tail:
    print("REFUS : R404 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R404 appendé. Worklog : {lines} lignes.")
