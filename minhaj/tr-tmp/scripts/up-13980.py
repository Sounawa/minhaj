#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13980 (tawhid-1es, « Présentation du
manuel » — page de titre du livre : hamdala, présentation, sommaire des
26 leçons + 2 annexes, compétences).

Conventions main (pattern des intros 13014 hadith-1es / 14101 fiqh-6ep /
14604 tafsir-6ep) :
- h1 = titre du livre tel que imprimé ; hamdala d'ouverture rendue intégralement.
- Sommaire : items imprimés SANS le préfixe « التوحيد : » (le manuel l'omet
  dans la table) — titres harmonisés sur les titleFr officiels des 29 leçons
  du livre (préfixe retiré) ; les 2 annexes en clair.
- Compétences : 4 items à l'infinitif (convention 14101/14604).
- « الإثنين 13 أكتوير 2025 » = tampon de date du site CMS — NON rendu
  (convention corpus : « le tampon de date du site non rendu »).
- Coquille imprimée « صلى الله عيه وسلم » (pour عليه) — rendue normalement.
- FIX GT-ismes : « d'entrer » → « d'accéder » ; « le Fiqh Akbar » → « le
  Grand Droit (al-fiqh al-akbar) » ; « enseignement préparatoire ancien » →
  « enseignement secondaire traditionnel (taʿlīm ʿatīq) » (GT-isme récurrent
  depuis 12875) ; « l'école de la Sunna et de la communauté » → « gens de la
  Sunna et du Consensus (ahl al-sunna wa-l-jamāʿa) ».
- Injection : leçon (d['lessons'], hit==1 — 13980 est une leçon du JSON,
  l'intro éditoriale « muqaddima » est un emplacement distinct traité à part).
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd, tiré de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan — première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>)</h1>
<p>Louange à Dieu, l’Un, l’Unique (<em>al-wāḥid al-aḥad</em>), seul en Sa seigneurie et seul digne d’adoration ; prière et salut entiers et durables sur notre maître Muḥammad, fils de ʿAbd Allāh, le Prophète digne de foi, le meilleur de ceux qui connurent Dieu de la vraie connaissance et réalisèrent la sincérité (<em>ikhlāṣ</em>), en parole et en acte, ainsi que sur sa famille et l’ensemble de ses compagnons.</p>
<p>Nous mettons entre vos mains le « Livre du Tawḥīd, tiré de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, pour la première année de l’enseignement secondaire traditionnel » : c’est un auxiliaire éducatif en une matière scientifique qui compte parmi les plus importantes des matières religieuses, et aux horizons de laquelle vous êtes tenus d’accéder peu à peu, jusqu’à ce que s’achève en vous la connaissance nécessaire de ses principes, et que vous savouriez ses implications et ses significations.</p>
<p>L’importance de cette matière apparaît en ceci que son objet est la première obligation de tout redevable (<em>mukallaf</em>) : connaître Dieu, Puissant et Élevé, et croire en Lui comme dieu un, unique, singulier (<em>fardan ṣamad</em>), Seigneur des mondes et Créateur de l’ensemble des cosmos ; et ce qui s’ensuit de la foi aux anges, aux prophètes et aux envoyés, et au monde de l’invisible — ce qui est connu des juristes de cette science sous les noms de : théologie (<em>ilāhiyyāt</em>), prophétologie (<em>nubuwwāt</em>) et réalités rapportées (<em>samʿiyyāt</em>).</p>
<p>La construction du contenu de la matière du livre s’est fondée sur une approche éducative interactive, porteuse d’activités d’enseignement-apprentissage visant à vous faire acquérir la connaissance de la science du Tawḥīd, comprendre ses secrets, réaliser ses fins et rendre proches les notions en usage chez les savants de cet art — connu de certains comme le Grand Droit (<em>al-fiqh al-akbar</em>).</p>
<p>L’espoir est attaché à votre effort et à votre zèle, en plus de constance et d’application, pour qu’il vous soit ouvert de vastes horizons en les recherches de cette science — par laquelle Dieu est connu d’une connaissance où se réalise la sincérité, et la vérité de l’orientation vers Dieu, l’Un, l’Unique, en tous les mouvements et les repos.</p>
<p>Que Dieu nous accorde, à vous et à nous, la sincérité en science et en acte — certes, Il est, le Très-Haut, Audient et Exaucant l’invocation.</p>
<h3>Sommaire des leçons</h3>
<ol>
<li>La présentation d’Ibn Abī Zayd et de son livre la <em>Risāla</em>.</li>
<li>Le motif de la rédaction de la <em>Risāla</em> et son contenu.</li>
<li>La science du Tawḥīd : sa définition et son importance.</li>
<li>Ce que le cœur doit croire et la langue professer.</li>
<li>La transcendance divine à l’égard de l’embrassement de Son essence et de Sa science par la créature.</li>
<li>Parmi les plus beaux noms de Dieu, ceux qui indiquent Ses attributs.</li>
<li>Sa science — glorifié soit-Il — embrasse toute chose.</li>
<li>L’éternité de Ses attributs, Puissant et Majestueux, et Son adresse à Mūsā — sur lui la paix.</li>
<li>La foi au décret et à la prédestination.</li>
<li>La guidance et l’égarement, au nombre de ce dont la prescience précéda — du Subtil, le Bien-Informé.</li>
<li>Le dire sur la volonté divine, la félicité et l’infortune.</li>
<li>Sa seigneurie — Puissant et Élevé — sur les mondes, et l’envoi des messagers vers eux.</li>
<li>La mission de notre maître Muḥammad — paix et bénédiction sur lui —, sceau des missions célestes.</li>
<li>La foi en la survenue de l’Heure, la résurrection et la rétribution.</li>
<li>La sortie des croyants désobéissants du Feu par l’intercession du Prophète — paix et bénédiction sur lui.</li>
<li>Le Paradis, ses habitants et ses délices.</li>
<li>La présentation des créatures devant Dieu Très-Haut.</li>
<li>La foi en la Balance et la remise des feuillets.</li>
<li>La foi au Pont (<em>ṣirāṭ</em>).</li>
<li>La foi au Bassin du Prophète — paix et bénédiction sur lui —, et l’exposé de qui le boira.</li>
<li>La notion de foi (<em>īmān</em>) et ses degrés.</li>
<li>L’interdiction d’excommunier qui que ce soit des gens de la qibla pour un péché, et les réalités invisibles auxquelles il faut croire.</li>
<li>La foi aux anges — sur eux la paix.</li>
<li>La hiérarchie des générations et la supériorité des califes bien guidés.</li>
<li>Ce qu’il faut croire au sujet des Compagnons — que Dieu les agrée.</li>
<li>L’obligation d’obéir au détenteur de l’autorité et de délaisser la dispute en religion.</li>
</ol>
<ul>
<li>Notices biographiques des figures citées.</li>
<li>Sources et références.</li>
</ul>
<h3>Les compétences de l’enseignement de la matière du Tawḥīd</h3>
<p>À la fin de l’année scolaire, l’apprenant(e) de la première année de l’enseignement secondaire traditionnel est attendu capable de :</p>
<ul>
<li>faire présent le sens de la foi en Dieu comme dieu un, unique, paré des attributs de majesté, de beauté et de perfection ;</li>
<li>réaliser le sens de la foi en Dieu dans sa vie personnelle et son comportement individuel ;</li>
<li>réaliser la foi au monde de l’invisible — de ce dont informa le noble Coran, et dont la nouvelle est authentique dans la Sunna du Prophète digne de foi — sur lui la meilleure prière et le plus pur salut ;</li>
<li>exposer le rapport du choix du détenteur de l’autorité (<em>walī al-amr</em>) avec le credo, celui-ci étant une nécessité pour préserver la sécurité spirituelle et la paix sociale.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13980":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13980 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13980 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
