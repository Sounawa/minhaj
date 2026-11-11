#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12986 (hadith-1es, les règles de
l'oubli dans la prière — 1ʳᵉ partie — Muwaṭṭaʾ n° 247-249/251/253 +
Bukhārī + Abū Dāwūd/Tirmidhī/Ibn Ḥibbān/Ḥākim).

Conventions main (cf. 12875-12985 du même livre) :
- h1 « Règles sur l'oubli dans la prière — première partie (aḥkām
  al-sahw fī l-ṣalāh — 1) », 21e leçon (source : « -1- » + « الجزء
  الأول وله تتمة »).
- Préambule : Muwaṭṭaʾ 253 (règle mālikite : tout sahw-retranchement →
  prosternation AVANT le salut ; tout sahw-addition → APRÈS).
- Hadiths : 247 (Muḥammad b. ʿAmr b. ʿAlqama/Malīḥ b. ʿAbd Allāh
  al-Saʿdī/Abū Hurayra : « sa mèche est dans la main d'un diable ») ;
  248 (Yaḥyā/Mālik : revenir incliné ou prosterné sans attendre
  l'imam — « l'imam n'est institué que pour qu'on le suive : ne
  divergez pas sur lui ») ; **hadith 247 DOUBLÉ par OCR dans la liste
  (3e li sans isnād ni numéro) — traduit une seule fois, précédent
  R118/180** ; 249 (Ayyūb al-Sakhtiyānī/Ibn Sīrīn/Abū Hurayra :
  Dhū l-Yadayn — « la prière a-t-elle été abrégée ou as-tu oublié ? » ;
  « Dhū l-Yadayn a-t-il dit vrai ? » ; 2 rakʿas + salut + takbīr +
  2 prosternations ou plus long).
- Lexique : nāṣiya (mèche), li-yuʾtama bihi, inṣarafa min ithnatayn,
  a-qṣurat al-ṣalāt (les DEUX lectures vocaliques — passif « Dieu
  l'a abrégée » / actif « elle devint courte »).
- Taḥlīl I : avertissement (mawqūf — al-Bājī : menace + docilité à
  Satan ; Ibn al-ʿArabī : la hâte, remède = se représenter qu'on ne
  salue pas avant l'imam ; jumhūr : prière valide) ; règle (revenir
  incliné/prosterné — muqārana/musābaqa/mukhālafa éliminées).
- Taḥlīl II : Dhū l-Yadayn — Ẓuhr ou ʿAṣr ? (2 fois vs doute du
  rapporteur — rājiḥ) ; 2 rakʿas + 2 prosternations APRÈS le salut
  pour l'addition (salut + parole) ; permission du sahw aux prophètes
  en la voie du tashrīʿ (sans y être laissés) — « j'oublie ou suis
  fait oublier, pour instituer la sunna » [Muwaṭṭaʾ, n° 226 — réf.
  imprimée du manuel, cf. 12961 où le même n° couvre le hadith
  qudsī/khidāj : numérotation du CMS reprise telle quelle].
- Taḥlīl III : iḥrām du sujūd al-sahw (jumhūr : le takbīr suffit ;
  Mālik : takbīr obligatoire sans invalidation ; niyya d'achever
  indispensable ; al-Qurṭubī : thumma = délai → takbīr d'iḥrām) ;
  tashahhud du sujūd al-sahw (absent de Dhū l-Yadayn ; Salama b.
  ʿAlqama/Ibn Sīrīn chez Bukhārī : « il n'est pas dans le hadith
  d'Abū Hurayra » — impliqué : venu chez un autre ; ʿImrān b.
  Ḥuṣayn : 2 prosternations PUIS tashahhud PUIS salut).
- Istimḥār : Muwaṭṭaʾ 251 (version Dhū l-Shimālayn — Abū Bakr b.
  Sulaymān b. Abī Ḥathma ; « la prière ne fut pas abrégée et je
  n'ai pas oublié » ; « une partie de cela a eu lieu » ; achève ce
  qui reste SANS prosternations) + comparaison/conciliation.
- Préparation préalable : leçon SUIVANTE 12987 (shaffaʿahā/targhīm/
  qaḍā ṣalātahu ; doute 3 ou 4 rakʿas ; lever après l'achèvement).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Règles sur l’oubli dans la prière — première partie (<em>aḥkām al-sahw fī l-ṣalāh — 1</em>)</h1>
<p>Leçon sur les règles de l’oubli (<em>sahw</em>) dans la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-et-unième leçon, première partie, qui a une suite.</p>
<ol>
<li>Connaître le statut de qui oublia dans sa prière et releva la tête avant l’imam, ou fit le salut final au bout de deux rakʿas.</li>
<li>Comprendre le rapport du suivi à l’imam dans la prière.</li>
<li>Me conformer aux règles de l’oubli s’il se présente dans ma prière.</li>
</ol>
<h2>Préambule</h2>
<p>Parmi les rapports transmis de l’imam Mālik sur les règles de l’oubli dans la prière : « Tout oubli qui fut un retranchement de la prière, sa prosternation est avant le salut ; et tout oubli qui fut une addition dans la prière, sa prosternation est après le salut. » [Muwaṭṭaʾ, n° 253]</p>
<p>Quel est donc le statut de qui oublia dans sa prière et releva la tête avant l’imam ? Et quelle est la règle pour qui fit le salut final au bout de deux rakʿas ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Muḥammad ibn ʿAmr ibn ʿAlqama, d’après Malīḥ ibn ʿAbd Allāh al-Saʿdī, d’après Abū Hurayra : « qu’il dit : Celui qui relève sa tête et l’abaisse avant l’imam — sa mèche (<em>nāṣiya</em>) est dans la main d’un diable. » [Muwaṭṭaʾ, n° 247]</li>
<li>Yaḥyā a dit : « Mālik dit, sur celui qui oublia et releva la tête avant l’imam dans une inclinaison ou une prosternation : la sunna, en cela, est qu’il revienne incliné ou prosterné, sans attendre l’imam — et c’est une faute de qui le fit, car le Messager de Dieu — paix et bénédiction sur lui — dit : “L’imam n’est institué que pour qu’on le suive : ne divergez pas sur lui.” » [Muwaṭṭaʾ, n° 248]</li>
<li>D’après Mālik, d’après Ayyūb ibn Abī Tamīma al-Sakhtiyānī, d’après Muḥammad ibn Sīrīn, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — s’en fut au terme de deux [rakʿas] ; Dhū l-Yadayn lui dit : La prière a-t-elle été abrégée, ou as-tu oublié, ô Messager de Dieu ? Le Messager de Dieu — paix et bénédiction sur lui — dit : “Dhū l-Yadayn a-t-il dit vrai ?” Les gens dirent : Oui. Le Messager de Dieu — paix et bénédiction sur lui — se leva alors et pria deux autres rakʿas, puis fit le salut, puis fit le takbīr et se prosterna comme sa prosternation — ou plus long —, puis releva la tête, puis fit le takbīr et se prosterna comme sa prosternation — ou plus long —, puis releva la tête. » [Muwaṭṭaʾ, n° 249]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>nāṣiyatuhu</em> (« sa mèche ») : les cheveux du devant de sa tête.</li>
<li><em>li-yuʾtama bihi</em> (« pour qu’on le suive ») : pour qu’on prenne modèle sur lui dans les états de la prière.</li>
<li><em>inṣarafa min ithnatayn</em> (« s’en fut au terme de deux ») : il fit le salut final au bout de deux rakʿas.</li>
<li><em>a-qṣurat al-ṣalāt</em> (« la prière a-t-elle été abrégée ? ») : avec ḍamma du <em>qāf</em> et kasra du <em>ṣād</em>, au passif — Dieu l’a abrégée ; avec fatha du <em>qāf</em> et ḍamma du <em>ṣād</em>, à l’actif — elle est devenue courte.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Quel est le statut de qui releva la tête de l’inclinaison ou de la prosternation avant l’imam dans la prière ?</li>
<li>Que fait celui qui fit le salut final au bout de deux rakʿas ?</li>
<li>Explicite le statut de qui commit dans sa prière un oubli par addition.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut du relèvement de la prosternation ou de l’inclinaison avant l’imam</h3>
<h4>L’avertissement contre le relèvement avant l’imam</h4>
<p>Il fut rapporté d’Abū Hurayra, comme interrompu [sur lui] (<em>mawqūf</em>) : “Celui qui relève sa tête et l’abaisse avant l’imam — sa mèche est dans la main d’un diable.” Al-Bājī a dit : son sens est la menace (<em>waʿīd</em>) contre qui fait cela, et l’information que cela provient de l’action de Satan sur lui : sa docilité envers lui — son obéissance à Satan dans la hâte de l’abaissement et du relèvement avant son imam — est la docilité de celui dont la mèche est en sa main.<br>
Ibn al-ʿArabī a dit : il n’est d’autre cause à l’avance avant l’imam que la recherche de la hâte ; son remède : qu’il se représente qu’il ne dit pas le salut avant l’imam — il ne se hâtera donc pas en ces actes. Le <em>jumhūr</em> tient la validité de la prière : nulle répétition ne lui incombe, comme il viendra.</p>
<h4>Le statut de qui releva sa tête ou l’abaisssa avant l’imam</h4>
<p>L’imam Mālik exposa le statut de qui oublia et releva la tête avant l’imam dans une inclinaison ou une prosternation, par sa parole : « La sunna, en cela, est qu’il revienne incliné ou prosterné, sans attendre l’imam » — et il appuya par sa parole — paix et bénédiction sur lui — : « L’imam n’est institué que pour qu’on le suive », c’est-à-dire : pour qu’on prenne modèle sur lui — s’éliminent donc la parité (<em>muqārana</em>), la course (<em>musābaqa</em>) et la divergence (<em>mukhālafa</em>), comme il vient dans la suite du hadith : « ne divergez pas sur lui » — le relèvement avant lui, et l’abaissement, sont de la divergence sur lui : il revient donc, pour relever après son relèvement, et abaisser après son abaissement.</p>
<h3>Deuxièmement : le statut de qui fit le salut final au bout de deux rakʿas</h3>
<p>Il vient au hadith de Dhū l-Yadayn que le Prophète — paix et bénédiction sur lui — fit le salut final au bout de deux rakʿas ; les narrations divergèrent sur la prière dont il s’en fut : les uns dirent le Ẓuhr, d’autres le ʿAṣr. Certains savants portèrent cette divergence sur ce que l’histoire survint deux fois — une fois au Ẓuhr, une fois au ʿAṣr ; d’autres — et c’est le prépondérant (<em>rājiḥ</em>) — la portèrent sur le doute du rapporteur : tantôt prévalait, à son avis, que c’était le Ẓuhr, et il l’affirmait ; tantôt prévalait que c’était le ʿAṣr, et il l’affirmait.<br>
Et quand il en fut informé — paix et bénédiction sur lui —, il revint et pria deux autres rakʿas, puis se prosterna de deux prosternations après le salut, pour l’addition : car il avait ajouté le salut et la parole — selon sa parole : « Le Messager de Dieu — paix et bénédiction sur lui — se leva et pria deux autres rakʿas, puis fit le salut, puis fit le takbīr et se prosterna comme sa prosternation — ou plus long —, puis releva, puis fit le takbīr et se prosterna comme sa prosternation — ou plus long —, puis releva. » Il y a en cela : la permission de l’oubli aux prophètes, en ce qui est de la voie de la législation (<em>tashrīʿ</em>), bien qu’ils n’y soient pas laissés ; et le bénéfice de la permission de l’oubli en ce genre : l’exposé de la règle légale quand son pareil survient à un autre — car l’imam Mālik rapporta par sa chaîne : « qu’il lui parvint que le Messager de Dieu — paix et bénédiction sur lui — dit : “Moi, j’oublie — ou je suis fait oublier — pour instituer la sunna.” » [Muwaṭṭaʾ, n° 226]</p>
<h3>Troisièmement : les règles de la prosternation de l’oubli</h3>
<h4>Le statut de l’entrée en prière pour la prosternation de l’oubli</h4>
<p>Les savants divergèrent : la prosternation de l’oubli après le salut exige-t-elle une entrée en prière (<em>iḥrām</em>), ou le takbīr de la prosternation suffit-il ? Le <em>jumhūr</em> : on se contente du takbīr de la prosternation ; l’école de Mālik : le takbīr est obligatoire, mais la prière n’est pas invalidée par son délaissement ; quant à l’intention d’achever ce qui reste, elle en est indispensable. Le hadith de Dhū l-Yadayn indique la légitimité du takbīr, car il y a : « il pria deux autres rakʿas, puis fit le salut, puis fit le takbīr » — al-Qurṭubī a dit : il y a là indication que le takbīr est celui de l’entrée en prière, du fait du <em>thumma</em> qui implique le délai : si le takbīr avait été celui de la prosternation, il eût été avec elle.</p>
<h4>Le statut du tashahhud pour la prosternation de l’oubli</h4>
<p>Il n’est point venu, dans le hadith de Dhū l-Yadayn, de mention d’un <em>tashahhud</em> après les deux prosternations de l’oubli ; il vient dans sa description : « il fit le takbīr et se prosterna comme sa prosternation — ou plus long —, puis releva, puis fit le takbīr et se prosterna comme sa prosternation — ou plus long —, puis releva » — sans mentionner qu’il récitât le <em>tashahhud</em> après les deux prosternations de l’oubli. Al-Bukhārī rapporta à la suite de ce hadith, d’après Salama ibn ʿAlqama : « je dis à Muḥammad — c’est-à-dire Ibn Sīrīn — : y a-t-il un <em>tashahhud</em> dans les deux prosternations de l’oubli ? Il dit : il n’est pas dans le hadith d’Abū Hurayra » — le sens impliqué : il est venu dans le hadith d’un autre.<br>
Abū Dāwūd, at-Tirmidhī, Ibn Ḥibbān et al-Ḥākim rapportèrent d’ʿImrān ibn Ḥuṣayn : « que le Prophète — paix et bénédiction sur lui — pria avec eux, oublia, se prosterna de deux prosternations, puis récita le <em>tashahhud</em>, puis fit le salut. »</p>
<h2>L’évaluation</h2>
<ol>
<li>Explicite le statut de qui releva la tête de l’inclinaison ou de la prosternation avant l’imam.</li>
<li>Que signifie sa parole — paix et bénédiction sur lui — : « L’imam n’est institué que pour qu’on le suive » ?</li>
<li>Extrais du hadith de Dhū l-Yadayn le statut de l’entrée en prière et du <em>tashahhud</em> pour la prosternation de l’oubli.</li>
</ol>
<h2>L’exploitation</h2>
<p>D’après Mālik, d’après Ibn Shihāb, d’après Abū Bakr ibn Sulaymān ibn Abī Ḥathma : « qu’il lui parvint que le Messager de Dieu — paix et bénédiction sur lui — s’inclina de deux rakʿas de l’une des deux prières du jour — le Ẓuhr ou le ʿAṣr — et fit le salut final au terme de deux ; Dhū l-Shimālayn — un homme des Banū Zuhra ibn Kilāb — lui dit : La prière a-t-elle été abrégée, ô Messager de Dieu, ou as-tu oublié ? Le Messager de Dieu — paix et bénédiction sur lui — lui dit : “La prière n’a point été abrégée, et je n’ai point oublié.” Dhū l-Shimālayn dit : Une partie de cela a bien eu lieu, ô Messager de Dieu. Le Messager de Dieu — paix et bénédiction sur lui — se tourna vers les gens et dit : “Dhū l-Yadayn a-t-il dit vrai ?” Ils dirent : Oui, ô Messager de Dieu. Le Messager de Dieu — paix et bénédiction sur lui — acheva ce qui restait de la prière, puis fit le salut. » [Muwaṭṭaʾ, n° 251]</p>
<ol>
<li>Compare ce hadith au hadith de la leçon, en exposant les points de ressemblance et les points de différence.</li>
<li>Comment concilier les deux hadiths ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Explique ce qui suit : <em>shaffaʿahā</em> (il la compléta paire) – <em>targhīm</em> (l’humiliation [du diable]) – <em>qaḍā ṣalātahu</em> (il accomplit sa prière).</li>
<li>Quel est le statut de qui doute dans sa prière : a-t-il prié trois rakʿas ou quatre ?</li>
<li>Explicite le statut de qui se leva après l’achèvement de sa prière, par addition.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12986":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12986 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12986 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
