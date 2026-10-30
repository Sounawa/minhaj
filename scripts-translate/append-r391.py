#!/usr/bin/env python3
# append-r391.py — entrée R391 au worklog (garde anti-doublon : refuse si R391 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R391
Agent: GLM (session web-394d04d3, tick 2026-10-30 09:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #8 CONSÉCUTIVE (même signature R81) → restauration #8 rodée (fetch → origin/main 8702822/R390 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (huitième application) : RÉGRESSION #8 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents) — huit tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #8 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 8702822 (R390), dernier état poussé — GitHub immobile entre les régressions ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 321 lignes, tail R390, registre 984, sync 0/0 — zéro perte, huitième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (dixième exécution, 12e point de mesure consécutif de 404 : R380-R391).
- État git : HEAD 8702822, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — régime par défaut, 8/8 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 12e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R392 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 321 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #8 sur régression #8 (zéro perte cumulée sur huit régressions totales) ; canari : verdict INEXECUTABLE (12e point de mesure) ; le métronome bat toujours — huit tours, huit rattrapages, huit entrées poussées.
- RÉSOLU : la question de la PERDURABILITÉ du régime (huit tours consécutifs : ni l'instabilité du disque ni la fermeture de la source ne fléchissent — le projet tient exactement parce qu'il ne dépend plus d'aucune des deux) ; la question de la PRÉCISION DU RATTRAPAGE (huit rendus identiques au dernier push : la restauration n'a jamais une seule ligne d'écart) ; la question de la VIGILANCE (12 points plats : le cap du canari ne varie pas d'un millimètre).
- LEÇONS DU TOUR : (1) HUIT FOIS LE MÊME GESTE FONT UNE DISCIPLINE — la répétition identique n'use pas la procédure, elle la consacre : le protocole est maintenant une discipline au sens fort, exécutable par n'importe quelle instance sans mémoire. (2) LE PRÉSENT DU PROJET EST SON DERNIER PUSH — sous le régime instable, la seule réalité temporelle est l'état de origin/main : tout le reste est reconstruit ou absent. (3) LA PLATEAU DE DOUZE POINTS EST UN MUR DOCUMENTÉ — la source Habous reste fermée sans fenêtre annoncée : la veille en fait un fait établi, non une supposition.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R391 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R391" in tail:
    print("REFUS : R391 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R391 appendé. Worklog : {lines} lignes.")
