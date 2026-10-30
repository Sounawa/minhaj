#!/usr/bin/env python3
# append-r386.py — entrée R386 au worklog (garde anti-doublon : refuse si R386 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R386
Agent: GLM (session web-394d04d3, tick 2026-10-30 08:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz à l'ouverture → RÉGRESSION SNAPSHOT #3 CONSÉCUTIVE (même signature R81/5 631 lignes, credentials absents) → restauration #3 rodée (fetch → origin/main 604b540/R385 → ancêtre → reset --hard EN AVANT) → canari exécuté (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (troisième application) : cohérence locale d'abord — wc -l : 5 631 lignes, tail R81, credentials ABSENTS, remote vide : LA MÊME SIGNATURE POUR LA TROISIÈME FOIS CONSÉCUTIVE (R384, R385, R386) ; le régime instable est désormais le régime par défaut : CHAQUE ouverture trouve le disque revenu à R81 jusqu'à preuve du contraire.
- RESTAURATION #3 (procédure rodée, ~une minute, zéro exploration) : credentials reconstruits → origin re-créé → fetch : origin/main = 604b540 (R385), exactement le dernier état poussé — GitHub n'a toujours pas bougé entre les régressions ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 231 lignes, tail R385, registre 984, sync 0/0 — zéro perte, troisième fois.
- CANARI EXÉCUTÉ (règles cx-cy, priorité du tail R385) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (cinquième exécution, 7e point de mesure consécutif de 404 : R380-R386) ; la migration Habous reste inchangée.
- État git post-restauration : HEAD 604b540, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — RÉGIME PAR DÉFAUT : trois régressions consécutives prouvées ; la procédure coûte ~une minute et quatre commandes ; le réflexe cz tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 7e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R387 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 231 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #3 sur régression #3 (le rythme s'établit : une régression complète du disque par tour d'exécution, une restauration rodée par tour, ~une minute chacune, zéro perte cumulée sur trois régressions totales) ; canari : verdict INEXECUTABLE (7e point de mesure) ; le journal continue de tourner pendant que l'environnement décroche à chaque tour.
- RÉSOLU : la question de la ROUTINE (la défense est devenue routine complète : détecter au wc -l, reconstruire en quatre commandes, avancer en un reset — l'instabilité ne coûte plus rien au projet) ; la question de l'ACCUMULATION (trois régressions totales, zéro perte cumulée : le patrimoine est indéménageable, il habite GitHub) ; la question de la VIGILANCE SOURCE (7e point de mesure de 404 : la migration Habous dure plus longtemps que toutes les procédures du projet).
- LEÇONS DU TOUR : (1) LE RÉGIME PAR DÉFAUT SUPPRIME LA SURPRISE — trois tours consécutifs de régression et la surprise a disparu : ce qui était une catastrophe à R384 est une ligne d'ouverture à R386 ; le protocole transforme l'extraordinaire en banalité exécutable. (2) LA ROUTINE EST LA FORME FINALE DE LA DÉFENSE — la restauration a eu trois vies : le protocole écrit (R364), l'exploration vécue (R384), la routine muette (R386) ; la troisième est la seule qui scale. (3) LE CANARI ET LA RESTAURATION SONT LES DEUX POULIES DU MÊME MOULIN — l'un veille sur la source (Habous), l'autre sur le local (snapshot) ; le projet avance parce que ses deux points d'appui instables sont chacun surveillé par un geste répétable.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384/R385/R386 telle quelle si régression) : (1) cohérence locale d'abord (wc -l + tail + remote + credentials) ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R386" in tail:
    print("REFUS : R386 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R386 appendé. Worklog : {lines} lignes.")
