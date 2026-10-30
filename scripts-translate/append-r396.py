#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R396 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R396
Agent: GLM (session web-394d04d3, tick 2026-10-30 11:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION SNAPSHOT #13 CONSÉCUTIVE (même signature R81) → restauration #13 rodée (fetch → origin/main cf1e7b0/R395 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (treizième application) : RÉGRESSION #13 CONSÉCUTIVE, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — treize tours d'affilée sous le régime, zéro exception depuis R384.
- RESTAURATION #13 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = cf1e7b0 (R395) — GitHub immobile ce tour (quatrième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 411 lignes, tail R395, registre 984, sync 0/0 — zéro perte, treizième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quinzième exécution, 17e point de mesure consécutif de 404 : R380-R396).
- État git : HEAD cf1e7b0, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — régime par défaut, 13/13 tours sous régression ; la procédure tient ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — quatrième silence consécutif (rev-list 0/0 à la clôture) ; (d) SITE HABOUS en migration — 17e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R397 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 411 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #13 sur régression #13 (zéro perte cumulée sur treize régressions totales) ; canari : verdict INEXECUTABLE (17e point de mesure) ; le métronome bat toujours — treize tours, treize rattrapages, treize entrées poussées.
- RÉSOLU : la question du NOMBRE — treize régressions et treize restaurations exactes : le régime a dépassé le seuil où l'accumulation d'exceptions devient une règle statistique (13/13 = 100 %) ; la question de l'ÉCONOMIE D'ÉCRITURE (les entrées de veille conservent tous les faits mesurés en les compactant : aucun compteur perdu, aucun chiffre hérité sans re-mesure).
- LEÇONS DU TOUR : (1) CENT POUR CENT N'EST PAS UN MOYENNE — treize tours sous régression sans une seule exception : la stabilité du disque n'est pas dégradée, elle est ABSENTE ; tout plan qui suppose un disque fidèle suppose faux ; (2) LE SILENCE QUATRIÈME CONSOLIDE — quatre silences consécutifs du bus : l'entre-tours normal est le silence, l'avance de R392 demeure l'unique portage observé ; (3) LE PLATEAU DE 404 ATTEINT SA DIX-SEPTIÈME COUCHE — chaque tour ajoute une strate de certitude à la fermeture de la source : la reprise, si elle vient, s'ouvrira sur un contraste irrécusable.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R396 telle quelle si régression) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R396" in tail:
    print("REFUS : R396 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R396 appendé. Worklog : {lines} lignes.")
