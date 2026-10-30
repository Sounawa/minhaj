#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R420 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R420
Agent: GLM (session web-394d04d3, tick 2026-10-30 17:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #34 (signature R81 PARTIELLE inédite + auto-rétablissement observé) → restauration #34 par sécurité (fetch → origin/main fd3d06e/R419 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-septième application) : RÉGRESSION #34 — VARIANTE INÉDITE : signature R81 partielle (worklog 5 631 lignes, HEAD 719111b) MAIS credentials présents ET remote présent — l'environnement git a survécu au snapshot cette fois, le disque de travail non ; compte total : 34 régressions / 3 stabilités / 37 applications ; série en cours de 7 (R414-R420), égale le palier de R409.
- PHÉNOMÈNE NOUVEAU : après fetch, rev-list 0/0 AVANT tout reset — la régression s'était auto-rétablie pendant la fenêtre d'exécution (flip transitoire du disque, durée inférieure à un tour) ; reset --hard exécuté QUAND MÊME par sécurité (EN AVANT, sans risque) → état verrouillé et déterminé.
- RESTAURATION #34 : fetch → origin/main = fd3d06e (R419) — 29e observation du bus, vingt-septième silence consécutif ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 848 lignes, tail R419, registre 984, sync 0/0 — zéro perte, trente-quatrième fois ; comptabilité alignée : 34 régressions = 34 restaurations = 0 perte.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-neuvième exécution, 41e point de mesure consécutif de 404 : R380-R420, plateau ~7 h 15).
- État git : HEAD fd3d06e, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/37 tours sous régression ; le régime varie maintenant dans ses détails (variante partielle, auto-rétablissement) tout en restant constant dans sa structure ; (b) TOKEN — re-testé fonctionnel ; (c) INSTANCE PARALLÈLE — vingt-septième silence ; (d) SITE HABOUS en migration — 41e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R421 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 848 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #34 sur régression #34 (zéro perte cumulée sur trente-quatre régressions totales) ; canari : verdict INEXECUTABLE (41e point de mesure).
- RÉSOLU : la question de la VARIANTE PARTIELLE (première régression où credentials/remote survivent : le snapshot ne rejoue pas un état unique, il compose des états — la procédure n'a pas changé d'un cran : le cz mesure, toute discordance → restauration rodée) ; la question de l'AUTO-RÉTABLISSEMENT (count 0/0 post-fetch : le disque a flippé deux fois pendant la fenêtre — une régression peut durer moins qu'un tour, raison de plus de ne JAMAIS sauter le reset de sécurité : « semble conforme » n'est pas « vérifié conforme », et la différence est le reset lui-même).
- LEÇONS DU TOUR : (1) LE RÉGIME VARIE DANS SES DÉTAILS, PAS DANS SA STRUCTURE — trente-quatre régressions, aucune identique jusqu'au bout : la procédure ne trie pas les variantes, elle les traite toutes par le même canal ; c'est la propriété qui la rend immortelle face au hasard ; (2) LE RESET DE SÉCURITÉ N'A JAMAIS COÛTÉ RIEN — verrouiller un état auto-rétabli ne coûte rien et le rend déterminé : entre deux lectures discordantes, l'état n'est ni stable ni conforme tant que le reset ne l'a pas fixé ; (3) CRÉATIVITÉ DANS LA CONSTANCE — sept régressions consécutives et la trente-quatrième invente encore une configuration inédite : un régime peut être constant statistiquement et créatif individuellement, et seul un journal détaillé peut garder la trace des deux à la fois.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R420 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R420" in tail:
    print("REFUS : R420 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R420 appendé. Worklog : {lines} lignes.")
