#!/usr/bin/env python3
"""R774 — append de l'entrée worklog sous garde anti-doublon renforcée
(GARDE-DOUBLON.md : balayer TOUT le fichier, refuser tout ID ≤ dernier apposé
et tout doublon de l'ID nouveau)."""
import re, sys

CHEMIN = 'worklog.md'
ID = 'R774'

ENTREE = """## R774 — 2026-11-21 — IA-1 — commentaires hadith-tanawi-1 13121 (leçon 19 التفريق بين الزوجين للضرر و العيب — la séparation des époux pour préjudice ou vice, la dix-neuvième du livre, étiquetée leçon 25 par l'imprimé (الدرس 25), suite du fil après R773)

- REPRISE : fetch GitHub avant toute reprise (règle R109) — origin/main = 4f8fe730 ([ci] après R773), aucune pose concurrente depuis R773 ; bac à sable recyclé (dépôt retrouvé en /home/z/my-project/minhaj-repo — l'ancien chemin minhaj/ est vide) ; disque du sandbox plein (100 %) — espace libéré (tmp_pack orphelin du gc 688 Mo, caches navigateurs et /tmp), fetch R767→R773 réconcilié par fast-forward ; l'utilisateur confirme la production SOLO (« continue la traduction solo ») — IA-2 et IA-3 restent détachées.
- MISSION ANNEXE DE L'UTILISATEUR (chemin de récupération des documents du portail habous) : déjà résolue et consignée R773 — carte scripts-translate/SOLUTION-OUVRAGES.md (R458) en trois routes (A archive.org item 1_20220304_20220304_2251 — 77 PDF ; B page_reader SDK pour Wayback TDM ; C doublons URL-exacts) + cron MÉMOIRE OUVRAGES 490653 + supervisor hunt_sources + fetch-habous-page.py + veille-portail.sh ; revérifié intact ce tour : 45 manuels dans content/textbooks-src/ (787 Mo) dont hadith-1-thanawi_text.pdf (8,8 Mo) qui porte la matière de hadith-tanawi-1 — rien à réécrire.
- RÉDACTION : comm-r774-c19.py — 5013 mots (resume+explication+points ; la leçon est la plus longue du livre — 28 302 caractères débalisés, trois parties + trois écoles + lexique + Ibn Rushd — l'échelle du livre 4000-4800 dépassée par la matière, consigné), vocab 8 sans harakat (التحكيم، الشقاق، الحكمين، الإصلاح، المعلق، أثم، اعترض، الوكيل — translits de la leçon), 176 citations verbatim 0 manquant (corpus htmlFr débalisé de la leçon ; NB de corpus : le verset 4:35 recopié IN EXTENSO à CINQ emplacements — une sixième fois dans l'exploitation avec guillemets anglais —, et les formes du lexique arabe أثم: أي حنث، اعترض: منعه عن الوطء مانع recopiées telles quelles), recoupements 6/6 PASS (13117 dispute/suspendu [préparation] ; 13122 contraint/ivres [suivante] ; 12966 ẓihār/Nasāʾī ; 12991 dot/Māʾida ; 12957 banquet/Rushd ; 13121 taḥkīm/ḥakamayn) ; clef = la qualification juridique des deux arbitres (députés du juge nāʾibān ʿan al-ḥākim ou mandataires des époux wakīlān ʿan az-zawjayn — chaque doctrine en découle mécaniquement : Mālikites+Shāfiʿītes un dire / Ḥanafites+Ḥanbalites+Shāfiʿītes autre dire ; le dialogue dʿAlī par an-Nasāʾī contre « à eux la séparation entre les deux et le rassemblement ») et l'asymétrie du chapitre (le rassemblement court sans mandat, la séparation sous conditions — la porte de la réparation plus large que la porte de la dissolution) ; appareil : 1849 (ʿAlī ibn Abī Ṭālib, les deux arbitres + an-Nisāʾ 35 — pilier), 1852 (Ibn Masʿūd « s'il ne nomme ni tribu, ni femme en particulier » + le sceau de Mālik), 1854-1855 (Saʿīd ibn al-Musayyab via Ibn Shihāb — l'année des quatre saisons, le point de départ « du jour où elle saisit l'autorité », le second dire du touché-puis-empêché), 1850 et 1851 cités à l'analyse (le compilé de Mālik ; la parole collective des Médinois — ʿUmar, Ibn ʿUmar, Ibn Masʿūd, Sālim, al-Qāsim) ; les trois écoles du divorce suspendu (ash-Shāfiʿī/Aḥmad nullité par « point de divorce avant le mariage » d'Ibn Māja ; Abū Ḥanīfa obligation absolue ; les Mālikites distinguent généralisation désobéissance non liante / particularisation liante par al-Māʾida 1) ; le jabb et l'iʿtirāḍ (échelle de l'espérance — point d'ajournement / une année les quatre saisons) ; Bahrām le transmetteur de la Mudawwana depuis Ibn al-Qāsim (le point de départ procédural vs amiable) ; Ibn Rushd, le commencement du mujtahid 3/117 (quatre accords et une divergence) ; compteur site 76 → 77/1846.
- NB consignés sans correction : l'étiquette leçon 25 pour la dix-neuvième du livre (écart du fil, comme les précédentes — 13117 était leçon 24 pour la dix-huitième) ; le titreAr du CMS est PLEIN ici (التفريق بين الزوجين للضرر و العيب من موطأ الإمام مالك بشرح الزرقاني) — contrairement à 13117 tronqué ; le titre de la leçon (« préjudice ou vice ») ne couvre que la troisième partie — la leçon porte aussi l'arbitrage et le divorce suspendu (couleur du titre, matière plus large) ; le verset 4:35 recopié in extenso à CINQ emplacements de la couche française ; 0 écart d'étiquetage coranique nouveau (4:35 ×5 et 5:1 ×1 toutes concordantes au cache — le registre demeure 49 écarts cumulés) ; coquille du texte final « La asymétrie du chapitre » pour « L'asymétrie » ; six emplacements de versets en image, tous vides au scan.
- QA : build --publier . : 1357 pages + 1369 racine, traduction savante 1291/1291 (0 en attente), commentaires 77/1846, transcrites 1227/1782 (inchangées) ; qa-liens 1360×24866 PASS (0 404) ; qa-onglets 43/43 PASS (hors-ligne 30,1 Mo, console sans erreur) ; qa-apparat 2724 PASS (données intouchées) ; qa-structure h1 PASS (chantier h2 préexistant — 84 leçons dans 36 livres, zones IA-2/IA-3) ; recherche : contenu 13121 présent dans recherche/index-tanawi.js (ḥakamayn, al-iṣlāḥ) et miroir site ; miroir racine octet pour octet (13121.html sha256 7960a9d0…, identique site↔racine) ; page leçon 13121 Commentaire pédagogique + « IA-1, tour R774 » + ḥakamayn présents ; page du livre « ✧ 19 commentaires pédagogiques rédigés dans ce manuel » ; accueil « 77 / 1782 » ; avancement « 77 commentaires » ; avertissement build préexistant reconsigné (miroir racine savant-registry divergent du registre scripts-translate — déjà consigné R767-R773) ; scripts/comm-r774-c19.py ; worklog R774 ; trace 1a1fdb9d66198c89
- SUIVANT : hadith-tanawi-1 19/30 — reste 11 leçons (13122 le compte des divorces, le divorce du contraint, des deux en colère et des deux ivres [préparation amorcée par la leçon même], puis 13124, 13135, 13136, 13623, 13624, 13625, 13649, 13740, 13758, 13768) ; l'ensemble des zones reste sous IA-1 (production solo) ; surveiller toute pose concurrente ; fetch GitHub avant toute reprise (règle R109).
- trace 1a1fdb9d66198c89
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
