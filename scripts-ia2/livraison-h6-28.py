#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — livraison-h6-28 : traduction française (htmlFr) de la leçon 28
# «لائحة المصادر والمراجع» de hadith-6ep — docId pdf-mut23h3b-708
# (pp.146-148 du tirage, titre calligraphié). DERNIÈRE leçon de hadith-6ep
# (28/28 pdf-slots) — achève la zone préparatoire de l'IA-2.
# Transcription établie ce tour (Z2-64) sur les rendus 600 dpi survivants
# (l28-src/pg-146..148) + 2 passes OCR (l28-ocr, l28-src) + bandes de
# vérification 2000 px + microcrops 2400-4800 dpi (mc/ + mc-i*) :
#   - titre calligraphié «لائحة المصادر والمراجع» (الصادر لل calligraphie,
#     OCR «المصاءر» écarté — lecture directe) ;
#   - préambule «برواية ورش عن نافع من طريق الأزرق؛ المصحف المحمدي الذي
#     نشرته مؤسسة محمد السادس لنشر المصحف الشريف.» (lecture directe p.146) ;
#   - rubrique «كتب الحديث:» (OCR l'avait sautée) puis entrées 1-13 ;
#   - item 1 : المتوفى 256هـ (bande), glyphe ﷺ du titre épelé dans le rendu
#     (convention), دار ابن كثير، اليمامة - بيروت ;
#   - item 6 : fin RESTAURÉE par lecture directe (2 passes OCR la perdaient) :
#     «(المتوفى: 275هـ) تحقيق: محمد محيي الدين عبد الحميد، نشر: المكتبة
#     العصرية، صيدا - بيروت.» ;
#   - item 7 : البُسْتِي (4800 dpi mc/e147bas), «1414 - 1993» sans unités
#     (porté tel quel) ;
#   - item 9 : 1421هـ - 2001م (bande, contre OCR «1ه») ;
#   - item 12 : «بن سابق الدين» (2400 dpi mc-i12 — variante canonique
#     «سبق الدين» consignée au worklog, portée telle quelle) ;
#   - item 14 : «المعروف بابن دقيق العبد» 4800 dpi (mc/e147abd) — coquille
#     d'imprimerie manifeste pour «العيد» (le manuel cite ابن دقيق العيد en
#     sa leçon 1) ; rendu «Ibn Daqīq al-ʼĪd» + N.d.T. ; القشيري 4800 dpi
#     (mc/e147qsh) ; الطبعة السادسة، 1424هـ ;
#   - item 15 : الطبعة الأولى، 1428هـ (bande, contre OCR «68ه») ;
#   - item 16 : tête RESTAURÉE par lecture directe (bande p148-haut) :
#     «فتح الباري شرح صحيح البخاري؛ لمؤلفه: أبي الفضل أحمد بن علي بن حجر
#     العسقلاني. رقم كتبه وأبوابه وأحاديثه محمد فؤاد عبد الباقي. صححه
#     وأشرف على طبعه محب الدين الخطيب، نشر دار المعرفة بيروت، 1379هـ» ;
#   - item 18 : généalogie lettre à lettre (mc-i18-auth2/auth3/l2 4800 dpi) :
#     «محمد أشرف بن أمير بن علي بن حيدر، أبي الطيب، شرح الحق، الصديقي،
#     العظيم آبادي، علامة بالحديث، هندي. توفى (بعد 1310هـ - 1892م).» —
#     attribution canon (ʼAbd al-Ḥayy al-Laknawī al-ʼAẓīmābādī 1304 H)
#     consignée au worklog, portée telle quelle + N.d.T. ;
#   - item 19 : «ولد سنة (736هـ) وتوفي (795هـ)» (bande) ; le tirage range
#     فتح الباري parmi ses مصنفات — écart canon consigné + N.d.T. ;
#   - rubrique «مراجع أخرى:» (OCR l'avait sautée) puis item 20 : إحياء
#     علوم الدين، المتوفى 505هـ، دار المعرفة - بيروت، عدد الأجزاء: 4.
#   - «وآخرين» item 4 (mc-i4-fin, contre pass1 «وآخرين»/pass2 «وآخرون») ;
#   - فهرس الموضوعات p.149 HORS slot (contrôle pg-149) — consigné.
# Rendu calqué sur la page homologue hadith-5ep pdf-29 (IA-1) : titre
# translittéré + span arabe court, «vérification de», «mort en NNN H»,
# «N<sup>e</sup> éd., AAAA H / AAAA», glosses françaises des titres.
import re, os

SPAN = re.compile(r'(<span dir="rtl" lang="ar">.*?</span>)', re.S)

HTML = """<h1>Liste des sources et références</h1>
<p>Vingt-huitième et dernière leçon (28) du manuel « Le hadith tiré du livre des <em>Arba’ūn</em> nawawiyya de l’imam <em>al-Nawawī</em>, avec le commentaire d’Ibn Daqīq al-’Īd », à l’intention des élèves de sixième année de l’enseignement primaire traditionnel (<em>ta’līm ’atīq</em>) : la liste des sources et références (<em>lā’iḥat al-maṣādir wa-l-marāǧi’</em> <span dir="rtl" lang="ar">(لائحة المصادر والمراجع)</span>), sous un titre calligraphié, ferme le volume aux pages 146 à 148 du tirage, après la séance de soutien et d’application. Elle dresse, en une ouverture consacrée au noble Coran puis trois rubriques — les livres de hadith, les commentaires de hadith, puis d’autres références —, les vingt ouvrages mobilisés par les auteurs du manuel, avec, tels qu’imprimés : le titre, l’auteur et, le cas échéant, sa date de mort, le vérificateur, la maison d’édition, le lieu, le rang et le millésime de l’édition ; la numérotation, continue de 1 à 20, couvre les trois rubriques. S’y détache, en tête des commentaires, l’entrée n° 14 — le commentaire des Quarante d’Ibn Daqīq al-’Īd, l’ouvrage sur lequel le manuel est tout entier établi. N.d.T. : l’index des matières (<em>fihrist</em> <span dir="rtl" lang="ar">(فهرس)</span>) qui suit à la page 149 du tirage ne fait pas partie de la leçon ; trois singularités du tirage — entrées n° 14, 18 et 19 — sont signalées en leur lieu.</p>
<h2>Le noble Coran (<em>al-qur’ān al-karīm</em> <span dir="rtl" lang="ar">(القّرآن الكريم)</span>)</h2>
<p>Le noble Coran, selon la lecture de Warš d’après Nāfi’, par la voie d’al-Azraq (<em>al-qur’ān al-karīm, bi-riwāyat Warš ’an Nāfi’ min ṭarīq al-Azraq</em> <span dir="rtl" lang="ar">(برواية ورش عن نافع من طريق الأزرق)</span>) — le <em>muṣḥaf</em> « muḥammadien » (<em>al-muṣḥaf al-Muḥammadī</em> <span dir="rtl" lang="ar">(المصحف المحمدي)</span>) publié par la Fondation Mohammed VI pour l’édition du Noble Coran (<em>mu’assasat Muḥammad as-sādis li-našr al-muṣḥaf aš-šarīf</em> <span dir="rtl" lang="ar">(مؤسسة محمد السادس لنشر المصحف الشريف)</span>).</p>
<h2>Les livres de hadith (<em>kutub al-ḥadīṯ</em> <span dir="rtl" lang="ar">(كتب الحديث)</span>)</h2>
<ol>
<li><em>Ṣaḥīḥ al-Buḫārī</em> <span dir="rtl" lang="ar">(صحيح البخاري)</span>, « al-Ǧāmi’ al-musnad aṣ-ṣaḥīḥ al-muḫtaṣar min umūri rasūli llāhi ṣallā llāhu ’alayhi wa-sallam wa-sunanihi wa-’ayyāmih » (le Recueil authentique continu, abrégé des affaires du Messager d’Allah — prière et salut d’Allah sur lui —, de ses pratiques et de ses journées), de ’Abū ’Abd Allāh Muḥammad ibn Ismā’īl al-Buḫārī al-Ǧa’fī (mort en 256 H) ; vérification de Dr Muṣṭafā Dīb al-Buġā, professeur du hadith et de ses disciplines à la faculté de droit musulman de l’université de Damas ; Dār Ibn Kaṯīr, al-Yamāma - Beyrouth, 3<sup>e</sup> éd., 1407 H / 1987.</li>
<li><em>Ṣaḥīḥ Muslim</em> <span dir="rtl" lang="ar">(صحيح مسلم)</span>, dit « al-Ǧāmi’ », ou « al-Musnad », ou « al-Musnad aṣ-ṣaḥīḥ », de ’Abū l-Ḥusayn Muslim ibn al-Ḥaǧǧāǧ al-Qašayrī an-Naysābūrī (mort en 261 H) ; vérification de Muḥammad Fu’ād ’Abd al-Bāqī ; Dār al-Ḥadīṯ, 1<sup>re</sup> éd., 1414 H / 1994.</li>
<li><em>al-Muwaṭṭa’</em> <span dir="rtl" lang="ar">(الموطأ)</span>, de l’imam Mālik ibn ’Anas, transmission de Yaḥyā ibn Yaḥyā al-Layṯī ; édition du Conseil scientifique supérieur, 1<sup>re</sup> éd., 1434 H / 2013.</li>
<li>Les <em>Sunan d’at-Tirmiḏī</em> <span dir="rtl" lang="ar">(سنن الترمذي)</span>, de Muḥammad ibn ’Īsā, Abī ’Īsā, at-Tirmiḏī as-Sulamī ; vérification de ’Aḥmad Muḥammad Šākir et d’autres ; Dār ’Iḥyā’ at-Turāṯ al-’Arabī - Beyrouth.</li>
<li>Les <em>Sunan d’an-Nasā’ī</em> <span dir="rtl" lang="ar">(سنن النسائي)</span> — « al-Muǧtabā min as-sunan », les Sunan mineures d’an-Nasā’ī —, de ’Abū ’Abd ar-Raḥmān ’Aḥmad ibn Šu’ayb ibn ’Alī al-Ḫurāsānī, an-Nasā’ī (mort en 303 H) ; vérification de ’Abd al-Fattāḥ Abū Ġadda ; Maktab al-Maṭbū’āt al-Islāmiyya - Alep, 2<sup>e</sup> éd., 1406 H / 1986.</li>
<li>Les <em>Sunan d’Abū Dāwūd</em> <span dir="rtl" lang="ar">(سنن أبي داود)</span>, de ’Abū Dāwūd Sulaymān ibn al-’Aš’ath ibn ’Isḥāq al-Azdī as-Suǧistānī (mort en 275 H) ; vérification de Muḥammad Muḥyī d-Dīn ’Abd al-Ḥamīd ; al-Maktaba al-’Aṣriyya, Ṣaydā - Beyrouth.</li>
<li><em>Ṣaḥīḥ Ibn Ḥibbān</em> <span dir="rtl" lang="ar">(صحيح ابن حبان)</span>, de Muḥammad ibn Ḥibbān ibn ’Aḥmad ibn Ḥibbān ibn Mu’āḏ ibn Ma’bad at-Tamīmī, Abī Ḥātim, ad-Dārimī, al-Bustī (mort en 354 H) ; vérification de Šu’ayb al-’Arnā’ūṭ ; Mu’assasat ar-Risāla - Beyrouth, 2<sup>e</sup> éd., 1414 H / 1993.</li>
<li><em>al-Mustadrak ’alā ṣ-ṣaḥīḥayn</em> <span dir="rtl" lang="ar">(المستدرك على الصحيحين)</span>, de ’Abū ’Abd Allāh al-Ḥākim Muḥammad ibn ’Abd Allāh ibn Muḥammad ibn Ḥamdawayh ibn Na’īm ibn al-Ḥakam aḍ-Ḍabbī aṭ-Ṭahmānī an-Naysābūrī, connu comme Ibn al-Bayy’ (mort en 405 H) ; vérification de Muṣṭafā ’Abd al-Qādir ’Aṭā’ ; Dār al-Kutub al-’Ilmiyya, Beyrouth, 1<sup>re</sup> éd., 1411 H / 1990.</li>
<li>Le <em>Musnad de l’imam ’Aḥmad ibn Ḥanbal</em> <span dir="rtl" lang="ar">(مسند الإمام أحمد بن حنبل)</span>, de ’Abū ’Abd Allāh ’Aḥmad ibn Muḥammad ibn Ḥanbal ibn Hilāl ibn ’Asad aš-Šaybānī (mort en 241 H) ; vérification de Šu’ayb al-’Arnā’ūṭ, ’Ādil Muršid et d’autres, sous la supervision de Dr ’Abd Allāh ibn ’Abd al-Muḥsin at-Turkī ; Mu’assasat ar-Risāla, 1<sup>re</sup> éd., 1421 H / 2001.</li>
<li><em>al-Mu’ǧam al-awsaṭ</em> <span dir="rtl" lang="ar">(المعجم الأوسط)</span>, de Sulaymān ibn ’Aḥmad ibn ’Ayyūb aṭ-Ṭabarānī (mort en 360 H) ; vérification de Ṭāriq ibn ’Awḍ Allāh ibn Muḥammad et de ’Abd al-Muḥsin ibn Ibrāhīm al-Ḥusaynī ; Dār al-Ḥaramayn - Le Caire.</li>
<li>Le <em>Musnad d’ad-Dārimī</em> <span dir="rtl" lang="ar">(مسند الدارمي)</span>, de ’Abd Allāh ibn ’Abd ar-Raḥmān, Abī Muḥammad, ad-Dārimī ; éditeur : Dār al-Kitāb al-’Arabī - Beyrouth ; vérification de Fawwāz ’Aḥmad Zamarlī et de Ḫālid as-Sab’ al-’Ilmī ; nombre de volumes : 2 ; 1<sup>re</sup> éd., 1407 H.</li>
<li><em>al-Ǧāmi’ aṣ-ṣaġīr min ḥadīṯ al-bašīr an-naḏīr</em> <span dir="rtl" lang="ar">(الجامع الصغير من حديث البشير النذير)</span> (Le petit recueil des hadiths de l’annonciateur et de l’avertisseur), de l’imam Ǧalāl d-Dīn ’Abd ar-Raḥmān ibn ’Abī Bakr ibn Muḥammad ibn Sābiq d-Dīn as-Suyūṭī.</li>
<li><em>Makārim al-’aḫlāq wa-ma’ālīhā wa-maḥmūd ṭarā’iqihā</em> <span dir="rtl" lang="ar">(مكارم الأخلاق ومعاليها ومحمود طرائقها)</span> (Les nobles moeurs, leurs sublimités et leurs voies louables), de ’Abū Bakr Muḥammad ibn Ǧa’far ibn Sahl ibn Šākir as-Sāmarī al-Ḫarā’iṭī (mort en l’an 327 H) ; vérification et étude de Dr ’Abd Allāh ibn Baǧaš ibn Ṯābit al-Ḥimyarī ; édition de Maktabat ar-Rušd, année 2006.</li>
</ol>
<h2>Les commentaires de hadith (<em>šurūḥ al-ḥadīṯ</em> <span dir="rtl" lang="ar">(شروح الحديث)</span>)</h2>
<ol start="14">
<li><em>Šarḥ al-’Arba’īn an-nawawiyya fī l-’aḥādīṯ aṣ-ṣaḥīḥa an-nabawiyya</em> <span dir="rtl" lang="ar">(شرح الأربعين النووية في الأحاديث الصحيحة النبوية)</span> (Commentaire des Quarante nawawiennes parmi les hadiths prophétiques authentiques), de Taqīy d-Dīn Abī l-Fatḥ Muḥammad ibn ’Alī ibn Wahb ibn Muṭī’ al-Qašayrī, connu comme Ibn Daqīq al-’Īd — le commentaire dont le présent manuel est tiré — ; éditeur : Mu’assasat ar-Rayyān, 6<sup>e</sup> éd., 1424 H. N.d.T. : le tirage porte « connu comme Ibn Daqīq al-’Abd », coquille d’imprimerie manifeste pour le nom universellement attesté Ibn Daqīq al-’Īd, que le manuel même cite en ouverture de sa matière ; le rendu porte le nom correct, l’écart étant consigné.</li>
<li><em>al-Fatḥ al-mubīn bi-šarḥ al-’Arba’īn</em> <span dir="rtl" lang="ar">(الفتح المبين بشرح الأربعين)</span> (L’ouverture manifeste, commentaire des Quarante), du cheikh de l’islam ’Abī l-’Abbās Šihāb d-Dīn ’Aḥmad ibn Muḥammad ibn ’Alī ibn Ḥaǧar al-Haytamī as-Sa’dī al-Anṣārī ; éditeur : Dār al-Minhāǧ - Djeddah, 1<sup>re</sup> éd., 1428 H.</li>
<li><em>Fatḥ al-Bārī šarḥ Ṣaḥīḥ al-Buḫārī</em> <span dir="rtl" lang="ar">(فتح الباري شرح صحيح البخاري)</span>, de ’Aḥmad ibn ’Alī ibn Ḥaǧar, ’Abī l-Faḍl, al-’Asqalānī ; numérotation de ses livres, chapitres et hadiths par Muḥammad Fu’ād ’Abd al-Bāqī ; corrigé et imprimé sous la supervision de Muḥibb d-Dīn al-Ḫaṭīb ; publication : Dār al-Ma’rifa, Beyrouth, 1379 H.</li>
<li><em>Šarḥ Ibn Baṭṭāl li-Ṣaḥīḥ al-Buḫārī</em> <span dir="rtl" lang="ar">(شرح ابن بطال لصحيح البخاري)</span> (Le commentaire d’Ibn Baṭṭāl sur le Ṣaḥīḥ d’al-Buḫārī), de ’Alī ibn Ḫalaf ibn ’Abd al-Malik Ibn Baṭṭāl, Abī l-Ḥasan, savant du hadith originaire de Cordoue, mort en l’an 449 H.</li>
<li><em>’Awn al-ma’būd šarḥ sunan ’Abī Dāwūd</em> <span dir="rtl" lang="ar">(عون المعبود شرح سنن أبي داود)</span> (Le secours du Serviteur adoré, commentaire des Sunan d’Abū Dāwūd), de Muḥammad ’Ašraf ibn ’Amīr ibn ’Alī ibn Ḥaydar, ’Abī ṭ-Ṭayyib, Šarḥ al-Ḥaqq, aṣ-Ṣiddīqī, al-’Aẓīm ’Ābādī, savant du hadith, indien — décédé (après 1310 H / 1892). N.d.T. : l’attribution est portée telle quelle ; le commentaire est universellement attribué à ’Abd al-Ḥayy al-Laknawī al-’Aẓīm-’Ābādī (mort en 1304 H), dont l’imprimé porte ici la nisba d’al-’Aẓīm-’Ābādī, avec une année de décès suivie de « après 1310 H » ; l’écart est consigné sans correction.</li>
<li><em>Ǧāmi’ al-’ulūm wa-l-ḥikam šarḥ ḫamsīna ḥadīṯan min ǧawāmi’ al-kalim</em> <span dir="rtl" lang="ar">(جامع العلوم والحكم شرح خمسين حديثا من جوامع الكلم)</span> (Le compendium des sciences et des sagesses, commentaire de cinquante hadiths d’entre les paroles synthétiques), de Zayn d-Dīn ’Abd ar-Raḥmān ibn ’Aḥmad ibn Raǧab as-Salāmī, al-Baġdādī puis ad-Dimašqī, al-Ḥanbalī, le ḥāfiẓ, le traditionniste, le juriste — il a plusieurs ouvrages, dont le commentaire d’at-Tirmiḏī et Fatḥ al-Bārī, commentaire du Ṣaḥīḥ d’al-Buḫārī —, né en l’an (736 H) et décédé en l’an (795 H). N.d.T. : le tirage range Fatḥ al-Bārī parmi les ouvrages d’Ibn Raǧab ; ce commentaire est celui d’Ibn Ḥaǧar al-’Asqalānī (entrée n° 16 ci-dessus) ; l’écart est consigné sans correction.</li>
</ol>
<h2>Autres références (<em>marāǧi’ uḫrā</em> <span dir="rtl" lang="ar">(مراجع أخرى)</span>)</h2>
<ol start="20">
<li><em>Iḥyā’ ’ulūm d-dīn</em> <span dir="rtl" lang="ar">(إحياء علوم الدين)</span> (La vivification des sciences de la religion), de ’Abū Ḥāmid Muḥammad ibn Muḥammad al-Ġazālī aṭ-Ṭūsī (mort en 505 H) ; éditeur : Dār al-Ma’rifa - Beyrouth ; nombre de volumes : 4.</li>
</ol>"""

def normalize(html):
    out = []
    for part in SPAN.split(html):
        if part.startswith('<span dir="rtl"'):
            out.append(part)
            continue
        p = part
        p = re.sub(r' +([;:?!»])', '\u202f\\1', p)
        p = re.sub(r'(«) +', '\\1\u202f', p)
        out.append(p)
    return "".join(out)

def controls(html):
    assert "'" not in html, "apostrophe droite résiduelle"
    outside = []
    for seg in SPAN.split(html):
        if seg.startswith('<span dir="rtl"') or seg.endswith('</span>'):
            continue
        if re.search(r'[\u0621-\u064A]', seg) and 'ﷺ' not in seg:
            outside.append(seg[:60])
    assert not outside, f"arabe hors span: {outside[:3]}"
    assert html.count('«') == html.count('»'), f"guillemets déséquilibrés {html.count('«')}/{html.count('»')}"
    for tag in ["h1", "h2", "h3", "h4", "p", "ul", "ol", "li", "table", "tr", "td", "th", "strong", "em", "sup", "span"]:
        o = len(re.findall(rf"<{tag}[ >]", html))
        c = len(re.findall(rf"</{tag}>", html))
        assert o == c, f"balise {tag}: {o}o/{c}f"
    print(f"contrôles OK — U+202F ×{html.count(chr(0x202f))}, guillemets {html.count('«')}, {len(html)} caractères")

if __name__ == "__main__":
    HTML = normalize(HTML)
    controls(HTML)
    out = "/home/z/my-project/minhaj/tr-tmp/pdf-mut23h3b-708.html"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(HTML)
    print("écrit :", out)
