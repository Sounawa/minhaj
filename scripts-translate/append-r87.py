#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Append gardé R87 au worklog.md (GARDE-DOUBLON : Task ID = dernier + 1)."""
import re
import sys

WL = "/home/z/my-project/worklog.md"
NEW_ID = 87

ENTRY = """
---
Task ID: R87
Agent: Z.ai Code (agent principal — TOUR DE PRODUCTION AUTONOME cron 490824, trace 1a192862dcae2069-cron-agent-loop-202611010606)
Task: 9ᵉ exécution consécutive du canal (0253→0606) — tour de production sur la priorité R86 : hadith-1es leçons savantes 25-26 (13001, 13002) — viser DEUX leçons par tour (charge 490824) + QA navigateur + backup + worklog.

Work Log:
- **Canal / moteur** : TICK 0606 consigné dans tr-tmp/cron-alive.log ; superviseur v4 VIVANT (PID 1359) — pas de relance nécessaire.
- **Vérification physique de la charge (règle établie R85)** : le payload 490824 cite isra-map.py / verify-711-712 / append-r460.py / GARDE-DOUBLON.md / SOLUTION-OUVRAGES.md — VÉRITÉ TERRAIN : AUCUN n'existe dans scripts-translate/ (seul hand-set.py existe) ; fantômes récurrents du payload, ignorés conformément au constat R85/R86. La priorité réelle lue au tail (R86) : hadith-1es 25-28 — ce tour les deux premières (viser DEUX leçons).
- **savant(hadith-1es/13001)** — leçon 25 l'encouragement à la prière du tarāwīḥ : 301 (ʿĀʾisha : le Prophète pria une nuit au Ramaḍān, les gens grandirent, il ne sortit ni la 3ᵉ ni la 4ᵉ — « j'ai craint qu'il vous soit imposé »), 303 (ʿUmar réunit les gens derrière Ubayy ibn Kaʿb : « quelle bonne innovation que celle-ci », « ce dont vous dormez est meilleur que ce que vous veillez »). Analyse : étymologie tarwīḥa (repos entre chaque deux taslīms) ; origine légale du tarāwīḥ — Ibn Baṭṭāl : le qiyām était fard sur lui sans sa communauté, crainte d'égaliser le statut ; récompense 302 (qiām du Ramaḍān, īmānan wa-iḥtisāban : péchés passés pardonnés — jumhūr : mineurs vs Ibn al-Mundhir : les deux, al-Ḥāfiẓ : lettre apparente) ; animation par ʿUmar en l'an 14 (choix d'Ubayy : « prie avec les gens leur plus lettré » ; ʿAlī aqḍā-nā / Ubayy aqrāʾ-nā ; « n'a institué que ce que le Prophète a agréé » — Tirmidhī : imitez Abū Bakr et ʿUmar, sunna des califes bien guidés ; l'accord des Compagnons ôte le nom de bidʿa) ; nombre de rakʿa : 317 (11 rakʿa, Ramaḍān et hors Ramaḍān), 304 (ʿUmar ordonne à Ubayy et Tamīm al-Dārī onze), 305 (vingt-trois au temps de ʿUmar — al-Bājī : allonger d'abord la récitation puis l'alléger, multiplier les rakʿa), 306 (la Baqara en huit rakʿa ; en douze les gens trouvent qu'il a allégé) ; pas de limite à la récitation (« celui qui prie avec les gens, qu'il allège » ; Muʿādh au Yémen — Abū ʿUmar : cela pour les obligations, comment pour les surérogatoires ?). Exploitation 313 (ʿUmar réveille sa famille : « la prière, la prière ! ») + verset-image Ṭāhā (20) : 131 rendu. NOTE : la source écrit « الرقم : .305 » avec point parasite et nbsp — le croisage src↔final a été normalisé (crosscheck-r86.py étendu aux 6 leçons). QA 0 arabe, 20 guillemets.
- **savant(hadith-1es/13002)** — leçon 26 ce qui est venu sur la prière de la nuit, le witr et le fajr : 309 (celui que le sommeil emporte : récompense inscrite, son sommeil = aumône), 316 (onze rakʿa, witr par une, se couche sur le flanc droit), 321 (deux par deux ; une seule rend impair), 338 (2 rakʿa légères entre l'adhan et l'iqaqāma du ṣubḥ). Analyse : vertu de la prière de nuit (Ibn Abī Shayba : que Dieu fasse miséricorde à l'homme/la femme qui réveille sa famille) ; al-Bājī : 2 manières du sommeil emportant ; Ibn ʿAbd al-Barr : l'intention reçoit comme celui qui œuvre si l'obstacle est sommeil/oubli venu de Dieu (magnanimité de la Loi : 311 « qu'il dorme jusqu'à ce que le sommeil passe » + 312 « imposez-vous de l'acte ce dont vous avez la capacité ») ; witr — aqad des sunans (Abū Ḥanīfa : wājib proche du fard ; « le witr est un droit » Abū Dāwūd ; « Dieu est impair, Il aime l'impair » Sunan), 316 vs les compagnons d'Ibn Shihāb (couchage après les 2 rakʿa du fajr — Ibn ʿAbd al-Barr préfère la version du Muwaṭṭaʾ pour la place de Mālik, sa mémoire et sa maîtrise du hadith de son shaykh), 326 (witr avant de dormir ou retardé selon l'espérance de se réveiller), 331 (witr au début puis se lève : prie deux par deux) ; rattrapage du witr : 332 (Ibn ʿAbbās, aveugle, witr après le ṣubḥ manqué), 333 (Ibn ʿAbbās/ʿUbāda/al-Qāsim/Ibn ʿĀmir ibn Rabīʿa), 337 (Mālik : seulement celui qui a dormi sur son witr, jamais délibéré) ; fajr — rughbatā al-fajr, rang après le witr (Bukhārī/Muslim : plus ferme engagement), 339 (allège tant que ʿĀʾisha dit « a-t-il récité l'Umm al-Qurʾān ou pas ? » — al-Qurṭubī : comparaison aux autres prières ; Mālik : Fātiḥa seule vs jumhūr : al-Kāfirūn et al-Ikhlāṣ d'après Muslim) ; pas de nāfila quand la prescrite est établie (« pas de prière sinon la prescrite » ; 340 « deux prières ensemble ? » = désapprobation et blâme) ; rattrapage 341 (Ibn ʿUmar après le lever du soleil — preuve de l'aqad ; al-Shāfiʿī/ʿAṭāʾ/ʿAmr ibn Dīnār : après le salām de l'imam ; Mālik et la plupart refusent, pour l'interdiction de prier après le ṣubḥ). Exploitation 319 (Ibn ʿAbbās chez Maymūna : wuḍūʾ bien fait, Āl ʿImrān, 6×2 puis witr, 2 rakʿa légères à la venue du muʾadhdhin). Versets-image al-Dhāriyāt (51) : 17 + al-Isrāʾ (17) : 79 rendus (préambule). QA 0 arabe, 27 guillemets.
- **Outils du tour** : extraction inline (13001/13002), verify-r87-quran.py (labels ATTENDU : Ṭāhā 20:131 pour 13001 ; al-Dhāriyāt 51:17 + al-Isrāʾ 17:79 pour 13002 — PASS ×2), crosscheck-r86.py étendu aux 6 leçons + normalisation nbsp/point parasite (6× OK, 41 références Muwaṭṭaʾ cumulées), injection inline (htmlFr ×2 + titleFr corrigés + registre hand). qa-lesson.py PASS ×2 (auto-fix NNBSP appliqué).
- **QA navigateur (agent-browser)** : 13001 mobile 390 (h1 corrigé rendu, 105 blocs, 0 overflow), 13002 desktop 1280 (118 blocs, 0 overflow, les 2 versets-image rendus) — captures tr-tmp/qa-R87-13001-390.png, qa-R87-13002-1280.png.
- **Git** : git fetch origin ÉCHOUE — aucun remote configuré sur ce sandbox (constat R83-R86 inchangé, push impossible sans token) ; commits locaux : 6c43579 (13001), 96b5c61 (13002), chacun incluant book JSON + registre + tr-tmp (src/gt/final) + capture QA ; backup.sh PASS (96b5c61).

Stage Summary:
- **État** : registre **525/950** (+2 ce tour) — hadith-1es **27/32 savant** (intro + leçons 1-26). 48 livres complets. Corpus global côté GT inchangé.
- **Décisions clés** : (a) la charge cron 490824 contient 5 références fantômes (isra-map.py, verify-711-712, append-r460.py, GARDE-DOUBLON.md, SOLUTION-OUVRAGES.md) — vérifiées physiquement et ignorées ; le tail réel du worklog (R86) a dicté la priorité, conformément à la règle établie ; (b) crosscheck-r86.py généralisé : normalisation des nbsp et points parasites de la source (le « .305 » de 13001) et contrôle désormais étendu à toutes les leçons du corpus récent (41 références Muwaṭṭaʾ OK) ; (c) titleFr GT corrigés ×2 (« Encouragement à prier pendant le Ramadan » = GT-isme ; le h1 réel = الترغيب في صلاة التراويح) ; (d) 3 versets-image ancrés au cache coranique et rendus en français (Ṭāhā 20:131, al-Dhāriyāt 51:17, al-Isrāʾ 17:79).
- **Risques** : (a) push GitHub toujours sans token (dépôt à R74, ~53 commits d'avance locale) ; (b) 13001 : la question de l'évaluation n° 2 demande un texte coranique « convenable » en soutien à la compassion prophétique — laissé au lecteur (pas de verset-image dans le CMS pour ce point) ; (c) 13002 : la citation d'Ibn ʿAddī (chaîne bonne : « pas même les deux rakʿa du fajr ? ») mériterait un cross-check Zubdā/Ḥāwi sur l'attribution exacte.
- **Priorités suivantes** : (1) hadith-1es leçons savantes 27-28 : 13004 (la vertu de la prière en groupe), 13005 (les dispositions propres à l'imam et à ceux qui prient derrière lui) [titres GT-ismes à corriger au tour] ; (2) relecture croisée des labels de versets du CMS sur le PDF du manuel (Wāqiʿa 77, Muḥammad 34, Jumuʿa 9, Ṭāhā 131) ; (3) tour dédié faraid-tanawi-3 manẓūma (310-313).
"""

def main() -> None:
    with open(WL, encoding="utf-8") as f:
        text = f.read()
    ids = [int(m) for m in re.findall(r"^Task ID: R(\d+)", text, re.M)]
    last = max(ids) if ids else 0
    if NEW_ID != last + 1:
        sys.exit(f"✗ GARDE-DOUBLON : dernier Task ID R{last}, refusé d'apposer R{NEW_ID}")
    with open(WL, "a", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"✓ R{NEW_ID} apposé (dernier vérifié : R{last}) — {len(ENTRY)} car")


if __name__ == "__main__":
    main()
