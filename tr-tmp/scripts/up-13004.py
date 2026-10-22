#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13004 (hadith-1es, la vertu de la
prière en commun — Muwaṭṭaʾ n° 343/344/345/346/347/349/350 +
Tirmidhī + Aḥmad/Sunan/Ibn Khuzayma + Abū Dāwūd/Nasāʾī).

Conventions main (cf. 12875-13002 du même livre) :
- h1 « La vertu de la prière en commun (faḍl ṣalāt al-jamāʿa) »,
  27e leçon ; titleFr officiel conservé.
- Préambule : coopération en la piété, liens d'amour ; « tiens-toi
  au groupe : le loup ne mange de la brebis que l'écartée » (Abū
  Dāwūd/Nasāʾī d'Abū l-Dardāʾ).
- Hadiths : 343 (Nāfiʿ/Ibn ʿUmar : la prière du groupe excelle celle
  du solitaire de VINGT-SEPT degrés) ; 347 (ʿAbd al-Raḥmān b.
  Harmala/Saʿīd b. al-Musayyab, mursal : « entre nous et les
  hypocrites : l'assistance à la ʿishāʾ et au point du jour — ils
  n'en sont pas capables » ou approchant) ; 349 (Ibn Shihāb/Abū Bakr
  b. Sulaymān b. Abī Ḥathma : ʿUmar cherche Sulaymān au point du
  jour ; la mère al-Shifāʾ : « il a veillé en prière et ses yeux
  l'ont dominé » ; ʿUmar : « assister au point du jour en groupe
  m'est plus aimable que veiller une nuit entière »).
- Lexique : tafḍul, munāfiq, shuhūd al-ʿishāʾ, ghadā, ghalabathu
  ʿaynāhu.
- Taḥlīl I : sagesse — liens de fraternité + la mosquée espace
  d'éducation, de résolution des crises, de shūrā, d'étude du Coran
  et des sciences religieuses et mondaines.
- Taḥlīl II : 27 vs 25 (Tirmidhī : la plupart disent 25, Ibn ʿUmar
  27 ; Muwaṭṭaʾ 344 « vingt-cinq parts ») ; tarjīḥ disputé (nombreux
  rapporteurs vs addition du transmetteur sûr) ; égalité des groupes
  en nombre (le mérite dit sans intermédiaire — certains Mālikites)
  SANS nier le surcroît (Ubayy b. Kaʿb, Aḥmad+Sunan+Ibn Khuzayma :
  « la prière de l'homme avec l'homme est plus pure… et ce qui
  abonde est plus aimé de Dieu ») ; 346 (Zayd b. Thābit : la meilleure
  prière = celle de vos maisons, SAUF l'écrite).
- Taḥlīl III : le chapitre du Muwaṭṭaʾ « al-ʿatama et le point du
  jour » — le nom d'ʿatama pour la ʿishāʾ licite ; « entre nous et
  eux » = signe d'hypocrisie : ils n'assistent pas par obéissance ni
  en quête de récompense, l'assistance leur pèse ; Ibn ʿUmar : « si
  nous manquions un homme à ces deux prières, nous pensions du mal
  de lui » ; Shaddād b. Aws (ceux par qui Dieu détourne le châtiment
  des gens de la terre) ; 350 (ʿUthmān : assister à la ʿishāʾ = veiller
  une demi-nuit ; au point du jour = une nuit entière).
- Istimḥār : 345 (Abū Hurayra : « par Celui qui tient mon âme ! j'ai
  résolu d'ordonner qu'on ramassât du bois… puis d'ordonner la
  prière et l'appel… puis d'ordonner à un homme de guider les gens,
  puis de passer outre vers des hommes et brûler leurs maisons sur
  eux… s'il savait qu'il trouverait un os gras ou deux morceaux de
  conserve (mirmatayn) exquis, il assisterait à la ʿishāʾ ») + 2
  questions.
- Préparation préalable : leçon SUIVANTE 13005 (règles propres à
  l'imam et au maʾmūm ; sagesse de l'imam).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>La vertu de la prière en commun (<em>faḍl ṣalāt al-jamāʿa</em>)</h1>
<p>Leçon sur la vertu de la prière en commun, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-septième leçon.</p>
<ol>
<li>Connaître la vertu de la prière en commun.</li>
<li>Comprendre la sagesse de la législation de la prière en commun.</li>
<li>Persévérer en les prières devoir en la mosquée.</li>
</ol>
<h2>Préambule</h2>
<p>Le Prophète — paix et bénédiction sur lui — exhorta sa communauté à assister aux cinq prières avec le groupe, pour ce qu’il y a en cela de coopération en la piété et l’obéissance, et de consolidation des liens d’amour et de concorde. Et il mit sa communauté en garde contre l’isolement du groupe des musulmans, disant : « Tiens-toi au groupe : car le loup ne mange de la brebis que l’écartée. » [Rapporté par Abū Dāwūd et an-Nasāʾī, d’après Abū l-Dardāʾ]</p>
<p>Quelle est donc la vertu de la prière en commun ? Et la sagesse de sa législation ?</p>
<p>Et pourquoi l’Envoyé — paix et bénédiction sur lui — encouragea-t-il l’assistance à la prière du point du jour et à celle de la ʿishāʾ ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Nāfiʿ, d’après ʿAbd Allāh ibn ʿUmar : « que le Messager de Dieu — paix et bénédiction sur lui — dit : La prière du groupe excelle la prière du solitaire de vingt-sept degrés. » [Muwaṭṭaʾ, n° 343]</li>
<li>D’après Mālik, d’après ʿAbd al-Raḥmān ibn Harmala al-Aslamī, d’après Saʿīd ibn al-Musayyab : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Entre nous et les hypocrites : l’assistance à la ʿishāʾ et au point du jour — ils n’en sont pas capables — ou une parole approchante. » [Muwaṭṭaʾ, n° 347]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Abū Bakr ibn Sulaymān ibn Abī Ḥathma : « que ʿUmar ibn al-Khaṭṭāb manqua Sulaymān ibn Abī Ḥathma à la prière du point du jour, et que ʿUmar ibn al-Khaṭṭāb partit au matin au marché — la demeure de Sulaymān étant entre le marché et la mosquée prophétique — et passa auprès d’al-Shifāʾ, mère de Sulaymān, à qui il dit : Je n’ai point vu Sulaymān au point du jour. Elle dit : Il a passé la nuit à prier, et ses yeux l’ont dominé. ʿUmar dit : Que j’assiste à la prière du point du jour en groupe m’est plus aimable que de veiller une nuit entière. » [Muwaṭṭaʾ, n° 349]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>tafḍul</em> (« excelle ») : elle ajoute sur elle.</li>
<li><em>al-munāfiq</em> (« l’hypocrite ») : celui qui montre le contraire de ce qu’il recèle.</li>
<li><em>shuhūd al-ʿishāʾ</em> (« l’assistance à la ʿishāʾ ») : la présence à la ʿishāʾ.</li>
<li><em>ghadā ilā l-sūq</em> (« partit au matin au marché ») : il alla au matin.</li>
<li><em>ghalabathu ʿaynāhu</em> (« ses yeux l’ont dominé ») : le sommeil l’a domine, et il ne s’éveilla pas pour la prière du point du jour.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Explicite la sagesse de la législation de la prière en commun.</li>
<li>Par quoi la prière en commun excelle-t-elle celle du particulier ?</li>
<li>Pourquoi l’Envoyé — paix et bénédiction sur lui — tint-il le retard au point du jour et à la ʿishāʾ pour une marque d’hypocrisie ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la sagesse de la législation de la prière en commun</h3>
<p>Le Prophète — paix et bénédiction sur lui — encouragea sa communauté à persévérer en les cinq prières et à y assister avec le groupe des musulmans, pour ce qu’il y a en cela de consolidation des liens d’amour et de fraternité entre eux — en outre que la mosquée où se rassemblent les musulmans est un espace d’éducation et d’instruction, de résolution des crises et des contestations, de conduite des affaires par l’avis et les consultations, et d’étude du Coran et des sciences et connaissances religieuses et mondaines qui s’y rattachent.</p>
<h3>Deuxièmement : la vertu de la prière en commun sur celle du solitaire</h3>
<p>Le Prophète — paix et bénédiction sur lui — exposa, au premier hadith, la vertu de la prière en commun sur celle du particulier : « La prière du groupe excelle la prière du solitaire de vingt-sept degrés. » [Muwaṭṭaʾ, n° 343] At-Tirmidhī dit : “La plupart de qui le transmit dirent : vingt-cinq — sauf Ibn ʿUmar, qui dit : vingt-sept.” Et l’imam Mālik apporta la narration des vingt-cinq, en la teneur : « La prière du groupe est meilleure que la prière de quiconque de vous seul, de vingt-cinq parts. » [Muwaṭṭaʾ, n° 344]</p>
<p>On divergea sur laquelle des deux est la plus ferme : il fut dit les vingt-cinq, vu le nombre de leurs transmetteurs ; et il fut dit les vingt-sept, parce qu’il y a en elles l’addition d’un [transmetteur] sûr et rétenthif.</p>
<p>Le hadith du chapitre indique l’égalité des groupes en la vertu, qu’ils accroissent ou diminuent : car il mentionna la vertu du groupe sur le solitaire sans intermédiaire — tout groupe y entre donc : c’est la parole de certains Mālikites. Mais il ne nie pas le surcroît de vertu à ce qui fut plus nombreux, surtout avec l’existence du texte l’explicitant — ce que rapportèrent Aḥmad en son <em>Musnad</em>, les auteurs des <em>Sunan</em>, et qu’Ibn Khuzayma valida en son <em>Ṣaḥīḥ</em> et d’autres, d’après Ubayy ibn Kaʿb, remontant [au Prophète] : “La prière de l’homme avec l’homme est plus pure que sa prière seule ; et sa prière avec deux hommes plus pure que sa prière avec l’homme ; et ce qui abonde est plus aimé de Dieu.”</p>
<p>Et de ce qui indique la vertu de la prière en commun : ce qu’apporta Mālik par sa chaîne jusqu’à Zayd ibn Thābit : « qu’il dit : La meilleure des prières est votre prière en vos maisons — sauf la prière écrite. » [Muwaṭṭaʾ, n° 346]</p>
<h3>Troisièmement : l’encouragement à assister à la prière de la ʿishāʾ et du point du jour avec le groupe</h3>
<p>L’imam Mālik intitula ce chapitre : ce qui vint sur l’<em>ʿatama</em> et le point du jour — et apporta un hadith interrompu (<em>mursal</em>), de Saʿīd ibn al-Musayyab : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Entre nous et les hypocrites : l’assistance à la ʿishāʾ et au point du jour — ils n’en sont pas capables, ou approchant. » Et la venue du nom d’<em>ʿatama</em> en ce chapitre indique la permission de nommer la ʿishāʾ “l’ʿatama”.</p>
<p>Le sens de sa parole au hadith : “entre nous et les hypocrites” — c’est-à-dire : entre nous et eux, un signe et une marque d’hypocrisie : l’assistance à la ʿishāʾ et au point du jour avec le groupe. Le sens : qu’ils n’y assistent pas par acquiescement à l’ordre ni en quête de la récompense — l’assistance leur pèse en leur temps, et ils s’en abstiennent. Ibn ʿUmar disait : “Quand nous manquions l’homme à ces deux prières, nous pensions du mal de lui.”</p>
<p>Et Shaddād ibn Aws dit : “Quiconque aime que Dieu le fasse des gens par lesquels Dieu détourne le châtiment des gens de la terre — qu’il garde la prière de la ʿishāʾ et la prière du point du jour en groupe.”</p>
<p>Et de ce qui indique la vertu de la prière du point du jour avec le groupe : ce que rapporta l’imam Mālik, par sa chaîne, d’après ʿUthmān ibn ʿAffān : « qu’il dit : Quiconque assiste à la ʿishāʾ, c’est comme s’il avait veillé une demi-nuit ; et quiconque assiste au point du jour, c’est comme s’il avait veillé la nuit entière. » [Muwaṭṭaʾ, n° 350]</p>
<h2>L’évaluation</h2>
<ol>
<li>Quelle est la sagesse de la législation de la prière en commun ?</li>
<li>Mets en relief la divergence survenue en la gradation de la récompense du groupe.</li>
<li>Explicite la vertu de chacune des deux : la prière de la ʿishāʾ et la prière du point du jour, en groupe.</li>
</ol>
<h2>L’exploitation</h2>
<p>Mālik, d’après Abū l-Zinad, d’après al-Aʿraj, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Par Celui qui tient mon âme en Sa main ! j’ai résolu d’ordonner qu’on ramassât du bois, puis d’ordonner la prière et qu’on fit l’appel pour elle, puis d’ordonner à un homme de guider les gens — puis de passer outre vers des hommes et de brûler leurs maisons sur eux. Par Celui qui tient mon âme en Sa main ! si l’un d’eux savait qu’il trouverait un os gras, ou deux <em>mirmatayn</em> exquises, il assisterait à la ʿishāʾ. » [Muwaṭṭaʾ, n° 345]</p>
<ol>
<li>Qu’est-ce que l’Envoyé — paix et bénédiction sur lui — résolut de faire ? Et pourquoi ?</li>
<li>Extrais du hadith ce qui indique la mise en garde contre le délaissement de la ʿishāʾ en groupe.</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la prochaine leçon et réponds à ce qui suit :</p>
<ol>
<li>Extrais les règles propres à l’imam et au suivi.</li>
<li>Explicite la sagesse de ce que les musulmans prennent un imam en les prières obligatoires et certaines prières sunniques.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13004":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13004 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13004 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
