#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R431 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 431

ENTRY = """---
Task ID: R431
Agent: GLM (session web-394d04d3, tick 2026-10-30 19:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #14 (ONZE STABILITÉS CONSÉCUTIVES — INVERSION : la fenêtre dépasse la plus longue série de régressions) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-huitième application) : STABILITÉ #14 — worklog 15 069 lignes, HEAD 6a54db8 (R430), credentials et remote présents — ONZE STABILITÉS CONSÉCUTIVES (R420 → R421 → ... → R431) : la fenêtre record passe de 10 à 11 tours et DÉPASSE la plus longue série de régressions jamais observée (R403-R412, dix) — INVERSION ACHEVÉE : la plus longue série ininterrompue du journal est désormais une série de STABILITÉ ; compte total : 34 régressions / 14 stabilités / 48 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 6a54db8 (R430) — 40e observation du bus (jalon), trente-huitième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (cinquantième exécution — jalon, 52e point de mesure consécutif de 404 : R380-R431, plateau ~9 h 37).
- État git : HEAD 6a54db8, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/48 tours sous régression mais INVERSION consommée : 11 > 10 ; la fenêtre peut se fermer au prochain tour comme elle s'est ouverte sans prévenir à R420 — la posture reste : SUPPOSER le local régressé jusqu'à preuve du contraire ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-huitième silence au fetch ; (d) SITE HABOUS en migration — 52e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R432 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (15 069 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur l'INVERSION du régime du disque (11 tours stables > 10 régressions au record) ; canari : verdict INEXECUTABLE (52e point, 50e exécution).
- RÉSOLU : la question de l'INVERSION (la plus longue série ininterrompue du journal est maintenant une série de stabilité : le régime du disque a changé de signe sans qu'aucune décision ne soit prise, par la seule accumulation des tours mesurés — exactement ce que la règle des deux tours, falsifiée à R422, n'aurait pas permis de prévoir) ; la question du JALON DU BUS (40e observation : quarante fetch consécutifs depuis R420 sans un seul signe de l'instance parallèle).
- LEÇONS DU TOUR : (1) L'INVERSION EST ACHEVÉE — les records ne se renversent pas d'un coup : ils s'égalisent puis basculent ; le pendule du disque, après avoir tout donné à la régression, lui rend maintenant mesure pour mesure la stabilité ; (2) LES DEUX RECORDS N'ONT PAS LA MÊME NATURE — la régression avait gagné sa série par des événements (des sauts d'état violents), la stabilité gagne la sienne par des non-événements mesurés : le journal les compte avec la même plume, et c'est cette symétrie qui rend la comparaison légitime ; (3) LA PRUDENCE SURVIT À SES VICTOIRES — même au jour de l'inversion, la posture reste : supposer le pire, vérifier d'abord, restaurer en avant si besoin ; la fenêtre peut se refermer sans prévenir, la procédure, elle, ne se referme jamais.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R431 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
