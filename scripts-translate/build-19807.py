# -*- coding: utf-8 -*-
"""build-19807.py — assemble les fragments FR de 19807, extrait les citations du quran-cache, sondes."""
import json, re, unicodedata

BASE = '/home/z/my-project'
frag = [open(f'{BASE}/tr-tmp/fr19807_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
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
# Translittérations manuelles des fenêtres citées (style du corpus : article assimilé, wasla liée)
TRANSLIT = {
    (106,2): 'īlāfihim riḥlata aš-šitāʾi wa-ṣ-ṣayfi',
    (7,69): 'fa-ḏkurū ālāʾa llāhi laʿallakum tufliḥūna',
    (55,13): 'fa-bi-ayyi ālāʾi rabbikumā tukaḏḏibāni',
    (59,3): 'kataba llāhu ʿalayhimu l-jalāʾa la-ʿaḏḏabahum fī d-dunyā',
    (2,31): 'fa-qāla anbiʾūnī bi-asmāʾi hāʾulāʾi in kuntum ṣādiqīna',
    (2,5): 'ulāʾika ʿalā hudan min',
    (54,43): 'akuffārukum ḫayrun min ulāʾikum am lakum barāʾatun',
    (4,91): 'wa-ulāʾikum jaʿalnā lakum ʿalayhim',
    (72,9): 'fa-man yastamiʿi l-ʾāna yaǧid lahu šihāban',
    (37,106): 'inna hāḏā lahuwa l-balāʾu l-mubīnu',
    (44,33): 'al-āyāti mā fīhi balāʾun mubīnun',
    (2,49): 'wa-fī ḏālikum balāʾun min rabbikum ʿaẓīmun',
    (38,3): 'min qarnin fa-nādaw wa-l-lāta ḥīna manāṣin',
    (43,67): 'al-aḫillāʾu yawmaʾiḏin baʿḍuhum li-baʿḍin',
    (28,4): 'inna firʿawna ʿalā fī l-arḍi wa-jaʿala',
    (2,64): 'baʿdi ḏālika fa-lawlā faḍlu llāhi ʿalaykum',
    (10,20): 'wa-yaqūlūna lawlā unzila ʿalayhi āyatun',
    (5,23): 'qāla raǧulāni mina lladhīna yaḫāfūna',
    (5,75): 'ṣiddīqatun kānā yaʾkulāni ṭ-ṭaʿāma unẓur',
    (28,15): 'fa-waǧada fīhā raǧulayni yaqtatilāni hāḏā min šīʿatihī',
    (55,31): 'sanafruġu lakum ayyuhā ṯ-ṯaqalāni',
    (2,76): 'qālū āmannā wa-iḏā ḫalā baʿḍuhum ilā baʿḍin',
    (35,24): 'min ummatin illā ḫalā fīhā naḏīrun',
    (47,19): 'fa-iʿlam annahu lā ilāha illā llāhu',
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

def bctx(s, a, motif):
    """motif sur bare2 sans espaces (bigrammes/particules)"""
    verse = data[str(s)]['ar'][a-1][1]
    words = re.split(r'[\s\u00a0]+', verse.strip())
    bars = [bare2(w) for w in words]
    lens = [len(b) for b in bars]
    ns = ''.join(bars)
    i = ns.find(motif)
    if i < 0:
        return None
    # words couverts par [i, i+len(motif))
    acc, lo_w, hi_w = 0, None, None
    for k, L in enumerate(lens):
        st, en = acc, acc + L
        if st < i + len(motif) and en > i:
            if lo_w is None: lo_w = k
            hi_w = k
        acc = en
    lo, hi = max(0, lo_w-2), min(len(words), hi_w+3)
    return FINE.join(words[lo:hi])

fails = []
def sub(m):
    kind, s, a, motif = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
    c = ctx(s, a, motif) if kind == 'Q' else bctx(s, a, motif)
    if not c:
        fails.append(f'{kind}:{s}:{a}:{motif}')
        return '⟪ÉCHEC⟫'
    return f'«{TRANSLIT[(s, a)]}» ({s}:{a})'

html = re.sub(r'\{\{(Q|B):(\d+):(\d+):([^}]+)\}\}', sub, html)
html = html.replace(chr(39), '\u2019')

# ==== SONDES ====
ok = True
def probe(label, cond, detail=''):
    global ok
    print(('OK  ' if cond else 'FAIL') + f' [{label}] {detail}')
    if not cond: ok = False

h1s = re.findall(r'<h1>(.*?)</h1>', html)
probe('h1 unique', len(h1s) == 1, h1s[0] if h1s else '—')
probe('badge', 'Leçon 25 / 30' in html)
trs = re.findall(r'<tr>', html)
tds = re.findall(r'<td>', html)
probe('matn 5 tr / 10 td', len(trs) == 5 and len(tds) == 10, f'{len(trs)}/{len(tds)}')
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
    open(f'{BASE}/tr-tmp/19807.html', 'w', encoding='utf-8').write(html)
    print(f'\nWRITTEN tr-tmp/19807.html — {len(html)} car')
else:
    print('\nBLOQUÉ — corriger avant écriture')
