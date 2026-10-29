# -*- coding: utf-8 -*-
"""append-worklog-r359.py — append unique de l'entrée R359 au worklog.md."""
import os

HOME = "/home/z/my-project"
WL = f"{HOME}/worklog.md"

ENTRY = """
---
Task ID: R359
Agent: GLM (session web-394d04d3, tick 2026-10-29 21:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : conformité GitHub, rédaction savante (priorité worklog R358 : doc 19238 lessons[6], « أنشطة لاستثمار التعلمات ودعمها من الدرس 1 إلى 5 » — les activités d'exploitation des apprentissages et de leur soutien des leçons 1 à 5, la pause de consolidation), QA, push, backup, worklog.

Work Log:
- Ouverture : sandbox STABLE (remote origin présent, credentials présents — règle by reconfirmée) ; HEAD a3c59df (R358), 0/0 avec origin ; worklog 13 538 lignes, planchers vérifiés : R358 au tail, registre 962 (hand 905 + llm 57) ; le résumé de session périmé (R348/19807) écarté une quatrième fois — règle h : le worklog est la priorité.
- Choix du doc : 19238 (lessons[6]) — titreAr « التوقيت أنشطة لاستثمار التعلمات ودعمها من الدرس 1 إلى 5 », badge lessons[6]+2 = « Leçon 8 / 28 » (règle f, 73e confirmation) ; descripteur interne « الدرس السادس » (ad-dars as-sādis — la SIXIÈME leçon de l'imprimé, en torsion avec la 8e place au badge, comme aux tours précédents) ; fente liminaire dt ET dd VIDES (vingt-deuxième tour consécutif sans date) ; extraction extract.py (source 2 442 car AR → 19238.src.html + GT 3 513 car ; titleFr GT « Calendrier des activités pour développer et soutenir l'apprentissage des leçons 1 à 5 » — GT-isme écarté : aucun calendrier au titre source, le tawqīt y est en tête ; harmonisé « Le tawqīt : les activités d'exploitation des apprentissages et de leur soutien (des leçons 1 à 5) »).
- APPAREIL CORANIQUE (règle ax) : FENTE FORMELLE — l'āya de la caverne : après « قال الله تعالى: » le paragraphe de citation arrive VIDE ; identifiée par le contexte (la glose d'Ibn ʿAṭiyya qui suit déroule les trois cents années et les neuf), position UNIQUE au muṣḥaf du corpus, vérifiée au quran-cache : 18:25 « wa-labiṯū fī kahfihim ṯalāṯa miʾatin sinīna wa-zdādū tisʿā », calibrations du rasm ʿUṯmānī documentées (cercles de waqf sur les deux wāw, yāʾ sans points de fī, alif suscrit de ṯalāṯ, cercle sur l'alif de miʾatin, hamza de liaison écrite dans wazdādū, tanwīn + petit nūn suscrit de tisʿā) ; SECONDE fente formelle du livre après 9:36 (19229) — même mécanique, même restitution.
- FENTES DE CONTENU (règle ax) : SIXIÈME GRANDE FENTE du livre documentée — le tableau des étapes de l'entretien (après « باعتماد الخطوات المحددة في الجدول الآتي: ») arrive VIDE (après le fihrist des œuvres, le rubʿ al-muǧīb de 19216, le tableau maître des ǧummal, les étapes du calcul de l'année arabe et les comparaisons de 19237), portée sans reconstruction, renvoi conservé tel quel ; + fente liminaire dt/dd + p et div vides finales à leur place.
- Rédaction savante : fragments fr19238_1..5.html → build-19238.py (91 sondes, toutes OK — 27 419 car, source 2 442 AR ≈ 11,2× ; 0 table — pas de matn poétique à la pièce ; 44 guillemets appariés ; 1 recalibrage de sonde : li 22 = 12 consignes + 10 N.d.T.) → tr-tmp/19238.html → qa-lesson.py OK (auto-fix, 27 419 car — 0 arabe, guillemets appariés, 0 apostrophe droite) → hand-set.py OK (« 1 emplacement(s) htmlFr écrit(s), 27418 car FR — registre → 963 savants », 19238 ×1 SANS doublon) → harmonize-title.py OK (titleFr corpus harmonisé au h1 savant).
- DÉCOUVERTE CENTRALE (la conversion-est-la-démonstration, 3e démonstration) : l'exercice « 300 سنة شمسية = 309 عاما قمريا » se déroule avec les SEULS NOMBRES DU COURS : 300 × 365,25 (l'année ʿaǧmiyya du livre) = 109 575 j ; ÷ 354,36667 (le sund des trentièmes) ≈ 309,21 → ≈ 309 années lunaires ; et par l'écart : ~11 j × 300 ≈ 3 300 j ≈ 9,3 années — LE NEUF DU VERSET : l'āya 18:25 porte écrite la conversion entre les deux comptes que le cours outille — l'exercice de la caverne est un exercice de tawqīt avant d'être un exercice de tafsīr (Ibn ʿAṭiyya : « l'augmentation entre les deux comptes »).
- Écho transversal majeur : les grappes de l'exercice ǧummal (ش - مجـ - حش - قيد - سهص) — قيد = qayd 114 et سهص = sahṣ 365 sont DEUX DES SEIZE EXEMPLES de la leçon des lettres (19219) : le livre fait tourner son code sur ses propres specimens ; le sahṣ revient pour la TROISIÈME fois (exemples 19219 → bayt de l'année 19237 → exercice ici) ; déroulé du traducteur : š = 1000 (le millier de la 4e rangée), m-ǧ = 43, ḥ-š = 1008 ; l'exercice basīṭ/kabīs fait manier LES DEUX CRIBLES du cours en une ligne (÷30 et ses onze kabāʾis pour les h., ÷28 et ses sept pour les f.) — déroulé du correcteur : 1382 ÷ 30 = 46 r2 kabīs, 1404 ÷ 30 = 46 r24 kabīs, 2237 ÷ 28 = 79 r25 basīṭa, 2325 ÷ 28 = 83 r1 basīṭa.
- Le rubʿ al-muǧīb REPARAÎT : la citation d'al-Ḫaṭṭābī [ʿilm al-mawāqīt : uṣūluhu wa-manāhiǧuh, p. 04] — la première autorité extérieure depuis le ḫuṭba — nomme SIX instruments en deux familles (d'ombre, de rayon, composés, simples : al-kura, aṣ-ṣafīḥa, rubʿ al-muǧīb, rubʿ al-muqanṭarāt, ḏāt al-kursī, bayt al-ibra) : la seconde grande fente du livre reçoit sa première réponse extérieure (un voisinage, non une reconstruction) ; ET la citation se ferme sur « arǧūza et leurs gloses » : le manuel est exactement ce double objet (naẓm + šarḫ, un abrégé) — la bibliographie inclut son hôte ; le 3e objectif nomme l'héritage marocain (al-mūraṯ al-maġribī) : l'abjad maghrébin du cours, le sund, la chaîne du Muqniʿ et al-Firklī en sont la matière.
- QA : agent-browser double écran 1280×900 ET 390×844 : 0 erreur console, 0 page erreur, NO-OVERFLOW des deux côtés (desktop cw=1280 nOver=0 maxR=1280, h1 exact, badge « Leçon 8 / 28 » au DOM, méta 3/3, N.d.T. ×10, tables 0 ; mobile cw=390 nOver=0 maxR=390 — dix-huitième tour consécutif aux mêmes mesures), captures tr-tmp/qa-19238-{desktop,mobile}.png — capture desktop LUE : rendu conforme (vue bilingue FR/AR, badge ambre, progression 29 %, méta 3/3). Routage hash déjà documenté (404 sans #).
- Push : commit livraison 4940b18 — push OK (a3c59df..4940b18) ; backup.sh OK ; arbre propre ; leçon d'append R354 APPLIQUÉE : le script d'append dédié créé AVANT exécution (aucun doublon).
- Règles : (x)-(ch) inchangées ; (by) reconfirmée ; (f) reconfirmée (73e : badge = lesson_index+2, avec la torsion des deux comptes) ; (h) reconfirmée (priorité = le worklog) ; (ax) reconfirmée (fente formelle 18:25 identifiée + vérifiée + calibrée + 6e grande fente du tableau d'entretien portée sans reconstruction + exercices déroulés au titre de la garde du traducteur) ; (cg) reconfirmée (100 % translittéré — l'āya, les grappes de ǧummal, les instruments) ; (cc) reconfirmée (fenêtre compacte : 5 fragments + push immédiat après hand-set) ; (ai) reconfirmée (la QA vision lue).
- Risques : (a) TOKEN — PAT fonctionnel, reconstruire à CHAQUE ouverture ; (b) SANDBOX — vigilance de mise (vérifier remote + cred + tail à chaque ouverture) ; (c) instance parallèle — aucun TODO concurrent signalé sur taqtit-tanawi-1 ; (d) limite de contexte — aucun fragment en tension ; (e) les déroulés des exercices sans corrigé (ǧummal et cribles) sont de la GARDE DU TRADUCTEUR — ne pas les présenter au rang de corrigé du livre dans les harmonisations futures.
- Plancher suivant : >= R360 / >= 964 / lignes réelles mesurées post-append (13 538 avant cette entrée).

Stage Summary:
- LIVRÉ : 19238 « Le tawqīt : les activités d'exploitation des apprentissages et de leur soutien (des leçons 1 à 5) » (Leçon 8/28, la pause de consolidation, la sixième leçon de l'imprimé) — 27 418 car FR, registre 963/— (hand 906 + llm 57), poussé sur origin/main (4940b18), backup OK ; taqtit-tanawi-1 : 8/28 (intro + présentation + jours + introduction + ǧummal + jours importants + ʿaǧmiyya + activités), 20 leçons restantes.
- RÉSOLU : la consolidation du premier arc — la carte des méthodes d'al-Ḫaṭṭābī (instruments / calcul / classification) recouvre le chemin déjà marché ; les six instruments nommés (et le rubʿ al-muǧīb réapparié) ; les deux cribles maniés en une ligne (÷30 onze kabāʾis / ÷28 sept kabāʾis) ; le code des ǧummal retourné sur ses propres exemples (qayd 114, sahṣ 365) ; ET la conversion des deux comptes démontrée par les nombres du livre seul : 109 575 j ÷ 354,36667 ≈ 309,2 — les neuf de l'āya de la caverne — la 18:25 est le premier exercice résolu de la discipline.
- LEÇONS DU TOUR : (1) LA CITATION FAIT LA REVUE — l'autorité extérieure d'al-Ḫaṭṭābī décrit le genre du livre qu'elle accompagne (arǧūza + glose, abrégé) et nomme l'instrument perdu : la consolidation passe par l'extérieur, la fente reçoit un voisinage sans perdre son vide ; (2) LE VERSET EST UN EXERCICE — les trois cents et les neuf de la caverne sont un compte avant d'être un récit : le tafsīr d'Ibn ʿAṭiyya et les outils du manuel déroulent le même nombre, la conversion-est-la-démonstration gagne son troisième cas ; (3) LA PAUSE REGARDE EN AVANT — l'iʿdād de la page de consolidation annonce déjà la seconde leçon des jours de l'année ʿaǧmiyya (faṣl, manāzil, burūǧ, règle des débuts) et commande la mémorisation du matn : même la récapitulation avance selon l'ordre du codage.
- Prochaine priorité : taqtit-tanawi-1 selon l'ordre du codage — 19248 (lessons[7], « أيام السنة العجمية 2 » — la seconde leçon des jours de l'année ʿaǧmiyya, que l'iʿdād de 19238 prépare explicitement : les faṣl et leurs jours, les manāzil et les burūǧ, la règle des débuts des faṣl — et le matn à mémoriser) ; vérifier 0/0 + git log avant tout choix ; registre attendu 964.
"""

with open(WL, "r", encoding="utf-8") as fh:
    content = fh.read()

if "Task ID: R359" in content:
    raise SystemExit("✗ R359 déjà présent — aucun append (anti-doublon).")

if not content.endswith("\n"):
    content += "\n"
content += ENTRY.lstrip("\n").rstrip("\n") + "\n"

with open(WL, "w", encoding="utf-8") as fh:
    fh.write(content)

lines = content.count("\n")
print(f"✓ R359 append — worklog {lines} lignes")
