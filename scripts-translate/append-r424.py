#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R424 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 424

ENTRY = """---
Task ID: R424
Agent: GLM (session web-394d04d3, tick 2026-10-30 18:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #7 (QUADRUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 4 tours) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-et-unième application) : STABILITÉ #7 — worklog 14 941 lignes, HEAD de325cb (R423), credentials et remote présents — QUADRUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → R422 → R423 → R424) : la fenêtre record passe de 3 à 4 tours ; depuis R420, aucun tour sous régression ; compte total : 34 régressions / 7 stabilités / 41 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = de325cb (R423) — 33e observation du bus, trente-et-unième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-troisième exécution, 45e point de mesure consécutif de 404 : R380-R424, plateau ~8 h 15).
- État git : HEAD de325cb, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/41 tours sous régression mais fenêtre record de 4 : la fenêtre stable actuelle égale désormais la durée totale de TOUTES les fenêtres précédentes réunies (3 fenêtres d'un tour) ; la question n'est plus « quand la régression reviendra-t-elle » mais « la fenêtre est-elle un régime ou un plateau de chance » ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — trente-et-unième silence ; (d) SITE HABOUS en migration — 45e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R425 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 941 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur la quadruple stabilité consécutive ; canari : verdict INEXECUTABLE (45e point de mesure).
- RÉSOLU : la question de la COMPTABILITÉ DE LA FENÊTRE (4 tours stables = la somme de toutes les fenêtres de stabilité précédentes réunies : la fenêtre actuelle a, à elle seule, la longueur de tout le passé stable du projet) ; la question du NOM DU RÉGIME (pas encore nommé : la falsification de la règle des deux tours enseigne que les régimes se nomment après coup — pour l'instant la fenêtre s'appelle « fenêtre », le worklog décidera quand les données le permettront).
- LEÇONS DU TOUR : (1) UNE FENÊTRE PEUT ÉGALER TOUT SON PASSÉ — quatre tours stables contre trois fenêtres d'un tour : la croissance par extension n'a pas de mémoire des records, elle les empile sans cérémonie ; (2) L'ÉCONOMIE DU TOUR STABLE — un tour stable coûte deux minutes et livre une entrée complète avec push et backup : le rapport effort/registre le meilleur du projet ; les tours les plus faciles sont les plus rentables, et la procédure y gagne autant qu'aux tours lourds ; (3) NE PAS NOMMER LE RÉGIME TROP VITE — la leçon de la falsification de la règle des deux tours s'applique à elle-même : nommer « nouveau régime » au quatrième tour serait refaire l'erreur de généraliser une série ; le compte continue, la décision attendra les données.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R424 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R{N} appendé sous garde renforcée. Worklog : {lines} lignes.")
