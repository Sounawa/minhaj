#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12889 (hadith-1es, les règles du sang de
l'épistaxis et de la blessure — Muwaṭṭaʾ n° 90-96).

Conventions main (cf. 12875, 12884, 12885 du même livre) :
- h1 « Les règles du sang de l'épistaxis et de la blessure (aḥkām damm
  al-ruʿāf wa-l-jarḥ) », 6e leçon, 1re année secondaire traditionnel.
- Sections : Préambule / Les hadiths / Explication lexicale / Extraction des
  contenus / L'analyse (Premièrement/Deuxièmement/Troisièmement) / L'évaluation
  / L'exploitation / La préparation préalable.
- Muwaṭṭaʾ 90 (Ibn ʿUmar), 91 (Ibn ʿAbbās), 92 (Saʿīd ibn al-Musayyab —
  ḥujra d'Umm Salama), 93 (Ibn Harmala), 94 (Sālim — ʿAbd al-Raḥmān ibn
  al-Mujabbar), 95 (ʿUmar poignardé — « nulle part en l'islam pour qui
  délaisse la prière », il pria la blessure jaillissante), 96 (īmāʾ de
  celui que le sang maîtrise) : chaînes et textes intégraux.
- Structure « deux figures » du manuel : le commentaire d'al-Zarqānī (2e
  item imprimé de l'ol) est rendu comme paragraphe entre les deux figures —
  fidélité pédagogique sans perte de contenu.
- Compagnons (ʿUmar, Ibn ʿUmar, Ibn ʿAbbās, al-Miswar) : « que Dieu soit
  satisfait de lui/eux » (raḍiya) ; Ibn al-Musayyab, Sālim, al-Zarqānī,
  Ibn Abī Zayd : pas de formule (raḥima implicite pour les savants).
- Lexique : fa-tawaḍḍaʾa = ablution LEXICALE (purification du khabath, non
  de l'état ḥadath) ; yathʿab = couler et jaillir ; fatl = tordre/essuyer
  avec les bouts des doigts ; takhḍab = être teint (les doigts du sang) ;
  awḥāl = fange.
- Préparation préalable : questions de la leçon SUIVANTE 12897 (madhī,
  baiser/toucher).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les règles du sang de l’épistaxis et de la blessure (<em>aḥkām damm al-ruʿāf wa-l-jarḥ</em>)</h1>
<p>Leçon sur les règles du sang de l’épistaxis et de la blessure, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la sixième leçon.</p>
<ul>
<li>Connaître le statut de l’épistaxis pendant la prière.</li>
<li>Saisir l’agir obligatoire en cas d’épistaxis pendant la prière.</li>
<li>Comprendre le statut de celui que le sang d’une blessure ou d’un épistaxis a maîtrisé.</li>
</ul>
<h2>Préambule</h2>
<P>Parmi les règles en relation avec la pureté — en ses deux espèces — figure le statut de l’épistaxis pendant la prière ou en dehors d’elle. L’imam Mālik a produit des rapports (<em>āthār</em>) sur le sujet, pour exposer les règles de l’épistaxis et de la blessure survenant pendant les ablutions ou la prière, ainsi que les règles du sang issu d’une blessure.</P>
<p>Quelles sont les règles de l’épistaxis ? Et que faire du sang d’une blessure ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Nāfiʿ : « ʿAbd Allāh ibn ʿUmar — que Dieu soit satisfait d’eux deux —, quand il avait un épistaxis, se retirait, faisait ses ablutions, puis revenait et reprenait [sa prière] — sans parler. » [Muwaṭṭaʾ, n° 90]</li>
<li>D’après Mālik : « qu’il lui fut rapporté que ʿAbd Allāh ibn ʿAbbās — que Dieu soit satisfait d’eux deux — avait des épistaxis : il sortait, lavait le sang de lui, puis revenait et reprenait sur ce qu’il avait déjà prié. » [Muwaṭṭaʾ, n° 91]</li>
<li>D’après Mālik, d’après Yazīd ibn ʿAbd Allāh ibn Qusayṭ al-Laythī : « qu’il vit Saʿīd ibn al-Musayyab avoir un épistaxis alors qu’il priait : il se rendit à la chambre (<em>ḥujra</em>) d’Umm Salama — l’épouse du Prophète — paix et bénédiction sur lui — ; on lui apporta de l’eau, il fit ses ablutions, puis revint et reprit sur ce qu’il avait déjà prié. » [Muwaṭṭaʾ, n° 92]</li>
<li>D’après Mālik, d’après Hishām ibn ʿUrwa, d’après son père : « qu’al-Miswar ibn Makhrama — que Dieu soit satisfait de lui — lui rapporta : il entra auprès de ʿUmar ibn al-Khaṭṭāb — que Dieu soit satisfait de lui — la nuit où il fut poignardé, et réveilla ʿUmar pour la prière de l’aube. ʿUmar dit : “Oui — et nulle part en l’islam pour qui délaisse la prière.” Et ʿUmar pria, tandis que sa blessure jaillissait de sang. » [Muwaṭṭaʾ, n° 95]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>il fit ses ablutions</em> (<em>fa-tawaḍḍaʾa</em>) : c’est-à-dire lava le sang — ablution lexicale, au sens de la purification de l’impureté (<em>khabath</em>), non au sens de la purification de l’état (<em>ḥadath</em>).</li>
<li><em>jaillit</em> (<em>yathʿab</em>) : coule et sourd abondamment, de sang.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Expose les règles de celui qui a un épistaxis pendant la prière.</li>
<li>L’épistaxis annule-t-il les ablutions ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de celui qui a un épistaxis pendant la prière</h3>
<p>Si l’orant a un épistaxis pendant sa prière, l’affaire revêt deux figures :</p>
<ul>
<li>que le sang soit abondant : il tord le sang (<em>fatl</em>) — c’est-à-dire l’essuie avec les bouts de ses doigts ; et si le sang ne cesse pas, il sort pour le laver et reprend sur ce qu’il a prié de sa prière — ce que contient le rapport de ʿAbd Allāh ibn ʿUmar — que Dieu soit satisfait d’eux deux — : « quand il avait un épistaxis, il se retirait, faisait ses ablutions, puis revenait et reprenait, sans parler ».</li>
</ul>
<p>Al-Zarqānī a dit : « Cet agir de ceux-là enseigne que l’épistaxis n’annule pas les ablutions, et que s’il sort pour le laver sans parler et sans dépasser l’endroit le plus proche, il reprend sur ce qu’il a prié — et la question a ses conditions dans les dérivés (<em>furūʿ</em>). »</p>
<ul>
<li>que le sang soit léger — au point que la pointe de ses doigts suffise à l’essuyer, ou un petit mouchoir tiré de sa poche : s’il l’essuie et qu’il cesse, il achève sa prière, et rien ne lui incombe.</li>
</ul>
<h3>Deuxièmement : le statut des ablutions de l’épistaxique avant la prière</h3>
<p>L’épistaxis n’annule pas les ablutions selon l’imam Mālik. Et c’est pour l’établir par preuve que l’imam Mālik a produit les deux rapports de ʿAbd Allāh ibn ʿUmar et d’Ibn ʿAbbās — que Dieu soit satisfait d’eux deux —, tous deux parmi les jeunes Compagnons : ils se contentaient de laver le sang. De même, ce qu’il transmit d’Ibn al-Musayyab — qui est des Suivants (<em>tābiʿūn</em>) — confirme que l’épistaxis n’annule pas les ablutions. Tout cela atteste l’établissement de la règle et la continuité de sa mise en œuvre — en riposte aux ḥanafites, qui tiennent que l’épistaxis annule les ablutions.</p>
<p>Et ce qui le confirme encore est ce qui fut transmis de certains des sept juristes [de Médine] — dont Saʿīd ibn al-Musayyab : Mālik rapporta, d’après ʿAbd al-Raḥmān ibn Harmala al-Aslamī : « qu’il dit : Je vis Saʿīd ibn al-Musayyab avoir un épistaxis, le sang sortant de lui jusqu’à ce que ses doigts en fussent teints (<em>takhḍab</em>) du sang qui sortait de son nez — puis il priait, sans faire les ablutions. » [Muwaṭṭaʾ, n° 93]</p>
<p>Et parmi eux : Sālim ibn ʿAbd Allāh — Mālik rapporta, d’après ʿAbd al-Raḥmān ibn al-Mujabbar : « qu’il vit Sālim ibn ʿAbd Allāh, le sang sortant de son nez jusqu’à ce que ses doigts en fussent teints ; il le tordait [de ses doigts], puis priait sans faire les ablutions » [Muwaṭṭaʾ, n° 94] — c’est-à-dire : sans faire les ablutions de la purification de l’état.</p>
<h3>Troisièmement : le statut de celui que le sang a maîtrisé — d’une blessure ou d’un épistaxis</h3>
<p>Celui que le sang d’une blessure a maîtrisé, et qui voit qu’il continuera sans cesser jusqu’à la sortie du temps de la prière : qu’il prie en l’état — et ne fait pas sortir la prière de son temps —, à preuve le rapport de ʿUmar — que Dieu soit satisfait de lui — que l’imam Mālik transmit : « …il pria, tandis que sa blessure jaillissait de sang ».</p>
<p>De même, celui que le sang de l’épistaxis a maîtrisé, et qui sait qu’il ne cessera pas : qu’il fasse signe (<em>īmāʾ</em>) dans sa prière, comme fait signe celui qui est au milieu de la boue et de la fange (<em>awḥāl</em>). L’atteste ce que rapporta Mālik, d’après Yaḥyā ibn Saʿīd : « Saʿīd ibn al-Musayyab dit : Que dites-vous de celui que le sang d’un épistaxis a maîtrisé, sans cesser ? Yaḥyā ibn Saʿīd dit : puis Saʿīd ibn al-Musayyab dit : J’estime qu’il fasse signe de sa tête, d’un signement. Yaḥyā dit : Mālik dit : c’est ce que j’ai le plus aimé entendre en la matière. » [Muwaṭṭaʾ, n° 96]</p>
<h2>L’évaluation</h2>
<ol>
<li>L’épistaxis annule-t-il les ablutions ? Appuie ta réponse d’une preuve.</li>
<li>Expose ce qui incombe à celui qui a un épistaxis pendant la prière.</li>
<li>Tire [du corpus] le statut de celui que le sang d’une blessure ou d’un épistaxis a maîtrisé pendant la prière.</li>
</ol>
<h2>L’exploitation</h2>
<p>Ibn Abī Zayd al-Qayrawānī a dit dans sa <em>Risāla</em> : « Celui qui a un épistaxis derrière l’imam : qu’il sorte et lave le sang, puis reprenne [sa prière] — tant qu’il n’a pas parlé ou marché sur une impureté ; et qu’il ne reprenne pas sur une <em>rakʿa</em> non achevée de ses deux prosternations : qu’il la laisse [de côté] ; qu’il ne se retire pas pour un sang léger : qu’il le tord [de ses doigts] — sauf s’il coule ou goutte. » [<em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī, p. 43]</p>
<p>Tire du texte les situations de l’épistaxis qu’il contient et leurs règles.</p>
<h2>La préparation préalable</h2>
<ol>
<li>Quelles sont les règles du <em>madhī</em> (liquide pré-éjaculatoire) ?</li>
<li>Quels sont les critères d’annulation des ablutions par le baiser et le toucher ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12889":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12889 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12889 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
