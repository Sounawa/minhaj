# -*- coding: utf-8 -*-
"""append-r381.py — append de l'entrée R381 au worklog (une seule fois, jamais deux)."""
HOME = '/home/z/my-project'
p = f'{HOME}/worklog.md'
tail = open(p, encoding='utf-8').read()[-400:]
if 'Task ID: R381' in tail:
    raise SystemExit('REFUS : R381 déjà présent au tail — pas de doublon.')

entry = """---
Task ID: R381
Agent: GLM (session web-394d04d3, tick 2026-10-30 07:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : conformité GitHub, ANTI-RESET vérifié, priorité worklog R380 (faraid-tanawi-3 lessons[1] pdf-mut23h2v-311) — VÉRIFICATION DU RASM D'ABORD : INEXÉCUTABLE (pas de cache, 404 re-confirmé) → TOUR DE VEILLE ET DE CONSOLIDATION journalisé (cartographie exhaustive, audit d'intégrité, plan de reprise), worklog.

Work Log:
- Ouverture : worklog 14 131 lignes, tail R380, registre 984 (hand 927 + llm 57), fetch origin → rev-list 0/0 (session-start implicite : Local = GitHub = 9910127) — AUCUNE régression, tous les planchers dépassés (R380 >= R224 ; 984 >= 831 ; 14 131 >= 10 201). Le template cron « hadith-tanawi-1 : 12966, 12967, 12971, 12981… » écarté une VINGT-QUATRIÈME fois.
- Priorité 311 INEXÉCUTABLE (vérifiée d'abord, comme écrit au tail R380) : pdf-mut23h2v-311 « فقه الحجب (2) » — AUCUN cache OCR (content/ocr-cache/ ne contient rien après 310) ET le téléchargement re-testé : HTTP 404. Le site des Habous reste mort pour ses PDF.
- RÉCUPÉRATION TENTÉE (trois voies, toutes mortes ce tour) : (1) variantes d'URL — 2025 au lieu de 2024, .pdf minuscule, préfixe /ar/ : toutes 404 ; (2) WebSearch — la page « كتب مدرسية للتعليم المدرسي العتيق » (14260) trouvée par le moteur répond 404 elle aussi ; (3) navigation agent-browser sur habous.gov.ma — le site répond 200 mais l'accueil ne rend que deux liens (contenu JS lourd, menu non navigable) : les PDF introuvables ce tour. La veille est journalisée : le site peut les re-publier à tout moment, le test de 311 est refait À CHAQUE TOUR AVANT TOUT AUTRE CHOIX.
- CARTOGRAPHIE EXHAUSTIVE (0 pièce exécutable) : les leçons à rasm HTML — 42 restantes, toutes déjà traduites ; les intros à rasm HTML — toutes traduites (faraid-tanawi-3 18693 vérifiée : html 3 294 car, htmlFr 5 550 car, au registre) ; le cache OCR — quatorze docs, TREIZE traduits, 310 le quatorzième : CACHE ÉPUISÉ ; les leçons pdfOnly — 853 restantes, toutes sans rasm ET sans téléchargement possible. Rien à rédiger ce tour.
- AUDIT D'INTÉGRITÉ (tour de consolidation) : registre 984 savants uniques (hand 927 + llm 57), ZÉRO doublon ; ZÉRO docId au registre sans htmlFr avec rasm présent ; ZÉRO htmlFr sans registre — la comptabilité du projet est PARFAITEMENT cohérente d'un bout à l'autre (58 livres JSON + intros + leçons scannés). Récapitulatif global : 1 854 pièces au projet (intros + leçons des 58 livres), 1 001 livrées (984 au registre savant + 17 héritées du protocole pré-registre), 853 restantes pdfOnly sans rasm.
- État git : arbre propre, sync 0/0, les trois derniers commits en chaîne (d964995 → d94ea5f → 9910127) confirmés sur origin/main.
- Règles : (x)-(ch) inchangées ; (f) reconfirmée (94e, inchangée) ; (h) reconfirmée (le tail du worklog EST la priorité — la priorité 311 est à RE-TESTER à chaque tour : cache puis téléchargement, avant tout autre choix) ; (cx) nouvelle règle de veille : SI le site Habous re-publie ses PDF → reprendre faraid-tanawi-3 lessons[1] (311) et dérouler la série farāʾiḍ (310 livrée, 311 la suite directe) ; SINON tour de veille journalisé sans leçon (le principe « mieux vaut une leçon complète » n'est pas violé : AUCUNE leçon ne peut être écrite sans rasm — la garde n'invente pas sa matière).
- Risques : (a) SANDBOX — vigilance de mise ; (b) TOKEN — PAT fonctionnel ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à l'ouverture et à la clôture (aucune course ce tour) ; (d) SITE HABOUS — mort pour ses PDF depuis le tour R380 au moins (deux tours consécutifs de 404) : la reprise du déroulé des 853 pièces dépend de sa republication ou d'une source alternative découverte ; (e) le tail du worklog reste l'autorité de priorité à chaque ouverture.
- Plancher suivant : >= R382 / >= 984 (aucun hand-set ce tour — le registre ne bouge que sur livraison) / lignes réelles mesurées post-append (14 131 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de VEILLE ET DE CONSOLIDATION (aucune leçon — 0 pièce exécutable au projet entier ce tour) : la priorité 311 vérifiée d'abord et renvoyée (pas de cache OCR, 404 re-confirmé) ; la récupération tentée par trois voies (variantes d'URL, WebSearch, navigation directe — toutes mortes) ; la cartographie exhaustive fermée (42 leçons à rasm toutes traduites, intros toutes traduites, cache OCR épuisé, 853 pdfOnly sans rasm) ; l'audit d'intégrité PARFAIT (984 savants uniques, zéro doublon, zéro incohérence registre/JSON — 1 854 pièces au projet, 1 001 livrées) ; la règle de veille (cx) posée : re-tester 311 À CHAQUE TOUR d'abord, reprendre la série farāʾiḍ dès la republication du site.
- RÉSOLU : la question de l'exhaustivité (plus AUCUNE pièce traduisible par le protocole rodé — la cartographie est fermée, chiffres au Work Log) ; la cohérence de la comptabilité (zéro anomalie sur les 58 livres) ; la stratégie de reprise (le test 311 premier à chaque tour, la règle cx).
- LEÇONS DU TOUR : (1) LA GARDE N'INVENTE PAS SA MATIÈRE — le principe « mieux vaut une leçon complète » porte sur la COMPLÉTION, jamais sur la fabrication : sans rasm pas de leçon, et la veille journalisée est un tour plein quand il verrouille l'état et le plan de reprise ; (2) L'OCR N'EST PAS UNE SOURCE, C'EST UN ÉTAT — le cache du 15 octobre a livré 310, le site mort emporte le reste : la matière du protocole est ce qui EXISTE, jamais ce qui pourrait exister ; (3) LA COMPTABILITÉ EST LA CONTINUITÉ — 984 savants sans doublon ni trou : l'ANTI-RESET le plus solide est le registre lui-même, chaque tour le relit en entier avant d'écrire.
- Prochaine priorité : RE-TESTER D'ABORD le rasm de faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») : cache OCR puis téléchargement (le site Habous peut être rétabli à tout moment) ; SI rasm → dérouler la série farāʾiḍ (le protocole OCR : ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu) ; SI sans rasm → tour de veille à nouveau journalisé (règle cx), et re-tester à chaque tour suivant ; VÉRIFIER rev-list 0/0 + git log frais + le titleFr AVANT tout choix ET AU MOMENT du push ; registre attendu 985 à la première livraison ; la règle h tient : le tail du worklog après cette entrée EST la priorité."""

with open(p, 'a', encoding='utf-8') as f:
    f.write(entry + chr(10))

print('OK — R381 appended, lignes:', sum(1 for _ in open(p, encoding='utf-8')))
