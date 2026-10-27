#!/usr/bin/env python3
# build-13995.py — 13995 « Le rasm et le ḍabṭ : l'arjūza ʿUmdat al-Bayān… »
# (rasm-wa-dabt-4ep, lessons[0] — PRÉSENTATION du manuel, pas une leçon, règle ah)
# PREMIER document du livre rasm-wa-dabt-4ep (graphie et vocalisation coraniques) :
# h1 fait foi (règle av, 27e tranchage — trame « ar-rasm wa-ḍ-ḍabṭ : … » sur
# l'étiquette GT) ; fente liminaire VIDE portée telle quelle (ax) ; hamdala +
# adresse + présentation institutionnelle (Direction de l'enseignement ancestral,
# ministère des Habous) ; méthodologie (matn al-Wadghīrī « m. 7521 H » porté tel
# quel + signalement 752 H, šarḥ Bahjat an-naẓar wa-l-ʿiyān d'al-Masārī, démarche
# en quatre épreuves) ; sommaire 28 items (dédoublement imprimé items 17/18
# « complément du rāʾ » porté tel quel — ax) ; h2 compétences (6 items) ;
# annonce éditoriale ; balises pendantes refermées proprement ; zéro āya/zéro
# hadith cités — onzième tour sans protocole triple.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr13995_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    ar = [c for c in ar if c != chr(0xFDFA)]
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'p', 'ul', 'li', 'em', 'span', 'dl', 'dt', 'dd', 'div']:
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

norm = lambda s: s.replace("'", chr(0x2019))
probes = [
    "Le rasm et le ḍabṭ : l'arjūza ʿUmdat al-Bayān sur le jugement du ḥaḏaf dans le Coran d'al-Wadghīrī, avec le commentaire Bahjat an-naẓar wa-l-ʿiyān d'al-Masārī — 4e AB",
    "louange à Dieu qui fit descendre sur Son serviteur le Livre",
    "miracle qui demeure au fil des ères et des siècles",
    "une prière qui enveloppe quiconque a suivi la trace de sa guidance",
    "Nos fils les élèves, nos filles les élèves.",
    "Il échoit à la Direction de l'enseignement ancestral et de l'alphabétisation dans les mosquées",
    "le ministère des Habous et des Affaires islamiques",
    "un auxiliaire éducatif pour la compréhension des chapitres de cette science",
    "l'une des manifestations du génie marocain dans la préservation du Coran noble",
    "un matn marocain suave et utile au rasm du Coran noble et à son ḍabṭ",
    "« ʿUmdat al-Bayān fī ḥukm al-maḥḏūf fī l-Qurʾān »",
    "de l'imam Abū l-ʿAlāʾ Idrīs b. ʿAbd Allāh al-Bakrāwī al-Wadghīrī (m. 7521 H)",
    "le naṣab, le quota qu'un maître peut mémoriser et commenter en une séance",
    "le lexique difficile que le commentaire dégage",
    "ce que le vers bref porte",
    "l'analyse qui les décompose, la discussion qui les confronte, l'exemplification qui les fixe par le cas, la justification qui les rattache à leur raison",
    "« Bahjat an-naẓar wa-l-ʿiyān fī ḥall ʿUmdat al-Bayān »",
    "le poète donne la règle, le commentateur l'explique, le manuel l'applique, la planche la porte",
    "C'est à Dieu que nous demandons qu'il vous soit donné de trouver dans ce livre le meilleur auxiliaire",
    "c'est Lui notre recours, le meilleur des mandataires",
    "vingt-huit chapitres qui dessinent l'architecture de l'année",
    "<span>1.</span> Introduction à la science du rasm et du ḍabṭ.",
    "La genèse de la science du rasm et du ḍabṭ, son évolution",
    "Le préambule du poème : l'exposé de la fin visée par le poème",
    "le reste de la méthode du poète dans la poésie et la mention de son nom",
    "<span>5.</span> Le chapitre de la hamza.",
    "<span>6.</span> Le chapitre du bāʾ.",
    "<span>7.</span> Le complément du chapitre du bāʾ.",
    "<span>8.</span> Le chapitre du tāʾ.",
    "<span>9.</span> Le complément du chapitre du tāʾ.",
    "<span>10.</span> Le chapitre du ṯāʾ.",
    "<span>11.</span> Le chapitre du ğīm.",
    "<span>12.</span> Le chapitre du ḥāʾ.",
    "<span>13.</span> Le chapitre du ḫāʾ.",
    "<span>14.</span> Le chapitre du dāl.",
    "<span>15.</span> Le chapitre du ḏāl.",
    "<span>16.</span> Le chapitre du rāʾ.",
    "<span>17.</span> Le complément du chapitre du rāʾ.",
    "<span>18.</span> Le complément du chapitre du rāʾ.",
    "<span>19.</span> Le chapitre du zāy.",
    "<span>20.</span> Le chapitre du ṭāʾ et du ẓāʾ ensemble.",
    "<span>21.</span> Le chapitre du kāf.",
    "<span>22.</span> Le complément du chapitre du kāf.",
    "<span>23.</span> Le chapitre du lām.",
    "<span>24.</span> Le complément du chapitre du lām.",
    "<span>25.</span> Le chapitre du mīm.",
    "<span>26.</span> Le complément du chapitre du mīm.",
    "<span>27.</span> Les notices biographiques des personnalités.",
    "<span>28.</span> Les sources et les références.",
    "les items 17 et 18 se répètent à l'identique",
    "l'alphabet du rasm ne suit pas l'ordre abgad des lexiques mais l'ordre alphabétique usuel",
    "Les compétences de l'enseignement du rasm et du ḍabṭ en quatrième année de l'enseignement primaire ancestral",
    "on attend que l'apprenant(e) soit :",
    "mémorisateur des vers réglementés du poème, capable de les citer à l'appui des règles du rasm",
    "familier des règles générales qui encadrent le rasm coranique et de leurs exceptions",
    "connaissant le rasm des mots à ḥaḏaf dans chaque chapitre du poème, et leurs lieux dans le Coran noble",
    "distinguant l'alif fixe de son élidé parmi les mots du Coran noble",
    "appliquant en pratique, dans ce qu'il rédige des planches",
    "ayant intériorisé les sagesses du rasm et du ḍabṭ, leurs causes",
    "Attendez l'insertion successive de ces leçons sur cette page consacrée à l'arjūza ʿUmdat al-Bayān en matière de rasm et de ḍabṭ.",
    "Sur le titre : le h1 imprimé",
    "vingt-septième tranchage du fil",
    "une présentation du manuel, pas une leçon",
    "la fente liminaire du h1 est vide dans l'imprimé",
    "est refermée proprement en français sans rien ajouter au contenu",
    "l'imprimé porte « m. 7521 H » pour al-Wadghīrī",
    "les recueils biographiques établissent la mort de l'imam Idrīs b. ʿAbd Allāh al-Bakrāwī al-Wadghīrī en 752 H",
    "la coquille de 752, mais la traduction ne corrige point silencieusement",
    "les items 17 et 18 du sommaire se répètent à l'identique",
    "le vocalisme inégal des titres des chapitres",
    "Sur la terminologie fondée en cette famille",
    "le ḥaḏaf (la lettre réputée omise dans la graphie consacrée — l'élision)",
    "l'arjūza (le poème en rajaz)",
    "le mandataire au sens établi du corpus",
    "la démarche en quatre épreuves",
    "l'apprentissage autonome (al-baḥṯ wa-t-taʿallum aḏ-ḏātī) est nommé dès la présentation",
    "les items 5 à 26 suivent l'alphabet lettre à lettre",
    "aucune āya et aucun hadith ne sont cités dans l'imprimé — onzième tour sans protocole triple",
    "mūsā sans alif final, ar-raḥmān réduit à ses six lettres, le i-l-i-lāfihim qui reçoit son lām ouvrant",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/13995.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")
