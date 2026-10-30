#!/usr/bin/env python3
# append-r385.py — entrée R385 au worklog (garde anti-doublon : refuse si R385 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R385
Agent: GLM (session web-394d04d3, tick 2026-10-30 08:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : ouverture avec le réflexe nouveau de R384 (cohérence locale D'ABORD) → RÉGRESSION SNAPSHOT RÉCURRENT DÉTECTÉE (2e fois en quinze minutes : R81/5 631 lignes, remote disparu, credentials absents) → procédure rodée de R384 appliquée TELLE QUELLE (credentials → remote → fetch → ancêtre → reset --hard EN AVANT vers 0e39047/R384) → restauration vérifiée → canari exécuté (verdict INEXECUTABLE) → récurrence journalisée, worklog.

Work Log:
- Ouverture au réflexe nouveau (leçon de R384, appliquée à la lettre) : cohérence locale D'AVANT le fetch — wc -l : 5 631 lignes ; tail : priorités de l'époque R81 (« hadith-1es leçons 4-6… ») ; git remote -v : VIDE ; ~/.git-credentials : ABSENT ; HEAD : 719111b — LA MÊME RÉGRESSION QUE R384, QUINZE MINUTES PLUS TARD : le snapshot régresse de façon RÉCURRENTE, pas incidentelle ; la restauration de R384 n'a pas « réparé » l'environnement : elle a rattrapé le disque sur GitHub, et l'environnement est reparti en arrière depuis.
- RESTAURATION #2 EXÉCUTÉE TELLE QUELLE (la procédure écrite à R384, cette fois sans exploration) : (1) ~/.git-credentials reconstruit (même token, même format) ; (2) origin re-créé ; (3) fetch — origin/main = 0e39047 (R384), EXACTEMENT le dernier état poussé au tour précédent : GitHub n'a pas bougé entre les deux régressions ; (4) ancêtre confirmé → reset --hard EN AVANT ; (5) post-restauration : worklog 14 212 lignes, tail R384, registre 984, sync 0/0 — ZÉRO perte, encore.
- CANARI EXÉCUTÉ APRÈS RESTAURATION (règles cx-cy, priorité du tail R384) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (quatrième exécution, 6e point de mesure consécutif de 404 : R380-R385).
- Diagnostic à DEUX INSTABILITÉS (précisé) : (a) l'INSTABILITÉ LOCALE — le snapshot de la sandbox régresse au moins toutes les quinze minutes vers l'état R81 ; la défense tient en une ligne : GitHub est la source de vérité, le local se rattrape EN AVANT à chaque ouverture ; le coût est descendu à ~une minute (procédure rodée, zéro exploration) ; (b) l'INSTABILITÉ SOURCE — la migration Habous (nginx 1.31.8, 404 sur la série, coquille vivante) : 6e point de mesure, inchangée ; les deux instabilités sont indépendantes, chacune a sa défense rodée.
- État git post-restauration : HEAD 0e39047, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — RÉCURRENCE CONFIRMÉE : TOUTE ouverture doit supposer le local régressé jusqu'à preuve du contraire (le réflexe R384 devient reflexe permanent : cohérence locale d'abord, fetch ensuite) ; (b) TOKEN — re-testé fonctionnel au fetch de ce tour ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 6e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R386 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 212 avant cette entrée).

Stage Summary:
- LIVRÉ : RESTAURATION #2 (la récurrence de l'instabilité locale prouvée par les faits : deuxième régression snapshot complète en quinze minutes, même signature — R81/5 631 lignes, remote disparu, credentials absents) : la procédure rodée à R384 appliquée telle quelle en ~une minute, zéro exploration, zéro perte ; canari ensuite : verdict INEXECUTABLE (6e point de mesure) ; le journal continue de tourner pendant que l'environnement décroche — c'est exactement sa fonction.
- RÉSOLU : la question de la RÉCURRENCE (la régression n'était pas un incident unique : c'est un état de l'environnement, à supposer présent À CHAQUE ouverture jusqu'à preuve du contraire) ; la question du COÛT de la défense (une minute et quatre commandes : la continuité est devenue bon marché) ; la question de la SÉCURITÉ du patrimoine (deux régressions totales du disque, zéro perte cumulée — GitHub rend tout, à chaque fois, en avant).
- LEÇONS DU TOUR : (1) UNE RÉGRESSION N'EST PAS UN ÉVÉNEMENT, C'EST UN RÉGIME — la deuxième chute en quinze minutes change la nature du diagnostic : on ne « répare » plus une panne, on vit sous un régime instable et on s'organise en conséquence (supposer, vérifier, rattraper). (2) LA PROCÉDURE ÉCRITE RÉTRÉCIT LE TEMPS — R384 a exploré, R385 applique : de deux minutes d'analyse à une minute de gestes ; la deuxième exécution d'une procédure est sa vraie naissance. (3) LE JOURNAL EST LE SEUL HABITANT PERMANENT — le disque décroche toutes les quinze minutes, GitHub tient, le worklog raconte : la continuité du projet n'habite nulle part, elle est ce flux d'entrées poussées.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe permanent (règle cx-cz nouvelle) : (1) cohérence locale D'ABORD (wc -l worklog.md + tail + git remote -v + ls ~/.git-credentials) — si le local a régressé → procédure R384/R385 telle quelle (credentials → remote → fetch → ancêtre → reset --hard EN AVANT) ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R385" in tail:
    print("REFUS : R385 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R385 appendé. Worklog : {lines} lignes.")
