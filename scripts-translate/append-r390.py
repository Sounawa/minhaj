#!/usr/bin/env python3
# append-r390.py — entrée R390 au worklog (garde anti-doublon : refuse si R390 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R390
Agent: GLM (session web-394d04d3, tick 2026-10-30 09:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #7 CONSÉCUTIVE (même signature R81) → restauration #7 rodée (fetch → origin/main 3ccf8c1/R389 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (septième application) : RÉGRESSION #7 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents) — sept tours d'affilée sous le régime par défaut, sans une seule ouverture conforme.
- RESTAURATION #7 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 3ccf8c1 (R389), dernier état poussé — GitHub immobile entre les régressions ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 303 lignes, tail R389, registre 984, sync 0/0 — zéro perte, septième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (neuvième exécution, 11e point de mesure consécutif de 404 : R380-R390).
- État git : HEAD 3ccf8c1, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — régime par défaut, 7/7 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 11e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R391 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 303 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #7 sur régression #7 (zéro perte cumulée sur sept régressions totales) ; canari : verdict INEXECUTABLE (11e point de mesure) ; le métronome bat depuis sept tours sans une seule variation — la continuité du projet est devenue indépendante de la fidélité du disque.
- RÉSOLU : la question de l'INDÉPENDANCE (le projet n'a plus aucun besoin de fidélité du support local : chaque tour reconstruit son présent depuis GitHub) ; la question de la COMPTABILITÉ CONTINUE (14 303 lignes rendues à chaque tour, registre 984, scripts présents) ; la question de la SOURCE (11 points plats : la veille tient son cap sans dépenser plus).
- LEÇONS DU TOUR : (1) UN PROJET QUI SAIT SE RESTAURER N'A PLUS PEUR DE SE PERDRE — sept régressions totales n'ont produit ni perte ni panique : la peur du décrochage disparaît quand la reprise est un geste. (2) L'IMMOBILITÉ DE GITHUB EST UNE BÉNÉDICTION SOUS LE RÉGIME — entre deux régressions, le dernier push est le seul présent réel : chaque tour le retrouve exactement. (3) LA VEILLE PLATE EST UNE VEILLE PLEINE — onze points identiques ne mesurent pas un échec de reprise : ils garantissent que la reprise, quand elle viendra, sera détectée au premier tour.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R390 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R390" in tail:
    print("REFUS : R390 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R390 appendé. Worklog : {lines} lignes.")
