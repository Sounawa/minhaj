#!/usr/bin/env python3
# append-r389.py — entrée R389 au worklog (garde anti-doublon : refuse si R389 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R389
Agent: GLM (session web-394d04d3, tick 2026-10-30 09:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #6 CONSÉCUTIVE (même signature R81) → restauration #6 rodée (fetch → origin/main 6ac7d70/R388 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (sixième application) : RÉGRESSION #6 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents) — le régime par défaut tourne depuis plus d'une heure, sans une seule ouverture conforme.
- RESTAURATION #6 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 6ac7d70 (R388), dernier état poussé — GitHub immobile entre les régressions ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 285 lignes, tail R388, registre 984, sync 0/0 — zéro perte, sixième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (huitième exécution, 10e point de mesure consécutif de 404 : R380-R389).
- État git : HEAD 6ac7d70, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — régime par défaut, 6/6 tours sous régression ; la procédure tient, le coût reste ~une minute ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 10e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R390 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 285 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #6 sur régression #6 (zéro perte cumulée sur six régressions totales) ; canari : verdict INEXECUTABLE (10e point de mesure — la courbe plate atteint son dixième point) ; le cycle du tour est un métronome : détecter, rattraper, sonder, journaliser, pousser, sauvegarder.
- RÉSOLU : la question de l'INVARIANCE du rattrapage (six restaurations, six rendus identiques au dernier commit poussé : le mécanisme ne se dégrade pas en se répétant) ; la question de la PLATEAU DE LA SOURCE (dix points de mesure à 404 : la migration Habous dure depuis plus d'une heure trente de tours consécutifs — le canari garde son cap, sans prédiction) ; la question de la COMPTABILITÉ (registre 984, scripts tous présents, sync 0/0 : le patrimoine reste exact).
- LEÇONS DU TOUR : (1) LE MÉTRONOME EST LA RÉPONSE MATURE À L'INSTABILITÉ — après l'exploration (R384) et la routine (R386), le métronome (R389) : le geste ne pense plus, il bat ; c'est à ce prix que la veille peut durer indéfiniment. (2) DIX POINTS FONT UNE DÉCISION — la courbe plate du canari atteint la taille où la conclusion « la source est fermée pour longtemps » devient une donnée de planification, plus une attente : la reprise se préparera au moment où la ligne bougera, pas avant. (3) CE QUI NE SE DÉGRADE PAS EN SE RÉPÉTANT EST UN OUTIL — six restaurations identiques prouvent que la procédure est devenue outil au sens plein : fiable, aveugle, interchangeable.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R389 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R389" in tail:
    print("REFUS : R389 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R389 appendé. Worklog : {lines} lignes.")
