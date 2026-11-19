# -*- coding: utf-8 -*-
"""R762 — commentaires vague 17 hadith-5ep pdf-24 (lecon 24 : Preserver les
commandements de Dieu — hifz awamir Allah ta'ala).

METHODE (precedent R753-R761) :
  - extraction non lossy de la lecon 24 FR (htmlFr du registre, 35 947 car
    html, 30 820 car texte) ;
  - TIRAGE DISPONIBLE (content/textbooks-src/hadith-5-ibtidai_text.pdf,
    /tmp/r761-tirage.txt) : bloc lecon 24 verifie (pages 131-133 du manuel) :
    matn p.131 (ya gulamu inni u'allimuka kalimatin : ihfazi llaha yahfazka /
    ihfazi llaha tajidhu tujahaka / idha sa'alta fas'ali llaha wa-idha
    sta'tanta fasta'in billah / ... rufi'ati l-aqlamu wa-^affat as-suhuf
    [سنن الترمذي]) ; notice Ibn 'Abbas (ibn 'am an-nabiyy, wulida qabla
    l-hi^ra bi-talati sinin, manaqibuhu aktharu min an tuhsara,
    « Allahumma faqqihhu fi d-dini wa-'allimhu t-ta'wila » [المعجم الصغير
    للطبراني], al-hikma marratayn, tuwuffiya 'am tamaniyatin wa-sittin) ;
    gloses p.132 (ihfaz Allah : ihfaz awamir Allah wa-nahiyahi bi-l-imtital ;
    tajidhu tujahaka : talqahu amamaka fi kulli ma turidu min ^albi hayrin aw
    daf'i makruh ; katabahu llahu laka : qaddarahu laka ; ^affat as-suhuf :
    al-murad bihi an ma qaddarahu llahu la tabdila lahu illa bi-idnih ;
    ta'arrafa ila llah : qum bi-huquqih wa-wa^ibatih ; fi r-raha' : fi
    s-sihhati wa-l-^ina ; ma 'ahta'aka lam yakun li-yusibak : ma qaddara llahu
    an yuhti'aka lan yusibaka 'abadan ; al-fara^ ma'a l-karab : dahab
    a-siddati wa-zawalaha yakunu ba'da l-'usr) ; istihla^ al-madamin ;
    tahil awwalan (ma'na hifz Allah wa-tamaratih — at-talata lladina asabahum
    l-matru fa-'awaw ila ^arin — ma^hura fi s-sahihayn) p.133.
  - NB CONSIGNE (cinq, tous verifiés web) : les références imprimées de la
    lecon divergent du mushaf standard : [Gafir : 13] -> le verset qui porte
    « fa-du llaha muhlisina lahu d-din » est le 14 ; [Luqman : 15] -> le
    verset du grain de moutarde (ya bunayya innaha in taku mitqala habbatin
    min hardalin...) est le 16 ; [Al-Baqara : 154-156] -> wa lanabluwannakum
    ... 'ula'ika 'alayhim salawatun = 155-157 ; [Az-Zumar : 11] -> innama
    yuwaffa s-sabiruna a^rahum bi-^ayri hisab = 10 ; [Al-An'am : 80-83] ->
    inni wa^ahtu wa^hiya... 'ula'ika lahumu l-amnu = 79-82 (versets cités).
    At-Talaq : 3 (wa-man yatawakkal 'ala llahi fa-huwa hasbuh) coincide : pas
    de NB. Regle R739/R742 (precedents pdf-15, pdf-22) : NB en langage
    planaire, reference imprimée / verset qui porte ces paroles.
  - recoupements de cette vague (verifiés verbatim au registre) :
    (a) boucle EXACTE : l'i'dad de la lecon 23 demande « il est devant toi »
        (tu^ahaka), « les feuilles se sont dessechees » (^affat as-suhuf),
        « connais Dieu » (ta'arrafa ila llah), « ce qui t'a ete epargne ne
        devait pas t'atteindre » (ma 'ahta'aka lam yakun li-yusibak) + « le
        sens de la garde de Dieu et de l'attachement a Lui », « son merite et
        son fruit » — les gloses de la lecon 24 les portent un a un ;
    (b) boucle coranique : le credo du hadit de ^ibril (lecons 3-4) porte
        « que tu croies au decret, en son bien et en son mal » ; la lecon 8
        (Le decret et la predestination) enseigne pour elle-meme ce que la
        lecon 24 reprend comme pilier de la foi ;
    (c) noms deja croises : Ibn 'Abbas lecon 3 (« Par une langue qui
        questionne et un coeur qui comprend » [Fath al-Bari — Tahrir al-matn
        — al-Musnad de l'imam Ahmad]) et lecon 15 (son istitmar sur Baqara —
        Sa'd ibn Abi Waqqas) ; Luqman lecons 4 (Luqman 33, l'Heure) et 17
        (sa sagesse [Muwatta']) ; al-Hakim deja nomme lecon 1 (les recueils
        des Quarante) ; la lecon 3 nommait deja « la religion de l'islam,
        designee comme la hanifiyya tolerante et la communaute (milla)
        d'Ibrahim » — le hanif des versets de l'istitmar porte le meme nom ;
    (d) AUCUN ordinal des Quarante revendique (le chapeau du htmlFr n'en
        porte pas — precedent R758-R761) ;
    (e) matns cites UNIQUEMENT avec leur source lecon (Sunan d'at-Tirmidi
        pour le matn ; Al-Mustadrak d'al-Hakim pour la seconde version ;
        Al-Mu'am a-sa'ir d'at-Tabarani pour l'invocation ; les deux Sahih
        pour la parabole de la grotte — mention du manuel).
  - translitteration du commentaire en convention corpus (ʾ U+02BE / ʿ
    U+02BF), les lecons htmlFr portant ' U+2019 — precedent R753-R761. Le
    vocabulaire arabe est SANS harakat (precedent pdf-19/pdf-22/pdf-23).
Garde-fous de comm-r761.py repris (typographie FR, arabe entre parentheses
seulement, vocab ar sans harakat, guillemets apparies) + fenetre de mots
1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_24 = {
    "auteur": "IA-1, tour R762",
    "resume": "Guide de lecture de la leçon 24 (Préserver les commandements de Dieu — ḥifẓ ʾawāmiri llāhi taʾālā (حفظ أوامر الله تعالى)) : le commentaire du hadīth d'Abū al-ʾAbbās ʿAbd Allāh ibn ʿAbbās — « que Dieu soit satisfait d'eux deux » — « Ô jeune garçon, je t'enseigne des paroles : garde les commandements de Dieu, Il te gardera » [Sunan d'at-Tirmiḏī], épaulé par la version du Mustadrak d'al-Ḥākim. Trois objectifs : connaître le sens de la garde de Dieu, en réaliser le fruit et le lien avec la foi au décret, s'approprier les finalités légales du commandement. La clef : la réciprocité de la garde — garder les ordres d'Allah pour être gardé par Lui ; l'analyse déroule quatre axes — le sens de la garde et ses fruits, la confiance en Dieu, la foi au décret, le soulagement avec la patience. La préparation ouvre la leçon 25 (la pudeur).",
    "explication": [
        "Après la piété et le bon caractère (leçon 23), la leçon 24 installe un nouveau hadīth des Quarante de l'imam al-Nawawī, avec le commentaire d'Ibn Daqīq al-ʾĪd : celui d'Abū al-ʾAbbās ʿAbd Allāh ibn ʿAbbās — « que Dieu soit satisfait d'eux deux » — « Ô jeune garçon, je t'enseigne des paroles : garde les commandements de Dieu, Il te gardera ; garde les commandements de Dieu, tu Le trouveras devant toi ; si tu demandes, demande à Dieu ; et si tu cherches secours, cherche-le auprès de Dieu » (yā ġulāmu ʾinnī ʾuʾallimuka kalimātin (يَا غُلَامُ، إِنِّي أُعَلِّمُكَ كَلِمَاتٍ)) [Sunan d'at-Tirmiḏī] ; le matn continue par le décret — « sache que la communauté, si elle se rassemblait pour te faire profiter de quelque chose, ne te ferait profiter que de ce que Dieu a écrit pour toi » — et se scelle : « les calames ont été levés et les feuilles se sont desséchées ».",
        "Le tamhīd (تَمْهِيدٌ) donne le cadre : « que le serviteur soit enveloppé d'une garde divine englobante » (ḥifẓin ʾilāhiyyin šāmilin (حِفْظٍ إِلَهِيٍّ شَامِلٍ)) « qui le rende sincère dans sa foi, apaisé dans son for intérieur, droit dans sa condition et favorisé dans son œuvre », « en secret comme au grand jour, dans la difficulté comme dans l'aisance » ; la question ouvre le cours : « Qu'est-ce donc que la garde de Dieu ? ».",
        "Le sabab est porté par le matn : « Je me tenais un jour derrière le Prophète — prière et salut d'Allah sur lui — » — une leçon donnée à hauteur d'enfant, « Ô jeune garçon ».",
        "Une seconde version appuie la première (wa-fī riwāyati ġayri t-Tirmiḏī (وَفِي رِوَايَةِ غَيْرِ التِّرْمِذِيِّ)) : « Garde les commandements de Dieu, tu Le trouveras devant toi ; connais Dieu dans l'aisance, Il te connaîtra dans la difficulté » ; « sache que la victoire est avec la patience, que le soulagement est avec l'angoisse et qu'avec la difficulté est la facilité » [Al-Mustadrak d'al-Ḥākim] — déjà nommé à la leçon 1 parmi les auteurs de recueils des Quarante.",
        "La notice du transmetteur (tarǧamat ar-rāwī (تَرْجَمَةُ الرَّاوِي)) : « le fils du cousin du Prophète — prière et salut d'Allah sur lui — », « l'une des sommités parmi les Compagnons » ; « Il naquit trois ans avant l'Hégire » — l'enfant du matn. Le Prophète « le bénit en touchant son palais de sa salive » et invoqua : « Seigneur, donne-lui la compréhension de la religion et enseigne-lui l'interprétation » [Al-Muʾǧam aṣ-ṣaġīr d'aṭ-Ṭabarānī] ; il fut « l'océan de la communauté, son docte et l'interprète du Coran » et « il mourut — que Dieu soit satisfait de lui — l'an soixante-huit de l'Hégire ». Déjà croisé : leçon 3 — « Par une langue qui questionne et un cœur qui comprend » — et leçon 15.",
        "L'explication (aš-šarḥ (الشَّرْحُ)) porte les gloses, clef de la leçon. « Garde les commandements de Dieu » (iḥfaẓi llāh (اِحْفَظِ اللهَ)) : « garde les ordres de Dieu et Ses interdits en te conformant » (iḥfaẓ ʾawāmira llāhi wa-nawāhiyahi bi-l-imtiṯāl (اِحْفَظْ أَوَامِرَ اللهِ وَنَوَاهِيهِ بِالِامْتِثَالِ)). « Tu Le trouveras devant toi » (taǧidhu tuǧāhaka (تَجِدْهُ تُجَاهَكَ)) : « tu Le rencontres face à toi dans tout ce que tu veux obtenir comme bien ou repousser comme mal ». « Les feuilles se sont desséchées » (ǧaffati ṣ-ṣuḥuf (جَفَّتِ الصُّحُفُ)) : « l'on vise par là que ce que Dieu a décrété ne subit pas de modification sans Sa permission ».",
        "Les gloses de la seconde version suivent : « Connais Dieu » (taʾarrafa ʾilā llāh (تَعَرَّفْ إِلَى اللهِ)) : « acquitte-toi de Ses droits et de Ses obligations » ; « ce qui t'a été épargné ne devait pas t'atteindre » (mā ʾaḫṭaʾaka lam yakun li-yuṣībak (مَا أَخْطَأَكَ لَمْ يَكُنْ لِيُصِيبَكَ)) : « ce que Dieu a décrété de t'épargner ne t'atteindra jamais » ; « le soulagement est avec l'angoisse » (wa-anna l-faraja maʿa l-karab (وَأَنَّ الْفَرَجَ مَعَ الْكَرْبِ)) : « la disparition de la dureté et sa dissolution adviennent après la gêne ».",
        "L'analyse (at-taḥlīl (التَّحْلِيل)) déroule quatre axes. Premier : le sens de la garde et ses fruits — « œuvre pour Dieu dans l'obéissance et ne t'appuie pas sur le fait de Le désobéir » ; « tu Le trouveras alors avec toi dans les épreuves : Il te garde par Sa garde et veille sur toi par Sa sollicitude » ; « comme il advint des trois hommes que la pluie surprit et qui se réfugièrent dans une grotte » ; « une pierre dévala et se referma sur eux » ; « Voyez quelle œuvre salutaire vous avez accomplie, puis implorez Dieu — Très-Haut — par elle : Il vous délivrera » ; chacun évoque « une bonne action accomplie auparavant pour son Seigneur » ; « la pierre roula loin d'eux et ils sortirent en marchant » — « Leur récit est célèbre dans les deux Ṣaḥīḥ » ; conclusion : Dieu est pour lui en ce bas-monde « par la rectitude de sa condition », et dans l'au-delà « par la rétribution et la bonne agréation ».",
        "Deuxième : la confiance en Dieu — Très-Haut — et l'attachement à Lui — une guidance « vers la confiance en Dieu — Très-Haut — seul », « de ne s'en remettre à nul autre que Lui et de ne s'attacher à autre que Lui dans la totalité de ses affaires, les minimes comme les considérables » ; « demande à Dieu seul et cherche secours auprès de Lui à l'exclusion de tout autre — d'un humain ou d'un génie, d'un vivant ou d'un mort —, afin de Lui préserver le droit de l'adoration pure » ; « à la mesure de ce que la personne s'appuie sur autre que Dieu — Très-Haut — par sa quête, son cœur ou son espoir, elle a détourné son visage de son Seigneur ». Appuis : « Quiconque place sa confiance en Dieu, Il lui suffit » [Aṭ-Ṭalāq : 3] et « Invoquez Dieu en Lui vouant une religion pure » [Ġāfir : 13] — NB de lecture : la référence imprimée porte le verset 13 ; le verset qui porte ces paroles est le 14 de la sourate Ġāfir (vérifié web).",
        "Troisième : la foi au décret de Dieu et à Sa prédestination — « un pilier fondamental des articles de la foi », « celui-là même qui fait son fruit que le croyant ne craigne et n'adresse sa demande à nul autre que Dieu » ; « aucun bien ni aucun mal ne l'atteint sinon par le décret de Dieu, que nul ne peut faire descendre ni repousser » ; « tout procède de Son décret et de Sa décision, dont il faut se satisfaire et auxquels il faut se soumettre » — les calames levés confirment « ni abrogation ni modification ». Boucle : les leçons 3-4 portaient déjà « et que tu croies au décret, en son bien et en son mal », et la leçon 8 enseignait ce pilier pour lui-même.",
        "Quatrième : le soulagement est avec la patience — l'autre version « avertit que les hommes en ce bas-monde — et les vertueux d'entre eux en premier lieu — sont exposés aux épreuves et aux tests ». Appuis : « Nous vous éprouverons certes par quelque chose de la peur, de la faim et d'une diminution des biens, des personnes et des fruits » [Al-Baqara : 154-156] — NB de lecture : la référence imprimée porte les versets 154-156 ; les versets qui portent ces paroles sont les 155 à 157 de la sourate al-Baqara (vérifié web) — et « Les endurants ne recevront leur récompense que sans compter » [Az-Zumar : 11] — NB de lecture : la référence imprimée porte le verset 11 ; le verset qui porte ces paroles est le 10 de la sourate Az-Zumar (vérifié web).",
        "Ce que le hadīth nous apprend (wa-mimmā yustafād min al-ḥadīṯ (وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ)) en trois enseignements. Premier : « la certitude que l'homme ne saurait manquer ce qui lui a été décrété et n'atteindra point ce qui ne lui a pas été décrété — qu'il fasse donc preuve de mesure dans la quête », « comme dans le testament de Luqmān à son fils » : « Ô mon fils, fût-elle du poids d'un grain de moutarde, fût-elle dans un rocher, dans les cieux ou dans la terre, Dieu la fera venir — Dieu est Subtil et Informé » [Luqmān : 15] — NB de lecture : la référence imprimée porte le verset 15 ; le verset qui porte ces paroles est le 16 de la sourate Luqmān (vérifié web). Deuxième : l'éducation de l'âme à la confiance en Dieu, « le refoulement du désespoir et la patience dans l'épreuve ». Troisième : « la douceur et la souplesse dans l'éducation de l'enfant et son instruction ».",
        "L'évaluation (at-taqwīm (التَّقْوِيم)) donne trois tâches : le sens de « Garde les commandements de Dieu, Il te gardera » ; « J'expose la manière de s'attacher à Dieu » ; « Je mets en harmonie le sens de » la parole du décret « et le profit que les gens tirent les uns des autres ». L'exploitation (al-istiṯmār (الِاسْتِثْمَارُ)) donne son texte — le récit d'Ibrāhīm l'Ami : « Je tourne mon visage, en pur monothéiste, vers Celui qui a créé les cieux et la terre, et je ne suis point des associateurs » ; « Ceux qui ont cru et n'ont point enveloppé leur foi d'iniquité, ceux-là ont la sécurité et ce sont eux les bien-guidés » [Al-Anʾām : 80-83] — NB de lecture : la référence imprimée porte les versets 80-83 ; les versets qui portent ces paroles sont les 79 à 82 de la sourate Al-Anʾām (vérifié web) ; la leçon 3 nommait déjà « la ḥanīfiyya tolérante » — le ḥanīf de ces versets porte le même nom.",
        "La préparation (al-ʾiʾdād al-qabliyy (الْإِعْدَادُ الْقَبْلِيُّ)) enjoint « Je mémorise le hadith de la leçon suivante, puis je fais ce qui suit » : « J'explique » deux fragments — « le langage de la prophétie première », « tu ne rougis pas, fais donc ce que tu veux » — puis « J'expose le mérite de la pudeur et les manifestations de la pudeur » ; boucle : l'iʾdād de la leçon 23 demandait « il est devant toi », « les feuilles se sont desséchées », « connais Dieu » et « ce qui t'a été épargné ne devait pas t'atteindre » — les gloses de la leçon 24 les portent un à un.",
    ],
    "points": [
        "La place : leçon 24, après la piété et le bon caractère — le hadīth du fils du cousin du Prophète [Sunan d'at-Tirmiḏī], épaulé par la version du Mustadrak d'al-Ḥākim ; plan : le sens de la garde et ses fruits, la confiance en Dieu, la foi au décret, le soulagement avec la patience.",
        "La clef : la réciprocité de la garde — « Garde les commandements de Dieu, Il te gardera » : la garde d'Allah répond à la garde de l'enfant ; la glose l'ouvre « en te conformant », et « Il te garde par Sa garde et veille sur toi par Sa sollicitude ».",
        "Le sabab : un enfant derrière le Prophète — et la pédagogie devient un enseignement du hadīth : « la douceur et la souplesse dans l'éducation de l'enfant et son instruction ».",
        "La structure des kalimāt : garde (« Il te gardera »), présence (« tu Le trouveras devant toi »), demande et secours (« si tu demandes, demande à Dieu »), décret clos par « les calames ont été levés et les feuilles se sont desséchées » ; la seconde version ajoute l'aisance reconnue et l'espérance triple.",
        "Le tawakkul : « si tu demandes, demande à Dieu » — demander à Dieu seul, pour « préserver le droit de l'adoration pure » ; à la mesure où l'on s'appuie sur autre que Dieu « par sa quête, son cœur ou son espoir », on « a détourné son visage de son Seigneur ».",
        "Le décret : la communauté entière rassemblée ne profite ni ne nuit « que de ce que Dieu a écrit » — « ni abrogation ni modification » ; le fruit : « que le croyant ne craigne et n'adresse sa demande à nul autre que Dieu ».",
        "L'espérance : « la victoire est avec la patience, que le soulagement est avec l'angoisse et qu'avec la difficulté est la facilité » — l'épreuve est la loi du bas-monde, « et les vertueux d'entre eux en premier lieu » ; trois enseignements : certitude du décret et mesure dans la quête (le testament de Luqmān), éducation de l'âme, douceur pédagogique.",
        "L'exploitation et la suite : Al-Anʾām 80-83 — Ibrāhīm le ḥanīf sans crainte, et la sécurité promise « Ceux qui ont cru et n'ont point enveloppé leur foi d'iniquité » boucle avec la foi au décret ; la préparation ouvre la leçon 25 (la pudeur — ḥayāʾ) ; la boucle tient : les quatre fragments de l'iʾdād de la leçon 23 sont portés.",
    ],
    "vocabulaire": [
        {"ar": "حفظ اوامر الله تعالى", "translit": "ḥifẓ ʾawāmiri llāhi taʾālā", "fr": "Préserver les commandements de Dieu — le titre de la leçon : « garde les ordres de Dieu et Ses interdits en te conformant », demandée « en secret comme au grand jour, dans la difficulté comme dans l'aisance »."},
        {"ar": "احفظ الله يحفظك", "translit": "iḥfaẓi llāha yaḥfaẓka", "fr": "« garde les commandements de Dieu, Il te gardera » — la réciprocité de la garde : « Il te garde par Sa garde et veille sur toi par Sa sollicitude », « en particulier au moment de la difficulté »."},
        {"ar": "تجده تجاهك", "translit": "taǧidhu tuǧāhaka", "fr": "« tu Le trouveras devant toi » — « tu Le rencontres face à toi dans tout ce que tu veux obtenir comme bien ou repousser comme mal »."},
        {"ar": "رفعت الاقلام وجفت الصحف", "translit": "rufiʿati l-ʾaqlāmu wa-ǧaffati ṣ-ṣuḥuf", "fr": "« les calames ont été levés et les feuilles se sont desséchées » — l'image du décret clos : « ni abrogation ni modification »."},
        {"ar": "تعرف الى الله", "translit": "taʾarrafa ʾilā llāh", "fr": "« connais Dieu » — « acquitte-toi de Ses droits et de Ses obligations » ; « dans l'aisance » = « dans la santé et l'opulence », « Il te connaîtra dans la difficulté »."},
        {"ar": "التوكل", "translit": "at-tawakkul", "fr": "la confiance en Dieu — « si tu demandes, demande à Dieu ; et si tu cherches secours, cherche-le auprès de Dieu » : s'en remettre à Lui seul « dans la totalité de ses affaires, les minimes comme les considérables »."},
        {"ar": "الايمان بالقضاء والقدر", "translit": "al-ʾīmānu bi-l-qaḍāʾi wa-l-qadar", "fr": "la foi au décret de Dieu et à Sa prédestination — « un pilier fondamental des articles de la foi », déjà enseignée pour elle-même à la leçon 8."},
        {"ar": "الفرج مع الكرب", "translit": "al-faraǧu maʿa l-karab", "fr": "« le soulagement est avec l'angoisse » — « la disparition de la dureté et sa dissolution adviennent après la gêne » ; la victoire « est avec la patience »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}
ENTREES = [('pdf-24', E_24)]


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
deja = [d for d, _ in ENTREES if d in com]
if deja:
    print('déjà présents, abandon :', deja)
    sys.exit(1)
for did, e in ENTREES:
    com[did] = norme_entree(e)
with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys(), key=lambda x: int(x.split('-')[1])))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-24',):
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
