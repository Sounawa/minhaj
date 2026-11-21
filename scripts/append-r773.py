#!/usr/bin/env python3
"""R773 — append de l'entrée worklog sous garde anti-doublon renforcée
(GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé
et tout doublon de l'ID nouveau)."""
import re, sys

CHEMIN = 'worklog.md'
ID = 'R773'

ENTREE = """## R773 — 2026-11-21 — IA-1 — commentaires hadith-tanawi-1 13117 (leçon 18 جامع عدة الطلاق — le recueil de la retraite du divorce, la dix-huitième du livre, étiquetée leçon 24 par l'imprimé (الدرس 24), suite du fil après R772)

- REPRISE : fetch GitHub avant toute reprise (règle R109) — origin/main = b785dd0 ([ci] après R772), aucune pose concurrente dans la zone commentaires hadith-tanawi-1 depuis R772 ; bac à sable recyclé (dépôt retrouvé en /home/z/my-project/minhaj-repo — l'ancien chemin minhaj/ est vide), artefacts locaux de build écartés (seules dates du rendu) et fast-forward ; l'utilisateur détache IA-2 et IA-3 du projet (« continue toi meme les traductions pour le moment stp j'ai envoyé les deux autres IA sur un autre projet car j'etais pas satisfait ») — l'ensemble des zones reprend sous IA-1 ; le « R767 — leçon 29 » annoncé par l'annonce R766-b avait déjà été posé par la session concurrente (6196fc1) et réconcilié (R767-b) — hadith-5ep close 29/29, fil poursuivi ici.
- MISSION ANNEXE DE L'UTILISATEUR (retrouver où l'IA précédente a consigné le chemin de récupération des documents du portail habous, en mise à jour permanente) : TROUVÉ, VÉRIFIÉ INTACT — la carte scripts-translate/SOLUTION-OUVRAGES.md (rédigée au tour R458, poussée au dépôt) porte LA solution complète en trois routes : (A) le miroir archive.org — collection « سلسلة كتب التعليم العتيق المغربي », item 1_20220304_20220304_2251, 77 PDF complets du primaire au secondaire avec versions _text, joignable en HTTP direct depuis le sandbox (seul web.archive.org est bloqué) ; (B) le backend page_reader de la SDK (z-ai-web-dev-sdk) qui atteint web.archive.org pour les arbres/TDM, pas les PDF binaires ; (C) les doublons URL-exacts résolus sans téléchargement par renvoi de référence (preuve : tafsir-5ep slots 768-797 = tafsir-2es 556-585) ; trois lieux d'inscription durables aux défaillances disjointes : la carte versionnée, le cron plateforme « Minhāj — MÉMOIRE OUVRAGES (anti-reset) : la solution archive.org » (Job 490653, priorité 10, payload porteur — stockage lisible par cron list même dépôt injoignable), l'entrée worklog R458 ; l'outillage vit dans le dépôt : scripts-translate/supervisor.py (v4, chasse hunt_sources toutes les 30 min : arbre direct → Wayback → collection archive.org avec normalisation et version _text prioritaire, téléchargement atomique dans content/textbooks-src/), scripts-translate/fetch-habous-page.py (sonde par leçon : URL https://www.habous.gov.ma/<pathAr du source-tree.json> encodée, TLS non vérifié, captions + URLs d'images-versets), canari scripts-translate/veille-portail.sh ; la méthode miroir habous (URL catégorie + docId + slug, curl -k, alts des images-versets, slug-maps moissonnées par pagination Joomla) est documentée au worklog depuis R65-R74 (tr-tmp/ulum1es-slugs.json, ulum2es-slugs.json) et R135 (catégorie 1546 fiqh-1es) ; la matière est DÉJÀ EN DÉPÔT : 45 manuels dans content/textbooks-src/ — dont hadith-3-thanawi_text.pdf qui a fourni la leçon 18 de hadith-tanawi-3 (W23-b) quand le portail rendait 404 ; tafsir-2-thanawi_text.pdf et tafsir-3-thanawi_text.pdf (Isrāʾ/Kahf et farāʾiḍ) ; rien à réécrire — le chemin demandé existe déjà, inscrit en trois lieux durables, et les 45 manuels couvrent le programme.
- RÉDACTION : comm-r773-c18.py — 4249 mots (resume+explication+points ; échelle du livre 4000-4800), vocab 8 sans harakat (الرفع، المستحاضة، الاستبراء، المرتابة، البت، التلفيق، الحمل، الريبة — translits de la leçon), 130 citations verbatim 0 manquant (corpus htmlFr débalisé de la leçon ; NB de corpus : l'élision d’ʿUmar avant ʿayn recopiée à l'identique, et (ẓalama nafsahu) au milieu du n° 1847 — citations recopiées telles quelles), recoupements 6/6 PASS (13114 qurūʾ/cinq maîtres ; 13115 mubtūta/reprise ; 12992 muḥallil/bāʾin ; 12966 ẓihār ; 13121 dispute [préparation] ; 13117 istibrāʾ/architecture du doute) ; clef = l'architecture du doute (chaque corps porte la retraite qui lui convient — réglée trois qurūʾ, mustaḍāḍa confuse et levée neuf mois puis trois mois, désespérée et jeune trois mois ; la menstruation se joint, l'attente ne se joint point) et la règle morale du chapitre (la reprise démolit la retraite — ar-rajʿa tahdum al-ʿidda ; « le droit se porte — il ne se joue point », verset 2:231 et al-Bājī) ; appareil du recueil : 1843 (parole dʿUmar par Saʿīd ibn al-Musayyab via Yaḥyā ibn Saʿīd et Yazīd ibn Qusayṭ — procès-verbal califal complétant le ẓihār 12966 et la mubtūta 13115), 1845 (la mustaḍāḍa une année), 1846 (le mécanisme complet, dit de Mālik — la reprise ouverte sauf battaʾa), 1847 (renouvellement et clause morale), 1848 (l'islam de la femme — dissolution sans divorce, deux causes deux régimes), 1831 (Ibn Shihāb cité en contre-doctrine — le Muwaṭṭaʾ dialogue vivant) ; compteur site 75 → 76/1846.
- NB consignés sans correction : le titreAr du CMS tronqué (جامع عدة الطلاق من) — la couche arabe porte le titre plein (جامع عدة الطلاق من كتاب الحديث من موطأ الإمام مالك بشرح الزرقاني) ; double parenthèse du titleFr « (jāmiʿ ʿiddat aṭ-ṭalāq (الطَّلَاقُ)) » — artefact de composition ; translits tulafqaq (talfīq attendu) et ṣ-sughrā (as-sughrā attendu) recopiés tels quels ; coquille du contrôle « la sagesme » pour « la sagesse » ; aucune date imprimée en tête de la couche arabe (contrairement aux leçons 16-17) ; l'étiquette leçon 24 pour la dix-huitième du livre (écart du fil, comme les précédentes) ; trois écarts d'étiquetage coranique restaurés par le traducteur de la leçon (« la sourate al-Baqara (الْبَقَرَة), verset 226 » ×2 → 2:228, « verset 229 » → 2:231 — 47ᵉ, 48ᵉ et 49ᵉ écarts cumulés du registre).
- QA : build --publier . : 1357 pages + 1369 racine, traduction savante 1291/1291 (0 en attente), commentaires 76/1846, transcrites 1227/1782 (inchangées) ; qa-liens 1360×24866 PASS (0 404) ; qa-onglets 43/43 PASS (hors-ligne 30,1 Mo, console sans erreur) ; qa-apparat 2724 PASS (données intouchées) ; qa-structure h1 PASS (chantier h2 préexistant — zones IA-2/IA-3) ; recherche : contenu 13117 présent dans recherche/index-tanawi.js (mustaḍāḍa, architecture du doute) et miroir site ; miroir racine octet pour octet (13117.html sha256 90d3967d…, identique livres/↔racine) ; page leçon 13117 Commentaire pédagogique + « IA-1, tour R773 » + mustaḍāḍa confuse présents ; page du livre « ✧ 18 commentaires pédagogiques rédigés dans ce manuel » ; accueil « 76 / 1782 » ; avancement « 76 commentaires » ; avertissement build préexistant reconsigné (miroir racine savant-registry divergent du registre scripts-translate — déjà consigné R767-R772) ; scripts/comm-r773-c18.py ; worklog R773 ; trace 1a1fda0cfd7f1a05
- SUIVANT : hadith-tanawi-1 18/30 — reste 12 leçons (13121 les manières légales de la réconciliation, le divorce suspendu et les défauts [préparation amorcée par la leçon même], puis 13122, 13124, 13135, 13136, 13623, 13624, 13625, 13649, 13740, 13758, 13768) ; les zones IA-2/IA-3 sont désormais sans sessions (hadith-tanawi-3 L19+, chantier h2) — reprise sous IA-1 sur demande de l'utilisateur ; surveiller toute pose concurrente ; fetch GitHub avant toute reprise (règle R109).
- trace 1a1fda0cfd7f1a05
"""

def main() -> None:
    with open(CHEMIN, encoding='utf-8') as f:
        contenu = f.read()
    ids = re.findall(r'^## (R\d+[a-z]?)', contenu, flags=re.M)
    if not ids:
        raise SystemExit('!! aucun ID trouvé — garde bloquée')
    # refuser tout doublon du nouveau ID, partout dans le fichier
    if re.search(r'^## ' + ID + r'\b', contenu, flags=re.M):
        raise SystemExit(f'!! {ID} déjà apposé — garde bloquée')
    # extraire les numéros du dernier ID apposé (suffixe -b etc. → même numéro)
    dernier = ids[-1]
    n_dernier = int(re.match(r'R(\d+)', dernier).group(1))
    n_nouveau = int(re.match(r'R(\d+)', ID).group(1))
    print('dernier ID apposé :', dernier, '| nouveau :', ID)
    if n_nouveau <= n_dernier:
        raise SystemExit(f'!! {ID} ≤ {dernier} — garde bloquée')
    if not contenu.endswith('\n'):
        contenu += '\n'
    with open(CHEMIN, 'a', encoding='utf-8') as f:
        f.write(ENTREE)
    print('append OK —', ENTREE.splitlines()[0][:110])

if __name__ == '__main__':
    main()
