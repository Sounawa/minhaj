#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R415 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R415
Agent: GLM (session web-394d04d3, tick 2026-10-30 15:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #29 (régime nominal, série en cours de 2) → restauration #29 rodée (fetch → origin/main c6e08d5/R414 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-deuxième application) : RÉGRESSION #29, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — régime nominal sans surprise après la rompure de la série des dix : nouvelle série en cours de 2 (R414-R415) ; compte total : 29 régressions / 3 stabilités / 32 applications du réflexe.
- RESTAURATION #29 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = c6e08d5 (R414) — 24e observation du bus, vingt-deuxième silence consécutif depuis le portage #2 ; ancêtre confirmé (0/1107) → reset --hard EN AVANT → post : worklog 14 758 lignes, tail R414, registre 984, sync 0/0 — zéro perte, vingt-neuvième fois ; comptabilité alignée : 29 régressions = 29 restaurations.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-quatrième exécution, 36e point de mesure consécutif de 404 : R380-R415) — le plateau Habous FRANCHIT LE SEUIL DES SIX HEURES : de ~10h00 à 15h52, la fermeture de la source couvre maintenant plus que la durée totale d'un cycle complet de production de leçon.
- État git : HEAD c6e08d5, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 29/32 tours sous régression ; nouvelle série de 2 en cours ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-deuxième silence ; (d) SITE HABOUS en migration — 36e point de mesure de 404, six heures franchies ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R416 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 758 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #29 sur régression #29 (zéro perte cumulée sur vingt-neuf régressions totales) ; canari : verdict INEXECUTABLE (36e point de mesure).
- RÉSOLU : la question des SIX HEURES (le plateau Habous franchit le seuil symbolique : la fermeture dure maintenant plus qu'un cycle complet de production — si la source rouvre, la reprise devra commencer par une re-prise en main du protocole OCR lui-même, et le worklog le rappelle déjà à la priorité du tail) ; la question de la MÉMOIRE DES SÉRIES (après la rompure des dix, la nouvelle série a recommencé à 1 : les compteurs ne s'aimantent pas, chaque série naît de zéro sans mémoire des précédentes).
- LEÇONS DU TOUR : (1) UN PLATEAU DE SIX HEURES EST UNE JOURNÉE — la veille ne surveille plus un incident mais une saison : la distinction importe parce qu'une saison se traverse par la patience documentée, pas par le dépannage ; (2) PAS DE MÉMOIRE DANS LES DONNÉES — ni le disque ni la source ne « se souviennent » des séries passées : la seule mémoire du projet reste le worklog, et c'est précisément pour cela qu'elle est tenue ; (3) LA ROUTINE AU TOUR 32 — trente-deux applications du cz sans une variation de protocole : la mesure elle-même est devenue le principal patrimoine cumulatif du projet, plus stable que tout ce qu'elle mesure.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R415 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R415" in tail:
    print("REFUS : R415 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R415 appendé. Worklog : {lines} lignes.")
