#!/usr/bin/env python3
"""R776 — ajoute le commentaire pédagogique de la leçon 21 de hadith-tanawi-1
(13124 عدة المتوفى عنها زوجها — la viduité de la femme dont l'époux est
décédé, « La viduité de la femme dont l'époux est décédé (ʿiddat
al-mutawaffā ʿanhā zawjuhā) » dans la traduction du manuel, la vingt-unième
du livre, étiquetée leçon 24 par la couche du CMS (الدرس 24) — concordante au
badge imprimé الدرس 24 (page 132 du PDF) — le SUIVANT de R775, 13122, annoncé
par sa préparation) à content/commentaires/hadith-tanawi-1.json.

ÉTAPE PRÉLIMINAIRE — RECTIFICATION DU REGISTRE DES ÉCARTS D'ÉTIQUETAGE :
le comptage canonique est celui de la chaîne de traduction (commits d'octobre
2026) : n°44-46 (13114), n°47-49 (13117), n°50-52 (13124 — 2:232 imprimé ×3 →
2:234), n°53-54 (13136 — 2:232→2:234 et 2:238→2:240), n°55 (13624 — 2:231→
2:233) — cumul canonique 55. L'entrée R775 avait numéroté la divergence
« verset 227 » de 13122 « 50ᵉ écart » par collision avec le cumul du worklog
(49 à R774) — le rang 50 était déjà pris. Rectification : la divergence 227
(une divergence d'étiquette, répétée à trois emplacements) occupe les rangs
56ᵉ-58ᵉ ; le TEXTE ÉDITORIAL du commentaire 13122 est corrigé en conséquence
(notre propre texte, non le corpus — aucune modification des données de
leçon).

Même protocole que comm-r775-c20.py : normalisation de la ponctuation FR,
rédaction d'après la lecture complète de la leçon (htmlFr intégral, ~22 100
caractères débalisés ; couche arabe lue pour le titre, les glosses et
l'exploitation), règle 2 de LISEZ-MOI.md — aucune invention : les numéros du
Muwaṭṭaʾ (1866, 1867, 1873, 1887, 1869, 1865, 1868 — vérifiés à la leçon),
les attributions (Nāfiʿ, ʿAbdallāh ibn ʿUmar, ʿUmar ibn al-Khaṭṭāb, l'homme
des Anṣār, Hishām ibn ʿUrwa et son père ʿUrwa, al-Miswar ibn Makhrama,
Subayʿa al-Aslamiyya, Saʿīd ibn Khawla, Umm Salama, al-Furayʿa bint Mālik
ibn Sinān, Abū Saʿīd al-Khudrī, Banū Khudra, al-Qadūm, Ibn ʿAbd al-Barr,
Saʿīd ibn Isḥāq, Mālik, ash-Shāfiʿī, Abū Ḥanīfa, ath-Thawrī, al-Awzāʾī,
al-Layth ibn Saʿd, Aḥmad ibn Ḥanbal, ʿUthmān ibn ʿAffān, al-Bukhārī, Muslim,
Jābir, le qāḍī ʿIyāḍ, Abū Dāwūd, Ibn Rushd al-Jadd, Ibn ʿAbbās), les
références (al-Baqara 234 ; aṭ-Ṭalāq 4 ; le pèlerinage de l'adieu ; les
Préliminaires exhaustives 1/513, édition at-Tajkānī) sont citées telles
qu'elles figurent dans la leçon.

Garde-fous (convention des vagues R765-R775) :
- verif-citations intégrée (fragments « » verbatim dans le htmlFr débalisé) ;
- recoupements : ancres vérifiées dans les leçons voisines (13122 — la
  leçon précédente immédiate, le collecteur du divorce ; 13124 — la leçon
  même, la viduité et la mubtūta ; 13115 — la retraite dans sa demeure,
  Fatima bint Qays « la mubtūta a le toit » ; 13117 — le recueil de la
  retraite, où la mubtūta fut établie ; 13114 — le divorce de la réglée, la
  retraite comptée en cycles ; 13121 — la séparation des époux, où Ibn Rushd
  fut déjà rencontré — la leçon distingue al-Jadd du petit-fils).

NB consignés sans correction (relevés à la lecture) :
- l'étiquette de la couche CMS (الدرس 24) pour la vingt-unième du livre est
  CONCORDANTE au badge imprimé (الدرس 24, page 132 du PDF) — la série des
  étiquettes CMS (22-26 pour les leçons 16-20, toutes +3) revient au badge
  pour cette leçon ; le duplicata « vingt-quatrième » (13117 et 13124 portent
  la même étiquette CMS) vient donc des étiquettes de la couche CMS, non des
  badges imprimés (21 et 24 au PDF) — raffine la vérification R775 et la
  note du traducteur de la leçon (« la compilation du manuel mêle deux
  séries d'origine et double ses numéros ») ;
- les écarts d'étiquetage coranique de la leçon SONT DÉJÀ CONSIGNÉS par ses
  propres notes du traducteur : 2:232 imprimé ×3 → 2:234 restauré (écarts
  50ᵉ-52ᵉ du registre canonique) ; aṭ-Ṭalāq 4 ×2 concordantes — le
  commentaire les rapporte, sans nouvelle vérification ;
- l'en-tête de la leçon porte « enseignement préparatoire traditionnel » là
  où les leçons voisines portent « secondaire » — déjà noté par la leçon
  elle-même (la compilation mêle deux séries) ;
- le titleAr du CMS est tronqué (عدة المتوفى عنها زوجها, sans من كتاب
  الحديث…) — le h1 de la couche arabe porte le titre plein ;
- la numérotation du Muwaṭṭaʾ (1866, 1867, 1873, 1887, 1869, 1865, 1868)
  est portée par la leçon elle-même — concordante ;
- 0 coquille FR nouvelle relevée.
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13124'

E_13124 = {
    "auteur": "IA-1, tour R776",
    "resume": (
        "Guide de lecture de la leçon 21 (عدة المتوفى عنها زوجها من كتاب الحديث من موطأ الإمام مالك بشرح "
        "الزرقاني — la viduité de celle dont l'époux est décédé du livre de hadith du Muwaṭṭaʾ de l'imam Mālik "
        "avec le commentaire de l'imam al-Zarqānī ; la traduction du manuel porte « La viduité de la femme dont "
        "l’époux est décédé (ʿiddat al-mutawaffā ʾanhā zawjuhā) »), la vingt-unième du livre, étiquetée leçon 24 "
        "par la couche du CMS — étiquette ici CONCORDANTE au badge imprimé (الدرس 24, page 132 du PDF) : trois "
        "documents du Muwaṭṭaʾ portent la matière — le n° 1866 est la double fatwa : ʿAbdallāh ibn ʿUmar "
        "interrogé au sujet de la femme enceinte dont l'époux meurt — « Lorsqu’elle met au monde sa grossesse, "
        "elle est libre. » — et un homme des Anṣār présent auprès de lui informe de la parole dʿUmar ibn "
        "al-Khaṭṭāb : « Si elle met au monde alors que son époux est sur son lit — il ne serait point encore "
        "enterré —, elle est libre. » ; le n° 1867 est le pilier : al-Miswar ibn Makhrama informe que Subayʿa "
        "al-Aslamiyya accoucha quelques nuits après la mort de son époux, et le Messager d'Allah — la bénédiction "
        "et la paix d'Allah sur lui — lui dit : « Tu es libre ; épouse donc qui tu voudras. » ; le n° 1873 est la "
        "coutume (kāna yaqūlu) dʿIbn ʿUmar : « La femme dont l’époux est décédé, tout comme la mubtūta, ne passe "
        "point la nuit sinon dans sa maison. » "
        "Le préambule fonde le tout : le mariage est « un apaisement, une affection et une miséricorde entre eux "
        "deux » ; quand la mort frappe l'époux, la Loi du Législateur sage institue des mesures qui préservent la "
        "dignité de la femme et « annulent les coutumes de l'ignorance — celles qui entravaient sa liberté et "
        "rabaissaient son rang, lorsque la veuve se voyait imposée une retraite d’une année entière, vêtue de la "
        "robe la plus pauvre, confinée jusqu’à ce que l’oiseau au-dessus de sa tête vînt à mourir. » La leçon "
        "précédente a clos les dissolutions par la volonté de l'homme ; celle-ci ouvre la dissolution par la "
        "volonté d'Allah Lui-même : la mort. "
        "Première partie — les jugements de la viduité. Deux états : la non-enceinte et l'enceinte. La non-"
        "enceinte : « la retraite est obligatoire en la Loi, par le Livre, la Sunna et l'accord (ijmāʿ) » — le "
        "Livre : « Et ceux d’entre vous qui meurent et laissent des épouses : celles-ci devront observer une "
        "période d’attente de quatre mois et dix jours. Une fois leur terme échu, qu’aucun blâme ne vous soit "
        "imputé pour ce qu’elles feront d’elles-mêmes, de manière convenable. Allah est Informé de ce que vous "
        "faites. » — « le verset fixe le terme de la viduité dans son absolu : quatre mois et dix jours, sans que "
        "rien dans son apparent ne sépare l’enceinte de celle qui ne l’est point. » — la Sunna : « Il n’est point "
        "licite à une femme qui croit en Allah et au Jour dernier de porter le deuil (iḥdād) d’un mort plus de "
        "trois nuits, sinon pour son époux : quatre mois et dix (jours). » — « le deuil et la retraite se "
        "recouvrent chez la veuve en un même terme. » — l'accord : « nul docteur n’a tenu qu’elle se remarie "
        "avant son terme — l’obligation est ici plus ferme encore que la retenue de la répudiée, puisque la mort "
        "a définitivement rompu la conjugalité et que le compte ne dépend d’aucune volonté d’homme. » L'enceinte "
        ": la mise au monde la libère — Subayʿa, qui « se fut purifiée de ses lochies », entend « Tu es libre ; "
        "épouse donc qui tu voudras. » — « Ce hadith fut également rapporté par al-Bukhārī. » Mālik le porte par "
        "des voies multiples (le n° 1865 et le n° 1868 — la seconde porte la version d'Umm Salama et le sceau "
        "doctrinal de Mālik : « et c’est là l’ordre sur lequel les gens de science ne cessent d’être, chez "
        "nous ») ; « d’autant que le hadith de Subayʿa figure parmi les derniers jugements du Prophète — la "
        "bénédiction et la paix d’Allah sur lui —, car il est postérieur au pèlerinage de l’adieu (ḥajj "
        "(حَجٌّ) al-wadāʾ) : la doctrine reçue en l’école est scellée par la parole prophétique la plus tardive, "
        "celle qui ne peut plus être abrogée par une suivante. » Le départage : « celle qui n’est point enceinte "
        "compte quatre mois et dix jours — le terme de la lettre coranique ; celle qui est enceinte compte la "
        "mise au monde — le terme de l’issue de la grossesse, fût-il plus bref que les quatre mois : la grossesse "
        "y supplée, comme le dira l’exploitation au texte d’Ibn Rushd. » "
        "Deuxième partie — où s'accomplit la retraite. Le n° 1873 assimile la veuve à la mubtūta : elle "
        "« n’accomplit point sa retraite sinon dans sa maison » ; le renforce le n° 1869 — al-Furayʿa bint Mālik "
        "ibn Sinān, sœur d'Abū Saʿīd al-Khudrī, dont l'époux fut tué alors qu'il cherchait un esclave fugitif, "
        "demande « car mon époux ne m’avait laissée ni dans une demeure qu’il possédât, ni pension. » — « Oui. » "
        "— puis rappelée : « Demeure dans ta maison, jusqu’à ce que le Livre atteigne son terme. » — « J’y "
        "accomplis ma retraite quatre mois et dix (jours). » — et ʿUthmān ibn ʿAffān, établi, l'interroge, "
        "« il le suivit et jugea par lui. » Ibn ʿAbd al-Barr commente : le hadith — dit de Saʿīd ibn Isḥāq — "
        "« est célèbre chez les juristes du Ḥijāz et de l’Irāq, et suivi chez eux : ils l’ont accueilli avec "
        "acceptation et en ont donné fatwa » — à lui sont allés Mālik, ash-Shāfiʿī, Abū Ḥanīfa et leurs "
        "compagnons, ath-Thawrī, al-Awzāʾī, al-Layth ibn Saʿd et Aḥmad ibn Ḥanbal — « tous disent que la femme "
        "dont l’époux est décédé accomplit sa retraite dans la maison qu’elle habitait, à elle ou à son époux, "
        "et ne passe point la nuit hors d’elle jusqu’à ce que sa retraite s’achève ; il lui est permis de sortir "
        "de jour pour ses besoins » ; la sortie de jour se fonde sur le hadith des palmiers que Muslim rapporte de "
        "Jābir — « Si, émonde tes palmiers : peut-être feras-tu aumône ou œuvre bonne. » — et sur le commentaire "
        "du qāḍī ʿIyāḍ : « Il y a en cela une preuve pour Mālik (مَالِك) et al-Layth de la licéité de la sortie "
        "de jour de la femme en retraite » ; « l’émondage (jidār) n’a lieu que de jour, selon la coutume et la "
        "Loi » ; la doctrine : « la demeure est le siège de la retraite, la nuit y est obligatoire, le jour y est "
        "libre. » — la maison de la veuve est celle qu'elle habitait, « à elle ou à son époux » — « la retraite "
        "du décès se tient dans la maison du deuil, non par saisie, mais par une courtoisie que le droit et le "
        "naturel d’accord imposent. » — et la règle de nécessité : « celle qui ne possède point de demeure ni ne "
        "reçoit point de pension retourne auprès des siens » — « lorsque la maison manque, la retraite suit la "
        "famille, et l’autorité califale — ʿUthmān — la consacre en jurisprudence régnante. » "
        "Troisième partie — la sagesse de la légalisation : la retraite impose « pour préserver la dignité de la "
        "famille, la protéger de la dissolution et de la désagrégation, de la confusion des lignages (ikhtilāṭ "
        "al-ansāb), et pour marquer le deuil de l’époux par la manifestation du chagrin et de l’affliction après "
        "la mort » ; son dessein est triple — « s’astreindre à l’ordre de la Loi par adoration (ʿibāda), "
        "s’acquitter du droit de l’époux, et s’assurer de la pureté du sein (barāʾat ar-raḥim) de toute "
        "grossesse » ; le Législateur a fait de la mise au monde la retraite de l'enceinte — le verset la "
        "spécialise : « et quant à celles qui sont enceintes, leur période d’attente se terminera à leur "
        "accouchement » — et la Sunna la consacre envers Subayʿa : « ni la robe de l’affliction portée une "
        "année, ni l’exclusion prolongée du mariage — mais un terme mesuré, un deuil honnête, et une liberté "
        "rendue. » "
        "L'exploitation porte Ibn Rushd al-Jadd — les Préliminaires exhaustives (al-Muqaddimāt al-Mumahhadāt), "
        "tome 1/513, édition at-Tajkānī — le grand-père d'Averroès, distinct du commencement du mujtahid du "
        "petit-fils déjà rencontré à la séparation des époux : « Quant à la retraite de la mort, sa durée est de "
        "quatre mois et dix si elle n’est point enceinte, et la mise au monde de sa grossesse si elle est "
        "enceinte. » — « l’apparent de cette généralité couvrait l’enceinte et la non-enceinte ; en fut "
        "spécialisée l’enceinte par Sa parole » — trois lectures s'y départagent : la mise au monde seule (la "
        "doctrine de Mālik et de la majorité), l'abrogation du verset des mois — refusée par la règle des "
        "sources : « l’abrogation n’a lieu que dans ce qui se contredit sans qu’on puisse le rassembler ; le "
        "juste est qu’elle ne l’abroge point, mais qu’elle l’explique et spécialise la généralité. » — et la "
        "lecture d'Ibn ʿAbbās : « Ibn ʿAbbās porta le verset sur sa généralité pour l’enceinte et la "
        "non-enceinte, et n’y vit ni abrogation ni spécialisation : il obligea l’enceinte, dans la retraite, le "
        "plus long des deux termes, en considération des deux versets. » L'école tient la première — « la "
        "retraite de la mort, pour l’enceinte, est l’issue de la grossesse — la doctrine la plus large en "
        "faveur de la femme, et la plus proche du dessein du terme : la certitude du sein pur. » "
        "Les notes du traducteur consignent l'apparat de la leçon : cinq emplacements de versets en image vides "
        "au scan — les étiquettes imprimées « la sourate al-Baqara (الْبَقَرَة), verset 232 » à TROIS emplacements, requérant "
        "en réalité le verset 234 (celui de la viduité — le 232 est celui de la retraite du divorce) : écarts "
        "50ᵉ-52ᵉ du registre canonique, textes restaurés 2:234 verbatim dans la couche française ; « la sourate "
        "aṭ-Ṭalāq, verset 4 » à DEUX emplacements, concordantes ; la glose du n° 1866 — « il ne serait point "
        "encore enterré » — rendue par « à la cassure du qāf (قَاف) dans l’original » : « la mise au monde "
        "libère la femme fût-elle survenue avant même que son époux ne fût déposé en sa tombe » ; Subayʿa "
        "portée par trois moments — la mise au monde qui épuise la retraite, la purification des lochies qui "
        "n'en est point partie, la licence prophétique finale. La préparation préalable requiert le sens de "
        "l'ʿazl (le retrait) et les motifs de son recours — annonce la leçon suivante du registre (13135, le "
        "chapitre du retrait)."
    ),
    "explication": [
        "La leçon 21 succède au collecteur du divorce (leçon 20) et change de versant : la précédente réglait le "
        "compte des divorces et le contraint — les dissolutions par la volonté de l'homme ; celle-ci ouvre la "
        "dissolution par la volonté d'Allah Lui-même — la mort. La matière est portée par trois documents du "
        "Muwaṭṭaʾ (le n° 1866, le n° 1867, le n° 1873) plus les supports internes de l'analyse (le n° 1887 du "
        "deuil, le n° 1869 d'al-Furayʿa, les n° 1865 et 1868 des voies multiples de Subayʿa). La leçon est la "
        "vingt-unième du livre, étiquetée leçon 24 par la couche du CMS — étiquette ici concordante au badge "
        "imprimé (الدرس 24, page 132 du PDF), la série des étiquettes CMS (22-26, toutes +3 aux leçons 16-20) "
        "revient au badge : le duplicata « vingt-quatrième » (13117 et 13124) vient des étiquettes de la couche "
        "CMS, non des badges imprimés (21 et 24).",

        "Les trois objectifs dessinent le dessein : reconnaître certains des jugements de la viduité, la "
        "distinguer « des autres espèces de retraite (ʿidda) », saisir « la sagesse de la légalisation de la "
        "viduité de la femme dont l’époux est décédé. » Le préambule pose la couleur : le mariage est « un "
        "apaisement, une affection et une miséricorde entre eux deux » ; la mort de l'époux suspend d'un coup le "
        "dessein, la demeure et l'avenir de la femme ; et la Loi institue des mesures qui préservent sa dignité "
        "en abrogeant les coutumes de l'ignorance — « une retraite d’une année entière, vêtue de la robe la plus "
        "pauvre, confinée jusqu’à ce que l’oiseau au-dessus de sa tête vînt à mourir. » L'image de l'oiseau porte "
        "tout le chapitre : la jāhiliyya ne mesurait pas le deuil, elle l'ornait de cruautés ; l'islam le mesure "
        "et le borne.",

        "Le n° 1866 porte la double fatwa que le Muwaṭṭaʾ aime : ʿAbdallāh ibn ʿUmar interrogé au sujet de la "
        "femme enceinte dont l'époux meurt répond « Lorsqu’elle met au monde sa grossesse, elle est libre. » — "
        "et un homme des Anṣār présent auprès de lui informe de la parole dʿUmar ibn al-Khaṭṭāb : « Si elle met "
        "au monde alors que son époux est sur son lit — il ne serait point encore enterré —, elle est libre. » "
        "La juxtaposition établit que la règle ne fut point un avis isolé mais la pratique médinoise unanime dès "
        "le califat. La glose du lexique rend « il ne serait point encore enterré » par « à la cassure du qāf "
        "(قَاف) dans l’original » — l'entendu le plus remarquable du chapitre : « la mise au monde libère la "
        "femme fût-elle survenue avant même que son époux ne fût déposé en sa tombe » — le terme du décès ne "
        "tient ni aux rites funèbres ni à un deuil social : « le droit de la femme se joue sur le fait naturel, "
        "non sur la cérémonie. »",

        "Le n° 1867 est le pilier : al-Miswar ibn Makhrama informe — par Hishām ibn ʿUrwa, de son père ʿUrwa — "
        "que Subayʿa al-Aslamiyya accoucha quelques nuits après la mort de son époux, et le Prophète — la "
        "bénédiction et la paix d'Allah sur lui — lui dit : « Tu es libre ; épouse donc qui tu voudras. » "
        "L'analyse distingue trois moments : la mise au monde (waḍʾ al-ḥaml), qui épuise la retraite ; la "
        "purification des lochies (nufās) — « lorsqu’elle se fut purifiée de ses lochies » — qui n'est point "
        "partie du terme mais l'état où la femme redevient prête au mariage ; la licence prophétique finale. "
        "Subayʿa savait déjà la règle avant de consulter — la doctrine était connue des femmes mêmes, et le "
        "Prophète la confirma sans correction. « Ce hadith fut également rapporté par al-Bukhārī. »",

        "Le n° 1873 est la coutume dʿIbn ʿUmar (kāna yaqūlu — la forme par laquelle l'école établit une règle "
        "continûment professée) : « La femme dont l’époux est décédé, tout comme la mubtūta, ne passe point la "
        "nuit sinon dans sa maison. » La veuve reçoit le régime du logement de la répudiée dissolvante — déjà "
        "établi aux leçons de la retraite dans sa demeure (Fatima bint Qays) et du recueil : la demeure est le "
        "siège de la retraite. La leçon du logement s'étend au décès par l'assimilation des deux femmes — celle "
        "que l'homme a quittée par divorce et celle qu'Allah en a privée.",

        "Première partie — la non-enceinte. La retraite « est obligatoire en la Loi, par le Livre, la Sunna et "
        "l'accord (ijmāʿ) » : le Livre — « Et ceux d’entre vous qui meurent et laissent des épouses : celles-ci "
        "devront observer une période d’attente de quatre mois et dix jours. Une fois leur terme échu, qu’aucun "
        "blâme ne vous soit imputé pour ce qu’elles feront d’elles-mêmes, de manière convenable. Allah est "
        "Informé de ce que vous faites. » — « le verset fixe le terme de la viduité dans son absolu : quatre "
        "mois et dix jours, sans que rien dans son apparent ne sépare l’enceinte de celle qui ne l’est point. » "
        "La Sunna — « Il n’est point licite à une femme qui croit en Allah et au Jour dernier de porter le deuil "
        "(iḥdād) d’un mort plus de trois nuits, sinon pour son époux : quatre mois et dix (jours). » — rend au "
        "deuil son régime général et excepte l'époux seul : « le deuil et la retraite se recouvrent chez la "
        "veuve en un même terme. » L'accord — « nul docteur n’a tenu qu’elle se remarie avant son terme » : "
        "l'obligation plus ferme que la retenue de la répudiée, car la mort a rompu la conjugalité et « le "
        "compte ne dépend d’aucune volonté d’homme. »",

        "Première partie — l'enceinte. La mise au monde la libère : le n° 1866 et le n° 1867 le portent ; Mālik "
        "le cite par des voies multiples — le n° 1865 et le n° 1868 —, la seconde portant la version d'Umm "
        "Salama, l'épouse du Prophète, et le sceau doctrinal : « et c’est là l’ordre sur lequel les gens de "
        "science ne cessent d’être, chez nous » ; la majorité des savants des anciens et les imams de la fatwa "
        "s'y sont accordés — « d’autant que le hadith de Subayʿa figure parmi les derniers jugements du "
        "Prophète — la bénédiction et la paix d’Allah sur lui —, car il est postérieur au pèlerinage de "
        "l’adieu (ḥajj (حَجٌّ) al-wadāʾ) : la doctrine reçue en l’école est scellée par la parole prophétique "
        "la plus tardive, celle qui ne peut plus être abrogée par une suivante. » Le départage : « celle qui "
        "n’est point enceinte compte quatre mois et dix jours — le terme de la lettre coranique ; celle qui est "
        "enceinte compte la mise au monde — le terme de l’issue de la grossesse, fût-il plus bref que les "
        "quatre mois : la grossesse y supplée, comme le dira l’exploitation au texte d’Ibn Rushd. »",

        "Deuxième partie — où s'accomplit la retraite. Le n° 1873 assimile la veuve à la mubtūta ; le n° 1869 "
        "en précise le fond : al-Furayʿa bint Mālik ibn Sinān, sœur d'Abū Saʿīd al-Khudrī, dont l'époux fut tué "
        "au bord d'al-Qadūm alors qu'il cherchait un esclave fugitif, demande à retourner chez les siens — "
        "« car mon époux ne m’avait laissée ni dans une demeure qu’il possédât, ni pension. » — le Prophète "
        "dit « Oui. », puis la rappelle : « Demeure dans ta maison, jusqu’à ce que le Livre atteigne son "
        "terme. » — elle « J’y accomplis ma retraite quatre mois et dix (jours). » — et ʿUthmān, établi, "
        "l'interroge puis « il le suivit et jugea par lui. » — l'exception devient précédent califal. Le "
        "« Livre » du dialogue est le terme coranique lui-même : la borne du séjour est la lettre de la "
        "viduité.",

        "L'apparat du logement : Ibn ʿAbd al-Barr commente que le hadith d'al-Furayʿa — dit de Saʿīd ibn Isḥāq, "
        "la voie du rapporteur — « est célèbre chez les juristes du Ḥijāz et de l’Irāq, et suivi chez eux : ils "
        "l’ont accueilli avec acceptation et en ont donné fatwa » — Mālik, ash-Shāfiʿī, Abū Ḥanīfa et leurs "
        "compagnons, ath-Thawrī, al-Awzāʾī, al-Layth ibn Saʿd et Aḥmad ibn Ḥanbal — « tous disent que la femme "
        "dont l’époux est décédé accomplit sa retraite dans la maison qu’elle habitait, à elle ou à son époux, "
        "et ne passe point la nuit hors d’elle jusqu’à ce que sa retraite s’achève ; il lui est permis de "
        "sortir de jour pour ses besoins » ; la sortie de jour se fonde sur le hadith des palmiers (Muslim de "
        "Jābir — « Si, émonde tes palmiers : peut-être feras-tu aumône ou œuvre bonne. ») et sur le qāḍī "
        "ʿIyāḍ : « Il y a en cela une preuve pour Mālik (مَالِك) et al-Layth de la licéité de la sortie de "
        "jour de la femme en retraite » — « l’émondage (jidār) n’a lieu que de jour, selon la coutume et la "
        "Loi » — « l'argument géographique achève l'argument rituel » : les palmiers des Anṣār ne sont point "
        "loin, la sortie de jour n'exige point la nuit hors de la demeure.",

        "La doctrine et sa largeur propre : « la demeure est le siège de la retraite, la nuit y est obligatoire, "
        "le jour y est libre. » — mais la veuve ajoute au régime de la répudiée deux largeurs : sa maison est "
        "celle qu'elle habitait, « à elle ou à son époux » — car le lien qui fonde l'obligation n'est point la "
        "propriété mais la demeure conjugale elle-même — et son cas n'exige point la contrainte du gouverneur : "
        "« la retraite du décès se tient dans la maison du deuil, non par saisie, mais par une courtoisie que le "
        "droit et le naturel d’accord imposent. » Et le hadith d'al-Furayʿa y ajoute la règle de nécessité : "
        "« celle qui ne possède point de demeure ni ne reçoit point de pension retourne auprès des siens » — "
        "« lorsque la maison manque, la retraite suit la famille, et l’autorité califale — ʿUthmān — la "
        "consacre en jurisprudence régnante. »",

        "Troisième partie — la sagesse. La retraite impose pour « préserver la dignité de la famille, la "
        "protéger de la dissolution et de la désagrégation, de la confusion des lignages (ikhtilāṭ al-ansāb), "
        "et pour marquer le deuil de l’époux par la manifestation du chagrin et de l’affliction après la mort » "
        "— en honneur du lien conjugal. Son dessein est triple : « s’astreindre à l’ordre de la Loi par "
        "adoration (ʿibāda), s’acquitter du droit de l’époux, et s’assurer de la pureté du sein (barāʾat "
        "ar-raḥim) de toute grossesse » ; le Législateur a fait de la mise au monde la retraite de l'enceinte — "
        "« et quant à celles qui sont enceintes, leur période d’attente se terminera à leur accouchement » — "
        "l'allégeant après que l'ignorance lui imposait le terme complet : « ni la robe de l’affliction portée "
        "une année, ni l’exclusion prolongée du mariage — mais un terme mesuré, un deuil honnête, et une "
        "liberté rendue. »",

        "L'exploitation porte Ibn Rushd al-Jadd — les Préliminaires exhaustives (al-Muqaddimāt al-Mumahhadāt), "
        "tome 1/513, édition at-Tajkānī — le grand-père d'Averroès, distinct du commencement du mujtahid du "
        "petit-fils déjà rencontré à la séparation des époux : « Quant à la retraite de la mort, sa durée est "
        "de quatre mois et dix si elle n’est point enceinte, et la mise au monde de sa grossesse si elle est "
        "enceinte. » — « l’apparent de cette généralité couvrait l’enceinte et la non-enceinte ; en fut "
        "spécialisée l’enceinte par Sa parole » ; trois lectures s'y départagent : la mise au monde seule (la "
        "doctrine de Mālik et de la majorité, portée par Subayʿa) ; l'abrogation du verset des mois — refusée "
        "par la règle des sources : « l’abrogation n’a lieu que dans ce qui se contredit sans qu’on puisse le "
        "rassembler ; le juste est qu’elle ne l’abroge point, mais qu’elle l’explique et spécialise la "
        "généralité. » — et la lecture d'Ibn ʿAbbās : « le plus long des deux termes » pour l'enceinte. "
        "L'école tient la première — « la retraite de la mort, pour l’enceinte, est l’issue de la grossesse — "
        "la doctrine la plus large en faveur de la femme, et la plus proche du dessein du terme : la certitude "
        "du sein pur. »",
    ],
    "points": [
        "Fil du livre : après le collecteur du divorce (leçon 20), la leçon ouvre la dissolution par la volonté "
        "d'Allah — la mort — après les dissolutions par la volonté de l'homme ; la leçon est la vingt-unième du "
        "livre, étiquetée leçon 24 par la couche du CMS — étiquette concordante au badge imprimé (الدرس 24, "
        "page 132), la série CMS (22-26, +3) revient au badge ici.",
        "Le préambule : le mariage « un apaisement, une affection et une miséricorde entre eux deux » ; la "
        "jāhiliyya imposait à la veuve « une retraite d’une année entière, vêtue de la robe la plus pauvre, "
        "confinée jusqu’à ce que l’oiseau au-dessus de sa tête vînt à mourir » — la Loi mesure le deuil et rend "
        "la liberté.",
        "Le n° 1866 : la double fatwa — ʿAbdallāh ibn ʿUmar « Lorsqu’elle met au monde sa grossesse, elle est "
        "libre. » et ʿUmar via l'homme des Anṣār « Si elle met au monde alors que son époux est sur son lit — "
        "il ne serait point encore enterré —, elle est libre. » — la pratique médinoise unanime dès le califat.",
        "La glose du qāf : « il ne serait point encore enterré » rendu par « à la cassure du qāf (قَاف) dans "
        "l’original » — la mise au monde libère fût-elle survenue avant la sépulture — « le droit de la femme "
        "se joue sur le fait naturel, non sur la cérémonie. »",
        "Le n° 1867 : Subayʿa al-Aslamiyya via al-Miswar ibn Makhrama par Hishām ibn ʿUrwa et son père — « Tu "
        "es libre ; épouse donc qui tu voudras. » — trois moments : la mise au monde qui épuise la retraite, la "
        "purification des lochies qui n'en est point partie, la licence finale ; al-Bukhārī rapporte également.",
        "Le n° 1873 : la coutume dʿIbn ʿUmar (kāna yaqūlu) — « La femme dont l’époux est décédé, tout comme la "
        "mubtūta, ne passe point la nuit sinon dans sa maison. » — le régime du logement de la mubtūta s'étend "
        "à la veuve.",
        "La non-enceinte : quatre mois et dix jours par le Livre (2:234 — « le verset fixe le terme de la "
        "viduité dans son absolu »), par la Sunna (le n° 1887 — « le deuil et la retraite se recouvrent chez la "
        "veuve en un même terme »), par l'ijmāʿ — « l’obligation est ici plus ferme encore que la retenue de "
        "la répudiée, puisque la mort a définitivement rompu la conjugalité ».",
        "L'enceinte : la mise au monde la libère — les voies multiples de Mālik (le n° 1865, le n° 1868 avec "
        "Umm Salama et le sceau « et c’est là l’ordre sur lequel les gens de science ne cessent d’être, chez "
        "nous ») ; le hadith de Subayʿa postérieur au pèlerinage de l'adieu — « la parole prophétique la plus "
        "tardive, celle qui ne peut plus être abrogée par une suivante. »",
        "Le départage : « celle qui n’est point enceinte compte quatre mois et dix jours — le terme de la "
        "lettre coranique ; celle qui est enceinte compte la mise au monde — le terme de l’issue de la "
        "grossesse, fût-il plus bref que les quatre mois : la grossesse y supplée » — la mise "
        "au monde supplée, quand elle est plus brève.",
        "Le logement : le n° 1873 + le n° 1869 (al-Furayʿa bint Mālik ibn Sinān, sœur d'Abū Saʿīd al-Khudrī — "
        "« Demeure dans ta maison, jusqu’à ce que le Livre atteigne son terme. » — la règle de nécessité, "
        "ʿUthmān « il le suivit et jugea par lui. ») ; Ibn ʿAbd al-Barr — le hadith célèbre du Ḥijāz et de "
        "l'Irāq — la demeure « à elle ou à son époux », la sortie de jour licite.",
        "La sortie de jour : le hadith des palmiers (Muslim de Jābir — « Si, émonde tes palmiers : peut-être "
        "feras-tu aumône ou œuvre bonne. ») et le qāḍī ʿIyāḍ — « l’émondage (jidār) n’a lieu que de jour, "
        "selon la coutume et la Loi » — « la demeure est le siège de la retraite, la nuit y est obligatoire, "
        "le jour y est libre. »",
        "La sagesse : « la confusion des lignages (ikhtilāṭ al-ansāb) », le deuil de l'époux, le triple dessein "
        "(« s’astreindre à l’ordre de la Loi par adoration (ʿibāda), s’acquitter du droit de l’époux, et "
        "s’assurer de la pureté du sein (barāʾat ar-raḥim) ») ; aṭ-Ṭalāq 4 spécialise l'enceinte — « ni la "
        "robe de l’affliction portée une année, ni l’exclusion prolongée du mariage — mais un terme mesuré, un "
        "deuil honnête, et une liberté rendue. »",
        "L'exploitation (Ibn Rushd al-Jadd, les Préliminaires exhaustives 1/513 — le grand-père, distinct du "
        "petit-fils) : trois lectures — la mise au monde seule (l'école), l'abrogation refusée (« la "
        "spécialisation (takhṣīṣ) n'est point l'abrogation (naskh) » au sens de la règle des sources), Ibn "
        "ʿAbbās (le plus long des deux termes) ; les étiquettes imprimées 232 ×3 requéraient le 2:234 (écarts "
        "50ᵉ-52ᵉ du registre canonique, consignés par les notes du traducteur de la leçon) ; la préparation "
        "(l'ʿazl) annonce 13135.",
    ],
    "vocabulaire": [
        {"ar": "العدة", "translit": "ʿidda",
         "fr": "la retraite / la période d'attente : celle du décès est « la plus simple au compte et la plus "
               "grave au sens » — quatre mois et dix jours pour la non-enceinte, la mise au monde pour "
               "l'enceinte"},
        {"ar": "المبتوتة", "translit": "al-mubtūta",
         "fr": "la répudiée d'une répudiation dissolvante : « la répudiée d’une répudiation dissolvante — la "
               "femme que son époux a répudiée trois fois, déjà rencontrée aux leçons du logement et du recueil "
               "de la retraite » — son régime de logement s'étend à la veuve"},
        {"ar": "النفاس", "translit": "nufās",
         "fr": "les lochies : « l’entendu est qu’elle enfanta — les lochies (nufās) suivirent son accouchement. » "
               "— la purification des lochies n'est point partie du terme, elle est l'état où la femme redevient "
               "prête au mariage"},
        {"ar": "وضع الحمل", "translit": "waḍʾ al-ḥaml",
         "fr": "la mise au monde : la retraite de l'enceinte — « la mise au monde libère la femme fût-elle "
               "survenue avant même que son époux ne fût déposé en sa tombe »"},
        {"ar": "قد حللت", "translit": "qad ḥalalti",
         "fr": "« tu es libre » : « l’entendu est que sa retraite s’est achevée, de sorte que le mariage lui "
               "redevient licite. » — la parole du Prophète ﷺ à Subayʿa"},
        {"ar": "دفن", "translit": "yudfan",
         "fr": "« il ne serait point encore enterré » : rendu par « à la cassure du qāf (قَاف) dans "
               "l’original » — le terme ne tient ni aux rites funèbres ni à un deuil social, il tient à la "
               "seule issue de la grossesse"},
        {"ar": "أقصى الأجلين", "translit": "aqṣā l-ajalayn",
         "fr": "le plus long des deux termes : la lecture d'Ibn ʿAbbās — « il obligea l’enceinte, dans la "
               "retraite, le plus long des deux termes, en considération des deux versets » — contre la doctrine "
               "de l'école (la mise au monde seule)"},
        {"ar": "العزل", "translit": "al-ʿazl",
         "fr": "le retrait : le sujet de la préparation préalable (« Que signifie l’ʿazl (le retrait) ? ») — "
               "annonce la leçon suivante du registre, le chapitre du retrait"},
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


# ---------- rectification du texte éditorial de 13122 (registre 50ᵉ -> 56ᵉ-58ᵉ) ----------
data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
corrige = 0
if '13122' in com:
    ancien = com['13122']['explication'][3]
    nouveau = ancien.replace(
        '50ᵉ écart d’étiquetage du registre (une divergence, répétée à trois emplacements)',
        '56ᵉ-58ᵉᵉ écarts d’étiquetage du registre (une divergence d’étiquette, répétée à trois '
        'emplacements — le rang 50 était déjà pris par les écarts 2:232 de la leçon 13124, comptage '
        'canonique de la chaîne de traduction)'
    ).replace('56ᵉ-58ᵉᵉ', '56ᵉ-58ᵉ')
    if nouveau != ancien:
        com['13122']['explication'][3] = nouveau
        corrige = 1
print('rectification 13122 (50ᵉ -> 56ᵉ-58ᵉ) :', 'OK' if corrige else 'déjà appliquée ou non requise')

# ---------- fusion ----------
if DOCID in com:
    print(f'!! {DOCID} déjà présent — rien de fait')
    raise SystemExit(1)
com[DOCID] = norme_entree(E_13124)

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
    hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t).replace('\ufdfa', '')
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

# ---------- verif-citations ----------
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
    ('13122 — la leçon précédente immédiate (le collecteur du divorce, le contraint)', 'contraint' in fr('13122')),
    ('13124 — la leçon même (la viduité et la mubtūta)', 'mubtūta' in corpus),
    ('13115 — la retraite dans sa demeure (leçon 17), Fatima bint Qays « la mubtūta a le toit »', 'Fatima' in fr('13115')),
    ('13117 — le recueil de la retraite (leçon 18), où la mubtūta fut établie', 'mubtūta' in fr('13117')),
    ('13114 — le divorce de la réglée (leçon 16), la retraite comptée en cycles', 'cycles' in fr('13114')),
    ('13121 — la séparation des époux (leçon 19), où Ibn Rushd fut déjà rencontré (le petit-fils)', 'Rushd' in fr('13121')),
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
