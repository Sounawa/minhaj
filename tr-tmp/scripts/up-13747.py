#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13747 (tafsir-tanawi-2 — liste des
sources et références, annexe du manuel — al-Muḥarrar al-wajīz d'Ibn
ʿAṭiyya).

Remarques de restitution :
- 27 notices bibliographiques imprimées INTACTES (le muṣḥaf de Warsh + 4
  premières entrées + 21 entrées de la liste) — traduites fidèlement.
- L'entrée du muṣḥaf a perdu son titre (elle commence à « برواية ورش ») —
  titre restitué, noté.
- L'entrée « البحر المحيط » d'Abū Ḥayyān s'est fondue dans l'entrée
  « الأعلام » (perte OCR) — titre en en-tête restitué, noté.
- Le tampon de date de la page source (« الإثنين 19 أغسطس 2019 ») est un
  artefact du site d'extraction — non rendu, noté.
- Coquille imprimée : « تونس 1984 هـ » — 1984 est une année grégorienne
  (le « هـ » est parasites) — noté.
- Aucune section fabriquée : l'annexe est rendue telle quelle (comme les
  annexes 13006/13011/13744)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>Liste des sources et références (<em>lāʾiḥat al-maṣādir wa-l-marājiʿ</em>) — le livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya</h1>
<p>La liste des sources et références du « livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> d’Ibn ʿAṭiyya », au programme des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>).</p>
<p>[Le tampon de date de la page source (« lundi 19 août 2019 ») est un artefact du site d’extraction — non rendu.]</p>
<ul>
<li><strong>Le noble Coran, en la lecture de Warsh d’après Nāfiʿ</strong> — l’édition publiée par la Fondation Mohammed VI pour l’impression du noble muṣḥaf, troisième édition, 2012.
<p>[Titre de l’entrée restitué : l’entrée imprimée commence à « برواية ورش » — le titre est perdu (perte OCR).]</p></li>
<li><strong><em>Aḥkām al-Qurʾān</em> (Les statuts du Coran)</strong> — du cadi Muḥammad b. ʿAbdallāh, Abū Bakr Ibn al-ʿArabī, le Maʿāfirite sévillan mālikite (mort en 543 H) ; Dār al-Kutub al-ʿIlmiyya, Beyrouth, Liban, troisième édition, 1424 H — 2003.</li>
<li><strong><em>Al-Aʿlām</em> (Les figures illustres)</strong> — de Khayr al-Dīn b. Maḥmūd b. Muḥammad b. ʿAlī b. Fāris, al-Ziriklī le Damascène (mort en 1396 H) ; Dār al-ʿIlm li-l-Malāyīn, quinzième édition, 2002.</li>
<li><strong><em>Al-Baḥr al-muḥīṭ fī l-tafsīr</em> (L’océan enveloppant en l’exégèse)</strong> — d’Abū Ḥayyān Muḥammad b. Yūsuf b. ʿAlī b. Yūsuf b. Ḥayyān, Athīr al-Dīn l’Andalou (mort en 745 H) ; édition critique de Ṣidqī Muḥammad Jamīl ; Dār al-Fikr, Beyrouth, édition de 1420 H.
<p>[Titre en en-tête restitué : l’entrée s’était fondue dans l’entrée « al-Aʿlām » par perte OCR.]</p></li>
<li><strong><em>Al-Baḥr al-madīd fī tafsīr al-Qurʾān al-majīd</em> (L’océan diffus en l’exégèse du Coran glorieux)</strong> — d’Abū al-ʿAbbās Aḥmad b. Muḥammad b. al-Mahdī b. ʿAjība, le Ḥasanite anjrite fassi soufi (mort en 1224 H) ; édition critique d’Aḥmad ʿAbdallāh al-Qurashī Raslān ; édition de 1419 H.</li>
</ul>
<h3>Les sources et références</h3>
<ul>
<li><strong><em>Taḥrīr al-maʿnā l-sadīd wa-tanwīr al-ʿaql al-jadīd min tafsīr al-kitāb al-majīd</em>, dit « al-Taḥrīr wa-l-tanwīr »</strong> — de Muḥammad al-Ṭāhir b. Muḥammad b. Muḥammad al-Ṭāhir b. ʿĀshūr le Tunisien (mort en 1393 H) ; Dār al-Tūnisiyya li-l-Nashr, Tunis, 1984. [Coquille de l’imprimé : « 1984 هـ » — l’année est grégorienne.]</li>
<li><strong><em>Al-Tashīl li-ʿulūm al-tanzīl</em> (La facilitation des sciences de la descente)</strong> — d’Abū al-Qāsim Muḥammad b. Aḥmad b. Muḥammad b. ʿAbdallāh, Ibn Juzayy, le Kalbite grenadin (mort en 741 H) ; édition critique du Dr ʿAbdallāh al-Khālidī ; société Dār al-Arqam b. Abī al-Arqam, Beyrouth, première édition, 1416 H.</li>
<li><strong><em>Tafsīr al-Qurʾān al-ʿaẓīm</em> (L’exégèse du Coran auguste)</strong> — d’Abū al-Fidāʾ Ismāʿīl b. ʿUmar b. Kathīr, le Qurashite de Baṣra puis de Damas (mort en 774 H) ; édition critique de Sāmī b. Muḥammad Salāma ; Dār Ṭayba li-l-Nashr wa-l-Tawzīʿ, deuxième édition, 1420 H — 1999.</li>
<li><strong><em>Tafsīr al-Qurʾān al-ʿaẓīm</em> (L’exégèse du Coran auguste)</strong> — de Muḥammad b. ʿAbd al-Raḥmān b. Muḥammad b. Idrīs b. al-Mundhir, le Tamīmite Ḥanẓalite al-Rāzī, Ibn Abī Ḥātim (mort en 327 H) ; édition critique d’Asʿad Muḥammad al-Ṭayyib ; Maktabat Nizār Muṣṭafā al-Bāz, Arabie saoudite, troisième édition, 1419 H.</li>
<li><strong><em>Jāmiʿ al-bayān fī taʾwīl al-Qurʾān</em> (Le recueil de l’éclaircissement en l’interprétation du Coran)</strong> — de Muḥammad b. Jarīr b. Yazīd b. Kathīr b. Ghālib, l’Āmulite Abū Jaʿfar al-Ṭabarī (mort en 310 H) ; édition critique d’Aḥmad Muḥammad Shākir ; Muʾassasat al-Risāla, première édition, 1420 H — 2000.</li>
<li><strong><em>Le Recueil chaîné, sonnant et abrégé, des affaires de l’Envoyé de Dieu — paix et bénédiction sur lui —, de ses sunnas et de ses jours</em>, dit « Ṣaḥīḥ al-Bukhārī »</strong> — de Muḥammad b. Ismāʿīl, Abū ʿAbdallāh al-Bukhārī le Jaʿfite (mort en 256 H) ; édition critique de Muḥammad Zuhayr b. Nāṣir al-Nāṣir ; Dār Ṭawq al-Najāt, première édition, 1422 H.</li>
<li><strong><em>Al-Jāmiʿ li-aḥkām al-Qurʾān, wa-l-mubayyin li-mā taḍammanahu min al-sunna wa-āy al-furqān</em> (Le recueil des statuts du Coran, et l’exposant de ce qu’il renferme de sunna et des versets du discernement)</strong> — d’Abū ʿAbdallāh Muḥammad b. Aḥmad b. Abī Bakr b. Farḥ, l’Anṣārite Khazrajite Shams al-Dīn al-Qurṭubī (mort en 671 H) ; édition critique d’Aḥmad al-Bardūnī et Ibrāhīm Aṭfīsh ; Dār al-Kutub al-Miṣriyya, Le Caire, deuxième édition, 1384 H.</li>
<li><strong><em>Rūḥ al-maʿānī fī tafsīr al-Qurʾān al-ʿaẓīm wa-l-sabʿ al-mathānī</em> (L’esprit des sens en l’exégèse du Coran auguste et des sept répétées)</strong> — de Shihāb al-Dīn Maḥmūd b. ʿAbdallāh al-Ḥusaynī al-Alūsī (mort en 1270 H) ; édition critique de ʿAlī ʿAbd al-Bārī ʿAṭiyya ; Dār al-Kutub al-ʿIlmiyya, Beyrouth, première édition, 1415 H.</li>
<li><strong>Les <em>Sunan</em> d’Ibn Māja</strong> — d’Ibn Māja, Abū ʿAbdallāh Muḥammad b. Yazīd al-Qazwīnī — Māja étant le nom de son père Yazīd — (mort en 273 H) ; édition critique de Muḥammad Fuʾād ʿAbd al-Bāqī ; Dār Iḥyāʾ al-Kutub al-ʿArabiyya, Fayṣal ʿĪsā al-Bābī al-Ḥalabī.</li>
<li><strong>Les <em>Sunan</em> d’Abū Dāwūd</strong> — d’Abū Dāwūd Sulaymān b. al-Ashʿath b. Isḥāq b. Bashīr b. Shaddād b. ʿAmr, l’Azdite de Sijistān (mort en 275 H) ; édition critique de Shuʿayb al-Arnaʾūṭ et Muḥammad Kāmil Qarah Ballī ; Dār al-Risāla al-ʿĀlamiyya, première édition, 1430 H — 2009.</li>
<li><strong>Les <em>Sunan</em> d’at-Tirmidhī</strong> — de Muḥammad b. ʿĪsā b. Sawra b. Mūsā b. al-Ḍaḥḥāk, at-Tirmidhī, Abū ʿĪsā (mort en 279 H) ; édition critique et annotation d’Aḥmad Muḥammad Shākir, Muḥammad Fuʾād ʿAbd al-Bāqī et Ibrāhīm ʿAṭwa ʿAwḍ ; société de la librairie et imprimerie Muṣṭafā al-Bābī al-Ḥalabī, Égypte, deuxième édition, 1395 H.</li>
<li><strong>La <em>Sīra nabawiyya</em> d’Ibn Hishām</strong> — de ʿAbd al-Malik b. Hishām b. Ayyūb, le Ḥimyarite Maʿāfirite, Abū Muḥammad Jamāl al-Dīn (mort en 213 H) ; société de la librairie et imprimerie Muṣṭafā al-Bābī al-Ḥalabī et ses fils, Égypte, deuxième édition, 1375 H — 1955.</li>
<li><strong><em>Shuʿab al-īmān</em> (Les rameaux de la foi)</strong> — d’Aḥmad b. al-Ḥusayn b. ʿAlī b. Mūsā, le Khusrūjirdite khurāsānien Abū Bakr al-Bayhaqī (mort en 458 H) ; édition critique du Dr ʿAbd al-ʿAlī ʿAbd al-Ḥamīd Ḥāmid ; Maktabat al-Rushd li-l-Nashr wa-l-Tawzīʿ, Riyad, première édition, 1423 H — 2003.</li>
<li><strong><em>Ṣafwat al-tafāsīr</em> (La crème des exégèses)</strong> — de Muḥammad ʿAlī al-Ṣābūnī ; Dār al-Ṣābūnī li-l-Ṭibāʿa wa-l-Nashr wa-l-Tawzīʿ, Le Caire, première édition, 1417 H.</li>
<li><strong><em>Al-Kashshāf ʿan ḥaqāʾiq ghawāmiḍ al-tanzīl</em> (Le découvreur des réalités des obscursités de la descente)</strong> — d’Abū al-Qāsim Maḥmūd b. ʿUmar b. Aḥmad, al-Zamakhsharī « l’hôte de Dieu » (mort en 538 H) ; Dār al-Kitāb al-ʿArabī, Beyrouth, troisième édition, 1407 H.</li>
<li><strong><em>Al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> (Le rédigé concis en l’exégèse du livre auguste)</strong> — d’Abū Muḥammad ʿAbd al-Ḥaqq b. Ghālib b. ʿAbd al-Raḥmān b. Tamām b. ʿAṭiyya, l’Andalou Maḥāribite (mort en 542 H) ; édition critique de ʿAbd al-Salām ʿAbd al-Shāfī Muḥammad ; Dār al-Kutub al-ʿIlmiyya, Beyrouth, première édition, 1422 H.</li>
<li><strong><em>Le Chaîné sonnant et abrégé, du transfert du juste d’après le juste jusqu’à l’Envoyé de Dieu — paix et bénédiction sur lui</em></strong> (le Ṣaḥīḥ de Muslim) — de Muslim b. al-Ḥajjāj, Abū al-Ḥusayn al-Qushayrī al-Naysābūrī (mort en 261 H) ; édition critique de Muḥammad Fuʾād ʿAbd al-Bāqī ; Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth.</li>
<li><strong><em>Al-Muʿjam al-awsaṭ</em> (Le dictionnaire moyen)</strong> — de Sulaymān b. Aḥmad b. Ayyūb b. Maṭīr, le Laḵmite syrien Abū al-Qāsim al-Ṭabarānī (mort en 360 H) ; édition critique de Ṭāriq b. ʿAwḍallāh b. Muḥammad et ʿAbd al-Muḥsin b. Ibrāhīm al-Ḥusaynī ; Dār al-Ḥaramayn, Le Caire.</li>
<li><strong><em>Mafātīḥ al-ghayb</em> (Les clefs du mystère), dit le « grand Tafsīr »</strong> — d’Abū ʿAbdallāh Muḥammad b. ʿUmar b. al-Ḥasan b. al-Ḥusayn, le Taymite al-Rāzī, surnommé Fakhr al-Dīn al-Rāzī, fils du prédicateur de Rayy (mort en 606 H) ; Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth, troisième édition, 1420 H.</li>
<li><strong><em>Al-Muwāfaqāt fī uṣūl al-sharīʿa</em> (Les concordances en les fondements de la Loi)</strong> — de l’imam al-Shāṭibī, mort en 790 H ; édition critique d’Abū ʿUbayda Mashhūr b. Ḥasan Āl Salmān ; éditeur : Dār Ibn ʿAffān, première édition, 1417 H — 1997.</li>
<li><strong>Le <em>Muwaṭṭaʾ</em></strong> — de l’imam Mālik b. Anas b. Mālik b. Abī ʿĀmir, l’Aṣbaḥite Médinois (mort en 179 H) ; révisé, numéroté, muni de l’extraction de ses hadiths et annoté par Muḥammad Fuʾād ʿAbd al-Bāqī ; Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth, Liban, 1406 H — 1985.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13747":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13747 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13747 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
