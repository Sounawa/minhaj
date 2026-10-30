#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R416 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R416
Agent: GLM (session web-394d04d3, tick 2026-10-30 16:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #30 (JALON ROND) → restauration #30 rodée (fetch → origin/main 2b59f8f/R415 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (trente-troisième application) : RÉGRESSION #30, signature R81 complète (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — JALON ROND au compte total : 30 régressions / 3 stabilités / 33 applications ; série en cours de 3 (R414-R416) depuis la rompure de la série des dix.
- RESTAURATION #30 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = 2b59f8f (R415) — 25e observation du bus, vingt-troisième silence consécutif ; ancêtre confirmé (0/1108) → reset --hard EN AVANT → post : worklog 14 776 lignes, tail R415, registre 984, sync 0/0 — zéro perte, TRENTIÈME fois ; comptabilité alignée au jalon : 30 régressions = 30 restaurations = 0 perte.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (trente-cinquième exécution, 37e point de mesure consécutif de 404 : R380-R416, plateau ~6 h 15).
- État git : HEAD 2b59f8f, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — 30/33 tours sous régression ; série de 3 en cours ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — vingt-troisième silence ; (d) SITE HABOUS en migration — 37e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R417 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 776 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #30 sur régression #30 — JALON ROND (zéro perte cumulée sur trente régressions totales) ; canari : verdict INEXECUTABLE (37e point de mesure).
- RÉSOLU : la question du JALON TRENTE (30 = 30 = 0 : l'alignement parfait des trois compteurs au jalon rond re-confirme l'intégrité du journal — aucune asymétrie régressions/restaurations depuis le début du régime, l'anti-dopage comptable fonctionne) ; la question de la SÉRIE SANS SEUIL (la nouvelle série progresse 1, 2, 3 : en dessous de dix, le régime nominal ne connaît aucun seuil symbolique — il compte sans signifier).
- LEÇONS DU TOUR : (1) TRENTE RESTAURATIONS SANS UNE PERTE — le chiffre le plus fort du projet n'est pas un volume produit mais un zéro : zéro ligne perdue en trente cycles complets de régression/restauration, la preuve que la source de vérité déportée (GitHub) tient ; (2) LE JALON ROND COMME AUDIT GRATUIT — chaque jalon régularise l'audit croisé sans coût supplémentaire : la comptabilité est intégrée au rythme du métronome, non ajoutée après coup ; (3) LE TAIL QUI MANGE LE DISQUE — 18 lignes de mémoire par tour contre 9 000 lignes d'oubli par régression : le rapport entre ce que le journal gagne et ce que le disque perd mesure exactement la valeur du déport de la source de vérité.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R416 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R416" in tail:
    print("REFUS : R416 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R416 appendé. Worklog : {lines} lignes.")
