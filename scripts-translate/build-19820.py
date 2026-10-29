# -*- coding: utf-8 -*-
"""build-19820.py — assemble les fragments FR de 19820, vérifie les citations au cache, sondes."""
import json, re, unicodedata

BASE = '/home/z/my-project'
frag = [open(f'{BASE}/tr-tmp/fr19820_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
html = '\n'.join(frag)

data = json.load(open(f'{BASE}/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare2(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c == '\u0622': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out).replace('\u0671', '\u0627')

FINE = '\u202f'
TRANSLIT = {
    (2,102): 'wa-ittabaʿū mā tatlū aš-šayāṭīnu ʿalā mulki sulaymāna wa-mā yuʿallimāni min aḥadin',
    (21,78): 'wa-dāwūda wa-sulaymāna iḏ yaḥkumāni fī l-ḥarṯi iḏ nafašat fīhi ġanamu l-qawmi',
    (2,37): 'fatalaqqā Ādamu min rabbihī kalimātin fatāba ʿalayhi',
    (8,7): 'yurīdu llāhu an yuḥiqqa l-ḥaqq bi-kalimātihi wa-yaqṭaʿa dābira l-kāfirīna',
    (6,115): 'wa-tammat kalimatu rabbika ṣidqan wa-ʿadlan lā mubaddila li-kalimātihi',
    (33,35,'صءمت'): 'wa-l-mutaṣaddiqīna wa-l-mutaṣaddiqāti wa-ṣ-ṣāʾimīna wa-ṣ-ṣāʾimāti wa-l-ḥāfiẓīna',
    (33,35): 'inna l-muslimīna wa-l-muslimāti wa-l-muʾminīna wa-l-muʾmināti',
    (3,7): 'hūwa allaḏī anzala ʿalayka l-kitāba minhu āyātun muḥkamātun hunna ummu l-kitābi',
    (47,20): 'lawlā nuzzilat sūratun fa-iḏā unzilat sūratun muḥkamatun ruʾiyā llāḏīna',
    (24,61): 'aw buyūti aʿmāmikum aw buyūti ʿammātikum aw buyūti aḫwālikum',
    (33,50): 'wa-banāti ʿammika wa-banāti ʿammātika wa-banāti ḫālika wa-banāti ḫālatika',
    (22,30): 'ḏālika wa-man yuʿaẓẓim ḥurumāti llāhi fahuwa ḫayrun lahu ʿinda rabbihī',
    (3,54): 'wa-makarū wa-makara llāhu wa-llāhu ḫayru l-mākirīna',
    (51,48): 'wa-l-arḍa farašnāhā fa-niʿma l-māhidūna',
    (18,3): 'mākiṯīna fīhi abadan',
    (43,77): 'wa-nādaw yā māliku li-yaqḍi ʿalaynā rabbuka qāla innakum mākiṯūna',
    (31,12): 'wa-laqad ātaynā Luqmāna l-ḥikmata ani škur li-llāhi wa-man yaškur',
    (31,13): 'wa-iḏ qāla Luqmānu li-bnihi wa-huwa yaʿiẓuhū yā bunayya lā tušrik',
    (28,38): 'fāwaqid lī yā Hāmānu ʿalā ṭ-ṭīni fa-ǧʿal lī ṣarḥan laʿallī aṭṭaliʿu',
    (28,6): 'wa-numakkina lahum fī l-arḍi wa-nuriya Firʿawna wa-Hāmāna wa-ǧunūdahumā',
    (19,54): 'wa-uḏkur fī l-kitābi Ismāʿīla innahū kāna ṣādiqa l-waʿdi wa-kāna rasūlan',
    (2,136): 'qūlū āmannā bi-llāhi wa-mā unzila ilaynā wa-mā unzila ilā Ibrāhīma wa-Ismāʿīla',
    (2,57): 'wa-ẓallalnā ʿalaykumu l-ġamāma wa-anzalnā ʿalaykumu l-manna wa-s-salwā',
    (2,210): 'hal yanẓurūna illā an yaʾtiyahumu llāhu fī ẓulalin mina l-ġamāmi wa-l-malāʾikatu',
    (26,197): 'awalam yakun lahum āyatan an yaʿlamahū ʿulamāʾu banī Isrāʾīla',
    (1,4): 'māliki yawmi d-dīni',
    (3,26): 'quli llāhumma mālika l-mulki tuʾtī l-mulka man tašāʾu',
    (68,39): 'am lakum aymānun ʿalaynā bāliġatun ilā yawmi l-qiyāmati',
    (5,108): 'aw yaḫāfū an turadda aymānun baʿda aymānihim wa-ttaqū llāha',
    (8,2): 'innamā l-muʾminūna allaḏīna iḏā ḏukira llāhu wiǧilat qulūbuhum wa-iḏā tuliyat ʿalayhim āyātuhū zādathum īmānan',
    (23,63): 'bal qulūbuhum fī ġamratin min hāḏā wa-lahum aʿmālun min dūni ḏālika',
    (2,167): 'kaḏālika yurīhimu llāhu aʿmālahum ḥasarātin ʿalayhim',
    (2,33): 'qāla yā Ādamu anbiʾhum bi-asmāʾihim fa-lammā anbaʾahum bi-asmāʾihim qāla',
    (7,71): 'atugādilūnanī fī asmāʾin sammaytumūhā antum wa-ābāʾukum',
    (33,72): 'innā ʿaraḍnā l-amānata ʿalā s-samāwāti wa-l-arḍi fa-aḥallanhā',
    (55,1): 'bismi llāhi r-raḥmāni r-raḥīmi ar-raḥmānu',
    (17,71): 'yawma nadʿū kulla unāsin bi-imāmihim fa-man ūtiya kitābahū',
    (15,79): 'fa-ntaqamnā minhum wa-innahumā labi-imāmin mubīnin',
    (36,12): 'wa-kulla šayʾin aḥṣaynāhū fī imāmin mubīnin',
}

def ctx(s, a, motif):
    verse = data[str(s)]['ar'][a-1][1]
    words = re.split(r'[\s\u00a0]+', verse.strip())
    bars = [bare2(w) for w in words]
    idx = [i for i, b in enumerate(bars) if motif in b]
    if not idx:
        return None
    i = idx[0]
    lo, hi = max(0, i-3), min(len(words), i+4)
    sel = words[lo:hi]
    sel = sel[0].lstrip('،') if lo > 0 else sel[0]
    return FINE.join(sel)

fails = []
def sub(m):
    s, a, motif = int(m.group(1)), int(m.group(2)), m.group(3)
    c = ctx(s, a, motif)
    if not c:
        fails.append(f'Q:{s}:{a}:{motif}')
        return '⟪ÉCHEC⟫'
    tr = TRANSLIT.get((s, a, motif), TRANSLIT.get((s, a)))
    if tr is None:
        fails.append(f'TR:{s}:{a}:{motif}')
        return '⟪ÉCHEC⟫'
    return f'«{tr}» ({s}:{a})'

html = re.sub(r'\{\{Q:(\d+):(\d+):([^}]+)\}\}', sub, html)
html = html.replace(chr(39), '\u2019')

# ==== SONDES ====
ok = True
def probe(label, cond, detail=''):
    global ok
    print(('OK  ' if cond else 'FAIL') + f' [{label}] {detail}')
    if not cond: ok = False

h1s = re.findall(r'<h1>(.*?)</h1>', html)
probe('h1 unique', len(h1s) == 1, h1s[0] if h1s else '—')
probe('badge', 'Leçon 27 / 30' in html)
trs = re.findall(r'<tr>', html)
tds = re.findall(r'<td>', html)
probe('matn 5 tr / 10 td (istitmār en prose, convention 19818)', len(trs) == 5 and len(tds) == 10, f'{len(trs)}/{len(tds)}')
probe('marqueurs résolus', len(fails) == 0 and '⟪ÉCHEC⟫' not in html, str(fails))
probe('volume', len(html) >= 12000, f'{len(html)} car')
q = html.count('«') + html.count('»')
probe('guillemets appariés', q % 2 == 0, f'{q}')
probe("0 apostrophe droite", "'" not in html)
ar = [c for c in html if '\u0600' <= c <= '\u06ff']
probe('0 arabe résiduel', len(ar) == 0, f'{len(ar)} chars AR')
probe('N.d.T. 8', html.count('<li><p>') >= 8, f"{html.count('<li><p>')}")
probe('h2 x7', len(re.findall(r'<h2>', html)) == 7, f"{len(re.findall(r'<h2>', html))}")

if ok:
    open(f'{BASE}/tr-tmp/19820.html', 'w', encoding='utf-8').write(html)
    print(f'\nWRITTEN tr-tmp/19820.html — {len(html)} car')
else:
    print('\nBLOQUÉ — corriger avant écriture')
