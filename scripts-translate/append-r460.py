#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""append-r460.py — appose l'entrée R460 au worklog SOUS GARDE GARDE-DOUBLON."""
import re
import sys

PATH = "/home/z/my-project/worklog.md"
N = 460

ENTRY = """---
Task ID: R460
Agent: Z.ai Code (agent principal — session web-394d04d3, fenêtre utilisateur ; directive du tour : « il faut avancer non stop dans les traductions » — DEUXIÈME livraison du même tour)
Task: LA LEÇON 711 — Isrāʾ versets 5-8 (troisième leçon du volume, pages 24-29 du manuel miroir), livrée dans le même tour que la 710 sur la même chaîne : extraction → décodage → rédaction FR-seule → verify → registre → navigateur → commit → push.

Work Log:
- LA PIÈCE : 13 661 car. La troisième leçon du livre du Tafsīr de 2e année (al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya, p.24-29 de l'imprimé miroir) : les deux corruptions et leurs châtiments — REGISTRE 1034 (976 main + 57 llm), tafsir-5ep 64/122. DEUX leçons livrées dans LE tour (710 + 711) — la réponse au « non stop ».
- LE CORPUS DE LA LEÇON : le tamhīd (la Torah avait informé du décret — ces versets exposent la corruption, la tyrannie et le châtiment) ; Ibn ʿAṭiyya sur « ūlāhumā » (le pronom retourne sur « marratayn », les deux fois) et sur le mal dit « promesse » (waʿd au fonds de bien — permis pour le mal à indication du contexte : la mention de la punition) ; LA DOUBLE LECTURE de « fa-ǧāsū » (le gros des gens au jīm) CONTRE « fa-ḥāsū » d'Abū s-Sammāl (au ḥāʾ) — les deux valant domination et entrée par force, l'anecdote rendue (« il fut dit à Abū s-Sammāl : la lecture n'est que fa-ǧāsū — il répondit : ǧāsū et ḥāsū ne font qu'un ») ; le sens (lâcher des serviteurs tyrans pour la vengeance, le délaissement à cause de leur injustice) ; LE PASSÉ POUR LE FUTUR (« baʿathnā » — l'information toraïque non encore advenue, mais la promesse d'Allah certaine : le futur exprimé par le passé — repris par la question 2 de l'évaluation) ; la reprise (al-karra) après le premier exil — la royauté revenue, l'état amélioré « un temps de l'âge », aṭ-Ṭabarī (« Nous fîmes de vous, en nombre rallié, les plus »), QATĀDA (« au temps de Dāwūd — sur lui la paix ») ; Ibn ʿAṭiyya sur « nafīran » (pluriel de nafar comme kilāb/ʿabīd, ou fuʿīl valant fāʿil) ; le conseil du verset 7 (le bien pour vous-mêmes, le mal contre elle — Allah le Riche : l'obéissance ne L'avantage pas) ; la seconde corruption (la réponse elliptique de idā indiquée par la première, le lām du commandement ou de but, le pronom sur les serviteurs) ; l'entrée de la Mosquée et l'anéantissement (« tabbara » : réduire en menues parcelles comme on brise l'or et le fer ; « mā » objet ou circonstanciel de temps) ; LA PORTE DU RETOUR (« ʿasā » portant l'espoir — la miséricorde de l'obéissant, ET DE L'OBÉISSANCE FUT LEUR SUIVI DE ʿĪSĀ ET DE MUḤAMMAD — sur eux deux les prières et la paix) ; l'avertissement (« si vous récidivez, Nous recommencerons » — la lecture warš du cache : ʿudtum ʿudnā) ; « ḥaṣīran » (le fuʿīl de ḥaṣr = la prison, Mujāhid ; al-Ḥasan al-Baṣrī : le tapis connu des gens, ce qu'on déploie et étend — un gîte et une prison durable) ; LES SEPT FINALITÉS ÉDUCATIVES rendues intégralement (l'obéissance voie du bonheur ; les Lois révélées commandent la mise en valeur de la terre ; le salaire convient à l'espèce de l'acte, le repentir cause de victoire ; l'avertissement des destinataires du Qurʾān — le plus grand profit des récits ; le fruit retourne à l'homme, Allah le Riche des mondes ; LA MISÉRICORDE DOUBLÉE — « aḥsantum aḥsantum » deux fois contre le mal une fois, et la promesse de miséricorde à tout pénitent).
- LES HONNÊTETÉS D'APPARAT : la ligne d'ouverture de la première matière corrompue (consignée, le contenu porté par les membres suivants) ; la fin de la réponse d'Abū s-Sammāl + la glose de « et ce fut une promesse accomplie » corrompues (le membre lisible « le décret d'Allah est un » rendu) ; la première question de l'évaluation DÉCLARÉE PERDUE ; la liste des cinq termes de la préparation DÉCLARÉE PERDUE ; la troisième consigne partiellement perdue ; l'étiquette de plage de la préparation (« 9-21 » lue à l'OCR) TRANCHÉE PAR LA MATIÈRE : l'en-tête de la leçon suivante (p.30) porte « versets 9-14 » — doctrine des écarts d'étiquette (précédent doublons R458).
- GARDES ET QA : qa-lesson.py : 13 662 car, 0 arabe, 29 guillemets appariés, 11 types de balises appariées, 0 apostrophe droite (auto-fix appliqué ; deux coquilles de composition corrigées avant QA, une coquille Qurân→Qurʾān) ; verify-711-quran.py : PASS — les QUINZE segments des versets 5-8 rendus au DOM, concordance au cache par rasm dédiacritiqué (y compris ʿudtum ʿudnā en 17:8 — la lecture warš), la double lecture ǧāsū/ḥāsū rendue, AUCUNE citation hors rasm (17:9-14 interdits au corps — matière de la leçon suivante), 0 arabe résiduel ; hand-set.py : REGISTRE 1034 ; navigateur agent-browser (route #/livre/tafsir-5ep/pdf-mut23h3c-711) : desktop 1280 — h1 « Sourate Al-Isra (versets : 5-8) », badge « Leçon 35 / 123 », « Traduction savante », note « Source du cours », fa-ḥāsū, Abū s-Sammāl, Dāwūd, al-Ḥasan al-Baṣrī, la question des finalités AU DOM, 0 overflow (scrollW=clientW=1280), 0 erreur console ; mobile 390 — 0 overflow ; captures ×2 (tr-tmp/qa-R459-711-{desktop,mobile}.png).

Stage Summary:
- Registre : 1034 leçons savantes livrées (976 main + 57 llm). Position : R460 close. tafsir-5ep : 64/122. DEUX leçons livrées dans le tour (710 + 711) — le « non stop » exécuté.
- Leçons du tour : (1) LE RASM WARŠ DU CACHE COMME ANCRE — ʿudtum ʿudnā en 17:8 confirmé par le cache et par la glose du manuel, sans jamais ouvrir le débat ḥafṣ ; (2) les honnêtetés d'apparat se multiplient sans coût : une liste perdue est DÉCLARÉE perdue, une étiquette tranchée par l'en-tête suivant — le lecteur reçoit la double vérité ; (3) la question 2 de l'évaluation (le passé pour le futur) renvoie le lecteur à la glose centrale du verset 5 — la pédagogie de l'imprimé rendue intégralement.
- Prochaine priorité : (1) LA LEÇON 712 — Isrāʾ versets 9-14 (p.30-36 : « Ce Qurʾān guide vers ce qui est plus droit », les deux versets de la guidée et de la miséricorde, la parole de l'homme pressé?, la consultation des fils d'Israël, les deux fois dix nuisances) — l'étiquette du portail et l'en-tête p.30 concordent déjà ; (2) le rythme deux-leçons-par-tour est tenable — le viser ; (3) hadith-2-iadadi (manuel acquis) en parallèle ; (4) canari en second ; (5) APPEND SOUS GARDE RENFORCÉE (GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé). La règle h tient : le tail du worklog après cette entrée EST la priorité.
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
