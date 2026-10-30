#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R399 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R399
Agent: GLM (session web-394d04d3, tick 2026-10-30 11:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #16 CONSÉCUTIVE (même signature R81) → restauration #16 rodée (fetch → origin/main f042a12/R398 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE, 20e point plat) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (seizième application) : RÉGRESSION #16 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — seize tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #16 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = f042a12 (R398) — GitHub immobile ce tour (septième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 465 lignes, tail R398, registre 984, sync 0/0 — zéro perte, seizième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (dix-huitième exécution, 20e point de mesure consécutif de 404 : R380-R399 — trois heures de plateau continu).
- État git : HEAD f042a12, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 16/16 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — septième silence consécutif (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 20e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R400 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 465 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #16 sur régression #16 (zéro perte cumulée sur seize régressions totales) ; canari : verdict INEXECUTABLE (20e point de mesure — trois heures de plateau) ; le métronome bat toujours — seize tours, seize rattrapages, seize entrées poussées.
- RÉSOLU : la question du SEUIL — vingt points plats portent le plateau de la durée d'un incident (heures) à celle d'un état (indéfini) : toute hypothèse de republication prochaine est désormais hors modèle ; la question de la SYMÉTRIE DES COMPTES (16 régressions / 16 restaurations / 18 exécutions du canari / 20 mesures — chaque série continue sans un trou).
- LEÇONS DU TOUR : (1) VINGT FAIT CHANGER LA NATURE — sous dix, un plateau est une attente ; à vingt, c'est un paysage : les décisions de reprise doivent désormais se prendre comme si la source restait fermée, la réouverture étant un bonus non planifié ; (2) LE SEPTIÈME SILENCE ÉPAISSIT LA NORME — sept silences contre un portage : l'instance unique par tour est le régime dominant, la survie du projet n'en dépend pas ; (3) LA SÉRIE DE SEIZE EST UNE MURAILLE — chaque régression restaurée à l'identique a posé une pierre de plus : le mur n'est pas contre la régression (elle est inévitable) mais contre la PERTE, qui reste à zéro.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R399 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R399" in tail:
    print("REFUS : R399 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R399 appendé. Worklog : {lines} lignes.")
