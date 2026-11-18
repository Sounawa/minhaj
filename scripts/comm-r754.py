#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R754 — commentaire de la leçon 17 hadith-5ep : pdf-17 (ترك ما لا يعني
— délaisser ce qui ne nous regarde pas : le douzième hadīth des Quarante
« Il est de la beauté de l'islam d'un homme qu'il délaisse ce qui ne le
regarde pas » — statut de l'islam à l'égard de l'inutile, effets de
l'occupation par ce qui ne regarde pas, exhortation à l'occupation par ce
qui regarde).
Dixième vague du livre (SUIVANT de R753-b ; hadith-5ep 16/29 au départ).
Rédaction d'après la lecture complète FR de la leçon (extraction non lossy
extrait-r754.py : /tmp/r754-lecon17-fr.txt) ET du tirage arabe du livre
(content/textbooks-src/hadith-5-ibtidai_text.pdf) — vérifications :
* le matn arabe de la leçon 17 porte « من حُسْنِ إِسْلَامِ الْمَرْءِ تَرْكُهُ
  مَا لَا يَعْنِيهِ » (vérifié pdftotext, offset ~83 650 dans la citation du
  taḥlīl أولاً, doublon ~84 830 dans ثالثاً — pages 94-95 du manuel) ; la
  traduction FR « Il est de la beauté de l'islam d'un homme qu'il délaisse
  ce qui ne le regarde pas » est conforme ;
* le transmetteur porte « أَبُو هُرَيْرَة رضي الله عنه، سبقت ترجمته »
  (offset ~82 500, tarjama arabe) — VIGILANCE SUIVANT de R753-b TRANCHÉE :
  matn et transmetteur vérifiés sur le tirage avant de citer ;
* les trois objectifs, le tamhīd (outrepassement des convenances,
  immiscence à dessein ou sans dessein, l'embarras), le glossaire
  (حُسْن / الْمَرْءُ / مَا لَا يَعْنِيهِ / الْعِنَايَة avec
  « عَنَاهُ يَغْنِيهِ إذا اهْتَمّ به وَطَلَبَه », offset ~82 300), le
  استخلاص (« أبَيّنُ من الْحَديث مَؤْقفَ الإسْلام ممّا لا يَعْنِي »), les
  trois axes du taḥlīl avec az-Zarqānī ×2 (« وَفي إفهامه أنَّ من قُبْح
  حالِ الْمَرْءِ الِاشتغال بِمَا لا يَعْنِيه؛ لِأنه ضَيَاعٌ لِلوقتِ النفيس... »
  et « فَإِنَّ الذي يَعْنيه الإسْلامُ وَالإيمانُ العمل الصالح... »),
  Mālik ibn Dīnār (« إذا رَأَيْتَ قَسَاوَةَ في قلبك... » [فيض القدير
  للمناوي]), les trois récits du salaf (صحيح ابن حبان / الموطأ — Luqmān
  « صدق الحَديث وَأَدَاءُ الأمَانَة وتَرك مَالا يَعْنيني » / al-Ḥasan
  al-Baṣrī « مَن عَلامَة إِغْضاضِ الله تَعَالَى عَن الْعَبْد »), la fāʾida
  (« حَثَ الإسْلامُ عَلَى فْعْلٍ ما فيه الخَيْرُ... حَتّى لا يَضِيعَ
  عُمُرُهُ في سَفَاسِف الأمُور »), les trois questions du taqwīm et
  l'istiṯmār (« حَدّ ما لا يَعْنيك في الكلام... كَنْز من كُنوز الجَنّة
  وَأَخَذَ بدلَه بَدْرَةَ كَانَ خَاسِرا » [دليل الفالحين لطرق رياض الصالحين
  ونسبه للغزالي]) — tout le bloc FR de la leçon est fidèle au tirage.
Aucune invention (règle 2) : hadiths, citations et attributions tels que
la leçon les donne.
NB de lecture : AUCUN NB cette vague — la leçon 17 ne cite aucun verset du
Coran (vérifié sur l'extraction intégrale : 0 ﴿, 0 réf. coranique) ; les
références sont hadithiques ou homilétiques (Sunan de at-Tirmiḏī, Ṣaḥīḥ
d'Ibn Ḥibbān, al-Muwaṭṭaʾ, Šarḥ az-Zarqānī sur le Muwaṭṭaʾ, Fayḍ al-Qadīr
d'al-Munāwī, Dalīl al-fāliḥīn) et sont citées telles quelles.
OBSERVATION positive (règle 5) : l'attribution « Dalīl al-fāliḥīn, qui
l'attribue à al-Ġazālī » est cohérente avec le tirage « ونسبه للغزالي » —
le livre est celui d'Ibn al-Qayyim, le passage est la parole d'al-Ġazālī
qu'il rapporte : la formulation du manuel est exacte (pas d'écart à
consigner, contrairement au إفتح الباري de R753).
Translittération du commentaire en convention corpus (ʾ U+02BE / ʿ U+02BF),
les leçons htmlFr portant ’ U+2019 — précédent R753 « at-tawarruʿ ʿani
š-šubuhāt » (leçon : « at-tawarru’ ’an-iš-šubuhāt »). Les parenthèses
translit/arabe sont serrées dans le htmlFr (« (ḥusn (حُسْنٌ)) »,
« (iḥsān) », « (badra) ») — vérifié sur le source brut des leçons.
Garde-fous de comm-r753 repris (typographie FR, arabe entre parenthèses
seulement, vocab ar sans harakat, guillemets appariés) + fenêtre de mots
1700-2400 (resume+explication+points)."""
import json, re, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_17 = {
    "auteur": "IA-1, tour R754",
    "resume": "Guide de lecture de la leçon 17 (délaisser ce qui ne nous regarde pas — tarku mā lā yaʿnīhi (تَرْكُ مَا لَا يَعْنِيهِ)) : le douzième hadīth des Quarante de l'imam al-Nawawī, rapporté par Abū Hurayra — qu'Allah soit satisfait de lui — : « Il est de la beauté de l'islam d'un homme qu'il délaisse ce qui ne le regarde pas » [Sunan de at-Tirmiḏī]. Le tamhīd peint ceux qui s'immiscent dans ce qui ne les regarde pas ; trois objectifs répondent : connaître le sens et le statut de l'occupation par ce qui ne regarde pas et le statut que la Loi religieuse lui assigne, saisir ses effets néfastes et la différence entre elle et ce qui regarde, s'occuper de ce qui regarde et délaisser le reste dans la parole et l'action. L'analyse déroule trois axes : l'exhortation au délaissement, les effets de l'occupation par l'inutile, l'exhortation à l'occupation par ce qui regarde ; l'exploitation couronne par le critère de la parole et l'échange du trésor contre la bourse.",
    "explication": [
        "La leçon 17 tient les deux engagements de la préparation de la leçon 16 : « Je recherche le sens de l'occupation par ce qui ne regarde pas, et son statut dans la Loi religieuse. » et « Je mentionne les méfaits de l'occupation par ce qui ne regarde pas. » Le chapeau la déclare « consacrée au délaissement de ce qui ne regarde pas (tarku mā lā yaʿnīhi (تَرْكُ مَا لَا يَعْنِي)) », « le commentaire du douzième hadīth des Quarante de l'imam al-Nawawī, rapporté par Abū Hurayra — qu'Allah soit satisfait de lui ». Trois objectifs la précisent : « Que je connaisse le sens de l'occupation par ce qui ne regarde pas, et le statut que la Loi religieuse lui assigne. », « Que je saisisse les effets néfastes de l'occupation par ce qui ne regarde pas, et la différence entre elle et ce qui regarde. », « Que je m'occupe de ce qui me regarde, et que je délaisse ce qui ne me regarde pas, dans la parole et l'action. »",
        "Le tamhīd ouvre la scène : « Certains gens outrepassent les convenances dans leurs propos ou leur conduite envers autrui : ils ne sont point parés des nobles caractères et des beautés de la nature ; aussi trouves-tu parmi eux qui s'immisce dans ce qui ne le regarde pas, à dessein ou sans dessein, et qui tombe — ou fait tomber — dans l'embarras. » L'immiscence entraîne autrui. Puis trois questions donnent le plan : la définition, le statut, les effets — les trois axes de l'analyse.",
        "Le texte porte le hadīth entier : « D'après Abū Hurayra — qu'Allah le Très-Haut soit satisfait de lui —, qui a dit : le Messager d'Allah — prière et salut d'Allah sur lui — a dit : Il est de la beauté de l'islam d'un homme qu'il délaisse ce qui ne le regarde pas » [Sunan de at-Tirmiḏī]. Le tirage arabe porte le matn (مِنْ حُسْنِ إِسْلَامِ الْمَرْءِ تَرْكُهُ مَا لَا يَعْنِيهِ). La structure tient en un échange : la beauté de l'islam ne se prouve pas par un ajout — elle se prouve par un abandon.",
        "La notice répond en une ligne : Abū Hurayra — qu'Allah soit satisfait de lui — : « sa notice biographique a été donnée précédemment. » Le renvoi n'est pas une économie de plume : la notice complète fut donnée à la leçon 13 — ʿAbd ar-Raḥmān ibn Ṣaḫr ad-Dawsī, la kunya reçue du Prophète — prière et salut d'Allah sur lui — ; la leçon 15 l'avait déjà renvoyée en une ligne pareille : le livre s'apprend aussi par ses renvois.",
        "Le glossaire déplie les clés du matn. « beauté (ḥusn (حُسْنٌ)) » : « le beau est le contraire du laid » — l'islam se dit beau, et sa beauté se prouve par un délaissement. « un homme (al-marʾ (الْمَرْءُ)) » : « la personne » — la règle vaut pour tout responsable. « ce qui ne le regarde pas (mā lā yaʿnīhi (مَا لَا يَعْنِيهِ)) » : « ce qui ne l'importe pas, parmi les affaires de la religion et de la vie d'ici-bas » — l'utile se mesure aux deux demeures ensemble. Et la racine est dépliée : « Le soin (al-ʿināya) : l'intensité de l'attention portée à une chose » ; on dit ʿanāhu yaʿnīhi — « il l'a pris à cœur » — le délaissement commandé par le hadīth est l'inverse exact de la prise à cœur.",
        "L'extraction annonce le chantier : « J'expose, à partir du hadīth, le statut de l'islam à l'égard de ce qui ne regarde pas. » Et l'analyse définit : « Le hadīth oriente vers l'abandon de l'occupation par ce qui ne regarde pas parmi les affaires — c'est-à-dire ce dont l'homme n'a pas besoin et auquel nulle nécessité ne le lie, attendu qu'il n'y a là ni utilité ni intérêt qui le requière, ni pour la religion ni pour ici-bas » — le critère est le besoin, mesuré aux deux demeures.",
        "Premièrement — l'exhortation au délaissement (ʾawwalan : al-ḥaṯṯu ʿalā tarki mā lā yaʿnī (أَوَّلًا: الْحَثُّ عَلَى تَرْكِ مَا لَا يَعْنِي)). « Le Prophète — prière et salut d'Allah sur lui — a exhorté, dans le hadīth, à ce que l'homme délaisse ce qui ne le regarde pas — ce qui ne l'importe pas des affaires de la religion et d'ici-bas, parmi les propos et les actes. » Le hadīth fait du délaissement « un bienfait (iḥsān) qui compte pour un degré élevé dans l'islam », et la clef suit : « Celui donc qui s'occupe de ce qui le regarde et délaisse ce qui ne le regarde pas, voilà le bienfaiteur véritable : car il a réalisé son islam en son extérieur comme en son intérieur. »",
        "Deuxièmement — les effets de l'occupation par ce qui ne regarde pas (ṯāniyan : ʾāṯāru l-ištiġāli bi-mā lā yaʿnī (ثَانِيًا: آثَارُ الِاشْتِغَالِ بِمَا لَا يَعْنِي)) : « l'islam a exhorté à délaisser ce qui ne regarde pas en raison des dommages graves et des suites funestes que cela comporte — et ils sont fort nombreux ». Le premier est la dilapidation du temps : « la dilapidation du temps précieux, impossible à compenser, et qui compte pour une grâce immense et une faveur très grande ». Az-Zarqānī fixe la règle : « Sa compréhension implique qu'il est des laideurs des états de l'homme que de s'occuper de ce qui ne le regarde pas : c'est en effet une dilapidation du temps précieux, dont le perdu ne peut être compensé en ce pour quoi l'homme n'a pas été créé » [Šarḥ az-Zarqānī sur le Muwaṭṭaʾ] — la mesure du gaspillage est la destination de l'homme.",
        "Vient la mécanique du temps : « la négligence dans l'accomplissement des obligations qui regardent l'homme et l'importent : l'occupation par ce qui ne regarde pas est en effet le moyen de délaisser ce qui regarde » — l'inutile prend sur l'utile. Puis l'issue : « l'occupation par ce qui ne regarde pas a le plus souvent pour issue le regret : il arrive à l'homme d'entendre ce qui lui déplaît, ou de se jeter dans ce dont la suite n'est pas louée ». Et le symptôme triple, donné par Mālik ibn Dīnār : « Si tu vois une dureté dans ton cœur, une faiblesse dans ton corps et une privation dans ta subsistance, sache que tu as parlé de ce qui ne te regarde pas » [Fayḍ al-Qadīr d'al-Munāwī] — trois thermomètres d'une même cause, la parole qui déborde son objet.",
        "Les vertueux des premières générations (as-salaf aṣ-ṣāliḥ) « ont compris le sens du délaissement, par l'homme, de ce qui ne le regarde pas, et en ont saisi la sagesse : ils s'occupaient de ce qui les regardait et délaissaient ce qui ne les regardait pas ». Trois récits l'incarnent. Abū ḏarr — qu'Allah soit satisfait de lui — : « et quiconque compte sa parole au nombre de ses actes, sa parole se fait rare, sinon en ce qui le regarde » [Ṣaḥīḥ d'Ibn Ḥibbān]. À Luqmān on demandait le secret de son mérite, et il répondit : « La véracité du propos, l'acquittement du dépôt, et le délaissement de ce qui ne me regarde pas » [al-Muwaṭṭaʾ]. Et al-Ḥasan al-Baṣrī retourne la perspective : « Au nombre des signes qu'Allah le Très-Haut détourne Son attention du serviteur, il y a qu'Il place son occupation dans ce qui ne le regarde pas » — un signe du détour de l'attention divine.",
        "Troisièmement — l'exhortation à l'occupation par ce qui regarde (ṯāliṯan : al-ḥaṯṯu ʿalā l-ištiġāli bi-mā yaʿnī (ثَالِثًا: الْحَثُّ عَلَى الِاشْتِغَالِ بِمَا يَعْنِي)) : « le hadīth indique qu'il est de la beauté de l'islam de l'homme de s'occuper de ce qui le regarde parmi les affaires, de même qu'il indique explicitement qu'il est de la beauté de son islam de délaisser ce qui ne le regarde pas » — les deux versants. Az-Zarqānī déplie ce qui regarde : « Ce qui le regarde, au titre de l'islam et de la foi, c'est l'œuvre droite, et ce qui se rattache à la nécessité de sa vie pour sa subsistance : satiété et désaltèrement, couverture de la nudité, chasteté du sexe, et ce qui est semblable — de quoi la nécessité est satisfaite, sans superflu d'aisance. Par là, il est préservé de l'ensemble des maux, pour sa religion et pour son au-delà. Quiconque adore Allah en ayant présent à l'esprit Sa proximité de son Seigneur, ou la proximité de son Seigneur de lui, celui-là a réalisé la beauté de son islam » [Šarḥ az-Zarqānī sur le Muwaṭṭaʾ] — le nécessaire, non le superflu.",
        "Ce qu'il faut retirer du hadīth tient en un bilan : « L'islam exhorte à faire ce en quoi résident le bien, la rectitude et le profit pour l'homme, en ce monde et dans l'au-delà, et à délaisser ce qui est sans utilité, afin qu'il ne gaspille pas sa vie dans les futilités. » — un partage du temps : l'utile fait, l'inutile quitté.",
        "L'évaluation pose trois questions : « Je mentionne certaines des conséquences qui découlent de l'occupation par ce qui ne regarde pas. », « Que retire-t-on de l'exhortation de l'islam à l'occupation par ce qui regarde ? », « Je cite des exemples de ce qui regarde l'homme et de ce qui ne le regarde pas. » L'exploitation donne l'instrument : « La définition de ce qui, dans la parole, ne te regarde pas : que tu parles de ce dont, si tu t'en taisais, tu n'encourrais ni faute ni dommage, ni à l'immédiat ni à terme. Si tu t'occupes de ce qui ne te regarde pas, tu dilapides ton temps et tu auras à rendre compte de l'activité de ta langue, puisque tu échanges ce qui est moindre contre ce qui est meilleur ; et si tu la consacrais à l'évocation d'Allah et à l'invocation, il s'ouvrirait peut-être pour toi, des effusions d'Allah, ce dont le profit est immense : quiconque est en mesure de prendre un trésor des trésors du Paradis et prend à sa place une bourse (badra) est perdant » [Dalīl al-fāliḥīn li-ṭuruqi Riyāḍ aṣ-ṣāliḥīn, qui l'attribue à al-Ġazālī]. Le critère de la parole est l'épreuve du silence : faute, dommage, terme — l'immédiat et le terme ensemble ; l'échange : le moindre contre le meilleur, le trésor contre une bourse.",
        "La préparation tourne la page : « Je mémorise le hadīth de la leçon qui vient, et j'accomplis ce qui suit : Je recherche le mérite de l'amour du bien pour les gens. Je mentionne certaines des manifestations de l'amour du bien pour les gens. » — la leçon suivante, « Aimer le bien pour les gens », prendra le relais : l'amour actif qui donne. La leçon 17 est ainsi un pivot : la leçon 16 quittait l'équivoque pour le certain, la 17 quitte l'inutile pour l'utile, la 18 passera du délaissement au don.",
    ],
    "points": [
        "La continuité : la préparation de la leçon 16 demandait le sens et le statut de l'occupation par ce qui ne regarde pas, et ses méfaits — la leçon 17 tient les deux, dans le douzième hadīth des Quarante.",
        "Le matn : « Il est de la beauté de l'islam d'un homme qu'il délaisse ce qui ne le regarde pas » [Sunan de at-Tirmiḏī] — le tirage porte (مِنْ حُسْنِ إِسْلَامِ الْمَرْءِ تَرْكُهُ مَا لَا يَعْنِيهِ) ; la beauté de l'islam se prouve par un abandon.",
        "La définition : ce qui ne regarde pas = « ce dont l'homme n'a pas besoin et auquel nulle nécessité ne le lie » — « ni pour la religion ni pour ici-bas » ; le critère est le besoin, mesuré aux deux demeures.",
        "L'extérieur et l'intérieur : « Celui donc qui s'occupe de ce qui le regarde et délaisse ce qui ne le regarde pas, voilà le bienfaiteur véritable : car il a réalisé son islam en son extérieur comme en son intérieur. »",
        "Les quatre effets : la dilapidation du temps précieux (az-Zarqānī — « en ce pour quoi l'homme n'a pas été créé »), la négligence des obligations, le regret, le triple symptôme de Mālik ibn Dīnār [Fayḍ al-Qadīr d'al-Munāwī].",
        "Les salaf : Abū ḏarr compte la parole parmi les actes, « sa parole se fait rare, sinon en ce qui le regarde » [Ṣaḥīḥ d'Ibn Ḥibbān] ; Luqmān — « La véracité du propos, l'acquittement du dépôt, et le délaissement de ce qui ne me regarde pas » [al-Muwaṭṭaʾ] ; al-Ḥasan al-Baṣrī — l'occupation par l'inutile, signe du détour de l'attention divine.",
        "Le versant positif : la beauté de l'islam commande aussi l'occupation par ce qui regarde — az-Zarqānī déplie le nécessaire « sans superflu d'aisance », et couronne par la conscience de la proximité.",
        "L'exploitation : le critère de la parole — « si tu t'en taisais, tu n'encourrais ni faute ni dommage, ni à l'immédiat ni à terme » ; l'échange du moindre contre le meilleur — le trésor du Paradis contre une bourse (badra) [Dalīl al-fāliḥīn, qui l'attribue à al-Ġazālī] ; la préparation annonce la leçon 18, « Aimer le bien pour les gens ».",
    ],
    "vocabulaire": [
        {"ar": "ترك ما لا يعنيه", "translit": "tarku mā lā yaʿnīhi", "fr": "le délaissement de ce qui ne le regarde pas — le titre de la leçon et le mouvement du hadīth tout entier : quitter l'inutile, tenir l'utile."},
        {"ar": "من حسن إسلام المرء", "translit": "min ḥusni islāmi l-marʾ", "fr": "il est de la beauté de l'islam d'un homme — l'ouverture du matn : la beauté comme mesure de la religion."},
        {"ar": "حسن", "translit": "ḥusn", "fr": "le beau — « le beau est le contraire du laid » : l'islam se dit beau, et sa beauté se prouve par un délaissement."},
        {"ar": "المرء", "translit": "al-marʾ", "fr": "l'homme, la personne — la règle vaut pour tout responsable : nul n'est dispensé du tri."},
        {"ar": "ما لا يعنيه", "translit": "mā lā yaʿnīhi", "fr": "ce qui ne l'importe pas — « parmi les affaires de la religion et de la vie d'ici-bas » : l'utile se mesure aux deux demeures ensemble."},
        {"ar": "العناية", "translit": "al-ʿināya", "fr": "le soin — « l'intensité de l'attention portée à une chose » ; ʿanāhu yaʿnīhi, « il l'a pris à cœur », lorsqu'il s'en est soucié et l'a recherchée."},
        {"ar": "الاشتغال بما لا يعني", "translit": "al-ištiġālu bi-mā lā yaʿnī", "fr": "l'occupation par ce qui ne regarde pas — le mal que la leçon expose : ses effets sur le temps, les obligations, le cœur."},
        {"ar": "الآثار", "translit": "al-āṯār", "fr": "les effets, les suites — le titre du deuxième axe de l'analyse : le statut prouve par ses conséquences."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-17', E_17)]


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
for DOCID in ('pdf-17',):
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
