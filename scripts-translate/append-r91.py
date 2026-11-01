#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R91 — Append de l'entrée worklog du tour (relecture croisée des labels de versets)."""

ENTRY = """\
---
Task ID: R91
Agent: Z.ai Code (agent principal — TOUR DE PRODUCTION AUTONOME cron 490480, trace 1a192862dcae2069-cron-agent-loop-202611010657)
Task: 13ᵉ exécution consécutive du canal (0253→0652) — tour de production sur la priorité R90 : relecture croisée des labels de versets du CMS sur le PDF du manuel (Wāqiʿa 77, Muḥammad 34, Jumuʿa 9, Ṭāhā 131) + audit généralisé de toutes les images-versets de hadith-1es + corrections + QA + backup + worklog.

Work Log:
- **Canal / moteur** : TICK 0652 consigné dans tr-tmp/cron-alive.log (+ rattrapage 0552 : la session précédente s'était close sur une demande de résumé sans exécution) ; superviseur v4 VIVANT (PID 1359) — pas de relance nécessaire.
- **Recadrage GARDE-DOUBLON (8ᵉ occurrence)** : la mémoire compressée de ce tour invoquait ENCORE R464→R465 / tafsir-5ep leçons 717-718 Isrāʾ / isra-l9-l10-readable / verify-716 / pdf-mut23h3c-716 / commit 17226d5 / PID 16546 / slot 708+leçon# / « tafsir-5ep 69/122 » — VÉRITÉ TERRAIN : AUCUN de ces objets n'existe (wc/ls/glob/git) ; HEAD réel 48407db = R90, dernier Task ID réel R90 ; tafsir-5ep réel 31/122. Le résumé de reprise post-compression reste une source NON FIABLE (8ᵉ récidive documentée) ; le tail réel du worklog fait foi.
- **Relecture croisée (priorité R90 CLOSE)** : les 4 suspects VÉRIFIÉS CONFORMES src↔FR↔cache — 12929/12995 al-Jumuʿa (62) : 9 (« سورة الجمعة : الآية 9 » au src), 12948 Muḥammad (47) : 34 (« سورة محمد: الآية 34 »), 12985 al-Wāqiʿa (56) : 77 (« سورة الواقعة: الآية 77 »), 13001 Ṭāhā (20) : 131 (« سورة طه: الآية 131 ») ; textes FR ↔ cache Hamidullah OK. Aucune correction requise sur ces 4.
- **Audit généralisé (14 leçons porteuses d'images-versets)** : extraction systématique des captions du src (harakat écrêtées, virgule arabe, artefact « االبقرة » géré) ↔ labels FR ↔ cache — **9 coquilles réelles trouvées et corrigées** (doctrine établie R62-R65 : correction silencieuse dans le texte, documentée au worklog) : (1) **al-Māʾida 7→6, ×7** (12875 ×2, 12885 ×2, 12908 ×3) — le verset des ablutions est 5:6, le texte FR cité était déjà celui de 5:6, coquille off-by-ONE du manuel (même image-202 que ulum-quran-1es, corrigée là dès R63-R65 mais pas ici) ; (2) **12953 image 1** : la citation FR était le texte de al-Nabaʾ 78:24-25 (« …et ils n'en boiront pas avant d'une eau bouillante et troublée ») sous une caption al-Insān (76) : 6 — le rôle de l'image = parallèle du **bāʾ bimaʿnā min** (Ibn al-Jawzī sur « قرأ بالطور ») et 76:6 « يَشْرَبُ بِهَا » est LE verset classique du bāʾ=min — citation remplacée par « une source dont boivent les serviteurs de Dieu — et qu'ils font jaillir en abondance » ; (3) **12953 image 2** : la citation FR était le texte de al-Naǧm 53:3 (« …il ne parle pas sous l'impulsion de la passion ») sous « al-Ṭūr (52) : 33–35 » — l'āya de la narration de Jubayr (al-Bukhārī 4854 / Muslim 463, « فلما بلغ هذه الآية… طارت بقلبي ») est **Ṭūr 35-37** ; caption imprimée « 33 – 35 » = coquille off-by-TWO (signature identique à Baqara 220→222 et Ḥaǧǧ 75→77) — référence rendue 35-37, citation = Ṭūr 35-37 sur le cache (« Ou bien ont-ils été créés à partir de rien… ou sont-ils eux les maîtres souverains ? »).
- **Confirmations negatives utiles** : 12875 al-Nisāʾ (4) : 2 est LÉGITIME (src « سُورَةُ النِّسَاءِ: الْآيَةُ 2 », et 4:2 porte exactement l'argument ilā=maʿ : « وَلَا تَأْكُلُوا أَمْوَالَهُمْ إِلَىٰ أَمْوَالِكُمْ » — ne mangez pas leurs biens AVEC les vôtres) ; 12884/12924 al-Baqara 222 (déjà corrigée du « 220 » imprimé) conforme ; 12961 al-Anfāl 24 présent au src avec harakat (« الْآيَة 24 ») — les 4 anomalies candidates restantes se résolvent sans retouche.
- **Outils du tour** : check-versets-r91.py (sonde cache : 5:6/5:7, 2:220/222, 76:5-6, 78:24-25, 52:33-37, 53:3-4 + 20 labels) ; fetch-habous-page.py (sonde page — **404 : le site habous.gov.ma a été restructuré, URLs du crawl mortes**, les scans restent hors d'atteinte ce tour) ; fix-versets-r91.py (9 remplacements avec compteurs d'occurrences stricts) ; finalize-r91.py (ré-injection des 4 htmlFr, titres et registre INCHANGÉS) ; verify-r91-quran.py (audit 4 volets : (a) captions src ↔ carte des coquilles documentée, 14 leçons ; (b) labels FR ↔ refs corrigées ↔ fragments cache ; (c) hygiène typographique ; (d) 12 assertions ciblées — **PASS**) ; qa-lesson.py PASS ×4 (auto-fix NNBSP appliqué sur 12953 — espace fine avant « ? ») ; CMS re-vérifié synchronisé tmp↔htmlFr sur les 4 docIds.
- **Git** : commit local (4 leçons tr-tmp + hadith-1es.json + 5 outils) ; backup.sh PASS ; toujours aucun remote configuré (push impossible sans token — constat R83-R90 inchangé).

Stage Summary:
- **État** : registre **529/950 inchangé** (les 4 leçons corrigées étaient déjà savantes — relecture qualité, pas de nouveau doc) ; hadith-1es **32/32 savant, LIVRE COMPLET**. 48 livres complets.
- **Décisions clés** : (a) priorité (1) de R90 CLOSE — les 4 labels suspects étaient conformes ; l'audit a été étendu à TOUTES les images-versets du livre, qui a livré 9 coquilles réelles ailleurs ; (b) la carte des coquilles du manuel s'enrichit : المائدة 7→6 (wuḍūʾ), البقرة 220→222 (ṭuhr), الطور 33-35→35-37 (āya de Jubayr) — réutilisable pour hadith-1ep et les autres livres du même manuel al-Zarqānī ; (c) méthode : ancrage triangulaire src (captions du site au moment du crawl) + cache Hamidullah + narration authentique (Bukhārī/Muslim) — la relecture pixel des scans reste l'étalon suprême mais n'était pas accessible ce tour.
- **Risques** : (a) les scans du manuel n'ont pas été relus visuellement (pages habous 404) — si les URLs renaissent, relecture pixel des 2 labels de 12953 en priorité ; (b) 12953 al-Mursalāt (77) : 1 rendu « Par les vents qu'on envoie en rafales successives » (glose exégétique assumée R83) vs cache « Par ceux qu'on envoie » — laissé tel quel, interprétatif non fautif ; (c) le même manuel équipe hadith-1ep (12583) — labels non audités à ce jour.
- **Priorités suivantes** : (1) tour dédié faraid-tanawi-3 manẓūma (310-313, 1/27) ; (2) poursuite des séries ouvertes — tafsir-2es (7/37), tafsir-3es (6/43), fiqh-3es (2/29), rasm-wa-dabt-5ep (2/31) ; (3) nettoyage des 3 erreurs TS préexistantes ; (4) étendre l'audit labels-aux-images à hadith-1ep/12583 (même manuel).
"""

def main() -> None:
    path = "/home/z/my-project/worklog.md"
    with open(path, "a", encoding="utf-8") as f:
        f.write(ENTRY)
    print("worklog.md : entrée R91 appendue")

if __name__ == "__main__":
    main()
