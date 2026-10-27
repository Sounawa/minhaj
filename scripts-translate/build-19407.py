#!/usr/bin/env python3
# build-19407.py — 19407 « Jurisprudence : les jugements de l'interdiction
# du fou et du mineur » (fiqh-tanawi-3, lessons[11], badge Leçon 13/33) —
# suite du bāb, neuvième cours consécutif (… → 9e). 3 axes : concept et
# causes du ḥağr (Ibn Fāris / Ğawharī / Tawḍīḥ 6/226 / Ibn ʿArafa via
# Dasūqī — deux ailes : au-delà de la subsistance vs gratuité au-delà du
# tiers ; Saʿd hadith du tiers ; 5 causes), interdiction du fou et du
# mineur (père/waṣī vs juge ; réveil sans formalité ; mağbūn — Laḫmī,
# Zurqānī 5/512 ; ḥağr de garde ; signes de puberté ×4 ; droit de Dieu vs
# hommes — tardud ; ṣadaq sans soupçon — istiṣḥāb), dispositions du
# discernant et du prodigue (iğāza/radd d'après l'intérêt ; Ibn Rushd
# Bayān 10/537 — 3 avis Ibn al-Qāsim/Aṣbagh/maintien ; Muqaddimāt 2/246
# nul tatabbuʿ ; dirham de nécessité — la comparaison ne particularise
# point ; ḍamān des destructions — ḫiṭāb al-waḍʿ ; testament valide ;
# fin de l'interdit 3 cas — fakk ; prodigue lié : divorce/filiation/
# talion/aveu de peine). Bidāya 4/62 (interdit de l'orphelin — ijmāʿ ;
# grands : Mālik/Šāfiʿī vs Abū Ḥanīfa). CINQ fentes de versets remplies :
# an-Nisāʾ 4:5 (×3) et 4:6 (×2) — vérifiées au quran-cache. Fente
# liminaire NON VIDE (lundi 12 février 2024 — 2e du fil) ; 4 hadiths ;
# ﷺ ×4 exemptées ; coquille التعبيم 8e.
import re

parts = []
for i in range(1, 7):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19407_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    # la ligature ﷺ (0xFDFA) est exemptée par convention de famille
    ar = [c for c in ar if c != chr(0xFDFA)]
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'br', 'dl', 'dt', 'dd']:
    if tag in ('br',):
        continue
    o, c = html.count(f'<{tag}>'), html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')

PROBES = [
    'Jurisprudence : les jugements de l\u2019interdiction du fou et du mineur',
    'Lundi 12 février 2024',
    'Dieu a honoré l\u2019homme par la raison et lui a confié toutes les obligations de la Loi',
    'le Prophète ﷺ a dit : « Le Calame est levé sur trois : sur celui qui dort jusqu\u2019à son réveil',
    'sur le fou jusqu\u2019à ce qu\u2019il retrouve sa raison. » [Musnad de l\u2019imam Aḥmad',
    'Quel est le concept de l\u2019interdiction, et quelles en sont les causes ?',
    'neuvième leçon, au profit des élèves et des élèves de la troisième année secondaire',
    'Connaître le concept de l\u2019interdiction, ses causes et ses jugements.',
    'Distinguer l\u2019interdiction du mineur de celle du fou.',
    'Saisir la sagesse de l\u2019interdiction du fou et du mineur.',
    'Chapitre : le fou est frappé d\u2019interdiction jusqu\u2019à son réveil [de la folie]',
    'Le mineur [l\u2019est] jusqu\u2019à son arrivée à [l\u2019âge de] dix-huit ans, ou au songe',
    'Et cela [s\u2019applique-t-il] aussi au droit de Dieu Très-Haut ? — hésitation',
    'Et au tuteur, le renvoi de la disposition du discernant',
    'et il garantit ce qu\u2019il a corrompu, s\u2019il n\u2019a point été tenu pour digne de confiance',
    'comme celle du prodigue, s\u2019il ne s\u2019y contredit point',
    'jusqu\u2019à ce que, lui qui a un père, il garde son bien après cela',
    'et la levée [de l\u2019interdit] par le tuteur testamentaire et le préposé',
    'tel un dirham de sa vie. Nul divorce de lui, ni l\u2019attribution d\u2019une filiation ni sa négation',
    'ni le talion ni sa négation, ni l\u2019aveu d\u2019une peine',
    'Par : « il est cru » (<em>yuṣaddaq</em>)',
    'Par : « [la disposition] ait réussi » (<em>waqaʿa al-mawqiʿa</em>)',
    'Par : « s\u2019il ne s\u2019y contredit point » (<em>lam yuḫalliṭ</em>)',
    'l\u2019interdit du mineur, du fou, du prodigue et de l\u2019insolvable',
    'Axe premier : le concept de l\u2019interdiction et ses causes',
    'a. Dans la langue :',
    'Ibn Fāris a dit : « Ḥā-ğīm-rāʾ : une seule racine, constante',
    '[Maqāyīs al-luġa, article : ḥağr 2/138]',
    'le gouverneur a interdit le prodigue (<em>ḥagara as-safīh</em>)',
    '[aṣ-Ṣiḥāḥ 2/623]',
    'b. En terminologie :',
    'L\u2019empêchement de l\u2019ayant-droit de toute disposition sur son bien',
    '[at-Tawḍīḥ, commentaire du Muḫtaṣar al-farʿī d\u2019Ibn al-Ḥāğib, du cheikh Khalīl, 6/226]',
    'une qualification de jugement (<em>ṣifa ḥukmiyya</em>)',
    'l\u2019originel en étant à Ibn ʿArafa, dans le Mukhtaṣar 6/444',
    'ou sa disposition à titre gratuit au-delà du tiers de son bien',
    'l\u2019interdit du malade',
    'quand bien même cette disposition ne serait point gratuite, comme la vente et l\u2019achat',
    'hadīth de Saʿd ibn Abī Waqqāṣ',
    'lors du pèlerinage de l\u2019adieu, d\u2019une maladie qui le mit au seuil de la mort',
    'il n\u2019hérite de moi qu\u2019une fille unique',
    'Non : le tiers, et le tiers est beaucoup',
    'la main tendue vers les gens. » [Ṣaḥīḥ Muslim, Livre du testament, chapitre du testament au tiers]',
    'La garde du bien est un des desseins de la Loi islamique',
    '« Et ne donnez pas aux faibles d\u2019esprit vos biens, que Dieu a établis pour vous comme subsistance ; pourvoyez à leurs besoins de ces biens, habillez-les, et tenez-leur un propos convenable. » (Sourate an-Nisāʾ, verset 5)',
    'a. L\u2019insolvabilité</span> (<em>al-fals</em>) : quand la dette cerne le bien du débiteur',
    'ses jugements ont été exposés précédemment, au livre de la défaillance',
    'b. La folie</span> (<em>al-ğunūn</em>), par épilepsie, par obsessions, ou autrement',
    'c. L\u2019enfance</span> (<em>aṣ-ṣibā</em>)',
    'd. La prodigalité</span> (<em>as-safah</em>)',
    'e. La maladie funeste</span> (<em>al-maraḍ al-mawhūm</em>)',
    'Axe deuxième : les jugements de l\u2019interdiction du fou et du mineur',
    '1. Les jugements de l\u2019interdiction du fou',
    'par son père ou son tuteur testamentaire, si la folie le saisit avant la puberté',
    's\u2019il est atteint après elle, l\u2019interdit sur lui relève du juge',
    'sans besoin de lever l\u2019interdit ni de le retirer par jugement',
    '« Et ne donnez pas aux faibles d\u2019esprit vos biens, que Dieu a établis pour vous comme subsistance. » (Sourate an-Nisāʾ, extrait du verset 5)',
    'le fou est faible : il est donc dépouillé de l\u2019expression, et on l\u2019interdit ; tel est le dire d\u2019al-Qarāfī [la Dhakhīra 7/85]',
    'sur le dément jusqu\u2019à son réveil',
    '[as-Sunan al-kubrā d\u2019al-Bayhaqī, Livre de l\u2019aveu, chapitre de celui dont l\u2019aveu n\u2019est point recevable]',
    'ceux qui se laissent tromper dans la vente',
    'Al-Laḫmī a détaillé et dit',
    'on lui commande la stipulation au moment de la vente, et d\u2019en faire témoigner',
    'on lui commande de se tenir en arrière du commerce, et son bien ne lui est point retiré',
    '[Šarḥ az-Zurqānī sur le Mukhtaṣar de Khalīl 5/512, adapté]',
    'le dire du Prophète ﷺ à Ḥabīb ibn Manqidh',
    '« Lorsque tu conclues un échange, dis : point de tromperie (<em>lā ḫilāba</em>). » [Ṣaḥīḥ al-Bukhārī, Livre des ventes, chapitre de ce qui est blâmable de tromperie dans la vente]',
    '2. Les jugements de l\u2019interdiction du mineur',
    'a. La durée de l\u2019interdit sur le mineur.',
    'd\u2019un interdit de garde (<em>ḥağr ḥiḍāna</em>)',
    'il va où il veut ; sauf si l\u2019on craint pour lui corruption ou perdition',
    'b. Les signes de l\u2019âge de la raison.',
    'L\u2019accomplissement de dix-huit années — et l\u2019on a dit : l\u2019entrée dans la dix-huitième.',
    'Le songe (<em>al-ḥulm</em>) : c\u2019est-à-dire l\u2019émission séminale en absolu',
    'Les règles ou la grossesse, à l\u2019égard de la femelle.',
    'La pousse du poil du pubis',
    'l\u2019aisselle, de la barbe ou de la moustache — car elle vient après la puberté',
    'des obligations comme la prière et le jeûne, dont le juge n\u2019a point à connaître',
    '« Et cela [s\u2019applique-t-il] aussi au droit de Dieu Très-Haut ? — hésitation. »',
    'Quand le mineur allègue la puberté, il est cru dans l\u2019affaire de la puberté',
    'le soupçon qui pèse sur sa parole est une ambiguïté',
    'le maintien de l\u2019état (<em>istiṣḥāb al-ḥāl</em>) jusqu\u2019à ce que son contraire s\u2019établisse',
    'Axe troisième : les jugements des dispositions du mineur et du prodigue',
    '1. Le droit du tuteur d\u2019approuver ou de renvoyer les dispositions du mineur',
    'Quand le mineur discernant, ou le prodigue, dispose de son bien par un échange onéreux',
    'au prix juste, et qu\u2019il est destiné à le dépenser sur lui-même en ce dont il ne peut se passer',
    'd\u2019après l\u2019intérêt, non d\u2019après le désir — d\u2019après le dire du Très-Haut',
    '« Éprouvez les orphelins jusqu\u2019à ce qu\u2019ils atteignent l\u2019âge de mariage ; si vous discernez en eux de la raison, alors remettez-leur leurs biens. » (Sourate an-Nisāʾ, extrait du verset 6)',
    'quand l\u2019orphelin vend, sans l\u2019autorisation de son tuteur',
    '[al-Bayān wa-t-taḥṣīl 10/537, adapté]',
    'la vente est renvoyée en toute hypothèse, et qu\u2019aucun du prix n\u2019est poursuivi',
    'on agit donc avec lui au contraire de son dessein corrompu, selon la règle — et c\u2019est le dire d\u2019Ibn al-Qāsim',
    'car la dissipation du bien n\u2019est point permise, et donner pleine main au mineur prodigue sur le bien est le dissiper',
    'le prix n\u2019est point annulé à l\u2019orphelin : on le prélève sur son bien que cette vente a préservé',
    'et c\u2019est le dire d\u2019Aṣbagh',
    'Le troisième, que la vente demeure et n\u2019est point renvoyée',
    's\u2019il a vendu à moins que le prix, ou vendu ce que d\u2019autres avaient plus de droit que lui d\u2019en disposer',
    'le choix du tuteur porte sur les dispositions pécuniaires à titre onéreux ; quant aux grâces, il incombe de les renvoyer',
    'au jeune qui n\u2019a point atteint le songe parmi les hommes, et à la femme qui n\u2019a point atteint les règles, il n\u2019est point permis dans son bien d\u2019acte de bienfaisance — ni don, ni aumône, ni présent. [al-Muqaddimāt al-mumahhadāt 2/246]',
    'la disposition du discernant qui relève des nécessités de la vie',
    'car la sauvegarde de la personne prime la sauvegarde du bien',
    'le kāf y est pour la comparaison, et la règle chez les théoriciens est que la comparaison ne particularise point',
    's\u2019il est devenu rationnel et maître de sa personne',
    'quand bien même sa disposition, avant la puberté, aurait réussi au juste',
    'Et quand le mineur détruit le bien d\u2019autrui, il le garantit sur son bien, s\u2019il en a',
    'la valeur est poursuivie sur sa charge',
    'la garantie des destructions relève de l\u2019ordre de l\u2019institution légale (<em>ḫiṭāb al-waḍʿ</em>), et la puberté n\u2019y est point requise',
    'la règle est que les dépositaires de confiance ne garantissent que s\u2019ils font preuve de négligence',
    '2. Ce qui est valide des dispositions du mineur',
    'comme qu\u2019il fût pour les riches, ou pour les gens de la désobéissance',
    'L\u2019interdit sur le mineur, à l\u2019égard de sa personne, s\u2019achève par sa puberté',
    'jointe à ce qu\u2019il soit devenu gardien de son bien après la puberté, s\u2019il a un père',
    'L\u2019interdit sur celui qui a un tuteur testamentaire ou un préposé s\u2019achève par la levée de l\u2019interdit',
    'l\u2019interdit du père est un interdit d\u2019originel, sans nomination ni introduction d\u2019autrui',
    'tel est le dire d\u2019Ibn ʿĀʾish [Mīnāḥ al-ẓalīl 5/71]',
    '« Témoignez que j\u2019ai levé l\u2019interdit sur un tel, mon interdit',
    'pour la raison qui s\u2019est manifestée auprès de moi, et sa garde de son bien. »',
    '3. Ce qui lie le prodigue de ses dispositions',
    'a. Son divorce</span> : son divorce de son épouse le lie, que ce fût un divorce de libération (<em>ḫulʿ</em>) ou autre.',
    'b. L\u2019attribution d\u2019une filiation et sa négation</span>',
    'pour la sauvegarde des filiations',
    'c. Le talion et sa négation</span>',
    'quant à l\u2019erreur, il n\u2019a point de droit de pardonner — car elle est de l\u2019argent',
    'd. Son aveu d\u2019une peine</span> : qu\u2019il dise : j\u2019ai volé, j\u2019ai tué, j\u2019ai calomnié',
    'les dispositions du mineur sont permises, mais non passées',
    'Quelle est la raison pour laquelle celui qui a un tuteur testamentaire a besoin de la levée de l\u2019interdit',
    '« Les savants s\u2019accordent sur l\u2019obligation d\u2019interdire les orphelins qui n\u2019ont point atteint le songe — d\u2019après le dire du Très-Haut : »',
    'l\u2019interdiction des grands doués de raison, quand paraît d\u2019eux le gaspillage de leurs biens',
    'Mālik, al-Šāfiʿī, les gens de Médine et beaucoup d\u2019entre les gens de l\u2019Iraq',
    'par le jugement du gouverneur',
    'tels sont Ibn ʿAbbās et Ibn az-Zubayr',
    'Et Abū Ḥanīfa et un groupe d\u2019entre les gens de l\u2019Iraq tiennent que l\u2019interdit ne commence point sur les grands',
    'c\u2019est le dire d\u2019Ibrāhīm et d\u2019Ibn Sīrīn',
    's\u2019ils ont maintenu le gaspillage depuis l\u2019enfance, l\u2019interdit se poursuit sur eux',
    '[Bidāyat al-muğtahid 4/62]',
    'J\u2019identifie ce qui est souligné dans le texte.',
    '2. Quelle est l\u2019indication du verset :',
    'sur l\u2019interdiction de l\u2019orphelin ?',
    'J\u2019extrais du texte les avis des savants sur l\u2019interdiction du grand, avec l\u2019argumentation.',
    'Je cherche dans le Code de la famille marocain les causes de l\u2019interdiction et ses effets.',
    'Quels sont les jugements des dispositions du prodigue majeur ?',
    'Qui sont les tuteurs de l\u2019interdit ? Et quels sont leurs degrés ?',
    'Quelles sont les conditions de la vente judiciaire du bien de l\u2019orphelin ?',
    'le livre de la personne, après le livre du failli qui avait ouvert celui du bien',
    'Sur le titre : l\u2019étiquette GT du registre rend le titre par « Dispositions d\u2019interdiction pour les aliénés et l\u2019enfant »',
    'Sur la fente liminaire : NON VIDE au contrôle — « lundi 12 février 2024 »',
    'Sur la salutation prophétique',
    'Sur les cinq fentes de versets',
    'Sur an-Nisāʾ 4:5',
    'Sur an-Nisāʾ 4:6',
    'le quran-cache lit « fā-dfaʿū ilay-him amwāla-hum » (remettez-leur leurs biens)',
    'la leçon 19388 citait la même portion sous la variante « fa-bdhalū »',
    'Sur le Calame levé : deux versions du hadīth',
    'le fou y est nommé « al-maʿtūh » (le dément)',
    'Sur le hadīth de Saʿd : Ṣaḥīḥ Muslim, Livre du testament',
    'Sur l\u2019interdit de garde (<em>ḥağr ḥiḍāna</em>)',
    'Sur les signes de la puberté',
    'Sur la divergence du droit de Dieu et des hommes',
    'Sur les trois avis d\u2019Ibn Rushd (al-Bayān wa-t-taḥṣīl 10/537, adapté)',
    'la règle « on agit avec lui au contraire de son dessein corrompu » est la même que celle du fil (19383)',
    'Sur la comparaison ne particularisant point',
    'Sur « l\u2019ordre de l\u2019institution légale » (<em>ḫiṭāb al-waḍʿ</em>)',
    'Sur le Code de la famille marocain',
    'sans rétro-révision (règle ax)',
]
for probe in PROBES:
    if probe not in html:
        issues.append('SONDE ABSENTE: ' + probe[:80])

n = len(html)
print(f"longueur totale: {n} caractères (≥ 12000 requis)")
if n < 12000:
    issues.append(f"longueur insuffisante: {n}")
ok = sum(1 for p in PROBES if p in html)
print(f"sondes de contenu: {ok}/{len(PROBES)} présentes")
print(f"guillemets: {html.count('«')} / {html.count('»')} ; em: {html.count('<em>')} / {html.count('</em>')} ; li: {html.count('<li>')} / {html.count('</li>')} ; ﷺ: {html.count(chr(0xFDFA))}")

if issues:
    print("PROBLÈMES:")
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
out = '/home/z/my-project/tr-tmp/19407.html'
open(out, 'w').write(html)
print("OK →", out)
