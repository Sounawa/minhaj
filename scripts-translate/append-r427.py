#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R427 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 427

ENTRY = """---
Task ID: R427
Agent: GLM (session web-394d04d3, tick 2026-10-30 18:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #10 (SEPTUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 7 tours, jalon rond) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-quatrième application) : STABILITÉ #10 — worklog 14 995 lignes, HEAD 4cce6c7 (R426), credentials et remote présents — SEPTUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → R422 → R423 → R424 → R425 → R426 → R427) : la fenêtre record passe de 6 à 7 tours — JALON ROND : dix stabilités au compte, avec 34 régressions / 10 stabilités / 44 applications du réflexe ; la fenêtre actuelle (7) approche désormais la plus longue série de régressions jamais observée (10, R403-R412).
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 4cce6c7 (R426) — 36e observation du bus, trente-quatrième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-sixième exécution, 48e point de mesure consécutif de 404 : R380-R427, plateau ~8 h 52).
- État git : HEAD 4cce6c7, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/44 tours sous régression mais fenêtre record de 7 : la stabilité se compare maintenant aux pires régressions sur la même échelle ; un tour stable de plus et elle dépassera toutes les séries de régressions sauf une ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-quatrième silence au fetch ; (d) SITE HABOUS en migration — 48e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R428 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 995 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la septuple stabilité consécutive et le jalon des dix stabilités ; canari : verdict INEXECUTABLE (48e point de mesure).
- RÉSOLU : la question de L'ÉCHELLE COMMUNE (7 tours stables contre 10 régressions au record : les deux extrêmes du disque se répondent enfin à la même échelle — si le prochain tour est stable, la stabilité dépassera toutes les séries de régressions sauf une) ; la question du JALON ROND (10e stabilité : le compte compte désormais en jalons des deux côtés, dix régressions consécutives d'un côté, dix stabilités cumulées de l'autre).
- LEÇONS DU TOUR : (1) LA FENÊTRE REJOINT LA SÉRIE — la stabilité n'a jamais été aussi proche de la durée des pires régressions : le disque réécrit sa moyenne glissante par la fin du journal, non par son début, et c'est ainsi qu'un régime change sans qu'on le décide ; (2) L'INSTRUMENT NE S'ENDORMT PAS — 48 points plats et 34 silences : la tentation du raccourci (« la source sera encore fermée, pourquoi re-sonder ? ») culmine exactement quand la stabilité l'invite ; la règle cx re-sonde à CHAQUE tour parce que le jour où la source rouvrira ressemblera en tout point aux jours où elle est restée fermée ; (3) LES JALONS SE CUMULENT SANS CÉRÉMONIE — dix stabilités sont arrivées une par une, sans seuil annoncé : la croissance régulière ne connaît pas de fanfare, elle connaît des comptes exacts.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R427 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
