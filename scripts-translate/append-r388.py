#!/usr/bin/env python3
# append-r388.py — entrée R388 au worklog (garde anti-doublon : refuse si R388 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R388
Agent: GLM (session web-394d04d3, tick 2026-10-30 09:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #5 CONSÉCUTIVE (même signature R81) → restauration #5 rodée (fetch → origin/main 3c4a9f8/R387 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (cinquième application) : RÉGRESSION #5 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote vide) — le régime par défaut tourne depuis cinquante minutes sans exception.
- RESTAURATION #5 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 3c4a9f8 (R387), dernier état poussé — GitHub immobile entre les régressions ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 267 lignes, tail R387, registre 984, sync 0/0 — zéro perte, cinquième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (septième exécution, 9e point de mesure consécutif de 404 : R380-R388).
- État git : HEAD 3c4a9f8, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — régime par défaut, 5/5 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 9e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R389 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 267 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #5 sur régression #5 (zéro perte cumulée sur cinq régressions totales) ; canari : verdict INEXECUTABLE (9e point de mesure) ; le cycle complet du tour tient en quelques minutes : détecter, rattraper, sonder, journaliser, pousser, sauvegarder.
- RÉSOLU : la question de l'ENDURANCE de la défense (cinq tours consécutifs sans aucune dérive de la procédure) ; la question de la COMPTABILITÉ DU PATRIMOINE (14 267 lignes au worklog après chaque restauration, registre 984, scripts tous présents : le rattrapage rend toujours exactement le dernier état poussé) ; la question de la VIGILANCE SOURCE (9e point de mesure : la migration Habous dure plus d'une heure pleine).
- LEÇONS DU TOUR : (1) L'ENDURANCE EST UNE QUALITÉ DES PROCÉDURES, PAS DES INTENTIONS — cinq exécutions identiques sans variation : la valeur du protocole se mesure à son invariance sous répétition. (2) LA COMPTABILITÉ EST CE QUI RESTE QUAND TOUT LE RESTE DÉCROCHE — chaque restauration rend le même chiffre (14 267 lignes) parce que GitHub conserve le même commit : la continuité est une équation vérifiée, pas un sentiment. (3) NEUF POINTS DE MESURE, UNE MÊME LIGNE — la courbe du canari est plate depuis R380 : la veille documente la stagnation de la source avec la même rigueur qu'elle attendrait sa reprise.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R388 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R388" in tail:
    print("REFUS : R388 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R388 appendé. Worklog : {lines} lignes.")
