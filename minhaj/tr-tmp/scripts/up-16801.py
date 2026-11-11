#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16801 (tawhid-1es, leçon imprimée 25 —
ce qu'il faut croire au sujet des Compagnons, que Dieu les agrée).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations :
- 1 citation vide (perte OCR systématique CMS) :
  Baqara 140 CONFORME — la réponse d'Ibn ʿUmar aux Basrans est le fragment
  « قل ءأنتُم أعلم أم الله » (les gens du Livre prétendant connaître mieux
  que Dieu le sort des ancêtres — transposé : Dieu Lui-même a attesté
  l'excellence des Compagnons, nul n'a à enquêter sur eux).
- 4 hadiths/citations VÉRIFIÉS sunnah.com :
  Abū Hurayra « لا تسبوا أصحابي » = Muslim 2540, Kitāb Faḍāʾil al-Ṣaḥāba,
  bāb تحريم سب الصحابة EXACT — CONFORME (variantes : ما بلغ/ما أدرك,
  la répétition d'ouverture en moins) ;
  ʿImrān « خير أمتي قرني » = Bukhārī 3650, Kitāb Faḍāʾil al-Ṣaḥāba, bāb
  فضائل أصحاب النبي ﷺ EXACT — CONFORME (truncation de la réserve
  d'ʿImrān dans l'imprimé) ;
  Ibn Ḥibbān « الله الله في أصحابي » : réf imprimée conservée (Ṣaḥīḥ Ibn
  Ḥibbān, bāb فضل الصحابة والتابعين) — identifié aussi comme Tirmidhī 3862
  (de ʿAbd Allāh b. Mughaffal), noté ;
  al-Ḥākim « قوم يكونون من بعدي يؤمنون بي ولم يروني » : réf imprimée
  conservée (Mustadrak, d'Abū Jumʿa) — non hébergé, pattern documenté R89.
- Citations à réf imprimée conservées : ʿUrwa b. Masʿūd (al-Bayhaqī, al-Sunan,
  bāb de la trêve sur le regard) ; Zarrūq (Sharḥ ʿalā l-Risāla 1/69 — l'œil
  qu'on ne touche pas).
- Doctrines rendues au plus près : les trois fondements de l'obligation
  d'aimer les Compagnons ; la tuḥḍīt du matn ; le taʾwīl du conflit
  ʿAlī/Muʿāwiya (fiqh des priorités : le tout sur la partie, la stabilité
  du pouvoir sur le talion ; deux récompenses/une récompense — l'ijmāʿ des
  gens de la Sunna) ; le Jamal par le même principe ; la clause anti-mondane
  (le conflit n'était pas pour ce bas monde) ; le silence des imams (Mālik)
  ; le verset comme lame de fond (l'excellence attestée par Dieu).
- OCR/artefacts : dl/dt/dd vides + <p> vides + écho du titre en queue + divs
  vides — artefacts non rendus ; « اُلنَّاسِ » voyelle superflue — corrigé.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : ce qu’il faut croire au sujet des Compagnons (qu’Allāh les agrée)</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingt-cinquième leçon (25).</p>
<ul>
<li>Connaître la station des Compagnons — que Dieu les agrée.</li>
<li>Avoir présent à l’esprit l’obligation de vénérer les Compagnons et de penser d’eux le meilleur.</li>
</ul>
<h2>Préambule</h2>
<p>La communauté de notre maître Muḥammad ﷺ est la meilleure des communautés, la plus excellente absolument ; et cette excellence varie d’une génération à l’autre, et d’une personne à l’autre : la meilleure des générations est la génération du Prophète ﷺ et de ses Compagnons, et les meilleurs des hommes de la communauté de Muḥammad ﷺ sont ses nobles Compagnons — et, à leur tête, les quatre califes.</p>
<p>Quelle est donc la station des Compagnons ? Et que nous est-il obligatoire envers eux ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et qu’il n’est fait mention d’aucun des Compagnons du Messager de Dieu ﷺ sinon en la plus belle des mentions ; le silence sur ce qui opposa des dissensions entre eux ; et qu’ils sont, des hommes, ceux qui méritent le plus qu’on leur cherche les plus belles issues, et qu’on suppose d’eux les plus belles voies. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>shajara</em> (opposa des dissensions) : advint, se produisit.</li>
<li><em>yultamas</em> (qu’on cherche) : qu’on demande, qu’on recherche.</li>
<li><em>yuẓann</em> (qu’on suppose) : qu’on tienne pour vrai.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>Je dégage du <em>matn</em> les convenances qu’il convient d’observer envers les Compagnons — que Dieu les agrée.</li>
<li>J’extrais du <em>matn</em> ce qu’il faut leur rechercher en ce qui advint entre eux — que Dieu les agrée.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon embrasse les axes suivants :</p>
<h3>Premièrement : l’observation des convenances envers les Compagnons — que Dieu les agrée</h3>
<h4>1. Les mentionner en la plus belle des mentions — que Dieu les agrée</h4>
<p>L’auteur — que Dieu Très-Haut lui faisse miséricorde — dit : « Et qu’il n’est fait mention d’aucun des Compagnons du Messager de Dieu ﷺ sinon en la plus belle des mentions. » Ce qu’il faut tenir pour vrai : la mention de l’ensemble des Compagnons en la plus belle des mentions est commandée — pour ce qu’elle comporte d’acquittement de l’ordre de les magnifier et de les aimer. Eux sont les croyants qui vécurent avec le Messager de Dieu ﷺ, crurent en lui, le fortifièrent et le soutinrent, répondirent à son appel de son vivant, et défendirent sa religion après sa mort ﷺ. Le Prophète ﷺ recommanda de les aimer et mit en garde contre le fait de leur nuire, disant : « Craignez Dieu, craignez Dieu au sujet de mes Compagnons : ne les prenez pas pour cible après moi. Quiconque les aime, c’est par amour de moi qu’il les aime ; quiconque les déteste, c’est par détestation de moi qu’il les déteste ; quiconque leur nuit m’a nui ; et quiconque me nuit a nui à Dieu ; et quiconque nuit à Dieu — Il est proche de le saisir. » [Ṣaḥīḥ d’Ibn Ḥibbān, bāb du mérite des Compagnons et des Suivants — que Dieu les agrée : référence imprimée conservée ; le hadith est également celui de Tirmidhī 3862, de ʿAbd Allāh b. Mughaffal.]</p>
<h4>2. L’obligation de les aimer — que Dieu les agrée</h4>
<p>L’amour des Compagnons — que Dieu les agrée — est obligatoire pour trois motifs :</p>
<ul>
<li>Premier : la beauté de leur caractère et de leurs actes, la grandeur de leur conseil à la Communauté, leur sollicitude pour la religion et la Loi, l’acquittement du dépôt, et l’établissement de la justice entre la Communauté par la droiture.</li>
<li>Second : la beauté de leur compagnie au Prophète de la miséricorde ﷺ, et la beauté de leur commerce avec lui en tout temps : lorsqu’il ﷺ faisait ses ablutions, ils s’empressaient vers son eau, au point d’en venir presque à se disputer ; il ne tombait de lui un cheveu qu’ils ne s’en empressassent ; lorsqu’il leur commandait une chose, ils s’empressaient d’exécuter son commandement ; lorsqu’il parlait, ils baisaient leurs voix auprès de lui, et ne fixaient pas sur lui leur regard, par vénération — au point que ʿUrwa b. Masʿūd dit : « Par Dieu, j’ai été en ambassade auprès des rois — auprès de César, de Chosroès et du Négus — ; par Dieu, je n’ai jamais vu un roi dont les compagnons magnifient [leur roi] comme magnifient leur Muḥammad les compagnons de Muḥammad. » [Al-Bayhaqī, <em>al-Sunan</em>, bāb de la trêve sur le regard — référence imprimée conservée.]</li>
<li>Troisième : l’amour que Dieu leur porte, la descente du Coran avec Son agrément d’eux, Son choix d’eux pour la compagnie de Son Prophète ﷺ — puis l’agrément qu’en eut le Prophète — prière et salut sur lui —, la salutaire prière qu’il fit pour eux, l’intensité de sa joie d’eux, et la grandeur de leur éloge. D’après Abū Hurayra — que Dieu l’agrée — : le Messager de Dieu ﷺ a dit : « Ne insultez pas mes Compagnons : par Celui qui tient mon âme en Sa main, si l’un de vous dépensait l’équivalent de [la montagne d’] Uḥud en or, il n’atteindrait pas le <em>mudd</em> de l’un d’eux, ni même sa moitié. » [Ṣaḥīḥ Muslim, Kitāb Faḍāʾil al-Ṣaḥāba, bāb de l’interdiction d’insulter les Compagnons — bāb imprimé EXACT (hadith 2540, d’Abū Hurayra) : texte VÉRIFIÉ sur sunnah.com ; « il n’atteindrait pas » (<em>mā balagha</em>) suit la leçon de l’imprimé (la narration 2540 porte <em>mā adraka</em> — variante canonique).]</li>
</ul>
<h3>Deuxièmement : l’obligation du silence sur ce qui opposa des dissensions entre eux</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « le silence sur ce qui opposa des dissensions entre eux ». Il est obligatoire de s’abstenir et de se taire sur les dissensions et les conflits advenus entre les Compagnons — que Dieu les agrée ; et il est obligatoire, à tout musulman, d’interpréter selon la plus belle interprétation ce qui fut transmis d’eux par voie authentique, parmi ce qui advint entre eux. Ainsi interprète-t-on ce qui advint entre ʿAlī et Muʿāwiya — que Dieu les agrée — : ʿAlī — que Dieu l’agrée — jugea, par son effort d’interprétation (<em>ijtihād</em>) et selon le fiqh des priorités, que la stabilité de l’ordre du commandement primait sur l’exécution du talion contre les assassins de ʿUthmān — que Dieu l’agrée —, donnant la priorité au général sur le particulier : l’ordre des hommes ne tient droit que par un imam ; et Muʿāwiya — que Dieu l’agrée — exigeait le talion contre les assassins de ʿUthmān — que Dieu l’agrée — avant la conclusion du serment d’allégeance à ʿAlī — que Dieu l’agrée. Ce qui devait advenir advint ; et les gens de la Sunna sont d’accord : ʿAlī fit un effort d’interprétation et atteignit le juste — il a deux récompenses ; et Muʿāwiya fit un effort d’interprétation et manqua le juste — il a une récompense — que Dieu les agrée tous deux.</p>
<p>Par le même principe s’interprète ce qui advint entre ʿAlī, al-Zubayr et Ṭalḥa en la journée du Chameau (<em>yawm al-Jamal</em>), en Irak. Aussi, lorsque les gens de Basra interrogèrent ʿAbd Allāh b. ʿUmar — que Dieu les agrée tous deux — sur l’affaire de ʿUthmān et sur l’affaire de ʿAlī, il répondit :</p>
<p>« … Dis : „Etes-vous plus savants, ou Dieu ?“… » (al-Baqara, 140)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — la réponse d’Ibn ʿUmar est le fragment « Etes-vous plus savants, ou Dieu ? » : Dieu Lui-même a attesté de l’excellence des Compagnons — nul n’a à enquêter sur eux.] Et il fut rapporté d’Abū Saʿīd al-Khudrī — que Dieu l’agrée — : « Les compagnons de Muḥammad sont comme l’œil ; et le remède de l’œil est de ne pas y toucher. » [<em>Sharḥ Zarrūq ʿalā l-Risāla</em>, 1/69 — référence imprimée conservée.]</p>
<h3>Troisièmement : leur chercher l’excuse et l’issue, et penser d’eux le meilleur</h3>
<h4>1. Leur chercher l’excuse</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et qu’ils sont, des hommes, ceux qui méritent le plus qu’on leur cherche les plus belles issues ». Les Compagnons sont, des hommes, ceux qui méritent le plus qu’on leur recherche les plus belles issues et les plus justes interprétations en ce qui advint entre eux ; et qu’on tienne pour vrai que cela ne fut point pour ce bas monde : leur dissension ne porta pas sur son commandement, l’obtention de ses parts et ses désirs — la religion était leur visée suprême, et ce qui advint entre eux fut de leur part effort d’interprétation (<em>ijtihād</em>).</p>
<h4>2. Penser d’eux le meilleur</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et qu’on suppose d’eux les plus belles voies ». Il est obligatoire au musulman de penser le meilleur des Compagnons du Messager de Dieu ﷺ. Les imams — parmi eux l’imam Mālik, que Dieu leur fasse miséricorde —, avec la force de leur science, l’enracinement de leur pied en la religion et la proximité de leur époque de celle des Compagnons, ne s’engageaient point en cela et n’en parlaient point : quiconque d’autre, dont l’œuvre est moindre, est plus en droit de s’y tenir. Le juste est donc de détourner [le regard] de ce qui advint entre les Compagnons, et de tenir pour vrai que tout ce qui advint entre eux fut effort d’interprétation, et que l’excellence est établie pour eux tous — selon sa parole ﷺ : « La meilleure partie de ma communauté est ma génération, puis ceux qui les suivent, puis ceux qui les suivent. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb Faḍāʾil al-Ṣaḥāba, bāb des mérites des Compagnons du Prophète ﷺ — bāb imprimé EXACT (hadith 3650, d’ʿImrān b. Ḥuṣayn) : texte VÉRIFIÉ sur sunnah.com ; l’imprimé cite la seule ouverture, sans la réserve d’ʿImrān.]</p>
<h2>Les fruits de la leçon</h2>
<p>Faire connaître la station des Compagnons et leur droit à l’estime et à l’amour : les aimer, c’est aimer le Messager de Dieu ﷺ ; purifier le cœur de la mauvaise supposition à leur sujet ; purifier la langue de tomber en eux — par le silence sur ce qui opposa des dissensions entre eux et sa mise sur le plus beau compte : et c’est là même la sagesse et l’équité.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Comment doit-on mentionner les Compagnons — que Dieu les agrée ?</li>
<li>Que signifie le silence sur ce qui opposa des dissensions entre eux ?</li>
<li>Comment peut-on chercher l’excuse des Compagnons — que Dieu les agrée — en ce qui advint entre eux ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Al-Ḥākim rapporte dans le <em>Mustadrak</em>, d’après Abū Jumʿa : « Je déjeunai avec le Prophète ﷺ — et avec lui se trouvait Abū ʿUbayda b. al-Jarrāḥ. Abū ʿUbayda lui dit : „ô Messager de Dieu, y a-t-il des hommes meilleurs que nous ? Nous avons embrassé l’islam avec toi, et combattu avec toi.“ Il dit : „Oui : un peuple qui sera après moi, qui croira en moi sans m’avoir vu.“ » [Le <em>Mustadrak</em> d’al-Ḥākim — bāb du mérite de la communauté après les Compagnons et les Suivants : référence imprimée conservée.]</p>
<h3>Je lis le hadith et en mets en relief :</h3>
<ul>
<li>les mérites des Compagnons — que Dieu les agrée ;</li>
<li>la station des croyants qui n’ont pas vu le Prophète ﷺ.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qui suit :</p>
<ul>
<li>Le statut de l’obéissance au détenteur de l’autorité.</li>
<li>La manière de traiter avec les disputeurs en religion.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16801":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16801 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16801 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
