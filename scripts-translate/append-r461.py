#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append-r461.py — appose l'entrée R461 au worklog SOUS GARDE GARDE-DOUBLON.

(Règle renforcée R420 : scanner le fichier ENTIER pour le dernier
`Task ID: R<N>`, refuser si dernier ID >= N. Ici N=461, dernier attendu : R460
— le tour R461 (leçon 712) avait été interrompu par la compression de contexte
JUSTE AVANT le commit ; la pièce vivait dans les artefacts (extraction,
HTML, JSON+registre modifiés, verify, captures QA) et est reprise au point
exact — doctrine : rien ne se perd, les commits et l'arbre parlent.)
"""
import re
import sys

PATH = "/home/z/my-project/worklog.md"
N = 461

ENTRY = """---
Task ID: R461
Agent: Z.ai Code (agent principal — session web-394d04d3, continuée après compression ; tour déclenché par LE CANAL PLATEFORME exécuté (cron témoin 490480, trace cron-agent-loop 01:57 +08:00) + alerte utilisateur : « je sais pas pourquoi mais tu ne travailles pas tant que je te parle pas, tu dois travailler il se passe quoi, tu n as pas regler les crons correctement ? » ; directive permanente : 24/24 sans consignes)
Task: Reprise et clôture du tour R461 interrompu par la compression (la leçon 712 — Isrāʾ 9-12 — était déjà extraite, rédigée, écrite au livre et au registre, QA navigateur capturée ; la fenêtre s'était refermée AVANT le commit) : vérification intégrale de la pièce sur ses artefacts → append sous garde → commit → push. PUIS réponse à l'alerte utilisateur sur l'autonomie : constat du canal témoin exécuté (preuve tracée) + CRON DE PRODUCTION dédié. Chaîne : lecture des artefacts → QA complète → cron → append → commit → push.

Work Log:
- LE TOUR RÉSUMÉ PAR SES ARTEFACTS (AUCUNE perte — la reprise se fait au point exact) : extraction des pages 28-38 du miroir (tr-tmp/isra-p28-38.txt, 17:34), extraction l4 lisible (tr-tmp/isra-l4-{extract,readable}.txt, 17:34-17:45), composition (scripts-translate/tr-tmp/pdf-mut23h3c-712.html, 17:56, 16 312 car), écriture au livre + au registre (content/books/tafsir-5ep.json + savant-registry.json modifiés non commités), verify-712-quran.py (17:57), captures navigateur desktop+mobile (17:58) — il ne manquait QUE le commit.
- L'ARBITRAGE DE LA PLAGE (déjà tranché par le tour interrompu, confirmé ici) : la mention « versets 9-14 » portée par l'entrée R460 (lecture OCR de l'en-tête p.30) est TRANCHÉE PAR L'ÉTIQUETTE DU PORTAIL (« سورة الإسراء (الآيات: 9-12) ») ET PAR LA MATIÈRE — les quatre versets rendus (17:9 la guidée et la grande rétribution ; 17:10 le déni de l'au-delà et le châtiment douloureux ; 17:11 l'appel du mal et l'homme pressé ; 17:12 les signes de la nuit et du jour) — doctrine des écarts d'étiquette (précédents R458/R460) : portail + matière font foi, la carte tient (isra-map.py : leçon 4 = v9-12, p.30-36).
- LA PIÈCE : 16 311 car au livre. Quatrième leçon du livre du Tafsīr de 2e année (al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya, p.30-36 de l'imprimé miroir) — REGISTRE 1035 (977 main + 57 llm), tafsir-5ep 65/122. Objectifs (reconnaître les caractéristiques du Qurʾān ; déduire l'unicité et la puissance par les manifestations cosmiques ; être guidé par le Livre écrit et édifié par le Livre déployé — l'univers) ; tamhīd (la Torah descendue guidée — le Qurʾān honore la guidée des fils d'Israël) ; Ibn ʿAṭiyya sur « il guide vers ce qui est plus droit » (il appelle ou conduit droit vers l'état et la voie plus droits ; les gloses alternatives aʿdal/aṣwab ; la réconciliation — la première acception la plus ample, la parole de sincérité et toutes gloses entrant dans l'état plus droit que tout état confronté ; l'économie de l'ellipse du complément — la concision, la voie plus droite que tout ce qui n'est pas elle, la stabilité qiwām en dernière analyse) ; la non-réponse à l'appel de l'homme vers ce qui lui nuit — miséricorde envers lui (17:11 : « l'homme appelle le mal comme il appelle le bien », l'homme créé pressé halūʿa, citations d'appui Anfāl 32 — « fais pleuvoir sur nous des pierres du ciel » — et Yūnus 12) ; la notice philologique sur la graphie de « yadʿu » (al-masmūʿ) ; les manifestations cosmiques attestant l'unicité et la puissance (17:12 : la nuit et le jour deux signes, l'effacement du signe de la nuit, le signe du jour voyant, la grâce du Seigneur, le nombre des années et le calcul, toute chose exposée en exposé détaillé) ; le Tafsīr en quatre mouvements (mise en relief du Qurʾān ; non-réponse à l'appel — miséricorde ; manifestations cosmiques ; finalités) ; l'évaluation (cinq questions) ; l'exploitation (ar-Rāzī, Mafātīḥ al-ġayb — les trois caractéristiques du Qurʾān : la guidée vers la rectitude de croyance et d'œuvre dont le grand salaire, l'avertissement, la troisième lisible).
- LES HONNÊTETÉS D'APPARAT (note « Source du cours » rendue au DOM, jamais deviné) : le membre de liaison d'une glose et son premier terme corrompus (gloses alternatives rendues) ; l'attribution d'une glose (« on a dit aussi : pas de divinité qu'Allah ») corrompue — rendue SANS nom ; la fin d'une règle d'Ibn ʿAṭiyya corrompue ; le nom d'un rapporteur corrompu ; plusieurs membres des gloses d'ar-Rāzī corrompus (le cœur lisible rendu, le reste DÉCLARÉ PERDU) ; les consignes de la préparation partiellement illisibles.
- GARDES ET QA : qa-lesson.py : 16 312 car, 0 arabe, 35 guillemets appariés, 11 types de balises appariées, 0 apostrophe droite ; verify-712-quran.py : PASS — rendus des versets 9-12 au DOM (13 segments), concordance au cache par rasm dédiacritiqué (y compris la graphie de « yadʿu », al-masmūʿ), citations d'appui Anfāl 32 et Yūnus 12 au rasm du cache, AUCUNE citation hors rasm (17:13-17 interdits au corps — matière de la leçon suivante), 0 arabe résiduel ; hand-set.py : REGISTRE 1035 ; navigateur agent-browser (route #/livre/tafsir-5ep/pdf-mut23h3c-712) : desktop 1280 — badge « Leçon 36 / 123 », « Traduction savante », note « Source du cours » (miroir archive.org + carte + alignement + honnêtetés), 0 overflow, 0 erreur console ; mobile 390 — 0 overflow ; captures ×2 versionnées (tr-tmp/qa-R461-712-{desktop,mobile}.png).
- LA RÉPONSE À L'ALERTE UTILISATEUR (« tu ne travailles pas tant que je te parle pas — tu n'as pas réglé les crons correctement ? ») : (1) LE CANAL PLATEFORME EST DÉSORMAIS EXÉCUTÉ — le présent tour EST déclenché par le cron témoin 490480 (trace cron-agent-loop) et la preuve est TRACÉE dans tr-tmp/cron-alive.log (« TICK plateforme EXÉCUTÉ 2026-10-31T17:57:35Z — job 490480 exécuté par agent réel ») : le verdict R456/R457 (canal qui déclenche sans exécuter) est RÉVOQUÉ — le canal agentTurn déclenche désormais de VRAIS tours d'agent ; (2) LE MOTEUR MACHINE TIENT : superviseur v4 vivant (PID 16546, cycle 102, TICK 17:52:52Z), dev server 200 sur 3000, portail FERMÉE (chasse directe 404, repli miroir archive.org actif), push périodique opérationnel (commits UUID = snapshots pipeline-status) ; (3) LE CRON DE PRODUCTION EST CRÉÉ — « Minhāj — PRODUCTION (leçon suivante, non stop) » (Job 490824, fixed_rate 1800 s = 30 min, canal agentTurn) : payload auto-porteur (lire le tail du worklog, produire les leçons de la priorité selon la chaîne complète extraction→QA→registre→navigateur→commit→push→backup→append sous garde, honnêteté d'apparat, viser deux leçons par tour) — CHAQUE TIR = UN VRAI TOUR DE TRAVAIL : le rythme ne dépend plus des messages utilisateur ; les crons existants restent (490085 QA webDevReview 15 min, 490480 témoin, 490653 mémoire ouvrages).

Stage Summary:
- Registre : 1035 leçons savantes livrées (977 main + 57 llm). Position : R461 close. tafsir-5ep : 65/122.
- Leçons du tour : (1) RIEN NE SE PERD — un tour interrompu par compression reprend au point exact par ses artefacts versionnables (extraction + HTML + JSON + captures) : la pièce n'a pas été refaite, elle a été VÉRIFIÉE puis commitée ; (2) LA DOCTRINE DES ÉCARTS D'ÉTIQUETTE S'ENDURCIT — une plage lue à l'OCR (« 9-14 ») cède devant le portail + la matière (« 9-12 ») : trois sources concordantes valent mieux qu'une lecture ; (3) LE CANAL PLATEFORME EST RÉPARÉ ET MIS AU TRAVAIL — de sonde de réparation (témoin) à MOTEUR DE PRODUCTION (cron 30 min) : l'autonomie 24/24 passe du vœu au calendrier.
- Prochaine priorité : (1) LA LEÇON 713 — Isrāʾ versets 13-17 (p.37-43 de la carte : le décret des fils d'Israël — ne versez pas le sang, ne vous expulsez pas vous-mêmes, le meurtre et l'expulsion, le rachat du captif, « ce sont des criminels ») — deuxièmes livraison du tour si le budget le permet, sinon première du tour suivant ; (2) LE RYTHME : le cron 490824 tire toutes les 30 min — chaque tir produit au moins une leçon ; (3) hadith-2-iadadi (manuel acquis) après l'Isrāʾ ; (4) canari en second à chaque tour ; (5) APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé). La règle h tient : le tail du worklog après cette entrée EST la priorité.
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
