#!/usr/bin/env python3
# W34 — pose fiqh-3es pdf-10 أحكام المزارعة (pp.77-83) + registre + worklog
import json, re, sys

REPO = '/home/z/my-project/repo-417'
HTMLFR = '/home/z/my-project/download/f3-l10/htmlfr-pdf10-W34.html'
DOCID = 'pdf-10'

html = open(HTMLFR, encoding='utf-8').read().strip()
body = re.sub(r'<[^>]+>', '', html)
checks = {
    'car': len(body),
    'arabe': len(re.findall(r'[\u0600-\u06FF]', body)),
    'guillemets_écart': body.count('«') - body.count('»'),
    'apostrophe_droite': body.count("'"),
    'h1': html.count('<h1>'), 'h2': html.count('<h2>'), 'h3': html.count('<h3>'),
    'dl': html.count('<dl>'), 'ol': html.count('<ol>'), 'ul': html.count('<ul>'),
    'p_o': html.count('<p>'), 'p_f': html.count('</p>'),
    'em_o': html.count('<em>'), 'em_f': html.count('</em>'),
    'ndt': body.count('N.d.T.'),
}
for tag in ('em', 'p', 'h1', 'h2', 'h3', 'dl', 'ul', 'ol'):
    o = html.count(f'<{tag}>'); c = html.count(f'</{tag}>')
    assert o == c, f'balises {tag} déséquilibrées: {o} vs {c}'
assert checks['arabe'] == 0, 'arabe résiduel'
assert checks['guillemets_écart'] == 0, 'guillemets non appariés'
assert checks['apostrophe_droite'] == 0, 'apostrophes droites'
assert checks['h2'] == 9, f'h2 attendus 9: {checks["h2"]}'
assert checks['h1'] == 1 and checks['dl'] == 1 and checks['ul'] == 2 and checks['ol'] == 1
assert len(body) > 14000, f'htmlFr trop court: {len(body)}'

path = f'{REPO}/content/books/fiqh-3es.json'
raw = open(path, encoding='utf-8').read()
d = json.loads(raw)
lessons = [x for x in d['lessons'] if x.get('docId') == DOCID]
assert len(lessons) == 1, f'{DOCID}: {len(lessons)} correspondances'
assert lessons[0]['htmlFr'].strip() == '', 'slot pdf-10 non vide — pose concurrente ?'
lessons[0]['htmlFr'] = html
out = json.dumps(d, ensure_ascii=False, indent=2) + '\n'
open(path, 'w', encoding='utf-8').write(out)

regp = f'{REPO}/scripts-ia3/savant-registry-ia3.json'
reg = json.load(open(regp, encoding='utf-8'))
entry = f'fiqh-3es/{DOCID}'
if entry not in reg['hand']:
    reg['hand'].append(entry)
json.dump(reg, open(regp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open(regp, 'a', encoding='utf-8').write('\n')

entry_w34 = """
## W34 — 2026-11-21 — IA-3 — traduction fiqh-3es leçon 10 أحكام المزارعة (pdf-10, pp.77-83, suite W33) — RE-PRISE après passation v2 (URL dépôt + PAT fournis ; clone repo-417 réparé après checkout incomplet «no space left on device» — index reconstruit par git reset --mixed, checkout complété par git restore ; ht3-mirror (656 Mo PDFs wadod recouvrables) libéré)

- ORDRE DU PROPRIÉTAIRE R777 APPLIQUÉ : traduction SEULE (s-commentaires suspendus — la recommandation §8 de la passation v2 «s-commentaire L24 hadith-5ep» est PÉRIMÉE) ; carte PARTAGE-TRADUCTION : fiqh-3es = zone IA-3 (197), leçons DANS L'ORDRE → pdf-10 (slot du SUIVANT W32, sa session parallèle perdue) avant pdf-12 ; W33 (pdf-11 الشفعة والتبرعات) re-posé et poussé ce tour (commit d23e9860, re-pose du livrable reconstruit après recyclage).
- MATIÈRE : content/textbooks-src/fiqh-3-iadadi_text.pdf pp.77-83 par couche pdftotext pp.76-84 + 14 lectures VLM 150 dpi (2 moitiés × 7 pages, 2+ passes) + 14 zooms 600-1200 dpi + 4 re-zooms ciblés (clause هـ p.80, hadith أبو الزبير p.82) ; leçon délimitée : استثمار L9 + إعداد p.76, متن pp.77-78, الفهم/استخلاص p.78, التحليل 2 axes pp.79-82, التقويم/استثمار خليل p.83, إعداد الشفعة p.83.
- CANON : shamela 11373/134-135 fetché (fin المزارعة → المساقاة → الشركة في الزرع → الجائحة : règle du tiers, exclusions, البقول, خلاص, 5 أوسق) ; Mukhtaṣar Khalīl shamela 11355/245 (ص180 = renvoi imprimé ✓) + شرح الزرقاني 14297/2710 corroboration ; aliftaa.jo ResearchId=221 (الجوائح عند المالكية, as-Ṣayfī) pour définitions et البقول.
- ARBITRAGES : متن — البذر imprimé (3 lectures letter) vs canon الزرع (variante d'édition consignée) ; نخلات imprimé (3 letter) vs canon خلاص (consigné) ; تقاربت tranché (zoom 600 + canon contre VLM 150 تفاوتا) ; ينقد maintenu (couche+canon contre zoom ينقطع) ; أصاب الثلث فأكثر maintenu (canon+sens contre lectures corrompues أجيح/أجاب/قبل) ; البقول «ما لا تطول مدته» tranché (zoom+VLM+canon aliftaa — pas d'écart) ; جذاذ maintenu (2 letter+canon contre zoom الجناب) ; جنانه maintenu (2+canon contre zoom جنوبه) ; clause هـ = الإكنان من عندهما (couche letter + zoom fin «كان من عندهما» contre VLM «خطأ البائع») ; أهليتا الشركة والإجارة (VLM bas+sens contre corruptions) ; بناء renvoi الدواني 2/127 tranché (couche bidi 2/721→127 + VLM ×2) ; ابن عرفة [المختصر الفقهي 6/189] tranché (couche bidi 981/6→189 + VLM+zoom) ; définition أبو الحسن «كالبرد والريح والجيش» — 2 letter concordantes maintenues vs aliftaa «الحشيش» (N.d.T. consigné) ; clause 1 الشروط «أن تكون الثمرة من بيع لا إن كانت من مهر ولا من هبة ولا صدقة» — structure imprimée portée telle quelle (3 letter), canon aliftaa (achat indépendant de l'origine) consigné ; خليل : «لم يبذ/يبذر» letter vs variante 11355 «لم يبذر» vs éditions courantes «لم ينتفض» — N.d.T. ; «بممنوع/تساونا/لتبرع» letter-major imprimé vs canon fetché consigné ; hadith أبو الزبير : canon Muslim «وهو يأخذ» vs imprimé «هتأخذ» — N.d.T. ; renvoi [صحيح مسلم كتاب المساقاة باب فضل الغرس والزرع] ✓ 3 concordances ; [صحيح مسلم ... باب وضع الجوائح] ✓ 3 concordances ; zoom j-asbab vide (marge de page) — zone couverte par j-islah.
- POSE : hand-set w34-pose-f3l10.py — QA PASS (balises équilibrées, guillemets appariés, 0 apostrophe droite, 0 arabe, 9 h2, 1 dl, 2 ul, 1 ol) ; registre IA-3 → pdf-10 ; worklog W34.
- SUIVANT : pdf-12 الحبس وهبة الثواب (leçon 12, pp.93+, متن aperçu p.93 — canon shamela 11373/141-142 pré-fetchable) ; pdf-11 déjà posé (W33) ; la séquence ordre de la carte est rétablie.
"""
open(f'{REPO}/worklog-ia3.md', 'a', encoding='utf-8').write(entry_w34)

print('POSE OK —', json.dumps(checks, ensure_ascii=False))
print('registre:', reg['hand'][-2:])
print('worklog: W34 appendu,', len(entry_w34), 'car')
