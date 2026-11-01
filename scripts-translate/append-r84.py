#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Append gardé R84 au worklog.md (GARDE-DOUBLON : Task ID = dernier + 1)."""
import re
import sys

WL = "/home/z/my-project/worklog.md"
NEW_ID = 84

ENTRY = """
---
Task ID: R84
Agent: Z.ai Code (agent principal — TOUR DE PRODUCTION AUTONOME cron 490480, trace 1a192862dcae2069-cron-agent-loop-202611010514)
Task: 6ᵉ exécution consécutive du canal (0253→0514) — RÉVISION FORMELLE du jugement R457 + tour de production sur la priorité R83 : hadith-1es leçons savantes 13-16 (12929, 12945, 12948, 12953) + QA navigateur + backup + worklog.

Work Log:
- **Canal / moteur** : TICK 0514 consigné + RECTIFICATION consignée dans tr-tmp/cron-alive.log ; superviseur v4 VIVANT (PID 1359) — pas de relance nécessaire.
- **RÉVISION FORMELLE du jugement R457** : R457 disait « ce canal cron-plateforme DÉCLENCHE mais n'EXÉCUTE pas les payloads ». VÉRITÉ ÉTABLIE : 6 exécutions consécutives (traces 0253, 0322, 0407, 0452, 0506, 0514), chacune suivie d'un tour réel consigné (R82, R83, R84). Le canal témoin déclenche ET exécute — R457 est officiellement abrogé ; l'architecture « canal = témoin passif » n'a plus de raison d'être.
- **Recadrage GARDE-DOUBLON (2ᵉ occurrence)** : la mémoire compressée de ce tour affirmait R465 / tafsir-5ep leçons 717-718 / outils isra-*, verify-716, commit 17226d5 — VÉRITÉ TERRAIN : AUCUN de ces objets n'existe (17226d5 inconnu de git, pas d'isra-*.py, dernier Task ID réel R83). Même univers fantôme que celui documenté à R82 (récidive exacte). Leçon consignée : après compression, vérifier l'EXISTENCE PHYSIQUE des outils et commits cités (git cat-file / ls) avant de suivre le résumé — le tail réel du worklog fait foi.
- **savant(hadith-1es/12929)** — leçon 13 dispositions de l'appel à la prière : 174 (songe d'Ibn Zayd, deux pièces de bois → ordre de l'adhān), 179 (le diable tourne le dos et laisse échapper un ḍurāṭ, s'insinue entre l'homme et son âme), 182 (adhān doublé, iqāma simple, lever selon la capacité) ; statut (obligation aux mosquées de congrégation — 183 ; Zarqānī : sunnas confirmées ; 2 avis tardifs kifāya), vertus (protection du diable, témoignage des jinn et hommes, heures d'exaucement 180), manière (shafʿ/watr — Bukhārī Bilāl, Zayn ibn al-Munīr : takbīr non quadruple, Ibn ʿAbd al-Barr : 2× initial), lever à l'iqāma (capacité / achèvement / qad qāmat-Anas) ; lexique 4 entrées (naqūs, ḍurāṭ, thūbba, yaḫṭur double lecture) ; versets-image Jumuʿa 9 + Māʾida 60 rendus ; exploitation 181 + 188 (ʿUmar « la prière est meilleure que le sommeil »). QA 0 arabe, 19 guillemets.
- **savant(hadith-1es/12945)** — leçon 14 l'appel en voyage : 193 (ʿUrwa→Hishām, adhān+iqāma au choix), 194 (appel monté), 193 encore (nuit froide, « venons prier dans vos campements ») — NOTE : n° 193 porté 2× par le CMS (tel quel) ; statut (Ibn al-Qāsim : miṣr seul, voyageur dispensé ; Ashhab : délibéré → refaire ; prévalent : la prière suffit), posture (monté permis, iqāma du monté 2 récits ; assis désapprouvé — Mudawwana vs Abū l-Faraj, « Ô Bilāl lève-toi » : Nawawī vs Ibn al-Mundhir/Ibn Khuzayma/ʿIyāḍ), abandon de la jamaʿa (pluie+vent, ʿilla de la peine ; Bukhārī : restriction au voyage + report absolu→restreint ; Abī ʿAwāna : 3 excuses ; Mālikites/Shāfiʿites : vent de nuit seulement) ; exploitation Salmān (rangs d'anges, Bayhaqī). QA 0 arabe, 13 guillemets.
- **savant(hadith-1es/12948)** — leçon 15 dispositions de l'ouverture de la prière : 198 (mains au niveau des épaules, entrée + relevé du rukūʿ, rien au sujūd), 206 (oubli de la takbīr d'entrée : recommencer aimé, dispense si intention) ; statut de l'élévation (recommandé — jumhūr ; obligation Awzāʿī/Ḥumaydī/Ibn Khuzayma/Dāwūd — « anomalie et erreur » Ibn ʿAbd al-Barr ; consensus sur la permission), manière 3 questions (épaules/poitrine/oreilles — tarjīḥ d'isnad + jamʿ paumes-épaules/doigts-oreilles ; mains dressées vs Sahnūn tendues ; simultané + variantes), sagesse (sourd voit/aveugle entend, Qurṭubī, Ibn ʿAbd al-Barr), rukūʿ (Ibn al-Qāsim/Ḥanīfa non vs Abū Muṣʿab/Ibn Waḥb/Ashhab oui, Aṣīlī : mawqūf), sujūd (rien ni descente ni relevé — corroborations ʿAlī/Abū Ḥumayd), māʾmūm oublieux (2 récits : recommencer / continuer-refaire — prière divergée Ibn Shihāb vs Rabīʿa ; préférable : réunir). NOTE : rubrique CMS « رابعا » imbriquée sous ثالثا (tel quel) ; Muḥammad 34 rendu comme imprimé. QA 0 arabe, 21 guillemets.
- **savant(hadith-1es/12953)** — leçon 16 la récitation dans la prière : 211 (Ṣunābiḥī : Abū Bakr maghrib Fātiḥa + courtes du mufaṣṣal, 3e rakʿa + Āl ʿImrān 8), 212 (Ibn ʿUmar : sūra chaque rakʿa seul), 213 (ʿishāʾ al-Tīn), 220 (Abū Bakr : al-Baqara ×2 à l'aube), 223 (voyage : dix premières du mufaṣṣal) ; maghrib (courtes/al-Ṭūr/al-Mursalāt/ṭūlay al-ṭūlayn — Aʿrāf + Māʾida/Anʿām/Yūnus ; réunion : divergence permise Ibn Khuzayma), ʿishāʾ (Inshiqāq en résidence, Tīn en voyage), aube (ʿUmar Yūsuf+Ḥajj 221, ʿUthmān Yūsuf répétée 222 ; marfūʿ : Ṭūr-Bukhārī/Qāf-Muslim ; allègement dû aujourd'hui + « fauteur de trouble » Muʿādh), ẓuhr/ʿaṣr (Abū Qatāda : deux sūras aux premières, Fātiḥa seule aux dernières — Ibn ʿUmar seul non suivi) ; exploitation Ibn ʿAbd al-Barr (mubāḥ, pas de temps fixé après la Fātiḥa — consensus, Zarqānī 1/306) ; versets-image Āl ʿImrān 8 + Insān 6 + Ṭūr 33-35 + Mursalāt 1 + Inshiqāq 1 rendus. QA 0 arabe, 28 guillemets.
- **QA navigateur (agent-browser)** : 12929 desktop 1280 (h1 ok, 118 blocs, 0 overflow, 0 erreur), 12953 mobile 390 (h1 ok, 0 overflow), 12948 mobile 390 (h1 ok, 0 overflow), 12945 desktop 1280 (h1 ok, 0 overflow) — captures tr-tmp/qa-R84-12929-1280.png, qa-R84-12953-390.png, qa-R84-12948-390.png, qa-R84-12945-1280.png. Le badge « Traduction savante » s'affiche sur les 4 (registre lu par le lecteur).
- **Git** : aucun remote sur ce sandbox (constat R83 inchangé) — commits locaux + backup.sh ; commits : 49f6aa9 (12929), a0671c8 (12945), 0acafa6 (12948), 95177e3 (12953), chacun incluant book JSON + registre + tr-tmp (src/gt/savant).

Stage Summary:
- **État** : registre **515/950** (+4 ce tour) — hadith-1es **17/32 savant** (intro + leçons 1-16 ; le rythme 4/tour tient). 48 livres complets. Corpus global côté GT inchangé.
- **Décisions clés** : (a) R457 abrogé formellement (6 exécutions consécutives du canal) ; (b) récidive d'univers fantôme post-compression (R465/tafsir-717+718) — la règle de recadrage physique est confirmée indispensable ; (c) titleFr GT corrigés : 12948 « prière d'ouverture » → « ouverture de la prière », 12953 « Lire dans la prière » → « La récitation dans la prière », 12945 harmonisé « Dispositions de l'appel… en voyage » ; (d) quirks CMS rendus tel quel (n° 193 ×2, رابعا imbriqué, Muḥammad 34) et consignés aux commits.
- **Risques** : (a) push GitHub toujours sans token (dépôt à R74, ~44 commits d'avance locale) ; (b) bracket des versets-image reconstitué d'après le label CMS — le lien Zarqānī « Muḥammad 34 » (12948, pour la prière divergée) mérite une relecture croisée sur le PDF du manuel ; (c) le badge lecteur compte l'intro (leçon 16 du CMS = 17/32 côté lecteur) — convention de comptage à garder en tête pour les cross-checks.
- **Priorités suivantes** : (1) hadith-1es leçons savantes 17-20 : 12958 (العمل في القراءة في الصلاة), 12961 (فضل الفاتحة وحكم قراءتها), 12980 (التأمين والتحميد في الصلاة), 12985 (العمل في الجلوس والتشهد) ; (2) relecture croisée des numéros Muwaṭṭaʾ et des labels de versets du CMS sur le PDF du manuel (12948 Muḥammad 34 en tête) ; (3) tour dédié faraid-tanawi-3 manẓūma (310-313).
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
