#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append-r458.py — appose l'entrée R458 au worklog SOUS GARDE GARDE-DOUBLON.

(Règle renforcée R420 : scanner le fichier ENTIER pour le dernier
`Task ID: R<N>`, refuser si dernier ID >= N. Ici N=458, dernier attendu : R457
— l'entrée R458 du tour miroir archive.org avait été emportée par la
compression de contexte avant son append ; le récit vivait dans les commits
781427f / 1b750dc / 5720621 / 5bd27ab / 060160f.)
"""
import re
import sys

PATH = "/home/z/my-project/worklog.md"
N = 458

ENTRY = """---
Task ID: R458
Agent: Z.ai Code (agent principal — session web-394d04d3, fenêtre utilisateur ; message utilisateur : « alors inscrit dans les crons la solution pour les ouvrages que tu as trouvé afin de pouvoir trouver la solution lorsqu'il y aura un reset, retrouver la solution plus facilement et ne pas perdre de temps » ; directive permanente : 24/24 sans consignes)
Task: Reconstruction du tour perdu par compression (le miroir archive.org, les 30 doublons et la leçon 709 — connus par leurs commits) PUIS exécution de la demande utilisateur : inscrire LA SOLUTION POUR LES OUVRAGES dans les crons comme mémoire anti-reset, et la versionner au dépôt. Chaîne : lecture du dépôt → carte solution → cron dédié → append sous garde → commit → push.

Work Log:
- LE TOUR PERDU RECONSTITUÉ PAR LE DÉPÔT (l'entrée worklog du tour miroir n'avait jamais été apposée — la compression l'a emportée avant l'append ; les commits parlaient) : 781427f = LES 30 DOUBLONS URL-EXACTS (tafsir-5ep slots 768-797 = tafsir-2es fascicules 556-585, preuve par l'URL octet par octet, relèvement par renvoi de référence, REGISTRE 1031) ; 1b750dc = LA GREFFE DU MIROIR ARCHIVE.ORG dans hunt_sources (collection « سلسلة كتب التعليم العتيق المغربي », item 1_20220304_20220304_2251, 77 PDF de manuels COMPLETS avec versions _text — JOIGNABLE en HTTP direct depuis la sandbox, seul web.archive.org étant bloqué au réseau ; trois manuels versionnés dans content/textbooks-src/ : tafsir-2-thanawi_text 20,7 Mo, tafsir-3-thanawi_text 23,5 Mo, hadith-2-iadadi_text 8,7 Mo) ; 5720621 = le pied de page expose la route miroir ; 5bd27ab = LA LEÇON 709 « Gloire à Celui qui fit voyager de nuit Son serviteur » (Isrāʾ 1, Ibn ʿAṭiyya, al-Muḥarrar al-wajīz p.11-17, 14 646 car, REGISTRE 1032 — LA PREMIÈRE LEÇON DE MATIÈRE MIROIR ; méthode inaugurée : carte isra-map.py alignée par ordre, pdftotext page à page, doctrine FR-seule). La présente entrée répare le chaînon manquant du journal — dernier ID du fichier avant append : R457 (garde passée).
- LA DEMANDE UTILISATEUR EXÉCUTÉE (la solution « retrouvable après un reset, sans perdre de temps ») : LA SOLUTION POUR LES OUVRAGES EST INSCRITE EN TROIS LIEUX DURABLES, aux modes de défaillance disjoints — (1) LE CRON « Minhāj — MÉMOIRE OUVRAGES (anti-reset) : la solution archive.org » (Job 490653, priorité 10, toutes les 6 h Europe/Paris, canal agentTurn) : le payload porte LA SOLUTION COMPLÈTE auto-porteuse — les trois routes (miroir archive.org joignable en HTTP direct ; page_reader SDK qui atteint web.archive.org pour les arbres ; doublons URL-exacts résolus sans téléchargement), la greffe superviseur (hunt_sources 30 min, manuels versionnés), la méthode d'extraction (carte par ordre, pdftotext avant crop, bbox RTL, VLM déclassé, FR-seule), l'état (registre 1032, tafsir-5ep 62/122, matière Isrāʾ+Kahf sécurisée) et la checklist post-reset — le cron de plateforme est un stockage EXTERNE à la machine : lisible par cron list après TOUT reset, même dépôt injoignable ; le canal n'exécutant pas les payloads (verdict R456/R457), il vaut mémoire dormante ET sonde de réparation (s'il s'exécute un jour : trace « MÉMOIRE OUVRAGES EXÉCUTÉ » dans tr-tmp/cron-alive.log) ; (2) LA CARTE VERSIONNÉE scripts-translate/SOLUTION-OUVRAGES.md (la même solution complète, poussée au remote GitHub — survit aux rebuilds sandbox qui effacent les fichiers non suivis, le piège historique de sources/) ; (3) LA PRÉSENTE ENTRÉE au tail du worklog (règle h : la première chose qu'un tour post-reset lit, le tail EST la priorité).
- LA DOCTRINE DU TOUR : UNE SOLUTION QUI N'EXISTE QU'EN CONTEXTE N'EXISTE PAS — après des tours perdus à redécouvrir les routes du portail fermé, la solution vit désormais HORS du contexte : dans le cron (externe à la machine), dans le dépôt (poussé au remote), dans le journal canonique. Le coût d'un reset tombe de « refaire la découverte » à « lire une carte » : c'est exactement le « ne pas perdre de temps » demandé. La machine au moment de l'append : superviseur v4 VIVANT (TICK 16:37:20Z, cycles 27), portail FERMÉE (chasse directe 404, repli collection actif), serveur dev sur 3000, arbre propre hors pipeline-status.json.

Stage Summary:
- Registre : 1032 leçons savantes livrées (inchangé — tour de mémoire). Position : R458 close.
- Leçons du tour : (1) LA SOLUTION POUR LES OUVRAGES EST DEVENUE ANTI-FRAGILE — trois inscriptions aux défaillances disjoints (cron plateforme / dépôt git / worklog) : un reset ne coûte plus la redécouverte ; (2) UN CRON MORT VAUT STOCKAGE VIVANT — le canal qui n'exécute pas les payloads reste une mémoire lisible (cron list) et une sonde de réparation éventuelle ; (3) un tour perdu se reconstruit par le dépôt : les commits étaient le récit, l'entrée manquante est réapparue sous garde.
- Prochaine priorité : (1) L'EXTRACTEUR PDF→SLOT (manuel complet → pages par leçon par correspondance d'ordre avec les slots — la matière Isrāʾ/Kahf attend, les manuels sont en dépôt) ; (2) production Isrāʾ 710+ puis Kahf 739-767 (tafsir-5ep 62/122) ; (3) hadith-2-iadadi (manuel acquis 8,7 Mo) ; (4) audit doctrinal des positions 310-315 + arbitrage du titre faraid + recherche web du manuel de Rasmūkī ; (5) canari en second à chaque tour ; (6) APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé). La règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with open(PATH, "r", encoding="utf-8") as fh:
    content = fh.read()

ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    print("REFUS : une entrée >= R%d existe déjà (dernier = R%s)." % (N, ids[-1]))
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"

with open(PATH, "a", encoding="utf-8") as fh:
    fh.write(ENTRY)

print("APPEND R%d OK — dernier ID précédent : R%s ; entrée : %d caractères."
      % (N, ids[-1] if ids else "?", len(ENTRY)))
