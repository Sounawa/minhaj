#!/usr/bin/env python3
"""R770 — ajoute le commentaire pédagogique de la leçon 15 de hadith-tanawi-1
(13101 عدة التي فقد زوجها ومراجعة الغائب — lʿidda de la femme qui a perdu son
mari et le retour de l'absent, « Plusieurs femmes qui ont perdu leur mari et
passent en revue les absents » dans la traduction du manuel, la quinzième du
livre, étiquetée « leçon 21 » par l'imprimé (الدرس 21) — le SUIVANT de R769,
13079, selon l'ordre des leçons du registre : 12925 … 13074, 13079, puis 13101)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r769-c14.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~12 500 caractères débalisé ; couche
arabe lue en entier pour l'étiquette de l'imprimé « (الدرس 21) », la
référence coranique de la couche arabe — سورة البقرة الآية: 226, en
étiquette seule, sans texte de verset imprimé — et la seconde question de la
préparation préalable, porteuse d'un emplacement de verset vide
(ما المراد بالأقراء في قوله تعالى؟), absente de la couche française).
Règle 2 de LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ
(1819, 1820, 1821, 1822), les attributions (ʿUmar b. al-Khaṭṭāb, Mālik,
Yahyā b. Saʿīd, Saʿīd b. al-Musayyib, Ibn ʿĀsim, al-Shāfiʿī, Abū Ḥanīfah,
ʿAlī, al-Bayhaqī, Ibn al-Qāsim, al-Ashhab, al-Nafrāwī), les rapports
(Sunan al-Kubrā, al-Taḥfah, la Mudawwana, al-Fawākhid al-Dawānī) sont cités
tels qu'ils figurent dans la leçon. Les formes arabes du vocabulaire sont
reprises de la couche arabe ou dérivées des translittérations de la leçon,
sans harakat (règle 3).

Garde-fous (convention des vagues R765-R769) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr de la leçon (0 manquant, abort sinon) ;
- recoupements : ancres vérifiées dans les leçons voisines (13079 — la
  leçon précédente du registre, le liʿān ; 13074 — le khulʿ et son débat
  divorce/rupture ; 12925 — l'exploitation de L1, al-Baqara 233 ;
  12971 — l'īlāʾ, dont le verset général [al-Baqara 226] est l'argument
  du Shafiʿite ici ; 13114 — la leçon suivante du registre, le divorce
  durant les règles, annoncée par la préparation préalable).
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13101'

E_13101 = {
    "auteur": "IA-1, tour R770",
    "resume": (
        "Guide de lecture de la leçon 15 (عدة التي فقد زوجها ومراجعة الغائب — lʿidda "
        "de la femme qui a perdu son mari et le retour de l'absent ; la traduction "
        "du manuel porte « Plusieurs femmes qui ont perdu leur mari et passent en "
        "revue les absents »), la quinzième du livre, étiquetée leçon 21 par "
        "l'imprimé (الدرس 21) : le n° 1819 du Muwaṭṭaʾ arme le fond — « de Yahyā "
        "b. Saʿīd, de Saʿīd b. al-Musayyib, rapporte que ʿUmar b. al-Khaṭṭāb a dit : "
        "« Toute femme qui a perdu son mari et ne sait pas où il se trouve, attendra "
        "quatre ans, puis accomplit une ʿidda de quatre mois et dix jours, et ensuite "
        "elle devient libre (pour se remarier). » » — l'attente de quatre ans, puis "
        "lʿidda de veuve, puis la libération. Le n° 1820 en tire l'effet dans les deux "
        "sens : « Et si elle se marie après l'expiration de son ʿidda, que son mari "
        "(le premier) ait eu des relations avec elle ou non, il n'a plus aucun droit "
        "sur elle. » — et son pendant : « Tel est notre avis. Et si son mari (le "
        "premier) la rejoint avant qu'elle ne se marie, il a le plus grand droit sur "
        "elle. » Le n° 1821 borne le premier propos : « J'ai entendu les gens "
        "contredire ce que certains ont rapporté sur ʿUmar b. al-Khaṭṭāb à savoir "
        "qu'il aurait dit : » — « Son premier mari a le choix, s'il revient, entre "
        "le mahr (dot) ou l'épouse ». Et le n° 1822 transporte la règle au divorcé de "
        "l'absente : ʿUmar au sujet d'une femme « que son mari a divorcée d'elle alors "
        "qu'il était absent, puis l'a rejointe sans que son retour parvienne à elle, "
        "alors que le divorce avait déjà été notifié à celle-ci », « qu'elle s'est "
        "alors mariée » : « Que le second mari ait eu des relations avec elle ou non, "
        "le premier mari qui l'avait divorcée n'a plus aucun droit sur elle. » — "
        "« Tel est ce qui me paraît le plus juste dans ces affaires de disparus. » Le "
        "tamhīd fonde le tout : « Il n'est pas permis à l'un des époux de causer le "
        "moindre préjudice à l'autre » — « le préjudice est interdit par la loi "
        "divine » ; quand il se produit « de manière intentionnelle ou non », « la "
        "loi religieuse l'efface » et donne au lésé « le droit de s'en défaire par le "
        "divorce » — et le préjudice de l'épouse « à cause de la disparition de son "
        "mari » est du nombre. Deux questions ordonnent la leçon : « Quel est donc le "
        "sort de la femme dont le mari a disparu ? » et « que se passe-t-il si un "
        "homme divorce de son épouse alors qu'il est absent, puis la revoit sans l'en "
        "informer, et qu'elle s'est mariée dans l'intervalle ? » Les termes : Ayyimā "
        "— composé de « ayyu » (nom qui remplace une condition) et de « mā » "
        "(indéfini ajouté), « locution qui dispense d'un développement trop long ou "
        "inutile » ; Faqadat — le qāf ouvert, sa forme verbale faqida ; le mafqūd est "
        "« celui dont on perd la trace sans nouvelles de lui ». L'analyse déploie "
        "« Le disparu se présente sous trois aspects ». A) Le disparu dont on ignore "
        "le lieu, non tombé au combat où « la supposition penche pour son décès » : "
        "« Si son épouse porte l'affaire devant le juge, celui-ci enquête sur son "
        "sort » ; sans nouvelles, il « lui accorde un nouveau délai de quatre ans » "
        "— « S'il revient durant ce délai, ou si des nouvelles de sa vie parviennent, "
        "le lien conjugal subsiste » ; sinon « elle accomplit alors la ʿidda de "
        "veuve » — s'il revient durant cette ʿidda, le lien subsiste ; à l'expiration "
        "du délai sans retour ni nouvelles, « elle devient libre pour se remarier » "
        "— « c'est le sens du propos de ʿUmar b. al-Khaṭṭāb » ; et si elle ne porte "
        "pas l'affaire au juge et consent à cela, « elle reste sous sa protection "
        "légale jusqu'à ce que son sort se clarifie ». Divergences sur la fixation de "
        "ce délai : « c'est un acte d'obéissance rituelle » ('amr taʿabbudī) que "
        "notre maître ʿUmar a institué et que les Compagnons ont approuvé ; « c'est "
        "la durée maximale d'une grossesse » ; ou « le délai maximal dans lequel on "
        "peut espérer obtenir des nouvelles du mari à cette époque ». B) Le disparu "
        "au combat : « son épouse ne se marie jamais et elle et son patrimoine sont "
        "en suspens jusqu'à ce qu'il atteigne l'âge au-delà duquel la vie est "
        "impossible, c'est-à-dire l'âge de son équivalent » — divergences sur cet "
        "âge : soixante-dix ans, quatre-vingts, cent, et d'autres encore — « Le "
        "premier avis est le plus solide, à cause du propos d'Ibn ʿĀsim dans "
        "al-Taḥfah » : « Et à eux plusieurs avis, le plus solide est celui de "
        "soixante-dix ans. » C) Le disparu au temps de la fitna : « on ne fixe pas "
        "de délai pour lui, et son épouse l'attend » — elle patiente aussi longtemps "
        "que durent « les fuyards et les vaincus », puis elle accomplit sa ʿidda et "
        "se marie — « à moins qu'il ne se soit disparu dans un pays lointain, auquel "
        "cas on fixe pour lui un délai correspondant au temps qu'il faudrait pour "
        "l'atteindre ». Et l'école de la certitude : al-Shāfiʿī, Abū Ḥanīfah et un "
        "groupe de savants estiment que l'épouse d'un disparu « n'a pas de délai de "
        "quatre ans, ni plus, ni moins », et « elle ne se marie pas jusqu'à ce que "
        "la mort ou le divorce soit certainement établi » — « son contrat est "
        "certainement valide, et il ne peut être levé que par certitude » ; à cela "
        "fait allusion le rapport d'al-Shāfiʿī de ʿAlī, avec une suspension "
        "(taqyīf) : « L'épouse d'un disparu est une femme éprouvée, qu'elle patiente "
        "jusqu'à ce que la certitude de sa mort lui parvienne. » — « Al-Bayhaqī l'a "
        "rapporté dans son Sunan al-Kubrā. » Le retour du disparu après lʿidda : si "
        "elle ne s'est pas remariée, « il a le plus grand droit sur elle » ; si elle "
        "s'est remariée et que le premier revient après que le second a eu des "
        "relations avec elle, « il n'a plus aucun droit sur elle » ; s'il revient "
        "avant que le second n'ait eu de relations, « il y a eu divergence dans "
        "l'avis de l'imam Mālik » lui-même : dans le Muwaṭṭaʾ « le premier n'a plus "
        "aucun droit sur elle » — le sens du n° 1820 — et « Il a été rapporté de lui "
        "qu'il s'est rétracté de cet avis un an avant sa mort » : « Le seul moyen "
        "pour le premier de conserver son droit sur elle est que le second ait eu "
        "des relations avec elle sans savoir qu'il était vivant. » — « Ibn al-Qāsim "
        "et al-Ashhab ont adopté cet avis. » Le n° 1821 admet deux sens : ou les "
        "gens contredisent le propos « bien qu'il soit authentique d'après ʿUmar, "
        "mais ils ne le considèrent pas comme applicable, car celui qui a contracté "
        "un mariage avec une femme et que survient une cause de séparation, n'a plus "
        "droit au mahr » ; ou ils contredisent « la narration, c'est-à-dire "
        "l'authenticité du propos attribué à ʿUmar b. al-Khaṭṭāb ». Deuxièmement : "
        "le statut de celui qui a revu son épouse alors qu'il était absent et ne l'a "
        "pas informée jusqu'à ce qu'elle se soit mariée — « Qu'un homme ait divorcé "
        "de son épouse puis disparu, ou qu'il l'ait divorcée alors qu'il était absent "
        "et l'ait informée, puis qu'il l'ait rejointe sans l'en informer, et qu'elle "
        "se soit mariée après l'expiration de sa ʿidda, et que son premier mari "
        "revienne : a-t-il un droit sur elle ou non ? » Mālik dans le Muwaṭṭaʾ : « il "
        "n'a absolument aucun droit de retour sur elle, que le second mari ait eu "
        "des relations avec elle ou non » — c'est ce qui a été rapporté de ʿUmar — "
        "« Tel est ce qui me paraît le plus juste dans ces affaires et dans celles "
        "des disparus » — « la simple conclusion du mariage avec le second l'ôte au "
        "premier ». Mais « dans la Mudawwana, son avis est qu'elle n'est perdue pour "
        "le premier que si le second a eu des relations avec elle, et non par le "
        "simple contrat » — « C'est l'avis le plus répandu dans le madhhab » ; "
        "rétractation rapportée avant sa mort ; et son propos du Muwaṭṭaʾ « est une "
        "preuve qu'il a entendu d'autres avis ». Al-Shāfiʿī « et d'autres savants "
        "ont estimé » que « le premier a le plus grand droit sur elle, que le second "
        "ait eu des relations avec elle ou non » — argument par « le verset général "
        "d'Allah le Très-Haut » : « Quant à ceux qui jurent de s'abstenir de leurs "
        "épouses, ils ont un délai de quatre mois. S'ils reviennent, alors Allah est "
        "Pardonneur et Miséricordieux. » (Sourate al-Baqarah, verset 226) ; le "
        "raisonnement : consensus sur le droit du premier s'il revient avant le "
        "remariage — ce qui indique « la validité du retour (du premier mari) alors "
        "que l'épouse était ignorante de cela » — et si le retour est valide, elle "
        "est l'épouse du premier et « le mariage du second est dissous » — « C'est "
        "ce qui a été rapporté de ʿAlī ». La sagesse derrière le divorce de la femme "
        "dont le mari a disparu, après la recherche et la fixation du délai : « "
        "d'éliminer tout préjudice, sous toutes ses formes et de tous les types, "
        "subi par l'épouse à cause de la disparition de son mari, et de garantir le "
        "droit de l'épouse à demander le divorce si elle subit un préjudice de la "
        "part de son mari. » L'évaluation demande « les différents cas de disparus "
        "et le statut de l'épouse de chacun d'eux », le statut de la divorcée que "
        "son mari a rejointe en absence sans l'informer jusqu'à son remariage, et la "
        "sagesse du divorce de l'épouse du disparu après recherche et délai. "
        "L'enrichissement (istithmār) imprime un extrait des « Fruits mûrs » "
        "(al-Fawākhid al-Dawānī) sur l'épître d'Ibn Abī Zayd al-Qayrawānī par Aḥmad "
        "b. Ghānim al-Nafrāwī (41/2), « avec adaptations » : le disparu « dont on "
        "connaît le lieu » et « dont la disparition n'est pas due à une famine ou à "
        "une épidémie » — la procédure : la femme qui ne veut pas patienter porte "
        "l'affaire au juge « après avoir établi le mariage, la disparition du mari "
        "et la continuation de la protection légale jusqu'à ce jour », et le juge "
        "« rédige un document contenant son nom, sa généalogie et sa description », "
        "« l'envoie au juge du pays où on pense qu'il se trouve » — ou « l'envoie au "
        "pays de rassemblement » ; trois questions. La préparation préalable annonce "
        "la leçon suivante : « Lis les hadiths de la leçon suivante et réponds à ce "
        "qui suit » — « Énonce le statut du divorce pendant les règles d'impureté "
        "(ḥayḍ). » — le divorce durant les menstrues et lʿidda des aqrāʾ, la "
        "seizième du livre. NB consignés (sans correction, règle 5) : (1) la "
        "traduction du titre rend (عدة) par « Plusieurs femmes » et (مراجعة) par « "
        "passent en revue » — calques littéraux ; le sujet réel de la leçon est "
        "lʿidda de la femme qui a perdu son mari et le retour du disparu ou du "
        "divorcé absent ; (2) l'emplacement coranique : la couche arabe porte "
        "l'étiquette seule (سورة البقرة الآية: 226) sans texte de verset, la couche "
        "française imprime le texte du verset 226 — le verset de l'īlāʾ — conforme "
        "à l'étiquette, à la différence de la leçon précédente (13079) où les deux "
        "emplacements portaient le texte du verset du fouet ; (3) la couche arabe de "
        "la préparation préalable porte deux questions, la couche française une "
        "seule — la seconde (ما المراد بالأقراء في قوله تعالى؟) porte un emplacement "
        "de verset vide au scan, parenthèses sans texte : le verset des aqrāʾ est "
        "al-Baqara 228 (المطلقات يتربصن بأنفسهن ثلاثة قروء) — reconstruction "
        "consignée, sans correction ; (4) la référence d'al-Fawākhid porte le "
        "millésime « 41/2 » tel qu'imprimé, et l'extrait est donné « avec "
        "adaptations » ; (5) les deux rédactions de la réponse malikite — « Tel est "
        "ce qui me paraît le plus juste dans ces affaires de disparus. » (n° 1822) "
        "et « Tel est ce qui me paraît le plus juste dans ces affaires et dans "
        "celles des disparus » (le commentaire) — variante consignée sans "
        "correction."),
    "explication": [
        ("La leçon 15 succède au liʿān (leçon 14, n° 1784-1788) et ouvre le chapitre "
         "du disparu (al-mafqūd) et du retour de l'absent : les numéros 1819-1822 du "
         "Muwaṭṭaʾ succèdent aux 1784-1788 du liʿān, dans le même livre du mariage. "
         "Le fil du livre passe du divorce (leçons 4 à 7), de l'īlāʾ et du ẓihār, de "
         "la dot, du khulʿ et du liʿān au temps qui court sur l'absence : l'épouse du "
         "disparu d'abord, la divorcée que l'absent rejoint à son insu ensuite. Trois "
         "objectifs sont posés à l'ouverture : connaître les règles de la ʿidda de "
         "l'épouse d'un disparu et celles qui s'appliquent si son mari le revoit "
         "durant son absence ; distinguer les types de disparus et le statut de "
         "l'épouse de chacun d'eux ; comprendre la sagesse derrière le divorce de "
         "l'épouse d'un disparu après l'expiration du délai."),
        ("Le tamhīd enracine le tout dans l'interdit du préjudice conjugal : « Il "
         "n'est pas permis à l'un des époux de causer le moindre préjudice à "
         "l'autre » — « le préjudice est interdit par la loi divine ». Quand il se "
         "produit, « de manière intentionnelle ou non », « la loi religieuse "
         "l'efface » et donne au lésé « le droit de s'en défaire par le divorce ». "
         "La disparition du mari est rangée parmi ces préjudices : l'épouse dont le "
         "mari a perdu la trace subit un préjudice continu, et la charia lui ouvre "
         "une sortie. Deux questions ordonnent l'analyse entière : le sort de la "
         "femme dont le mari a disparu ; et le sort du retour de l'homme qui divorce "
         "en absence, revoit son épouse sans l'en informer, et la trouve mariée dans "
         "l'intervalle."),
        ("Le premier aspect du disparu déploie la procédure judiciaire : l'épouse "
         "porte l'affaire au juge, « celui-ci enquête sur son sort » ; sans "
         "nouvelles, il lui accorde « un nouveau délai de quatre ans » ; le retour "
         "ou les nouvelles de la vie du mari pendant ce délai maintiennent la "
         "conjugalité ; sinon elle accomplit « la ʿidda de veuve » — quatre mois et "
         "dix jours, le même compte que la veuve ordinaire ; le retour pendant "
         "l'ʿidda la maintient encore ; l'expiration sans retour ni nouvelles la "
         "libère — « c'est le sens du propos de ʿUmar b. al-Khaṭṭāb ». La leçon "
         "ajoute l'option de la femme qui ne saisit pas le juge et consent : elle "
         "reste « sous sa protection légale jusqu'à ce que son sort se clarifie ». "
         "Les quatre ans reçoivent trois justifications dans la divergence : un "
         "« acte d'obéissance rituelle » ('amr taʿabbudī) institué par ʿUmar et "
         "approuvé des Compagnons ; « la durée maximale d'une grossesse » ; ou « le "
         "délai maximal dans lequel on peut espérer obtenir des nouvelles du mari à "
         "cette époque » — l'obéissance rituelle l'emporte dans la lecture malikite, "
         "les deux autres étant des sagesses adjacentes."),
        ("Les deux autres aspects déploient la patience imposée. Le disparu au "
         "combat : son épouse ne se marie jamais, et elle et son patrimoine sont en "
         "suspens « jusqu'à ce qu'il atteigne l'âge au-delà duquel la vie est "
         "impossible, c'est-à-dire l'âge de son équivalent » — divergences sur cet "
         "âge (soixante-dix, quatre-vingts, cent ans), le plus solide étant "
         "soixante-dix, « à cause du propos d'Ibn ʿĀsim dans al-Taḥfah » : « Et à "
         "eux plusieurs avis, le plus solide est celui de soixante-dix ans. » Le "
         "disparu au temps de la fitna : aucun délai, l'attente aussi longue que "
         "durent « les fuyards et les vaincus », puis ʿidda et mariage — et si le "
         "pays de disparition est lointain, « un délai correspondant au temps qu'il "
         "faudrait pour l'atteindre ». Face aux trois aspects, l'école de la "
         "certitude (al-Shāfiʿī, Abū Ḥanīfah et un groupe de savants) refuse le "
         "délai : « son contrat est certainement valide, et il ne peut être levé "
         "que par certitude » — pas de mariage « jusqu'à ce que la mort ou le "
         "divorce soit certainement établi », à l'appui le rapport d'al-Shāfiʿī de "
         "ʿAlī (taqyīf) rapporté par al-Bayhaqī dans son Sunan al-Kubrā : la femme "
         "éprouvée patiente « jusqu'à ce que la certitude de sa mort lui "
         "parvienne »."),
        ("Le retour du disparu après lʿidda se règle sur trois cas. Avant "
         "remariage : « il a le plus grand droit sur elle » — le propos de Mālik du "
         "n° 1820. Après remariage et relations du second : plus aucun droit. Après "
         "remariage sans relations : divergence chez Mālik lui-même — le Muwaṭṭaʾ "
         "porte « le premier n'a plus aucun droit sur elle », mais « Il a été "
         "rapporté de lui qu'il s'est rétracté de cet avis un an avant sa mort » : "
         "le seul moyen pour le premier de conserver son droit est que le second "
         "ait eu des relations avec elle « sans savoir qu'il était vivant » — "
         "« Ibn al-Qāsim et al-Ashhab ont adopté cet avis ». Le n° 1821 admet deux "
         "sens : les gens contredisent le propos attribué à ʿUmar « bien qu'il soit "
         "authentique d'après ʿUmar, mais ils ne le considèrent pas comme "
         "applicable » — celui qui a contracté puis qu'une cause de séparation "
         "survienne n'a plus droit au mahr ; ou ils contredisent « la narration, "
         "c'est-à-dire l'authenticité du propos attribué à ʿUmar b. al-Khaṭṭāb » — "
         "la récusation porte alors sur la transmission même."),
        ("La seconde partie transporte la règle au divorcé de l'absente. Mālik dans "
         "le Muwaṭṭaʾ (n° 1822) : « il n'a absolument aucun droit de retour sur "
         "elle, que le second mari ait eu des relations avec elle ou non » — "
         "rapporté de ʿUmar, « la simple conclusion du mariage avec le second l'ôte "
         "au premier » ; mais « dans la Mudawwana, son avis est qu'elle n'est "
         "perdue pour le premier que si le second a eu des relations avec elle, et "
         "non par le simple contrat » — « C'est l'avis le plus répandu dans le "
         "madhhab » ; la rétractation rapportée avant sa mort va dans ce sens, et "
         "son propos du Muwaṭṭaʾ « est une preuve qu'il a entendu d'autres avis ». "
         "L'école adverse : al-Shāfiʿī « et d'autres savants ont estimé » que « le "
         "premier a le plus grand droit sur elle, que le second ait eu des "
         "relations avec elle ou non » — argument par « le verset général d'Allah "
         "le Très-Haut » (al-Baqarah, verset 226, le verset de l'īlāʾ) : le "
         "consensus sur le droit du premier s'il revient avant le remariage "
         "indique « la validité du retour (du premier mari) alors que l'épouse "
         "était ignorante de cela » ; si le retour est valide, elle est l'épouse du "
         "premier et « le mariage du second est dissous » — « C'est ce qui a été "
         "rapporté de ʿAlī »."),
        ("La clôture récolte le fil. La sagesse du divorce de l'épouse du disparu "
         "après recherche et délai : « d'éliminer tout préjudice, sous toutes ses "
         "formes et de tous les types, subi par l'épouse à cause de la disparition "
         "de son mari, et de garantir le droit de l'épouse à demander le divorce si "
         "elle subit un préjudice de la part de son mari. » L'exploitation (istithmār) "
         "imprime la procédure judiciaire d'an-Nafrāwī (al-Fawākhid al-Dawānī, 41/2) : "
         "le disparu « dont on connaît le lieu », hors famine et épidémie ; la "
         "requête exige « après avoir établi le mariage, la disparition du mari et "
         "la continuation de la protection légale jusqu'à ce jour » ; le juge « "
         "rédige un document contenant son nom, sa généalogie et sa description » et "
         "« l'envoie au juge du pays où on pense qu'il se trouve », ou « l'envoie au "
         "pays de rassemblement ». L'évaluation demande les cas des disparus et le "
         "statut de l'épouse de chacun, le statut de la divorcée rejointe en absence "
         "sans information jusqu'à son remariage, et la sagesse du divorce après "
         "recherche et délai. La préparation préalable annonce la leçon suivante : "
         "« Lis les hadiths de la leçon suivante et réponds à ce qui suit » — « "
         "Énonce le statut du divorce pendant les règles d'impureté (ḥayḍ). » — le "
         "divorce durant les menstrues et lʿidda des aqrāʾ, la seizième du livre."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (les règles de la ʿidda de l'épouse du "
         "disparu et le retour pendant l'absence ; les types de disparus et le "
         "statut de l'épouse de chacun ; la sagesse du divorce après le délai) → "
         "tamhīd (le préjudice interdit, l'effacement légal, le divorce comme "
         "remède du lésé) → quatre textes (n° 1819-1822)."),
        ("Le n° 1819 : l'attente de quatre ans puis « une ʿidda de quatre mois et "
         "dix jours » puis la libération — le propos de ʿUmar b. al-Khaṭṭāb "
         "rapporté de Yahyā b. Saʿīd et de Saʿīd b. al-Musayyib."),
        ("Le n° 1820 : après lʿidda, plus aucun droit sur elle, relations du "
         "premier ou non ; avant le remariage, « il a le plus grand droit sur "
         "elle »."),
        ("Les trois aspects du disparu : le lieu ignoré (le juge enquête, quatre "
         "ans, lʿidda de veuve, la libération ; l'option de la patiente sous la "
         "protection légale) ; le disparu au combat (jamais de mariage, elle et "
         "son patrimoine en suspens, l'âge de l'équivalent — soixante-dix ans, "
         "Ibn ʿĀsim dans al-Taḥfah) ; le disparu de la fitna (pas de délai, "
         "l'attente des fuyards et des vaincus, le délai du pays lointain)."),
        ("Les quatre ans et la divergence : « acte d'obéissance rituelle » "
         "('amr taʿabbudī) institué par ʿUmar et approuvé des Compagnons ; « la "
         "durée maximale d'une grossesse » ; « le délai maximal » de l'espérance "
         "de nouvelles à cette époque."),
        ("L'école de la certitude (al-Shāfiʿī, Abū Ḥanīfah et un groupe) : « son "
         "contrat est certainement valide, et il ne peut être levé que par "
         "certitude » — le rapport de ʿAlī (taqyīf) chez al-Bayhaqī (Sunan "
         "al-Kubrā) : la patience « jusqu'à ce que la certitude de sa mort lui "
         "parvienne »."),
        ("Le retour après lʿidda : avant remariage → le plus grand droit ; après → "
         "plus aucun droit si relations ; avant relations → le Muwaṭṭaʾ (plus "
         "aucun droit) contre la rétractation un an avant sa mort (le seul moyen "
         "de conserver le droit : des relations du second « sans savoir qu'il "
         "était vivant ») — Ibn al-Qāsim et al-Ashhab."),
        ("Le n° 1821 et ses deux sens : récusation de l'application (la cause de "
         "séparation ôte le droit au mahr) ou récusation de la narration "
         "(l'authenticité du propos attribué à ʿUmar)."),
        ("Le divorcé de l'absente (n° 1822) : la simple conclusion du mariage "
         "l'ôte au premier (rapporté de ʿUmar) contre la Mudawwana (la "
         "consommation requise — « l'avis le plus répandu dans le madhhab ») ; "
         "l'école adverse par le verset général (al-Baqarah 226) : le retour "
         "valide à l'insu de l'épouse, le second mariage dissous — rapporté de "
         "ʿAlī."),
        ("La sagesse et l'exploitation : éliminer tout préjudice de la disparition "
         "et garantir le droit de l'épouse au divorce ; la procédure d'an-Nafrāwī "
         "(al-Fawākhid al-Dawānī, 41/2) — les trois établissements préalables de "
         "la requête, le document du juge (nom, généalogie, description), l'envoi "
         "au pays supposé ou « au pays de rassemblement » ; la préparation "
         "annonce le divorce durant les règles et les aqrāʾ (leçon suivante)."),
    ],
    "vocabulaire": [
        {"ar": "المفقود", "translit": "al-mafqūd",
         "fr": "le disparu : « celui dont on perd la trace sans nouvelles de lui » — « Le disparu se présente sous trois aspects » : le lieu ignoré, le disparu au combat, le disparu au temps de la fitna"},
        {"ar": "العدة", "translit": "al-ʿidda",
         "fr": "la période d'attente : ici « une ʿidda de quatre mois et dix jours » — lʿidda de veuve — après l'attente de quatre ans de l'épouse du disparu ; le retour du mari pendant lʿidda maintient la conjugalité"},
        {"ar": "المراجعة", "translit": "al-murājaʿa",
         "fr": "le retour de l'absent vers son épouse : celui qui la revoit « sans l'en informer » et la trouve mariée à son retour — la seconde question de la leçon"},
        {"ar": "ايما", "translit": "ayyimā",
         "fr": "locution du texte d'ʿUmar — composée de « ayyu » (nom qui remplace une condition) et de « mā » (indéfini ajouté), « locution qui dispense d'un développement trop long ou inutile »"},
        {"ar": "العصمة", "translit": "al-ʿiṣma",
         "fr": "la protection légale du mari : l'épouse qui ne saisit pas le juge « reste sous sa protection légale jusqu'à ce que son sort se clarifie » ; sa continuation est l'une des conditions de la requête dans l'exploitation"},
        {"ar": "الفتنة", "translit": "al-fitna",
         "fr": "le trouble : le disparu au temps de la fitna n'a pas de délai — l'épouse patiente aussi longtemps que durent « les fuyards et les vaincus », puis accomplit sa ʿidda et se marie"},
        {"ar": "الاقراء", "translit": "al-aqrāʾ",
         "fr": "les périodes de pureté : lʿidda de la divorcée annoncée par la préparation préalable (leçon suivante) ; l'emplacement du verset est vide au scan — al-Baqara 228, reconstruction consignée"},
        {"ar": "المدونة", "translit": "al-Mudawwana",
         "fr": "le recueil malikite : elle requiert la consommation du second mari pour ôter la divorcée au premier, contre le Muwaṭṭaʾ (la simple conclusion du mariage) — « C'est l'avis le plus répandu dans le madhhab »"},
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
com[DOCID] = norme_entree(E_13101)

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
    ('13079 — la leçon précédente du registre (le liʿān)', 'liʿān' in fr('13079')),
    ('13074 — le khulʿ et son débat divorce/rupture', 'khulʿ' in fr('13074')),
    ('12925 — l’exploitation de L1 (al-Baqara 233, la kināya à lʿidda de veuvage)', '233' in fr('12925')),
    ('12971 — lʿīlāʾ, dont le verset général [al-Baqara 226] est l’argument du Shafiʿite', '226' in fr('12971')),
    ('13114 — la leçon suivante du registre (le divorce durant les règles)', 'menstrues' in fr('13114')),
    ('13101 — le mafqūd, sujet de la leçon', 'mafqūd' in corpus),
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
