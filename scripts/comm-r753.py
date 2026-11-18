#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R753 — commentaire de la leçon 16 hadith-5ep : pdf-16 (التورع عن الشبهات
— la circonspection envers le douteux : le onzième hadīth des Quarante
« Laisse ce qui te met en doute pour ce qui ne t'y met pas » — sens des
šubuhāt, statut en deux classes, types dont on est ou non excusé, trois
divisions du waraʿ).
Neuvième vague du livre (SUIVANT de R752-b ; hadith-5ep 15/29 au départ).
Rédaction d'après la lecture complète FR de la leçon (extraction non lossy
extrait-r753.py : /tmp/r753-lecon16-fr.txt) ET du tirage arabe du livre
(content/textbooks-src/hadith-5-ibtidai_text.pdf) — vérifications :
* le matn arabe de la leçon 16 porte « دع ما يريبك إلى ما لا يريبك »
  (vérifié pdftotext, offset ~79 460, dans la citation de Fatḥ al-Bārī) ;
  la traduction FR « Laisse ce qui te met en doute pour ce qui ne t'y met
  pas » est conforme ;
* la tarjama arabe porte « ولد مُنْتَصَفَ رَمَضَانَ سَنَة ثَلَاث منَ الهِجْرَة
  عَلَى الْأَصَح وَمَاتَ سَنَة أَرْبَع وَأَرْبَعِينَ وَقِيل غَيْرُ ذَلِك وَدُفِنَ
  بالبَقِيع » et « سَيِّدُ شَبَاب أَهْلِ الْجَنَّة » (offset ~77 800) ;
* les types du gibier/ذكاة, la règle « الْيَقِينُ لَا يُزَالُ بِالشَّك », le
  waswās (odeur/son), les deux bénéfices et les trois divisions du waraʿ
  avec « [إفتح الباري، ونسبه للغزالي] » (offsets ~79 000-82 100) — tout le
  bloc FR de la leçon est fidèle au tirage ;
* la préparation de la leçon 15 (offset ~77 500 : « أَبْحَث عَنْ تَرْجَمَةِ
  الحَسَنِ بن عَلِي » + « مَعْنَى الشَبَهَاتِ وَحُكْمِهَا ») est bien tenue.
Aucune invention (règle 2) : hadiths, versets, citations et attributions
tels que la leçon les donne.
VIGILANCE R752-b — formulation du matn TRANCHÉE : le SUIVANT de R752-b
citait provisoirement « Laisse ce qui te jette dans le doute... » ; la leçon
16 porte « Laisse ce qui te met en doute pour ce qui ne t'y met pas » —
cette formulation exacte est utilisée ici.
NB de lecture : AUCUN NB cette vague — la leçon 16 ne cite aucun verset du
Coran (vérifié sur l'extraction intégrale) ; les références sont hadithiques
(Sunan d'Ibn Māǧa, at-Tirmiḏī, an-Nasāʾī, ʿUmdat al-qārī d'al-ʿAynī, Fatḥ
al-bārī, Šarḥ Ṣaḥīḥ al-Buḫārī d'Ibn Baṭṭāl) et sont citées telles quelles.
OBSERVATION consignée (règle 5 — non corrigée dans le commentaire, zone du
manuel) : la leçon (FR et tirage arabe « إفتح البارى لابن رجب ») attribue au
« Fatḥ al-bārī d'Ibn Raǧab » les deux passages de l'analyse et, pour les
divisions du waraʿ, « Fatḥ al-bārī, qui l'attribue à al-Ġazālī » — le Fatḥ
al-bārī célèbre est l'œuvre d'Ibn Ḥaǧar al-ʿAsqalānī ; Ibn Raǧab a écrit
Ǧāmiʿ al-ʿulūm wa-l-ḥikam (commentaire des Cinquante). La traduction FR est
fidèle au tirage arabe ; l'attribution du tirage lui-même est à faire
vérifier par le propriétaire du manuel — le commentaire la cite telle
quelle et n'endosse pas l'écart.
Garde-fous de comm-r747/comm-r749/comm-r750/comm-r751/comm-r752 repris
(typographie FR, arabe entre parenthèses seulement, vocab ar sans harakat,
guillemets appariés) + fenêtre de mots 1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_16 = {
    "auteur": "IA-1, tour R753",
    "resume": "Guide de lecture de la leçon 16 (la circonspection envers le douteux — at-tawarruʿ ʿan-iš-šubuhāt (التَّوَرُّعُ عَنِ الشُّبُهَاتِ)) : le onzième hadīth des Quarante de l'imam al-Nawawī, rapporté par al-Ḥasan ibn ʿAlī ibn Abī Ṭālib — qu'Allah soit satisfait de lui et de son père — : « Laisse ce qui te met en doute pour ce qui ne t'y met pas » [Rapporté par at-Tirmiḏī et an-Nasāʾī]. Le tamhīd oppose la voie blanche de l'islam aux matières équivoques où « le statut légal se brouille pour le responsable (mukallaf) » ; trois objectifs répondent : connaître le sens des choses ambiguës, discerner le statut que la Loi religieuse assigne à leurs types, s'en écarter dans l'adoration et les transactions. L'analyse déroule le sens, le statut et les types (ce dont on n'est pas excusé, ce dont on est excusé) ; l'exploitation couronne par les trois divisions du waraʿ : des véridiques, des pieux, des vertueux.",
    "explication": [
        "La leçon 16 tient les deux engagements de la préparation de la leçon 15 : « Je recherche la notice biographique de al-Ḥasan ibn ʿAlī — qu'Allah soit satisfait de lui et de son père. » et « Je recherche le sens des choses ambiguës (šubuhāt) et leur statut. » Le chapeau la déclare « consacrée à la circonspection envers les choses ambiguës (at-tawarruʿ ʿan-iš-šubuhāt (التَّوَرُّعُ عَنِ الشُّبُهَاتِ)) » et « le commentaire du onzième hadīth des Quarante de l'imam al-Nawawī, rapporté par al-Ḥasan ibn ʿAlī — qu'Allah soit satisfait de lui et de son père ». Trois objectifs la précisent : « Que je connaisse le sens des choses ambiguës (aš-šubuhāt (الشُّبُهَات)) », « Que je discerne le statut que la Loi religieuse assigne aux divers types de choses ambiguës », « Que je m'écarte des choses ambiguës dans mes actes d'adoration et mes transactions ».",
        "Le tamhīd ouvre la scène : « La voie de l'islam est une route blanche et éclatante, comme l'a dit le Messager d'Allah — prière et salut d'Allah sur lui — : Je vous ai laissés sur la voie blanche : sa nuit en est comme le jour ; ne s'en détourne après moi que celui qui est perdu » [Sunan d'Ibn Māǧa]. Vient le fait qui donne la leçon : « il arrive que se présentent des matières équivoques où le statut légal se brouille pour le responsable (mukallaf), en sorte qu'il ne distingue plus son droit de celui d'autrui, ni le licite de l'illicite, ni que la chose relève des obligations ou n'en relève pas, ni qu'elle relève du bien reconnu ou du réprouvé : tel est ce que l'on appelle les choses ambiguës. » Puis deux questions : « Qu'entend-on donc par choses ambiguës ? Et quel est le statut de la Loi religieuse à leur égard ? »",
        "Le texte porte le hadīth entier : « D'après Abū Muḥammad al-Ḥasan ibn ʿAlī ibn Abī Ṭālib, petit-fils du Messager d'Allah — prière et salut d'Allah sur lui — et son rayon de parfum — qu'Allah soit satisfait de lui et de son père —, qui a dit : J'ai retenu du Messager d'Allah — prière et salut d'Allah sur lui — : Laisse ce qui te met en doute pour ce qui ne t'y met pas » [Rapporté par at-Tirmiḏī et an-Nasāʾī]. Le tirage arabe porte le matn (دع ما يريبك إلى ما لا يريبك) : l'ordre tient en un balancement — laisser l'incertain, revenir au certain.",
        "La notice répond à la préparation : « c'est Abū Muḥammad al-Ḥasan ibn ʿAlī ibn Abī Ṭālib, le Qurayšite, le Hāšimite, le Médinois, fils de la fille du Messager d'Allah — prière et salut d'Allah sur lui —, Fāṭima az-Zahrāʾ — qu'Allah le Très-Haut soit satisfait d'elle —, son petit-fils et son rayon de parfum, le maître de la jeunesse des gens du Paradis. Il naquit au milieu de Ramaḍān de l'an trois de l'Hégire, selon l'avis le plus juste, et mourut en l'an quarante-quatre — d'autres dates ont été proposées — ; il fut enterré au Baqīʿ. »",
        "Le glossaire déplie les deux clés du matn. « laisse (daʿ (دَعْ)) » : « abandonne ». « ce qui te met en doute (yurībuka (يُرِيبُكَ)) » : « avec la première syllabe voyellée au fatḥa ou au ḍamma, de rāba et de arāba — le fatḥa étant plus pur et plus répandu — ; le mot dérive du doute (ar-rayb), qui est le soupçon ». L'extraction annonce le chantier : « Je détermine ce que le hadīth indique du statut de la Loi religieuse à l'égard des choses ambiguës. » Et l'analyse précise : « Cette leçon expose le sens des choses ambiguës et le statut de la Loi religieuse selon leurs types ».",
        "Premièrement — le sens. « Les choses ambiguës sont le pluriel de šubha, laquelle est : toute chose qui ressemble au licite à un égard et à l'illicite à un autre. » L'exemple des possessions l'incarne [ʿUmdat al-qārī d'al-ʿAynī, adapté] : « le licite certain est ce dont il est su avec certitude que la propriété revient à soi » ; « l'illicite manifeste (al-ḥarām al-bayyin) est ce dont il est su avec certitude que la propriété revient à autrui » ; « la chose ambiguë est ce dont on ne sait si elle lui appartient ou à un autre — la circonspection (waraʿ) consiste à l'éviter ». La leçon 10 — le sixième hadīth des Quarante, rapporté par an-Nuʿmān ibn Bašīr — avait déjà posé le trio : « le licite est évident, l'illicite est évident, et entre les deux se trouvent des choses ambiguës », et son tamhīd conseillait déjà l'abstention par scrupule (at-tawarruʿ) dès que le statut devient ambigu — la leçon 16 le développe.",
        "Deuxièmement — le statut. « Le Prophète — prière et salut d'Allah sur lui — a exhorté, dans le hadīth, à délaisser les choses ambiguës en raison de leur équivocité et de leur obscurité » ; les statuts légaux « se répartissent en deux classes ». La première : « ce qui est limpide et manifeste, qui n'échappe pas à la généralité de la communauté tant il est clair et répandu — à peine son statut échappe-t-il à l'un des musulmans : ce sont le licite manifeste et l'illicite manifeste dont il est parlé dans le hadīth des choses ambiguës précédent ». La seconde : « ce au sujet de quoi l'on n'a pas tranché d'interdiction ni de permission, faute de clarté de sa preuve et par suite du désaccord des savants ». Vient la règle : « Quand la matière devient équivoque pour quelqu'un et que le licite ne se distingue plus pour lui de l'illicite, il lui est obligatoire de délaisser ce qui lui est devenu équivoque, par prévention de l'ambiguïté » — le sens du matn : « abandonne ce dont tu doutes de l'interdiction parmi les propos et les actes, et tourne-toi vers ce dont tu ne doutes pas parmi eux » [Fatḥ al-bārī d'Ibn Raǧab, adapté].",
        "Vient « dans ce même sens » le degré supérieur : « Le serviteur n'atteint pas d'être au nombre des pieux tant qu'il ne délaisse pas ce qui est sans inconvénient, par crainte de ce qui en comporte » [Sunan de at-Tirmiḏī]. « C'est là un degré de circonspection plus élevé que le précédent. » Le matn commande de quitter ce qui met en doute ; les pieux quittent même ce qui est sans inconvénient, par crainte de ce qui en peut sortir — la circonspection ne se mesure plus à l'équivoque réelle, mais à la prudence qui la devance.",
        "Troisièmement — les types. D'abord ce dont on n'est pas excusé : « ce sont des degrés gradués selon leur proximité ou leur éloignement de l'illicite ». Trois types au moins : a) « l'équivoque du fait de l'existence des causes de licéité et d'interdiction, comme lorsque l'homme doute au sujet d'un bien — est-il sa propriété ou non ? —, ou qu'il doute de la disparition de la propriété et de son inexistence ». b) « l'équivoque par suite du mélange du licite et de l'illicite dans les aliments, les boissons et le reste ». c) « que la chose soit interdite et que l'homme doute à son sujet : quelque chose est-il survenu qui la rende licite ? » — l'exemple qui fixe la règle : « tel le gibier, qu'il est interdit à l'homme de manger avant son égorgement rituel (ḏakāh) : s'il doute de l'égorgement, il ne sort de l'interdiction qu'avec la certitude de l'égorgement » [Šarḥ Ṣaḥīḥ al-Buḫārī d'Ibn Baṭṭāl, adapté]. Dans les trois cas le doute pèse du côté de l'illicite : on s'abstient.",
        "En face, « Il est des matières qui comportent le sens de l'ambiguïté sans que celle-ci s'y réalise ; aussi n'ont-elles pas reçu ce statut, et elles sont devenues au nombre de celles dont on est excusé. » Deux figures. La première : « que la chose soit licite et que le doute porte sur son interdiction : ce qui est tel demeure dans la permission jusqu'à ce que son interdiction soit sue avec certitude, selon la règle : la certitude ne fait pas place au doute ». La seconde : « celui dont le doute est fréquent et qui est atteint de suggestion obsédante (waswās) : il bâtit sur la certitude et ne prête pas attention au doute — comme celui que domine le doute au sujet de la rupture de l'ablution après la purification. » La réponse prophétique suit [Šarḥ Ṣaḥīḥ al-Buḫārī d'Ibn Baṭṭāl, adapté] : « l'homme trouve quelque chose pendant la prière — doit-il interrompre la prière ? Il dit : Non, jusqu'à ce qu'il sente une odeur ou qu'il entende un son ». « Et cela s'entend de celui que le doute assaille fréquemment ».",
        "Ce qu'il faut retirer du hadīth tient en deux bénéfices — le thermomètre du cœur. « Le licite pur n'engendre pour le croyant, dans son cœur, ni soupçon ni gêne : l'âme s'y apaise et le cœur s'en tranquillise ; les choses ambiguës, elles, engendrent le soupçon et la gêne. » — le trouble intérieur dénonce l'équivoque. Et l'élévation : « La circonspection à l'égard des choses ambiguës entraîne, à plus forte raison, la circonspection à l'égard des interdictions. »",
        "L'évaluation pose le bilan : « Je définis les choses ambiguës, et je donne un exemple pour chacun de leurs types. » et « Je mentionne le statut du délaissement des choses ambiguës, en l'appuyant d'une preuve. » Définition, exemple par type, preuve du statut — la preuve est le matn lui-même : « Laisse ce qui te met en doute pour ce qui ne t'y met pas », l'ordre prophétique reçu.",
        "L'exploitation couronne : « La circonspection (waraʿ) a ses divisions » [Fatḥ al-bārī, qui l'attribue à al-Ġazālī]. « la circonspection des véridiques (aṣ-ṣiddīqūn) : délaisser ce dont on ne fait pas usage sans l'intention d'en tirer force pour l'adoration » ; « la circonspection des pieux (al-muttaqūn) : délaisser ce qui ne comporte aucune ambiguïté, mais dont on craint qu'il n'entraîne vers l'illicite » ; « la circonspection des vertueux (aṣ-ṣāliḥūn) : délaisser ce à quoi touche la possibilité de l'interdiction — à condition que cette possibilité ait quelque poids ; si elle n'en a pas, c'est là la circonspection des obsédés ». Le texte demande le tri : « J'extrais les types de circonspection mentionnés dans le texte, en précisant lesquels comptent comme délaissement des choses ambiguës et lesquels n'y comptent pas. » Les définitions du texte tranchent : seul le troisième degré porte sur ce à quoi « la possibilité de l'interdiction » touche avec quelque poids — l'équivoque au sens du matn ; les deux premiers se règlent sur l'usage et l'intention, ou sur la crainte de l'entraînement.",
        "La préparation tourne la page : « Je mémorise le hadīth de la leçon qui vient, et j'accomplis ce qui suit : Je recherche le sens de l'occupation par ce qui ne regarde pas, et son statut dans la Loi religieuse. Je mentionne les méfaits de l'occupation par ce qui ne regarde pas. » — la leçon suivante, « Délaisser ce qui ne nous regarde pas », prendra le relais : la garde du temps et du cœur après celle du gain.",
    ],
    "points": [
        "La continuité : la préparation de la leçon 15 demandait la notice de al-Ḥasan ibn ʿAlī et le sens des šubuhāt — la leçon 16 tient les deux, dans le onzième hadīth des Quarante.",
        "Le matn : « J'ai retenu du Messager d'Allah — prière et salut d'Allah sur lui — : Laisse ce qui te met en doute pour ce qui ne t'y met pas » — quitter l'équivoque, revenir au certain.",
        "La définition : šubha = « toute chose qui ressemble au licite à un égard et à l'illicite à un autre » — le certain à soi, le certain à autrui, l'incertain que le waraʿ évite.",
        "Le statut en deux classes : le limpide (le hadīth des choses ambiguës précédent — la leçon 10) et le non-tranché — pour celui-ci, délaissement obligatoire « par prévention de l'ambiguïté ».",
        "Le degré supérieur : « Le serviteur n'atteint pas d'être au nombre des pieux tant qu'il ne délaisse pas ce qui est sans inconvénient, par crainte de ce qui en comporte » [Sunan de at-Tirmiḏī].",
        "Ce dont on n'est pas excusé : la cause de statut douteuse, le mélange du licite et de l'illicite, l'interdit dont une cause de licéité peut être survenue (le gibier — « il ne sort de l'interdiction qu'avec la certitude de l'égorgement »).",
        "Ce dont on est excusé : le licite demeure dans la permission jusqu'à certitude — « la certitude ne fait pas place au doute » ; le waswās bâtit sur la certitude — « Non, jusqu'à ce qu'il sente une odeur ou qu'il entende un son ».",
        "L'exploitation : les trois divisions de waraʿ (des véridiques, des pieux, des vertueux) ; le délaissement des šubuhāt relève de la troisième — « la circonspection des obsédés » si la possibilité n'a aucun poids ; la préparation annonce la leçon 17.",
    ],
    "vocabulaire": [
        {"ar": "التورع عن الشبهات", "translit": "at-tawarruʿ ʿani š-šubuhāt", "fr": "la circonspection envers les choses ambiguës — le titre de la leçon et le mouvement du hadīth tout entier : quitter l'équivoque pour le certain."},
        {"ar": "الشبهات", "translit": "aš-šubuhāt", "fr": "les choses ambiguës — pluriel de šubha : « toute chose qui ressemble au licite à un égard et à l'illicite à un autre »."},
        {"ar": "الورع", "translit": "waraʿ", "fr": "la circonspection — « la circonspection (waraʿ) consiste à l'éviter » : la garde du cœur et du bien devant l'incertain."},
        {"ar": "دع", "translit": "daʿ", "fr": "laisse — « abandonne » : le premier mot du matn, l'impératif qui commande le délaissement."},
        {"ar": "يريبك", "translit": "yurībuka", "fr": "te met en doute — voyelle au fatḥa ou au ḍamma, de rāba et de arāba ; dérive du doute (ar-rayb), « qui est le soupçon »."},
        {"ar": "الذكاة", "translit": "aḏ-ḏakāh", "fr": "l'égorgement rituel — l'exemple du gibier : « il ne sort de l'interdiction qu'avec la certitude de l'égorgement »."},
        {"ar": "الوسواس", "translit": "waswās", "fr": "la suggestion obsédante — le doute fréquent qui n'est pas excusé : « il bâtit sur la certitude et ne prête pas attention au doute »."},
        {"ar": "اليقين", "translit": "al-yaqīn", "fr": "la certitude — la règle qui gouverne le cas excusé : « la certitude ne fait pas place au doute »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-16', E_16)]


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
    print(f'!! déjà présent : {bloque} — rien de fait')
    raise SystemExit(1)
for docid, e in ENTREES:
    com[docid] = norme_entree(e)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys()))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-16',):
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
