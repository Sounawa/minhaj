#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append-r459.py — appose l'entrée R459 au worklog SOUS GARDE GARDE-DOUBLON."""
import re
import sys

PATH = "/home/z/my-project/worklog.md"
N = 459

ENTRY = """---
Task ID: R459
Agent: Z.ai Code (agent principal — session web-394d04d3, fenêtre utilisateur ; message utilisateur : « il faut avancer non stop dans les traductions » ; directive permanente : 24/24 sans consignes)
Task: Production directe sur la priorité inscrite au tail (R458) : LA LEÇON 710 — Isrāʾ versets 2-4 (deuxième leçon du volume, pages 18-23 du manuel miroir tafsir-2-thanawi_text.pdf), matière neuve extraite par la méthode inaugurée à la leçon 709. Chaîne : extraction pdftotext page à page → décodage → arbitration des zones corrompues par sources canoniques web → rédaction savante FR-seule → QA → registre → navigateur → commit → push.

Work Log:
- LA PIÈCE : 13 945 car. La deuxième leçon du livre du Tafsīr de 2e année (al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya, p.18-23 de l'imprimé miroir) : la Torah donnée à Mūsā comme guidée (v2), la descendance de ceux portés avec Nūḥ (v3), le décret des deux corruptions (v4) — REGISTRE 1033 (975 main + 57 llm), tafsir-5ep passe de 62 à 63/122.
- LA DÉCOUVERTE PHILOLOGIQUE DU TOUR : LA LECTURE WARŠ DU VERSET 2 PORTE « WAKĪLAN » (le garant) — le cache coranique, le manuel marocain et les éditions du Muḥarrar concordent (le « ʿiwlan » ḥafṣ n'est pas en jeu dans ce corpus waršien) ; et cette lecture FERME le puzzle iʿrābique du verset 3 : le quatrième aspect du naṣb de « dhurriyyata » est l'APPOSITION DE « WAKĪLAN » — ne prenez pas de garant en dehors de Moi — [c'est-à-dire] une descendance de ceux que Nous portâmes avec Nūḥ : ne prenez pas les humains pour divinités. L'aspect 1 (mafʿūl de « yattakhidhū », sens : qu'un humain ne soit pas pris pour divinité) et l'aspect 4 (apposition) disent la même chose par deux voies syntaxiques ; l'aspect 2 (vocatif, invalide au yāʾ d'al-Ḥasan — la contorsion) et l'aspect 3 (ellipse de « aʿnī ») complètent la série.
- LES ARBITRAGES PAR SOURCES CANONIQUES (méthode établie — l'OCR du miroir corrompant deux zones) : (1) le passage des quatre aspects restitué mot à mot contre l'édition du Muḥarrar citée par les agrégateurs (quranpedia, concordance intégrale avec l'imprimé) ; (2) le hadith de la reconnaissance de Nūḥ (section exploitation) restitué en teneur reçue avec sa chaîne : Ibn Abī d-Dunyā et al-Bayhaqī dans Shuʿab al-Īmān, d'après Mujāhid (« il ne mangea jamais chose sans louer Allah… il ne s'empara jamais de chose sans Le louer ») — l'appel de note [31] de l'imprimé étant illisible ; la recherche fut menée par le SDK (web_search + page_reader — islamweb étant derrière reCAPTCHA en direct, le page_reader l'atteint).
- LES HONNÊTETÉS D'APPARAT (doctrine : jamais deviné) : le verbe de la question-cadre du tamhīd restitué d'après l'ouverture de la leçon suivante (lisible, p.24) ; la question de « je contemple le texte » DÉCLARÉE PERDUE ; le cinquième terme de la préparation déclaré illisible ; la référence de l'exercice d'iʿrāb de la préparation déclarée partiellement perdue (le seul segment lisible « al-āḫira » renvoyant aux versets 5-8) ; une brève glose intermédiaire de « taʿlunna » consignée corrompue.
- LE CORPUS DE LA LEÇON : le tamhīd (l'honneur fait à Muḥammad ﷺ par l'Isrāʾ, puis à Mūsā par la Torah — la sortie des ténèbres vers la lumière, la corruption qui suivit) ; les trois iʿrāb de (an) dans « allā tattakhidhū » (subjonctive par ellipse d'aversion / explicative avec iltifāt sur la lecture du gros des gens au tāʾ, al-Ḥasan ayant le yāʾ / superflue avec ellipse d'un dire) ; la glose de « wakīlan » (fuʿīl du tawakkul valant fāʿil ; Mujāhid : « un associé ») ; le pronom de « Nous en fîmes une guidée » (Livre ou Mūsā) ; aṭ-Ṭabarī sur « qaḍaynā » (faraghnā / akharnā / écrit dans la Mère du Livre) ; Ibn ʿAṭiyya sur la préposition (ilā) — l'exécution dans la Mère du Livre et la descente de l'information jusqu'aux Banū Isrāʾīl, les deux glosses d'Ibn ʿAbbās ; le Livre = la Torah (non la Table gardée), Saʿīd ibn Jubayr au pluriel, Abū Ḥātim au singulier ; les fils propres de Nūḥ — l'Adam le cadet, quiconque est sur terre en descend (aṭ-Ṭabarī d'après Qatāda et Mujāhid) ; « aš-šakūr » — la louange en tout état ; les finalités (foi : tawḥīd, l'origine une des hommes ; formation : la gratitude à l'imitation de Nūḥ) ; le sens des versets (l'information de la Torah comme avertissement et appel) ; l'évaluation (trois questions) ; l'exploitation (le hadith de Mujāhid + la préparation des versets 5-8).
- GARDES ET QA : qa-lesson.py : 13 946 car, 0 arabe (ﷺ exemptée par convention), 46 guillemets appariés, 0 apostrophe droite, 10 types de balises appariées (auto-fix appliqué) ; verify-710-quran.py : PASS — rendus français des versets 2-4 présents, concordance au cache par rasm dédiacritiqué (wakīlan en 17:2 confirmé), hadith rendu avec sa chaîne, AUCUNE citation hors rasm (les versets 5-8 interdits au corps — matière de la leçon suivante), 0 arabe résiduel ; hand-set.py : REGISTRE 1033, 1 emplacement écrit ; navigateur agent-browser (route #/livre/tafsir-5ep/pdf-mut23h3c-710) : desktop 1280 — h1 « Sourate Al-Isra (versets : 2-4) », badge « Leçon 34 / 123 », « Traduction savante », note « Source du cours », wakīlan, quatre aspects, chaîne du hadith, section évaluation AU DOM, 0 overflow (scrollW=clientW=1280), 0 erreur console ; mobile 390 — 0 overflow (scrollW=clientW=390), contenu présent ; captures ×2 (tr-tmp/qa-R459-710-{desktop,mobile}.png).
- L'ALIGNEMENT CONFIRMÉ : l'étiquette du portail pour le slot 710 (« سورة الإسراء (الآيات: 2-4) ») concorde EXACTEMENT avec la matière du manuel miroir — la carte par ordre (isra-map.py) tient sur son deuxième point ; la leçon suivante 711 = versets 5-8 (p.24-29, l'étiquette du portail et l'en-tête de la p.24 concordent déjà).

Stage Summary:
- Registre : 1033 leçons savantes livrées (975 main + 57 llm). Position : R459 close. tafsir-5ep : 63/122.
- Leçons du tour : (1) LA LECTURE WARŠ EST UNE GARDE PHILOLOGIQUE — « wakīlan » (pas « ʿiwlan ») : le rasm du corpus décide des gloses et ferme les puzzles d'iʿrāb (l'apposition du quatrième aspect n'a de sens que contre le mot waršien) ; (2) l'arbitrage par sources canoniques web tranche en deux recherches ce que l'OCR du miroir corrompt — la chaîne du hadith (Ibn Abī d-Dunyā + al-Bayhaqī) et le texte intégral d'Ibn ʿAṭiyya ; (3) l'alignement portail/miroir se vérifie à chaque leçon — l'étiquette du portail concorde avec la matière : la carte par ordre tient.
- Prochaine priorité : (1) LA LEÇON 711 — Isrāʾ versets 5-8 (p.24-29 : les deux corruptions, les serviteurs à redoutable force, le retour de fortune, la Dernière promesse, « عسى ربكم أن يرحمكم ») — la matière attend, l'étiquette du portail concorde déjà ; (2) puis 712+ (Kahf en vue) ; (3) hadith-2-iadadi (manuel acquis) ; (4) canari en second à chaque tour ; (5) APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé). La règle h tient : le tail du worklog après cette entrée EST la priorité.
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
