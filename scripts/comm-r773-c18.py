#!/usr/bin/env python3
"""R773 — ajoute le commentaire pédagogique de la leçon 18 de hadith-tanawi-1
(13117 جامع عدة الطلاق — le recueil de la retraite du divorce, « Le recueil
de la retraite du divorce (jāmiʿ ʿiddat aṭ-ṭalāq) » dans la traduction du
manuel, la dix-huitième du livre, étiquetée « leçon 24 » par l'imprimé
(الدرس 24) — le SUIVANT de R772, 13115, annoncé dès R771/R772)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r772-c17.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~25 000 caractères débalisés ; couche
arabe lue en entier pour le titre plein جامع عدة الطلاق من كتاب الحديث من
موطأ الإمام مالك بشرح الزرقاني et l'étiquette de l'imprimé « (الدرس 24) »).
Règle 2 de LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ (1843,
1845, 1846, 1847, 1848, et le n° 1831 cité en contre-doctrine), les
attributions (ʿUmar ibn al-Khaṭṭāb, Saʿīd ibn al-Musayyab, Yaḥyā ibn Saʿīd,
Yazīd ibn ʿAbdallāh ibn Qusayṭ al-Laythī, Ibn Shihāb az-Zuhrī, Mālik, Abū
Ḥanīfa, ath-Thawrī, al-Layth, ash-Shāfiʿī, al-Bājī) et les références
(aṭ-Ṭalāq 4 ; al-Baqara 228 et 231 ; la Mudawwana absente ici ; al-Muntaqā)
sont cités tels qu'ils figurent dans la leçon.

Garde-fous (convention des vagues R765-R772) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr débalisé de la leçon (convention :
  frontières de blocs -> espace, tags inline -> '') ;
- recoupements : ancres vérifiées dans les leçons voisines (13114 — la
  leçon du compte des réglées, les qurūʾ et les cinq maîtres de Médine ;
  13115 — la leçon précédente immédiate, la mubtūta et la doctrine de la
  reprise ; 12992 — la leçon du muḥallil, où la bāʾin fut établie ;
  12966 — la leçon du ẓihār, première pièce du corpus califal ;
  13121 — la leçon suivante du registre, objet de la préparation).

NB consignés sans correction (relevés à la lecture) :
- le titreAr du CMS est tronqué (« جامع عدة الطلاق من ») ; la couche arabe
  porte le titre plein ;
- le titleFr du CMS porte une double parenthèse avec harakat
  « (jāmiʿ ʿiddat aṭ-ṭalāq (الطَّلَاقُ)) » — artefact de composition ;
- translit « tulafqaq » pour la jonction (talfīq attendu) et « ṣ-sughrā »
  (as-sughrā attendu) — recopiés tels quels ;
- coquille du contrôle « la sagesme » pour « la sagesse » ;
- aucune date imprimée en tête de la couche arabe (contrairement aux
  leçons 16 et 17) ;
- la leçon dit « la vingt-quatrième leçon » alors qu'elle est la
  dix-huitième du livre — écart d'étiquetage du fil (comme les précédentes).
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13117'

E_13117 = {
    "auteur": "IA-1, tour R773",
    "resume": (
        "Guide de lecture de la leçon 18 (جامع عدة الطلاق من كتاب الحديث من موطأ الإمام مالك بشرح الزرقاني — le "
        "recueil de la retraite du divorce du livre de hadith du Muwaṭṭaʾ de l'imam Mālik avec le commentaire de "
        "l'imam al-Zarqānī ; la traduction du manuel porte « Le recueil de la retraite du divorce »), la "
        "dix-huitième du livre, étiquetée leçon 24 par l'imprimé (الدرس 24) : trois textes du Muwaṭṭaʾ portent la "
        "matière — le n° 1843 est le procès-verbal califal : la parole dʿUmar ibn al-Khaṭṭāb — qu'Allah l'agrée — "
        "transmise par Saʿīd ibn al-Musayyab, prince des Successeurs médinois, par la voie de Yaḥyā ibn Saʿīd — le "
        "juge de Médine — et de Yazīd ibn ʿAbdallāh ibn Qusayṭ al-Laythī : « Toute femme répudiée qui a menstrué "
        "une ou deux fois, puis ses menstrues se sont levées, attendra neuf mois ; si une grossesse lui apparaît, "
        "tel est [son terme] ; sinon, après les neuf mois, elle comptera trois mois, puis elle deviendra licite. » "
        "— l'échelle des neuf mois de l'attente, la grossesse qui tranche, sinon les trois mois ; le n° 1845 est la "
        "sentence de la mustaḍāḍa, par Ibn Shihāb az-Zuhrī de Saʿīd ibn al-Musayyab : « La retraite de la "
        "mustaḍāḍa est une année. » ; le n° 1846 est le mécanisme complet, le dire compilé de Mālik lui-même : la "
        "double échelle des neuf mois et des trois mois, la menstruation qui réceptionne le compte, la reprise "
        "ouverte « avant qu'elle ne devienne licite — sauf s'il avait coupé (battaʾa) son divorce ». Le préambule "
        "fonde le tout : la retraite est légiférée « pour la connaissance de la pureté du sein (barāʾat ar-raḥim) », "
        "« en sauvegarde des lignages de tout mélange », et « pour la magnification du rang du mariage et la "
        "manifestation de sa noblesse » ; elle est « un droit d'Allah — que Sa gloire soit exaltée — qu'Il a rendu "
        "obligatoire, un bien pour l'épouse, un droit du mari et de l'enfant : c'est pourquoi nul n'a à la "
        "renoncer » ; trois espèces : « la retraite des qurūʾ — les cycles —, la retraite des mois, et la retraite "
        "de la mise au monde (waḍʾ al-ḥaml) ». La leçon précédente a réglé le compte des réglées ; celle-ci "
        "« rassemble ce qui reste » — les corps que les cycles ne règlent plus : « la femme dont les menstrues se "
        "sont levées (ar-rafʿ), la mustaḍāḍa dont le sang ne s'interrompt point, l'âgée qui a désespéré, la jeune "
        "qui n'a point encore vu le sang » — et la répudiée reprise puis séparée une seconde fois. Première "
        "partie — par quoi compte celle qui ne menstrue point. L'accord : la désespérée (al-yāʾisa) par l'âge et "
        "la jeune par la jeunesse comptent trois mois, à la lettre d'aṭ-Ṭalāq 4 — « le verset porte les deux "
        "extrêmes du cycle féminin » ; entre les deux s'ouvre la divergence : la shābba dont les menstrues se "
        "lèvent, et la mustaḍāḍa. La doctrine de Mālik pour la levée des menstrues : neuf mois — « les neuf mois "
        "sont la durée ordinaire de la grossesse » — ; grossesse apparue, la retraite est la mise au monde ; "
        "sinon trois mois — « C’est l’implicite de la parole d’ʿUmar ibn al-Khaṭṭāb — qu’Allah l’agrée » ; la levée "
        "des menstrues « ne dénote point la grossesse » — beaucoup de causes la produisent sans elle ; après les "
        "neuf mois, « elle a alors le statut de celle qui a désespéré des menstrues », à ceci près que « la marque "
        "du désespoir est apparente par l'âge et ses signes » quand elle ne l'est point ici — d'où l'istibrāʾ, "
        "« la purification de la certitude », et l'istiqṣāʾ, « l'examen exhaustif ». Point d'implicite contraire "
        "(mafhūm mukhālaf) écarté — « point de différence entre la grossesse et les menstrues » : si elle "
        "menstrue, « le statut des mois s'annule et elle reprend le compte par les qurūʾ ». Le mécanisme du "
        "n° 1846 déplie le jeu complet : « la double échelle des mois et des menstrues, l'annulation et la "
        "reprise, la jonction de la menstruation et la non-jonction de l'attente : la doctrine du recueil se tient "
        "tout entière dans ce mécanisme » — la menstruation se joint (talfīq), l'attente ne se joint point : "
        "« les menstrues ne sont point un doute : elles le nient — c'est pourquoi une part d'elles se joint à "
        "l'autre ». La contre-doctrine : Abū Ḥanīfa, ath-Thawrī, al-Layth et ash-Shāfiʿī — les qurūʾ à jamais, "
        "fussent-elles espacées, jusqu'à l'âge où les femmes de son peuple ne menstruent point, par l'apparent "
        "d'al-Baqara 228 et d'aṭ-Ṭalāq 4 ; et le n° 1831 d'Ibn Shihāb — « la retraite de la répudiée est les "
        "qurūʾ, fussent-elles espacées » — est cité en ce même chapitre comme contre-doctrine : « la parole "
        "d'Ibn Shihāb est rapportée fidèlement, l'école la pèse et la tient pour contre-doctrine — la fidélité de "
        "la compilation n'est point l'adhésion aveugle ». La mustaḍāḍa — deux cas : la non-muḥayyira distingue "
        "« entre les menstrues et l'istiḥāḍa — le sang pathologique — par l'odeur, ou la couleur, ou l'abondance, "
        "ou la maigreur, ou la coutume » et compte par les qurūʾ — « la discrimination des sangs rétablit la règle "
        "commune des réglées » ; la muḥayyira, qui ne distingue point et a oublié sa coutume, compte « une année "
        "complète » (n° 1845) — « neuf mois d'istibrāʾ, pour la disparition du doute », puis trois mois — "
        "« La gradation de l'école est ainsi complète : la réglée compte trois qurūʾ ; la mustaḍāḍa qui distingue "
        "compte comme elle ; la mustaḍāḍa confuse et celle dont les menstrues se sont levées portent l'attente "
        "des neuf mois puis trois mois ; la désespérée et la jeune comptent trois mois — chaque corps porte la "
        "retraite qui lui convient, et nulle femme ne demeure suspendue entre les règles. » Deuxième partie — la "
        "répudiée de ce qui précède de sa retraite avant le second divorce : Mālik — « elle renouvelle une retraite "
        "nouvelle, et ne bâtit point sur ce qui précède de la retraite avant le divorce » ; « parce que la reprise "
        "démolit la retraite (ar-rajʿa tahdum al-ʿidda) » et « le statut de la conjugalité contredit le statut de "
        "la retraite » ; elle est possédée sexuellement (madkhūl bihā), « son sein ne s'est point purifié par "
        "l'expiration d'une retraite » — le n° 1847 scelle : « elle renouvelle, du jour où il l'a répudiée, une "
        "retraite à venir ; et le mari s'est lésé (ẓalama nafsahu) et a erré s'il l'a reprise sans besoin d'elle ». La morale du "
        "chapitre : « il est interdit au mari de reprendre son épouse s'il n'a point de dessein en elle » — la "
        "reprise sans besoin « conduit à l'allongement de la retraite sur elle », et c'est « du préjudice (iḍrār) » "
        "qu'al-Baqara 231 interdit — « la reprise sans besoin est la rétention pour le tort : le verset la nomme "
        "du même nom que la leçon » ; al-Bājī explicite : « il veut — et Allah sait mieux — qu'il la reprenne et "
        "qu'il n'ait point de besoin d'elle » — « le dessein de la reprise est le rapport conjugal (jimāʿ) » ; la règle "
        "morale du chapitre : « la reprise est un droit, mais le droit se porte — il ne se joue point ». "
        "L'exploitation scelle par le n° 1848 — l'islam de la femme sans son mari : le mariage suspendu à la "
        "retraite ; le mari qui suit avant l'expiration « est le plus en droit d'elle tant qu'elle est en sa "
        "retraite » ; sinon la séparation s'accomplit par la seule différence de religion — « cela n'est point "
        "compté un divorce — c'est l'islam qui l'a dissoute sans divorce » : « elle ne porte ni la barrière de la "
        "troisième ni la prohibition du retour, car ce n'est point le ṭalāq qui les sépara, mais l'islam même » — "
        "« deux causes, deux régimes ». La préparation ouvre la leçon suivante (13121) : les manières légales de la "
        "réconciliation entre les époux en dispute, le statut du divorce suspendu (al-muʿallaq), les défauts qui "
        "requièrent la séparation entre les époux. Les notes du traducteur : cinq emplacements de versets en "
        "image, tous vides au scan ; les étiquettes imprimées « la sourate al-Baqara (الْبَقَرَة), verset 226 » à deux "
        "emplacements et « verset 229 » à un — le contenu exégétique requiert 2:228 (le mot même de qurūʾ) et "
        "2:231 (la rétention pour le tort) — 47ᵉ, 48ᵉ et 49ᵉ écarts d'étiquetage cumulés, textes restaurés "
        "verbatim au cache coranique ; les chaînes — Yaḥyā ibn Saʿīd et Yazīd ibn ʿAbdallāh ibn Qusayṭ al-Laythī, "
        "de Saʿīd ibn al-Musayyab (n° 1843) ; Ibn Shihāb az-Zuhrī (n° 1845) ; les dits compilés de Mālik lui-même "
        "(n° 1846, 1847, 1848) ; le n° 1831, contre-doctrine, au chapitre des qurūʾ."
    ),
    "explication": [
        "La leçon 18 succède à la double leçon du temps et du lieu (leçons 16 et 17, n° 1823-1838) et referme le "
        "chapitre des corps ordinaires : la précédente réglait la demeure et la pension de la répudiée, celle-ci "
        "rassemble ce qui restait du compte — les corps que les cycles ne règlent plus. Le titre porte le mot "
        "jāmiʿ — le recueil : la leçon compile en une seule architecture les statuts que le livre avait dispersés "
        "— la levée des menstrues était annoncée dès la préparation de la leçon 17. La vingt-quatrième leçon de "
        "l'imprimé (الدرس 24) annonce trois objectifs : connaître par quoi compte (taʿtaddu) celle qui ne "
        "menstrue point, saisir la différence entre la murtāba — celle qui est dans le doute — et la mustaḍāḍa, "
        "comprendre la sagesse de la législation de la retraite après la séparation des époux.",
        "Le préambule pose la doctrine du droit avant la mécanique du compte : la retraite est légiférée « pour "
        "la connaissance de la pureté du sein (barāʾat ar-raḥim) », « en sauvegarde des lignages de tout "
        "mélange », et « pour la magnification du rang du mariage et la manifestation de sa noblesse » — trois "
        "raisons qui en font autre chose qu'un délai technique. Elle est « un droit d'Allah — que Sa gloire soit "
        "exaltée — qu'Il a rendu obligatoire, un bien pour l'épouse, un droit du mari et de l'enfant : c'est "
        "pourquoi nul n'a à la renoncer » — la théorie du statut personnel en une phrase : ce qui protège le "
        "lignage n'est la propriété de personne, ni de la femme qui souffrirait d'attendre, ni du mari qui "
        "voudrait raccourcir. Trois espèces la partagent : « la retraite des qurūʾ — les cycles —, la retraite "
        "des mois, et la retraite de la mise au monde (waḍʾ al-ḥaml) » — et la leçon entière explore la zone où "
        "ni les cycles ni l'expérience ne parlent encore.",
        "Le n° 1843 entre par la plus haute autorité du chapitre : la parole dʿUmar ibn al-Khaṭṭāb — qu'Allah "
        "l'agrée — transmise par Saʿīd ibn al-Musayyab, le prince des Successeurs médinois, par la voie double de "
        "Yaḥyā ibn Saʿīd — le juge de Médine — et de Yazīd ibn ʿAbdallāh ibn Qusayṭ al-Laythī. « Toute femme "
        "répudiée qui a menstrué une ou deux fois, puis ses menstrues se sont levées, attendra neuf mois ; si une "
        "grossesse lui apparaît, tel est [son terme] ; sinon, après les neuf mois, elle comptera trois mois, puis "
        "elle deviendra licite. » La sentence complète le corpus califal du chapitre déjà rencontré — la sentence "
        "du ẓihār (leçon 12966) et la parole sur la mubtūta rapportée par Muslim (leçon 17) : le compte des corps "
        "déréglés est une question que le calife lui-même a tranchée, et l'école la reçoit comme un "
        "procès-verbal de la médine du Prophète — paix et bénédiction sur lui.",
        "Du côté du sens : « les neuf mois sont la durée ordinaire de la grossesse — l'usage veut que la "
        "grossesse, si elle est, se manifeste, ou que la femme s'assure de ses signes et les sente » ; si le "
        "terme passe sans manifestation, l'apparent est qu'elle est saine de grossesse, « dès lors qu'il ne se "
        "trouve d'elle nul doute (rayba) autre que la levée des menstrues. Or les menstrues se lèvent pour "
        "beaucoup de causes sans grossesse : leur levée ne dénote point la grossesse. » Après les neuf mois, "
        "« elle a alors le statut de celle qui a désespéré des menstrues — à ceci près que la désespérée n'a "
        "point eu besoin de neuf mois, parce que la marque du désespoir est apparente par l'âge et ses signes ; "
        "celle-ci, dont le statut propre est les menstrues, porte sur sa levée un doute dont elle ne se déporte "
        "qu'après l'istibrāʾ — la purification de la certitude — et l'istiqṣāʾ — l'examen exhaustif. » La "
        "doctrine distingue ainsi deux irrégularités de même effet et de statut différent : la désespérée est "
        "une évidence — l'âge parle ; la levée est une énigme — le corps se tait ; l'évidence compte "
        "directement, l'énigme exige la procédure.",
        "Point d'implicite contraire (mafhūm mukhālaf) écarté dans la parole dʿUmar : « car point de différence "
        "entre la grossesse et les menstrues » — si elle menstrue avant les neuf mois ou entre eux et les trois "
        "mois, « le statut des mois s'annule et elle reprend le compte par les qurūʾ ». Le n° 1846 déplie le jeu "
        "complet — la lettre même de Mālik : neuf mois ; si menstruation, elle réceptionne les menstrues ; si "
        "les menstrues se lèvent de nouveau, « elle annule ce qui précède de sa retraite, par la menstruation et "
        "par les mois qui l'ont précédée, et elle reprend l'istibrāʾ » ; et ainsi jusqu'à la troisième "
        "menstruation — si la troisième lui vient, elle aura achevé la retraite des menstrues ; si elle ne "
        "menstrue point, trois mois puis elle devient licite ; et la reprise demeure ouverte « avant qu'elle ne "
        "devienne licite — sauf s'il avait coupé (battaʾa) son divorce ». La règle technique qui porte tout : "
        "« La menstruation se joint (tulafqaq), fût-il entremêlé en elle du doute ; la durée de l'istibrāʾ ne se "
        "joint point, mais s'annule chaque fois qu'une menstruation la précède et qu'une menstruation la suit — "
        "car elle est un istibrāʾ qui renouvelle un doute isolé : la jonction n'y est point valable. Et les "
        "menstrues ne sont point un doute : elles le nient — c'est pourquoi une part d'elles se joint à "
        "l'autre. » La menstruation est une certitude qui nie le doute — deux certitudes s'additionnent ; "
        "l'attente est une probabilité qui dissout un doute isolé — elle ne s'additionne point : « la doctrine "
        "du recueil se tient tout entière dans ce mécanisme ».",
        "La leçon donne la contre-doctrine avec ses preuves : Abū Ḥanīfa, ath-Thawrī, al-Layth et ash-Shāfiʿī "
        "soutiennent que celle dont les menstrues se lèvent compte par les menstrues à jamais, fût-ce que les "
        "menstruations s'espacent, jusqu'à l'âge où les femmes de son peuple ne menstruent point — alors elle "
        "reprend la retraite de la désespérée, trois mois. Leur preuve est « l'apparent du noble Coran » : "
        "al-Baqara 228 donne les trois qurūʾ sans exception apparente, aṭ-Ṭalāq 4 réserve les mois à la "
        "désespérée et à la jeune — « l'apparent du verset 228 est qu'il n'y a point de place en lui pour les "
        "détentrices de qurūʾ de compter par les mois ». Et le Muwaṭṭaʾ lui-même porte la voix adverse : le dire "
        "d'Ibn Shihāb, rapporté par Mālik au chapitre des qurūʾ — « la retraite de la répudiée est les qurūʾ, "
        "fussent-elles espacées » [Muwaṭṭaʾ, n° 1831] — « un dire qui entre en ce chapitre, mais qui s'oppose à "
        "la doctrine de Mālik (مَالِك) en lui, et s'accorde à la parole d'ash-Shāfiʿī et de ceux qui l'ont "
        "suivi ». La leçon en tire la leçon de méthode : « la parole d'Ibn Shihāb est rapportée fidèlement, "
        "l'école la pèse et la tient pour contre-doctrine — la fidélité de la compilation n'est point l'adhésion "
        "aveugle » — le trait est constant du commentaire d'al-Zarqānī, déjà rencontré aux leçons du ẓihār et "
        "du muḥallil : l'école pèse ses propres matériaux au lieu de les gommer.",
        "La mustaḍāḍa — « celle dont le sang s'écoule de façon continue » — ouvre l'autre moitié de la leçon, et "
        "son cas ne manque point d'être l'un des deux. La mustaḍāḍa qui distingue (non-muḥayyira) reconnaît "
        "« entre les menstrues et l'istiḥāḍa — le sang pathologique — par l'odeur, ou la couleur, ou "
        "l'abondance, ou la maigreur, ou la coutume » : elle compte par les qurūʾ, à la généralité d'al-Baqara "
        "228, « parce qu'elle revient aux jours de sa coutume connue d'elle », et « parce que le sang distingué "
        "après une pureté complète (ṭuhr tām) compte pour des menstrues » — « la discrimination des sangs "
        "rétablit la règle commune des réglées ». La mustaḍāḍa confuse (muḥayyira) « n'a point pu distinguer "
        "entre les deux sangs et a oublié la mesure de sa coutume » : Mālik lui donne « une année complète », "
        "« parce qu'elle est en la position de celle dont les menstrues se sont levées et qui ne sait point ce "
        "qui les a levées » — « elle attendra neuf mois d'istibrāʾ, pour la disparition du doute — car c'est la "
        "durée de la grossesse d'ordinaire —, puis elle comptera trois mois, et elle deviendra licite aux époux "
        "après l'année ». Le n° 1845 — « La retraite de la mustaḍāḍa est une année. » — fournit la lettre, la "
        "doctrine en fournit la mécanique : l'année n'est point un sixième délai inventé, mais l'addition des "
        "deux procédures déjà connues. La gradation se clôt : « La gradation de l'école est ainsi complète : la "
        "réglée compte trois qurūʾ ; la mustaḍāḍa qui distingue compte comme elle ; la mustaḍāḍa confuse et "
        "celle dont les menstrues se sont levées portent l'attente des neuf mois puis trois mois ; la désespérée "
        "et la jeune comptent trois mois — chaque corps porte la retraite qui lui convient, et nulle femme ne "
        "demeure suspendue entre les règles. »",
        "La deuxième partie répond à la question de procédure laissée ouverte par la leçon 17 : que devient la "
        "retraite déjà comptée lorsque le mari reprend son épouse puis la sépare avant de la toucher ? Mālik "
        "tranche : « elle renouvelle une retraite nouvelle, et ne bâtit point sur ce qui précède de la retraite "
        "avant le divorce » — « parce que la reprise démolit la retraite (ar-rajʿa tahdum al-ʿidda) », et « le "
        "statut de la conjugalité contredit le statut de la retraite : dès lors que la reprise est établie, la "
        "retraite s'annule » ; la femme est possédée sexuellement (madkhūl bihā), « son sein ne s'est point "
        "purifié par l'expiration d'une retraite : la retraite lui fut donc obligatoire ». Le n° 1847 — le "
        "second dit compilé de Mālik — porte la lettre et la clause morale dans une même phrase : « elle "
        "renouvelle, du jour où il l'a répudiée, une retraite à venir ; et le mari s'est lésé (ẓalama nafsahu) et "
        "a erré s'il l'a reprise sans besoin d'elle » — la doctrine ne sépare jamais le compte du droit.",
        "La morale se déplie : « il est interdit au mari de reprendre son épouse s'il n'a point de dessein en "
        "elle », car le divorce après reprise « conduit à l'allongement de la retraite sur elle — et c'est du "
        "préjudice (iḍrār) » qu'al-Baqara 231 interdit — « la reprise sans besoin est la rétention pour le "
        "tort : le verset la nomme du même nom que la leçon ». Al-Bājī — Abū l-Walīd al-Bājī (m. 474/1081), "
        "l'auteur du al-Muntaqā, le commentaire mālikite du Muwaṭṭaʾ, déjà rencontré — explicite : « il veut — "
        "et Allah sait mieux — qu'il la reprenne et qu'il n'ait point de besoin d'elle » ; « le dessein de la "
        "reprise est le rapport conjugal (jimāʿ) », sans profit pour l'homme et au prix de l'injustice pour la "
        "femme — « La règle morale du chapitre : la reprise est un droit, mais le droit se porte — il ne se "
        "joue point ; l'homme qui lève et abat l'inviolabilité pour l'orgueil de la posséder fait tourner le "
        "temps de la femme à son propre mépris. » L'exploitation scelle par le n° 1848 : la femme qui embrasse "
        "l'islam sans son mari voit le mariage suspendu à la retraite ; le mari qui suit avant l'expiration "
        "« est le plus en droit d'elle tant qu'elle est en sa retraite » ; sinon la séparation s'accomplit sans "
        "divorce — « cela n'est point compté un divorce — c'est l'islam qui l'a dissoute sans divorce » — et le "
        "mariage ultérieur « ne porte ni la barrière de la troisième ni la prohibition du retour, car ce n'est "
        "point le ṭalāq qui les sépara, mais l'islam même » : « la Loi distingue la fin du conjugal par la "
        "volonté de l'homme et sa fin par l'ordre de Dieu — deux causes, deux régimes ». La préparation ouvre "
        "la leçon suivante (13121) : les manières légales de la réconciliation entre les époux en dispute, le "
        "statut du divorce suspendu (al-muʿallaq), les défauts qui requièrent la séparation entre les époux. "
        "Les notes du traducteur consignent les cinq emplacements de versets en image, tous vides au scan, et "
        "les trois écarts d'étiquetage restaurés au cache coranique (2:228 à deux emplacements, 2:231) — "
        "47ᵉ, 48ᵉ et 49ᵉ écarts cumulés du registre.",
    ],
    "points": [
        "Fil du livre : après le compte des réglées (leçon 16) et le toit et le blé (leçon 17), le recueil "
        "(jāmiʿ) rassemble les corps que les cycles ne règlent plus — la levée des menstrues (ar-rafʿ), la "
        "mustaḍāḍa, la désespérée, la jeune — et la retraite après reprise et second divorce.",
        "Le préambule : la retraite est « un droit d'Allah », « un bien pour l'épouse, un droit du mari et de "
        "l'enfant : c'est pourquoi nul n'a à la renoncer » — trois espèces : les qurūʾ, les mois, la mise au "
        "monde (waḍʾ al-ḥaml).",
        "Le n° 1843 : la parole dʿUmar par Saʿīd ibn al-Musayyab, via Yaḥyā ibn Saʿīd et Yazīd ibn ʿAbdallāh ibn "
        "Qusayṭ al-Laythī — neuf mois d'attente, la grossesse qui tranche, sinon trois mois — le procès-verbal "
        "califal qui complète la sentence du ẓihār et la parole sur la mubtūta.",
        "Le fond du sens : les neuf mois sont « la durée ordinaire de la grossesse » — passé le terme sans "
        "manifestation, la femme prend « le statut de celle qui a désespéré des menstrues », moins la "
        "procédure : l'istibrāʾ (la purification de la certitude) et l'istiqṣāʾ (l'examen exhaustif).",
        "Point d'implicite contraire (mafhūm mukhālaf) écarté : « point de différence entre la grossesse et les "
        "menstrues » — si elle menstrue, « le statut des mois s'annule et elle reprend le compte par les "
        "qurūʾ ».",
        "Le mécanisme du n° 1846 : la double échelle des mois et des menstrues, l'annulation et la reprise, "
        "« la jonction de la menstruation et la non-jonction de l'attente » — « la doctrine du recueil se tient "
        "tout entière dans ce mécanisme ».",
        "La règle du talfīq : « la menstruation se joint » — « les menstrues ne sont point un doute : elles le "
        "nient » ; l'attente ne se joint point — elle « renouvelle un doute isolé » ; « la certitude du lignage "
        "ne se construit point sur la probabilité, mais sur la succession réglée du sang et de la pureté ».",
        "La contre-doctrine : Abū Ḥanīfa, ath-Thawrī, al-Layth et ash-Shāfiʿī — les qurūʾ à jamais jusqu'à "
        "l'âge du peuple, par l'apparent d'al-Baqara 228 et d'aṭ-Ṭalāq 4 ; le n° 1831 d'Ibn Shihāb s'accorde à "
        "eux — le Muwaṭṭaʾ « dialogue avec lui-même », « la fidélité de la compilation n'est point l'adhésion "
        "aveugle ».",
        "La mustaḍāḍa non-muḥayyira : elle distingue les sangs — l'odeur, la couleur, l'abondance, la maigreur, "
        "la coutume — et compte par les qurūʾ — « la discrimination des sangs rétablit la règle commune des "
        "réglées ».",
        "La mustaḍāḍa muḥayyira : « une année complète » (n° 1845) — « neuf mois d'istibrāʾ » puis trois mois ; "
        "l'année n'est point un sixième délai, mais l'addition des deux procédures déjà connues.",
        "La gradation close : « chaque corps porte la retraite qui lui convient, et nulle femme ne demeure "
        "suspendue entre les règles » — réglée trois qurūʾ ; confuse et levée neuf mois puis trois ; désespérée "
        "et jeune trois mois.",
        "La reprise démolit la retraite (ar-rajʿa tahdum al-ʿidda, n° 1847) : renouvellement du compte, "
        "madkhūl bihā — et la clause morale : « le mari s'est lésé et a erré s'il l'a reprise sans besoin "
        "d'elle » ; la rétention pour le tort d'al-Baqara 231 — « le droit se porte — il ne se joue point ».",
        "L'exploitation (n° 1848) : la dissolution par l'islam — « cela n'est point compté un divorce », sans "
        "barrière de la troisième ni prohibition du retour — « deux causes, deux régimes » ; la préparation "
        "ouvre 13121 (réconciliation en dispute, divorce suspendu al-muʿallaq, défauts requiérant la "
        "séparation).",
    ],
    "vocabulaire": [
        {"ar": "الرفع", "translit": "ar-rafʿ",
         "fr": "la levée : « elle n'a point menstrué — le sang s'est levé d'elle sans qu'elle le voie » ; le "
               "premier statut du recueil — la shābba dont les menstrues se lèvent attend neuf mois puis trois "
               "mois ; beaucoup de causes lèvent les menstrues sans grossesse — « leur levée ne dénote point la "
               "grossesse »"},
        {"ar": "المستحاضة", "translit": "al-mustaḍāḍa",
         "fr": "celle dont le sang coule sans interruption : « celle dont le sang s'écoule de façon continue » ; "
               "deux cas — la non-muḥayyira distingue les sangs et compte par les qurūʾ, la muḥayyira qui a "
               "oublié sa coutume compte « une année complète » (n° 1845)"},
        {"ar": "الاستبراء", "translit": "al-istibrāʾ",
         "fr": "« la purification de la certitude » : l'attente des neuf mois — « la durée ordinaire de la "
               "grossesse » — avant le compte de trois mois ; elle ne se joint point (point de talfīq pour "
               "l'attente) et s'annule chaque fois qu'une menstruation la précède"},
        {"ar": "المرتابة", "translit": "al-murtāba",
         "fr": "celle qui est dans le doute : les menstrues se sont levées sans cause apparente — son doute se "
               "lève par l'istibrāʾ puis le compte de trois mois ; à distinguer de la mustaḍāḍa (question du "
               "contrôle de la leçon)"},
        {"ar": "البت", "translit": "al-batt",
         "fr": "« la coupure » : « il l'a répudiée d'une répudiation sans reprise, dissolvante » (battaʾa) — la "
               "forme déjà établie aux leçons du muḥallil et de la mubtūta ; la batta ferme la reprise que le "
               "n° 1846 laisse ouverte « avant qu'elle ne devienne licite »"},
        {"ar": "التلفيق", "translit": "at-talfīq",
         "fr": "la jonction : « la menstruation se joint » à la menstruation, car elle n'est point un doute mais "
               "ce qui le nie ; l'attente de l'istibrāʾ ne se joint point — « la rigueur de l'école envers la "
               "rayba »"},
        {"ar": "الحمل", "translit": "al-ḥaml",
         "fr": "la grossesse : « le fardeau se manifeste dans son corps » (bāna bihā ḥaml) — son apparition "
               "tranche la retraite à la mise au monde (waḍʾ al-ḥaml) ; les neuf mois d'attente la présupposent"},
        {"ar": "الريبة", "translit": "ar-rayba",
         "fr": "le doute : « nul doute (rayba) autre que la levée des menstrues » — l'architecture du recueil "
               "dissout chaque doute par sa procédure : « chaque doute porte sa procédure de dissolution, et "
               "nulle retraite ne se compte qu'une fois la rayba dissoute »"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}


def norme_fr(s):
    s = s.replace('\'', '’')
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


def texte_corpus():
    """htmlFr débalisé : frontières de blocs -> espace, tags inline -> ''."""
    d = json.load(open(LIVRE, encoding='utf-8'))
    e = [x for x in d['lessons'] if x['docId'] == DOCID][0]
    raw = e['htmlFr']
    t = re.sub(r'</?(p|h[1-6]|li|dd|dt|blockquote|div|tr|td|th|ul|ol|dl|section)[^>]*>', ' ', raw, flags=re.I)
    t = re.sub(r'<[^>]+>', '', t)
    t = H.unescape(t)
    t = t.replace('\u00a0', ' ').replace('\u202f', ' ')
    return re.sub(r'\s+', ' ', t).strip()


def norme_cmp(s):
    s = s.replace('\u202f', ' ').replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s)


# ---------- fusion ----------
data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
if DOCID in com:
    print(f'!! {DOCID} déjà présent — rien de fait')
    raise SystemExit(1)
com[DOCID] = norme_entree(E_13117)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# ---------- validation ----------
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
e = data2['commentaires'][DOCID]
mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
for t in [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]:
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
    if not motif_ar.search(v['ar']):
        mauvais += 1
        print('   vocab ar non arabe :', v['ar'])
    if re.search(r'[\u064B-\u0652\u0670]', v['ar']):
        mauvais += 1
        print('   vocab ar avec harakat :', v['ar'])

# ---------- verif-citations (fragments « » verbatim dans le htmlFr) ----------
corpus = norme_cmp(texte_corpus())
textes = [e['resume']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']]
fragments = []
for t in textes:
    fragments += re.findall(r'«([^«»]+)»', t)
manquants = []
for f in fragments:
    fc = norme_cmp(f).strip(' …\u202f\u00a0')
    if fc and fc not in corpus:
        manquants.append(f)
print(f'verif-citations : {len(fragments)} fragments « », {len(manquants)} manquant(s)')
for f in manquants:
    print('   MANQUE :', f[:100])
if manquants:
    mauvais += len(manquants)

# ---------- recoupements ----------
an = json.load(open(LIVRE, encoding='utf-8'))['lessons']
def fr(docid):
    x = [y for y in an if y['docId'] == docid][0]
    t = re.sub(r'</?(p|h[1-6]|li|dd|dt|blockquote|div|tr|td|th|ul|ol|dl|section)[^>]*>', ' ', x['htmlFr'], flags=re.I)
    t = re.sub(r'<[^>]+>', '', t)
    t = H.unescape(t)
    return re.sub(r'\s+', ' ', t)

ancres = [
    ('13114 — la leçon du compte des réglées (les qurūʾ et les cinq maîtres de Médine)', 'qurūʾ' in fr('13114') and 'cinq maîtres' in fr('13114')),
    ('13115 — la leçon précédente immédiate (la mubtūta et la doctrine de la reprise — corpus califal)', 'mubtūta' in fr('13115') and 'reprise' in fr('13115')),
    ('12992 — la leçon du muḥallil, où la bāʾin fut établie', 'muḥallil' in fr('12992') and 'bāʾin' in fr('12992')),
    ('12966 — la leçon du ẓihār, première pièce du corpus califal du chapitre', 'ẓihār' in fr('12966')),
    ('13121 — la leçon suivante du registre (objet de la préparation : la réconciliation entre les époux en dispute)', 'dispute' in fr('13121')),
    ('13117 — la leçon même (l\'istibrāʾ et l\'architecture du doute)', 'istibrāʾ' in corpus and 'architecture du doute' in corpus),
]
ok = 0
for nom, b in ancres:
    print('recoupement :', 'PASS' if b else 'ÉCHEC', '—', nom)
    ok += 1 if b else 0
if ok != len(ancres):
    mauvais += len(ancres) - ok

print('contrôle ponctuation/arabe FR + citations + recoupements :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
if mauvais:
    sys.exit(1)
