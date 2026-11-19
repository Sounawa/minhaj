# -*- coding: utf-8 -*-
"""R759 — commentaires vague 15 hadith-5ep pdf-22 (lecon 22 : l'excellence
(ihsan) en toute chose — al-'ihsan fi kulli say').

METHODE (precedent R753-R758) :
  - extraction non lossy de la lecon 22 FR (/tmp/r759-lecon22.html -> txt,
    14 297 car htmlFr, 11 246 car texte ; le champ html arabe est vide pour
    ce livre, le FR porte l'arabe des gloses entre parentheses) ;
  - tirage arabe toujours indisponible (PDF locaux emportes par le
    recyclage, habous.gov.ma 404 sur /المدرج/ — consigne en R757-R758) :
    la verification s'appuie sur la traduction savante htmlFr de la lecon
    (produite depuis le tirage, validee au registre) ET sur recoupements ;
  - recoupements de cette vague :
    (a) echo textuel : la definition des cultes (« que tu adores Dieu comme
        si tu Le voyais ») est celle installee a la lecon 4 dans le dialogue
        de Jibril (« Informe-moi sur l'excellence » — verifie verbatim au
        htmlFr de la lecon 4) ;
    (b) i'dad de la lecon 21 verifie verbatim (« Je definis la bienfaisance »
        / « Je cite des exemples de bienfaisance ») : la lecon 22 les tient ;
    (c) boucle suivante : l'i'dad de la lecon 22 annonce les fragments
        « crains Dieu » / « elle l'efface » / « comporte-toi avec les gens »
        + husn al-huluq -> lecon 23 (la piete (taqwa) et le bon caractere,
        titleFr du registre) — le matn a venir n'est PAS cite sans source ;
    (d) transmisseur Saddad ibn Aws : 3 occurrences du nom dans le livre,
        toutes a la lecon 22 — premier hadith du livre porte par ce
        Compagnon (aucun ordinal des Quarante revendique : le chapeau n'en
        porte pas) ;
    (e) matns cites UNIQUEMENT avec leur source lecon (Sahih de Muslim ×2,
        Sahih d'al-Buhari et de Muslim, Sahih d'al-Buhari ×2, Muwatta',
        Sunan d'Ibn Maja, Al-Awsat d'at-Tabarani et Shu'ab al-'iman
        d'al-Bayhaqi) ;
    (f) references coraniques : Al-'Ankabut 46 et An-Nisa' 36 coïncident
        avec les versets du mushaf — AUCUN NB ; Ar-Rahman : 59 imprime — le
        verset qui porte « hal gaz_'u l-ihsan 'illa l-ihsan » est le 60
        (verifie web, surahquran.com + quran.com) — NB de lecture consigne
        (regle R739/R742/R756-R758 : NB seulement si divergence reelle).
Translitteration du commentaire en convention corpus (ʾ U+02BE / ʿ U+02BF),
les lecons htmlFr portant ' U+2019 — precedent R753-R758 (ex. lecon :
« al-'ihsan » ecrit al-ʾihsan au corpus). Vocabulaire arabe SANS harakat
(emelets conservees, precedent pdf-19 « al-'iman » / pdf-21 « awisini »).
Garde-fous de comm-r758.py repris (typographie FR, arabe entre parentheses
seulement, vocab ar sans harakat, guillemets apparies) + fenetre de mots
1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_22 = {
    "auteur": "IA-1, tour R759",
    "resume": "Guide de lecture de la leçon 22 (l’excellence (iḥsān) en toute chose — al-ʾiḥsān fī kulli šayʾ (الإحسان في كل شيء)) : le commentaire du hadīth de Šaddād ibn Aws « Dieu a prescrit l’excellence en toute chose » [Ṣaḥīḥ de Muslim]. Trois objectifs : connaître le sens de l’excellence en toute chose, réaliser le mérite de l’excellence envers les animaux, s’approprier les finalités de l’ordre. La clef : « Il a rendu obligatoire le perfectionnisme » « et l’a établi en loi » — le perfectionnisme est une obligation ; « chose » est « le plus indéterminé des noms indéfinis » : « nulle action n’en sort ». L’analyse déroule « le droit de l’excellence » en quatre domaines — cultes, transactions, dialogue et débats, œuvres — puis l’excellence envers les animaux et les règles de l’abattage. La préparation ouvre la leçon 23 : la piété (taqwā) et le bon caractère.",
    "explication": [
        "Après l’interdiction de la colère (leçon 21), la leçon 22 installe un nouveau hadīth des Quarante de l’imam al-Nawawī, avec le commentaire d’Ibn Daqīq al-ʾĪd : « Dieu a prescrit l’excellence en toute chose » (inna llāha kataba al-ʾiḥsān ʿalā kulli šayʾ (إِنَّ اللهَ كَتَبَ الْإِحْسَانَ عَلَى كُلِّ شَيْءٍ)), rapporté par Šaddād ibn Aws [Ṣaḥīḥ de Muslim]. Le chapeau : « le sens de l’excellence (al-ʾiḥsān) en toute chose, ses domaines d’application — cultes, transactions, dialogue et débats, travaux —, puis l’excellence envers les animaux et les règles de l’abattage rituel ». Premier hadīth du livre porté par ce Compagnon : son nom ne paraît dans aucune leçon antérieure.",
        "Trois objectifs ouvrent la marche : « Que je connaisse » (aʿrif (أَعْرِفَ)) « le sens de l’excellence en toute chose » ; « Que je réalise » (ʾudrik (أُدْرِكَ)) « le mérite de l’excellence envers les animaux » ; « Que je m’approprie » (atamaṯṯal (أَتَمَثَّلَ)) « les finalités de l’ordre de l’excellence en toute chose ».",
        "Le tamhīd (تَمْهِيدٌ) s’ouvre : « L’islam est venu comme miséricorde pour toutes les créatures » — « hommes, animaux et autres ; il a institué l’excellence en toute chose et envers toute chose, il l’a ordonnée envers le proche et le lointain comme envers l’animal, dans le culte, la parole et l’action ; il en a fait l’un des plus hauts degrés de la foi » « et lui a attaché l’immense récompense dans les jardins ». Deux questions ferment la mise en condition : « Qu’entend-on donc par l’excellence en toute chose ? » et « comment faire du bien à l’animal » ?",
        "Le hadīth (al-ḥadīṯ (الْحَدِيثُ)) installe le matn en trois temps. Le principe : « Dieu Très-Haut a prescrit l’excellence en toute chose ». Les applications : « lorsque vous mettez à mort, faites-le avec excellence » (fa-ʾaḥsinū al-qitla (فَأَحْسِنُوا الْقِتْلَةَ)), « lorsque vous égorgez, faites-le avec excellence » (aḏ-ḏibḥa (الذَّبْحَةَ)). Le geste : « que chacun de vous aiguise sa lame » (yuḥidd šafratah (وَلْيُحِدَّ شَفْرَتَهُ)) « et épargne toute souffrance à sa bête » (yuriḥ ḏabīḥatah (وَلْيُرِحْ ذَبِيحَتَهُ)) [Ṣaḥīḥ de Muslim].",
        "La notice du transmetteur (tarǧamat ar-rāwī (تَرْجَمَةُ الرَّاوِي)) présente : « Compagnon ansarite » (anṣārī (أَنْصَارِيٌّ)) « khazraǧite de la lignée des Banū an-Naǧǧār, il comptait parmi les savants et les meilleurs des Compagnons ; il rapporta du Prophète — prière et salut d’Allah sur lui — une cinquantaine de hadiths. Il était connu pour sa dévotion, sa scrupulosité, sa crainte révérencielle de Dieu et sa sagesse. Il s’établit à Bayt al-Maqdis (Jérusalem) et mourut en l’an cinquante-huit de l’Hégire. »",
        "L’explication (aš-šarḥ (الشَّرْحُ)) porte une seule glose, la clef de toute la leçon : « Il a prescrit l’excellence » (kataba al-ʾiḥsān (كَتَبَ الْإِحْسَانَ)) — « Il a rendu obligatoire le perfectionnisme » (faraḍa al-ʾitqān (فَرَضَ الْإِتْقَانَ)) « et l’a établi en loi » (wa-šaraʿah (وَشَرَعَهُ)). Le verbe « prescrit » est lu juridiquement : l’excellence est le droit même de toute œuvre. L’extraction des idées (istiḫlāṣ al-maḍāmīn (اِسْتِخْلَاصُ الْمَضَامِينِ)) pose la question du sens et le geste de sortie : « Je dégage du hadith la manière dont se pratique l’excellence ».",
        "L’analyse (at-taḥlīl (التَّحْلِيل)) ouvre sur une annonce de rang : « Ce hadith contient un enseignement juridique immense qui embrasse tous les chapitres du droit et d’autres domaines encore : c’est le droit de l’excellence » (fiqh al-ʾiḥsān (فِقْهُ الْإِحْسَانِ)). Premier thème : « le sens de l’excellence en toute chose ». La parole signifie « que l’excellence, le perfectionnisme et la réalisation de la qualité sont une obligation et une exigence en toute chose » ; et le mot « chose » « est le plus indéterminé des noms indéfinis » — « nulle action n’en sort ».",
        "Quatre domaines déroulent ce droit. Les cultes d’abord — la parole est celle du dialogue de Jibrīl, déjà installée à la leçon 4 (« Informe-moi sur l’excellence ») : « C’est que tu adores Dieu comme si tu Le voyais ; car si tu ne Le vois pas, Lui, certes, te voit » [Ṣaḥīḥ d’al-Buḫārī et de Muslim].",
        "Les transactions ensuite : d’après Ǧābir ibn ʿAbd Allāh — que Dieu soit satisfait de lui —, le Messager d’Allah — prière et salut d’Allah sur lui — dit : « Que Dieu fasse miséricorde à l’homme accommodant » « lorsqu’il vend, lorsqu’il achète et lorsqu’il réclame son dû » [Ṣaḥīḥ d’al-Buḫārī]. Le dialogue et la controverse : « Et ne discutez avec les gens du Livre que de la meilleure manière » [Al-ʿAnkabūt : 46]. Les œuvres : « Dieu aime que, lorsque l’un de vous fait une œuvre, il l’accomplisse avec excellence » [Al-Awsaṭ d’aṭ-Ṭabarānī, et Šuʿab al-ʾīmān d’al-Bayhaqī].",
        "Le second thème répond à la seconde question du tamhīd : « l’excellence envers les animaux ». L’islam « a exhorté à l’excellence envers les animaux et à la douceur à leur égard, et il y a attaché l’immense récompense et la généreuse rétribution ». Le conseil d’abord : les Compagnons demandent « Ô Messager d’Allah, y a-t-il donc pour nous une récompense dans les bêtes ? » ; la réponse : « Dans tout foie humide » (fī kulli ḏāti kabid raṭba (فِي كُلِّ ذَاتِ كَبْدٍ رَطْبَةٍ)) « il y a une récompense » [Muwaṭṭaʿ].",
        "L’interdiction ensuite : le Prophète — prière et salut d’Allah sur lui — a interdit « de les tourmenter, de les frapper ou de les retenir captives ». Le hadīth d’Anas — que Dieu soit satisfait de lui — précise : le Prophète « a interdit que les bêtes soient tenues confinées » (tuṣbar al-bahāʾim (تُصْبَرَ الْبَهَائِمُ)) [Ṣaḥīḥ de Muslim], le sens étant « être retenue sans nourriture ni boisson ». Et l’avertissement : « Une femme entra en Enfer à cause d’une chatte qu’elle avait attachée : elle ne l’a point nourrie et ne l’a point laissée manger des bestioles de la terre » (ḫišāš al-ʾarḍ (خَشَاشِ الْأَرْضِ)) « jusqu’à ce qu’elle mourût » [Sunan d’Ibn Māǧa].",
        "Au cœur du thème, les règles de l’abattage : « l’excellence dans l’abattage des bêtes » « consiste en ceci » — « que l’abatteur soigne son geste » « et évite la torture ; qu’il soit doux avec la bête — sans la renverser brusquement ni la traîner d’un lieu à un autre ; qu’il aiguise le couteau ; qu’il l’oriente vers la qibla ; qu’il prononce le nom de Dieu et Le loue ; qu’il tranche la gorge et les deux jugulaires » (al-ḥulqūm wa-l-wadajayn (الْحُلْقُومَ وَالْوَدَجَيْنِ)) ; « qu’il la laisse jusqu’à ce qu’elle refroidisse » (ʾilā ʾan tabrad (إِلَى أَنْ تَبْرُدَ)) ; « qu’il n’aiguise pas le couteau devant elle ; qu’il n’égorge pas une autre bête devant elle ; et que rien ne soit coupé d’elle avant qu’elle ne meure ». Trois interdits épargnent à la bête le spectacle de sa propre mort.",
        "La règle suit l’homme jusque dans le cas limite : « de même que l’excellence est requise dans l’abattage du bétail dont Dieu a permis la consommation, elle est requise également dans la mise à mort des animaux dont la Loi a permis de tuer ceux qui nuisent à l’homme » — « serpents, scorpions et rats » (al-fiʾrān (الْفِئْرَانِ)) — « ou que frappent des maladies dont la guérison est impossible ».",
        "Ce que le hadīth nous apprend (wa-mimmā yustafād min al-ḥadīṯ (وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ)) élargit encore. La croyance et la conduite : « L’excellence du musulman dans sa croyance et sa conduite passe par la vigilance devant Dieu » — « et dans son culte par l’obéissance qui Lui est purement vouée, sans ostentation ». Le voisin : « la préservation de son droit en sa présence comme en son absence » ; « la garde de son secret » ; « le secours qu’on lui apporte dans son besoin ou sa pauvreté ».",
        "Les deux parents ensuite : « entretenir sans cesse leur amour, leur piété filiale, leur fidélité et leur honneur ; prier pour eux et faire l’aumône en leur nom » « ; et rester fidèle à ceux qui les aimaient ». Et la rétribution : l’homme de bien « mérite l’amour de Dieu Très-Haut et Sa bienfaisance, en récompense équitable » « et qu’il s’attire l’amour des gens » — « Y a-t-il d’autre récompense de l’excellence que l’excellence ? » (hal ǧazāʾu al-ʾiḥsān ʾillā al-ʾiḥsān (هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ)) [Ar-Raḥmān : 59]. NB de lecture : la référence imprimée porte le verset 59 ; le verset qui porte ces paroles est le 60 de la sourate Ar-Raḥmān (vérifié web). Enfin : « L’excellence est un principe islamique général qui embrasse toutes les affaires de la vie » et « toutes les relations de l’homme avec l’homme et avec l’ensemble des créatures ».",
        "L’évaluation (at-taqwīm (التَّقْوِيم)) donne trois tâches : « Je cite cinq choses qui entrent dans la généralité de l’excellence en toute chose » ; « Je cite cinq choses qui comptent parmi l’excellence envers l’animal » ; « J’expose quelques bienfaits de l’excellence » et les appuie « de textes religieux ».",
        "L’exploitation (al-istiṯmār (الِاسْتِثْمَارُ)) donne à la tâche son texte : « Adorez Dieu et ne Lui associez rien ; soyez excellents envers les parents et les proches, les orphelins et les indigents, le voisin parent, le voisin étranger, le compagnon d’à côté, le voyageur et ceux que vos mains possèdent. Dieu n’aime pas l’orgueilleux plein de fatuité » [An-Nisāʾ : 36]. Puis deux exercices : « J’expose deux sortes d’excellence envers chacun des suivants : les parents, les proches, les orphelins et les indigents » ; « J’explique le sens de » — « le voisin parent », « le voisin étranger », « le compagnon d’à côté », « et le voyageur » — du plus proche au plus lointain.",
        "La préparation de la leçon suivante (al-ʾiʿdād al-qabliyy (الْإِعْدَادُ الْقَبْلِيُّ)) enjoint d’abord « Je mémorise le hadith de la leçon », puis « J’explique » : « crains Dieu » (attaqi llāh (اتَّقِ اللهَ)), « elle l’efface » (tamḥuhā (تَمْحُهَا)), « comporte-toi avec les gens » (ḫāliqi n-nās (وَخَالِقِ النَّاسَ)) — les fragments du hadīth de la leçon à venir — et « J’expose le sens du bon caractère » « et son mérite » : la leçon 23, « la piété (taqwā) et le bon caractère ». La boucle : la leçon 21 demandait « Je définis la bienfaisance » et « Je cite des exemples de bienfaisance » — la leçon 22 les a tenus ; la leçon à venir installera la piété et le caractère.",
    ],
    "points": [
        "La place : leçon 22, après l’interdiction de la colère — le hadīth de Šaddād ibn Aws « Dieu a prescrit l’excellence en toute chose » [Ṣaḥīḥ de Muslim], premier du livre porté par ce Compagnon ; plan : le sens de l’excellence en toute chose, ses domaines — cultes, transactions, dialogue et débats, travaux —, les animaux, l’abattage rituel.",
        "Le tamhīd : « L’islam est venu comme miséricorde pour toutes les créatures » — « hommes, animaux et autres » ; l’excellence « l’un des plus hauts degrés de la foi » ; deux questions dessinent le plan de l’analyse.",
        "La clef : « Il a rendu obligatoire le perfectionnisme » « et l’a établi en loi » (faraḍa al-ʾitqān wa-šaraʿah) ; « chose » (šayʾ) est « le plus indéterminé des noms indéfinis » — « nulle action n’en sort » ; l’ensemble se nomme « le droit de l’excellence » (fiqh al-ʾiḥsān).",
        "Les quatre domaines : cultes — « C’est que tu adores Dieu comme si tu Le voyais » [Ṣaḥīḥ d’al-Buḫārī et de Muslim] ; transactions — « Que Dieu fasse miséricorde à l’homme accommodant » [Ṣaḥīḥ d’al-Buḫārī] ; dialogue — « Et ne discutez avec les gens du Livre que de la meilleure manière » [Al-ʿAnkabūt : 46] ; œuvres — « Dieu aime que, lorsque l’un de vous fait une œuvre, il l’accomplisse avec excellence » [Al-Awsaṭ d’aṭ-Ṭabarānī, et Šuʿab al-ʾīmān d’al-Bayhaqī].",
        "Les animaux : « Dans tout foie humide » « il y a une récompense » [Muwaṭṭaʿ] ; l’interdit « que les bêtes soient tenues confinées » — « être retenue sans nourriture ni boisson » [Ṣaḥīḥ de Muslim] ; la chatte de l’avertissement [Sunan d’Ibn Māǧa].",
        "L’abattage : « que l’abatteur soigne son geste » et « évite la torture » ; la douceur, la qibla, le nom de Dieu ; « qu’il tranche la gorge et les deux jugulaires » ; « qu’il n’aiguise pas le couteau devant elle » ; « que rien ne soit coupé d’elle avant qu’elle ne meure » ; étendu à « serpents, scorpions et rats ».",
        "Les enseignements : « L’excellence du musulman dans sa croyance et sa conduite passe par la vigilance devant Dieu » ; le voisin — « la garde de son secret », « le secours qu’on lui apporte dans son besoin ou sa pauvreté » ; les parents — « prier pour eux et faire l’aumône en leur nom » ; « Y a-t-il d’autre récompense de l’excellence que l’excellence ? » (Ar-Raḥmān — imprimée 59, verset porteur 60, vérifié web).",
        "La préparation : expliquer « crains Dieu », « elle l’efface », « comporte-toi avec les gens » et « le sens du bon caractère » — la leçon 23, « la piété (taqwā) et le bon caractère ».",
    ],
    "vocabulaire": [
        {"ar": "الإحسان في كل شيء", "translit": "al-ʾiḥsān fī kulli šayʾ", "fr": "l’excellence en toute chose — le titre de la leçon : le principe prescrit, ses domaines d’application (cultes, transactions, dialogue et débats, travaux), les animaux et les règles de l’abattage rituel."},
        {"ar": "كتب الإحسان", "translit": "kataba al-ʾiḥsān", "fr": "il a prescrit l’excellence — lu juridiquement : « Il a rendu obligatoire le perfectionnisme » « et l’a établi en loi » ; l’excellence est une obligation, non un supplément."},
        {"ar": "الاتقان", "translit": "al-ʾitqān", "fr": "le perfectionnisme — le contenu même de l’excellence : « l’excellence, le perfectionnisme et la réalisation de la qualité sont une obligation et une exigence en toute chose »."},
        {"ar": "فقه الإحسان", "translit": "fiqh al-ʾiḥsān", "fr": "le droit de l’excellence — « un enseignement juridique immense qui embrasse tous les chapitres du droit et d’autres domaines encore »."},
        {"ar": "فاحسنوا القتلة", "translit": "fa-ʾaḥsinū al-qitla", "fr": "faites-le avec excellence lorsque vous mettez à mort — la première application du principe, suivie de l’égorgement (aḏ-ḏibḥa) ; « que chacun de vous aiguise sa lame » « et épargne toute souffrance à sa bête »."},
        {"ar": "في كل ذات كبد رطبة", "translit": "fī kulli ḏāti kabid raṭba", "fr": "dans tout foie humide — la parole du conseil : « il y a une récompense » [Muwaṭṭaʿ] ; la récompense descend jusqu’à l’être vivant le plus humble."},
        {"ar": "تصبر البهائم", "translit": "tuṣbar al-bahāʾim", "fr": "que les bêtes soient tenues confinées — l’interdit du hadīth d’Anas : « être retenue sans nourriture ni boisson » [Ṣaḥīḥ de Muslim]."},
        {"ar": "الحلقوم والودجين", "translit": "al-ḥulqūm wa-l-wadajayn", "fr": "la gorge et les deux jugulaires — ce que l’abatteur tranche avec excellence : la lame aiguisée, la bête douce, « que rien ne soit coupé d’elle avant qu’elle ne meure »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-22', E_22)]


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
for DOCID in ('pdf-22',):
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
