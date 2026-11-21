#!/usr/bin/env python3
"""R774 — ajoute le commentaire pédagogique de la leçon 19 de hadith-tanawi-1
(13121 التفريق بين الزوجين للضرر و العيب — la séparation des époux pour
préjudice ou vice, « La séparation des époux pour préjudice ou vice
(at-tafrīq bayn az-zawjayn li-ḍ-ḍarar wa-l-ʿayb) » dans la traduction du
manuel, la dix-neuvième du livre, étiquetée « leçon 25 » par l'imprimé
(الدرس 25) — le SUIVANT de R773, 13117, annoncé dès R772/R773)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r773-c18.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~28 300 caractères débalisés ; couche
arabe lue pour le titre plein التفريق بين الزوجين للضرر و العيب من موطأ الإمام
مالك بشرح الزرقاني et l'étiquette de l'imprimé « (الدرس 25) »). Règle 2 de
LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ (1849, 1850, 1851,
1852, 1854, 1855), les attributions (ʿAlī ibn Abī Ṭālib, ʿAbdallāh ibn Masʿūd,
Saʿīd ibn al-Musayyab, Ibn Shihāb az-Zuhrī, Mālik, Bahrām le transmetteur de
la Mudawwana depuis Ibn al-Qāsim, Jābir ibn ʿAbdallāh, ash-Shāfiʿī, Aḥmad,
Abū Ḥanīfa, Ibn Rushd, al-Zarqānī), les références (an-Nisāʾ 35 ×5 ; al-Māʾida
1 ; an-Nasāʾī Sunan Kubrā ; Ibn Māja ; le commencement du mujtahid 3/117) sont
cités telles qu'elles figurent dans la leçon.

Garde-fous (convention des vagues R765-R773) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr débalisé de la leçon (convention :
  frontières de blocs -> espace, tags inline -> '') ;
- recoupements : ancres vérifiées dans les leçons voisines (13117 — la
  leçon précédente immédiate, dont la préparation annonçait la réconciliation
  en dispute, le divorce suspendu et les défauts ; 13122 — la leçon suivante
  du registre, objet de la préparation : le compte des divorces, le divorce
  du contraint, des deux en colère et des deux ivres ; 12966 — le corpus
  califal du ẓihār, où an-Nasāʾī fut déjà rencontré ; 12991 — la leçon de la
  dot, où al-Māʾida fut déjà rencontré ; 12957 — la leçon du banquet, où Ibn
  Rushd fut déjà rencontré ; 13121 — la leçon même, l'arbitrage et le
  ḥakamayn).

NB consignés sans correction (relevés à la lecture) :
- le titreAr du CMS est PLEIN ici (التفريق بين الزوجين للضرر و العيب من موطأ
  الإمام مالك بشرح الزرقاني) — contrairement à 13117 dont il était tronqué ;
- l'étiquette de l'imprimé « (الدرس 25) » pour la dix-neuvième du livre —
  écart du fil, comme les précédentes (13117 = leçon 24 pour la dix-huitième) ;
- la couche arabe écrit les deux gloses du lexique « أثم: أي حنث. اعترض:
  منعه عن الوطء مانع » — le lexique français porte « athima » et
  « iʿtaraḍa ʾanhā » ;
- le verset 4:35 est recopié IN EXTENSO à CINQ emplacements de la leçon —
  et une sixième fois dans l'exploitation avec guillemets anglais ;
- 0 écart d'étiquetage coranique nouveau (4:35 ×5 et 5:1 ×1 concordants) —
  le registre demeure 49 écarts cumulés ;
- coquille du texte final « La asymétrie du chapitre » pour « L'asymétrie ».
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13121'

E_13121 = {
    "auteur": "IA-1, tour R774",
    "resume": (
        "Guide de lecture de la leçon 19 (التفريق بين الزوجين للضرر و العيب من موطأ الإمام مالك بشرح الزرقاني — la "
        "séparation des époux pour préjudice ou vice du livre de hadith du Muwaṭṭaʾ de l'imam Mālik avec le "
        "commentaire de l'imam al-Zarqānī ; la traduction du manuel porte « La séparation des époux pour "
        "préjudice ou vice (at-tafrīq bayn az-zawjayn li-ḍ-ḍarar wa-l-ʿayb) »), la dix-neuvième du livre, "
        "étiquetée leçon 25 par l'imprimé (الدرس 25) : trois documents du Muwaṭṭaʾ portent la matière — le n° 1849 "
        "est le pilier : le dire dʿAlī ibn Abī Ṭālib au sujet des deux arbitres dont Allah — le Très-Bienheureux "
        "et le Très-Élevé — a parlé, qui recopie le verset de l'envoi — « Si vous craignez le désaccord entre les "
        "deux [époux], envoyez alors un arbitre de sa famille à lui, et un arbitre de sa famille à elle. Si les "
        "deux veulent la réconciliation, Allah rétablira l’entente entre eux. Allah est certes, Omniscient et "
        "Parfaitement Connaisseur. » [la sourate an-Nisāʾ, verset 35] — et le scelle par la formule consacrée : "
        "« à eux la séparation entre les deux et le rassemblement. » ; le n° 1852 est le dire dʿAbdallāh ibn "
        "Masʿūd au sujet de celui qui dit « toute femme que j’épouse est répudiée » : « s’il ne nomme ni tribu, "
        "ni femme en particulier, il n’a rien contre lui. » — que Mālik honore de son sceau : « et cela est la "
        "meilleure chose que j’aie entendue. » ; les n° 1854 et 1855 courent d'Ibn Shihāb az-Zuhrī jusqu'à Saʿīd "
        "ibn al-Musayyab — « quiconque épouse une femme et ne peut la toucher, un délai d’une année lui est fixé "
        "; s’il la touche — sinon, les deux seront séparés. » — et portent l'interrogation de Mālik lui-même : "
        "« quand lui est fixé le délai — du jour où il pénètre en elle, ou du jour où elle saisit l’autorité ? » "
        "réponse : « mais du jour où elle saisit l’autorité. » — puis le second dire de Mālik : « quant à celui "
        "qui a touché sa femme, puis en a été empêché, je n’ai point entendu qu’un délai lui soit fixé, ni que "
        "les deux soient séparés. » Le préambule fonde le tout : lorsque le désaccord s'aggrave et que l'on "
        "craint la mésentente (shiqāq) portée au degré interdit, la Loi institue entre les deux l'arbitrage "
        "(taḥkīm) — « l’envoi de deux arbitres des deux familles qui œuvrent à réparer ce qui s’est rompu entre "
        "les deux — la réconciliation des parties (iṣlāḥ dhāt al-bayn) — par l’exhortation et ce qui la suit » ; "
        "l'arbitrage conjugal « est le dernier rempart avant la dissolution, le lieu où la famille élargie "
        "reprend le mariage qu’elle avait conclu et témoin ». La leçon précédente a réglé le compte de "
        "la retraite de celle qui ne menstrue point ; celle-ci descend le dernier versant du chapitre : que "
        "devient le mariage lorsque la mésentente résiste à toutes les manières de la réconciliation, que valent "
        "les paroles qui suspendent le divorce au mariage lui-même, et quels sont les défauts (ʿuyūb) qui "
        "autorisent l'épouse à demander la séparation lorsque le mariage ne peut accomplir son dessein. "
        "Première partie — la séparation des époux pour la mésentente. Le verset de l'envoi porte « trois "
        "précautions qui dessinent tout le régime » : l'envoi d'abord (« il répond à un désaccord réel, aggravé "
        "et persistant »), la provenance ensuite (« celui qui connaît les états intérieurs est le plus à même de "
        "les apaiser »), la condition de la réussite enfin (« la réconciliation des cœurs est un secours divin "
        "placé dans des mains sincères »). Les jurisconsultes ont différé sur la mission des deux arbitres, et "
        "la cause du désaccord "
        "remonte à leur qualification juridique : « sont-ils députés du juge (nāʾibān ʿan al-ḥākim), ou "
        "mandataires des époux (wakīlān ʿan az-zawjayn) ? » Les Mālikites et les Shāfiʿītes — dans un dire — "
        "soutiennent que l'obligation des deux arbitres est la réparation d'abord, puis la séparation sans mandat "
        "des époux ; leur preuve est le dire dʿAlī — « à eux la séparation entre les deux et le rassemblement » — "
        "et le compilé de Mālik au n° 1850 : « les deux arbitres peuvent prononcer entre l’homme et sa femme la "
        "séparation et le rassemblement » — « la mission des arbitres embrasse les deux issues, non la seule "
        "maison de la réconciliation ». Les "
        "Ḥanafites, les Ḥanbalites et les Shāfiʿītes — dans un autre dire — soutiennent que la mission est la "
        "réparation seule, la séparation exigeant le mandat des époux ; leur preuve est le dialogue dʿAlī avec "
        "l'homme récalcitrant, rapporté par an-Nasāʾī dans la grande collection des Sunan : « tu as menti, par "
        "Dieu : tu ne partiras point tant que tu n’auras point accepté ce que j’ai accepté ». L'école mālikite "
        "répond par l'apparent du Coran : les destinataires du verset « sont les juges et les émirs » — le "
        "jugement des arbitres « est de l’ordre du jugement, non de l’ordre du mandat » — « et le juge n’a point "
        "besoin, dans le divorce qu’il fait tomber, de l’autorisation du mari ». Des conditions "
        "des deux arbitres : qu'ils soient des familles des deux époux s'il s'y trouve qui soit capable, sinon "
        "d'autres qu'eux — « la famille qui avait témoigné le mariage reprend la plume pour le sauver avant que "
        "le juge ne la prenne pour le dissoudre ». Deuxième partie — le statut du divorce suspendu à la condition "
        "du mariage. L'accord de base "
        ": « le divorce ne se produit que sur les femmes qui sont dans l’inviolabilité de leurs maris, ou avant "
        "que n’expire leur retraite dans le divorce révocable — et qu’il ne se produit point sur les femmes "
        "étrangères au lien (al-aʿānib) ». Trois écoles sur la suspension à l'étrangère — « si j’épouse telle, "
        "elle est répudiée » : ash-Shāfiʿī, Aḥmad et un groupe — point de suspension du tout, par « point de "
        "divorce avant le mariage » de Jābir ibn ʿAbdallāh rapporté par Ibn Māja ; Abū Ḥanīfa — obligatoire "
        "absolument, par la parole collective des Médinois du n° 1851 : « si l’homme jure du divorce de la femme "
        "avant de l’épouser, puis entre en rupture de serment, cela l’oblige lorsqu’il l’épouse » ; les Mālikites "
        "distinguent : la généralisation ne l'oblige point — « la parole qui ferme la porte que Dieu a ouverte "
        "ne lie point en droit, elle n’engage que en péché » — et la particularisation l'oblige, par l'implicite "
        "du n° 1852 et « quiconque conclut un contrat auquel il n’est point inapte — le contrat lui est "
        "obligatoire » (al-Māʾida 1). Et les réponses : aux Ḥanafites, « le particulier tient la général sur la "
        "borne de son sens » ; aux Shāfiʿītes, « la suspension n’est point une production, elle est un lien qui "
        "attend son objet, et l’arrivée de l’objet engage le lien ». Troisième partie — la répudiation pour "
        "défaut. Si un empêchement "
        "s'est dressé, « l’épouse est mise en choix de demeurer avec lui ou de s’en séparer, après avoir élevé "
        "son affaire au juge » — « la séparation ne se prononce point sur la rumeur du défaut, mais sur sa preuve "
        "devant l’autorité ». Deux espèces d'empêchements : le jabb — « l’amputation du membre et des deux "
        "testicules » — dont « son cas n’est point ajourné, car il n’y a point d’intérêt à l’ajournement — la "
        "certitude de l’impossibilité dispense de l’attente » ; et l'iʿtirāḍ — « l’incapacité de la pénétration "
        "pour une cause qui peut se lever » — ajourné « une année : s’il guérit dans l’année — sinon, les deux "
        "seront séparés, si elle le veut », d'après le n° 1854 ; « l’année fut son terme pour que passent sur lui "
        "les quatre saisons ». Le point de départ : « du jour où elle saisit l’autorité » (n° 1855) — et, en cas "
        "d'accord sans procès, du jour de l'accord — Bahrām : « la procédure judiciaire fixe le point de départ, "
        "et l’accord amiable en fixe un autre ». Le second dire du n° 1855 — celui qui a touché puis été "
        "empêché : « je n’ai point entendu qu’un délai lui soit fixé, ni que les deux soient séparés » — « le "
        "défaut qui était présent à l’entrée dans le mariage » fonde la demande de séparation, « l’empêchement "
        "qui survient après la consommation » relève d’autres régimes — « la leçon du divorce avant consommation "
        "et du divorce du malade en prolongera la doctrine ». L'exploitation scelle par Ibn Rushd — le "
        "commencement du mujtahid, "
        "tome 3/117 — « quatre accords et une divergence » : la légalité de l'envoi (« l’arbitrage est une "
        "institution coranique, non une coutume tolérée »), la provenance familiale, la suspension de "
        "l'exécution en cas de désaccord des arbitres, la force du rassemblement sans mandat — et la divergence "
        "sur la séparation : « faut-il une permission du mari, ou n’en faut-il point ? » L'asymétrie du chapitre "
        "est sa morale : « le rassemblement court sans mandat, la séparation court sous conditions — la Loi a "
        "rendu la porte de la réparation plus large que la porte de la dissolution » : « le dernier mot du "
        "ménage appartient à la réconciliation, la séparation n’arrive que lorsque toutes les voies se sont "
        "fermées l’une après l’autre. » La préparation "
        "ouvre la leçon suivante (13122) : « Clarifier comment on compte le nombre des divorces. » et « Indiquer "
        "le statut du divorce du contraint, des deux en colère et des deux ivres. » Les notes du traducteur : six "
        "emplacements de versets en image, tous vides au scan ; les références imprimées — « la sourate an-Nisāʾ, "
        "verset 35 » à cinq emplacements et « la sourate al-Māʾida, verset 1 » à un — « références TOUTES "
        "concordantes au cache coranique » ; « 0 écart d’étiquetage nouveau — le registre demeure 49 écarts "
        "cumulés » ; les chaînes — le n° 1849 par la voie du « il est parvenu », la formule du Muwaṭṭaʾ pour les "
        "dits largement circulés, jusqu'à ʿAlī ibn Abī Ṭālib, le quatrième calife, cousin et gendre du Prophète "
        "; les n° 1854-1855 par Ibn Shihāb az-Zuhrī jusqu'à Saʿīd ibn al-Musayyab, le prince des Successeurs "
        "médinois ; et l'exploitation porte Ibn Rushd, l'abrégé comparatif des écoles, déjà "
        "rencontré."
    ),
    "explication": [
        "La leçon 19 succède au recueil de la retraite (leçon 18) et referme le chapitre du divorce par son dernier "
        "versant : la précédente réglait le compte de la retraite et la reprise qui démolit le compte ; celle-ci "
        "traite ce que la retraite ne peut "
        "plus sauver — le mariage que la mésentente résiste à réparer. La vingt-cinquième leçon de l'imprimé "
        "(الدرس 25) annonce trois objectifs : « Reconnaître les règles des défauts qui requièrent la séparation "
        "des époux, et par quoi ils s’établissent », « Distinguer les défauts qui requièrent la séparation des "
        "époux », « Saisir les voies de la réconciliation entre les époux » — la réconciliation d'abord, la "
        "séparation ensuite : l'ordre même des objectifs dessine la morale du chapitre.",
        "Le préambule institue l'arbitrage comme institution, non comme artifice : « Lorsque le désaccord s’aggrave "
        "entre les deux époux, que leur affaire s’obscurcit, que nul ne sait lequel des deux a mal agi, et que "
        "l’on craint la mésentente (shiqāq) portée au degré qui conduit à ce qu’Allah a interdit de désobéissance "
        "et d’injustice, la Loi institue entre les deux l’arbitrage (taḥkīm) ». Trois conditions d'ouverture — le "
        "désaccord aggravé, l'obscurcissement des torts, la crainte du degré interdit — et une procédure : « l’"
        "envoi de deux arbitres des deux familles qui œuvrent à réparer ce qui s’est rompu entre les deux — la "
        "réconciliation des parties (iṣlāḥ dhāt al-bayn) — par l’exhortation et ce qui la suit ». Le commentaire "
        "de la traduction en donne la portée : « il est le dernier rempart avant la dissolution, le lieu où la "
        "famille élargie reprend le mariage qu’elle avait conclu et témoin » — et la formule finale du préambule "
        "porte tout le régime : le lien conjugal « ne se brise point par la fatigue d’un jour ni par la colère "
        "d’une nuit, mais par une décision posée, entourée de précautions, rendue après examen des deux côtés ».",
        "Le verset d'an-Nisāʾ 35 — recopié in extenso par la leçon à cinq emplacements, sixième fois dans "
        "l'exploitation — porte « trois précautions qui dessinent tout le régime ». L'envoi d'abord : « l’"
        "arbitrage ne se décrète point dès le premier différend, il répond à un désaccord réel, aggravé et "
        "persistant ». La provenance ensuite : « un arbitre de la famille de chacun des deux — celui qui connaît "
        "les états intérieurs est le plus à même de les apaiser ». La condition de la réussite enfin : « Si les "
        "deux veulent la réconciliation, Allah rétablira l’entente entre eux » — « la sincérité de l’intention est le moyen "
        "de la réussite, non la seule procédure : la réconciliation des cœurs est un secours divin placé dans des "
        "mains sincères ». La doctrine du chapitre est ainsi posée avant toute divergence : la procédure ne "
        "produit point la réconciliation, elle la reçoit.",
        "La grande question d'école est la qualification juridique des arbitres : « sont-ils députés du juge "
        "(nāʾibān ʿan al-ḥākim), ou mandataires des époux (wakīlān ʿan az-zawjayn) ? » — et « chaque doctrine en "
        "découle mécaniquement ». Les Mālikites et les Shāfiʿītes — dans un dire — tiennent la réparation "
        "d'abord, puis la séparation sans mandat ; le juge homologue leur accord « fût-elle contraire à son "
        "propre effort d’interprétation » ; leur preuve est le dire dʿAlí du n° 1849 — « à eux la séparation "
        "entre les deux et le rassemblement » — et le compilé de Mālik au n° 1850 : « et cela est la meilleure "
        "chose que j’aie entendue des gens de la science : les deux arbitres peuvent prononcer entre l’homme et "
        "sa femme la séparation et le rassemblement » — « le dire de ʿAlī met la séparation et le rassemblement "
        "dans la même main, et la parole de Mālik (مَالِك) en fait la doctrine des gens de la science tout "
        "entière : la mission des arbitres embrasse les deux issues, non la seule maison de la réconciliation ».",
        "Les Ḥanafites, les Ḥanbalites et les Shāfiʿītes — dans un autre dire — tiennent la réparation seule : si "
        "elle échappe, « la séparation ne leur est point permise, sauf que les deux époux leur en délèguent le "
        "pouvoir ». Leur preuve est le dialogue dʿAlī avec l'homme récalcitrant, rapporté par an-Nasāʾī dans la "
        "grande collection des Sunan : « es-tu satisfait de ce que les deux ont jugé ? » — « non ; mais je "
        "serais satisfait qu’ils rassemblent, et non satisfait qu’ils séparent. » — « tu as menti, par Dieu : tu "
        "ne partiras point tant que tu n’auras point accepté ce que j’ai accepté » — dont la leçon tire : « Cela "
        "dénote que les deux arbitres ne séparent point sinon avec la satisfaction du mari : le jugement n’"
        "arrache point le lien conjugal contre la volonté de celui qui le détient, tant que la Loi ne l’a point "
        "dissous elle-même ». La doctrine mālikite répond par l'apparent du Coran : « les savants se sont "
        "accordés » que les destinataires du verset « sont les juges et les émirs » — « cela dénote que le "
        "jugement des deux arbitres est de l’ordre du jugement, non de l’ordre du mandat » — et le Coran les a "
        "même nommés « deux arbitres » (ḥakamayn) « à l’expression claire » : « et le juge n’a point besoin, "
        "dans le divorce qu’il fait tomber, de l’autorisation du mari » — la formule d'al-Zarqānī transpose aux "
        "arbitres le régime du juge : l'inviolabilité conjugale se lève par l'autorité publique quand elle ne "
        "se répare plus par la famille.",
        "Des conditions des deux arbitres : « qu’ils soient des familles des deux époux — l’un des familles du "
        "mari, l’autre des familles de l’épouse — s’il se trouve dans leurs familles qui soit capable de cela ; "
        "sinon, on envoie d’autres qu’eux. » Et la sagesse de la provenance se déplie en trois raisons : « les "
        "proches sont plus savants des états intérieurs des deux époux, plus demandeurs de leur réconciliation, "
        "et les âmes des époux leur sont plus paisibles » — ils « dévoilent alors ce que gardent leurs poitrines "
        "d’amour et de haine » — et la phrase qui scelle : « la famille qui avait témoigné le mariage reprend la "
        "plume pour le sauver avant que le juge ne la prenne pour le dissoudre. » La connaissance privée sert le "
        "droit public : la famille sait ce que le juge ne peut interroger.",
        "La deuxième partie traite le divorce suspendu (al-muʿallaq) à la condition du mariage. L'accord de base "
        ": « le divorce ne se produit que sur les femmes qui sont dans l’inviolabilité de leurs maris, ou avant "
        "que n’expire leur retraite dans le divorce révocable — et qu’il ne se produit point sur les femmes "
        "étrangères au lien (al-aʿānib) ». Le débat porte sur la suspension à l'étrangère : « comme de dire : "
        "« si j’épouse telle, elle est répudiée », puis il l’épouse » — et « les savants ont trois écoles en "
        "cela ». ash-Shāfiʿī, Aḥmad et un groupe : point de suspension du tout, par « point de divorce avant le "
        "mariage » de Jābir ibn ʿAbdallāh rapporté par Ibn Māja — « la suspension à une femme non encore épousée "
        "place le divorce avant son objet, et l’objet est la condition de la validité ». Abū Ḥanīfa : « le "
        "divorce l’oblige absolument, qu’il ait généralisé toutes les femmes ou particularisé », par la parole "
        "collective des Médinois du n° 1851 : « si l’homme jure du divorce de la femme avant de l’épouser, puis "
        "entre en rupture de serment, cela l’oblige lorsqu’il l’épouse » — « le serment prononcé sur le divorce "
        "porte sa charge, et l’épouse encaisse ce que la langue a posé ».",
        "Les Mālikites distinguent : « la généralisation de toutes les femmes ne l’oblige point, et la "
        "particularisation l’oblige » — exemple de la première : « toute femme que j’épouse est répudiée » ; "
        "exemple de la seconde : « toute femme que j’épouse d’une telle tribu, ou d’une telle ville, est "
        "répudiée » — « à plus forte raison s’il dit : « si j’épouse telle, elle est répudiée » ». Leur preuve "
        "est le n° 1852 — « s’il ne nomme ni tribu, ni femme en particulier, il n’a rien contre lui » — « et son "
        "implicite (mafhūmuhu) est que s’il désigne une femme en particulier, ou nomme une tribu, ou une ville, "
        "le divorce est sur lui ». Du côté du sens : « il n’est point inapte (ʾāṣin) dans ce contrat, et "
        "quiconque conclut un contrat auquel il n’est point inapte — le contrat lui est obligatoire, et il lui "
        "incombe de s’en acquitter », par al-Māʾida 1. Et la généralisation est désobéissance : « car il vise à "
        "s’interdire le mariage qu’Allah lui a rendu licite — son contrat ne se réalise donc point » — « la "
        "parole qui ferme la porte que Dieu a ouverte ne lie point en droit, elle n’engage que en péché ». Puis "
        "les deux réponses : aux Ḥanafites, la parole collective des Médinois est portée par la particularisation "
        "d'Ibn Masʿūd — « le particulier tient la général sur la borne de son sens » ; aux Shāfiʿītes, « le débat "
        "porte sur son obligation après le mariage » : « la suspension n’est point une production, elle est un "
        "lien qui attend son objet, et l’arrivée de l’objet engage le lien ». La signature mālikite est de "
        "nouveau la borne du particulier — déjà rencontrée aux leçons de la retraite : la parole ne lie point là "
        "où elle vise l'impossible, elle lie là où elle vise le déterminé.",
        "La troisième partie — la répudiation pour défaut. Si un empêchement s'est dressé, « l’épouse est mise "
        "en choix de demeurer avec lui ou de s’en séparer, après avoir élevé son affaire au juge ; et il la "
        "répudie d’après lui après l’établissement du défaut » — « la séparation ne se prononce point sur la "
        "rumeur du défaut, mais sur sa preuve devant l’autorité ». Les empêchements sont de deux espèces, "
        "réparties par l'espérance : le jabb — « l’amputation du membre et des deux testicules » — « celui-là, "
        "son cas n’est point ajourné, car il n’y a point d’intérêt à l’ajournement — la certitude de "
        "l’impossibilité dispense de l’attente, et le délai n’a de sens que là où demeure une espérance » ; "
        "l'iʿtirāḍ — « l’incapacité de la pénétration pour une cause qui peut se lever » — « celui-là, son cas "
        "est ajourné ; et l’avis de la majorité des jurisconsultes est qu’il est ajourné une année : s’il guérit "
        "dans l’année — sinon, les deux seront séparés, si elle le veut », d'après le n° 1854. Et la sagesse du "
        "terme : « l’année fut son terme pour que passent sur lui les quatre saisons ; car le remède touche "
        "parfois une saison et non une autre — la santé du corps suit les temps de l’année, et l’attente fait le "
        "tour de chaque saison avant que le corps ne soit prononcé incurable » — la doctrine attend le corps "
        "avant de le dissoudre.",
        "Le point de départ du délai : « le commencement de l’année en cela est du jour où son épouse l’élève à "
        "l’autorité » — et cela n'obtient le jugement qu'après « l’aveu du mari, ou l’établissement de ce qui "
        "l’oblige » — « quand donc ce qui oblige à fixer le délai s’établit chez le juge, le délai recommence à "
        "se compter du jour de l’exécution du jugement » — d'après l'interrogation de Mālik à Ibn Shihāb et sa "
        "réponse : « mais du jour où elle saisit l’autorité » (n° 1855). Et « quant à s’ils ne saisissent point "
        "l’autorité et se mettent d’accord sur cela, alors du jour de l’accord — comme l’a dit Bahrām, le "
        "transmetteur de la Mudawwana depuis Ibn al-Qāsim : la procédure judiciaire fixe le point de départ, et "
        "l’accord amiable en fixe un autre — chaque voie porte son propre temps » : la procédure et l'amiable "
        "ont chacun leur horloge. Le second dire du n° 1855 scelle la borne du régime : « quant à celui qui a "
        "touché sa femme, puis en a été empêché, je n’ai point entendu qu’un délai lui soit fixé, ni que les "
        "deux soient séparés » — « la doctrine distingue le défaut qui était présent à l’entrée dans le mariage "
        "— et qui fonde la demande de séparation, le mariage n’ayant point accompli son dessein — et "
        "l’empêchement qui survient après la consommation, et qui relève d’autres régimes que celui-ci » — « la "
        "leçon du divorce avant consommation et du divorce du malade en prolongera la doctrine ».",
        "L'exploitation scelle par Ibn Rushd — « le commencement du mujtahid, tome 3/117 », l'abrégé comparatif "
        "des écoles, déjà rencontré à la leçon du banquet — « quatre accords et une divergence » : « les savants "
        "se sont accordés sur la licéité de l’envoi des deux arbitres lorsque la dispute s’est produite entre "
        "les deux époux » — « l’arbitrage est une institution coranique, non une coutume tolérée » ; l'accord "
        "sur la provenance familiale — « et ils se sont accordés que les deux arbitres ne peuvent être que des "
        "familles des deux époux » ; l'accord sur la suspension de l'exécution — « et ils se sont accordés que "
        "les deux arbitres, s’ils diffèrent, leur parole ne s’exécute point » — « deux jugements contraires ne "
        "peuvent s’exécuter ensemble, la mésentente des arbitres renvoie l’affaire au juge » ; l'accord sur la "
        "force du rassemblement — « et ils se sont accordés que leur parole au rassemblement entre les deux "
        "s’exécute sans mandat des deux époux » — « réparer n’exige point de pouvoir sur autrui, le "
        "rassemblement est la voix naturelle de la famille » ; et la divergence : « et ils ont différé sur la "
        "séparation prononcée par les deux arbitres entre eux s’ils s’accordent sur cela : faut-il une "
        "permission du mari, ou n’en faut-il point ? » — précisément la question des députés et des mandataires "
        "que l'analyse a traversée. L'asymétrie du chapitre est sa morale : « le rassemblement court sans "
        "mandat, la séparation court sous conditions — la Loi a rendu la porte de la réparation plus large que "
        "la porte de la dissolution, et l’a voulu ainsi : le dernier mot du ménage appartient à la "
        "réconciliation, la séparation n’arrive que lorsque toutes les voies se sont fermées l’une après "
        "l’autre. » La préparation ouvre la leçon suivante (13122) : le compte des divorces, le divorce du "
        "contraint, des deux en colère et des deux ivres. Les notes du traducteur consignent les six "
        "emplacements de versets en image tous vides au scan et la mention du jugement de Mālik « la formule "
        "d’appréciation (taʿdīl) par laquelle l’école scelle une doctrine ».",
    ],
    "points": [
        "Fil du livre : après le recueil de la retraite (leçon 18), le chapitre du divorce descend son dernier "
        "versant — la mésentente qui résiste à la réconciliation, le divorce suspendu au mariage, les défauts "
        "qui requièrent la séparation ; la leçon est la dix-neuvième du livre, étiquetée leçon 25 par l'imprimé "
        "(الدرس 25).",
        "Le préambule : la Loi institue l'arbitrage (taḥkīm) « entre les deux » quand la mésentente (shiqāq) est "
        "portée au degré interdit — « le dernier rempart avant la dissolution », la famille qui avait témoigné "
        "le mariage « reprend le mariage qu’elle avait conclu et témoin ».",
        "Le n° 1849 : le dire dʿAlī ibn Abī Ṭālib sur les deux arbitres — le verset d'an-Nisāʾ 35 recopié in "
        "extenso et la formule « à eux la séparation entre les deux et le rassemblement. » — le pilier de la "
        "doctrine mālikite de la séparation pour mésentente.",
        "Le verset porte « trois précautions qui dessinent tout le régime » : l'envoi d'abord (désaccord réel, "
        "aggravé, persistant), la provenance ensuite (un arbitre de chaque famille), la condition de la "
        "réussite enfin — « la réconciliation des cœurs est un secours divin placé dans des mains sincères ».",
        "La grande divergence : les arbitres sont-ils « députés du juge (nāʾibān ʿan al-ḥākim), ou mandataires "
        "des époux (wakīlān ʿan az-zawjayn) ? » — Mālikites et Shāfiʿītes (un dire) : réparation puis séparation "
        "sans mandat, par le n° 1849 et le n° 1850 ; Ḥanafites, Ḥanbalites et Shāfiʿītes (autre dire) : "
        "réparation seule, séparation sur mandat, par le dialogue dʿAlī rapporté par an-Nasāʾī.",
        "La réponse mālikite : les destinataires du verset « sont les juges et les émirs » — le jugement des "
        "arbitres « est de l’ordre du jugement, non de l’ordre du mandat » ; le Coran les nomme « deux arbitres » "
        "(ḥakamayn) — « et le juge n’a point besoin, dans le divorce qu’il fait tomber, de l’autorisation du "
        "mari ».",
        "Conditions et sagesse des arbitres : familles des deux époux s'il s'y trouve qui soit capable, sinon "
        "d'autres ; « les proches sont plus savants des états intérieurs », plus demandeurs de la "
        "réconciliation, âmes plus paisibles — la famille témoigne le mariage puis le sauve.",
        "Le divorce suspendu : l'accord — il ne se produit que sur l'épouse en inviolabilité ou en retraite "
        "révocable, point sur les étrangères au lien (al-aʿānib) ; trois écoles — ash-Shāfiʿī et Aḥmad (point de "
        "suspension, par « point de divorce avant le mariage », Ibn Māja), Abū Ḥanīfa (obligatoire absolument, "
        "par le n° 1851), les Mālikites (généralisation non liante — désobéissance ; particularisation liante, "
        "par l'implicite du n° 1852 et al-Māʾida 1).",
        "Les deux réponses mālikites : aux Ḥanafites — « le particulier tient la général sur la borne de son "
        "sens » ; aux Shāfiʿītes — « la suspension n’est point une production, elle est un lien qui attend son "
        "objet » ; la signature de l'école : la parole ne lie point là où elle vise l'impossible, elle lie là "
        "où elle vise le déterminé.",
        "La répudiation pour défaut : l'épouse « mise en choix » après le juge — « la séparation ne se prononce "
        "point sur la rumeur du défaut, mais sur sa preuve devant l’autorité » ; deux espèces par l'espérance : "
        "le jabb (point d'ajournement — la certitude de l'impossibilité), l'iʿtirāḍ (une année — les quatre "
        "saisons, « le remède touche parfois une saison et non une autre »).",
        "Le point de départ du délai : « du jour où elle saisit l’autorité » (n° 1855, l'interrogation de Mālik "
        "à Ibn Shihāb) ; en cas d'accord sans procès, du jour de l'accord — Bahrām, transmetteur de la "
        "Mudawwana depuis Ibn al-Qāsim : « la procédure judiciaire fixe le point de départ, et l’accord amiable "
        "en fixe un autre ».",
        "Le second dire du n° 1855 : touché puis empêché — « je n’ai point entendu qu’un délai lui soit fixé, "
        "ni que les deux soient séparés » — le défaut présent à l'entrée fonde la séparation, l'empêchement "
        "après consommation relève d'autres régimes (le divorce avant consommation, le divorce du malade).",
        "L'exploitation (Ibn Rushd, le commencement du mujtahid 3/117) : quatre accords et une divergence — "
        "l'asymétrie du chapitre est sa morale : « le rassemblement court sans mandat, la séparation court sous "
        "conditions » — « le dernier mot du ménage appartient à la réconciliation » ; la préparation ouvre "
        "13122 (le compte des divorces, le divorce du contraint, des deux en colère et des deux ivres).",
    ],
    "vocabulaire": [
        {"ar": "التحكيم", "translit": "taḥkīm",
         "fr": "l'arbitrage : l'institution coranique de l'envoi de deux arbitres quand la mésentente résiste — "
               "« la Loi institue entre les deux l’arbitrage (taḥkīm) » ; « le dernier rempart avant la "
               "dissolution », fondé sur an-Nisāʾ 35"},
        {"ar": "الشقاق", "translit": "shiqāq",
         "fr": "la mésentente : « la mésentente (shiqāq) portée au degré qui conduit à ce qu’Allah a interdit de "
               "désobéissance et d’injustice » — son aggravation ouvre la procédure de l'arbitrage"},
        {"ar": "الحكمين", "translit": "ḥakamayn",
         "fr": "les deux arbitres : le Coran les nomme « deux arbitres » (ḥakamayn) « à l’expression claire » — "
               "nomination qui fonde la doctrine des députés du juge : leur jugement « est de l’ordre du "
               "jugement, non de l’ordre du mandat »"},
        {"ar": "الإصلاح", "translit": "al-iṣlāḥ",
         "fr": "la réconciliation : « la réconciliation des parties (iṣlāḥ dhāt al-bayn) » — la mission première "
               "des arbitres, « par l’exhortation et ce qui la suit » ; « Si les deux veulent la réconciliation, "
               "Allah rétablira l’entente entre eux »"},
        {"ar": "المعلق", "translit": "al-muʿallaq",
         "fr": "le divorce suspendu : la parole qui suspend le divorce au mariage — « la suspension n’est point "
               "une production, elle est un lien qui attend son objet, et l’arrivée de l’objet engage le lien »"},
        {"ar": "أثم", "translit": "athima",
         "fr": "« il est entré en rupture de serment (ḥanatha) » : « l’homme a violé le serment qu’il avait "
               "prononcé, et il en porte la charge de la rupture de serment » — le terme du lexique de la leçon"},
        {"ar": "اعترض", "translit": "iʿtaraḍa",
         "fr": "« il en a été empêché » : « une cause s’est dressée entre lui et l’accomplissement du rapport "
               "conjugal, et le retient de la pénétration » — le cas de l'iʿtirāḍ, ajourné une année"},
        {"ar": "الوكيل", "translit": "wakīlān",
         "fr": "les mandataires : la doctrine qui tient les arbitres pour « mandataires des époux "
               "(wakīlān ʿan az-zawjayn) » — leur séparation exige le mandat, contre les députés du juge "
               "(nāʾibān ʿan al-ḥākim)"},
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
com[DOCID] = norme_entree(E_13121)

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
    ('13117 — la leçon précédente immédiate (la préparation annonçait réconciliation, divorce suspendu, défauts)', 'dispute' in fr('13117') and 'suspendu' in fr('13117')),
    ('13122 — la leçon suivante du registre (le compte des divorces, le contraint, les deux en colère et les deux ivres)', 'contraint' in fr('13122') and 'ivres' in fr('13122')),
    ('12966 — le corpus califal du ẓihār, où an-Nasāʾī fut déjà rencontré', 'ẓihār' in fr('12966') and 'Nasāʾī' in fr('12966')),
    ('12991 — la leçon de la dot, où al-Māʾida fut déjà rencontré', 'Māʾida' in fr('12991') and 'dot' in fr('12991')),
    ('12957 — la leçon du banquet, où Ibn Rushd fut déjà rencontré', 'Rushd' in fr('12957') and 'banquet' in fr('12957')),
    ('13121 — la leçon même (le taḥkīm et le ḥakamayn)', 'taḥkīm' in corpus and 'ḥakamayn' in corpus),
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
