#!/usr/bin/env python3
"""Fix 11945 fragments: apostrophes typographiques + translittération des runs arabes."""
import glob, re

REPL_AR = [
    ('graphie <em>al-bayūʿ al-manhī ʿanhā</em> (البويع), l\'introduction <em>al-bayūʿ</em> (البيوع)',
     'porte <em>al-bayūʿ al-manhī ʿanhā</em>, l\'introduction <em>al-buyūʿ</em>'),
    ('« <em>talqī as-saʿ</em> » (السع) pour « <em>talqī as-silaʿ</em> » (السلع — les marchandises)',
     '« <em>talqī as-saʿ</em> » pour « <em>talqī as-silaʿ</em> » — les marchandises'),
    ('le <em>alif</em> initial tronqué de « <em>ishtamala</em> » (شتمل pour اشتمل)',
     'le <em>alif</em> initial tronqué de « <em>ishtamala</em> » — <em>shtamala</em> pour <em>ishtamala</em>'),
    ('la asymétrie', 'l\'asymétrie'),
]

for f in sorted(glob.glob('/home/z/my-project/tr-tmp/11945.f*.html')):
    t = open(f, encoding='utf-8').read()
    t = t.replace(chr(39), '\u2019')  # apostrophe droite -> typographique
    for a, b in REPL_AR:
        if a in t:
            t = t.replace(a, b)
    open(f, 'w', encoding='utf-8').write(t)
    # vérification
    t2 = open(f, encoding='utf-8').read()
    ar = re.findall(r'[\u0600-\u06FF]+', t2)
    sq = t2.count(chr(39))
    print(f'{f.split("/")[-1]}: arabic={ar} straight={sq}')
