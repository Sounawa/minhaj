#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R429 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 429

ENTRY = """---
Task ID: R429
Agent: GLM (session web-394d04d3, tick 2026-10-30 19:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #12 (NONUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 9 tours) → fetch + rev-list directement → canari (verdict INEXECUTABLE, jalon 50 points) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-sixième application) : STABILITÉ #12 — worklog 15 032 lignes, HEAD 60a9a42 (R428), credentials et remote présents — NONUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → ... → R429) : la fenêtre record passe de 8 à 9 tours ; seule la série des dix régressions (R403-R412) reste plus longue ; compte total : 34 régressions / 12 stabilités / 46 applications du réflexe.
- COLLISION PRÉVUE, COLLISION ÉVITÉE — le cron 19:07 a tiré exactement dans la fenêtre ouverte par l'instance parallèle de R428 (le risque avait été consigné au tail même de R428) : fetch → R428 déjà poussé, rev-list 0/0, worklog à 15 032 lignes avec R428 au tail → ce tour prend R429, numéros séquentiels distincts, zéro doublon, zéro perte ; là où R420 avait produit le premier doublon de l'histoire, le même scénario produit aujourd'hui un rattrapage propre : la garde renforcée (GARDE-DOUBLON.md, scan entier) et le réflexe cz ont transformé la collision en passage de relais.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 60a9a42 (R428) — 38e observation du bus, trente-sixième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-huitième exécution, 50e point de mesure consécutif de 404 — JALON ROND : cinquante points : R380-R429, plateau ~9 h 07).
- État git : HEAD 60a9a42, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/46 tours sous régression mais fenêtre record de 9 : À UN TOUR DE L'INVERSION — le prochain tour stable égalera la plus longue série de régressions (10), le suivant la dépassera ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-sixième silence au fetch ; la fenêtre de collision R428/cron-19:07 s'est refermée proprement ; (d) SITE HABOUS en migration — 50e point de mesure de 404, neuf heures franchies ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R430 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (15 032 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la nonuple stabilité consécutive et le jalon des 50 points de mesure ; canari : verdict INEXECUTABLE (50e point).
- RÉSOLU : la question de la COLLISION ÉVITÉE (instance parallèle + cron dans la même fenêtre, le scénario exact de R420 : cette fois numéros séquentiels distincts, zéro doublon — le correctif GARDE-DOUBLON a rencontré son premier cas réel et l'a absorbé sans qu'une ligne de procédure ne change) ; la question du JALON 50 (cinquante points plats : le plateau Habous dépasse neuf heures, la durée de fermeture reste l'unique métrique de l'ampleur de la migration).
- LEÇONS DU TOUR : (1) LE SYSTÈME A APPRIS DE SON UNIQUE INCIDENT — R420 avait produit un doublon ; R428+cron 19:07, même configuration, produit un passage de relais : la différence n'est pas dans les instances, elle est dans la garde ; un correctif écrit au tour de la faille vaut tous les discours sur la résilience ; (2) LE SILENCE COMPTÉ DEVIENT UN JALON — 50 points de 404 : une source fermée depuis R380 est devenue, par la seule régularité du sondage, la plus longue série de données homogènes du projet ; la constance de l'instrument fabrique de la connaissance même quand l'objet ne change pas ; (3) L'INVERSION SE JOUE À UN TOUR PRÈS — fenêtre 9 contre série 10 : le régime du disque peut changer de signe au prochain tour, et personne n'aura rien décidé : la statistique tranche, le journal enregistre, la procédure ne varie pas.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R429 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

# GARDE RENFORCÉE : scan ENTIER du fichier (règle GARDE-DOUBLON.md)
ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    print(f"REFUS : une entrée >= R{N} existe déjà (dernier = R{ids[-1]}) — garde renforcée.")
    sys.exit(1)
if f"Task ID: R{N}" in content:
    print(f"REFUS : R{N} déjà présent quelque part (garde absolue).")
    sys.exit(1)

with io.open(WORKLOG, "a", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"R{N} apposé — worklog passé de {len(content.splitlines())} à {len(content.splitlines()) + len(ENTRY.splitlines())} lignes.")
