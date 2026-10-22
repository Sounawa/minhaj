#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13006 (hadith-1es, biographies des
Compagnons dont les noms paraissent en la matière — 28 entrées
d'aʿlām issues du Muwaṭṭaʾ/Zarqānī).

Conventions main (cf. 12875-13005 du même livre) :
- h1 « Biographies des Compagnons, que Dieu soit satisfait d'eux
  (tarājim al-ṣaḥāba, raḍiya Allāhu ʿanhum) » + sous-titre du source
  (« الواردة أسماؤهم في مادة الحديث… س 1 إع عت ») rendu en intro ;
  29e leçon (annexe aʿlām).
- 28 entrées : ʿAbd Allāh b. Zayd b. ʿĀṣim (al-Ḥarra 63 H) ; Abū
  Hurayra (ʿAbd al-Raḥmān b. Ṣakhr ; la chatte dans la manche —
  « ô Abū Hurayra » ; Khaybar ; 57-59 H) ; Abū Qatāda (le cavalier
  du Prophète ; al-Ḥārith/al-Nuʿmān/ʿAmr b. Rabʿī) ; Umm Salama
  (Hind bt. Abī Umayya ; sœur d'Ibn Yāsir par la mère ou l'allaitement ;
  Shawwāl après Badr ; 59 ou 62) ; Ibn ʿAbbās (le turjumān du Coran ;
  « le savant et la mer » ; Gabriel ×2 ; la sagesse ×2 ; Ṭāʾif 68 H) ;
  Hishām b. ʿUrwa (fiqh, tadlīs parfois ; 145/146 à 87 ans) ;
  ʿAbd Allāh al-Ṣanābiḥī (compagnonnage disputé ; Bukhārī vs
  al-Ḥāfiẓ ; Ibn Maʿīn) ; Ibn ʿUmar (premier né de l'islam ?
  « un homme de bien » ; 73/74) ; al-Mughīra b. Shuʿba (« Mughīra
  du ra'y », dahāʾ ; 50) ; Yazīd b. ʿAbd Allāh b. Qusayṭ (122) ;
  al-Miqdād b. al-Aswad (adopté par al-Aswad b. ʿAbd Yaghūth ; =
  b. ʿAmr b. Thaʿlaba al-Bahrānī (Quḍāʿa puis Kinda) ; CAVALIER DE
  BADR — seul attesté ; 33 H à 70 ans) ; Busra bt. Ṣafwān (le hadith
  du wuḍūʾ du toucher) ; ʿĀʾisha (mariée à 6 ans, consommé à 9 ;
  veuve à 18 ; +40 ans ; 57/58) ; ʿUmar (Abū Ḥafṣ ; modèle de
  justice/ascétisme/humilité ; martyre 23) ; ʿUthmān (Dhū l-Nūrayn ;
  l'Abyssinie avec Ruqayya ; martyre 35 à 90 ans) ; ʿAṭāʾ b. Yasār
  (103 ou 94) ; Umm Sulaym (al-Ghumayṣāʾ, mère d'Anas) ; Umm Qays
  bt. Miḥṣan (sœur d'ʿUkkāsha ; Āmina) ; Yaḥyā b. Saʿīd (Aḥmad :
  « le plus établi des hommes » ; 144 ±1) ; al-Barāʾ b. ʿĀzib
  (Abū ʿAmāra/Abū ʿAmr/Abū l-Ṭufayl ; trop jeune à Badr ; bayʿat
  al-riḍwān) ; Abū Bakr (le plus fort en foi ; 13) ; ʿAlī (40) ;
  al-Bayāḍī (Furwa b. ʿAmr Wadqa — vérifié web : Ibn Wadhifa chez
  les généalogues ; la Rawḍa des Banū Bayāḍa, clan des Khazraj ;
  Wathīma/le Livre de l'apostasie : 2 chevaux ; 1000 wasq/jour) ;
  Abū Saʿīd mawlā ʿĀmir b. Kurayz (Successor anonyme ; Ḥākim/al-ʿAlāʾ
  → Ubayy) ; ʿAbd Allāh ibn Buḥayna (Buḥayna = la MÈRE → ibn à
  l'alif ; Mālik b. al-Qashab ; ḥalīf des Banū l-Muṭṭalib ; +50) ;
  Ḥafṣa (née 5 ans avant la mission ; 41) ; Miḥjan (b. Abī Miḥjan
  al-Daylī ; son fils Bishr — dit Busr) ; Anas b. Mālik (Abū
  Ḥamza ; « il vint quand j'avais 10 ans, mourut quand j'en avais
  20 » ; 93 H, passé cent).
- Pas de tamhīl/hadiths/tahlīl : leçon-annexe d'aʿlām — rendue
  fidèlement (liste + intro), sans sections fabriquées.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Biographies des Compagnons, que Dieu soit satisfait d’eux (<em>tarājim al-ṣaḥāba, raḍiya Llāhu ʿanhum</em>)</h1>
<p>Biographies des Compagnons — que Dieu soit satisfait d’eux — dont les noms paraissent en la matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>), première étape :</p>
<ul>
<li><strong>ʿAbd Allāh ibn Zayd ibn ʿĀṣim</strong> — l’Anṣārite Māzinīte Médinois ; le compagnonnage lui appartient, à lui et à ses deux parents ; il assista à Uḥud ; son neveu ʿIbād ibn Tamīm, Saʿīd ibn al-Musayyab et une troupe transmirent de lui. Tué à la <em>Ḥarra</em> en Dhū l-ḥijja de l’an 63 de l’Hégire, à soixante-dix ans.</li>
<li><strong>Abū Hurayra</strong> — ʿAbd al-Raḥmān ibn Ṣakhr — que Dieu soit satisfait de lui ; la cause de son surnom : ce qu’Ibn ʿAbd al-Barr rapporta de lui : “Je portai un jour une chatte dans ma manche ; le Prophète — paix et bénédiction sur lui — me vit et dit : Qu’est-ce que c’est ? Je dis : une chatte. Il dit : Ô Abū Hurayra.” — et il fut dit autre chose. Il embrassa l’islam l’année de Khaybar et y assista avec le Messager de Dieu — paix et bénédiction sur lui —, puis le suivit d’une fréquention entière, en désir de science. Mort en 57, 58 ou 59 de l’Hégire, à soixante-dix-huit ans ; enterré à al-Baqīʿ.</li>
<li><strong>Abū Qatāda</strong> — l’Anṣārite, cavalier du Prophète — paix et bénédiction sur lui. Son nom fut dit al-Ḥārith, et al-Nuʿmān, et ʿAmr ibn Rabʿī al-Salamī. Il assista à Uḥud et aux batailles qui suivirent ; ses deux fils ʿAbd Allāh et Thābit, Jābir ibn ʿAbd Allāh, Anas et une multitude transmirent de lui. Mort en l’an cinquante-quatre, à soixante-dix ans.</li>
<li><strong>Umm Salama, épouse du Prophète</strong> — Umm Salama Hind, fille d’Abū Umayya — son nom Ḥudhayfa, et on dit Sahl — fils d’al-Mughīra ; Qurashite Machzoumite, Mère des croyants ; sœur de ʿAmmār ibn Yāsir par sa mère — et on dit : par l’allaitement. Le Messager de Dieu — paix et bénédiction sur lui — l’épousa en Shawwāl, au lendemain de Badr ; elle mourut en Shawwāl de l’an 59 — il fut dit : l’an 62.</li>
<li><strong>ʿAbd Allāh ibn ʿAbbās</strong> — Hāshimite, Abū l-ʿAbbās, cousin du Messager de Dieu — paix et bénédiction sur lui — et interprète (<em>turjumān</em>) du Coran ; on l’appelait “le savant” (<em>al-ḥabr</em>) et “la mer”. Il vit Gabriel deux fois, et le Prophète — paix et bénédiction sur lui — implora pour lui la sagesse deux fois. Mort à Ṭāʾif en l’an soixante-huit, à soixante et onze ou soixante-douze ans.</li>
<li><strong>Hishām ibn ʿUrwa</strong> — fils d’ʿUrwa ibn al-Zubayr ibn al-ʿAwwām, Asadite ; il transmit de son père, de son oncle ʿAbd Allāh ibn al-Zubayr et d’une troupe ; sûr, juriste, des moindres Suivants ; Mālik, Abū Ḥanīfa, les deux Sufyān, Shuʿba, les deux Ḥammād et une multitude transmirent de lui ; il pratiquait parfois le <em>tadlīs</em>. Mort en 145 ou 146, à quatre-vingt-sept ans.</li>
<li><strong>ʿAbd Allāh al-Ṣanābiḥī</strong> — on dit aussi Abū ʿAbd Allāh ; son compagnonnage est disputé ; il transmit du Prophète — paix et bénédiction sur lui —, d’Abū Bakr et d’ʿUbāda ibn al-Ṣāmit. Al-Bukhārī dit : Mālik se trompa en le nommant ʿAbd Allāh al-Ṣanābiḥī — il n’est qu’Abū ʿAbd Allāh, qui n’entendit pas le Prophète ; al-Ḥāfiẓ rébuta cette imputation d’erreur, et Yaḥyā ibn Maʿīn dit : “ʿAbd Allāh al-Ṣanābiḥī — les Médinois transmettent de lui : il ressemble qu’il ait le compagnonnage.”</li>
<li><strong>ʿAbd Allāh ibn ʿUmar</strong> — Qurashite ʿAdawite, Abū ʿAbd al-Raḥmān, Mecquois ; il embrassa l’islam de bonne heure avec son père, tout enfant — il fut même rapporté qu’il fut le premier nouveau-né né en l’islam ; trop jeune à Uḥud, il assista à la Tranchée et aux batailles suivantes ; le Prophète — paix et bénédiction sur lui — dit de lui : “C’est un homme de bien.” Mort en l’an soixante-treize — il fut dit : soixante-quatorze.</li>
<li><strong>Al-Mughīra ibn Shuʿba</strong> — Thaqafite, Abū ʿĪsā ; il embrassa l’islam l’année de la Tranchée, et sa première bataille fut Ḥudaybiya ; ses fils ʿUrwa et Ḥamza et une multitude transmirent de lui. Ibn Saʿd dit : on l’appelait “Mughīra de l’avis” (<em>al-raʾy</em>), et il était d’une grande ruse. Mort en l’an cinquante.</li>
<li><strong>Yazīd ibn ʿAbd Allāh ibn Qusayṭ</strong> — Laythite Médinois ; il transmit d’Ibn ʿUmar, d’Abū Hurayra, de ʿAṭāʾ ibn Yasār et d’un nombre ; ses deux fils ʿAbd Allāh et al-Qāsim, Mālik, Ibn Isḥāq et d’autres transmirent de lui ; an-Nasāʾī, Ibn Saʿd et d’autres le validèrent. Mort en l’an cent vingt-deux.</li>
<li><strong>Al-Miqdād ibn al-Aswad</strong> — Zuhrīte : al-Aswad ibn ʿAbd Yaghūth l’adopta tout enfant, et il fut connu par lui ; il est al-Miqdād ibn ʿAmr ibn Thaʿlaba al-Bahrānī — fatha du <em>bāʾ</em> et du <em>rāʾ</em> — tribu de Quḍāʿa puis de Kinda ; Compagnon renommé des devanciers, il assista à toutes les batailles et fut le cavalier du jour de Badr — il n’est pas établi qu’un autre cavalier y assistât. Mort en l’an 33 de l’Hégire, de commun accord, à soixante-dix ans.</li>
<li><strong>Busra fille de Ṣafwān</strong> — Asadite ; elle a le compagnonnage et la narration du hadith des ablutions du toucher du membre ; ʿAbd Allāh ibn ʿAmr, ʿUrwa ibn al-Zubayr, Marwān ibn al-Ḥakam et d’autres transmirent d’elle.</li>
<li><strong>La Mère des croyants ʿĀʾisha</strong> — ʿĀʾisha la Véridique, fille d’Abū Bakr le Véridique ; des plus prolixes en narration. Le Messager de Dieu — paix et bénédiction sur lui — l’épousa à La Mecque quand elle avait six ans, un mois après [son mariage avec] Sawda, trois ans avant l’Hégire ; il la consomma en Shawwāl, au retour de Badr, l’an deux de l’Hégire, elle avait neuf ans ; il mourut quand elle en avait dix-huit ; elle lui survécut quarante ans ; morte en 57 ou 58 de l’Hégire.</li>
<li><strong>ʿUmar ibn al-Khaṭṭāb</strong> — Abū Ḥafṣ ʿUmar ibn al-Khaṭṭāb ibn Nufayl, Qurashite ʿAdawite — que Dieu soit satisfait de lui —, Commandeur des croyants, calife du Messager de Dieu — paix et bénédiction sur lui — ; on le prend pour parangon de justice, d’ascétisme, d’humilité et d’acharnement pour le vrai ; des volumes furent écrits sur sa vie. Martyrisé l’an 23 de l’Hégire.</li>
<li><strong>ʿUthmān ibn ʿAffān</strong> — ʿUthmān ibn ʿAffān ibn Abī l-ʿĀṣ ibn Umayya, Qurashite, Commandeur des croyants — que Dieu soit satisfait de lui. Il embrassa l’islam de bonne heure et émigra en Abyssinie avec son épouse Ruqayya, fille du Prophète — paix et bénédiction sur lui — ; on dit d’ʿUthmān “l’homme aux deux lumières” (<em>Dhū l-nūrayn</em>) parce qu’il épousa les deux filles du Messager de Dieu — paix et bénédiction sur lui. On lui prêta le califat après ʿUmar ; tué martyr en l’an trente-cinq, à quatre-vingt-dix ans.</li>
<li><strong>ʿAṭāʾ ibn Yasār</strong> — Hilālite, Abū Muḥammad, Médinois, son juge ; il transmit d’Ibn Masʿūd, de Zayd ibn Thābit, d’Ibn ʿUmar, d’Abū Hurayra, de ʿĀʾisha, de sa maîtresse Maymūna, d’Umm Sulaym et d’une multitude ; Abū Ḥanīfa, Zayd ibn Aslam, Abū Salama ibn ʿAbd al-Raḥmān et d’autres transmirent de lui ; Ibn Maʿīn, Abū Zurʿa, an-Nasāʾī et d’autres le validèrent. Mort en l’an cent trois — il fut dit : 94 — à quatre-vingt-quatre ans.</li>
<li><strong>Umm Sulaym</strong> — Umm Sulaym, fille de Milḥān ibn Khālid, Anṣārite, mère d’Anas ibn Mālik ; on dit son nom al-Ghumayṣāʾ ; elle a le compagnonnage et la narration ; son fils Anas, Ibn ʿAbbās et d’autres transmirent d’elle ; elle était des plus vertueuses et des plus sensées des femmes.</li>
<li><strong>Umm Qays, fille de Miḥṣan</strong> — Umm Qays bint Miḥṣan ibn Khirthān, Asadite, sœur d’ʿUkkāsha ; on dit son nom Āmina ; elle embrassa l’islam de bonne heure et émigra à Médine, et transmit du Prophète — paix et bénédiction sur lui — ; son affranchi ʿAdī ibn Dīnār, Wābiṣa ibn Maʿbad et d’autres transmirent d’elle.</li>
<li><strong>Yaḥyā ibn Saʿīd</strong> — Anṣārite, Abū Saʿīd, Médinois, son juge ; il transmit d’Anas, d’ʿAdī ibn Thābit et d’une multitude ; Mālik, les deux Sufyān et Abū Ḥanīfa transmirent de lui ; sûr, bien établi, des rétenthifs — Aḥmad dit : “Le plus établi des hommes.” Mort en l’an 144, ou un an après, ou un an avant.</li>
<li><strong>Al-Barāʾ ibn ʿĀzib</strong> — Abū ʿAmāra — ḍamma du <em>ʿayn</em> et allègement du <em>rāʾ</em> — on dit Abū ʿAmr, on dit Abū l-Ṭufayl : al-Barāʾ ibn ʿĀzib ibn al-Ḥārith, Anṣārite Awsite Ḥārithite Médinois ; trop jeune à Badr, sa première bataille fut Uḥud, et il assista au serment du Plaisir (<em>bayʿat al-riḍwān</em>).</li>
<li><strong>Abū Bakr al-Ṣiddīq</strong> — ʿAbd Allāh ibn Abī Quḥāfa — que Dieu soit satisfait de lui —, aux mérites et vertus nombreux ; le plus fort de la Communauté en foi après le Messager de Dieu — paix et bénédiction sur lui —, et son premier calife ; des volumes furent écrits sur sa vie — il est d’une renommée notoire. Mort l’an 13 de l’Hégire.</li>
<li><strong>ʿAlī ibn Abī Ṭālib</strong> — que Dieu soit satisfait de lui — cousin du Messager de Dieu — paix et bénédiction sur lui — et époux de sa fille Fāṭima — que Dieu soit satisfait d’elle — ; quatrième calife ; aux mérites nombreux et aux stations immenses. Mort l’an 40 de l’Hégire.</li>
<li><strong>Al-Bayāḍī</strong> — fatha du <em>bāʾ</em> et <em>ḍād</em> pointé ; son nom est Furwa — fatha du <em>fāʾ</em>, sukūn du <em>rāʾ</em> — fils de ʿAmr Wadqa, de la <em>Rawḍa</em> des Banū Bayāḍa, clan (<em>fiʿḍ</em>) des Khazraj, l’Anṣārite. Il assista à [la deuxième] ʿAqaba, à Badr et à ce qui suivit ; Wathīma mentionna, en le <em>Livre de l’apostasie</em>, que Furwa était de ceux qui menèrent, avec le Messager de Dieu — paix et bénédiction sur lui —, deux chevaux sur le chemin de Dieu ; et il faisait l’aumône, chaque jour, de mille <em>wasq</em> de son palmier.</li>
<li><strong>Abū Saʿīd, affranchi de ʿĀmir ibn Kurayz</strong> — Ibn ʿAbd al-Barr dit : c’est un Suivi Médinois, dont le nom ne se détermine pas ; dans le <em>Tahdhīb</em> d’al-Mizzī : il transmit d’Abū Hurayra et d’al-Ḥasan al-Baṣrī, sans troisième — bien que, parmi les transmetteurs de Mālik, certains dirent : d’après al-ʿAlāʾ ibn ʿAbd al-Raḥmān, Abū Saʿīd l’affranchi de ʿĀmir l’informa qu’il entendit Ubayy ibn Kaʿb dire : le Prophète — paix et bénédiction sur lui — l’appela — ce qu’al-Ḥākim fit sortir.</li>
<li><strong>ʿAbd Allāh ibn Buḥayna</strong> — ḍamma du <em>bāʾ</em>, fatha du <em>ḥāʾ</em> non pointé, sukūn du <em>yāʾ</em>, puis <em>nūn</em> : c’est le nom de sa mère — et de la mère de son père —, de sorte qu’il convient d’écrire <em>ibn</em> avec alif ; le nom de son père : Mālik ibn al-Qashab — kasra du <em>qāf</em>, sukūn de la pointée [chīn], puis <em>bāʾ</em> — Azdite, Abū Muḥammad, allié des Banū l-Muṭṭalib ; Compagnon ; mort après l’an 50 de l’Hégire.</li>
<li><strong>Ḥafṣa, épouse du Prophète</strong> — Ḥafṣa, fille d’ʿUmar ibn al-Khaṭṭāb, Mère des croyants ; née cinq ans avant la Mission ; le Messager de Dieu — paix et bénédiction sur lui — l’épousa l’an trois — il fut dit : l’an deux — de l’Hégire ; son frère ʿAbd Allāh, Ḥārith ibn Wahb, Umm Mubashshir l’Anṣārite et un groupe transmirent d’elle. Morte en l’an 41 de l’Hégire.</li>
<li><strong>Miḥjan</strong> — Miḥjan ibn Abī Miḥjan le Daylite ; il a le compagnonnage et la narration ; son fils Bishr transmit de lui — on dit : Busr.</li>
<li><strong>Anas ibn Mālik</strong> — Abū Ḥamza, Anas ibn Mālik, Anṣārite Khazrajite Najjārite, Médinois puis Baṣrite ; serviteur du Messager de Dieu — paix et bénédiction sur lui —, en résidence et en voyage, depuis son arrivée à Médine jusqu’à sa mort. Il dit : “Le Prophète vint à Médine quand j’avais dix ans, et il mourut quand j’en avais vingt.” Des plus prolixes en hadith ; le sûr est qu’il mourut en l’an quatre-vingt-treize, ayant dépassé la centaine.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13006":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13006 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13006 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
