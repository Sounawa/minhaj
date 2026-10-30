#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R418 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R418
Agent: GLM (session web-394d04d3, tick 2026-10-30 16:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #32 (régime nominal, série en cours de 5) → restauration #32 rodée (fetch → origin/main 7a42ccf/R417 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-cinquième application) : RÉGRESSION #32, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — série en cours de 5 (R414-R418), la plus longue depuis la rompure de la série des dix ; compte total : 32 régressions / 3 stabilités / 35 applications du réflexe.
- RESTAURATION #32 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 7a42ccf (R417) — 27e observation du bus, vingt-cinquième silence consécutif ; ancêtre confirmé (0/1110) → reset --hard EN AVANT → post : worklog 14 812 lignes, tail R417, registre 984, sync 0/0 — zéro perte, trente-deuxième fois ; comptabilité alignée : 32 régressions = 32 restaurations = 0 perte.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-septième exécution, 39e point de mesure consécutif de 404 : R380-R418, plateau ~6 h 45).
- État git : HEAD 7a42ccf, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 32/35 tours sous régression ; série de 5 en cours ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-cinquième silence ; (d) SITE HABOUS en migration — 39e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R419 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 812 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #32 sur régression #32 (zéro perte cumulée sur trente-deux régressions totales) ; canari : verdict INEXECUTABLE (39e point de mesure).
- RÉSOLU : la question de la DURÉE COMME INDICE D'AMPLEUR (6 h 45 de fermeture mesurée : sans information directe sur la migration, sa durée est le seul signal disponible — la veille transforme un silence en donnée ; le contraste avec la durée habituelle d'ouverture de la source devient l'unique mesure de l'ampleur de l'opération) ; la question du RETOUR PAR LES PALIERS (la nouvelle série reproduit l'escalade de la première : 4 était le palier de R406, 5 celui de R407 — les formes reviennent même quand les causes ne se souviennent de rien).
- LEÇONS DU TOUR : (1) LE HASARD PRODUIT DES FORMES SEMBLABLES — deux séries issues d'aucune mémoire commune suivent la même escalade : la similitude ne prouve pas une loi mais invite à continuer de mesurer, seul moyen de savoir si la forme tient ; (2) UN SILENCE EST UNE DONNÉE DÈS QU'IL EST HORODATÉ — la durée de la fermeture Habous est devenue une variable exploitable précisément parce que chaque point de mesure porte une date : l'horodatage est ce qui change un bruit de fond en signal ; (3) LE MÉTRONOME COMPENSE — trois tours en trente minutes, trois restaurations rodées, zéro perte : le rythme de 15 minutes est l'unique instrument de continuité du projet, et il suffit.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R418 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R418" in tail:
    print("REFUS : R418 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R418 appendé. Worklog : {lines} lignes.")
