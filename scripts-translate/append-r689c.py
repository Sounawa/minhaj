# -*- coding: utf-8 -*-
"""Append worklog R689-c — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R689-c
Agent: GLM (session web-1564f3be, canal principal, tick 2026-11-12 10h05 +08:00, trace 1a1cf01d0f8f7441)
Task: LIVRAISON leçon 411 hadith-3es (pdf-mut23h2x-411, leçon 22 imprimée « من أحكام الفدية » — le locuste et le rasage, p.147-152) — protocole simplifié demandé par l'utilisateur (plus de re-clonage systématique ; vérification d'état local rapide ; priorité aux traductions).

Work Log:
- DIRECTIVE UTILISATEUR consignée : ne plus re-cloner le dépôt à chaque session — vérifier l'état local (git fetch + rev-list), reprendre là où le worklog s'est arrêté, et garder le site en preview (page d'accueil) ; priorité absolue à l'avancement des traductions. Le protocole de reprise est ALLÉGÉ mais les garanties restent : git fetch 0/0 avant production, règle de vague (push immédiat après livraison), backup, worklog.
- État de reprise : local == origin/main après push aaa58b6 (auto-commit superviseur), deps OK, site UP (port 3000, hydratation OK — le fix allowedDevOrigins de R689 tient au réveil).
- CLAIM posé (hadith3-pdf-mut23h2x-411, trace 1a1cf01d0f8f7441-r689-main, 09h12 UTC) et LIBÉRÉ après livraison (archivé .livre-r689c).
- EXTRACTION : couche logique PDF p.147-152 (mots réinversés + ordre de mots) → tr-tmp/h3-411-logical.txt ; 16 lectures VLM (6 pages + 10 zooms) + 8 microcrops d'adjudication (4 recadrés) — tr-tmp/vlm-411/.
- ADJUDICATIONS PAR L'IMAGE (8, lettre à lettre) : (1) n° 1263 — « عَتْقُ رقبةٍ » (affranchissement d'un esclave, point sur le tā') — la couche texte « عنق » récusée (le sens du tuage fautif de l'homme confirme : ka-kaffārat qatl al-insān) ; (2) n° 1252 — « la'alaka adhāka hawāmuk » (lām-'ayn-lām lu lettre à lettre, alif sans madda) ; (3) gloses — « taqarrab bihā » et « qabḍa : fatha sur le qāf, le damma est le parler, c'est-à-dire ḥafna » ; (4) n° 1251 — « li-ifādat 'umūm at-tathniya » (le thā' de tathniya lu point par point, « النية » récusé) ; (5) n° 1255 — fin « kamā amarah llāh ta'ālā » (deux lectures d'image concordantes, couche texte fragmentaire résolue) ; (6) n° 1256 — « man nataf cha'ran » (netf, couche « تتف » récusée), la pâte « nūra » au damma du nūn avec sa glose parenthétique d'arsenic, « šaǧǧat ra'sih » (la plaie), « qafāh li-mawḍi' aṣ-ṣā'im » ; (7) dialogue d'Umar — « hal taqra' sūrat al-mā'ida » (qāf-rā-hamza aux deux occurrences, « تحفظ » récusé) ; (8) sourate al-Mā'ida imprimée « l'āya : 97 » DEUX FOIS chiffre par chiffre (٩٧) — le cache ḥafṣ compte 95 : décalage de l'édition consigné (doctrine R511 étendue). Chiffres tranchés : 1252/2521, 1263/3621, 1255/5521, 1251/1521, 1256/6521, 1241/1421 (re-cité ×3), 1253/3521, al-Baqara 195 (×2, cache 196 — doctrine R511 déjà consignée), Ka'b m. 51 h. (15 inversé).
- RÉDACTION : leçon 22 en 5 fragments → tr-tmp/lesson-hadith3-411-fr.html (38 674 car) — h1 long, objectifs ×3, tamhīd (les interdits de la personne et de l'entourage), deux textes (1252 la compensation triple de Ka'b ; 1263 l'association au gibier, l'atq raqaba, la kaffāra ne se partage pas), notice de Ka'b b. 'Uǧra (l'Auxiliaire, m. 51 h., ses fils ont rapporté de lui), gloses ×2 (an-suk bi-cha'a, qabḍa — la préparation de la leçon 21 rendue), résumé ×2, recherche légale en deux sections : premièrement la fidya du rasage (le sens large — 1255 ; pour excuse — 1252 re-cité + 1251 « madān madān » + tathniya + al-Baqara 195 + les deux authentiques « l'āya descendue pour un cas particulier vaut pour vous en général » + l'herméneutique de Mālik : la généralité du terme contre la spécificité de la cause, la Sunna mubayyina li-muǧmal al-qur'ān ; délibéré — la divergence Mālik/abū Ḥanīfa/ach-chāfi'ī, l'argument a fortiori, Ibn Baṭṭāl 4/174 bi-taṣarruf ; la généralisation — 1256 : le nez, l'aisselle, la nūra, la šaǧǧa, la nuque du jeûneur) ; deuxièmement l'association au gibier (1263 re-cité ×2 — la compensation pleine pour chacun, le choix ouvert ; les deux juges équitables savants — 1241, 'Umar et 'Abd ar-Raḥmān b. 'Awf, l'un des Dix ; l'étonnement du questionneur, la roya d'al-Ḥākim, la leçon d'Umar par al-Mā'ida 97 imprimée, le dialogue complet) ; évaluation ×2 résolues ; exploitation (1253 — la marmite de Ka'b, « il n'avait pas de quoi immoler » — et la question du recueillement des deux rapports) ; i'dād ×2 (la 'umra — leçon 23) ; apparat de preuve complet.
- QA : qa-lesson.py PASS après correctifs (un guillemet fermant manquant dans le paragraphe de la règle du rasage — 79/78 → appariés ; sept mots arabes de l'apparat repris en spans RTL) — 38 675 car, 0 arabe hors spans, 79 guillemets appariés, 0 apostrophe droite.
- VÉRIFICATION : verify-hadith3-pdf411.py — 51 contrôles OK / 0 échec (garde-doublon htmlFr vide vérifié avant pose, claim, 38k+, 11 sections, 2 textes, 7 numéros, 10 fragments de matière adjudiquée, notice/gloses, āyas + doctrine R511 étendue, 0 arabe hors spans, 0 placeholder).
- POSE : hand-set.py hadith-3es pdf-mut23h2x-411 → « 1 emplacement(s) htmlFr écrit(s), 38674 car FR — registre → 1213 savants » ; API : leçon 411 hasFr=true savant=true — hadith-3es désormais 22/29 (restants : 412-418).
- QA NAVIGATEUR (r689c) : leçon rendue — h1 « Des règles de la compensation (fidya) », badge « Traduction savante », 12 sections H2, les 7 numéros présents, 0 débordement horizontal desktop 1280 (screenshot tr-tmp/qa-crops-r689c/qa-r689c-411-desktop.png).
- NOTE SDK : les scripts VLM importent désormais z-ai-web-dev-sdk depuis /home/z/node_modules/z-ai-web-dev-sdk/dist/index.js (my-project/node_modules évincé en R689-bis, recette R603 tenue) — les prochains scripts partent de ce chemin.

Stage Summary:
- LIVRÉ : leçon 22 hadith-3es « Des règles de la compensation (fidya) » (slot pdf-mut23h2x-411, 21e slot livré du livre, 38 674 car au registre, registre → 1213 savants) — hadith-3es 22/29.
- RÉSOLU : la structure exacte de la leçon 22 reconstituée (la rubrique استخلاص المضامين perdue par la couche texte en bas de p.148 retrouvée par lecture VLM — items « أستخرج/أستخلص ») ; la correspondance des fragments du n° 1255 entre les leçons 21 et 20 (même matn, lames différentes, même numéro — jamais re-numéroté).
- MÉCANIQUE CONSOLIDÉE : microcrops 900 dpi à coordonnées vérifiées (4 zones recadrées après coup) — la localisation des bandes doit être contrôlée sur le rendu avant lecture ; les requêtes d'adjudication pointent DÉSORMAIS le mot contesté ET son contexte immédiat (la lecture pleine-page sert de repère y).
- Prochaine priorité : slot pdf-mut23h2x-412 (leçon 23 — la 'umra, i'dād livré : أعرّف العمرة وأذكر أحكامها + أبين فضل العمرة وأهميتها في الإسلام, médaillon p.152-153) ; git fetch 0/0 avant production ; PARALLÈLE : 1.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R689-c" in tail:
    print("REFUS : R689-c déjà présent (garde anti-doublon).")
    sys.exit(1)

content = content.rstrip("\n") + "\n\n" + ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

print("OK : R689-c appendé.")
