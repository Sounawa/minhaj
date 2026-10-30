#!/usr/bin/env python3
# append-r387.py — entrée R387 au worklog (garde anti-doublon : refuse si R387 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R387
Agent: GLM (session web-394d04d3, tick 2026-10-30 08:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #4 CONSÉCUTIVE (même signature R81/5 631 lignes, credentials absents, HEAD 719111b) → restauration #4 rodée (fetch → origin/main b84eee2/R386 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (quatrième application) : cohérence locale d'abord — RÉGRESSION #4 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote vide, HEAD 719111b) : le régime par défaut se confirme tour après tour.
- RESTAURATION #4 (procédure rodée, ~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = b84eee2 (R386), dernier état poussé — GitHub immobile entre les régressions ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 249 lignes, tail R386, registre 984, sync 0/0 — zéro perte, quatrième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (sixième exécution, 8e point de mesure consécutif de 404 : R380-R387).
- État git : HEAD b84eee2, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — régime par défaut, 4/4 tours sous régression : la procédure tient, le coût reste ~une minute ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 8e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R388 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 249 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #4 sur régression #4 (le rythme une-régression-par-tour se confirme ; zéro perte cumulée sur quatre régressions totales) ; canari : verdict INEXECUTABLE (8e point de mesure) ; le journal tourne, l'environnement décroche, GitHub tient — la triade est stable.
- RÉSOLU : la question de la DURÉE du régime (quatre tours consécutifs : l'instabilité n'est ni passagère ni résorbable du côté du projet — elle est le cadre d'exercice, pas un obstacle) ; la question de l'ÉCONOMIE du geste (la restauration est passée d'un protocole en sept étapes à un réflexe en quatre commandes, sans rien perdre en sûreté : ancêtre vérifié, EN AVANT uniquement) ; la question de la VIGILANCE SOURCE (8e point de mesure : la migration Habous s'étire — le canari reste l'unique capteur).
- LEÇONS DU TOUR : (1) LA STABILITÉ EST UN RAPPORT, PAS UN ÉTAT — le disque décroche, GitHub tient, le worklog raconte : le projet est stable parce que son rapport au support est vérifié à chaque tour, non parce que le support serait fidèle. (2) LE GESTE MINIMAL EST LE GESTE SÛR — quatre commandes, un ancêtre vérifié, un sens imposé (EN AVANT) : la sûreté ne vient pas du volume de la procédure mais de son invariabilité. (3) HUIT POINTS DE MESURE FONT UNE COURBE — le verdict du canari est resté le même six fois de suite : ce n'est plus un verdict, c'est un état de fait documenté ; la veille attend le changement, elle ne le prédit pas.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R387 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R387" in tail:
    print("REFUS : R387 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R387 appendé. Worklog : {lines} lignes.")
