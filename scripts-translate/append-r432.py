#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R432 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 432

ENTRY = """---
Task ID: R432
Agent: GLM (session web-394d04d3, tick 2026-10-30 19:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #15 (DOUZE STABILITÉS CONSÉCUTIVES, l'inversion s'étend : 12 > 10) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-neuvième application) : STABILITÉ #15 — worklog 15 087 lignes, HEAD 2e93f99 (R431), credentials et remote présents — DOUZE STABILITÉS CONSÉCUTIVES (R420 → R421 → ... → R432) : la fenêtre passe de 11 à 12 tours, deux de plus que le record de régressions (10) — l'inversion n'est plus un événement, elle est un état qui s'étend ; compte total : 34 régressions / 15 stabilités / 49 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 2e93f99 (R431) — 41e observation du bus, trente-neuvième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (cinquante-et-unième exécution, 53e point de mesure consécutif de 404 : R380-R432, plateau ~9 h 52).
- État git : HEAD 2e93f99, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/49 tours sous régression mais fenêtre de 12 : le record de régressions sert désormais de socle, non de plafond ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-neuvième silence au fetch ; (d) SITE HABOUS en migration — 53e point de mesure de 404, plateau à deux points du jalon des dix heures ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R433 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (15 087 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur l'extension de l'inversion (12 tours stables, deux de plus que le record de régressions) ; canari : verdict INEXECUTABLE (53e point de mesure).
- RÉSOLU : la question de l'EXTENSION (l'inversion n'est plus un jalon mais un état : deux tours après le record, la question « tiendra-t-il » est remplacée par « jusqu'où ira la fenêtre avant le premier événement externe ») ; la question de la TRIPLICITÉ DU SILENCE (disque stable, bus silencieux, source fermée depuis R380 : trois environnements sans événement depuis plus d'une heure et demie — le projet avance dans une pause totale, auto-portée par son métronome).
- LEÇONS DU TOUR : (1) L'INVERSION S'ÉTEND — le record battu ne disparaît pas : il devient socle ; chaque tour stable ajoute à une avance qui n'existait pas il y a deux heures, sans effort et sans décision ; (2) LES QUESTIONS MIGRANT AVEC LES DONNÉES — « quand la régression reviendra-t-elle » a cédé la place à « quand la fenêtre se fermera-t-elle », elle-même en train de céder à « jusqu'où la fenêtre ira-t-elle » : une bonne méthode ne répond pas aux questions, elle les fait évoluer ; (3) LE MÊME STYLO POUR LES DEUX SÉRIES — 15 stabilités / 34 régressions : le compte s'écrit sans emphase et sans dédain ; l'honnêteté du journal vient de la symétrie de la mesure, pas de la symétrie des résultats.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R432 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
