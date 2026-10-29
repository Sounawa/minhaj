# -*- coding: utf-8 -*-
"""build-19818.py — assemble les fragments FR de 19818, extrait les citations du quran-cache, sondes."""
import json, re, unicodedata
from collections import Counter

BASE = '/home/z/my-project'
frag = [open(f'{BASE}/tr-tmp/fr19818_{i}.html', encoding='utf-8').read() for i in range(1, 5)]
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
    (2,43): 'wa-aqīmū ṣ-ṣalāta wa-ʾātū z-zakāta',
    (24,58): 'ṯalāṯa marrātin min qabli ṣalāti l-faǧri wa-ḥīna taḍaʿūna ṯiyābakum',
    (23,2): 'wa-lladhīna hum fī ṣalātihim ḫāšiʿūna',
    (6,162): 'qul inna ṣalātī wa-nusukī wa-mamātī',
    (24,41): 'kullun qad ʿalima ṣalātahu wa-tasbīḥahu wa-llāhu ʿalīmun',
    (17,110): 'wa-lā tajhar bi-ṣalātika wa-lā tuḫāfit bihā',
    (9,103): 'ʿalayhim inna ṣalātaka sakanun lahum',
    (2,157): 'ulāʾika ʿalayhim ṣalawātun min rabbihim wa-raḥmatun',
    (23,9): 'wa-lladhīna hum ʿalā ṣalawātihim yuḥāfiẓūna',
    (18,81): 'an yubdilahumā rabbuhumā ḫayran minhu zakātan wa-aqraba',
    (2,125): 'min maqāmi ʾibrāhīma muṣallan wa-ʿahidnā ilā',
    (2,205): 'wa-iḏā tawallā saʿā fī l-arḍi',
    (6,62): 'ruddū ilā llāhi mawlāhumu l-ḥaqqi a-lā',
    (3,150): 'bali llāhu mawlākum wa-huwa ḫayrun',
}

def ctx(s, a, motif):
    verse = data[str(s)]['ar'][a-1][1]
    words = [w for w in re.split(r'[\s\u00a0]+', verse.strip()) if w]
    bars = [bare2(w) for w in words]
    idx = [i for i, b in enumerate(bars) if motif in b]
    if not idx:
        return None
    i = idx[0]
    lo, hi = max(0, i-3), min(len(words), i+4)
    return lo, hi, words[lo:hi]

fails, windows = [], []
def sub(m):
    kind, s, a, motif = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
    c = ctx(s, a, motif)
    if not c:
        fails.append(f'{kind}:{s}:{a}:{motif}')
        return '⟪ÉCHEC⟫'
    lo, hi, ww = c
    windows.append((s, a, ' '.join(ww)))
    tr = TRANSLIT.get((s, a))
    if not tr:
        fails.append(f'TRANSLIT MANQUANT {s}:{a}')
        return '⟪TRANSLIT MANQUANT⟫'
    return f'«{tr}» ({s}:{a})'

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
probe('badge', 'Leçon 26 / 30' in html)
trs, tds = re.findall(r'<tr>', html), re.findall(r'<td>', html)
probe('matn 6 tr / 12 td', len(trs) == 6 and len(tds) == 12, f'{len(trs)}/{len(tds)}')
probe('marqueurs résolus', len(fails) == 0 and '⟪' not in html, str(fails))
probe('volume', len(html) >= 12000, f'{len(html)} car')
q = html.count('«') + html.count('»')
probe('guillemets appariés', q % 2 == 0, f'{q}')
probe('0 apostrophe droite', "'" not in html)
ar = [c for c in html if '\u0600' <= c <= '\u06ff']
probe('0 arabe résiduel', len(ar) == 0, f'{len(ar)} chars AR')
probe('N.d.T. 8', html.count('<li><p>') >= 8, f"{html.count('<li><p>')}")
probe('h2 x7', len(re.findall(r'<h2>', html)) == 7, f"{len(re.findall(r'<h2>', html))}")

print('\n-- FENÊTRES CITÉES (contrôle des translittérations) --')
for s, a, w in windows:
    print(f'   {s}:{a} :: {w[:95]}')

if ok:
    open(f'{BASE}/tr-tmp/19818.html', 'w', encoding='utf-8').write(html)
    print(f'\nWRITTEN tr-tmp/19818.html — {len(html)} car')
else:
    print('\nBLOQUÉ — corriger avant écriture')
