#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R758 - commentaire de la lecon 21 hadith-5ep : pdf-21 (an-nahy 'an al-gadab -
l'interdiction de la colere, hadith d'Abu Hurayra « Ne te mets pas en colere »
[Sahih d'al-Bukhari], donne a celui qui demandait « Donne-moi un conseil » et
repete plusieurs fois ; clef du commentaire : l'interdiction ne porte pas sur
le sentiment mais sur son execution ; preuve d'appui : « La colere vient du
diable... » [Musnad de l'imam Ahmad] avec ablutions + recours a Dieu ; cinq
fruits de la maitrise de soi (Al 'Imran 134, le fort [Bukhari], appel au
premier rang [Tirmidi], porte du Paradis [Al 'Imran 133-134], coeur rempli
d'esperance [al-Mu'jam as-Sagir d'at-Tabarani]) ; exploitation : refuge contre
le diable [Bukhari, Sulayman ibn Surd] + s'asseoir/s'allonger [Sunan d'Abu
Dawud, Abu Darr]).
Quatorzieme vague du livre (SUIVANT de R757 ; hadith-5ep 20/29 au depart).
Redaction d'apres la lecture complete FR de la lecon (extraction non lossy,
/tmp/r758-lecon21-fr.txt, 2002 mots) - etat des sources cette vague :
* l'arabe de la lecon 21 n'est pas encore transpose (html vide, pdfOnly),
  comme pour les lecons 14-22 du livre ;
* le tirage reste indisponible (consigne en R757 : PDF locaux emportes par le
  recyclage du bac a sable, habous.gov.ma 404 sur /المدرج/) - verification
  par la traduction savante htmlFr de la lecon (produite depuis le tirage,
  validee au registre savant) ET recoupements :
  (a) echo textuel exact : le tamhid de la lecon 21 reprend mot pour mot
      l'ouverture du texte de la lecon 20 (« L'homme est sociable par
      nature » (ʾiǧtimāʿiyy bi-ṭabʿih)) et en tire la suite (nuisance ->
      colere) - visible dans les deux htmlFr ;
  (b) chapeau conforme a l'iʿdad de la lecon 20 (« Je mémorise le hadīth de
      la leçon à venir » + orientations religieuses « pour traiter la
      colère ») - le hadith d'Abu Hurayra « Ne te mets pas en colere » ;
  (c) matn source : la lecon cite [Sahih d'al-Bukhari] sur le matn ; les
      appuis sont sources lecon : [Musnad de l'imam Ahmad], [Sunan
      d'at-Tirmidi], [al-Mu'jam as-Sagir d'at-Tabarani], [Sahih d'al-Bukhari]
      (le fort ; Sulayman ibn Surd), [Sunan d'Abu Dawud] (Abu Darr) - matn
      non cite sans source ;
  (d) tarǧamat ar-rāwī : « sa biographie a été donnée précédemment » -
      notice complete donnee a la lecon 13 (Abu Hurayra ʿAbd ar-Rahman ibn
      Sahkr, neuvieme hadith des Quarante rapporte par lui), renvois 15, 17,
      19 (grecs verifiables : chapeaux « rapporté par Abū Hurayra ») ;
  (e) boucle lexical : « l'ordre de maîtriser la langue... et d'étouffer
      l'irritation » du tahlll fait echo a « la droiture de la langue relève
      des qualités de la foi » (lecon 19, verifie verbatim) et a la maitrise
      des membres (dabt al-ğawarih) des lecons 18-19 (R757) ;
  (f) references coraniques de la lecon (Al 'Imran 134 ; Al 'Imran 133-134)
      coïncident avec les versets qui portent ces sens dans le mushaf
      (134 : والكاظمين الغيظ والعافين عن الناس والله يحب المحسنين ; 133 :
      وسارعوا إلى مغفرة من ربكم وجنة عرضها السماوات والأرض) - AUCUN NB a
      consigner (regle R739/R742/R756/R757 : NB seulement si divergence
      reelle).
Translitteration du commentaire en convention corpus (ʾ U+02BE / ʿ U+02BF),
les lecons htmlFr portant ' U+2019 - precedent R753-R757 (ex. lecon :
« ʾawṣinī » ecrit ʾawṣinī au corpus, mawqif as-sar' -> mawqif aš-šarʿ).
Garde-fous de comm-r757 repris (typographie FR, arabe entre parentheses
seulement, vocab ar sans harakat, guillemets apparies) + fenetre de mots
1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_21 = {
    "auteur": "IA-1, tour R758",
    "resume": "Guide de lecture de la leçon 21 (l'interdiction de la colère — an-nahy ʿan al-ġaḍab (النهي عن الغضب)) : le commentaire du hadīth d'Abū Hurayra « Ne te mets pas en colère » (lā taġḍab (لا تغضب)) [Ṣaḥīḥ d'al-Buḫārī]. Un homme demande « Donne-moi un conseil » (ʾawṣinī (اوصني)) ; la réponse revient « plusieurs fois » : « Ne te mets pas en colère ». Trois objectifs : définir la colère et la position de la Loi, citer les fruits de la maîtrise de soi, s'approprier les finalités légales de l'interdiction. La clef du commentaire : l'interdiction ne porte pas sur le sentiment — « en tant que simple sentiment, elle relève de sa nature » — mais sur son exécution. Première partie : l'interdiction et son sens, la preuve « La colère vient du diable » et ses deux remèdes (ablutions, recours à Dieu). Seconde partie : cinq fruits de la maîtrise de soi. L'exploitation livre deux gestes : chercher refuge contre le diable et s'asseoir, s'allonger. La préparation ouvre la leçon 22 : l'excellence (iḥsān) en toute chose.",
    "explication": [
        "Après la consolidation de la leçon 20, un nouveau hadīth des Quarante de l'imam al-Nawawī est installé, avec le commentaire d'Ibn Daqīq al-ʾĪd : « l'interdiction de la colère » (an-nahy ʿan al-ġaḍab (النهي عن الغضب)). Trois objectifs ouvrent la marche : « Que je définisse la colère et la position de la Loi » (mawqif aš-šarʿ (مَوْقِفِ الشَّرْعِ)), « Que je cite les fruits » de la maîtrise de soi, « Que je m'approprie les finalités légales » (al-maqāṣid aš-šarʿiyya (الْمَقَاصِدَ الشَّرْعِيَّةَ)) de l'interdiction — définir, citer, s'approprier.",
        "Le tamhīd (تَمْهِيدٌ) reprend mot pour mot l'ouverture du texte de la consolidation : « L'homme est sociable par nature » (ʾiǧtimāʿiyy bi-ṭabʿih (اجْتِمَاعِيٌّ بِطَبْعِهِ)) — et en tire la suite logique : « il lui était donc indispensable de fréquenter autrui, et il en reçoit alors quelque nuisance, par une parole ou par un acte : il se met en colère et se laisse entraîner à rendre l'offense par l'offense et le mal par son pareil ». « Et en repoussant cela, la Loi a, à l'égard de la colère, une position qui en écarte les effets néfastes dans la psyché de l'individu, sa conduite et ses relations. » Deux questions ferment la mise en condition et dessinent le plan de l'analyse.",
        "Le texte (an-naṣṣ (النَّصُّ)) installe le matn : d'après Abū Hurayra — que Dieu soit satisfait de lui —, un homme dit au Prophète — prière et salut d'Allah sur lui — : « Donne-moi un conseil » (ʾawṣinī (أَوْصِنِي)). « Il répéta plusieurs fois » (faraddada mirāran (فَرَدَّدَ مِرَارًا)) ; il dit : « Ne te mets pas en colère » [Ṣaḥīḥ d'al-Buḫārī].",
        "La notice du transmetteur (tarǧamat ar-rāwī (تَرْجَمَةُ الرَّاوِي)) tient en une ligne : « sa biographie a été donnée précédemment » (sabaqat tarǧamatuh (سَبَقَتْ تَرْجَمَتُهُ)) — la cinquième fois qu'un hadīth des Quarante lui est attribué dans le fil du livre, après les leçons 13, 15, 17 et 19 ; sa notice complète (ʿAbd ar-Raḥmān ibn Ṣaḫr) a été donnée à la leçon 13.",
        "L'explication (aš-šarḥ (الشَّرْحُ)) déroule trois gloses, et la troisième est la clef. « Donne-moi un conseil » : « il m'a confié une injonction importante qui me profite » (bi-ʾamr muhimm yanfaʿunī (بِأَمْرٍ مُهِمٍّ يَنْفَعُنِي)). « Il répéta plusieurs fois » : « il répéta l'interdiction un certain nombre de fois ». « Ne te mets pas en colère » : « n'exécute pas ta colère » (lā tunaffiḏ ġaḍabak (لَا تُنَفِّذْ غَضَبَكَ)) contre « celui qui t'a mis en colère » (ḍidd man ʾaġḍabak (ضِدَّ مَنْ أَغْضَبَكَ)). La glose scinde le mot : le sentiment n'est pas visé, son exécution l'est.",
        "L'extraction des idées (istiḫlāṣ al-maḍāmīn (اِسْتِخْلَاصُ الْمَضَامِينِ)) pose deux gestes : « Je détermine le motif » de sa parole, puis « Je cherche à puiser dans le hadith » (ʾastawḥī (أَسْتَوْحِي)) « le motif du confinement de la réponse » (ḥaṣr al-ǧawāb (حَصْرِ الْجَوَابِ)) « en une seule parole » — pourquoi répondre cela ? L'analyse répond : l'exhortation est globale — la colère maîtrisée tient ensemble langue, membres et relations.",
        "L'analyse (at-taḥlīl (التَّحْلِيل)) ouvre sur le premier thème : « l'interdiction de la colère et son sens ». Le hadīth « relève de ses paroles lapidaires » (ǧawāmiʿ kalimih (جَوَامِعِ كَلِمِهِ)) ; la phrase concise « compte parmi ses formules lapidaires révélatrices de la sublimité de son éloquence, car c'est une exhortation globale et englobante. Elle comporte l'interdiction de laisser s'exécuter la colère » (tanfīḏ al-ġaḍab (تَنْفِيذِ الْغَضَبِ)) « et l'entraînement de l'âme à cela, ainsi que l'ordre de maîtriser la langue » (ḍabṭ al-lisān (بِضَبْطِ اللِّسَانِ)) « et d'étouffer l'irritation » (kazm al-ġayẓ (وَكَظْمِ الْغَيْظِ)) — « ce qui relève des œuvres des bienfaiteurs », loués par Dieu Très-Haut et Son Messager — prière et salut d'Allah sur lui. La droiture de la langue « relève des qualités de la foi » (leçon 19) et la maîtrise des membres (leçons 18-19) sont déjà en place.",
        "Vient le sens précis : « ne favorise pas en toi le mobile de la colère, et ne te laisse pas entraîner à ce qu'exige l'âme en colère. Ce que l'interdiction vise dans le hadith, c'est l'interdiction d'agir selon ce qu'exige la colère — rendre l'offense par l'offense et le mal par son pareil. » Puis la distinction qui protège de tout excès : la colère, « en tant que simple sentiment, elle relève de sa nature et de ses émotions, et rare est l'homme qui en est préservé » ; mais il peut « affiner ce penchant naturel » « en le maîtrisant sans le laisser libre d'agir » : il éteint « la braise de sa colère », « étouffe son irritation » et « résiste à son âme » — âme « susceptible de perdre son équilibre sous l'effet des suggestions du diable » (wasāwis aš-šayṭān (وَسَاوِسِ الشَّيْطَانِ)) « et des emportements de la nature humaine ». L'interdiction n'exige pas de ne pas ressentir — elle interdit de suivre le ressenti dans l'acte ; le mérite naît de la résistance, non de l'insensibilité.",
        "La preuve d'appui porte sur l'origine de la colère : le hadīth de ʿAṭiyya as-Saʿdī — que Dieu soit satisfait de lui — rapporte que le Messager d'Allah — prière et salut d'Allah sur lui — a dit : « La colère vient du diable » ; « or le diable a été créé de feu, et le feu ne s'éteint que par l'eau : lorsque l'un de vous se met en colère, qu'il fasse ses ablutions » (falyatawaḍḍaʾ) [Musnad de l'imam Aḥmad]. Et les effets : l'homme « sous l'effet de la colère, sort de l'équilibre de son état » (iʿtidāl ḥālih (اعْتِدَالِ حَالِهِ)) : « il profère le faux, commet le blâmable, conçoit la rancune et la haine, et [commet] d'autres interdits » ; « quiconque répond à la colère a en vérité répondu au diable sans s'en rendre compte ». D'où les deux remèdes : « les ablutions » (al-wuḍūʾ) et « le recours à Dieu » (al-istiʾāḏa bi-llāh) « comptent parmi les plus puissants moyens de repousser sa ruse ».",
        "Le second thème répond à la seconde question du tamhīd : « le mérite de la maîtrise de soi dans la colère » (ṯāniyan : faḍl mulk an-nafs ʿind al-ġaḍab). Premier — la louange de Dieu et Son amour : « qui étouffent leur irritation » (al-kāẓimīn al-ġayẓ (وَالْكَاظِمِينَ الْغَيْظَ)) « et pardonnent aux gens — Dieu aime les bienfaiteurs » [Āl ʾImrān : 134] ; et la louange du Messager : « Le fort n'est pas celui qui terrasse » (aṣ-ṣurʾa (بِالصُّرَعَةِ)) — « le fort, en vérité, est celui qui se maîtrise dans la colère » [Ṣaḥīḥ d'al-Buḫārī] : la force n'est pas dans le bras, elle est dans le cœur. Deuxième — la réussite dans l'au-delà : « Celui qui étouffe son irritation alors qu'il est capable de la laisser passer, Dieu — Puissant et Majestueux — l'appellera au premier rang des créatures au Jour de la résurrection, jusqu'à lui donner à choisir parmi les houris ce qu'il voudra » [Sunan d'at-Tirmiḏī] — étouffer, alors même qu'on est capable de laisser passer.",
        "Troisième — « l'une des portes de la réussite du Paradis », le même verset étendu : « Et concourez au pardon de votre Seigneur et à un Paradis large comme les cieux et la terre, préparé pour les pieux, qui dépensent dans l'aisance et dans l'adversité, qui étouffent leur irritation et pardonnent aux gens — Dieu aime les bienfaiteurs » [Āl ʾImrān : 133-134]. Quatrième — « l'emplissement du cœur de lumière et d'espérance au Jour de la résurrection » : « Et quiconque étouffe son irritation alors même qu'il pourrait la laisser s'accomplir, Dieu remplira son cœur d'espérance au Jour de la résurrection » [al-Muʾǧam aṣ-Ṣaġīr d'aṭ-Ṭabarānī]. Cinquième — « le repos du cœur et la préservation de la santé psychique, corporelle et des relations sociales » (al-ʿalāqāt al-ʾiǧtimāʿiyya (الْعَلَاقَاتِ الِاجْتِمَاعِيَّةِ)) : « répondre à la colère expose la santé psychique et corporelle aux dangers et aux effets néfastes, de même que repousser la colère loin de soi préserve les relations familiales et sociales » — aucun domaine n'est laissé dehors.",
        "Ce que le hadīth nous apprend (wa-mimmā yustafād min al-ḥadīṯ (وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ)) tient en trois enseignements : « Le recours aux hommes de bien pour demander conseil et exhortation » — demander est déjà une vertu ; « Conseiller à chacun ce qui convient à son état » — « il lui conseilla de repousser la colère loin de lui » ; « La concision dans le conseil et le souci qu'il soit global » : il « fit de son exhortation à ce Compagnon deux ou trois paroles ». La leçon 12, la religion c'est le conseil (naṣīḥa), avait installé le conseil ; ici, peu de mots et un sens immense.",
        "L'évaluation (at-taqwīm (التَّقْوِيم)) donne trois tâches : résumer le sens de « Ne te mets pas en colère » (ʾulaḫḣiṣu (أُلَخِّصُ)) ; trancher une situation — « L'un de deux amis vient à moi, en colère contre son ami, et menace d'exécuter sa colère » (yuhaddid bi-tanfīḏ ġaḍabih (يُهَدِّدُ بِتَنْفِيذِ غَضَبِهِ)) — « comment le convaincre d'étouffer son irritation et de ne pas se laisser emporter par sa colère ? » ; et « Je cite les effets de l'étouffement de l'irritation sur l'individu et la société ».",
        "L'exploitation (al-istiṯmār (الِاسْتِثْمَارُ)) livre deux hadīth d'application. Le premier, d'après Sulaymān ibn Ṣurd — que Dieu soit satisfait de lui — : « J'étais assis auprès du Prophète — prière et salut d'Allah sur lui — tandis que deux hommes s'injuriaient » (yastabbān (يَسْتَبَّانِ)) ; « l'un d'eux en eut le visage rouge et les veines gonflées » ; il connut « une parole qui, s'il la disait, ferait partir ce qu'il éprouve » : « Je cherche refuge auprès de Dieu contre le diable » [Ṣaḥīḥ d'al-Buḫārī]. Le second, d'après Abū Ḏarr al-Ġifārī : « Lorsque l'un de vous se met en colère alors qu'il est debout, qu'il s'asseye ; si la colère le quitte — sinon, qu'il s'allonge » (falyaḍṭaǧiʾ (فَلْيَضْطَجِعْ)) [Sunan d'Abū Dāwūd]. Puis extraire « les moyens les plus importants qui écartent la colère de l'homme » : refuge contre le diable, baisse de posture — des gestes qu'un enfant peut exécuter.",
        "La préparation de la leçon suivante (al-ʾiʿdād al-qabliyy (الْإِعْدَادُ الْقَبْلِيُّ)) enjoint de mémoriser le hadīth de la leçon à venir (al-ʾātī (الْآتِيَ)), puis : « Je définis la bienfaisance » (al-ʾiḥsān (الْإِحْسَانَ)) et « Je cite des exemples de bienfaisance » — en toute chose (fī kulli šayʾ (فِي كُلِّ شَيْءٍ)) : la leçon 22, « l'excellence (iḥsān) en toute chose ». Le fil se tend : le caractère se dresse par degrés, et le premier degré est la maîtrise de la colère. La leçon l'a promis dès le tamhīd : écarter « les effets néfastes dans la psyché de l'individu, sa conduite et ses relations » — lʾiḥsān commence là.",
    ],
    "points": [
        "La place : leçon 21, nouveau hadīth des Quarante après la consolidation — « Ne te mets pas en colère » [Ṣaḥīḥ d'al-Buḫārī], répété à celui qui demandait conseil ; cinquième hadīth du livre porté par Abū Hurayra (leçons 13, 15, 17, 19).",
        "Les objectifs : définir la colère et la position de la Loi (mawqif aš-šarʿ) ; citer les fruits (ṯamarāt) de la maîtrise de soi ; s'approprier les finalités légales (al-maqāṣid aš-šarʿiyya) de l'interdiction.",
        "L'écho : le tamhīd reprend mot pour mot l'ouverture de la consolidation — « L'homme est sociable par nature » ; la Loi écarte « les effets néfastes dans la psyché de l'individu, sa conduite et ses relations ».",
        "La clef : l'interdiction ne porte pas sur le sentiment — « en tant que simple sentiment, elle relève de sa nature » — mais sur son exécution : « n'exécute pas ta colère » contre celui qui a mis en colère ; ne pas « rendre l'offense par l'offense et le mal par son pareil ».",
        "L'origine : « La colère vient du diable » ; « or le diable a été créé de feu, et le feu ne s'éteint que par l'eau » — ablutions et « le recours à Dieu » (al-istiʾāḏa bi-llāh) [Musnad de l'imam Aḥmad] ; « quiconque répond à la colère a en vérité répondu au diable ».",
        "Les cinq fruits : louange et amour de Dieu [Āl ʾImrān : 134] ; « le fort, en vérité, est celui qui se maîtrise dans la colère » [Ṣaḥīḥ d'al-Buḫārī] ; l'appel au premier rang des créatures [Sunan d'at-Tirmiḏī] ; « l'une des portes de la réussite du Paradis » [Āl ʾImrān : 133-134] ; le cœur rempli d'espérance [al-Muʾǧam aṣ-Ṣaġīr d'aṭ-Ṭabarānī] — plus la santé psychique, corporelle et sociale.",
        "Les remèdes d'application : « Je cherche refuge auprès de Dieu contre le diable » (Sulaymān ibn Ṣurd [Ṣaḥīḥ d'al-Buḫārī]) ; « qu'il s'asseye » … « qu'il s'allonge » (Abū Ḏarr [Sunan d'Abū Dāwūd]) — les gestes qui écartent la colère.",
        "La préparation : « Je définis la bienfaisance » (al-ʾiḥsān) et « Je cite des exemples de bienfaisance » en toute chose — la leçon 22, « l'excellence (iḥsān) en toute chose ».",
    ],
    "vocabulaire": [
        {"ar": "النهي عن الغضب", "translit": "an-nahy ʿan al-ġaḍab", "fr": "l'interdiction de la colère — le titre de la leçon : la position de la Loi à l'égard de la colère et les finalités légales (al-maqāṣid aš-šarʿiyya) de cette interdiction."},
        {"ar": "لا تغضب", "translit": "lā taġḍab", "fr": "ne te mets pas en colère — la parole du Prophète — prière et salut d'Allah sur lui — répétée à celui qui demandait conseil ; glose : « n'exécute pas ta colère » contre celui qui t'a mis en colère."},
        {"ar": "اوصني", "translit": "ʾawṣinī", "fr": "donne-moi un conseil — la demande du Compagnon : « il m'a confié une injonction importante qui me profite »."},
        {"ar": "جوامع كلمه", "translit": "ǧawāmiʿ kalimih", "fr": "ses paroles lapidaires — peu de mots portant un sens immense : « une exhortation globale et englobante », clef du rang du hadīth."},
        {"ar": "ضبط اللسان", "translit": "ḍabṭ al-lisān", "fr": "la maîtrise de la langue — l'ordre contenu dans l'interdiction ; la droiture de la langue « relève des qualités de la foi » (leçon 19)."},
        {"ar": "كظم الغيظ", "translit": "kazm al-ġayẓ", "fr": "étouffer l'irritation — l'autre moitié de l'ordre : « ce qui relève des œuvres des bienfaiteurs », louées par Dieu et Son Messager."},
        {"ar": "الكاظمين الغيظ", "translit": "al-kāẓimīn al-ġayẓ", "fr": "ceux qui étouffent leur irritation — les loués du verset : « et pardonnent aux gens — Dieu aime les bienfaiteurs » [Āl ʾImrān : 134]."},
        {"ar": "تمالك النفس", "translit": "tamāluk an-nafs", "fr": "la maîtrise de soi — la question du tamhīd : quel est l'effet de la maîtrise de soi dans la colère ? ; son mérite (faḍl mulk an-nafs ʿind al-ġaḍab) déroule les cinq fruits."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}
ENTREES = [('pdf-21', E_21)]


def norme_fr(s):
    s = s.replace('\'', '\u2019')
    s = re.sub(r'\s+([;:!?»])', '\u202f\\1', s)
    s = s.replace('« ', '«\u202f')
    return s


def norme_entree(e):
    e['resume'] = norme_fr(e['resume'])
    e['avertissement'] = norme_fr(e['avertissement'])
    e['explication'] = [norme_fr(x) for x in e['explication']]
    e['points'] = [norme_fr(x) for x in e['points']]
    for v in e.get('vocabulaire', []):
        v['fr'] = norme_fr(v['fr'])
    return e


data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
bloque = [d for d, _ in ENTREES if d in com]
if bloque:
    print(f'!! déjà présent : {bloque} — replacement (passe de correction)')
    for d in bloque:
        del com[d]
for docid, e in ENTREES:
    com[docid] = norme_entree(e)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys(), key=lambda x: int(x.split('-')[1])))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-21',):
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    fenetre = 'PASS' if 1700 <= mots <= 2400 else 'HORS FENETRE'
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])} — fenêtre 1700-2400 : {fenetre}')
    if fenetre != 'PASS':
        mauvais += 1
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] \
             + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t)
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
        if t.count('«') != t.count('»'):
            mauvais += 1
            print('   guillemets non appariés :', t[:60])
    for v in e['vocabulaire']:
        if not motif_ar.search(v['ar'].replace(' ', '')):
            mauvais += 1
            print('   vocab ar non arabe :', v['ar'])
        if re.search(r'[\u064B-\u0652\u0670]', v['ar']):
            mauvais += 1
            print('   vocab ar avec harakat :', v['ar'])
        if motif_ar.search(v['fr']):
            mauvais += 1
            print('   vocab fr contient de l arabe :', v['fr'][:60])
        if not re.search(r'[\u02BE\u02BF]', v['translit']):
            print('   note : translit sans ʾ/ʿ :', v['translit'])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
if mauvais:
    sys.exit(1)
