#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13744 (tafsir-tanawi-2 — index des
figures citées / fihris al-aʿlām, annexe du manuel — al-Muḥarrar al-wajīz
d'Ibn ʿAṭiyya).

Remarques de restitution :
- 20 notices biographiques imprimées INTACTES (Ibn ʿAṭiyya → al-Marāghī) —
  traduites fidèlement, noms rendus dans la graphie du livre.
- L'en-tête de la notice d'al-Qurṭubī est perdu (le nom s'est fondu dans le
  paragraphe par perte OCR : « القرطبيأبو عبد الله… ») — restitué en
  en-tête, noté.
- Le tampon de date de la page source (« الإثنين 19 أغسطس 2019 ») est un
  artefact du site manhaj.ma — non rendu, noté.
- L'en-tête de section « الأعلام ترجمتهم » (garbled) rendu par sa forme
  intendue (« الأعلام وترجماتهم »).
- Le <br> parasite dans l'en-tête « مجاهد » — non rendu.
- Aucune section fabriquée : l'annexe est rendue telle quelle (comme les
  annexes 13006/13011 du livre hadith-1es)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>Index des figures citées (<em>fihris al-aʿlām</em>) — le livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya</h1>
<p>Les notices biographiques des figures dont la mention paraît en le « livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> d’Ibn ʿAṭiyya », au programme des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>).</p>
<p>[Le tampon de date de la page source (« lundi 19 août 2019 ») est un artefact du site d’extraction — non rendu.]</p>
<h3>Les figures et leurs notices biographiques</h3>
<h4>Ibn ʿAṭiyya</h4>
<p>ʿAbd al-Ḥaqq b. Ghālib b. ʿAbd al-Raḥmān b. Ghālib b. ʿAbd al-Raʾūf b. ʿAbdallāh b. Tamām b. ʿAṭiyya, Abū Muḥammad al-Maḥāribī al-Gharnāṭī al-Mālikī al-Andalusī, le juriste interprète. Il reçut la science des maîtres d’al-Andalus — dont son père Abū Bakr Ghālib, et Abū ʿAlī al-Ghassānī. Ses compositions sont nombreuses, dont : <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em>. Mort en 542 de l’Hégire.</p>
<h4>Ibn Jarīr al-Ṭabarī</h4>
<p>Muḥammad b. Jarīr b. Yazīd, Abū Jaʿfar al-Ṭabarī, le juriste interprète historien. Il refusa la judicature et l’office des griefs. De ses compositions les plus célèbres : <em>Jāmiʿ al-bayān fī tafsīr al-Qurʾān</em>, <em>Ikhtilāf al-fuqahāʾ</em> et <em>Akhbār al-rusul wa-l-mulūk</em> — connu comme la « Chronique d’al-Ṭabarī ». Né à Āmul, au Ṭabaristān, il s’établit à Baghdad et y mourut en 310 de l’Hégire.</p>
<h4>Ibn ʿĀshūr</h4>
<p>Muḥammad al-Ṭāhir b. ʿĀshūr, le Tunisien : chef des muftis mālikites de Tunis, et shaykh de la mosquée-université d’al-Zaytūna et de ses dépendances en Tunisie. Ses compositions sont nombreuses, dont les plus célèbres : <em>Maqāṣid al-sharīʿa al-islāmiyya</em> et <em>al-Taḥrīr wa-l-tanwīr fī tafsīr al-Qurʾān</em>, et le reste de ses compositions. Mort — Dieu lui fasse miséricorde — en 1393 de l’Hégire.</p>
<h4>Ibn ʿAbbās</h4>
<p>ʿAbdallāh b. ʿAbbās b. ʿAbd al-Muṭṭalib, le Qurashite Hāshimite, le vénérable Compagnon, docteur de la communauté. Né à La Mecque, il grandit au début de l’ère de la prophétie et fréquenta assidûment le Messager de Dieu — paix et bénédiction sur lui —, transmettant de lui maints hadiths : ils atteignirent, en les deux Ṣaḥīḥ et ailleurs, environ 1660 hadiths. Il habita Ṭāʾif, et perdit la vue au dernier de son âge. Mort en cette ville en 68 de l’Hégire.</p>
<h4>Ibn ʿAjība</h4>
<p>Aḥmad b. Muḥammad b. al-Mahdī b. al-Ḥusayn b. Muḥammad, connu comme Ibn ʿAjība et surnommé Abū al-ʿAbbās, l’imam interprète. De ses compositions : <em>al-Baḥr al-madīd fī tafsīr al-Qurʾān al-majīd</em>, la <em>Glose sur le Mukhtaṣar de Khalīl</em>, la <em>Glose sur al-Jāmiʿ al-ṣaghīr</em> d’al-Suyūṭī, et le reste. Mort — Dieu lui fasse miséricorde — en 1224 de l’Hégire.</p>
<h4>Ibn Kathīr</h4>
<p>Ismāʿīl b. ʿUmar b. Kathīr, ʿImād al-Dīn Abū al-Fidāʾ, le Damascène shāfiʿite, l’imam mémorateur, traditionaliste et historien. De ses compositions : le <em>Tafsīr al-Qurʾān al-ʿaẓīm</em> et le <em>Bāʿith al-ḥathīth sharḥ ikhtiṣār ʿulūm al-ḥadīth</em>, et le reste. Mort — Dieu lui fasse miséricorde — en 774 de l’Hégire.</p>
<h4>Abū Bakr Ibn al-ʿArabī</h4>
<p>Muḥammad b. ʿAbdallāh b. Muḥammad, Abū Bakr Ibn al-ʿArabī, le Maʿāfirite sévillan mālikite, des mémorateurs du hadith. Il excella en la belle-lettre et atteignit le degré de l’effort personnel (<em>ijtihād</em>) en les sciences de la religion. Il composa des livres en hadith, droit, fondements, exégèse, littérature et histoire — dont : <em>al-ʿAwāṣim min al-qawāṣim</em>, <em>ʿĀriḍat al-aḥwadhī fī sharḥ al-Tirmidhī</em>, <em>Aḥkām al-Qurʾān</em> et <em>al-Qabas fī sharḥ Muwaṭṭaʾ Ibn Anas</em>. Né à Séville, il y tint la judicature, voyagea vers l’Orient, et mourut aux environs de Fès, où il fut enterré, en l’an 543 de l’Hégire.</p>
<h4>Abū Ḥayyān</h4>
<p>Muḥammad b. Yūsuf b. ʿAlī b. Yūsuf b. Ḥayyān, le Grenadin andalou jaénais nafzite, Athīr al-Dīn Abū Ḥayyān, des grands savants en l’arabe, l’exégèse, le hadith, les biographies et les langues. De ses livres les plus célèbres : <em>al-Baḥr al-muḥīṭ fī tafsīr al-Qurʾān</em>. Né à Grenade, il voyagea vers Malaga, puis s’établit au Caire, où il mourut en 745 de l’Hégire.</p>
<h4>al-Alūsī</h4>
<p>Maḥmūd b. ʿAbdallāh al-Ḥusaynī al-Ālūsī, Shihāb al-Dīn, Abū al-Thanāʾ, interprète, traditionaliste et littérateur. Il assuma la fetva en son pays en 1248 de l’Hégire, puis en fut destitué, et se voua à la science. De ses livres : <em>Rūḥ al-maʿānī fī l-tafsīr</em>. Né à Baghdad, il y mourut en 1270 de l’Hégire.</p>
<h4>ʿĀʾisha, Mère des croyants</h4>
<p>Umm ʿAbdallāh ʿĀʾisha, fille d’Abū Bakr al-Ṣiddīq, le compagnon du Messager de Dieu — paix et bénédiction sur lui — : la plus juriste des femmes des musulmans, et la plus savante d’entre elles en religion et en littérature. Le Prophète — paix et bénédiction sur lui — l’épousa avant l’Hégire et consomma le mariage en la deuxième année après l’Hégire ; elle fut, de ses épouses, la plus abondante en transmission du hadith de lui — paix et bénédiction sur lui. Morte en 58 de l’Hégire.</p>
<h4>al-Ḥasan al-Baṣrī</h4>
<p>Al-Ḥasan b. Yasār al-Baṣrī, le Suivant (<em>tābiʿī</em>) : il fut l’imam des gens de Baṣra et le docteur de la communauté en son temps — l’un des savants, juristes, orateurs, braves et ascètes. Né à Médine, il grandit sous la protection de ʿAlī b. Abī Ṭālib. Mort à Baṣra en 110 de l’Hégire.</p>
<h4>al-Thaʿlabī</h4>
<p>Aḥmad b. Muḥammad b. Ibrāhīm, Abū Isḥāq al-Thaʿlabī, de Nīsābūr, historien et interprète. De ses livres : <em>ʿArāʾis al-majālis fī qiṣaṣ al-anbiyāʾ</em> et <em>al-Kashf wa-l-bayān fī tafsīr al-Qurʾān</em>, connu comme le « Tafsīr d’al-Thaʿlabī ». Mort en 427 de l’Hégire.</p>
<h4>al-Zamakhsharī</h4>
<p>Abū al-Qāsim Maḥmūd b. ʿUmar b. Aḥmad, al-Zamakhsharī « l’hôte de Dieu » (<em>Jār Allāh</em>) : imam en exégèse, grammaire, lexicographie et littérature. Il composa maints livres, dont le plus important, son célèbre tafsīr : <em>al-Kashshāf ʿan ḥaqāʾiq ghawāmiḍ al-tanzīl</em>. Mort en 538 de l’Hégire.</p>
<h4>al-Ḍaḥḥāk</h4>
<p>Abū al-Qāsim al-Ḍaḥḥāk b. Muzāḥim, le Hilālite : grande fut sa part en exégèse et en les récits. Il fut rapporté de lui qu’il dit : “ Il est un droit sur quiconque apprend le Coran, d’être juriste. ” Mort en 202 de l’Hégire.</p>
<h4>Fakhr al-Dīn al-Rāzī</h4>
<p>Muḥammad b. ʿUmar b. al-Ḥasan b. al-Ḥusayn, le Taymite Bakrite, Abū ʿAbdallāh Fakhr al-Dīn al-Rāzī, l’imam interprète. Né à al-Rayy — d’elle sa dénomination —, on le dit aussi « fils du prédicateur de Rayy » (<em>Ibn Khaṭīb al-Rayy</em>) ; il voyagea vers le Khwārizm, le Mā-warāʾ al-nahr et le Khurāsān. L’unique de son temps en le rationnel et le transmis. De ses livres les plus célèbres : le <em>grand Tafsīr dit Mafātīḥ al-ghayb</em>, et <em>al-Maḥṣūl fī ʿilm al-uṣūl</em>. Mort à Harāt en 606 de l’Hégire.</p>
<h4>Qatāda</h4>
<p>Qatāda b. Diʿāma al-Sadūsī, le modèle des interprètes et des traditionalistes. Il transmit de ʿAbdallāh b. Sarjas, Anas b. Mālik, Abū al-Ṭufayl al-Kinānī et Saʿīd b. al-Musayyab. Mort en 118 de l’Hégire.</p>
<h4>al-Qurṭubī</h4>
<p>Abū ʿAbdallāh Muḥammad b. Aḥmad b. Abī Bakr b. Farḥ, l’Anṣārite Khazrajite andalou cordouan, l’interprète. De ses compositions les plus importantes : <em>al-Jāmiʿ li-aḥkām al-Qurʾān</em> — l’un des tafsīrs les plus considérables et des plus grands en profit. Mort — Dieu lui fasse miséricorde — en 671 de l’Hégire.</p>
<p>[En-tête « al-Qurṭubī » restitué : le nom s’était fondu dans le paragraphe par perte OCR (« القرطبيأبو عبد الله… »).]</p>
<h4>Mālik b. Anas</h4>
<p>Mālik b. Anas, Abū ʿAbdallāh le Médinois, l’imam de la Maison de l’Hégire. Son école se répandit au Ḥijāz, à Baṣra et leurs alentours, en Ifrīqiya, au Maghreb, en al-Andalus et en Égypte ; ses partisans sont très nombreux. Né en 93 de l’Hégire, il mourut en 179.</p>
<h4>Mujāhid</h4>
<p>Mujāhid b. Jabr, le shaykh des lecteurs et des interprètes. Il transmit d’Ibn ʿAbbās, Abū Hurayra, ʿĀʾisha, Saʿd b. Abī Waqqāṣ, ʿAbdallāh b. ʿAmr, Rāfiʿ b. Khadīj, Jābir b. ʿAbdallāh, Abū Saʿīd al-Khudrī et d’autres. Mort en 104 de l’Hégire.</p>
<h4>al-Marāghī</h4>
<p>Aḥmad b. Muṣṭafā al-Marāghī, interprète égyptien, sorti de Dār al-ʿUlūm en 1909, puis enseignant de la Loi islamique en cette maison. De ses compositions : le <em>Tafsīr al-Marāghī</em>, <em>al-Ḥisba fī l-islām</em>, <em>al-Wajīz fī uṣūl al-fiqh</em> et <em>ʿUlūm al-balāgha</em>. Mort au Caire en 1371 de l’Hégire.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13744":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13744 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13744 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
