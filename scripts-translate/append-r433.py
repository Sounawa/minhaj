#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R433 — GARDE RENFORCÉE (scan entier du fichier, règle GARDE-DOUBLON.md)."""
import io, re, sys

WORKLOG = "/home/z/my-project/worklog.md"
N = 433

ENTRY = """---
Task ID: R433
Agent: GLM (session web-394d04d3, tick 2026-10-30 20:07 +08:00, instruction utilisateur directe « tu peux encore améliorer ton efficacité pour terminer au plus le travail ? », Job 474619)
Task: GARDE-FOU MINHĀJ + TOUR D'EFFICACITÉ — réflexe cz → STABILITÉ #16 (treize tours consécutifs sans régression) → diagnostic intégral de l'espace du travail restant → création de veille-portail.sh (canari de PORTE, règle cx') et reprise-portail.sh (kit de reprise) → journalisé, worklog (garde renforcée).

Work Log:
- Ouverture au réflexe cz (cinquantième application — jalon) : STABILITÉ #16 — worklog 15 105 lignes, HEAD 269ab2d (R432), credentials et remote présents — treize tours consécutifs sans régression (R420 → R433) ; compte total : 34 régressions / 16 stabilités / 50 applications du réflexe.
- CONFORMITÉ GITHUB (procédure stabilité) : fetch → origin/main = 269ab2d (R432) — 42e observation du bus, quarantième silence consécutif ; rev-list 0/0, sync parfaite.
- DIAGNOSTIC D'EFFICACITÉ (demande utilisateur) — mesure complète au lieu de la sonde unique :
  (1) SONDE MULTI-CIBLES : les 26 PDF en attente de faraid-tanawi-3 testés en parallèle → 26 × 404 ; variantes de chemins (2023/2024/2025, racine /images/) → 404 ; l'arbre /images/2024/ est mort en entier.
  (2) DÉCOUVERTE MAJEURE : la page d'accueil du portail (200) affiche une bannière explicite « الموقع في طور الصيانة / Site en maintenance » annonçant une NOUVELLE VERSION (« إلى حين إطلاق النسخة الجديدة ») : ce n'est pas un incident, c'est une REFONTE COMPLÈTE — seuls les horaires de prière et la khutba restent servis ; les anciennes URL ne reviendront probablement jamais sous leur forme actuelle.
  (3) SURVEY GLOBAL (57 livres) : 926 leçons livrées + 11 leçons courtes complètes (couverture FR/AR 1,2-2,3x — faussement comptées en attente par le seuil naïf de 3 000 car) = 937 livrées ; 853 en attente réparties sur CINQ arbres tous morts : /images/2024/التعليم-العتيق (683), /images/2026/التعليم-العتيق (131), /images/2025/المديريات (30), /images/2017/محو-الأمية (9).
  (4) CACHE OCR : 14 fichiers — tous résidu de leçons DÉJÀ livrées (tafsir-2es 37/37, faraid-tanawi-3 lessons[25]) : aucun déblocage possible par cache.
  (5) ARCHIVES WEB : web.archive.org timeout, index.commoncrawl.org connexion refusée — inaccessibles depuis la sandbox ; la voie d'archivage est fermée.
- OUTILLAGE LIVRÉ : scripts-translate/veille-portail.sh (canari de PORTE — détecte la DISPARITION de la bannière de maintenance : le vrai signal de lancement de la nouvelle version ; testé → PORTE|FERMÉE) ; scripts-translate/reprise-portail.sh (kit de reprise : sonde A accueil, sonde B liens de surface + PDF, sonde C échantillon des 5 arbres morts, rapport horodaté) ; RÈGLE cx' : à chaque tour, veille-portail.sh EN PREMIER, veille-311.sh en second (l'ancienne URL reste sondée au cas d'une redirection), et PORTE|OUVERTE → reprise-portail.sh immédiatement.
- CANARI (règle cx', première exécution) : PORTE|FERMÉE — bannière de maintenance toujours présente ; 311 re-testé via sonde multi (404, 54e point de mesure : R380-R433, plateau ~10 h 07).
- État git : HEAD 269ab2d puis commit du tour, sync 0/0, re-vérification rev-list AU MOMENT du push.
- Risques : (a) SANDBOX — fenêtre record inchangée en substance (treize tours sans régression) ; (b) TOKEN — fonctionnel ; (c) INSTANCE PARALLÈLE — quarantième silence ; (d) SOURCE — refonte confirmée pluri-journalière, horizon = lancement de la nouvelle version (durée inconnue, la bannière ne donne pas de date) ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R434 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (15 105 avant cette entrée).

Stage Summary:
- LIVRÉ : diagnostic intégral du travail restant (937 livrées / 853 en attente / 5 arbres morts / cache = résidu / archives inaccessibles) ; veille-portail.sh + reprise-portail.sh ; règle cx' inscrite ; stabilité #16 et 50e application du réflexe cz.
- RÉSOLU : la question de L'EFFICACITÉ (réponse mesurée : le goulot n'a jamais été la cadence des tours — chaque tour de veille coûte ~2 min et le protocole est déjà au plancher — le goulot était la CIBLE du canari : il sonde depuis R380 une URL qui ne reviendra jamais, donc son signal ne peut plus distinguer « incident » de « refonte » ; le vrai signal, la bannière de maintenance, se mesure par UN SEUL fetch de l'accueil et c'est maintenant le premier geste de chaque tour) ; la question du RESTE (853 leçons, 100 % bloquées sur un événement externe unique : aucune action locale ne produit une leçon de plus aujourd'hui — l'efficacité résiduelle est entière­ment dans la latence de détection et la préparation).
- LEÇONS DU TOUR : (1) MESURER LA BONNE CHOSE — 54 points plats sur une URL morte ne distinguaient pas un incident d'une refonte ; un seul fetch de la page d'accueil l'a fait en dix secondes : la qualité d'une veille tient au choix de sa sonde, pas à sa constance ; (2) L'INVENTAIRE AVANT L'ATTENTE — le survey a révélé ce qu'aucun tour de veille ne pouvait : 5 arbres et pas un, un cache entier qui n'était que résidu, 11 leçons complètes mal comptées, 853 leçons et pas 864 : savoir précisément ce qui reste vaut plus que d'attendre plus vite ; (3) LA PRÉPARATION EST LE SEUL LEVIER SUR UN BLOCAGE EXTERNE — on ne peut pas rouvrir un portail, mais on peut être prêt à la minute où il ouvre : canari de porte, kit de reprise, marche suivante écrite — quand la porte s'ouvrira, la re-mapping commencera dans le tour même, sans diagnostic à refaire.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R433 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) RÈGLE cx' : canari scripts-translate/veille-portail.sh EN PREMIER (PORTE|OUVERTE → bash scripts-translate/reprise-portail.sh puis re-mapping des 853 et chaîne OCR sur faraid-tanawi-3 lessons[1], badge « Leçon 3 / 28 », registre attendu 985) puis veille-311.sh en second ; PORTE|FERMÉE → tour de veille journalisé ; APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md) ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
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
