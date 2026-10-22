#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : doc 14063 (tafsir-5ep, ترجمة الأعلام — index biographique).

Vérifications :
- 11 notices : al-Maḥallī (864 H — notice d'ouverture SANS titre h2 dans la
  source : titre restitué, manifestement perdu par l'OCR), al-Suyūṭī (911 H),
  Ibn Ǧuzayy (741 H), Ibn ʿĀshūr (1393 H), Ibn ʿAbbās (68 H — ḥabr al-umma,
  ~1660 hadiths dans les deux Ṣaḥīḥ et ailleurs, aveugle en fin de vie,
  Ṭāʾif), Ibn ʿAǧība (1224 H), Ibn Kathīr (774 H), Abū Ḥayyān (745 H —
  al-Jayyānī al-Nifzī, Gharnāṭa→Mālaqa→Caire), Fakhr al-Dīn al-Rāzī (606 H —
  al-Taymī al-Bakrī, Ibn Khaṭīb al-Rayy, Khwārizm/Transoxiane/Khurāsān,
  Herāt), Qatāda (118 H — ibn Diʿāma al-Sadūsī), al-Qurṭubī (671 H).
- Translittérations harmonisées sur 14067 (Sources et références, main) :
  Ibn Ǧuzayy, Ibn ʿAǧība, Ǧamʿ al-Ǧawāmiʿ, al-Ǧāmiʿ li-aḥkām al-Qurʾān.
- Corrections vs baseline LLM : « Manhāj » → Minhāj (le manuel visé EST le
  Minhāj des shāfiʿites) ; « une ville dans le Haute-Égypte » → en
  Haute-Égypte ; « Il a servi le Prophète » → لازم = « il tint compagnie » ;
  « de nombreuses hadiths » → de nombreux hadiths ; « les deux Sahīhs » →
  les deux Ṣaḥīḥ ; ajouts des traductions des nisbas manquantes
  (ʿImād al-Dīn, Jayyānī/Nifzī, ouḥid zamānihi fī al-maʿqūl wa-l-manqūl).
- Titres d'œuvres : italique implicite par « », conservés tels quels avec
  leurs gloses (genre des ouvrages) comme 14067.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>Personnalités citées (aʿlām) — le Tafsīr al-Jalālayn</h1>
<p>Notices biographiques des personnalités citées dans le livre d'exégèse fondé sur le Tafsīr al-Jalālayn, pour la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq).</p>
<h2>Jalāl al-Dīn al-Maḥallī :</h2>
<p>Muḥammad ibn Aḥmad ibn Muḥammad ibn Ibrāhīm, Jalāl al-Dīn al-Maḥallī al-Shāfiʿī : spécialiste des fondements du droit (uṣūlī) et exégète. Né et mort au Caire, il composa un livre d'exégèse que Jalāl al-Dīn al-Suyūṭī acheva — d'où son nom de « Tafsīr al-Jalālayn ». Il a d'autres œuvres, dont « Kanz al-rāghibīn » [Le Trésor des désireux], commentaire du Minhāj en droit shāfiʿite, et « al-Badr al-ṭāliʿ fī ḥall Ǧamʿ al-Ǧawāmiʿ » [La Lune montante, résolution du Recueil des recueils], en fondements du droit, parmi d'autres. Il mourut en 864 H.</p>
<h2>Jalāl al-Dīn al-Suyūṭī :</h2>
<p>ʿAbd al-Raḥmān ibn Abī Bakr, l'imam Jalāl al-Dīn Abū al-Faḍl al-Miṣrī al-Suyūṭī — ainsi nommé d'après Asyūṭ, ville de Haute-Égypte. Savant encyclopédique en hadith, exégèse, langue, histoire, littérature, droit et autres sciences, on lui attribue environ 600 ouvrages. Parmi ses livres les plus célèbres : « al-Ǧāmiʿ al-kabīr » [Le Grand Recueil] et « al-Itqān fī ʿulūm al-Qurʾān » [La Maîtrise des sciences coraniques]. Il acheva l'exégèse du noble Coran nommée « Tafsīr al-Jalālayn ». Qu'Allah lui fasse miséricorde, il mourut en 911 H.</p>
<h2>Ibn Ǧuzayy :</h2>
<p>Muḥammad ibn Aḥmad ibn ʿAbd Allāh ibn Yaḥyā ibn ʿAbd al-Raḥmān ibn Yūsuf ibn Ǧuzayy al-Kalbī al-Andalusī. Il laissa de nombreuses œuvres dans les diverses disciplines du savoir : le droit, le hadith, le soufisme et les lectures coraniques. Parmi ses œuvres les plus importantes : « al-Qawānīn al-fiqhiyya » [Les Lois juridiques] et « al-Tashīl li-ʿulūm al-tanzīl » [La Facilitation des sciences de la Révélation]. Qu'Allah lui fasse miséricorde, il mourut en 741 H.</p>
<h2>Ibn ʿĀshūr :</h2>
<p>Muḥammad al-Ṭāhir ibn ʿĀshūr al-Tūnisī, président des muftis malikites de Tunis, et shaykh de la Zaytūna et de ses annexes en Tunisie. Il a de nombreuses œuvres, dont les plus célèbres : « Maqāṣid al-sharīʿa al-islāmiyya » [Les Finalités de la loi islamique] et « al-Taḥrīr wa-l-tanwīr fī tafsīr al-Qurʾān » [La Libération et l'illumination, en exégèse du Coran], parmi d'autres. Qu'Allah lui fasse miséricorde, il mourut en 1393 H.</p>
<h2>Ibn ʿAbbās :</h2>
<p>ʿAbd Allāh ibn ʿAbbās ibn ʿAbd al-Muṭṭalib al-Qurashī al-Hāshimī, le noble Compagnon, « l'érudit de la Communauté » (ḥabr al-umma). Né à La Mecque et grandi aux débuts de l'ère prophétique, il tint compagnie au Messager d'Allah — paix et bénédiction sur lui — et rapporta de lui de nombreux hadiths, au nombre d'environ 1660 dans les deux Ṣaḥīḥ et ailleurs. Il perdit la vue en fin de vie, s'établit alors à Ṭāʾif, et y mourut en 68 H.</p>
<h2>Ibn ʿAǧība :</h2>
<p>Aḥmad ibn Muḥammad ibn al-Mahdī ibn al-Ḥusayn ibn Muḥammad, connu sous le nom d'Ibn ʿAǧība, portant la kunya d'Abū al-ʿAbbās, l'imam exégète. Parmi ses œuvres : « al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd » [L'Océan prodigieux, en exégèse du glorieux Coran], une ḥāshiya sur le Mukhtaṣar de Khalīl, une ḥāshiya sur « al-Ǧāmiʿ al-ṣaghīr » d'al-Suyūṭī, parmi d'autres. Qu'Allah lui fasse miséricorde, il mourut en 1224 H.</p>
<h2>Ibn Kathīr :</h2>
<p>Ismāʿīl ibn ʿUmar ibn Kathīr, ʿImād al-Dīn Abū al-Fidāʾ al-Dimashqī al-Shāfiʿī, l'imam, le ḥāfiẓ, le traditionniste et l'historien. Parmi ses œuvres : « Tafsīr al-Qurʾān al-ʿaẓīm » [L'Exégèse du noble Coran] et « al-Bāʿith al-ḥathīth sharḥ ikhtiṣār ʿulūm al-ḥadīth » [Le Mobilisateur ardent, commentaire de l'Abrégé des sciences du hadith], parmi d'autres. Qu'Allah lui fasse miséricorde, il mourut en 774 H.</p>
<h2>Abū Ḥayyān :</h2>
<p>Muḥammad ibn Yūsuf ibn ʿAlī ibn Yūsuf ibn Ḥayyān al-Gharnāṭī al-Andalusī al-Jayyānī al-Nifzī, Athīr al-Dīn Abū Ḥayyān, l'un des grands savants de la langue arabe, de l'exégèse, du hadith, des biographies et des langues. Parmi ses livres les plus célèbres : « al-Baḥr al-muḥīṭ » [L'Océan enveloppant, en exégèse du Coran]. Né à Grenade, il voyagea vers Málaga puis s'établit au Caire, où il mourut en 745 H.</p>
<h2>Fakhr al-Dīn al-Rāzī :</h2>
<p>Muḥammad ibn ʿUmar ibn al-Ḥasan ibn al-Ḥusayn al-Taymī al-Bakrī, Abū ʿAbd Allāh, Fakhr al-Dīn al-Rāzī, l'imam exégète, unique de son temps en sciences rationnelles et traditionnelles. Parmi ses livres les plus célèbres : « al-Tafsīr al-kabīr » dit « Mafātīḥ al-ghayb » [Les Clefs du mystère] et « al-Maḥṣūl fī ʿilm al-uṣūl » [Le Résultat, en science des fondements]. Né à Rayy — d'où sa nisba —, on l'appelle aussi Ibn Khaṭīb al-Rayy ; il voyagea vers le Khwārizm, la Transoxiane et le Khurāsān, et mourut à Herāt en 606 H.</p>
<h2>Qatāda :</h2>
<p>Qatāda ibn Diʿāma al-Sadūsī, le modèle des exégètes et des traditionnistes. Il rapporta d'après ʿAbd Allāh ibn Sarjis, Anas ibn Mālik, Abū al-Ṭufayl al-Kinānī et Saʿīd ibn al-Musayyab. Qu'Allah lui fasse miséricorde, il mourut en 118 H.</p>
<h2>al-Qurṭubī :</h2>
<p>Muḥammad ibn Aḥmad ibn Abī Bakr ibn Farḥ, Abū ʿAbd Allāh al-Anṣārī al-Khazraǧī al-Andalusī al-Qurṭubī, l'exégète. Parmi ses œuvres les plus importantes : « al-Ǧāmiʿ li-aḥkām al-Qurʾān » [Le Recueil des règles du Coran], l'un des plus considérables tafsīr et des plus profitables. Qu'Allah lui fasse miséricorde, il mourut en 671 H.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "14063":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 14063 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 14063 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
