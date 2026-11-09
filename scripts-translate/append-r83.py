#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Append guardé R83 au worklog.md (GARDE-DOUBLON : Task ID = dernier + 1)."""
import re, sys

WL = "/home/z/my-project/worklog.md"
NEW_ID = 83

def main() -> None:
    with open(WL, encoding="utf-8") as f:
        text = f.read()
    ids = [int(m) for m in re.findall(r"^Task ID: R(\d+)", text, re.M)]
    last = max(ids) if ids else 0
    if NEW_ID != last + 1:
        sys.exit(f"✗ GARDE-DOUBLON : dernier Task ID R{last}, refusé d'apposer R{NEW_ID}")
    entry = """
---
Task ID: R83
Agent: Z.ai Code (agent principal — TOUR DE PRODUCTION AUTONOME cron 490824, trace 1a192862dcae2069-cron-agent-loop-202611010506)
Task: 5ᵉ exécution consécutive du canal (0253→0506) — tour de production sur la priorité R82 : hadith-1es leçons savantes 9-12 (12901, 12908, 12911, 12924) + correction du pattern CMS « Baqara 220 » + QA navigateur + fetch/push + backup + worklog.

Work Log:
- **Canal / moteur** : trace 0506 consignée dans tr-tmp/cron-alive.log ; superviseur v4 VIVANT (PID 1359) — pas de relance nécessaire.
- **savant(hadith-1es/12901)** — leçon 9 l'une des décisions sur l'impureté (من أحكام الجنابة) : Muwaṭṭaʾ 120 (ʿUmar : ablutions + lave l'organe puis dors), 122 (Ibn ʿUmar mange/dort), 123 (ʿAṭāʾ ibn Yasār : takbīr, trace d'eau), 129 (Umm Sulaym/ʿĀʾisha, taribat yamīnuki = réprobation) ; ablutions de sommeil (wāw non ordonnée, version Abū Nūḥ taqdīm-taʾkhīr ; comme celle de la prière mais pour le sommeil — 121 ; fadaʿ Ibn ʿUmar ; jumhūr istḥbāb), sagesse (moitié du ghusl — Shaddād ibn Aws/Ibn Abī Shayba ; dormir sur l'une des deux purités — Tabarānī Maymūna bint Saʿd « que Gabriel ne soit pas présent »), rajaz du versificateur rendu (n'annule pas sauf reprise de l'union), prié par oubli → reprend (124 Zuyayd ibn al-Ṣalt/ʿUmar al-Juruf, duḥā), manī najis → ghusl (126 wadak) + naḍḥ du doute (127 ʿAmr ibn al-ʿĀṣ), iḥtilām de la femme = ghusl par iṣāl seulement (130), eau laissée par un autre (131 + ʿĀʾisha un récipient tawātur), doigt dans l'eau (135), sueur du mutajanbid pure (Abū Hurayra « le croyant ne souille pas ») ; NOTE : liste d'objectifs CMS réduite à une référence (Riyāḍ al-Ṣāliḥīn) rendue comme imprimée ; n° 135 porté 2× par le CMS (tel quel). QA 0 arabe, 16 guillemets.
- **savant(hadith-1es/12908)** — leçon 10 dispositions du tayammum : 136 (collier de ʿĀʾisha, Usayd ibn Ḥuḍayr), 144, 145 (Musayyab : ghusl pour l'à-venir), 146 (lave l'organe + tayammum) ; verset du tayammum (Qurṭubī Nisāʾ 43 vs Ibn Ḥajar/Bukhārī Māʾida sans hésitation), une seule fard par tayammum (nāfila/janāza suivent — 137, tayammum mubīḥ), imamat mutayammim makrūh jāʾiz (138 + ʿAmr ibn al-ʿĀṣ Dhāt al-Salāsil, Nisāʾ 29), prière commencée puis eau → on achève (139, parallèle ẓihār Shāfiʿī+Dāwūd vs Ḥanīfa+Aḥmad, maʿāda excuse-mois), mutayammim pur (Māʾida 7), 2 frappes (1 fard + 1 sunna, 143 Ibn ʿUmar coudes), ʿAmmār Ṣaḥīḥayn (acte+parole, non-mentionné ≠ fard), istithmār 140 (obéissance égale)/141 (ḥizb+nāfil)/sebkha (tout ṣaʿīd). Versets-image : Māʾida 7 ×3 + Nisāʾ 43 + Nisāʾ 29. QA 0 arabe, 18 guillemets.
- **savant(hadith-1es/12911)** — leçon 11 les règles des menstrues et des métrorragies : 148 (izār + couvrir par-dessus), 152 (darg/kursuf/qassa blanche), 160 (décompte des jours, ceinture) ; ḥayḍ (fond de l'utérus — Azharī/Harawī) vs istiḥāḍa (veine du bas), jaufūf < qassa (présence > absence), permis de la menstruée (ijmāʿ interdiction de l'union, nombril-genou — jumhūr + 3 imams, Ṣaḥīḥayn izzār « qui de vous maîtrise son organe ? »), femme enceinte (2 madhhab : mashhūr Mālik oui par consensus-silence vs Ḥanīfa/Aḥmad/Thawrī non — istibrāʾ ; le rare ne s'oppose pas au prédominant), muṣtaḥāḍa : prie (159 Faṭima bint Abī Ḥubaysh « ce n'est qu'une veine »), 1 ghusl + wuḍūʾ par prière (163, jumhūr wujūb/Mālik istḥbāb), union permise après la prière (164 + Bukhārī Ibn ʿAbbās) ; istithmār 158 (Asmāʾ : frotter-asperger-prier) + 153 (lumières de nuit désapprouvées). Lexique 7 entrées. QA 0 arabe, 15 guillemets.
- **savant(hadith-1es/12924)** — leçon 12 dispositions pour l'urine des garçons et des adultes : 167 (Umm Qays : nourrisson, naḍḥ sans lavage), 169 (Ibn ʿUmar debout), 170 (laver l'organe) ; urine du garçonnet/fillette 2 madhhab (gusl mashhūr — qiyās + réponse naḍḍa=gusl, hadith ʿOmān Bayhaqī ; naḍḥ suffisant — Awzāʿī, Ibn al-ʿArabī cavités vierges) ; urination debout (permis Ibn ʿUmar/Zayd/Musayyab/Sīrīn/Nakhaʿī/Aḥmad ; tanzīh ; Mālik éparpillement — Ḥudhayfa subāṭa Ṣaḥīḥayn, naskh prétendu Abū ʿAwāna/Ibn Shāhīn réfuté : ʿĀʾisha s'appuie sur son savoir, Ḥudhayfa Médine, ʿUmar/ʿAlī/Zayd debout) ; gusl préféré à istijmār/istibrāʾ (Qubāʾ) — RESTAURATION doctrinale : le CMS imprime ENCORE « Baqara 220 » (2ᵉ occurrence du pattern, après 12884) → resta 2:222 (fīhim rijālun yuḥibbūna an yataṭahharū), label CMS systématiquement 220 — convention consignée au commit 8386dbf ; istithmār 168 (bédouin « laissez-le » + dhanūb d'eau). Le bloc-date CMS (lundi 25 mars 2019 dans le dd) est un métadonnée éditoriale, non reproduit. QA 0 arabe, 9 guillemets.
- **QA navigateur (agent-browser)** : 12908 desktop 1280 (52 blocs, 1 lexique, 0 erreur), 12901 mobile 390 (0 overflow), 12924 mobile 390 (0 overflow, 0 erreur), 12911 (h1 + 0 overflow) — captures tr-tmp/qa-R83-12908-1280.png, qa-R83-12901-390.png, qa-R83-12924-390.png.
- **Git** : fetch origin ÉCHOUE — aucun remote configuré sur ce sandbox (« fatal : 'origin' does not appear to be a git repository ») : le push/fetch exige une session avec remote+token ; dépôt Sounawa/minhaj toujours à R74 d'après le worklog, ~40 commits d'avance locale ; rev-list bidirectionnel non calculable ; commits locaux + backup.sh après chaque doc.
- Commits : eb6b254 (12901), e0de9e5 (12908), bf5c362 (12911), 8386dbf (12924) + backup.sh.

Stage Summary:
- **État** : registre **511/950** (+4 ce tour) — hadith-1es **13/32 savant** (intro + leçons 1-12 ; le rythme 4-5/tour tient). 48 livres complets. Corpus global côté GT inchangé.
- **Décisions clés** : (a) CONFIRMATION du pattern CMS « al-Baqara, āya 220 » pour le verset des purifiés — 2 occurrences indépendantes (12884, 12924) → restauration 2:222 systématisée et documentée aux commits bb12c27 + 8386dbf ; (b) liste d'objectifs CMS parfois corrompue (12901 : une référence de livre) — rendue comme imprimée, source autorité ; (c) bloc-date éditorial dans le dd de 12924 (25 mars 2019) non reproduit dans le corps.
- **Risques** : (a) push GitHub toujours sans token (dépôt à R74) ; (b) le rajaz de 12901 rendu en prose rythmée — une relecture métrique serait idéale ; (c) hadith ʿOmān (12901) rapporté par le CMS « Bihaqī » : formulation de Dārimī/Bayhaqī à relecture croisée.
- **Priorités suivantes** : (1) hadith-1es leçons savantes 13-16 : 12929 (أحكام النداء للصلاة), 12945 (النداء في السفر), 12948 (أحكام افتتاح الصلاة), 12953 (القراءة في الصلاة) ; (2) révision formelle du jugement R457 dans le worklog (5 exécutions consécutives du canal) ; (3) relecture croisée des numéros Muwaṭṭaʾ du CMS sur le PDF du manuel ; (4) tour dédié faraid-tanawi-3 manẓūma (310-313).
"""
    with open(WL, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"✓ R{NEW_ID} apposé (dernier vérifié : R{last}) — {len(entry)} car")

if __name__ == "__main__":
    main()
