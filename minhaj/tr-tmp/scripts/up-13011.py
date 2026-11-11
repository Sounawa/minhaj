#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13011 (hadith-1es, liste des
sources et références de la matière — leçon finale du manuel).

Conventions main (cf. 12875-13006 du même livre) :
- h1 « Liste des sources et références (lāʾiḥat al-maṣādir
  wa-l-marājiʿ) » + intro (élèves 1ʳᵉ année, première étape) ;
  la date CMS du <dd> (lundi 8 avril 2019) = métadonnée de page,
  non rendue (comme les <dl> vides des autres leçons).
- Structure : Coran (muṣḥaf muḥammadi, Warsh/Nāfiʿ via al-Azraq,
  Fondation Mohammed VI) ; livres de hadith (13) ; commentaires (6) ;
  livres de fiqh (3) — éditions, éditeurs, dates rendus fidèlement.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Liste des sources et références (<em>lāʾiḥat al-maṣādir wa-l-marājiʿ</em>)</h1>
<p>Liste des sources et références qui furent adoptées en la matière Ḥadīth — sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī — à l’intention des élèves de la première année de l’enseignement secondaire traditionnel, première étape.</p>
<ul>
<li><strong>Le Noble Coran, en la lecture de Warsh d’après Nāfiʿ, par voie d’al-Azraq</strong> — le <em>muṣḥaf</em> muḥammadien publié par la Fondation Mohammed VI pour la publication du Noble Muṣḥaf.</li>
</ul>
<h2>Les livres de hadith</h2>
<ol>
<li><strong>Le <em>Muwaṭṭaʾ</em></strong> — de l’imam Mālik ibn Anas, lecture de Yaḥyā ibn Yaḥyā al-Laythī ; édition du Conseil scientifique supérieur, première édition, 1434 H — 2013.</li>
<li><strong><em>Le Collectaneum abrégé, sonnant et chaîné, des affaires de l’Envoyé de Dieu — paix et bénédiction sur lui —, de ses sunnas et de ses jours</em></strong> (le Ṣaḥīḥ) — de Muḥammad ibn Ismāʿīl, Abū ʿAbd Allāh al-Bukhārī ; édition critique de Muḥammad Zuhayr ibn Nāṣir al-Nāṣir ; Dār Ṭawq al-Najāt, première édition, 1422 H.</li>
<li><strong><em>Le Sonnant abrégé, du transfert du sûr d’après le sûr jusqu’à l’Envoyé de Dieu — paix et bénédiction sur lui</em></strong> (le Ṣaḥīḥ) — de Muslim ibn al-Ḥajjāj, Abū l-Ḥasan al-Qushayrī al-Naysābūrī ; édition critique de Muḥammad Fuʾād ʿAbd al-Bāqī ; Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth.</li>
<li><strong><em>Le Supplément aux deux Ṣaḥīḥ</em></strong> (al-Mustadrak) — de Muḥammad ibn ʿAbd Allāh, Abū ʿAbd Allāh al-Ḥākim al-Naysābūrī ; édition critique de Muṣṭafā ʿAbd al-Qādir ʿAṭā ; Dār al-Kutub al-ʿIlmiyya, Beyrouth, première édition, 1411 H.</li>
<li><strong>Les <em>Sunan</em> d’at-Tirmidhī</strong> — de Muḥammad ibn ʿĪsā ibn Sawra ibn Mūsā ibn al-Ḍaḥḥāk at-Tirmidhī ; édition critique et annotation d’Aḥmad Muḥammad Shākir (vols 1-2), Muḥammad Fuʾād ʿAbd al-Bāqī (vol. 3) et Ibrāhīm ʿAṭwa ʿAwḍ (vols 4-5) ; Librairie et imprimerie Muṣṭafā al-Bābī al-Ḥalabī, Égypte, deuxième édition, 1395 H.</li>
<li><strong>Les <em>Sunan</em> d’Ibn Māja</strong> — d’Abū ʿAbd Allāh Muḥammad ibn Yazīd al-Qazwīnī ; édition critique de Muḥammad Fuʾād ʿAbd al-Bāqī ; Dār Iḥyāʾ al-Kutub al-ʿArabiyya, sans date.</li>
<li><strong>Les <em>Sunan</em> d’al-Dāraquṭnī</strong> — d’Abū l-Ḥasan ʿAlī ibn ʿUmar ibn Aḥmad ibn Mahdī ibn Masʿūd ibn al-Nuʿmān ibn Dīnār al-Baghdādī al-Dāraquṭnī ; texte établi, vocalisé et annoté par Shuʿayb al-Arnaʾūṭ, Ḥasan ʿAbd al-Munʿim Shalabī, ʿAbd al-Laṭīf Ḥarz Allāh et Aḥmad Barhūn ; Muʾassasat al-Risāla, Beyrouth-Liban, première édition, 1424 H.</li>
<li><strong>Les <em>Rameaux de la foi</em></strong> (Shuʿab al-īmān) — d’Abū Bakr Aḥmad ibn al-Ḥusayn al-Bayhaqī ; édition critique de Muḥammad al-Saʿīd Basyūnī Zaghlūl ; Dār al-Kutub al-ʿIlmiyya, Beyrouth, première édition, 1410 H.</li>
<li><strong>Le <em>Musnad</em> de l’imam Aḥmad ibn Ḥanbal</strong> — d’Abū ʿAbd Allāh Aḥmad ibn Muḥammad ibn Ḥanbal ibn Hilāl ibn Asad al-Shaybanī ; édition critique de Shuʿayb al-Arnaʾūṭ, ʿĀdil Murshid et d’autres, sous la direction de ʿAbd Allāh ibn ʿAbd al-Muḥsin al-Turkī ; Muʾassasat al-Risāla, première édition, 1421 H.</li>
<li><strong>Le <em>Musnad</em> d’al-Bazzār, publié sous le nom <em>La Mer débordante</em></strong> (Baḥr al-zakhkhār) — d’Abū Bakr Aḥmad ibn ʿAmr ibn ʿAbd al-Khāliq ibn Khallād ibn ʿUbayd Allāh al-ʿAtakī, connu sous le nom d’al-Bazzār ; édition critique de Maḥfūẓ al-Raḥmān Zayn Allāh, ʿĀdil ibn Saʿd et Ṣabrī ʿAbd al-Khāliq al-Shāfiʿī ; Maktabat al-ʿUlūm wa-l-Ḥikam, Médine, première édition, 2009.</li>
<li><strong>Le <em>Ṣaḥīḥ</em> d’Ibn Ḥibbān</strong> — de Muḥammad ibn Ḥibbān ibn Aḥmad ibn Ḥibbān ibn Muʿādh ibn Maʿbad, at-Tamīmī ; édition critique de Shuʿayb al-Arnaʾūṭ ; Muʾassasat al-Risāla, Beyrouth, deuxième édition, 1414 H.</li>
<li><strong>Le <em>Ṣaḥīḥ</em> d’Ibn Khuzayma</strong> — de Muḥammad ibn Isḥāq ibn Khuzayma, Abū Bakr as-Sulamī al-Naysābūrī ; édition critique de Muḥammad Muṣṭafā al-Aʿẓamī ; al-Maktab al-Islāmī, Beyrouth, 1390 H.</li>
<li><strong>Le <em>Muṣannaf</em></strong> — d’Abū Bakr ʿAbd al-Razzāq ibn Hammām ibn Nāfiʿ al-Ḥimyarī al-Yamānī aṣ-Ṣanʿānī ; édition critique de Ḥabīb al-Raḥmān al-Aʿẓamī ; al-Maktab al-Islāmī, Beyrouth, deuxième édition, 1403 H.</li>
</ol>
<h2>Les commentaires du hadith</h2>
<ol>
<li><strong>Le <em>Commentaire du Muwaṭṭaʾ</em> de l’imam Mālik</strong> — de Muḥammad ibn ʿAbd al-Bāqī ibn Yūsuf al-Zarqānī al-Miṣrī al-Azharī ; édition critique de Ṭāhā ʿAbd al-Raʾūf Saʿd ; Maktabat al-Thaqāfa al-Dīniyya, Le Caire, première édition, 1424 H.</li>
<li><strong>L’<em>Istidhkār</em></strong> — d’Abū ʿUmar Yūsuf ibn ʿAbd Allāh ibn Muḥammad ibn ʿAbd al-Barr ibn ʿĀṣim an-Namrī al-Qurṭubī ; édition critique de Sālim Muḥammad ʿAṭā et Muḥammad ʿAlī Maʿwaḍ ; Dār al-Kutub al-ʿIlmiyya, Beyrouth, première édition, 1421 H.</li>
<li><strong>Le <em>Tamhīd de ce que renferme le Muwaṭṭaʾ de sens et de chaînes</em></strong> — d’Abū ʿUmar Yūsuf ibn ʿAbd Allāh ibn Muḥammad ibn ʿAbd al-Barr ibn ʿĀṣim an-Namrī al-Qurṭubī ; édition critique de Muṣṭafā ibn Aḥmad al-ʿAlawī et Muḥammad ʿAbd al-Kabīr al-Bakrī ; Ministère des habous et des affaires islamiques, Maroc, année de publication : 1387 H.</li>
<li><strong><em>Le Choisi, commentaire du Muwaṭṭaʾ</em></strong> (al-Muntaqā) — d’Abū l-Walīd Sulaymān ibn Khalaf ibn Saʿd ibn Ayyūb ibn Wārith at-Tujībī al-Qurṭubī al-Bājī al-Andalusī ; Maṭbaʿat al-Saʿāda, première édition, 1332 H.</li>
<li><strong><em>L’Ouverture du Créateur, commentaire du Ṣaḥīḥ d’al-Bukhārī</em></strong> (Fatḥ al-Bārī) — d’Aḥmad ibn ʿAlī ibn Ḥajar, Abū l-Faḍl al-ʿAsqalānī ; Dār al-Maʿrifa, Beyrouth, 1379 — livres, chapitres et hadiths numérotés par Muḥammad Fuʾād ʿAbd al-Bāqī.</li>
<li><strong><em>L’Arrêt des arrêts, commentaire des Arrêts capitaux</em></strong> (Iḥkām al-aḥkām sharḥ ʿUmdat al-aḥkām) — d’Ibn Daqīq al-ʿĪd ; Maṭbaʿat al-Sunna al-Muḥammadiyya, sans date.</li>
</ol>
<h2>Les livres de fiqh</h2>
<ol>
<li><strong>La <em>Mudawwana</em></strong> — de l’imam Mālik ibn Anas ibn Mālik ibn ʿĀmir al-Aṣbaḥī al-Madanī ; Dār al-Kutub al-ʿIlmiyya, première édition, 1415 H.</li>
<li><strong>Les <em>Notice rares et additions</em></strong> (an-Nawādir wa-ziyādāt) — d’Abū Muḥammad ʿAbd Allāh ibn ʿAbd al-Raḥmān Abī Zayd al-Qayrawānī ; édition critique du professeur Muḥammad ʿAbd al-ʿAzīz ad-Dabbāgh ; première édition, Dār al-Gharb al-Islāmī, 1999.</li>
<li><strong>Le <em>Texte de l’Épître</em></strong> (Matn ar-Risāla) — d’Ibn Abī Zayd al-Qayrawānī, ʿAbd Allāh ibn ʿAbd al-Raḥmān ; Dār al-Fikr.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13011":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13011 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13011 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
