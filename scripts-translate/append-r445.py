#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — append worklog R445 (tour de reprise post-convergence) sous GARDE
RENFORCÉE (GARDE-DOUBLON.md) : balayer le fichier ENTIER pour le dernier Task ID,
refuser tout ID >= 445."""
import re
import sys

N = 445
PATH = "/home/z/my-project/worklog.md"
content = open(PATH, encoding="utf-8").read()

ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    print(f"REFUS : une entrée >= R{N} existe déjà (dernier = R{ids[-1]}).")
    sys.exit(1)

entry = """
---
Task ID: R445
Agent: GLM (session web-394d04d3, tick 2026-10-30 23:22 +08:00, Job 487303 — segment de reprise t2 après convergence en direct ; pas de nouvelle pièce ce tour)
Task: GARDE-FOU MINHĀJ — TOUR DE REPRISE POST-CONVERGENCE : la leçon 318 ayant été livrée PENDANT la fenêtre de ce tour par le segment convergent (entrée R444), le présent segment a (1) détecté la collision par l'état git AVANT tout push, (2) restauré les deux fichiers écrasés par git checkout — zéro perte, (3) complété la chaîne interrompue du segment convergent (push du registre 992 resté en attente), (4) backup + canari. AUCUNE nouvelle pièce ce tour — la 319 au prochain tick selon le plancher de R444.

Work Log:
- Ouverture au réflexe cz (cinquante-neuvième application) : tail lu à l'ouverture = R443, leçon 317, registre 991 ; fetch → rev-list 0/0 (HEAD a02bfb3). Le tail désignant la 318, le segment a ouvert le mapping (le ders 13 du bāb 12 du fiqh-3 borné p.105-113 par les deux الإعداد الذهني p.105 et p.114, certifié aux images 150 dpi) et réécrit la pièce indépendamment.
- LA CONVERGENCE EN DIRECT (sixième de la série, la plus serrée) : PENDANT la lecture des images (15:29-15:44 UTC), le segment convergent livrait la MÊME pièce par la MÊME source : verify-318-quran.py apparu tracké et non modifié (15:38) → contrôle git → la 318 DÉJÀ COMMITTÉE (cd630db leçon 28 560 car + 9f80c67 worklog R444, poussés) et le registre 992 committé (5c235de, 15:43:59) mais NON poussé (rev-list 1/0) — le segment convergent s'étant interrompu entre son commit de registre et son push.
- L'ÉCRASEMENT ET LA RESTAURATION (la leçon opérationnelle du tour) : le présent segment avait écrasé deux fichiers DÉJÀ COMMTTÉS par le segment convergent (content/textbooks/fiqh-3-sulh2.txt et scripts-translate/tr-tmp/pdf-mut23h2v-318.html — deux réécritures indépendantes de la même pièce) ; git status montrait « M » sur les deux — le signal de la collision — et git checkout -- les a restaurés à l'identique des versions livrées. ZÉRO perte : la réécriture du présent segment (~24 000 car, même matn, même hadith rendu, même mapping) n'a JAMAIS été committée ni poussée. LEÇON DU TOUR : la garde anti-collision commence par git status — un fichier déjà tracké qui change sous la plume signale le travail committé d'une instance sœur ; lire l'état git AVANT d'écrire, pas seulement avant de pousser. Validation croisée acquise malgré tout : deux traductions indépendantes du même chapitre, même bornage (p.105-113 + الإعداد p.114), même hadith identifié (Umm Salama, Ṣaḥīḥ Muslim, livre des jugements — localisation confirmée par la recherche web des deux côtés).
- CHAÎNE COMPLÉTÉE : push 9f80c67..5c235de (l'inscription hand de pdf-mut23h2v-318 — registre 992 SAVANTS) au premier essai ; rev-list 0/0 re-vérifiée APRÈS push ; backup.sh exécuté (OK : 5c235de) ; canari veille-portail.sh : PORTE|FERMÉE (bannière de maintenance toujours présente) — la production tournant sans le portail.
- État git : HEAD 5c235de poussé, sync 0/0 ; registre 992 ; la leçon 318 comptée — 945 leçons livrées au total.
- Risques : (a) SANDBOX — stabilité #18 continuée (vingt-trois tours sans régression) ; (b) INSTANCE PARALLÈLE — la sixième convergence traitée sans conflit git ni perte ; le risque restant : un tick imminent (~23:37 +08) pouvant lire ce tail frais — le plancher ci-dessous étant à jour ; (c) SOURCE — 8 pièces livrées depuis le miroir (311-318), la 319 mappée d'avance (faraid-2 p.164-174).
- Plancher suivant : >= R446 / registre >= 992 (993 attendu dès la livraison de 319) / 945 leçons livrées / lignes réelles mesurées post-append (15 382 avant cette entrée).

Stage Summary:
- RÉSOLU : la sixième convergence EN DIRECT (même tick, même pièce, deux segments) — réponse : git status AVANT d'écrire ; le travail committé d'une instance sœur se reconnaît à ses fichiers trackés et à son registre ; la restauration par git checkout est sans perte et sans doublon ; la chaîne interrompue se complète par le push du commit en attente (rev-list 1/0 → 0/0). La division du travail du système à journal tient même quand deux segments prennent la MÊME pièce : le premier committé gagne, le second valide par voie indépendante et restaure.
- ÉTAT : la leçon 318 livrée, poussée, backupée (l'entrée R444 en faisant foi) ; registre 992 ; sync 0/0 ; canari PORTE|FERMÉE.
- Prochaine priorité : INCHANGÉE — le plancher de R444 tient : LIVRER LA LEÇON 319 (مسائل الإقرار, « Questions relatives à l'aveu (iqrār) », badge « Leçon 11 / 28 », registre attendu 993) en ouvrant par le mapping (faraid-2 p.164-174, la méthode de correction des deux farīḍa, la ǧāmiʿa, les quatre regards ; les TROIS pièces de l'aveu 319-321 à découper contre l'étendue réelle du chapitre) ; canari en second ; append sous garde renforcée ; rev-list 0/0 AU MOMENT du push.
"""

with open(PATH, "a", encoding="utf-8") as fh:
    fh.write(entry)

print(f"OK : entrée R{N} apposée ({len(entry)} car).")
