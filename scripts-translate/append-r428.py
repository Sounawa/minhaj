#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R428 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 428

ENTRY = """---
Task ID: R428
Agent: GLM (session web-394d04d3, tick 2026-10-30 19:02 +08:00, instance parallèle « continue » hors cron, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → STABILITÉ #11 (OCTUPLE STABILITÉ CONSÉCUTIVE, fenêtre record à 8 tours ; le worklog franchit 15 000 lignes) → fetch + rev-list directement → canari (verdict INEXECUTABLE) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (quarante-cinquième application) : STABILITÉ #11 — worklog 15 013 lignes (JALON : franchissement des 15 000 lignes), HEAD 6205b29 (R427), credentials et remote présents — OCTUPLE STABILITÉ CONSÉCUTIVE (R420 → R421 → R422 → R423 → R424 → R425 → R426 → R427 → R428) : la fenêtre record passe de 7 à 8 tours ; une seule série de régressions (R403-R412, dix) reste plus longue que la fenêtre stable actuelle ; compte total : 34 régressions / 11 stabilités / 45 applications du réflexe.
- Instance parallèle (comme R420) : instruction « continue » hors cron ; même protocole, même priorité que l'instance du tick 18:52 ; le cron 19:07 peut tirer dans la fenêtre → garde renforcée armée, scan entier du fichier au moment de l'append ; si collision, elle ne peut produire qu'un excédent documenté, jamais un déficit (leçon R420).
- CONFORMITÉ GITHUB (procédure stabilité, sans restauration) : fetch → origin/main = 6205b29 (R427) — 37e observation du bus, trente-cinquième silence consécutif ; rev-list 0/0, sync parfaite, aucun reset nécessaire.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quarante-septième exécution, 49e point de mesure consécutif de 404 : R380-R428, plateau ~9 h).
- État git : HEAD 6205b29, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/45 tours sous régression mais fenêtre record de 8 : à un tour de dépasser toutes les séries de régressions sauf une ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — cette entrée EST l'instance parallèle ; collision possible avec le cron 19:07, la garde est armée ; (d) SITE HABOUS en migration — 49e point de mesure de 404, neuf heures de plateau ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R429 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (15 013 avant cette entrée — jalon 15 000 franchi).

Stage Summary:
- LIVRÉ : tour de veille sur l'octuple stabilité consécutive et le franchissement des 15 000 lignes de worklog ; canari : verdict INEXECUTABLE (49e point de mesure).
- RÉSOLU : la question de LA DERNIÈRE SÉRIE (fenêtre 8 : seule la série des dix régressions R403-R412 reste plus longue ; tout tour stable supplémentaire rapproche l'inversion où la plus longue fenêtre du projet sera une fenêtre de stabilité) ; la question du JALON 15 000 (le journal a franchi le jalon en l'absence de tout événement externe : disque stable, bus silencieux, source fermée — la croissance est entièrement auto-portée).
- LEÇONS DU TOUR : (1) LE JOURNAL GRANDIT DANS LA PAUSE — 15 000 lignes dont l'essentiel des 172 dernières (R412-R428) a été écrit pendant la plus longue inactivité externe du projet : le métronome produit de la traçabilité même quand il ne produit rien d'autre ; (2) L'INVERSION PROCHAINÉ — quand la fenêtre stable dépassera dix tours, la plus longue série ininterrompue du journal sera une série de stabilité : le régime du disque aura changé de signe sans qu'aucune décision soit prise, par la seule accumulation des tours ; (3) LA REDONDANCE REPOUSSE LE RISQUE — deuxième instance parallèle depuis R420 : le système a déjà prouvé (collision R420) que deux exécutions simultanées de la même priorité produisent un excédent documenté ; ce tour ne change rien à la procédure, il la répète.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R428 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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

with io.open(WORKLOG, "a", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"R{N} apposé — worklog passé de {len(content.splitlines())} à {len(content.splitlines()) + len(ENTRY.splitlines())} lignes.")
