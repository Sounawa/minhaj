# -*- coding: utf-8 -*-
"""Append worklog R689 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R689
Agent: GLM (session web-continue, canal principal, tick 2026-11-12 09h00 +08:00)
Task: LIVRAISON leçon 410 hadith-3es (pdf-mut23h2x-410, leçon 21 imprimée « أحكام الفدية في الحج », p.141-146) + RÉSOLUTION du bug « site invisible sur le preview » (Next 16.4 allowedDevOrigins).

Work Log:
- Reprise de session : protocole session-start exécuté — local == origin/main (b332345), 0/0, pas de régression ; registre 1154/950 au départ de la passe.
- TAKEOVER LÉGAL du claim pdf-mut23h2x-410 (canal principal, trace 1a1ce7065e34bd49-r688-main-takeover, 06h41 UTC — le claim r688-main était périmé de 7h40 au regard de la règle des 50 min) ; claim tenu et LIBÉRÉ après livraison (archivé .livre-r689).
- EXTRACTION : couche logique du PDF reconstruite (scripts-translate/h3-410-logical.py — mots réinversés + ordre de mots inversé par ligne, la couche BRUTE étant en ordre visuel) → tr-tmp/h3-410-logical.txt ; 13 lectures VLM (6 pages plein-cadre + 7 zooms, tr-tmp/vlm-410/) recoupées à la couche logique.
- ADJUDICATIONS PAR L'IMAGE (7, toutes lettre à lettre) : (1) n° 1243 — verbe قُتِّلَ forme passive intensive (chadda sur le tā' + deux kasras), « شاف » de la couche récusé (crop m410-J) ; (2) tamhīd p.141 — فَتَّلَ (fā' à un point, NON qāf) + « بمختلف أنواعها », lecture « بألوانها » récusée (z410-9) ; (3) n° 1244 — « فيُغلَقُ عليها » (ghayn de l'enfermement, ṭā' de yuṭlaq récusé par le sens : cagées elles meurent) (m410-C) ; (4) n° 1260 — chiffre par chiffre, le 6 lu sur image, 1250 récusé (m410-F) ; (5) sanad n° 1241 — « عبد الملك بن قريز » (mīm de الملك + rā'-zāy de قريز), « عبد الله بن قيس » récusé (z410-8, crop 3000px) ; (6) n° 1255 — يَصْلُحُ (ṣād sans point, ḍād récusé) + يَطْرُحُها (ṭā', dāl de yaṭrud récusé) + حَفْنَة (nūn, ẓā' récusée) (m410-I) ; (7) n° 144 types — « ستة مساكين » (six, la lecture « sept » d'une passe pleine-page récusée — le total de trois ṣā' ne se couvre que de six mud) (z410-4). Chiffres tranchés chiffre par chiffre : 1240/0421, 1242/2421, 1243/3421, 1244/4421, 1245/5421, 1248/8421, 1260/0621, 1261/1621 (×3), 1266/6621, 1241/1421, 1262/2621 (×2), 1255/5521, aṣ-Ṣāffāt 107, al-Baqara 195 (décalage régional d'une unité vs cache ḥafṣ 196 — doctrine R511, consigné, jamais corrigé), Jorjānī p.165, hégire 128.
- RÉDACTION : leçon 21 en 5 fragments (tr-tmp/frag-l410-1..5.html) → assemblage tr-tmp/lesson-hadith3-410-fr.html (46 595 car) — h1 long (médaillon, objectifs, six textes, notice, gloses, résumé, recherche légale en deux sections, évaluation, exploitation, préparation), objectifs ×3 avec translittération, tamhīd, six textes (1240, 1242, 1243, 1244, 1245, 1248) chacun suivi de son commentaire d'intégration, notice d'abū az-Zubayr (Muḥammad b. Muslim b. Tidris al-Asadī al-Makkī, ṣadūq, 8 hadiths, m.128), gloses ×3, résumé ×2, fiqh : première section (concept en langue/terminologie — Ṣāffāt 107 + Jorjānī 165 ; statut — consensus, n° 1260 ×2, la licence pour la nécessité ; types — nusk 1261, iṭ'ām six pauvres 1261, ṣiyām 1266, takhīyr — Baqara 195 + Bukhārī + 1261) ; seconde section (gibier — 1240 re-cité, 1241 de la course ; oiseau — colombe de La Mecque, 1244 re-cité, 1262 ×2, itlāf m'aḍmūn, jumhūr salafan wa-khalfan ; autruche/badana ; règle du petit et du grand 1248 re-cité) ; évaluation ×2 résolues ; exploitation (1255 + invite) ; i'dād ×2 (jarād + ḥalaq — leçon 22) ; apparat de preuve complet (bornes p.141-146, douze numéros tranchés, sept adjudications, āyas cache, personnes, mécanique).
- QA : qa-lesson.py PASS (auto-fix NNBSP/apostrophes — 2 caractères arabes hors spans « شاف »/« بألوانها » repris en spans RTL) ; verify-hadith3-pdf410.py 56 contrôles OK / 0 échec (garde-doublon htmlFr vide vérifié avant pose, claim, 45k+, 11 sections, 6 textes, 12 numéros, matière adjudiquée, gloses, āyas, 0 arabe hors spans, 0 placeholder).
- POSE : hand-set.py hadith-3es pdf-mut23h2x-410 → « 1 emplacement(s) htmlFr écrit(s), 46594 car FR — registre → 1212 savants » ; API /api/books/hadith-3es : leçon 410 hasFr=true savant=true (21/29 leçons du livre).
- QA NAVIGATEUR (r689) : leçon rendue — h1 « Les compensations (fidya) pendant le pèlerinage », badge « Traduction savante », badge Leçon 21/29, 12 sections H2, les 12 numéros présents, contenus clés (six pauvres, poignée de nourriture, proximité de leur mesure), 0 débordement horizontal desktop 1280 ET mobile 390 (screenshots tr-tmp/qa-crops-r689/qa-r689-410-{desktop,mobile}.png) ; 0 erreur console.
- BUG « JE NE VOIS PLUS LE SITE SUR LE PREVIEW » — RÉSOLU (blocage cross-origin Next 16.4) : diagnostic via dev.log — « Blocked cross-origin request to Next.js dev resource /_next/hmr from "127.0.0.1" » ; Next 16.4 bloque par défaut les ressources de dev (hmr-client, chunks turbopack) servies depuis un hôte non déclaré → l'hydratation React échouait SILENCIEUSEMENT (pas d'erreur console, shell SSR affiché, effets jamais lancés) : accueil figé sur « Chargement de la bibliothèque… », voyant figé sur « interrogation du moteur… » — en local (127.0.0.1) ET à plus forte raison sur le domaine de preview (*.space-z.ai). CORRECTIF : next.config.ts + allowedDevOrigins ["localhost", "127.0.0.1", "*.space-z.ai"] (commenté R689) ; redémarrage dev server (le serveur de 06h37 était en dev mode, non standalone) ; VÉRIFICATIONS : hydratation locale OK (h1 leçon rendu, 40 682 car, widgets débloqués) ; chunk dev servi avec Origin https://preview-abc123.space-z.ai → HTTP 200, 0 « Blocked cross-origin » au log — le preview redevient visible.
- NOTE OPÉRATIONNELLE : le serveur dev lancé par l'agent meurt à la fin de la session d'outils (constaté ×2, relance setsid tenue pendant la passe) — le relais de redémarrage au réveil suivant reste `bun run dev` (script dev de package.json, mécanisme d'immortalité documenté) ; la config corrigée est dans le dépôt.
- Doctrine WIP-10min appliquée : commit 6dff95b (matériaux adjudiqués + scripts de passe) poussé AVANT la rédaction ; règle de vague tenue : une leçon livrée = push immédiat + backup + worklog.

Stage Summary:
- LIVRÉ : leçon 21 hadith-3es « Les compensations (fidya) pendant le pèlerinage » (slot pdf-mut23h2x-410, 20e slot livré du livre, 46 594 car au registre, registre → 1212 savants) — hadith-3es désormais 21/29 (restants : 411-418, la leçon 22 étant préparée par l'i'dād livré : jarād + ḥalaq).
- RÉSOLU : le preview invisible — cause Next 16.4 (allowedDevOrigins), correctif en dépôt, hydratation vérifiée locale + Origin preview simulée (200, zéro blocage).
- MÉCANIQUE RÉUTILISABLE consignée : reconstruction de la couche logique PDF (h3-410-logical.py — réinversion mots + ordre, plus fiable que la VUE LISIBLE pour les lignes simples) + adjudications d'image par microcrops ciblés (3000 px de large, questions lettre à lettre, « ne devine pas ») — sept/sept adjudications tranchées sans deviner, deux lectures VLM pleines récusées par convergence (بألوانها, sept pauvres).
- Prochaine priorité : slot pdf-mut23h2x-411 (leçon 22 — « أحكام فدية قتل الجراد وحلق الرأس » attendue, i'dād livré dans la présente : أشرح أنسك بشاة/جرادات/قبضة + حكم فدية قتل الجراد وحلق الرأس) ; vérifier session-start + 0/0 au réveil ; claim 404/405 actifs par d'autres ouvriers — PARALLÈLE respecté.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R689" in tail:
    print("REFUS : R689 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\\n"):
    content += "\\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\\n")
print(f"OK : R689 appendé. Worklog : {lines} lignes.")
