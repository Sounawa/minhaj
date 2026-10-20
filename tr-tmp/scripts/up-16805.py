#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16805 (tawhid-1es, annexe — notices
biographiques des figures citées).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire).

Notes :
- Annexe sans citations coraniques ni hadithiques — traduction directe.
- Les 12 notices concordent avec les identifications documentées au fil du
  livre : al-Ḍarīr = Abū l-Ḥajjāj Yūsuf b. Mūsā al-Kalbī, m. 520 H
  (découverte R89, leçon 19) ; Zarrūq (Sharḥ 1/61, 1/69 cités leçons 21-22) ;
  al-ʿAdawī (la ḥāshiya) ; al-Manūfī (l'auteur du commentaire Kifāya).
- Coquille imprimée : « التنوير في إسفاط التدبير » → le titre canonique est
  al-Tanwīr fī ISQĀṬ al-tadbīr (إسقاط) — corrigée et notée.
- OCR/artefacts : dl/dt/dd vides + <p> vides + écho du titre en queue + divs
  vides — artefacts non rendus.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Notices biographiques des figures citées dans le Livre du Tawḥīd, tiré de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan — première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>)</h1>
<p>Voici les notices biographiques (<em>tarājim</em>) des figures citées dans les leçons de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention de la première année de l’enseignement secondaire traditionnel.</p>
<ul>
<li>1. Abū l-Ḥasan ʿAlī b. Muḥammad al-Manūfī al-Miṣrī al-Shādhilī : il a six commentaires de la <em>Risāla</em>, dont le plus célèbre est <em>Kifāyat al-ṭālib al-rabbānī</em>, et d’autres œuvres. Mort en 939 H.</li>
<li>2. Al-ʿAdawī : Abū l-Ḥasan ʿAlī b. Aḥmad, connu comme al-Ṣaʿīdī, le malikite établi en Égypte. De nombreux ouvrages, parmi lesquels la <em>ḥāshiya</em> (glose) sur le commentaire d’Abū l-Ḥasan de la <em>Risāla</em>, une <em>ḥāshiya</em> sur l’<em>Alfiyya</em> d’al-ʿIrāqī, et d’autres encore. Mort en 1189 H.</li>
<li>3. Zarrūq : Aḥmad b. Muḥammad al-Burnusī al-Fāsī. Parmi ses œuvres les plus célèbres : <em>al-Naṣīḥa al-kāfiya li-man khawṣahu Allāh bi-l-ʿāfiya</em> et le commentaire de la <em>Risāla</em>. Mort en 899 H.</li>
<li>4. Le qāḍī ʿAbd al-Wahhāb : Abū Muḥammad [ʿAlī] b. ʿAlī b. Naṣr al-Baghdādī al-Mālikī — parmi les premiers commentateurs du tawḥīd de la <em>Risāla</em> du Qayrawānī. Mort en 422 H.</li>
<li>5. Al-Ṣāwī : Aḥmad b. Muḥammad al-Ṣāwī al-Khalwatī, Shihāb al-Dīn, le connaissant de Dieu (<em>ʿārif bi-Llāh</em>), modèle des itinérants. De nombreux ouvrages, parmi lesquels le commentaire de la <em>Jawharat al-tawḥīd</em> d’al-Laqānī. Mort en 1241 H.</li>
<li>6. Al-Ghazālī : la Preuve de l’islam (<em>Ḥujjat al-Islām</em>) Abū Ḥāmid Muḥammad b. Muḥammad al-Ṭūsī al-Ghazālī. Il composa beaucoup de livres en les diverses disciplines, parmi lesquels : <em>Iḥyāʾ ʿulūm al-dīn</em>, <em>Maqāṣid al-falāsifa</em>, <em>Tahāfut al-falāsifa</em>, <em>Bidāyat al-hidāya</em>, <em>Shifāʾ al-ghalīl</em>, <em>Tahdhīb al-uṣūl</em> et d’autres. Mort en 505 H.</li>
<li>7. Sufyān al-Thawrī : Abū ʿAbd Allāh Sufyān b. Saʿīd b. Masrūq b. Ḥabīb b. Rāfiʿ — né en 97 H à Kūfa, en Irak ; mort en 161 H, à soixante-trois ans. Imâm célèbre de la génération des suiveurs des Suivants (<em>atbāʿ al-tābiʿīn</em>), pris pour modèle.</li>
<li>8. Ibn ʿAṭāʾ Allāh al-Iskandarī : Tāj al-Dīn [b. ʿAṭāʾ Allāh] Abū l-ʿAbbās Aḥmad b. Muḥammad b. ʿAbd al-Karīm al-Judhamī al-Iskandarī — l’imâm soufi et théologien. De nombreux ouvrages, parmi lesquels : les <em>Ḥikam</em> [sentences] d’ʿAṭāʾ Allāh, <em>al-Tanwīr fī isqāṭ al-tadbīr</em> [la graphie imprimée porte <em>isfāṭ</em> pour <em>isqāṭ</em> — coquille corrigée], <em>Laṭāʾif al-minan</em> et d’autres. Mort en 709 H.</li>
<li>9. Al-Ḍarīr : Abū l-Ḥajjāj Yūsuf b. Mūsā al-Kalbī, surnommé al-Ḍarīr — originaire de Saragosse (<em>Saraqusṭa</em>), en al-Andalus, il résida à Marrakech. Son œuvre la plus célèbre : <em>al-Tanbīh wa-l-irshād fī ʿilm al-iʿtiqād</em>. Mort en 520 H. [C’est lui que vise le vers de la leçon dix-neuf — identification documentée : <em>al-Tanbīh wa-l-irshād</em>, p. 236.]</li>
<li>10. Abū l-Qāsim al-Qushayrī : l’ustādh ʿAbd al-Karīm b. Hawāzin b. ʿAbd al-Mālik al-Qushayrī al-Khurāsānī al-Naysābūrī — le shafiite, le soufi, le jurisconsulte, l’exégète, l’éducateur. Parmi ses œuvres : la <em>Risāla qushayriyya</em>, le <em>Tafsīr kabīr</em>, <em>Ādāb al-ṣūfiyya</em> et d’autres. Mort en 465 H.</li>
<li>11. Ibn ʿAsākir : Abū l-Qāsim al-Dimashqī, connu comme Ibn ʿAsākir — traditionniste (<em>ḥāfiẓ</em>) rigoureux. Parmi ses œuvres : le <em>Tārīkh Dimashq</em> et <em>Faḍāʾil aṣḥāb al-ḥadīth</em>. Mort en 565 H.</li>
<li>12. Ibn ʿAṭiyya : l’imâm, le qāḍī Abū Muḥammad ʿAbd al-Ḥaqq b. Ghālib b. ʿAbd al-Raḥmān b. ʿAṭiyya al-Maḥāribī, de Grenade. De nombreux ouvrages, dont le plus célèbre : <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em>. Mort en 542 H.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16805":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16805 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16805 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
