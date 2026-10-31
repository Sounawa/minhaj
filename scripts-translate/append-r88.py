#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Append gardé R88 au worklog.md (GARDE-DOUBLON : Task ID = dernier + 1)."""
import re
import sys

WL = "/home/z/my-project/worklog.md"
NEW_ID = 88

ENTRY = """
---
Task ID: R88
Agent: Z.ai Code (agent principal — TOUR DE PRODUCTION AUTONOME cron 490480, trace 1a192862dcae2069-cron-agent-loop-202611010613)
Task: 10ᵉ exécution consécutive du canal (0253→0607) — tour de production sur la priorité R87 : hadith-1es leçons savantes 27-28 (13004, 13005) + QA navigateur + backup + worklog.

Work Log:
- **Canal / moteur** : TICK 0552 (tardif) + TICK 0607 consignés dans tr-tmp/cron-alive.log, avec RECTIFICATION du décompte (le tour est le 10ᵉ déclenchement consécutif, non le « sixième » écrit d'emblée) ; superviseur v4 VIVANT (PID 1359) — pas de relance nécessaire.
- **Recadrage GARDE-DOUBLON (5ᵉ occurrence)** : la mémoire compressée de ce tour invoquait ENCORE R465 / tafsir-5ep leçons 717-718 Isrāʾ / isra-l9-l10-readable / verify-716 / commit 17226d5 / slot 708+leçon# — VÉRITÉ TERRAIN : AUCUN de ces objets n'existe ; dernier Task ID réel R87 (lu au tail, lignes 5743-5760), registre 525/950, HEAD a43b295 (R87). Le tail réel a dicté la priorité : hadith-1es 27-28. Le fantôme post-compression en est à sa 5ᵉ récidive documentée (R82, R84, R85, R86, R88) — la vérification physique (tail worklog + git log + ls) demeure la 1ʳᵉ étape obligatoire du tour.
- **savant(hadith-1es/13004)** — leçon 27 la vertu de la prière en commun : 343 (la prière en commun surpasse celle de l'isolé de 27 degrés ; Tirmidhī : la plupart des rapporteurs disent 25, sauf Ibn ʿUmar 27 ; Muwaṭṭaʾ 344 : version des 25 « vingt-cinq parts »), 347 (entre nous et les hypocrites : la présence à ʿishāʾ et ṣubḥ — « ou des mots proches de cela »), 349 (ʿUmar perd Sulaymān au ṣubḥ, passe chez al-Shifāʾ : « le sommeil l'a vaincu » — « que j'assiste au ṣubḥ en commun m'est plus cher que de me lever en prière une nuit »). Analyse : sagesse de l'institution (liens d'amour/fraternité ; mosquée = espace d'éducation, règlement des différends, shūrā, étude du Qurʾān) ; divergence 25/27 (multiplicité des rapporteurs vs augmentation d'un ḥāfiẓ ; égalité des groupes — certains Mālikites, surcroît du plus nombreux : Ubayy ibn Kaʿb marfūʿ authentifié par Ibn Khuzayma « ce qui est plus nombreux est plus aimé de Dieu » ; 346 Zayd ibn Thābit « sauf la prière prescrite ») ; encouragement ʿishāʾ/ṣubḥ (chapitre « ce qui est venu sur ʿatama et ṣubḥ » ouvert par Mālik — licéité du nom ʿatama ; signe du nifāq, conformité vs comptage de la récompense ; Ibn ʿUmar mauvaise opinion ; Shaddād ibn Aws ; 350 ʿUthmān : ʿishāʾ = moitié de la nuit, ṣubḥ = nuit entière). Exploitation 345 (brûler les maisons des délaissants d'ʿishāʾ — « un os gras, ou deux bonnes pièces de gibier »). Préparation-préalable 13005. NOTE : la source écrit « الرقم : .346 » avec point parasite — normalisé dans le crosscheck (même traitement que le « .305 » de 13001). QA 0 arabe, 16 guillemets.
- **savant(hadith-1es/13005)** — leçon 28 les dispositions propres à l'imam et à ceux qui prient derrière lui : 351 (Miḥjan des Banū al-Dīl, rapporté par Busr : « quand tu viens, prie avec les gens, même si tu as déjà prié »), 357 (qu'il allège — le faible, le malade, le vieillard ; seul : qu'il allonge tant qu'il veut), 360 (chute du cheval, écorchure au flanc droit, prière assis ; « l'imam n'a été institué que pour qu'on le suive » — formule samiʿa/rabbanā rendue « Dieu entend celui qui Le loue » / « notre Seigneur, à Toi la louange », alignée sur 12980). Analyse : refaire avec l'imam (352 Ibn ʿUmar « cela t'est-il confié ? Cela appartient à Dieu » ; 355 maghrib/ṣubḥ ne se refont pas ; 356 Mālik : sauf le maghrib — « elle devient un shafʿ », glose lexicale « une paire ») ; allègement (Bukhārī/Muslim « ô gens, parmi vous il y a des repoussoirs… que celui qui dirige abrège » ; Ibn ʿAbd al-Barr : l'imam ignore les événements et besoins de ceux qui le suivent ; al-Yaʿmurī : l'habituel et non le cas rare — comme le qaṣr du voyage légiféré même sans peine) ; iqtidāʾ (jonction des versions al-Zuhrī/Ḥāmid par ʿĀʾisha ; Istidhkār : « ne divergez pas de lui » — preuve Mālik/Thawrī/Abū Ḥanīfa/tābiʿūn : l'intention contredite annule la prière ; jumhūr : pas d'assise pour le capable ; Shāfiʿī + plupart des Mālikites : le debout ne suit pas l'assis, fard ou nāfila). Évaluation 2 cas (assise prétextant une prière faite chez soi ; debout derrière l'imam assis excusé). Exploitation 362 (le Prophète malade s'assoit à côté d'Abū Bakr : « Abū Bakr priait avec la prière du Messager de Dieu, et les gens avec la prière d'Abū Bakr »). NOTE : le CMS porte le hadith 362 et sa question DEUX fois à l'identique (2ᵉ occurrence avec ligature ﷺ) — rendu tel quel ×2 avec mention « le manuel reprend ici ce hadith une seconde fois, à l'identique » (convention 12986/12945). Pas de préparation-préalable dans le CMS (dernière leçon de matière). titleFr GT-isme corrigé : « Dispositions particulières pour l'imam et ceux qui prient derrière lui » → « Les dispositions propres à l'imam et à ceux qui prient derrière lui ». QA 0 arabe, 11 guillemets.
- **Outils du tour** : extract-r88.py (src/gt ×2), verify-r88-quran.py (0 arabe + 0 apostrophe droite + guillemets appariés + 0 verset-image attendu/trouvé — PASS ×2), crosscheck-r86.py étendu aux 8 leçons (13004 : 7 n° Muwaṭṭaʾ OK, 13005 : 7 n° OK — le doublon 362 du src ne compte qu'une fois, tel quel en rendu), finalize-r88.py (injection htmlFr ×2 + titleFr ×1 + registre hand trié). qa-lesson.py PASS ×2 (auto-fix NNBSP appliqué).
- **QA navigateur (agent-browser)** : 13004 desktop 1280 (h1 rendu, badge « Traduction savante », 42 li + 32 p, 0 overflow, 0 erreur console), 13005 mobile 390 (36 li + 30 p, 0 overflow, mention du doublon 362 rendue, hadith 360 et sa formule visibles) — captures tr-tmp/qa-R88-13004-1280.png, qa-R88-13005-390.png.
- **Git** : aucun remote configuré sur ce sandbox (constat R83-R87 inchangé, push impossible sans token) ; commits locaux : c6667b2 (13004), fa4f21f (13005), chacun incluant book JSON + registre + tr-tmp (src/gt/final) + capture QA ; backup.sh PASS.

Stage Summary:
- **État** : registre **527/950** (+2 ce tour) — hadith-1es **29/32 savant** (intro + leçons 1-28). 48 livres complets. Corpus global côté GT inchangé.
- **Décisions clés** : (a) 5ᵉ recadrage GARDE-DOUBLON consécutif — le fantôme « R465 / tafsir-717+718 Isrāʾ » survit encore à une compression ; le tail réel du worklog fait foi, la vérification physique reste la 1ʳᵉ étape du tour ; (b) le doublon CMS du hadith 362 (13005) est rendu tel quel en DEUX blocs identiques avec mention explicite — la question « Résume ce qui se tire de ce hadith » figure deux fois, conformément au manuel ; (c) « الرقم : .346 » de 13004 normalisé (point parasite, convention .305) ; (d) titleFr GT-isme corrigé ×1 (13005) — le GT de 13004 coïncidait déjà avec le titre juste.
- **Risques** : (a) push GitHub toujours sans token (dépôt à R74, ~55 commits d'avance locale) ; (b) 13004 : la parole de Mālik sur le maghrib refait « elle devient un shafʿ » (356) est rendue avec une glose lexicale minimale (« une paire ») — la lecture Zarqānī précise mériterait un cross-check sur le Sharḥ ; (c) 13005 : la « version ajoutée » « فلا تختلفوا عليه » de l'Istidhkār est rendue « ne divergez pas de lui » — l'attribution exacte de la version (« zāda maʿnā ») mériterait une relecture Zubdā/Ḥāwi ; (d) compteur lecteur « Leçon 28/32 » vs titre « vingt-septième leçon » (le badge compte l'intro) — convention inchangée, à garder pour les cross-checks.
- **Priorités suivantes** : (1) hadith-1es leçons savantes 29-30 : 13006 (les biographies des Compagnons — que Dieu les agrée), 13011 (la liste des sources et références) [viser DEUX leçons ; reste ensuite 13014, la présentation du livre, pour compléter 32/32] ; (2) relecture croisée des labels de versets du CMS sur le PDF du manuel (Wāqiʿa 77, Muḥammad 34, Jumuʿa 9, Ṭāhā 131) ; (3) tour dédié faraid-tanawi-3 manẓūma (310-313).
"""

def main() -> None:
    with open(WL, encoding="utf-8") as f:
        text = f.read()
    ids = [int(m) for m in re.findall(r"^Task ID: R(\d+)", text, re.M)]
    last = max(ids) if ids else 0
    if NEW_ID != last + 1:
        sys.exit(f"✗ GARDE-DOUBLON : dernier Task ID R{last}, refusé d'apposer R{NEW_ID}")
    with open(WL, "a", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"✓ R{NEW_ID} apposé (dernier vérifié : R{last}) — {len(ENTRY)} car")


if __name__ == "__main__":
    main()
