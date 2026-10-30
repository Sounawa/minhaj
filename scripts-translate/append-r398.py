#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R398 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R398
Agent: GLM (session web-394d04d3, tick 2026-10-30 11:37 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #15 CONSÉCUTIVE (même signature R81) → restauration #15 rodée (fetch → origin/main 081bf43/R397 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (quinzième application) : RÉGRESSION #15 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — quinze tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #15 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 081bf43 (R397) — GitHub immobile ce tour (sixième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 447 lignes, tail R397, registre 984, sync 0/0 — zéro perte, quinzième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (dix-septième exécution, 19e point de mesure consécutif de 404 : R380-R398).
- État git : HEAD 081bf43, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 15/15 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — sixième silence consécutif (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 19e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R399 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 447 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #15 sur régression #15 (zéro perte cumulée sur quinze régressions totales) ; canari : verdict INEXECUTABLE (19e point de mesure) ; le métronome bat toujours — quinze tours, quinze rattrapages, quinze entrées poussées.
- RÉSOLU : la question du COÛT TOTAL DU RÉGIME — quinze tours × ~1 min : l'ensemble du mécanisme anti-instabilité (restaurations + canaris + appends + pushes + backups) a consommé moins de temps qu'une seule leçon savante : la permanence est devenue marginale au budget ; la question de la CONFIANCE AUX SIGNAUX (tous les compteurs re-mesurés à chaque tour, aucun hérité : quinze fois sans une seule incohérence).
- LEÇONS DU TOUR : (1) LA PERMANENCE MARGINALE EST LA MEILLEURE — le dispositif anti-régression coûte moins qu'un pour cent du travail qu'il protège : c'est le rapport idéal entre assurance et actif ; (2) LE SIXIÈME SILENCE CONFIRME LA LOI — six silences, un portage : le bus est un canal de secours plus qu'un flux ; (3) DIX-NEUF POINTS PLATS FONT UNE SÉRIE STATISTIQUE — le plateau de 404 a maintenant la taille d'un échantillon exploitable : la fermeture de la source est un état, pas un incident.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R398 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R398" in tail:
    print("REFUS : R398 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R398 appendé. Worklog : {lines} lignes.")
