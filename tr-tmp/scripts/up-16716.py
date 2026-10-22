#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16716 (tawhid-1es, leçon 6 — parmi les
plus beaux noms de Dieu indiquant Ses attributs).

Vérifications et restitutions (cache quran = Ḥafṣ) :
- Matn : « العالم الخبير المدبر القدير السميع البصير العلي الكبير، وأنه فوق
  عرشه المجيد بذاته، وهو في كل مكان بعلمه » — rendu fidèlement.
- NUMÉROTATION : cette leçon suit la numérotation Ḥafṣ STANDARD (toutes les
  réfs imprimées vérifiées CONFORMES : Ḥadīd 4, Sajda 5, Yūnus 3, Raʿd 2,
  Baqara 106 [fin « ...قدير »], Kahf 45 [fin « مقتدرا »], Zukhruf 80,
  Shūrā 11, Ghāfir 12 [fin « العلي الكبير »], Naml 26, Burūj 15
  « ذو العرش المجيد », Mujādala 7) — à la différence des leçons 5 et 7
  (décalage −1) : les pages CMS du livre ne sont pas homogènes — documenté.
- CITATIONS VIDES (perte OCR) RESTAURÉES du cache : Ḥadīd 4 (istiwāʾ),
  Sajda 5 (yudabbir), Yūnus 3, Raʿd 2, Baqara 106, Kahf 45, Zukhruf 80
  (« أم يحسبون أنا لا نسمع سرهم » — la glose « أي نسمعها » s'y accorde),
  Shūrā 11, Ghāfir 12, Naml 26, Burūj 15, Mujādala 7 (maʿiyya bi-l-ʿilm).
- Ibn Kathīr (istithmār) : le récit d'Ubayy b. Kaʿb (hadith d'āyat al-Kursī
  « ليهنك العلم أبا المنذر... لها لسان وشفتان تقدس الملك عند ساق العرش »)
  [تفسير ابن كثير 1/672] — rendu INTÉGRALEMENT tel qu'imprimé (hadith
  Muslim 810 ; la glose « أَبِي هُوَ ابْنُ كَعْبٍ » imprimée telle quelle).
- Lisan al-ʿArab cité pour la qudra [مادة قدر] — réf rendue.
- « أصمخة » (pl. d'asmakh) : conques de l'oreille — rendu « conques ».
- FIX GT-ismes : « le Superviseur » (المدبر !) → « le Disposant » ;
  « tawqifiyya » expliqué ; « al-Majid le trône glorieux » → structure
  correcte (Majīd épithète du Trône).
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : parmi les plus beaux noms de Dieu, ceux qui indiquent Ses attributs</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la sixième leçon (6).</p>
<ul>
<li>Connaître quelques-uns des plus beaux noms de Dieu et leurs implications.</li>
<li>Distinguer entre les implications de ces noms.</li>
<li>Se parer, en ma vie, des sens des plus beaux noms de Dieu.</li>
</ul>
<h2>Préambule</h2>
<p>Les intelligences sont impuissantes à méditer l’essence du Vrai, Puissant et Élevé, et à saisir Sa quiddité : les intelligences et les vues ne Le saisissent point. Or Il ordonna, Puissant et Élevé, de méditer Ses créatures pour en inférer [Son existence] ; et le consensus se forma sur l’obligation de Le connaître, l’Elevé, par Ses noms et Ses attributs rapportés dans le Coran et la Sunna.</p>
<p>Quels sont donc les noms mentionnés dans le <em>matn</em> ? Quelle est leur portée ? Et qu’est-ce qui nous est dû à leur endroit ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « le Savant, le Bien-Informé ; le Disposant, le Puissant ; l’Audiant, le Voyant ; le Très-Haut, le Grand — et qu’Il est, en Son essence, au-dessus de Son Trône magnifique (<em>majīd</em>) ; et qu’Il est en tout lieu par Sa science. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>al-mudabbir</em> (le Disposant) : la disposition (<em>tadbīr</em>), pour les hommes, est la considération des issues des affaires ; envers Dieu, c’est l’arrêt définitif de l’affaire, son exécution et son décret selon Sa volonté et Sa science.</li>
<li><em>al-baṣīr</em> (le Voyant) : attribut qui se rapporte à tout existant sur le mode de la pleine clarté.</li>
<li>le Très-Haut, le Grand : <em>al-ʿAlī</em> est Sa qualité et Son titre aux attributs de majesté et de grandeur.</li>
<li><em>al-majīd</em> (le magnifique) : dérivé de <em>majada-istamjada</em>, “ il accrut ” — et la <em>majd</em> est le comble de la noblesse.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du texte les plus beaux noms de Dieu qu’il contient.</li>
<li>J’extrais du <em>matn</em> la portée de Sa parole — [al-Ḥadīd : 4].</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient deux axes :</p>
<h3>Premièrement : parmi les plus beaux noms de Dieu</h3>
<p>1. <em>al-ʿĀlim</em> (le Savant) : dérivé de la science (<em>ʿilm</em>) — attribut par lequel se dévoilent toutes les choses sues : les nécessaires, les possibles et les impossibles. De Ses noms aussi : <em>al-ʿAllām</em> et <em>al-ʿAlīm</em>. Et Il ne se nomme ni connaissant (<em>ʿārif</em>), ni pénétrant (<em>fatīn</em>), ni intelligent (<em>ʿāqil</em>), ni sage-de (<em>dārī</em>) : car les noms de Dieu Très-Haut sont d’attestation (<em>tawqīfiyya</em>) — on ne Le nomme, Puissant et Élevé, que de ce dont Il Se nomma Lui-même dans le noble Coran, ou de ce dont Le nomma Son prophète — sur lui la prière et le salut —, ou de ce sur quoi se forma le consensus.</p>
<p>2. <em>al-Khabīr</em> (le Bien-Informé) : le Savant des recoins cachés des affaires, auxquels nul autre que Lui n’atteint — comme <em>al-Shahīd</em> est Celui qui est informé de leurs apparences, et <em>al-ʿAlīm</em>, Celui qui est informé de leurs apparences et de leurs profondeurs.</p>
<p>3. <em>al-Mudabbir</em> (le Disposant) : il ne vint pas en cette forme parmi les noms les plus beaux ; son verbe vint dans le Coran, en Sa parole :</p>
<p>« Il dispose l’affaire du ciel vers la terre ; puis elle remonte vers Lui en un jour dont la mesure est de mille ans, de ceux que vous comptez. » (al-Sajda, 5)</p>
<p>et Sa parole :</p>
<p>« Certes, votre Seigneur est Dieu, qui créa les cieux et la terre en six jours, puis s’établit sur le Trône, disposant l’affaire... » (Yūnus, 3 — extrait)</p>
<p>et Sa parole, Puissant et Élevé :</p>
<p>« Dieu — qui éleva les cieux sans colonnes que vous voyiez — puis s’établit sur le Trône... dispose l’affaire... » (al-Raʿd, 2 — extrait)</p>
<p>[Trois citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES (numérotation Ḥafṣ de cette leçon — cf. notes).] — c’est-à-dire : Lui seul, Puissant et Élevé, décrète l’affaire de Sa création : en ce monde, par leurs subsistances ; en l’au-delà, par leur computation.</p>
<p>Et la disposition, pour les hommes, est le regard et l’emploi de la pensée sur les issues des affaires — leurs fins (<em>adbār</em>) — pour les poser à la face la plus droite et la plus parfaite ; tandis qu’envers Lui, l’Elevé, le sens du Disposant est : le Savant du devenir des affaires et de leurs issues, et de ce qui s’en cache — le sens de la disposition étant alors : l’arrêt définitif de l’affaire, son exécution et son décret, au comble de la parfaite solidité.</p>
<p>4. <em>al-Qadīr</em> (le Puissant) : dérivé de la puissance (<em>qudra</em>) — au sens propre : la force [<em>Lisān al-ʿArab</em>, racine <em>q-d-r</em>] ; au sens technique : attribut éternel établi en Son essence, l’Elevé, par lequel adviennent l’institué et l’anéanti du possible, selon la volonté — il ne se rapporte qu’aux possibles, et se rapporte universellement à l’ensemble des possibles. Le Très-Haut dit :</p>
<p>« Ce que Nous abrogeons d’un signe, ou que Nous faisons oublier — Nous en apportons un meilleur ou un pareil. Ne sais-tu pas que Dieu est, sur toute chose, Puissant ? » (al-Baqara, 106)</p>
<p>Et le Très-Haut dit :</p>
<p>« Et propose-leur la parabole de la vie d’ici-bas : une eau que Nous fîmes descendre du ciel, où la pousse de la terre se mêla, puis elle devint brins desséchés que les vents dispersent... Et Dieu fut, sur toute chose, Puissant-possesseur. » (al-Kahf, 45)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.] Et <em>al-Qadīr</em> est un schème d’intensité, eu égard à la multitude des objets de Sa puissance.</p>
<p>5. <em>al-Samīʿ al-Baṣīr</em> (l’Audiant, le Voyant) : ils sont de Ses noms, l’Elevé. L’oïe et la vue sont deux attributs par lesquels se dévoile l’existant, sur un mode que Lui, Puissant et Élevé, connaît ; et comme Son essence, l’Elevé, ne ressemble pas aux essences, de même Ses attributs ne ressemblent pas aux attributs : Il voit, l’Elevé, et entend les essences et les attributs, le manifeste et le caché, le secret et le public. Le Très-Haut dit :</p>
<p>« Ou bien comptent-ils que Nous n’entendons point leur secret et leur confidence ? Oh que si — et Nos scribes sont auprès d’eux, écrivant. » (al-Zukhruf, 80)</p>
<p>— c’est-à-dire : Nous l’entendons. Et le Très-Haut dit :</p>
<p>« ...il n’est rien qui Lui soit semblable ; et Il est l’Audiant, le Voyant. » (al-Shūrā, 11 — extrait)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.] Son ouïe, l’Elevé, se rapporte à tout existant — cet existant fût-il éternel ou survenu, fût-il de ceux dont nous percevons le son ou non : Son essence et Ses attributs, comme nos essences et nos attributs, Lui sont ouïes, Puissant et Élevé, de Son ouïe, sur un mode que Lui seul connaît.</p>
<p>6. <em>al-ʿAlī al-Kabīr</em> (le Très-Haut, le Grand) : le Grand au-dessus des attributs de Sa création, tel que nul autre que Lui ne saisit la réalité de Sa hauteur et de Sa grandeur. Sa hauteur et Sa grandeur ont pour sens : le rang, la dignité et les attributs intelligibles — non le lieu ni les attributs sensibles : Il voit sans pupille ni paupières, entend sans conques ni oreilles, parle sans lèvre ni langue, saisit sans organe, crée sans instrument, dispose sans pensée ni ordonnancement ; nulle distance ne voile Son ouïe, nulle obscurité ne repousse Sa vue — car tout cela est du nombre des implications de l’imperfection et de la survenance, et Ses attributs, l’Elevé, n’ont ni imperfection ni survenance. Sa hauteur, Puissant et Élevé, n’est pas hauteur de direction ni particularité de lieu : <em>al-ʿAlī</em> est Sa qualité — Son titre aux attributs de majesté ; et la grandeur (<em>kibriyāʾ</em>) est Sa description — Son titre aux attributs de beauté. Dieu, l’Elevé, dit :</p>
<p>« ...Il en est ainsi parce que, quand Dieu seul est invoqué, vous mécroyez ; et quand on Lui donne des associés, vous croyez. Le jugement appartient à Dieu, le Très-Haut, le Grand. » (Ghāfir, 12 — extrait)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<h3>Deuxièmement : Son établissement, Puissant et Élevé, sur Son Trône, et Sa présence (<em>maʿiyya</em>) auprès de Sa création</h3>
<p>1. Son établissement sur Son Trône. L’auteur — que Dieu lui fasse miséricorde — dit : « et qu’Il est, en Son essence, au-dessus de Son Trône magnifique » — le sens en est que Sa surélévation, l’Elevé, sur Son Trône, est surélévation de possession, de royauté, de conquête et d’empire : car le possesseur est au-dessus du possédé, et le Créateur au-dessus de la créature ; Sa surélévation revient donc au sens de la royauté et de l’empire — non à une surélévation sensible, celle-ci Lui étant impossible : l’interprétation est obligée par l’indice de l’impossibilité de la ressemblance aux survenus. Et le Trône est une créature immense au-dessus des sept cieux, dont l’existence est indiquée par le Livre, la Sunna et le consensus ; et <em>majīd</em> est épithète du Trône : le magnifique par Son essence et en Son essence. Le Très-Haut dit :</p>
<p>« Dieu — il n’est de dieu que Lui, le Seigneur du Trône immense. » (al-Naml, 26)</p>
<p>Et le Très-Haut dit :</p>
<p>« ...Possesseur du Trône magnifique. » (al-Burūj, 15 — extrait)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.]</p>
<p>2. Sa présence auprès de Sa création par Sa science. L’auteur — que Dieu lui fasse miséricorde — dit : « et qu’Il est en tout lieu par Sa science » : Sa science, l’Elevé, embrasse l’ensemble des êtres en leurs lieux — Il est informé de la totalité de leurs états. Le Très-Haut dit :</p>
<p>« Ne vois-tu pas que Dieu sait ce qui est dans les cieux et ce qui est dans la terre ? Point de confidence entre trois qu’Il ne soit leur quatrième... » (al-Mujādala, 7 — extrait)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.] Le verset indique donc l’ampleur de Sa science, l’Elevé, et Son embrassement de toute chose, nombreuse ou rare, grande ou vile : Dieu, Puissant et Élevé, a embrassé toute chose en science — et Il est, de toute chose, savant. Et le sens de Sa présence par Sa science est : le rapport de la science à toute chose en son lieu — non la cohabitation de l’essence en le lieu, par transcendance à Son endroit. La présence peut aussi être, envers Lui, l’Elevé, au sens du secours et de la garde. Et de Sa parole : « et qu’Il est en tout lieu par Sa science », on n’entend pas la direction — car Il est, Puissant et Élevé, trop saint pour le lieu ; ni que Sa science soit morcelée, séparée de Son essence : elle est un attribut éternel qui ne quitte pas l’essence. On ne vise que ceci : que Sa science embrasse l’ensemble des êtres en leurs lieux, et embrasse l’ensemble des lieux.</p>
<h2>Les fruits de la leçon</h2>
<ul>
<li>L’obligation de se tenir sous la vigilance de Dieu, Puissant et Majestueux : qui sait qu’Il est, Puissant et Élevé, l’Audiant, le Voyant, se surveille en ses mouvements et ses repos — ni qu’on Le trouve où Il l’a interdit, ni qu’on Le manque où Il l’a ordonné.</li>
<li>Conserver les plus beaux noms de Dieu, en s’attachant à ce qu’ils exigent, et L’invoquer, Puissant et Élevé, par eux — en réalisation de la fin de la servitude.</li>
<li>Remettre au Créateur la disposition de ses affaires — Lui qui dispose les affaires — pour que l’âme s’apaise.</li>
<li>Affermir la foi et la confiance en Dieu, qui conduisent à la sincérité de l’œuvre et à la vérité de l’orientation vers Lui, Puissant et Élevé.</li>
</ul>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Je donne les sens des plus beaux noms de Dieu qui suivent : le Savant ; le Bien-Informé ; l’Audiant ; le Voyant ; le Disposant.</li>
<li>J’expose le sens de la parole de l’auteur : « et qu’Il est en tout lieu par Sa science ».</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>D’Ibn Kathīr — que Dieu lui fasse miséricorde —, en son commentaire du verset du Kursī : « C’est là le verset du Kursī, dont le rang est immense : le hadith fit preuve, du Messager de Dieu — paix et bénédiction sur lui —, qu’il est le plus excellent verset du livre de Dieu. L’imam Aḥmad rapporta d’Abū [c’est-à-dire Ibn Kaʿb] que le Prophète — paix et bénédiction sur lui — l’interrogea : “ Quel est le plus grand verset du livre de Dieu ? Il dit : Dieu et Son Messager le savent mieux. Il le lui répéta plusieurs fois, puis Abū dit : le verset du Kursī. Il dit : Que la science te soit une joie, Abū al-Mundhir ! — par Celui qui tient mon âme en Sa main : certes il a une langue et deux lèvres, qui sanctifient le Roi auprès du pied du Trône. ” » [Le <em>Tafsīr</em> d’Ibn Kathīr : 1/672 — citation intégrale et conforme ; réf rendue telle qu’imprimée.]</p>
<p>Je lis le verset du Kursī, en extrais les plus beaux noms de Dieu qu’il contient, et compare cela avec ce qui est en la leçon.</p>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et en extrais ce qui indique la grandeur de Dieu Très-Haut en Son monde et en Sa science.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16716":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16716 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16716 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
