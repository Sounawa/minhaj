"""QA globale des livres rendus : intégrité JSON, RAID htmlFr, marqueurs, rendu site/sitemap."""
import json, os, re, sys

RACINE = '/home/z/my-project/push-work/minhaj'
REP_RENDU = f'{RACINE}/site/livres'
SITEMAP = f'{RACINE}/sitemap.xml'

MARKERS = ['TODO', 'XXX', '【', 'undefined', 'NaN', '|---']
ARABE = re.compile(r'[\u0600-\u06FF]')
FRAG_AR = re.compile(r'[\u0600-\u06FF][\u0600-\u06FF\u064B-\u065F\u0670 ﷺ\u06dd]*')
# le séparateur d'hémistiche « *** » est une convention du projet : l'exclure
# NB : les livres mantiq/taqtit/tafsir-tanawi-1/2/faraid-2 utilisent « ** » comme
# séparateur de vers — cohérent fr/ar — donc « ** » n'est pas un artefact
MD = re.compile(r'(^|\n)#{1,4}\s')
# arabe volontairement cité dans la page française = balisé rtl (matn des hadith, versets…)
# balise fermante correspondante (backreference) : sinon un <u> interne tronque l'extraction
BALISE_RTL = re.compile(r'<([a-z]+)[^>]*dir="rtl"[^>]*>.*?</\1>', re.S)
# livres à convention strictement sans arabe dans htmlFr (constaté dans le repo)
STRICTS = {
    'fikr-islami-tanawi-1', 'fikr-islami-tanawi-2', 'fikr-islami-tanawi-3',
    'fiqh-2es', 'qiraat-tanawi-2', 'qiraat-tanawi-3', 'tafsir-tanawi-3',
    'tajwid-3es', 'taqtit-tanawi-2', 'taqtit-tanawi-3',
    'usul-fiqh-tanawi-2', 'usul-fiqh-tanawi-3',
    'usul-qiyam-4ep', 'usul-qiyam-5ep', 'usul-qiyam-6ep', 'rasm-wa-dabt-6ep',
}
# exceptions documentées (termes techniques intraduisibles / citation du bandeau) :
# fiqh-3es pdf-27 « société du جبر », pdf-28 « ذمم/وجوه » ; hadith-tanawi-3
# pdf-mut23h2n-8 « suite ﴿تتمة﴾ » — choix éditoriaux de la session d'origine
EXCEPT_TITRE = {('fiqh-3es', 'pdf-27'), ('fiqh-3es', 'pdf-28'), ('hadith-tanawi-3', 'pdf-mut23h2n-8')}

def audit(livre):
    chemin = f'{RACINE}/content/books/{livre}.json'
    d = json.load(open(chemin, encoding='utf-8'))
    strict = livre in STRICTS
    lessons = d['lessons']
    print(f'== {livre}: {len(lessons)} entrées' + (' (strict sans arabe)' if strict else ' (matn arabe balisé admis)') + ' ==')
    ids = [x.get('docId', '?') for x in lessons]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        print(f'  !! docIds dupliqués: {sorted(dup)}')
    sitemap = open(SITEMAP, encoding='utf-8').read()
    problemes = []
    for x in lessons:
        did = x.get('docId', '?')
        tag = f'  {did}'
        # champs obligatoires
        for champ in ('titleAr', 'titleFr'):
            if not x.get(champ):
                problemes.append(f'{tag}: {champ} vide')
        if ARABE.search(x.get('titleFr', '')) and (livre, did) not in EXCEPT_TITRE:
            problemes.append(f'{tag}: arabe dans titleFr')
        fr, ar = x.get('htmlFr'), x.get('html')
        pdfonly = x.get('pdfOnly')
        # RAID htmlFr
        if fr is None:
            if not (pdfonly or x.get('pdfUrl')):
                problemes.append(f'{tag}: ni htmlFr ni pdf')
        else:
            hors_balise = BALISE_RTL.sub(' ', fr)
            frag = ARABE.findall(hors_balise)
            if frag:
                if strict:
                    problemes.append(f'{tag}: arabe (balisé) interdit dans htmlFr strict')
                # non-strict : l'arabe court hors balise est une convention des séries
                # d'origine (citations canoniques, bandeaux du tirage, gloses lexicales,
                # bibliographies en arabe) ; seule la pollution française↔arabe
                # massive (200+ fragments) serait suspecte :
                elif len(FRAG_AR.findall(hors_balise)) > 200:
                    problemes.append(f'{tag}: arabe massif non balisé — à inspecter')
            for m in MARKERS:
                if m in fr:
                    problemes.append(f'{tag}: marqueur «{m}» dans htmlFr')
            if MD.search(fr.replace(' *** ', ' ')):
                problemes.append(f'{tag}: markdown résiduel dans htmlFr')
            if len(fr) < 900 and not pdfonly:
                # < 900 : les annexes/activités légitimes (tableau des lettres
                # tajwid-6ep 17597, activité ulum-quran-2es 19288) sont au-dessus
                problemes.append(f'{tag}: htmlFr très court ({len(fr)} car)')
        # html arabe
        if ar is None and not (pdfonly or x.get('pdfUrl')):
            problemes.append(f'{tag}: ni html ni pdf')
        if ar is not None and not ARABE.search(ar) and not pdfonly:
            problemes.append(f'{tag}: html sans arabe')
        for m in ('TODO', 'XXX', '【', 'undefined', 'NaN'):
            if ar and m in ar:
                problemes.append(f'{tag}: marqueur «{m}» dans html')
        # rendu — les entrées pdfOnly n'ont pas de page html (renvoi PDF), c'est normal
        if not pdfonly:
            page = f'{REP_RENDU}/{livre}/{did}.html'
            if not os.path.exists(page):
                problemes.append(f'{tag}: page rendue ABSENTE')
            elif os.path.getsize(page) < 500:
                problemes.append(f'{tag}: page rendue trop petite ({os.path.getsize(page)} o)')
        if did not in sitemap and not pdfonly:
            problemes.append(f'{tag}: absent du sitemap')
    # séquence pdf-N : détecter les TROUS (les décalages d'origine sont documentés :
    # ex. hadith-2es = leçons 1-30 aux slots pdf-2..31, continu)
    nums = sorted(int(m.group(1)) for i in ids for m in [re.fullmatch(r'pdf-(\d+)', i)] if m)
    if nums:
        trous = [n for n, nxt in zip(nums, nums[1:]) if nxt > n + 1]
        if trous:
            problemes.append(f'  trous dans la séquence pdf après: {trous}')
    print('\n'.join(problemes) if problemes else '  ✔ aucun problème détecté')
    # longueurs htmlFr
    lens = [(x['docId'], len(x.get('htmlFr') or '')) for x in lessons]
    print('  longueurs htmlFr:', ', '.join(f'{i}:{l}' for i, l in lens))
    return not problemes

ok = True
for livre in sys.argv[1:]:
    ok = audit(livre) and ok
print('\nRÉSULTAT GLOBAL:', 'PASS' if ok else 'ÉCHEC')
