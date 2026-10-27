#!/usr/bin/env python3
# build-14661.py — 14661 « Présentation du manuel » (fiqh-tanawi-3, intro, badge Leçon 1/33)
# PREMIER document du NOUVEAU livre fiqh-tanawi-3 (choix R292 : « le plus grand gisement vierge
# non-pdfOnly » — 33 docs, 0 savant). Livre = Mukhtaṣar de Khalīl + commentaire d'al-Dardīr +
# ḥāshiya d'al-Dasūqī, 3e année secondaire traditionnelle, fiqh des transactions financières.
# Nature : PRÉSENTATION LIMINAIRE (muqaddima) — ZÉRO āyāt, ZÉRO hadith → protocole adapté :
# AUCUN cache coranique, AUCUN Muḥarrar. Source AR 2 847 car : h1 + fente liminaire dl/dt/dd
# VIDE (24e du fil) + paragraphe vide + salutation aux élèves + QUATRE paragraphes + sommaire
# ul de TRENTE-DEUX li + titre repris en clôture + div vides en queue.
# Découvertes de l'état de la source : tatwīl à travers DEUX mots du h1 (الفـقه, مختـصـر) —
# 23e leçon consécutive ; éléments fermants résiduels en queue. Lecture croisée sommaire /
# registre : la 2e entrée (compétences) couvre DEUX docs (16211 + 16212) ; la 4e (ce qui est
# interdit au failli) correspond à DEUX notices quasi jumelles (15355 portail, 19354 leçon) ;
# DEUX entrées sans doc propre (1re « mode d'emploi », 5e « déclaration de faillite ») ;
# INVERSION d'ordre : la pluralité des femmes enceintes (23e au sommaire) SUIT dans le livre
# les types de garantie (24e au sommaire) — signalé sans être tranché.
# Conventions de la FAMILLE fiqh-tanawi (intro 11509, main) : h1 « Le fiqh — le Mukhtaṣar du
# shaykh Khalīl avec le commentaire d'al-Dardīr et la ḥāshiya d'al-Dasūqī : ... année de
# l'enseignement secondaire traditionnel (ʿatīq) », sommaire à <h3> avec items numérotés ;
# N.d.T. RICHER (ère R291/R292) : état de la source, nature et structure, conventions et
# correspondances — ZÉRO arabe (règle g).
import re

FR1 = '''<h1>Le fiqh — le Mukhtaṣar du shaykh Khalīl avec le commentaire d’al-Dardīr et la ḥāshiya d’al-Dasūqī : troisième année de l’enseignement secondaire traditionnel (ʿatīq)</h1>
<p>[Présentation liminaire du manuel : premier document du livre de fiqh de la troisième année de l’enseignement secondaire traditionnel (ʿatīq), consacré cette année au fiqh des transactions financières, d’après le <em>Mukhtaṣar</em> du shaykh Khalīl, avec le commentaire d’al-Dardīr et la ḥāshiya d’al-Dasūqī. Après le titre, la présentation s’adresse directement aux élèves, expose la démarche du manuel en quatre paragraphes — l’arrivée au terme du cycle secondaire, la source du livre, sa méthodologie de construction des leçons, sa vocation d’auxiliaire didactique qui mène à l’habitus jurisprudentiel et aux études supérieures —, puis déroule le sommaire du manuel en TRENTE-DEUX entrées : les compétences visées, le glossaire des termes du shaykh Khalīl, les leçons du failli et de son bien, de l’interdiction, de la transaction, de la cession de dette, de la garantie et de ses espèces, des sociétés et de leurs règles, jusqu’aux deux index qui clôturent le livre.]</p>
<p>À vous, nos élèves, fils et filles :</p>
<p>Nous voici, par la faveur d’Allah le Très-Haut, de Sa grâce et de Sa bonne réussite, parvenus avec vous au terme du cycle secondaire de l’enseignement traditionnel (ʿatīq), mettant entre vos mains le livre de la discipline du fiqh de la troisième année de l’enseignement secondaire traditionnel, consacré au fiqh des transactions financières.</p>
<p>Fidèles à la voie tenue en la première et en la deuxième années de l’enseignement secondaire traditionnel, nous avons retenu, pour l’élaboration de ce livre, le <em>Mukhtaṣar</em> du shaykh Khalīl avec le commentaire d’al-Dardīr et la ḥāshiya d’al-Dasūqī, fondant la construction des leçons sur une méthodologie qui rapproche les contenus du <em>matn</em> — objet de l’étude et de l’analyse — par un style qui unit le démontage de ses parties et l’édification de contenus extraits du commentaire qui accompagne le <em>matn</em> et de la ḥāshiya qui le glose.</p>
<p>Ce livre demeure un auxiliaire d’enseignement qui stimule le retour au livre originaire avec ses commentaires pour l’étude, et l’acquisition d’une habileté accrue dans la fréquentation des livres de l’héritage jurisprudentiel malikite — fréquentation qui vous rendra maîtres du style juridique et vous qualifiera pour acquérir l’habitus jurisprudentiel (<em>malaka fiqhiyya</em>) en fiqh des transactions financières, dont vous avez passé les deux années précédentes à étudier certains chapitres et certaines règles ; habileté qui vous poussera, de la sorte, à poursuivre vos études supérieures, pourvus des règles de la science et des instruments de la recherche, de la précision et de la vérification — instruments essentiels de tout étudiant du savoir dans le domaine du fiqh en général, et du fiqh des transactions financières en particulier, domaine où ne cessent d’apparaître de nouvelles transactions financières.</p>
<p>Sur vous est fondé l’espoir, par votre engagement avec les contenus de ce livre, de réaliser les compétences et les objectifs que l’on entend réaliser au terme de cette année scolaire.<br>Qu’Allah nous accorde la réussite, à nous et à vous, affermisse votre démarche et fasse du succès votre allié — c’est Lui, le Très-Haut, le Maître de cela et le Capable de le réaliser.</p>
'''

FR2 = '''<h3>Sommaire du manuel</h3>
<ul>
<li>1. Comment utiliser mon livre</li>
<li>2. Les compétences de l’enseignement du fiqh en troisième année de l’enseignement secondaire traditionnel</li>
<li>3. Le glossaire des termes du shaykh Khalīl</li>
<li>4. Ce qui est interdit au failli et ce qui ne lui est pas interdit</li>
<li>5. Les règles de la déclaration de faillite et du renouvellement de l’interdiction prononcée contre lui</li>
<li>6. Les règles de la vente du bien du failli et du paiement de ses dettes</li>
<li>7. La garantie du droit du créancier et l’établissement de l’état du failli</li>
<li>8. Les moyens d’établir l’état du failli</li>
<li>9. Les options du créancier pour recouvrer son droit auprès du débiteur</li>
<li>10. Les règles des actes du créancier sur ce qui lui appartient auprès du failli</li>
<li>11. L’effet de la faillite de l’artisan, du loueur et du vendeur</li>
<li>12. Les règles de l’interdiction du fou et du mineur</li>
<li>13. Les règles des actes du prodigue majeur et l’ordre des tuteurs</li>
<li>14. Les règles de la vente de l’immeuble de l’orphelin</li>
<li>15. Les divisions de la transaction et ses règles</li>
<li>16. Les règles de la transaction de l’injuste et du tuteur du sang</li>
<li>17. Les règles de la transaction sur les vies et les blessures</li>
<li>18. Les règles de la transaction de l’un des deux héritiers ou des deux associés</li>
<li>19. Les règles de la cession de dette (ḥawāla)</li>
<li>20. Des règles du garant et du garanti</li>
<li>21. Les règles de la caution de l’absent et le différend du garant et du garanti</li>
<li>22. La stipulation dans la garantie et ses causes de nullité</li>
<li>23. Les règles de la pluralité des femmes enceintes</li>
<li>24. Les types de garantie et leurs règles</li>
<li>25. Qui conclut la société et par quoi elle se conclut</li>
<li>26. Les règles de la société de négociation</li>
<li>27. Les actes de l’associé de la société de négociation et les règles du litige</li>
<li>28. Les règles de la société d’ʿinān</li>
<li>29. Les règles de la société de transmission (ǧabr) et de la société de travail</li>
<li>30. Les règles de la société de dettes et de personnes</li>
<li>31. L’index des figures</li>
<li>32. L’index des sources et références</li>
</ul>
'''

FR3 = '''<p>Le fiqh — le Mukhtaṣar du shaykh Khalīl avec le commentaire d’al-Dardīr et la ḥāshiya d’al-Dasūqī, pour la troisième année de l’enseignement secondaire traditionnel.</p>
<p>N.d.T. — État de la source numérisée de ce premier document : la fente liminaire de listes est vide — VINGT-QUATRIÈME fente vide du fil ; le tatwīl court à travers DEUX mots du titre — le nom de la discipline et le nom du <em>matn</em> abrégé — VINGT-TROISIÈME leçon consécutive ; un paragraphe imprimé vide suit la fente liminaire, et des éléments de fermeture vides subsistent en queue du document, résidus de la structure de la page numérisée. Le titre est imprimé deux fois : en tête, puis repris à l’identique en clôture du sommaire — reprise fidèlement rendue. La présentation s’ouvre sur une salutation directe aux élèves, fils et filles, forme épistolaire qui place le lecteur au cœur de l’ouvrage ; elle s’achève sur la formule de vœu, appel à la réussite confiée à Allah. Ni verset coranique ni hadith ne figurent à la présentation — aucune vérification au cache coranique n’étant requise pour ce document.</p>
<p>N.d.T. — Nature et structure : cette présentation liminaire fait fonction de muqaddima du livre. La lecture croisée de son sommaire avec le registre du livre appelle TROIS observations, signalées sans être tranchées. PREMIÈREMENT, sur TRENTE-DEUX entrées, la deuxième (les compétences de l’enseignement du fiqh) correspond à DEUX documents distincts du livre — les compétences de la discipline, puis les compétences propres au <em>Mukhtaṣar</em> du shaykh Khalīl — et la quatrième (ce qui est interdit au failli) correspond, elle aussi, à DEUX notices quasi jumelles : une notice-portail portant le titre suivi du nom du livre, et la leçon de même titre qui la suit au registre. DEUXIÈMEMENT, DEUX entrées du sommaire ne reçoivent pas de document propre : la première (« Comment utiliser mon livre »), annoncée à l’ouverture et dont la matière se retrouve disséminée dans les rubriques des leçons, et la cinquième (la déclaration de faillite et le renouvellement de l’interdiction), dont la matière est traitée au fil des leçons consacrées au failli. TROISIÈMEMENT, une inversion d’ordre est observable : au sommaire, la pluralité des femmes enceintes (vingt-troisième entrée) précède les types de garantie (vingt-quatrième) ; au registre du livre, les types de garantie précèdent la pluralité des femmes enceintes — l’ordre du sommaire étant suivi ici tel quel, la divergence signalée. Reste l’architecture d’ensemble : ouverture didactique, compétences, glossaire, VINGT-SEPT leçons juridiques — du failli et de son bien aux sociétés en leurs espèces —, puis DEUX index ; la même architecture que celle du livre de tafsīr achevé au tour précédent, sommaire et index fermant le volume.</p>
'''

FR4 = '''<p>N.d.T. — Le genre de la présentation dans le corpus : les manuels de la collection s’ouvrent presque tous sur une présentation liminaire de ce genre — voix de l’équipe d’élaboration s’adressant directement à l’élève, rappel de la source du livre, exposé de la méthodologie, sommaire déroulé. La présentation du livre de fiqh de première année, de la même famille, tenait le même propos en des termes voisins : même salutation à l’élève, même fierté de remettre l’ouvrage entre ses mains, même insistance sur le retour au livre originaire avec ses commentaires, même promesse d’un savoir qui prépare aux études supérieures. Ce qui distingue la présentation de la troisième année, c’est l’horizon qu’elle assigne : là où la première année introduisait à la science des ventes, la troisième s’ouvre sur le fiqh des transactions financières — discipline qu’elle présente comme vivante, traversée par l’apparition de transactions nouvelles, et qui exige, dit-elle, les instruments du chercheur : les règles de la science, la recherche, la précision, la vérification. La présentation tient ainsi lieu de programme : elle annonce, en une phrase, l’arc de l’année — du failli et de son bien, dont les deux années précédentes avaient déjà abordé certains chapitres et certaines règles, aux sociétés en leurs espèces, jusqu’aux index ; elle expose, en une phrase, la méthode — le démontage du <em>matn</em>, l’édification des contenus à partir du commentaire et de la ḥāshiya ; elle assigne, en une phrase, le but — l’habitus jurisprudentiel, qui n’est point simple mémoire des règles mais possession maîtrisée de l’esprit de la loi. Aucun verset, aucun hadith ne soutient ce propos liminaire : la présentation relève du genre didactique, non du genre du commentaire — c’est aux leçons qui suivent qu’il reviendra de convoquer le Livre et la Sunna, et c’est là que s’exercera, tour après tour, la vérification aux sources.</p>
<p>N.d.T. — Conventions et correspondances : la terminologie juridique suit celle du fil — « failli » pour le débiteur frappé d’insolvabilité, « créancier » pour celui qui réclame son droit, « interdiction » pour l’incapacité légale (<em>ḥaǧr</em>), « transaction » pour le compromis légale (<em>ṣulḥ</em>), « cession de dette » pour la <em>ḥawāla</em>, « garant » et « garanti » pour les deux parties de la garantie, « société » pour les diverses formes de l’association — la société de négociation, la société d’ʿinān, la société de transmission, la société de travail, la société de dettes et de personnes ; « le prodigue » pour le <em>safīh</em>, « le tuteur du sang » pour le parent du tué porteur du droit au prix du sang, « les femmes enceintes » pour les porteuses réclamant la garantie d’accouchement. Le nom du shaykh Khalīl, d’al-Dardīr et d’al-Dasūqī, les mots <em>matn</em>, <em>Mukhtaṣar</em>, <em>ḥāshiya</em>, <em>malaka fiqhiyya</em>, suivent les conventions de la famille des livres de fiqh du corpus, où le même binôme — le <em>Mukhtaṣar</em> du shaykh Khalīl, le commentaire d’al-Dardīr et la ḥāshiya d’al-Dasūqī — servait déjà de source au livre de première année : la présentation le dit expressément, qui inscrit la troisième année dans la continuité des deux premières et annonce le passage des ventes, étudiées lors des années précédentes, aux transactions financières de l’année qui s’ouvre — domaine où, dit la présentation, ne cessent d’apparaître des transactions nouvelles, appelant les instruments de la recherche, de la précision et de la vérification qui font le savant. Correspondance avec le corpus : le livre s’ouvre l’année même où le précédent volume de la collection — le livre de tafsīr, achevé au tour précédent — se clôturait sur ses deux index ; le sommaire ici déroulé annonce, à ses entrées trente et unième et trente-deuxième, le même appareil d’index — figures citées, sources et références — qui sera livré en son temps selon le protocole des index déjà rodé. Les compétences annoncées à la deuxième entrée seront livrées dans leurs deux documents ; le glossaire des termes du shaykh Khalīl, à la troisième ; les leçons juridiques, dans l’ordre du registre, chaque verset — il ne s’en trouve point ici — étant autrefois vérifié au cache coranique, chaque leçon du fiqh devant être relue contre le commentaire et la ḥāshiya imprimés en ligne au fil des tours à venir.</p>
'''

html = FR1 + FR2 + FR3 + FR4
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [(0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF), (0xFB50, 0xFDF9), (0xFDFB, 0xFDFF), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h3', 'p', 'ul', 'li', 'em', 'br']:
    if tag == 'br':
        continue
    o, c = html.count(f'<{tag}'), html.count(f'</{tag}>')
    if tag == 'p':
        o = len(re.findall(r'<p>', html))
        c = html.count('</p>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')
n_li = html.count('<li>')
n_ndt = html.count('N.d.T.')
print(f'caractères: {len(html)}')
print(f'entrées li: {n_li}')
print(f'paragraphes N.d.T.: {n_ndt}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
if n_li != 32:
    issues.append(f'entrées attendues 32, trouvées {n_li}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/14661.html'
open(out, 'w').write(html)
print('écrit:', out)
