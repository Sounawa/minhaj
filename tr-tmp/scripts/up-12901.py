#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12901 (hadith-1es, des règles de
l'impureté majeure — Muwaṭṭaʾ n° 120-131, 135).

Conventions main (cf. 12875, 12884-12899 du même livre) :
- h1 « Des règles de l'impureté majeure (min aḥkām al-janāba) », 9e leçon.
- L'objectif imprimé unique (« كتاب الحديث من رياض الصالحين للإمام النووي »)
  est un artefact d'extraction (référence au Riyāḍ al-Ṣāliḥīn d'al-Nawawī —
  hors sujet : le manuel-commentaire est le Muwaṭṭaʾ/Zarqānī) → objectifs
  reconstitués des 4 thèmes du tamhīd.
- Muwaṭṭaʾ 120 (ʿUmar : « fais tes ablutions, lave ton sexe, puis dors »),
  121 (ʿĀʾisha), 122 (Ibn ʿUmar — excuse du fadaʿ de Khaybar), 123 (le
  Prophète sort en pleine prière, revient trace d'eau sur la peau), 124
  (Zayd ibn al-Ṣalt — ʿUmar à al-Juruf, refaire la prière), 126 (le wadak —
  « les veines s'amollissent »), 127 (ʿAmr ibn al-ʿĀṣ — « si je le faisais,
  ce serait une sunna ! »), 128 (dernier sommeil), 129 (Umm Sulaym — femme /
  rêve ; ʿĀʾisha « fi de toi » / « que ta main droite soit poussiéreuse »),
  130 (Umm Salama/Umm Sulaym « quand elle a vu l'eau »), 131 (reste d'eau de
  la femme), 135 (doigt dans l'eau + sueur de l'impur — n° imprimé deux
  fois, gardé tel quel avec note).
- Ṣaḥīḥ Bukhārī/Muslim (Abū Hurayra « le croyant ne se souille pas »),
  Ibn Abī Shayba (Shaddād — la moitié du lavage), al-Ṭabarānī (Maymūna bint
  Saʿd — Gabriel), vers didactique des ablutions du sommeil.
- « أ نه » imprimé = coquille pour « أنه » ; « فدع » = fadaʿ (déboîtement du
  poignet) — glosé.
- Préparation préalable : questions de la leçon SUIVANTE 12908 (tayammum).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Des règles de l’impureté majeure (<em>min aḥkām al-janāba</em>)</h1>
<p>Leçon sur des règles de l’impureté majeure, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la neuvième leçon.</p>
<ul>
<li>Connaître le statut des ablutions du sommeil de l’impur majeur, et celui de ce qu’il a prié par oubli.</li>
<li>Saisir le statut du vêtement atteint par le sperme.</li>
<li>Saisir le statut de la femme qui a une pollution nocturne (<em>iḥtilām</em>).</li>
</ul>
<h2>Préambule</h2>
<p>À la pureté majeure se rattache un ensemble de règles religieuses distinctes : parmi elles, ce qui concerne les ablutions du sommeil de l’impur majeur et le statut de ce qu’il a prié par oubli ; parmi elles aussi, le statut du vêtement atteint par le sperme, et ce qui concerne la pollution nocturne de la femme. Qu’en est-il de tout cela ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après ʿAbd Allāh ibn Dīnār, d’après ʿAbd Allāh ibn ʿUmar : « qu’il dit : ʿUmar ibn al-Khaṭṭāb fit mention au Messager de Dieu — paix et bénédiction sur lui — qu’une impureté majeure l’atteignait de nuit. Le Messager de Dieu — paix et bénédiction sur lui — lui dit : “Fais tes ablutions, lave ton sexe, puis dors.” » [Muwaṭṭaʾ, n° 120]</li>
<li>D’après Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar, quand il voulait dormir ou manger en état d’impureté majeure, lavait son visage et ses deux mains jusqu’aux coudes, et essuyait sa tête — puis mangeait ou dormait. » [Muwaṭṭaʾ, n° 122]</li>
<li>D’après Mālik, d’après Ismāʿīl ibn Abī Ḥakīm : « qu’ʿAṭāʾ ibn Yasār lui rapporta que le Messager de Dieu — paix et bénédiction sur lui — prononça le <em>takbīr</em> dans une des prières, puis leur fit signe de la main : demeurez [en place] ; il s’en alla, puis revint — et l’on voyait sur sa peau la trace de l’eau. » [Muwaṭṭaʾ, n° 123]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿUrwa ibn al-Zubayr : « qu’Umm Sulaym dit au Messager de Dieu — paix et bénédiction sur lui : La femme voit en rêve ce que voit l’homme — doit-elle se laver ? Le Messager de Dieu — paix et bénédiction sur lui — lui dit : “Oui — qu’elle se lave.” ʿĀʾisha lui dit : Fi de toi ! est-ce que cette femme voit cela ? Le Messager de Dieu — paix et bénédiction sur lui — lui dit : “Que ta main droite soit poussiéreuse ! Et d’où viendrait la ressemblance ?” » [Muwaṭṭaʾ, n° 129]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>manger</em> (<em>yaṭʿam</em>) : prendre de la nourriture.</li>
<li><em>fi de toi</em> (<em>uffin laki</em>) : mot employé pour les choses immondes et le mépris — ici au sens de la réprobation.</li>
<li><em>que ta main droite soit poussiéreuse</em> (<em>turibat yamīnuki</em>) : « sois réduite à la poussière », c’est-à-dire à la pauvreté — sans qu’une invocation soit visée : chez les Arabes, la formule tient lieu de réprobation ou de réprimande.</li>
<li><em>la ressemblance</em> (<em>al-shabah</em>) — avec <em>fatḥa</em> du <em>shīn</em> et du <em>bāʾ</em>, ou <em>kasra</em> du <em>shīn</em> et <em>sukūn</em> du <em>bāʾ</em> : la ressemblance de l’enfant à l’un de ses deux parents, ou à ses proches.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Quel est le statut des ablutions de l’impur majeur pour dormir ?</li>
<li>Expose le statut de ce qu’a prié l’impur majeur par oubli.</li>
<li>Expose le statut du vêtement atteint par le sperme.</li>
<li>La femme doit-elle un lavage si elle a une pollution nocturne ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : les ablutions de l’impur majeur pour dormir, et sa prière par oubli</h3>
<h4>Le statut des ablutions de l’impur majeur pour dormir</h4>
<p>Il est recommandé à l’impur majeur — s’il veut dormir avant le lavage — de laver son sexe, puis de faire avant de dormir les ablutions — les ablutions de la prière. C’est ce qu’on tire de sa parole — paix et bénédiction sur lui : « Fais tes ablutions et lave ton sexe, puis dors. » En ce sens, le <em>wāw</em> n’ordonne pas — comme l’a dit al-Zarqānī ; et dans la version d’Abū Nūḥ, de Mālik : « lave ton sexe, puis fais tes ablutions » ; c’est pourquoi Abū ʿUmar a dit : ceci relève de l’avance et du retard [des mots] — il a voulu : lave ton sexe et fais tes ablutions.</p>
<p>Et atteste que ces ablutions sont comme les ablutions de la prière — et qu’elles ne sont pas pour la prière, mais pour le sommeil — ce que rapporta Mālik, d’après Hishām ibn ʿUrwa, d’après son père, d’après ʿĀʾisha, l’épouse du Prophète — paix et bénédiction sur lui : « qu’elle avait coutume de dire : Quand l’un de vous approche la femme puis veut dormir avant de se laver — qu’il ne dorme pas avant de faire les ablutions, les ablutions de la prière. » [Muwaṭṭaʾ, n° 121]</p>
<p>Ibn ʿAbd al-Barr a dit : « Mālik a fait suivre le hadith d’Ibn ʿUmar de cette parole de ʿĀʾisha, pour enseigner que les ablutions ordonnées ne sont pas [celles] de la prière. » Al-Zarqānī a dit : je dis : et pour enseigner qu’elles leur sont semblables — contre qui tint que les ablutions ordonnées sont le lavage de l’impureté, le lavage du sexe et des mains, c’est-à-dire la propreté, en s’appuyant sur le sens apparent de ce que rapporta Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar, quand il voulait dormir ou manger en état d’impureté majeure, lavait son visage et ses deux mains jusqu’aux coudes, et essuyait sa tête, puis mangeait ou dormait » — [athar] entendu dans le sens d’une excuse : certains savants ont dit qu’il fut atteint à Khaybar, aux deux jambes, du <em>fadʿ</em> — déboîtement du poignet de la main ou du pied — dont le lavage lui nuisait.</p>
<p>Quant à la formule d’impératif dans sa parole « fais tes ablutions », au hadith de la leçon, Ibn ʿAbd al-Barr a dit : « le <em>jumhūr</em> est allé à ce qu’elle soit au sens du recommandé — contre les <em>ẓāhirites</em> ; et ce qui fut transmis d’Ibn al-ʿArabī s’entend d’un recommandé renforcé, non d’une obligation. »</p>
<h4>La sagesse des ablutions de l’impur majeur pour dormir</h4>
<p>Shaddād ibn Aws — le Compagnon, que Dieu soit satisfait de lui — a motivé les ablutions de l’impur majeur pour dormir par [l’idée] qu’elles sont la moitié du lavage de l’impureté majeure — rapporté par Ibn Abī Shayba dans son <em>Muṣannaf</em>, dont les transmetteurs sont dignes de foi. On a dit aussi : sa sagesse est qu’il se ranime pour y revenir, ou pour le lavage, lorsqu’il mouille ses membres ; on a dit : pour qu’il passe la nuit sur l’une de deux puretés, de crainte de mourir dans son sommeil.</p>
<p>Et il vient chez al-Ṭabarānī que Maymūna bint Saʿd dit : « Je dis : Ô Messager de Dieu, l’impur majeur peut-il dormir ? Il dit : Je n’aime pas qu’il dorme en état d’impureté majeure avant de faire ses ablutions : car je crains qu’il ne meure, et que Gabriel ne soit pas auprès de lui. »</p>
<p>Et les ablutions du sommeil de l’impur majeur ne sont pas annulées par l’urine ni par la selle — sauf par le retour au coït. L’a mis en vers le poète :</p>
<p><em>Quand on te demande : quelles ablutions n’annule<br>que le coït ? — les ablutions du sommeil de l’impur majeur.</em></p>
<h4>Le statut de ce qu’a prié l’impur majeur par oubli</h4>
<p>Celui qui prie par oubli, ou ne sait pas qu’il est en état d’impureté majeure : quand il s’en souvient, ou sait qu’il est en état d’annulation — il lui incombe de se purifier et de refaire, obligatoirement, ce qu’il a prié ; du fait de ce que rapporta Mālik, d’après Hishām ibn ʿUrwa, d’après son père, d’après Zayd ibn al-Ṣalt : « qu’il dit : Je sortis avec ʿUmar ibn al-Khaṭṭāb vers al-Juruf ; il regarda : il avait eu une pollution [nocturne] et avait prié sans se laver. Il dit : Par Dieu, il ne me semble rien d’autre sinon que j’ai eu une pollution sans m’en douter, et que j’ai prié sans me laver. Il se lava donc, lava ce qu’il vit sur son vêtement, aspergea ce qu’il ne vit pas, fit l’<em>adhān</em> ou l’<em>iqāma</em>, puis pria après la montée du <em>dhuḥā</em>, en toute quiétude. » [Muwaṭṭaʾ, n° 124]</p>
<h3>Deuxièmement : le statut du vêtement atteint par le sperme</h3>
<p>L’avis de l’imam Mālik est que le sperme (<em>manī</em>) est impur. En conséquence, il incombe à celui dont le vêtement fut atteint par le sperme ce qui suit :</p>
<h4>Le lavage</h4>
<p>Est obligatoire le lavage de la partie du vêtement atteinte par le sperme. La preuve : ce que rapporta Mālik, d’après Yaḥyā ibn Saʿīd, d’après Sulaymān ibn Yasār : « que ʿUmar ibn al-Khaṭṭāb dirigea les gens dans [la prière de] l’aube, puis partit au matin vers sa terre, à al-Juruf, et trouva sur son vêtement une trace de pollution. Il dit : Quand nous touchons la graisse (<em>wadak</em>), les veines s’amollissent. Il se lava, lava la pollution de son vêtement, et revint à sa prière. » [Muwaṭṭaʾ, n° 126] — le <em>wadak</em> est la graisse de la chair et son moelle, qu’on en extrait. L’endroit probant du hadith est ici sa parole : « et il lava la pollution de son vêtement ».</p>
<h4>L’aspersion</h4>
<p>Le <em>naḍḥ</em> est l’aspersion de la main, sans intention : on asperge ce dont on doute que le sperme l’ait atteint. La preuve : ce que rapporta Mālik, d’après Hishām ibn ʿUrwa, d’après son père, d’après Yaḥyā ibn ʿAbd al-Raḥmān ibn Ḥāṭib : « qu’il fit la <em>ʿumra</em> avec ʿUmar ibn al-Khaṭṭāb, dans un convoi où était ʿAmr ibn al-ʿĀṣ ; que ʿUmar campa en un point du chemin, près de points d’eau, et eut une pollution nocturne alors que l’aube allait poindre ; il ne trouva point d’eau avec le convoi, chevaucha donc jusqu’à l’eau, et se mit à laver ce qu’il voyait de cette pollution, jusqu’au plein jour. ʿAmr ibn al-ʿĀṣ lui dit : Tu es déjà au matin, et nous avons des vêtements : laisse donc laver ton vêtement. ʿUmar ibn al-Khaṭṭāb dit : Étonnant, ô ʿAmr ibn al-ʿĀṣ ! soit : tu trouves des vêtements — mais tout le monde trouve-t-il des vêtements ? Par Dieu, si je le faisais, ce serait une <em>sunna</em> ! Non : je lave ce que j’ai vu, et j’asperge ce que je n’ai pas vu. » [Muwaṭṭaʾ, n° 127]</p>
<h3>Troisièmement : le statut de la pollution nocturne de la femme</h3>
<p>La femme a des pollutions [nocturnes], comme l’homme — son cas est comme le sien. Cela n’est pas contredit par l’absence de pollution chez certaines femmes, comme par l’absence de pollution chez certains hommes. Le hadith du chapitre atteste la possibilité et l’occurrence ; et la question de ʿĀʾisha — que Dieu soit satisfait d’elle — atteste le défaut d’occurrence chez certaines femmes.</p>
<p>Les savants sont d’accord (ijmāʿ) : celui qui a eu une pollution — homme ou femme —, s’il n’a pas éjaculé et ne trouve ni humidité ni trace d’éjaculation : point de lavage sur lui, dût-il voir le coït véritable dans son sommeil ; et s’il éjacule, le lavage lui incombe — femme ou homme ; et le lavage, dans la pollution, n’est obligatoire que par l’éjaculation.</p>
<p>Et l’atteste — outre le hadith du chapitre — ce que rapporta Mālik, du hadith d’Umm Salama, l’épouse du Prophète — paix et bénédiction sur lui : « qu’elle dit : Umm Sulaym — l’épouse d’Abū Ṭalḥa l’Anṣārite — vint trouver le Messager de Dieu — paix et bénédiction sur lui — et dit : Ô Messager de Dieu, Dieu n’a pas honte de la vérité : y a-t-il pour la femme un lavage quand elle a eu une pollution ? Il dit : “Oui — quand elle a vu l’eau.” » [Muwaṭṭaʾ, n° 130]</p>
<h3>Quatrièmement : le lavage avec l’eau qui reste d’autrui, et l’introduction du doigt dans l’eau avant le lavage des mains</h3>
<h4>Le lavage avec l’eau qui reste d’autrui</h4>
<p>Il est permis de faire les ablutions avec l’eau qui reste (<em>faḍl</em>) d’autrui, après ses ablutions. La preuve : ce que rapporta Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar avait coutume de dire : il n’y a pas de mal à se laver du reste de la femme — tant qu’elle n’est ni menstruée, ni en état d’impureté majeure. » [Muwaṭṭaʾ, n° 131]</p>
<p>Et ce qui est authentique d’après ʿĀʾisha — que Dieu soit satisfait d’elle — : « Je me lavais, moi et le Messager de Dieu — paix et bénédiction sur lui —, d’un seul récipient, pour l’impureté majeure » ; et son acte avec Maymūna et le reste de ses épouses. Ibn ʿAbd al-Barr a dit : les rapports en ce sens sont massivement transmis.</p>
<h4>Le statut de l’introduction d’un doigt dans l’eau avant le lavage des mains</h4>
<p>Si la main est pure, l’eau n’est pas souillée par l’introduction du doigt. Yaḥyā a dit : on interrogea Mālik au sujet d’un homme en état d’impureté majeure à qui l’on avait posé de l’eau pour s’y laver : distrait, il y introduisit son doigt pour connaître la chaleur de l’eau ou sa fraîcheur. Mālik dit : « S’il n’y avait pas d’impureté sur ses doigts, je ne vois pas que cela lui souille l’eau. » [Muwaṭṭaʾ, n° 135]</p>
<h3>Cinquièmement : la pureté de la sueur de l’impur majeur</h3>
<p>Le corps de l’homme vivant est pur, fût-il non-musulman ; de même sa sueur, sa salive et sa morve. Dans les deux <em>Ṣaḥīḥ</em>, d’après Abū Hurayra — que Dieu soit satisfait de lui — : « que le Prophète — paix et bénédiction sur lui — le rencontra dans l’un des chemins de Médine alors qu’il était en état d’impureté majeure : il se replia [sur lui-même] (c’est-à-dire se rétracta et s’écarta de lui), s’en alla, se lava, puis vint. Il [le Prophète] dit : Où étais-tu, Abū Hurayra ? Il dit : J’étais en état d’impureté majeure, et il me déplaisait de m’asseoir avec toi sans pureté. Il dit : Gloire à Dieu ! le croyant ne se souille pas. » Et Mālik rapporta, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar transpirait dans le vêtement alors qu’il était en état d’impureté majeure, puis y priait. » [Muwaṭṭaʾ, n° 135 — numéro imprimé tel quel]</p>
<h2>L’évaluation</h2>
<ol>
<li>Cite le statut des ablutions du sommeil de l’impur majeur, et sa sagesse.</li>
<li>Quel est le statut de ce qu’a prié l’impur majeur par oubli de son état ?</li>
<li>Expose le statut du vêtement atteint par le sperme.</li>
</ol>
<h2>L’exploitation</h2>
<p>Yaḥyā a dit : Mālik dit, au sujet d’un homme qui trouva sur son vêtement une trace de pollution, sans savoir quand, et ne se rappelant rien de vu en songe : « Qu’il se lave du dernier sommeil qu’il a dormi ; et s’il a prié après ce sommeil, qu’il refasse ce qu’il a prié après ce sommeil — car l’homme peut avoir une pollution sans rien voir, et voir sans avoir de pollution : s’il trouve de l’eau sur son vêtement, le lavage lui incombe. Et ʿUmar ibn al-Khaṭṭāb refit ce qu’il avait prié depuis le dernier sommeil dormi, et ne refit pas ce qui était avant lui. » [Muwaṭṭaʾ, n° 128]</p>
<p>Expose les règles du lavage de l’impureté majeure qui figurent dans le texte.</p>
<h2>La préparation préalable</h2>
<ol>
<li>Quelle est la preuve de la légitimité du <em>tayammum</em> ?</li>
<li>Expose la méthode du <em>tayammum</em>.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12901":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12901 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12901 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
