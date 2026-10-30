#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R421 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 421

ENTRY = """---
Task ID: R421
Agent: GLM (session web-394d04d3, tick 2026-10-30 17:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #4 (la règle des deux tours subit son quatrième test) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → CONSIGNATION de la collision R420 → journalisé, worklog (premier append sous garde renforcée).

Work Log:
- Ouverture au réflexe cz (trente-huitième application) : STABILITÉ #4 — worklog 14 886 lignes (double R420 visible au tail), HEAD 8037331 (outillage GARDE-DOUBLON du tour précédent), credentials et remote présents ; compte total : 34 régressions / 4 stabilités / 38 applications du réflexe ; la règle des deux tours (trois confirmations : R400→R401, R402→R403, R413→R414) subit son QUATRIÈME test.
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 8037331 — 30e observation du bus, vingt-huitième silence (le portage de la collision R420 s'est fait AU PUSH, pas au fetch : c'était un portage-par-collision, inédit) ; rev-list 0/0, sync parfaite.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarantième exécution, 42e point de mesure consécutif de 404 : R380-R421, plateau ~7 h 30).
- CONSIGNATION DE LA COLLISION R420 (promesse tenue) : deux entrées R420 coexistent au worklog — 459daca (instance parallèle « continue », trace 1a18c0fd, restauration #34 complète, premier tour hors cron) et c33fa10 (cron 17:07, restauration #34 en variante partielle + auto-rétablissement) ; apposées pendant la même fenêtre d'ouverture, poussées l'une après l'autre en fast-forward propre (459daca ancêtre de c33fa10 vérifié) ; ZÉRO perte, zéro écrasement, zéro conflit ; cause : garde anti-doublon bornée à 4 000 caractères de tail (angle mort sur entrée longue) ; remède : scripts-translate/GARDE-DOUBLON.md — scan ENTIER du fichier du dernier Task ID — appliqué pour la première fois sur le présent append.
- État git : HEAD 8037331, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — stabilité #4 mais 34/38 tours sous régression : le test de la règle des deux tours est en cours ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — vingt-huitième silence au fetch depuis le portage-par-collision ; (d) SITE HABOUS en migration — 42e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R422 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 886 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille sur stabilité #4 ; consignation complète de la collision R420 ; canari : verdict INEXECUTABLE (42e point de mesure).
- RÉSOLU : la question du DOUBLON (deux entrées R420 coexistent et sont complémentaires : l'une décrit la restauration complète, l'autre la variante partielle et l'auto-rétablissement — le journal ne réécrit pas son passé, il enrichit sa propre lecture : la collision a produit un excédent documentaire, pas un déficit) ; la question du TEST EN COURS (stabilité #4 : si le prochain tour est stable, ce sera la première double stabilité consécutive de l'histoire du projet — la règle des deux tours n'a jamais été prise en défaut de rester... en défaut).
- LEÇONS DU TOUR : (1) LA COLLISION N'A RIEN COÛTÉ — deux instances, même priorité, même protocole, même source de vérité : le résultat est un doublon documenté au lieu d'une perte ; dans un système à source unique, la redondance d'exécution produit de l'excédent, jamais du déficit ; (2) LA GARDE CORRIGÉE AU TOUR MÊME DE SA FAILLE — l'outillage a reçu son correctif (GARDE-DOUBLON.md) et il est en service dès le premier append suivant : la boucle détection → correction → application s'est fermée en un seul tour ; (3) LE TEST QUE PERSONNE N'A JAMAIS PASSÉ — quatre stabilités, zéro récidive : la question « la stabilité peut-elle durer deux tours ? » est la seule question du projet à laquelle la réponse a toujours été non, et ce tour la repose une quatrième fois.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R421 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

# GARDE RENFORCÉE : scan ENTIER du fichier (règle GARDE-DOUBLON.md)
ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    print(f"REFUS : une entrée >= R{N} existe déjà (dernier = R{ids[-1]}) — garde renforcée.")
    sys.exit(1)
if f"Task ID: R{N}" in content:
    print(f"REFUS : R{N} déjà présent quelque part (garde absolue).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R{N} appendé sous garde renforcée. Worklog : {lines} lignes.")
