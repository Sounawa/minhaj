#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16795 (tawhid-1es, leçon imprimée 22 —
l'interdiction d'excommunier qui que ce soit des gens de la Qibla pour un
péché ; les réalités invisibles à croire).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations :
- 3 citations vides (perte OCR systématique CMS) :
  Ghāfir 46 CONFORME (l'exposition au Feu matin et soir — ancre de la doctrine
  de la vue de la demeure) ; Ibrāhīm 27 CONFORME (la parole ferme — citée mot
  à mot par le hadith d'al-Barāʾ qui suit) ; la citation vide de l'iʿdād →
  Sajda 11 (cible univoque : la question porte sur l'ange qui saisit les âmes,
  et la leçon suivante 16798 cite ce verset sous la référence imprimée
  « Sūrat al-Sajda, verset 11 »).
- 6 hadiths VÉRIFIÉS sunnah.com (curl + UA navigateur) :
  ʿĀʾisha « اللهم إني أعوذ بك من فتنة النار » = Bukhārī 6377, Kitāb
  al-Daʿawāt, bāb التعوذ من فتنة الفقر EXACT — CONFORME MOT À MOT (la suite
  du hadith, lavage du cœur, tronquée dans l'imprimé) ;
  Ibn ʿUmar « إن أحدكم إذا مات عرض عليه مقعده بالغداة والعشي » = Bukhārī
  1379, Kitāb al-Janāʾiz, bāb الميت يعرض عليه بالغداة والعشي EXACT — CONFORME
  MOT À MOT (les DEUX occurrences, courte et complète) ;
  Abū Saʿīd « إذا وضعت الجنازة فاحتملها الرجال على أعناقهم » = Bukhārī 1316,
  bāb قول الميت وهو على الجنازة قدموني EXACT — CONFORME MOT À MOT (1314 =
  parallèle à variantes) ;
  al-Barāʾ « المسلم إذا سئل في القبر » = Bukhārī 4699, Kitāb al-Tafsīr, bāb
  يثبت الله الذين آمنوا بالقول الثابت EXACT — l'ouverture « ثم شهد » suit la
  leçon de 1369 (Janāʾiz) : pattern bāb/localisation documenté (5e occurrence) ;
  Anas « إن العبد إذا وضع في قبره وتولى عنه أصحابه » = Bukhārī 1374, bāb ما
  جاء في عذاب القبر EXACT — « في هذا الرجل » suit la leçon de 1338 (variantes
  croisées notées) ;
  Ibn ʿAbbās « إنهما ليعذبان وما يعذبان في كبير » = Bukhārī 1361, bāb الجريد
  على القبر EXACT — « لم فعلت هذا » suit 218 (Wudūʾ) et « لا يستنزه » est la
  variante canonique (cf. Muslim 297) — l'ordre des deux fautes suit l'imprimé.
- Doctrines rendues au plus près : le takfīr et ses trois limites (négation
  d'une donnée notoire / rendre licite / attenter au sacré) ; Khārijites et
  Muʿtazilites (la station intermédiaire, le beau et le laid rationnels) ;
  les deux sens de « gens de la Qibla » ; la vie réelle des martyrs
  (l'étymologie shahīd/shāhid) ; la mort comme passage ; la vue de la demeure
  matin et soir ; la subsistance percevante des âmes (dirāka) ; Munkar et
  Nakīr (la création prodigieuse, la note philologique du fatha) ; le tawātur
  de l'épreuve de la tombe ; la palme fraîche (l'allègement conditionné).
- OCR/artefacts : dl/dt/dd de la date (lundi 20 décembre 2021) + <p> vides +
  écho du titre en queue + divs vides — artefacts non rendus ; le <span></span>
  vide après le matn — non rendu.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : l’interdiction d’excommunier qui que ce soit des gens de la Qibla pour un péché ; les réalités invisibles à croire</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingt-deuxième leçon (22).</p>
<ul>
<li>Connaître le sort des bienheureux et celui des infortunés.</li>
<li>Saisir que le croyant n’est pas excommunié pour un péché.</li>
<li>Avoir présent à l’esprit l’épreuve de la tombe et l’interrogation des deux anges, et s’y préparer par l’œuvre salutaire.</li>
</ul>
<h2>Préambule</h2>
<p>D’après ʿĀʾisha — que Dieu l’agrée —, elle dit : le Prophète ﷺ avait coutume de dire : « Ô Dieu, je cherche protection auprès de Toi contre l’épreuve du Feu et le châtiment du Feu, contre l’épreuve de la tombe et le châtiment de la tombe, contre le mal de l’épreuve de la richesse et le mal de l’épreuve de la pauvreté ; ô Dieu, je cherche protection auprès de Toi contre le mal de l’épreuve de l’Antéchrist (<em>al-Dajjāl</em>). » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Daʿawāt, bāb de la demande de protection contre l’épreuve de la pauvreté — bāb imprimé EXACT (hadith 6377, de ʿĀʾisha) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com ; la suite du hadith — le lavage du cœur par l’eau de la neige et de la grêle — est tronquée dans l’imprimé.]</p>
<p>Je médite le hadith et m’interroge : quel est le statut de l’excommunication d’un des gens de la Qibla ? Qu’entend-on par épreuve de la tombe ? Quel est le sort des âmes des bienheureux ? Et quel est le sort des âmes des infortunés ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que nul ne déclare mécréant, pour un péché, qui que ce soit des gens de la Qibla ; et que les martyrs sont vivants auprès de leur Seigneur, dotés de subsistance ; et que les âmes des gens de la félicité subsistent, délectées, jusqu’au jour où ils seront ressuscités ; et que les âmes des gens de l’infortune sont châtiées jusqu’au Jour du Jugement ; et que les croyants sont éprouvés en leurs tombes et interrogés. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>nāʿima</em> (délectées) : vivant dans l’aisance et l’agrément.</li>
<li><em>yubʿathūn</em> (ils seront ressuscités) : envoyés et remis debout.</li>
<li><em>yuftatanūn</em> (éprouvés) : soumis à l’épreuve et à l’examen.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> l’interdiction d’excommunier le croyant pour un péché.</li>
<li>Je dégage du <em>matn</em> le sort des bienheureux et celui des infortunés.</li>
<li>J’extrais du <em>matn</em> l’épreuve de la tombe.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<h3>Premièrement : l’interdiction d’excommunier qui que ce soit des gens de la Qibla</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que nul ne déclare mécréant, pour un péché, qui que ce soit des gens de la Qibla. » Ce qu’il faut tenir pour vrai : nul musulman n’est déclaré mécréant pour un péché, qu’il soit mineur ou majeur — sauf s’il renie une donnée notoire de la religion par nécessité (<em>maʿlūm min al-dīn bi-l-ḍarūra</em>), telle l’obligation de la prière, du jeûne, de la zakāt et du pèlerinage ; ou rend licite un péché, telle la fornication ; ou porte la main sur ce qui est sacré, telle la divine Essence ou les prophètes. Telle est l’école de l’ensemble des gens de la Sunna, prédécesseurs et successeurs — à la différence des Khārijites, qui tiennent que tout péché est faute majeure (<em>kabīra</em>), que toute faute majeure annule l’œuvre, et que son auteur est mécréant ; et à la différence des Muʿtazilites, qui tiennent que toute faute majeure annule l’œuvre, et que son auteur occupe une station entre les deux stations (<em>manzila bayn al-manzilatayn</em>) : on ne le nomme ni croyant ni mécréant, mais on dit de lui : pervers (<em>fāsiq</em>) — le tout fondé sur leur doctrine du beau et du laid rationnels, comme l’a dit Abū l-Ḥasan — que Dieu lui fasse miséricorde.</p>
<p>Quant à la parole de l’auteur « des gens de la Qibla » : gens de la Qibla (<em>ahl al-qibla</em>) est une appellation des gens de la prière ; et il fut dit : c’est le nom de tout croyant en Dieu Très-Haut et en Son Messager ﷺ, qu’il prie ou non.</p>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et que les martyrs sont vivants auprès de leur Seigneur, dotés de subsistance ». Ce qu’il faut tenir pour vrai : les martyrs sont vivants auprès de leur Seigneur — c’est-à-dire en le jardin de leur Seigneur —, dotés de subsistance comme le sont les vivants : ils mangent, boivent et goûtent une délectation corporelle. Ils furent nommés « martyrs » (<em>shuhadāʾ</em>) parce que leurs âmes furent conduites à la Demeure de la Paix (<em>dār al-salām</em>), ou parce qu’ils ont contemplé le Paradis : <em>shahīd</em>, alors, au sens de <em>shāhid</em> — le témoin, présent au Paradis. Et leur vie est réelle (<em>ḥaqīqiyya</em>), comme le manifeste le noble verset — telle est la position du Jumhūr.</p>
<h3>Deuxièmement : le sort des âmes des bienheureux et le sort des âmes des infortunés</h3>
<h4>1. Le sort des âmes des bienheureux</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et que les âmes des gens de la félicité subsistent, délectées, jusqu’au jour où ils seront ressuscités ». Ce qu’il faut tenir pour vrai : les âmes des gens de la félicité — les croyants, le vertueux comme le dévoyé d’entre eux — subsistent, sans s’anéantir : la mort n’est pas anéantissement pur, elle est passage d’un état à un état. La parole de l’auteur « délectées » (<em>nāʿima</em>) : comblées par la vue de leur demeure au Paradis, au matin et au soir — selon le hadith de ʿAbd Allāh b. ʿUmar — que Dieu les agrée tous deux — : le Messager de Dieu ﷺ a dit : « L’un d’entre vous, lorsqu’il meurt, il lui est présenté sa demeure au matin et au soir… » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Janāʾiz, bāb : le défunt voit sa demeure au matin et au soir — bāb imprimé EXACT (hadith 1379, d’Ibn ʿUmar) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.]</p>
<h4>2. Le sort des âmes des infortunés</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et que les âmes des gens de l’infortune sont châtiées jusqu’au Jour du Jugement » — c’est-à-dire : les âmes des mécréants — eux sont les infortunés — sont châtiées par la vue de leur demeure au Feu, et par les autres espèces de châtiment, jusqu’au Jour de la Résurrection. La parole de l’auteur embrasse deux points :</p>
<ul>
<li>Premier point : parmi les âmes, il en est qui sont comblées après la mort, et il en est qui sont châtiées ; leur délectation et leur châtiment tiennent à la vue de leur demeure, au Paradis ou au Feu — selon la parole de Dieu Très-Haut :</li>
</ul>
<p>« le Feu, auquel ils sont exposés matin et soir. Et le jour où l’Heure se lèvera (il sera dit) : „Faites entrer les gens de Pharaon au plus dur du châtiment“. » (Ghāfir, 46)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset de l’exposition au Feu matin et soir, ancre de la doctrine de la vue de la demeure.] — et selon le hadith de ʿAbd Allāh b. ʿUmar — que Dieu les agrée tous deux — : le Messager de Dieu ﷺ a dit : « L’un d’entre vous, lorsqu’il meurt, il lui est présenté sa demeure au matin et au soir : s’il était des gens du Paradis, [il lui est dit :] des gens du Paradis ; et s’il était des gens du Feu — il est dit : voici ta demeure, jusqu’à ce que Dieu te ressuscite au Jour de la Résurrection. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Janāʾiz, bāb : le défunt voit sa demeure au matin et au soir — bāb imprimé EXACT (hadith 1379, version complète) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.]</p>
<ul>
<li>Second point : les âmes subsistent après la mort — preuve en sont les hadiths qui attestent leur subsistance, leur activité, leur délectation et leur châtiment, leur ouïe et leur parole. Les gens de la Sunna et de la Communauté sont d’accord qu’elles sont vivantes, subsistantes, percevantes (<em>dirāka</em>), au point d’éprouver leurs plaisirs et leurs douleurs — d’après Abū Saʿīd al-Khudrī — que Dieu l’agrée — : le Messager de Dieu ﷺ a dit : « Lorsque la civière est posée et que les hommes la portent sur leurs nuques : si elle était vertueuse, elle dit : „Portez-moi en avant“ ; et si elle n’était pas vertueuse, elle dit à sa famille : „Malheur à elle ! Où l’emportez-vous ?“ Toute chose entend sa voix, hormis l’homme — et si l’homme l’entendait, il serait foudroyé. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Janāʾiz, bāb : la parole du mort porté sur la civière — « portez-moi en avant » — bāb imprimé EXACT (hadith 1316, d’Abū Saʿīd) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com ; la narration 1314 en est la parallèle, aux variantes de leçon près.]</li>
</ul>
<h3>Troisièmement : l’épreuve de la tombe et ses preuves</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et que les croyants sont éprouvés en leurs tombes et interrogés ». Ce qu’il faut tenir pour vrai : les croyants sont éprouvés et testés en leurs tombes par l’interrogation des deux anges : Munkar — avec fatha du kāf — et Nakīr. Les deux anges furent nommés Munkar et Nakīr parce que leur création ne ressemble à la création d’aucune des créatures : ils ont plutôt une création prodigieuse (<em>badiʿa</em>), et il n’y a en leur création nulle familiarité apaisante pour les regards.</p>
<p>L’auteur a appuyé l’épreuve de la tombe sur Sa parole — glorifié et exalté soit-Il :</p>
<p>« Dieu affermit ceux qui croient par la parole ferme, en la vie de ce monde et en l’au-delà ; et Dieu égare les injustes ; et Dieu fait ce qu’Il veut. » (Ibrāhīm, 27)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset de la parole ferme, que le hadith d’al-Barāʾ qui suit cite mot à mot.] Et les récits sur l’épreuve de la tombe ont atteint le degré du tawātur (transmission continue) ; ainsi, dans le Ṣaḥīḥ d’al-Bukhārī, d’après al-Barāʾ b. ʿĀzib — que Dieu l’agrée — : le Messager de Dieu ﷺ a dit : « Le musulman, lorsqu’il est interrogé en sa tombe puis témoigne qu’il n’est de dieu que Dieu et que Muḥammad est le Messager de Dieu — c’est la parole du Très-Haut : „Dieu affermit ceux qui croient par la parole ferme, en la vie de ce monde et en l’au-delà“. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Tafsīr, bāb : « Dieu affermit ceux qui croient par la parole ferme » — bāb imprimé EXACT (hadith 4699, d’al-Barāʾ) : texte VÉRIFIÉ sur sunnah.com ; l’ouverture « il témoigne ensuite » (<em>thumma shahida</em>) suit la leçon de la narration parallèle 1369 (Kitāb al-Janāʾiz) — pattern de bāb/localisation documenté.]</p>
<p>Et d’après Anas — que Dieu l’agrée — : le Messager de Dieu ﷺ a dit : « Le serviteur, lorsqu’il est déposé en sa tombe et que ses compagnons s’en détournent — il entend encore le claquement de leurs sandales —, deux anges viennent à lui, le mettent assis et lui disent : „Que disais-tu de cet homme ?…“ » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Janāʾiz, bāb : ce qui est rapporté du châtiment de la tombe — bāb imprimé EXACT (hadith 1374, d’Anas) : texte VÉRIFIÉ sur sunnah.com ; « de cet homme » suit la leçon de la narration parallèle 1338 (bāb : le mort entend le clapotement des sandales).]</p>
<h2>Les fruits de la leçon</h2>
<p>L’éducation du musulman à ne pas tomber dans l’excommunication d’aucun des musulmans, en marchant sur la voie des vertueux prédécesseurs en cela ; et à se munir de la crainte révérencielle de Dieu Très-Haut et de Son obéissance, en préparation de l’épreuve de la tombe et des terreurs qui suivent — dont n’échappe que celui qui vient à Dieu avec un cœur sain.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’explicite ce qu’on entend par gens de la Qibla.</li>
<li>Quel est le sort des bienheureux ? Et celui des infortunés ?</li>
<li>Par quoi le croyant est-il éprouvé en sa tombe ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Parmi ce qu’il faut croire par ouï-dire : le mort est châtié ou comblé en sa tombe s’il est enseveli — et même le non-enseveli est châtié ou comblé après sa mort. D’après Ibn ʿAbbās — que Dieu les agrée tous deux — : le Messager de Dieu ﷺ passa près de deux tombes et dit : « Ils sont, tous deux, châtiés — et ils ne sont point châtiés pour une faute grave : quant à l’un, il allait semant la calomnie (<em>nabīma</em>) ; quant à l’autre, il ne se préservait pas de l’urine. » Puis il prit une palme fraîche, la fendit en deux, et en posa une sur chaque tombe. On dit : « Ô Messager de Dieu, pourquoi as-tu fait cela ? » Il dit : « Peut-être leur sera-t-il allégé, tant qu’elles ne seront point desséchées. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Janāʾiz, bāb : la palme fraîche sur la tombe — bāb imprimé EXACT (hadith 1361, d’Ibn ʿAbbās) : texte VÉRIFIÉ sur sunnah.com ; « pourquoi as-tu fait cela » suit la leçon de 218 (Kitāb al-Wuḍūʾ), et « il ne se préservait pas » (<em>lā yastanzih</em>) est la variante canonique (cf. Muslim 297) ; l’ordre des deux fautes suit l’imprimé.]</p>
<h3>Je médite bien le hadith et en dégage ce qui suit :</h3>
<ul>
<li>De quoi vient le châtiment de la tombe ?</li>
<li>Quelles sont les œuvres qui allègent le châtiment de la tombe ?</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qui suit :</p>
<ul>
<li>Qui prend en charge la saisie des âmes ?</li>
<li>Je recherche l’exégèse de la parole du Très-Haut :</li>
</ul>
<p>« Dis : „L’Ange de la mort, qui est chargé de vous, vous saisira ; puis vous serez ramenés vers votre Seigneur“. » (al-Sajda, 11)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; cible univoque : la question porte sur l’ange qui saisit les âmes, et la leçon suivante — la foi aux anges — cite ce verset sous la même référence « Sūrat al-Sajda, verset 11 ».]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16795":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16795 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16795 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
