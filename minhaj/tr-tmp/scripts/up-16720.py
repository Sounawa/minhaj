#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16720 (tawhid-1es, leçon 8 — la pré-éternité
de Ses attributs et Son adresse à Mūsā).

RESTITUTION post-rollback : traduction savante intégralement vérifiée livrée
à l'origine après le tour R127 (perdue du disque par restauration sandbox à
R81 — présente dans le GitHub distant, inaccessible sans token). Le texte
est restitué à l'identique depuis la mémoire de session.

Vérifications et restitutions d'origine (cache quran = Ḥafṣ) :
- Matn : « لم يزل بجميع صفاته وأسمائه... ولا صفة لمخلوق فينفد » — rendu
  fidèlement.
- [النساء: 163] (citation vide, perte OCR) → Nisāʾ 164 « وكلم الله موسى
  تكليما » — réf d'adjacence (−1) notée : le masdar taklīman, analysé par
  le paragraphe suivant, s'y trouve — cible univoque.
- [الأعراف: 143] ×2 (citations vides) → 7:143 CONFORME, rendu deux fois
  (l'imprimé cite le verset deux fois : manifestation + demande de la vue).
- [الحشر: 21-22-23] (citation vide) → Ḥashr 21-23 CONFORMES, restituées.
- Doublons OCR détangles : paragraphe de l'ijmāʿ sur la modalité imprimé 2× ;
  queue de phrase « من جلاله... » soudée 2× ; item d'évaluation imprimé 2× ;
  titre h4 « تجليه سبحانه للجبل » dupliqué en soudure — rendus UNE fois.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : l’éternité de Ses attributs et Son adresse à Mūsā (sur lui la paix)</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la huitième leçon (8).</p>
<ul>
<li>Connaître que les attributs de Dieu et Ses noms sont pré-éternels et anciens.</li>
<li>Distinguer les attributs pré-éternels du Créateur des attributs advenus de la créature.</li>
</ul>
<h2>Préambule</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — ayant mentionné aux leçons précédentes une part de ce qu’il faut croire au sujet de Dieu Très-Haut : transcendance et sanctification, ainsi que les attributs les plus hauts et les noms les plus beaux qui Lui appartiennent — voulut avertir que Ses attributs, l’Elevé, sont anciens et pré-éternels, non advenus, niant d’eux le fait d’être créés ou survenus.</p>
<p>Qu’entend-on par la pré-éternité des attributs de Dieu et de Ses noms ? Et que signifie que le Coran est une parole subsistant en Son essence ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Il n’a point cessé d’être pourvu de la totalité de Ses attributs et de Ses noms — transcendant qu’Il soit que Ses attributs soient créés et Ses noms advenus. Il parla à Mūsā de Sa parole, qui est un attribut de Son essence, non une créature parmi Ses créatures ; et Il Se manifesta au mont, qui s’aplatit sous Sa majesté. Et [il faut croire] que le Coran est la parole de Dieu subsistant en Son essence : non créé — il périrait ; ni attribut d’une créature — il s’épuiserait. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>lam yazal</em> (Il n’a point cessé) : négation de la négation — ce qui est affirmation de permanence et de continuité.</li>
<li><em>dakkān</em> (aplati) : nivelé avec la terre, réduit en poussière.</li>
<li><em>yabīd</em> (il périrait) : être anéanti, s’en aller, être anéanti.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> que les attributs de Dieu Très-Haut et Ses noms ne sont pas créés ni advenus.</li>
<li>J’extrais du <em>matn</em> ce dont Dieu distingua Mūsā (sur lui la paix).</li>
<li>J’extrais du <em>matn</em> ce qui indique la majesté de Dieu et Sa grandeur.</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient ce qui suit :</p>
<h3>Premièrement : la pré-éternité de Ses attributs, l’Elevé, et leur permanence</h3>
<p>L’auteur dit : « Il n’a point cessé d’être pourvu de la totalité de Ses attributs et de Ses noms. » Au nombre de ce qu’il faut croire : qu’à Dieu Très-Haut appartiennent des noms les plus beaux et des attributs les plus hauts, et qu’Il Se nomma Lui-même de Ses noms les plus beaux et Se décrivit de Ses attributs les plus hauts dans la pré-éternité (<em>azal</em>) — de sorte qu’Il n’a point cessé d’être nommé de Ses noms et doté de Ses attributs. Tel est le <em>madhhab</em> des gens de la Sunna, parmi lesquels les Ashʿarites — que Dieu leur fasse miséricorde. L’auteur voulut ici attirer l’attention sur l’obligation d’affirmer la pré-éternité de Ses noms et de Ses attributs, comme l’on doit affirmer la pré-éternité de Son essence — ce qui entraîne l’obligation de Sa permanence : l’attribut de pré-éternité signifie qu’Il est le Pré-éternel par Son essence, Ses noms et Ses attributs, celui dont l’existence n’a point de commencement ; et l’attribut de permanence signifie qu’Il est le Permanent par Son essence, Ses noms et Ses attributs, celui dont l’existence et sa permanence n’ont point de fin. Tous deux sont au nombre des attributs de négation (<em>ṣifāt al-salb</em>), qui nient et ôtent de Dieu ce qui ne Lui sied pas : l’avènement (<em>ḥudūth</em>).</p>
<p>L’auteur dit : « transcendant qu’Il soit que Ses attributs soient créés et Ses noms advenus. » Au nombre de ce qu’il faut croire : Sa transcendance au point que Ses attributs soient créés et Ses noms advenus. Bien plutôt, Ses noms et Ses attributs sont anciens, en raison de l’impossibilité que les contingents (<em>ḥawādith</em>) subsistent en Lui : ils sont établis dans la pré-éternité par Sa parole pré-éternelle, et ne sauraient donc être advenus.</p>
<h3>Deuxièmement : l’adresse de Dieu à Mūsā (sur lui la paix) et Sa manifestation au mont</h3>
<h4>1. L’adresse de Dieu à Mūsā (sur lui la paix)</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Il parla à Mūsā de Sa parole, qui est un attribut de Son essence. » Au nombre de ce qu’il faut croire : que Dieu Très-Haut parla à Mūsā — sur lui la paix — de Sa parole pré-éternelle, qui est un attribut de Son essence, c’est-à-dire un trait de Ses traits : Il créa pour lui, en son cœur, une intelligence par laquelle il saisissait, et en ses oreilles une ouïe par laquelle il entendait une parole qui n’est ni son ni lettre — entendue de toute direction et par tout organe. Et la vision ne Lui advint pas, selon la majorité. Mūsā — sur lui la paix — fut distingué par le nom d’<em>al-Kalīm</em> (l’Interlocuteur) parce que son adresse eut lieu sans l’intermédiaire du Livre ni de l’ange.</p>
<p>La parole de l’auteur : « non une créature parmi Ses créatures » signifie que Mūsā ne fut point adressé par une créature : c’est Dieu qui lui parla. Le Très-Haut dit :</p>
<p>« Des messagers dont Nous t’avons narré l’histoire auparavant, et des messagers dont Nous ne t’avons point narré l’histoire — et Dieu parla à Mūsā en propre (<em>taklīman</em>). » (al-Nisāʾ, 164)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 163 », la visée est le verset 164 — le <em>masdar</em> « <em>taklīman</em> », dont le paragraphe suivant analyse le renforcement, s’y trouve ; réf d’adjacence notée.]</p>
<p>Le verbe fut renforcé par le <em>masdar</em> pour écarter la métaphore : l’adresse de Dieu Très-Haut à Mūsā — sur lui la paix — est réalité (<em>ḥaqīqa</em>). La communauté fut unanime sur le fait que Dieu Très-Haut parla à Mūsā ; elle divergea sur la modalité : les prédécesseurs (<em>salaf</em>) dirent : « Nous croyons à la parole, et ne nous exposons pas à la modalité », car elle relève de l’équivoque (<em>mutashābih</em>), que Dieu seul connaît.</p>
<p>[Paragraph imprimé deux fois par l’OCR — duplication rendue une seule fois.]</p>
<h4>2. Sa manifestation — glorifié soit-Il — au mont</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et Il Se manifesta au mont, qui s’aplatit sous Sa majesté. » C’est au nombre de ce dont le noble Coran fit mention. Le Très-Haut dit :</p>
<p>« Et lorsque Mūsā vint à Notre rendez-vous et que son Seigneur lui eut parlé, il dit : " Seigneur, montre-Toi à moi, que je Te voie ! " Il dit : " Tu ne Me verras point ; mais regarde le mont : s’il tient en sa place, tu Me verras. " Et lorsque son Seigneur Se manifesta au mont, Il le pulvérisa (<em>jaʿalahu dakkān</em>), et Mūsā s’effondra foudroyé. Lorsqu’il eut repris ses sens, il dit : " Gloire à Toi ! C’est vers Toi que je me repens ; et je suis le premier des croyants. " » (al-Aʿrāf, 143)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Et cette manifestation vint après la demande de Mūsā — sur lui la paix — de voir son Seigneur ; le Très-Haut dit :</p>
<p>« Et lorsque Mūsā vint à Notre rendez-vous et que son Seigneur lui eut parlé, il dit : " Seigneur, montre-Toi à moi, que je Te voie ! " Il dit : " Tu ne Me verras point ; mais regarde le mont : s’il tient en sa place, tu Me verras. " Et lorsque son Seigneur Se manifesta au mont, Il le pulvérisa, et Mūsā s’effondra foudroyé. Lorsqu’il eut repris ses sens, il dit : " Gloire à Toi ! C’est vers Toi que je me repens ; et je suis le premier des croyants. " » (al-Aʿrāf, 143)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME. Le verset est cité une seconde fois par l’imprimé — rendu tel quel.]</p>
<p>Et ce, dans l’espoir que Dieu le favoriserait de la vision comme Il l’avait favorisé de la parole : car il s’obtient par la vue de l’œil une félicité que la parole n’obtient point.</p>
<p>Sa parole : « et Il Se manifesta » (<em>wa-tajallā</em>) : Il apparut de Sa lumière, sans qualification (<em>takyīf</em>) ni comparaison (<em>tashbīh</em>). Ce mont est le Ṭūr Sīnāʾ — celui qui est mentionné aussi dans Sūrat al-Tīn. Et Sa parole : « qui s’aplatit (<em>dakkān</em>) sous Sa majesté » : le mont devint nivelé avec la terre, sous la majesté de Dieu Très-Haut, Son élévation, Sa hauteur, Sa toute-puissance et Sa grandeur.</p>
<p>[Queue de phrase imprimée deux fois en soudure par l’OCR — duplication rendue une seule fois.]</p>
<h3>Troisièmement : le Coran, parole de Dieu incréée, et qui n’est point un attribut d’une créature</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et [il faut croire] que le Coran est la parole de Dieu subsistant en Son essence : non créé — il périrait ; ni attribut d’une créature — il s’épuiserait. » Le Coran désigne, chez les spécialistes des fondements du droit (<em>uṣūl al-fiqh</em>), l’énoncé (<em>lafẓ</em>) fait descendre sur le Prophète Muḥammad ﷺ en vue du défi par une sourate de lui, dont la récitation est culte ; et, chez les savants des fondements de la religion (<em>uṣūl al-dīn</em>), le sens subsistant en Son essence — l’Elevé — transcendant la lettre et le son. En ce dernier sens, il est ancien, non créé : tel est le <em>madhhab</em> des gens de la Sunna. Car s’il était créé, il périrait et s’anéantirait comme périssent les substances (<em>jawāhir</em>), et s’épuiserait comme s’épuisent les accidents (<em>aʿrāḍ</em>) — voilà pourquoi il est interdit de proférer que le Coran est créé.</p>
<h2>Les fruits de la leçon</h2>
<ul>
<li>Éduquer le croyant à la foi en les réalités équivoques (<em>mutashābihāt</em>) venues de Dieu, à leur soumission, et à la remise de leur sens et de leur modalité à la volonté et à la science de Dieu, glorifié et magnifié soit-Il — c’est la croyance sur laquelle furent les pieux prédécesseurs ; ou bien leur interprétation en ce qui Lui sied — puissant et elevé soit-Il — selon les règles de l’interprétation correcte chez les savants : c’est la croyance des successeurs (<em>khalaf</em>) parmi les Ashʿarites.</li>
<li>Tirer la leçon et l’admonition de la majesté de Dieu et de Sa grandeur — et de la crainte des monts devant Sa majesté —, s’attacher à Ses noms et attributs et Le demander par eux, en reconnaissance de Sa seigneurie et de Sa divinité, et en aveu de la faiblesse et de l’absence de puissance et de force.</li>
</ul>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’expose que les noms de Dieu et Ses attributs sont pré-éternels et anciens, avec justification et appui sur le <em>matn</em> de la Risāla. [Item imprimé deux fois — rendu une fois.]</li>
<li>J’analyse la parole de l’auteur : « Il parla à Mūsā de Sa parole, qui est un attribut de Son essence ».</li>
<li>Je fais connaître le Coran, et j’appuie de versets coraniques qu’il n’est pas créé.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Dieu Très-Haut dit :</p>
<p>« Si Nous avions fait descendre ce Coran sur une montagne, tu l’aurais vu s’humilier et se fendre par crainte de Dieu. Et ces paraboles, Nous les citons aux gens — peut-être réfléchiront-ils. » (al-Ḥashr, 21)</p>
<p>« C’est Lui, Dieu : il n’est de divinité que Lui — le Connaisseur de l’invisible et du visible. C’est Lui, le Miséricordieux, le Très Miséricordieux. » (al-Ḥashr, 22)</p>
<p>« C’est Lui, Dieu : il n’est de divinité que Lui — le Roi, le Pur, la Paix, le Sécurisant, le Vigilant, le Puissant, le Contraignant, le Superbe. Gloire à Dieu, au-dessus de ce qu’ils associent ! » (al-Ḥashr, 23)</p>
<p>[Trois citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.]</p>
<h3>Je contemple le texte et réalise ce qui suit :</h3>
<ul>
<li>J’extrais des versets les noms les plus beaux qu’ils contiennent, en mettant en relief leurs sens.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche :</p>
<ul>
<li>les piliers de la foi.</li>
<li>le sens de la foi au décret et à la prédestination.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16720":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16720 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16720 restaurée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
