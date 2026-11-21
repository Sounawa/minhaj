#!/usr/bin/env python3
"""R775 — ajoute le commentaire pédagogique de la leçon 20 de hadith-tanawi-1
(13122 جامع الطلاق — le collecteur du divorce, « Collecteur de divorce » dans
la traduction du manuel, la vingtième du livre, étiquetée leçon 26 par la
couche du CMS ((الدرس 26) en couche arabe, « phase I (leçon 26) » en tête de la
couche française) — le SUIVANT de R774, 13121, annoncé dès R773/R774)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r774-c19.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~9 800 caractères débalisés ; couche
arabe lue pour le titre plein جامع الطلاق من كتاب موطأ الإمام مالك بشرح
الزرقاني, l'étiquette (الدرس 26) et les sections non traduites). Règle 2 de
LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ (1861, 1858, 1864,
1862 — vérifiés au manuel imprimé, pages 126-127), les attributions (Hishām
ibn ʿUrwah et son père ʿUrwah, Ibn Shihāb, Saʿīd ibn al-Musayyab, Humayd ibn
ʿAbd al-Raḥmān ibn ʿAwf, ʿUbayd Allāh ibn ʿAbd Allāh ibn ʿUtbah ibn Masʿūd,
Sulaymān ibn Yasār, Abū Hurayra, ʿUmar ibn al-Khaṭṭāb, ʿĀʾisha, Mālik,
at-Tirmidhī, al-Ḥākim, Ibn Mardawayah, Yaʿlā ibn Shabīb, Muḥammad ibn Isḥāq,
Ibn Abī Shaybah, Abū Ruzayn, Ibn ʿAbd al-Barr, al-Istidhkār, ash-Shāfiʿī,
al-Ḥasan ibn Ḥayy, Aḥmad, Isḥāq, Abū Thawr, Dāwūd, Abū Ḥanīfa, ath-Thawrī,
Qatāda, Mujāhid, az-Zuhrī, ʿUmar ibn ʿAbd al-ʿAzīz), les références (al-Baqara
227 étiquette ×3 ; 228 et 229 étiquettes arabes concordantes ; la Mudawwana de
la famille article 09) sont citées telles qu'elles figurent dans la leçon.

Garde-fous (convention des vagues R765-R774) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr débalisé de la leçon (convention :
  frontières de blocs -> espace, tags inline -> '') ;
- recoupements : ancres vérifiées dans les leçons voisines (13121 — la
  leçon précédente immédiate, l'arbitrage des ḥakamayn ; 13122 — la leçon
  même, le contraint et les deux en colère et les deux ivres ; 13117 — le
  recueil de la retraite, la leçon 18 des qurūʾ des non-réglées ; 13114 — le
  divorce de la réglée, la leçon 16 de la retraite comptée en cycles ;
  13115 — la retraite dans sa demeure et la pension, la leçon 17 de Fatima
  bint Qays ; 12966 — le corpus califal du ẓihār, où Abū Hurayra fut déjà
  rencontré — le n° 1858 court par Abū Hurayra de ʿUmar).

NB consignés sans correction (relevés à la lecture, vérifiés au manuel
imprimé content/textbooks-src/hadith-1-thanawi_text.pdf) :
- PREMIÈRE VÉRIFICATION DES BADGES IMPRIMÉS : le badge الدرس du manuel
  imprimé porte الدرس 19 pour طلاق الحائض (13114, page 105), الدرس 20 pour
  عدة المرأة (13115, page 110), الدرس 21 pour جامع عدة الطلاق (13117, page
  116), الدرس 22 pour التفريق (13121, page 121), الدرس 23 pour جامع الطلاق
  (13122, page 126) — les étiquettes de la couche du CMS (22 à 26 pour les
  leçons 16 à 20, portées par les en-têtes FR « la vingt-deuxième leçon »…
  et les étiquettes AR (الدرس 22)…(الدرس 26)) sont systématiquement +3 par
  rapport aux badges imprimés — les consignations R772-R774 (« étiquetée
  leçon N par l'imprimé ») enregistraient l'étiquette de la couche CMS, non
  le badge imprimé — consigné sans correction ;
- l'emplacement du verset du n° 1861 porte à TROIS reprises l'étiquette
  « verset : 227 » (×2) puis « verset 227 » (×1) ; le manuel imprimé (page
  126) porte la même étiquette (البقرة الآية : 227) pour une āya dont le
  texte imprimé est l'OUVERTURE du verset 229 (الطَّلَاقُ مَرَّتَانِ
  فَإِمْسَاكٌ بِمَعْرُوفٍ أَوْ تَسْرِيحٌ بِإِحْسَانٍ) — le vrai verset 227
  porte au cache coranique la décision au divorce et l'audience d'Allah ;
  le texte composite porté par la couche française (dont la fin correspond
  à la fin du verset 229) ne correspond ni au vrai verset 227 ni à l'āya
  imprimée — 50ᵉ écart d'étiquetage du registre (une divergence, répétée à
  trois emplacements) — consigné sans correction ;
- les autres emplacements coraniques concordants : البقرة الآية 228 pour le
  verset des trois menstrues, البقرة الآية 229 pour le verset du rachat et
  [al-Baqara (الْبَقَرَة), 229] pour le passage d'Ibn Abī Shaybah ; la couche
  française ne porte pas d'étiquette propre sur les deux versets du n° 1862
  (l'attribution « Muwaṭṭaʾ, n° 1862 » les couvre) ;
- la couche française s'arrête à la sous-section « Le divorce prononcé sous
  contrainte et en colère » : la couche arabe poursuit — طلاق السكران
  (divergence des gens de Médine et d'autres ; un groupe rend le divorce de
  l'ivrogne obligatoire et le lie : Saʿīd ibn al-Musayyab, Sulaymān ibn
  Yasār, Mujāhid, az-Zuhrī), رابعا حكم العاجز عن النفقة (Qatāda ; la sunna
  de Saʿīd via Abū az-Zinād ; Mālik le divorce révocable, ash-Shāfiʿī la
  bāʾin, Abū Ḥanīfa et ath-Thawrī la non-séparation forcée avec al-Ḥasan,
  Ibn Shihāb et ʿUmar ibn ʿAbd al-ʿAzīz — et un emplacement de verset
  étiqueté البقرة الآية 285 MUET au CMS), التقييم، الاستثمار (la Mudawwana
  classique 2/79 Dār al-Kutub al-ʿIlmiyya, بتصرف يسير — le contraint, le
  fou, le simple d'esprit ; طلاق السفيه جائز في قول مالك) et الإعداد القبلي
  (la ʿidda — définition, sagesse, types — annonce la leçon suivante du
  registre, 13124 la retraite de celle dont le mari est décédé) —
  paraphrasés dans le commentaire sans guillemets (hors corpus de
  vérification) ;
- les titres du CMS tronqués : titleAr « جامع الطلاق من », titleFr
  « Collecteur de divorce de » (le h1 de la couche française porte le même
  tronc) ;
- la numérotation du Muwaṭṭaʾ (1861, 1858, 1864, 1862) vérifiée au manuel
  imprimé (pages 126-127) — concordante ;
- les « trois Imams » de la deuxième partie ne sont pas nommés — Abū Ḥanīfa
  cité à part parmi les dissidents — consigné tel quel ;
- la glose du lexique « -lā āūka ilayya » — translit du lemme recopié tel
  quel (lā āwīka attendu) ; le rendu du verset des trois menstrues porte le
  double « si » (« si ils veulent une réconciliation ») — recopié tel quel ;
- l'étiquette « verset : 227 » (avec deux-points) puis « verset 227 » (sans)
  pour le même verset à trois emplacements — inconsistence de composition.
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13122'

E_13122 = {
    "auteur": "IA-1, tour R775",
    "resume": (
        "Guide de lecture de la leçon 20 (جامع الطلاق من كتاب موطأ الإمام مالك بشرح الزرقاني — le collecteur du "
        "divorce du livre de hadith du Muwaṭṭaʾ de l'imam Mālik avec le commentaire de l'imam al-Zarqānī ; la "
        "traduction du manuel porte « Collecteur de divorce », titre du CMS tronqué à « Collecteur de divorce de »), "
        "la vingtième du livre, étiquetée leçon 26 par la couche du manuel — l'étiquette arabe porte (الدرس 26), la "
        "tête de la couche française porte « phase I (leçon 26) » — alors que le badge imprimé du PDF porte (الدرس "
        "23), écart d'étiquetage vérifié et consigné aux NB : trois documents du Muwaṭṭaʾ portent la matière — le "
        "n° 1861 est le pilier : Mālik de Hishām ibn ʿUrwah, de son père, la coutume de l'époque préislamique — « Un "
        "homme, lorsqu’il divorçait sa femme, puis la réintégrait avant que ne s’achève sa période d’attente (ʿidda), "
        "cela lui était permis, même s’il l’avait divorcée mille fois. » — puis l'homme du récit, qui répudia de "
        "nouveau et jura « Par Allah, je ne te reprendrai jamais, et tu ne seras jamais licite pour moi. » — alors "
        "Allah, que soit béni et exalté, a révélé, et Mālik scelle : « Les gens prirent le divorce comme une "
        "nouveauté à partir de ce jour, qu’ils aient divorcé ou non. » ; le n° 1858 est la règle du compte "
        "survivant au mariage intermédiaire : quatre maîtres de Médine — Saʿīd ibn al-Musayyab, Humayd ibn ʿAbd "
        "al-Raḥmān ibn ʿAwf, ʿUbayd Allāh ibn ʿAbd Allāh ibn ʿUtbah ibn Masʿūd et Sulaymān ibn Yasār — tous "
        "d'Abū Hurayra disant de ʿUmar ibn al-Khaṭṭāb : « Quelle que soit la femme que son mari a divorcée une ou "
        "deux fois, puis qu’il a laissée jusqu’à ce qu’elle soit licite et qu’elle épouse un autre mari, et que "
        "celui-ci meure d’elle ou la divorce, puis que son premier mari l’épouse, alors elle sera avec lui pour ce "
        "qui reste de ses divorces, une ou deux. » — et le sceau de Mālik : « Et c’est la Sunnah parmi nous, sur "
        "laquelle il n’y a pas de divergence. » ; le n° 1864 est le dire de Saʿīd ibn al-Musayyab : « Si un homme "
        "ne trouve pas de quoi subvenir aux besoins de sa femme, on sépare entre eux. » — et son sceau : « Et c’est "
        "ainsi que j’ai trouvé les gens de science dans notre pays. » "
        "Le préambule fonde le tout : la Loi divine saine a autorisé le divorce, bien que son principe soit la "
        "réprobation en raison de ses causes — « Le plus détesté des licites auprès d’Allah est le divorce. » "
        "rapporté par Abū Dāwūd et Ibn Mājah — car « il rompt les liens du mariage (nikāḥ), mais il est, lorsque la "
        "nécessité s’en fait sentir, un moyen par lequel on peut se libérer d’une cohabitation difficile » ; les "
        "objectifs posent le dessein : « Comprendre certaines coutumes de l’ère préislamique (al-jāhiliyya) que "
        "l’Islam a abrogées dans le traitement de la femme. » et « Saisir la générosité de la Loi divine et Sa "
        "miséricorde dans l’organisation de la relation conjugale. » "
        "Première partie — ce qui se rapporte au nombre des divorces. Le premier hadith montre ce qu'étaient les "
        "gens de l'époque préislamique — « où un homme pouvait divorcer sa femme un grand nombre de fois, et chaque "
        "fois que sa période d’attente approchait, il la réintégrait pour la laisser dans une situation de suspens, "
        "ni mariée ni divorcée. » — tandis que la Loi généreuse « a brisé les chaînes préislamiques qui "
        "l’enchaînaient sans miséricorde ni pitié » et a fait « le divorce soit prononcé deux fois, permettant au "
        "mari de réintégrer sa femme à ces deux occasions. S’il la divorce une troisième fois, elle est "
        "définitivement séparée de lui, et ne lui est plus licite jusqu’à ce qu’elle épouse un autre mari. » "
        "L'analyse convoque trois corpus autour de la même révélation : la variante dʿĀʾisha rapportée par "
        "at-Tirmidhī et al-Ḥākim et d'autres, par la voie de Yaʿlā ibn Shabīb et d'Ibn Mardawayah, par la voie de "
        "Muḥammad ibn Isḥāq, les deux de Hishām, de son père — « Les gens et l’homme divorçaient sa femme autant "
        "qu’il voulait tant qu’elle était sa femme et qu’il la réintégrait pendant sa période d’attente, même s’il "
        "la divorçait cent fois ou plus. » — avec l'homme du dialogue « Par Allah, je ne te divorcerai pas pour que "
        "tu sois clairement séparée de moi et que je ne te reprendrai jamais. » et sa devise « Je te divorce, et "
        "chaque fois que ta période d’attente est sur le point de s’achever, je te réintègre. » — la femme « alla "
        "alors informer le Prophète d’Allah ﷺ, et il se tut jusqu’à ce que le Coran soit révélé » ; puis chez "
        "Ibn Abī Shaybah, d'Abū Ruzayn, l'homme qui demande « Ô Messager d’Allah, qu’en est-il de la parole "
        "d’Allah ? » [al-Baqara (الْبَقَرَة), 229] — « Où est donc le troisième divorce ? » — et la réponse du "
        "Prophète ﷺ : « Le maintien avec bienveillance ou le renvoi avec bienveillance. » ; enfin le compilé de "
        "Mālik au n° 1862 : « L’homme divorçait sa femme, puis la réintégrait, sans avoir besoin d’elle et sans "
        "vouloir la conserver, dans le seul but de prolonger sa période d’attente pour lui nuire » — suivi du "
        "verset des trois menstrues (étiquette arabe du CMS : البقرة الآية 228 — concordante) et du verset du "
        "rachat (étiquette البقرة الآية 229 — concordante), sans étiquette propre dans la couche française. "
        "Deuxième partie — le jugement de la femme divorcée réintégrée après son mariage. Le deuxième hadith "
        "montre que « lorsqu’elle retourne à son premier mari, elle sera avec lui pour ce qui reste du nombre de "
        "ses divorces, une ou deux » — et Mālik a mentionné que « c’était ainsi que faisaient les gens de Médine, "
        "et que c’était la Sunnah parmi eux, sans divergence ». Les écoles : « la majorité des Compagnons, des "
        "Tābiʿūn et des trois Imams étaient de l’avis que le deuxième mari n’annule pas ce qui est en deçà du "
        "troisième divorce, c’est-à-dire qu’il ne supprime pas ces divorces, de sorte que le nombre de divorces ne "
        "recommence pas comme c’est le cas pour celui qui a divorcé sa femme trois fois » ; Abū Ḥanīfa et certains "
        "Compagnons et Tābiʿūn — « Le deuxième annule ce qui est en deçà du troisième comme le troisième. Ainsi, "
        "lorsqu’elle retourne au premier, elle est avec lui sous une protection complète. » "
        "Troisième partie — le jugement du divorce prononcé sous contrainte, en colère et en état d'ivresse. "
        "Aḥmad, Ibn Mājah et d'autres rapportent dʿĀʾisha « un hadith élevé (marfūʿ) » : « Il n’y a pas de divorce "
        "ni de manumission (ʿitāq) sous contrainte (ighlāq). » — le nom s'explique : « la personne sous contrainte "
        "est comme si on lui fermait la porte, et on la serrait jusqu’à ce qu’elle prononce le divorce, de sorte "
        "que son divorce ne produit pas d’effet. » Ibn ʿAbd al-Barr a dit dans al-Istidhkār que « Les savants ont "
        "divergé sur le divorce prononcé sous contrainte » ; Mālik, ash-Shāfiʿī et leurs partisans, al-Ḥasan ibn "
        "Ḥayy, Aḥmad, Isḥāq, Abū Thawr et Dāwūd « sont allés dans le sens que le divorce prononcé sous contrainte "
        "n’est pas obligatoire, ne produit pas d’effet et n’est pas valide, et que leur argument est solide. » — "
        "pour « Certes, Allah a pardonné à ma communauté l’erreur, l’oubli et ce dont elles ont été contraintes. » "
        "rapporté par Ibn Mājah et Aḥmad. Et « c’est cet avis qui a été adopté par la Mudawwana de la famille, "
        "dans l’article 09 » : « La demande d’autorisation pour le divorce de l’ivrogne notoire et du contraint, "
        "ainsi que celui du colérique s’il était dans un état de perte de contrôle, n’est pas acceptée. » — contre "
        "Abū Ḥanīfa et ses partisans : « Le divorce, le mariage et le serment du contraint sont valides, mais sa "
        "vente ne l’est pas. » "
        "La couche arabe poursuit là où la couche française s'arrête (après la sous-section du contraint et du "
        "colérique) : le divorce de l'ivrogne (Ibn ʿAbd al-Barr — les gens de Médine et d'autres ont divergé ; un "
        "groupe rend le divorce de l'ivrogne obligatoire et le lie : Saʿīd ibn al-Musayyab, Sulaymān ibn Yasār, "
        "Mujāhid, az-Zuhrī), puis quatrièmement le jugement de l'incapable de subvenir (Qatāda ; la sunna de "
        "Saʿīd rapportée par Abū az-Zinād ; Mālik — le divorce révocable avec la régence dans la retraite ; "
        "ash-Shāfiʿī — la séparation définitive et la condition de l'imam ; Abū Ḥanīfa et ath-Thawrī — point de "
        "séparation forcée, avec al-Ḥasan, Ibn Shihāb et ʿUmar ibn ʿAbd al-ʿAzīz ; un emplacement de verset "
        "étiqueté البقرة الآية 285, muet au CMS), le bilan, l'exploitation (la Mudawwana classique 2/79 de Dār "
        "al-Kutub al-ʿIlmiyya, légèrement adaptée — le contraint, le fou, le simple d'esprit ; le divorce du "
        "simple d'esprit licite dans le dire de Mālik) et la préparation préalable (la définition linguistique et "
        "terminologique de la ʿidda, sa sagesse et ses types — annonce la leçon suivante du registre, 13124, la "
        "retraite de celle dont le mari est décédé) — paraphrasés sans guillemets (hors corpus de vérification)."
    ),
    "explication": [
        "La leçon 20 succède à la séparation des époux (leçon 19) et remonte à la racine du chapitre : combien de "
        "fois peut-on répudier ? La précédente réglait l'arbitrage des deux familles et les défauts qui requièrent "
        "la séparation ; celle-ci pose le compte des divorces tel que la révélation l'a fixé contre l'abus de "
        "l'époque préislamique, le sort du compte lorsqu'un mariage intermédiaire est passé, et la contrainte qui "
        "retire au divorce son effet. La matière est portée par trois documents du Muwaṭṭaʾ — le n° 1861, le "
        "n° 1858 et le n° 1864 — plus le compilé du n° 1862 dans l'analyse. La leçon est la vingtième du livre, "
        "étiquetée leçon 26 par la couche du manuel ; le badge imprimé du PDF porte (الدرس 23) — premier écart "
        "d'étiquetage de leçon vérifié au badge du manuel imprimé, consigné aux NB. La couche française s'arrête à "
        "la sous-section du contraint et du colérique ; la couche arabe poursuit — l'ivrogne, l'incapable de "
        "subvenir, le bilan, l'exploitation, la préparation.",

        "Les trois objectifs dessinent le dessein : connaître certains jugements relatifs au divorce, comprendre "
        "« certaines coutumes de l’ère préislamique (al-jāhiliyya) que l’Islam a abrogées dans le traitement de la "
        "femme. », saisir « la générosité de la Loi divine et Sa miséricorde dans l’organisation de la relation "
        "conjugale. » Le préambule fonde la licence par la réprobation : le divorce est autorisé bien que son "
        "principe soit la réprobation en raison de ses causes — la parole du Prophète ﷺ « Le plus détesté des "
        "licites auprès d’Allah est le divorce. » rapporté par Abū Dāwūd et Ibn Mājah ; il rompt le lien, mais il "
        "est « lorsque la nécessité s’en fait sentir, un moyen par lequel on peut se libérer d’une cohabitation "
        "difficile ». Puis la couleur de l'époque préislamique : les gens « s’amusaient avec sa question », et "
        "parfois « y recouraient dans l’intention de nuire à la femme et de la presser » — et la Loi divine saine "
        "est descendue, posant ses limites et délivrant la femme de l'injustice qu'elle subissait. La question du "
        "livre découle de là : quels sont les jugements qui organisent le divorce, et quelles limites la Loi a "
        "établies ?",

        "Le n° 1861 ouvre par la coutume : l'homme de l'époque préislamique répudiait et réintégrait avant "
        "l'achèvement de la retraite — « cela lui était permis, même s’il l’avait divorcée mille fois. » — la "
        "femme suspendue à volonté, ni mariée ni divorcée. Puis l'homme du récit : il répudia, laissa courir la "
        "retraite presque achevée, la réintégra, répudia de nouveau et jura « Par Allah, je ne te reprendrai "
        "jamais, et tu ne seras jamais licite pour moi. » — le serment qui prétend fixer à jamais le sort de "
        "l'épouse sans rompre le lien ni lui rendre sa liberté. La réponse vient d'en haut : Allah, que soit béni "
        "et exalté, a révélé — « Il a déjà ordonné (à l’homme) de ne pas s’opposer à la femme » et « et s’il se "
        "sépare d’elle, il ne doit pas la troubler pour la priver de ce qu’Allah lui a assigné, et s’il veut la "
        "réintégrer, il a le droit de le faire, tant qu’ils n’ont pas encore consommé le mariage. Voilà les "
        "limites d’Allah, et ne transgressez pas les limites d’Allah, car celui qui transgresse les limites "
        "d’Allah, ceux-là sont les injustes. » — et Mālik scelle la conséquence : « Les gens prirent le divorce "
        "comme une nouveauté à partir de ce jour, qu’ils aient divorcé ou non. »",

        "La clef de la première partie tient dans le verbe de Mālik : les gens « prirent le divorce comme une "
        "nouveauté » — le compte n'est pas une convention de juristes, il est une limite révélée qui remplace la "
        "coutume ; à partir de ce jour, qu'ils aient divorcé ou non, la règle s'impose à tous, précédents et "
        "suivants. La leçon ne dit pas pourquoi la révélation a réglé le compte à deux ; elle montre ce que le "
        "deux remplace — le mille divorces et la femme suspendue. NB consigné (sans correction) : l'emplacement du "
        "verset porte à trois reprises l'étiquette « verset : 227 » (à deux emplacements) puis « verset 227 » (au "
        "troisième) ; le manuel imprimé (page 126) porte la même étiquette (البقرة الآية : 227) pour une āya dont "
        "le texte imprimé est l'ouverture du verset 229 (الطَّلَاقُ مَرَّتَانِ فَإِمْسَاكٌ بِمَعْرُوفٍ أَوْ "
        "تَسْرِيحٌ بِإِحْسَانٍ) ; le vrai verset 227 porte au cache coranique la décision au divorce et "
        "l'audience d'Allah ; le texte composite porté par la couche française (dont la fin correspond à la fin du "
        "verset 229) ne correspond ni au vrai verset 227 ni à l'āya imprimée — 50ᵉ écart d'étiquetage du registre "
        "(une divergence, répétée à trois emplacements).",

        "L'analyse élargit le corpus : le hadith est rapporté par at-Tirmidhī et al-Ḥākim et d'autres, par la voie "
        "de Yaʿlā ibn Shabīb et d'Ibn Mardawayah, par la voie de Muḥammad ibn Isḥāq, les deux de Hishām, de son "
        "père, de ʿĀʾisha — « Les gens et l’homme divorçaient sa femme autant qu’il voulait tant qu’elle était sa "
        "femme et qu’il la réintégrait pendant sa période d’attente, même s’il la divorçait cent fois ou plus. » "
        "Le dialogue de l'homme porte la mécanique de l'abus : il refuse la séparation qui libérerait la femme "
        "(« Par Allah, je ne te divorcerai pas pour que tu sois clairement séparée de moi et que je ne te "
        "reprendrai jamais. ») et refuse le lien qui l'engagerait (« Je te divorce, et chaque fois que ta période "
        "d’attente est sur le point de s’achever, je te réintègre. ») — la femme « alla alors informer le "
        "Prophète d’Allah ﷺ, et il se tut jusqu’à ce que le Coran soit révélé » — le silence du Prophète ﷺ qui "
        "attend la révélation est lui-même une doctrine : le compte ne se fixe pas par humeur, il attend la limite "
        "divine.",

        "Chez Ibn Abī Shaybah, d'Abū Ruzayn, l'homme qui demande « Ô Messager d’Allah, qu’en est-il de la parole "
        "d’Allah ? » [al-Baqara (الْبَقَرَة), 229] — puis « Où est donc le troisième divorce ? » — et la réponse "
        "du Prophète ﷺ : « Le maintien avec bienveillance ou le renvoi avec bienveillance. » La réponse ne donne "
        "pas un nombre ; elle reprend la formule coranique du maintien ou du renvoi avec bienveillance (2:231 au "
        "cache coranique) — le troisième divorce n'est pas une chose à trouver, le compte s'arrête où la Loi l'a "
        "posé. La question du troisième et la réponse versétique préparent la doctrine du compté que la leçon a "
        "déjà posée : « le divorce soit prononcé deux fois » avec réintégration à chaque fois, la troisième qui "
        "sépare définitivement.",

        "Le compilé de Mālik au n° 1862 porte la nuance morale : « L’homme divorçait sa femme, puis la "
        "réintégrait, sans avoir besoin d’elle et sans vouloir la conserver, dans le seul but de prolonger sa "
        "période d’attente pour lui nuire » — la réintégration n'est plus l'exercice du droit, elle est la machine "
        "à prolonger le suspense. Le même document porte deux versets — celui des trois menstrues (l'étiquette "
        "arabe du CMS porte (البقرة الآية 228), concordante) qui donne à l'époux le droit de reprendre « si ils "
        "veulent une réconciliation » et élève les hommes d'un degré — « Et les femmes ont des droits similaires, "
        "conformément aux convenances, mais les hommes ont un degré plus élevé. » — et celui du rachat (étiquette "
        "البقرة الآية 229, concordante) qui autorise la séparation quand les limites d'Allah ne peuvent plus être "
        "observées. La couche française ne porte pas d'étiquette propre sur ces deux versets — l'attribution « "
        "Muwaṭṭaʾ, n° 1862 » les couvre (NB consigné).",

        "Le n° 1858 est la règle du compte survivant au mariage intermédiaire : quatre maîtres de Médine — "
        "Saʿīd ibn al-Musayyab, Humayd ibn ʿAbd al-Raḥmān ibn ʿAwf, ʿUbayd Allāh ibn ʿAbd Allāh ibn ʿUtbah ibn "
        "Masʿūd et Sulaymān ibn Yasār — tous d'Abū Hurayra, disant de ʿUmar ibn al-Khaṭṭāb : « Quelle que soit la "
        "femme que son mari a divorcée une ou deux fois, puis qu’il a laissée jusqu’à ce qu’elle soit licite et "
        "qu’elle épouse un autre mari, et que celui-ci meure d’elle ou la divorce, puis que son premier mari "
        "l’épouse, alors elle sera avec lui pour ce qui reste de ses divorces, une ou deux. » — et Mālik scelle : "
        "« Et c’est la Sunnah parmi nous, sur laquelle il n’y a pas de divergence. » Le lexique du manuel porte "
        "les clefs du récit : « jusqu’à ce qu’elle sorte de sa période d’attente (ʿidda). », « c’est-à-dire que le "
        "deuxième mari meurt. », « c’est-à-dire une ou deux divorces. » — le compte est attaché à la personne du "
        "premier mari, non au lien lui-même : il attend ce qui reste.",

        "La doctrine se ramasse en deux rangs : « la majorité des Compagnons, des Tābiʿūn et des trois Imams "
        "étaient de l’avis que le deuxième mari n’annule pas ce qui est en deçà du troisième divorce, c’est-à-dire "
        "qu’il ne supprime pas ces divorces, de sorte que le nombre de divorces ne recommence pas comme c’est le "
        "cas pour celui qui a divorcé sa femme trois fois » ; Abū Ḥanīfa et certains Compagnons et Tābiʿūn — « Le "
        "deuxième annule ce qui est en deçà du troisième comme le troisième. Ainsi, lorsqu’elle retourne au "
        "premier, elle est avec lui sous une protection complète. » L'enjeu est le sens même du compte : pour la "
        "majorité, les deux répudiations prononcées sont des faits consommés que rien n'efface — pas même le "
        "mariage intermédiaire ; pour Abū Ḥanīfa, le mariage intermédiaire régénère la protection complète et "
        "efface le compte. La leçon consigne les deux rangs sans les départager ; les « trois Imams » ne sont pas "
        "nommés (NB consigné).",

        "Le n° 1864 ouvre la troisième question (l'incapable de subvenir) sans la développer dans la couche "
        "française : Saʿīd ibn al-Musayyab disait « Si un homme ne trouve pas de quoi subvenir aux besoins de sa "
        "femme, on sépare entre eux. » — et Mālik scelle : « Et c’est ainsi que j’ai trouvé les gens de science "
        "dans notre pays. » Le sceau n'est pas une règle, il est l'attestation de la pratique des gens de science "
        "du pays — la sunna comme mœurs établies. La couche arabe porte la doctrine complète (quatrièmement) : "
        "Qatāda et la sunna de Saʿīd rapportée par Abū az-Zinād ; Mālik — le divorce révocable avec la régence "
        "dans la retraite ; ash-Shāfiʿī — la séparation définitive ; Abū Ḥanīfa et ath-Thawrī — point de "
        "séparation forcée, avec al-Ḥasan, Ibn Shihāb et ʿUmar ibn ʿAbd al-ʿAzīz ; et un emplacement de verset "
        "étiqueté (البقرة الآية 285), muet au CMS (NB consigné).",

        "Le divorce du contraint ferme la couche française : Aḥmad, Ibn Mājah et d'autres rapportent dʿĀʾisha "
        "« un hadith élevé (marfūʿ) » : « Il n’y a pas de divorce ni de manumission (ʿitāq) sous contrainte "
        "(ighlāq). » — le nom s'explique par l'image : « la personne sous contrainte est comme si on lui fermait "
        "la porte, et on la serrait jusqu’à ce qu’elle prononce le divorce, de sorte que son divorce ne produit "
        "pas d’effet. » Ibn ʿAbd al-Barr a dit dans al-Istidhkār que « Les savants ont divergé sur le divorce "
        "prononcé sous contrainte » ; Mālik, ash-Shāfiʿī et leurs partisans, al-Ḥasan ibn Ḥayy, Aḥmad, Isḥāq, "
        "Abū Thawr et Dāwūd « sont allés dans le sens que le divorce prononcé sous contrainte n’est pas "
        "obligatoire, ne produit pas d’effet et n’est pas valide, et que leur argument est solide. » — la preuve : "
        "« Certes, Allah a pardonné à ma communauté l’erreur, l’oubli et ce dont elles ont été contraintes. » "
        "rapporté par Ibn Mājah et Aḥmad. Et l'écho moderne : « c’est cet avis qui a été adopté par la Mudawwana "
        "de la famille, dans l’article 09 » — « La demande d’autorisation pour le divorce de l’ivrogne notoire et "
        "du contraint, ainsi que celui du colérique s’il était dans un état de perte de contrôle, n’est pas "
        "acceptée. » — contre Abū Ḥanīfa et ses partisans : « Le divorce, le mariage et le serment du contraint "
        "sont valides, mais sa vente ne l’est pas. »",

        "La couche arabe poursuit après le contraint et le colérique : le divorce de l'ivrogne (Ibn ʿAbd al-Barr — "
        "les gens de Médine et d'autres ont divergé sur le divorce de l'ivrogne ; un groupe le rend obligatoire et "
        "le lie : Saʿīd ibn al-Musayyab, Sulaymān ibn Yasār, Mujāhid, az-Zuhrī ; l'objection formulée contre qui "
        "tient l'éghlāq pour la seule colère — le divorce des gens tombe d'ordinaire dans la colère, et la parole "
        "d'Ibn ʿAbbās et dʿĀʾisha qui fait tomber le divorce des deux en colère), le bilan (le compte des divorces "
        "quand le deuxième mari est passé ; le statut du divorce du contraint chez les Mālikites et leur preuve ; "
        "le détail de la divergence sur l'incapacité de subvenir), l'exploitation (la Mudawwana classique 2/79 de "
        "Dār al-Kutub al-ʿIlmiyya, légèrement adaptée — le contraint, le fou, le simple d'esprit ; le divorce du "
        "simple d'esprit licite dans le dire de Mālik) et la préparation préalable (la définition linguistique et "
        "terminologique de la ʿidda, sa sagesse et ses types — annonce la leçon suivante du registre, 13124, la "
        "retraite de celle dont le mari est décédé) — paraphrasées sans guillemets (hors corpus de vérification).",
    ],
    "points": [
        "Fil du livre : après la séparation des époux pour préjudice ou vice (leçon 19), la leçon remonte à la "
        "racine du chapitre — le compte des divorces fixé par la révélation contre l'abus préislamique, le compte "
        "survivant au mariage intermédiaire, le divorce du contraint ; la leçon est la vingtième du livre, "
        "étiquetée leçon 26 par la couche du manuel — le badge imprimé du PDF porte (الدرس 23), écart consigné "
        "(première vérification des badges imprimés).",
        "Les objectifs et le tamhīd : connaître certains jugements relatifs au divorce, comprendre les coutumes "
        "préislamiques abrogées dans le traitement de la femme, saisir la générosité de la Loi divine ; le divorce "
        "licite mais réprobation par « Le plus détesté des licites auprès d’Allah est le divorce. » (Abū Dāwūd et "
        "Ibn Mājah) ; la jāhiliyya « s’amusaient avec sa question » et « y recouraient dans l’intention de nuire "
        "à la femme et de la presser ».",
        "Le n° 1861 : la coutume — réintégration avant l'achèvement de la retraite « même s’il l’avait divorcée "
        "mille fois. » — la femme suspendue, ni mariée ni divorcée ; l'homme du serment « Par Allah, je ne te "
        "reprendrai jamais, et tu ne seras jamais licite pour moi. »",
        "La révélation : l'interdit de nuire à l'épouse pour la priver de son dû, l'interdit de retenir pour "
        "nuire — « Voilà les limites d’Allah, et ne transgressez pas les limites d’Allah, car celui qui "
        "transgresse les limites d’Allah, ceux-là sont les injustes. » — et le scellement : « Les gens prirent le "
        "divorce comme une nouveauté à partir de ce jour, qu’ils aient divorcé ou non. » — le compte devient "
        "limite divine pour tous.",
        "Le compte fixé : deux répudiations avec réintégration à chaque fois, la troisième qui sépare "
        "définitivement — « ne lui est plus licite jusqu’à ce qu’elle épouse un autre mari. » — la barrière levée "
        "contre le mille divorces.",
        "La variante dʿĀʾisha (at-Tirmidhī, al-Ḥākim, Ibn Mardawayah, Yaʿlā ibn Shabīb, Muḥammad ibn Isḥāq — les "
        "deux de Hishām, de son père) : « même s’il la divorçait cent fois ou plus » ; le dialogue de l'homme qui "
        "refuse la séparation et refuse le lien ; la femme « alla alors informer le Prophète d’Allah ﷺ, et il se "
        "tut jusqu’à ce que le Coran soit révélé » — le silence qui attend la limite divine.",
        "Ibn Abī Shaybah, d'Abū Ruzayn : « Où est donc le troisième divorce ? » — « Le maintien avec bienveillance "
        "ou le renvoi avec bienveillance. » — la réponse reprend la formule coranique (2:231 au cache) ; le "
        "troisième n'est pas une chose à trouver.",
        "Le n° 1862 : la réintégration « sans avoir besoin d’elle et sans vouloir la conserver, dans le seul but "
        "de prolonger sa période d’attente pour lui nuire » ; deux versets concordants portés par les étiquettes "
        "arabes du CMS (2:228 les trois menstrues, 2:229 le rachat), sans étiquette propre dans la couche "
        "française ; le double « si » (« si ils veulent une réconciliation ») recopié tel quel.",
        "Le n° 1858 : « elle sera avec lui pour ce qui reste de ses divorces, une ou deux. » — quatre maîtres de "
        "Médine d'Abū Hurayra de ʿUmar ; le sceau de Mālik « Et c’est la Sunnah parmi nous, sur laquelle il n’y a "
        "pas de divergence. » — le compte attaché à la personne du premier mari.",
        "Les écoles : la majorité des Compagnons, des Tābiʿūn et des trois Imams — le deuxième mari n'annule pas "
        "ce qui est en deçà du troisième, le compte ne recommence pas ; Abū Ḥanīfa et certains Compagnons et "
        "Tābiʿūn — tout annule, « sous une protection complète » ; l'enjeu : le compte est un fait consommé que "
        "rien n'efface (la majorité) ou une protection régénérée par le mariage (Abū Ḥanīfa) ; les « trois "
        "Imams » sans nom, consignés tels quels.",
        "Le n° 1864 : l'incapable de subvenir — « Si un homme ne trouve pas de quoi subvenir aux besoins de sa "
        "femme, on sépare entre eux. » — « Et c’est ainsi que j’ai trouvé les gens de science dans notre pays. » "
        "— le sceau atteste la pratique des gens de science ; la doctrine complète reste dans la couche arabe "
        "(quatrièmement).",
        "Le divorce du contraint : « Il n’y a pas de divorce ni de manumission (ʿitāq) sous contrainte (ighlāq). » "
        "(ʿĀʾisha, marfūʿ, Aḥmad et Ibn Mājah) — l'image de la porte fermée ; Ibn ʿAbd al-Barr dans al-Istidhkār — "
        "pas obligatoire, pas d'effet, pas valide, argument solide (Mālik, ash-Shāfiʿī, al-Ḥasan ibn Ḥayy, Aḥmad, "
        "Isḥāq, Abū Thawr, Dāwūd) ; la preuve « Certes, Allah a pardonné à ma communauté l’erreur, l’oubli et ce "
        "dont elles ont été contraintes. »",
        "L'écho moderne et la suite : la Mudawwana de la famille, article 09 — « La demande d’autorisation pour le "
        "divorce de l’ivrogne notoire et du contraint, ainsi que celui du colérique s’il était dans un état de "
        "perte de contrôle, n’est pas acceptée. » — contre Abū Ḥanīfa (le divorce, le mariage et le serment du "
        "contraint valides, la vente non) ; la couche arabe poursuit — l'ivrogne, l'exploitation de la Mudawwana "
        "classique 2/79 (le contraint, le fou, le simple d'esprit) — et la préparation préalable requiert la "
        "définition de la ʿidda, sa sagesse et ses types — annonce 13124 (la retraite de celle dont le mari est "
        "décédé).",
    ],
    "vocabulaire": [
        {"ar": "العدة", "translit": "ʿidda",
         "fr": "la période d'attente : le temps qui reste au lien après la répudiation révocable — « avant que ne "
               "s’achève sa période d’attente (ʿidda) » ; « jusqu’à ce qu’elle sorte de sa période d’attente "
               "(ʿidda). » (lemme du lexique du manuel)"},
        {"ar": "الجاهلية", "translit": "al-jāhiliyya",
         "fr": "l'ère préislamique : « les gens à l’époque préislamique s’amusaient avec sa question » et parfois "
               "« y recouraient dans l’intention de nuire à la femme et de la presser » — le monde que la révélation "
               "du compte vient abroger"},
        {"ar": "الإغلاق", "translit": "ighlāq",
         "fr": "la contrainte : « sous contrainte (ighlāq) » — « la personne sous contrainte est comme si on lui "
               "fermait la porte, et on la serrait jusqu’à ce qu’elle prononce le divorce » — le nom porte l'image "
               "de la porte fermée"},
        {"ar": "العتاق", "translit": "ʿitāq",
         "fr": "l'affranchissement : « Il n’y a pas de divorce ni de manumission (ʿitāq) sous contrainte (ighlāq). » "
               "— le divorce et l'affranchissement jumelés dans la même règle du contraint"},
        {"ar": "المرفوع", "translit": "marfūʿ",
         "fr": "le hadith élevé : « un hadith élevé (marfūʿ) » — remonté jusqu'au Prophète ﷺ par ʿĀʾisha — le grade "
               "du dire avant sa chaîne de transmission"},
        {"ar": "بمعروف", "translit": "bi-maʿrūf",
         "fr": "avec bienveillance : « c’est-à-dire sans nuire. » (la glose du manuel) ; « Le maintien avec "
               "bienveillance ou le renvoi avec bienveillance. » (la réponse du Prophète ﷺ à la question du "
               "troisième divorce)"},
        {"ar": "حتى تحل", "translit": "ḥatta tuḥallu",
         "fr": "« jusqu’à ce qu’elle sorte de sa période d’attente (ʿidda). » — le lemme du lexique du manuel : "
               "elle redevient licite au mariage quand la retraite est sortie"},
        {"ar": "فيموت عنها", "translit": "fa-yamūtu ʾalayhā",
         "fr": "« c’est-à-dire que le deuxième mari meurt. » — le lemme du lexique du manuel : la mort du second "
               "époux rouvre la porte au retour du premier — « pour ce qui reste de ses divorces »"},
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
com[DOCID] = norme_entree(E_13122)

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
    ('13121 — la leçon précédente immédiate (l’arbitrage des ḥakamayn)', 'ḥakamayn' in fr('13121')),
    ('13122 — la leçon même (le contraint, les deux en colère et les deux ivres)', 'contraint' in fr('13122') and 'ivres' in fr('13122')),
    ('13117 — le recueil de la retraite (leçon 18), où la retraite des non-réglées fut réglée (les qurūʾ)', 'qurūʾ' in fr('13117')),
    ('13114 — le divorce de la réglée (leçon 16), où la retraite comptée en cycles fut posée', 'cycles' in fr('13114')),
    ('13115 — la retraite dans sa demeure et la pension (leçon 17), où Fatima bint Qays fut rencontrée', 'Fatima' in fr('13115')),
    ('12966 — le corpus califal du ẓihār, où Abū Hurayra fut déjà rencontré (le n° 1858 court par Abū Hurayra)', 'Hurayra' in fr('12966')),
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
