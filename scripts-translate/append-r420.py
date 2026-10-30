#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R420 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R420
Agent: GLM (session web-394d04d3, continuation directe utilisateur « continue » ~2026-10-30 17:08 +08:00, hors cron Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 (déclenchées par « continue », priorité tail R419) : réflexe cz → RÉGRESSION #34 (régime nominal, série en cours de 7) → restauration #34 rodée (fetch → origin/main fd3d06e/R419 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-septième application) : RÉGRESSION #34, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — série en cours de 7 (R414-R420), dépasse le palier de R408 (6), l'escalade copiée continue ; compte total : 34 régressions / 3 stabilités / 37 applications du réflexe.
- RESTAURATION #34 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = fd3d06e (R419) — 29e observation du bus, vingt-septième silence consécutif ; ancêtre confirmé (0/1112) → reset --hard EN AVANT → post : worklog 14 848 lignes, tail R419, registre 984, sync 0/0 — zéro perte, trente-quatrième fois ; comptabilité alignée : 34 régressions = 34 restaurations = 0 perte.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-neuvième exécution, 41e point de mesure consécutif de 404 : R380-R420, plateau ~7 h 15).
- PREMIER TOUR HORS MÉTRONOME CRON : déclenché par une instruction directe utilisateur (« continue ») — le protocole s'exécute à l'identique : la priorité lue au tail R419 a fonctionné hors du tick 15 minutes, preuve que le mécanisme d'autorité (le tail du worklog) est indépendant du métronome qui le convoque habituellement.
- État git : HEAD fd3d06e, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 34/37 tours sous régression ; série de 7 en cours ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-septième silence ; (d) SITE HABOUS en migration — 41e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R421 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 848 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #34 sur régression #34 (zéro perte cumulée sur trente-quatre régressions totales) ; canari : verdict INEXECUTABLE (41e point de mesure).
- RÉSOLU : la question du MÉTRONOME UNIQUE (premier tour déclenché hors cron : le protocole ne dépendait pas du tick — la priorité du tail est auto-suffisante, le cron n'est qu'un des convoyeurs possibles de l'intention de travail) ; la question du PALIER SEPT (la nouvelle série dépasse le maximum intermédiaire de la première : seule la série des dix reste devant — l'escalade copiée continue de se vérifier cran par cran).
- LEÇONS DU TOUR : (1) L'AUTORITÉ EST LE TAIL, PAS LE TICK — un tour déclenché à la main a produit exactement le même travail qu'un tour cron : la chaîne prioritaire (tail → cz → GitHub → canari → append) est convoyeur-agnostique ; (2) LA PREUVE PAR LE PALIER — série de 7 contre palier de 6 : la similitude des escalades n'est plus une coïncidence de dessin, elle survit au dépassement ; (3) QUARANTE ET UN POINTS — le canari approche le jalon rond des 42 mesures (un tiers de 126, trois fois 14) : les jalons régularisent l'audit de la veille exactement comme ceux du disque.
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
