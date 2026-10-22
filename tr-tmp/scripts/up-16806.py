#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16806 (tawhid-1es, annexe — sources et
références).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire).

Notes :
- Annexe bibliographique — traduction directe, conventions bibliographiques
  conservées (éditeur, édition, date).
- CLÉ DOCTRINALE : l'entrée 1 déclare le muṣḥaf de référence du manuel :
  « le Noble Coran, transmission de Warsh ʿan Nāfiʿ, selon le décompte du
  muṣḥaf » — ce qui explique les écarts de numérotation des versets sur
  certaines pages du manuel (muṣḥaf maghrébin), documentés au fil des
  leçons (Ṭā-Hā +3, Fajr −2, Zumur 39→42...) alors que les textes cités
  suivent la leçon Ḥafṣ du cache : l'hétérogénéité est page par page.
- « إسفاط » corrigé en إسقاط dans 16805 (même coquille d'atelier) ; ici
  « ابن سورة » imprimé pour ابن سَوْرة (al-Tirmidhī) — rendu canonique.
- OCR/artefacts : dl/dt/dd vides + <p> vides + écho du titre en queue + divs
  vides — artefacts non rendus.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Sources et références du Livre du Tawḥīd, tiré de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan — première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>)</h1>
<p>Voici les sources et références employées dans les leçons de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention de la première année de l’enseignement secondaire traditionnel.</p>
<ul>
<li>1. Le Noble Coran, transmission de Warsh ʿan Nāfiʿ, selon le décompte du muṣḥaf. [Note : le muṣḥaf de référence déclaré du manuel est le muṣḥaf maghrébin (Warsh) — d’où les écarts de numérotation des versets sur certaines pages du manuel, par rapport au décompte Ḥafṣ, documentés au fil des leçons ; les textes cités suivent quant à eux la leçon du corpus.]</li>
<li>2. <em>Īḍāʾat al-dujna fī iʿtiqād ahl al-sunna</em>, d’Aḥmad al-Maqqarī al-Tilimsānī — Dār al-Fikr, sans date.</li>
<li>3. <em>Tafsīr Ibn Kathīr</em>, d’Abū l-Fidāʾ Ismāʿīl b. Kathīr al-Dimashqī — Dār Ṭayba, 2ᵉ éd., 1420 H/1999.</li>
<li>4. <em>Al-Tanbīh wa-l-irshād fī ʿilm al-iʿtiqād</em>, d’Abū l-Ḥajjāj Yūsuf al-Ḍarīr — édition du Ministère des Habous et des Affaires islamiques (Royaume du Maroc), 1ʳᵉ éd., 1437 H ; Maktabat al-Raḥma al-Muhdāt, Égypte.</li>
<li>5. <em>Al-Jāmiʿ li-aḥkām al-Qurʾān</em>, d’al-Qurṭubī — Dār al-Kutub al-ʿIlmiyya, Beyrouth.</li>
<li>6. <em>Jawharat al-tawḥīd</em>, d’Ibrāhīm al-Laqānī, avec le commentaire <em>Hidāyat al-murīd</em> de l’auteur — Maktabat al-Maʿārif, éd. 1432/1 H.</li>
<li>7. <em>La ḥāshiya d’al-ʿAdawī sur le commentaire d’Abū l-Ḥasan de la Risāla</em>, intitulé <em>Kifāyat al-ṭālib al-rabbānī</em> [commentaire] de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī — édition Dār al-Fikr.</li>
<li>8. <em>Ḥilyat al-awliyāʾ wa-ṭabaqāt al-aṣfiyāʾ</em>, d’Abū Nuʿaym — Dār al-Kutub al-ʿIlmiyya, Beyrouth, éd. 1409 H.</li>
<li>9. <em>Al-Rāʾid fī ʿilm al-ʿaqāʾid</em>, d’al-ʿArabī al-Lawh — éd. Krimadis, Larache-Tétouan, 1974.</li>
<li>10. <em>Sunan d’Abū Dāwūd</em>, du ḥāfiẓ Sulaymān b. al-Ashʿath al-Sijistānī — édition critique de Muḥammad Muḥyī l-Dīn ʿAbd al-Ḥamīd, al-Maktaba al-ʿAṣriyya, Beyrouth.</li>
<li>11. <em>Sunan al-Tirmidhī</em>, d’Abū ʿĪsā Muḥammad b. ʿĪsā b. Sawra al-Tirmidhī — édition et correction de ʿAbd al-Wahhāb ʿAbd al-Laṭīf, Dār al-Fikr.</li>
<li>12. <em>Al-Sunan al-kubrā</em>, d’Abū Bakr Aḥmad b. al-Ḥusayn [al-Bayhaqī] — Dāʾirat al-Maʿārif, 1ʳᵉ éd., 1344 H.</li>
<li>13. <em>Le commentaire de l’illustre Aḥmad b. Muḥammad al-Burnusī al-Fāsī — connu comme Zarrūq — sur la Risāla d’Ibn Abī Zayd al-Qayrawānī</em> — Dār al-Fikr, 1410 H/1982.</li>
<li>14. <em>Le commentaire de l’illustre Qāsim b. ʿĪsā al-Tanūkhī sur le matn de la Risāla</em> — Dār al-Fikr, sans date.</li>
<li>15. <em>Ṣaḥīḥ Ibn Ḥibbān</em>, ordonné par Ibn Balbān, d’Abū Ḥātim Muḥammad b. Ḥibbān b. Aḥmad al-Tamīmī al-Bustī — édition critique de Shuʿayb al-Arnaʾūṭ, Muʾassasat al-Risāla.</li>
<li>16. <em>Ṣaḥīḥ d’al-Bukhārī</em>, d’Abū ʿAbd Allāh Muḥammad b. Ismāʿīl al-Bukhārī — Dār Ibn Kathīr, 3ᵉ éd., 1407 H/1987.</li>
<li>17. <em>Ṣaḥīḥ Muslim</em>, d’Abū l-Ḥusayn Muslim b. al-Ḥajjāj al-Qushayrī — édition critique de Muḥammad Fuʾād ʿAbd al-Bāqī, Dār Iḥyāʾ al-Turāth al-ʿArabī, Beyrouth.</li>
<li>18. <em>Kifāyat al-ṭālib al-rabbānī</em> sur la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī, d’Abū l-Ḥasan al-Mālikī.</li>
<li>19. <em>Lisān al-ʿArab</em>, d’Ibn Manẓūr.</li>
<li>20. <em>Al-Muḥarrar al-wajīz</em>, d’Ibn ʿAṭiyya — édition du Ministère des Habous et des Affaires islamiques, 1395 H/1975.</li>
<li>21. <em>Mukhtaṣar al-durr al-thamīn wa-l-mawrid al-maʿīn</em>, du shaykh Miyāra, sur <em>al-Murshid al-maʿīn</em> d’ʿAbd al-Wāḥid b. ʿĀshir — édition du Ministère des Habous et des Affaires islamiques, Royaume du Maroc.</li>
<li>22. <em>Al-Mustadrak ʿalā l-ṣaḥīḥayn</em>, d’Abū ʿAbd Allāh Muḥammad b. ʿAbd Allāh al-Ḥākim al-Naysābūrī — Dār al-Kutub al-ʿIlmiyya, Beyrouth, 1ʳᵉ éd., 1411 H.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16806":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16806 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16806 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
