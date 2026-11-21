#!/usr/bin/env python3
# W35 — pose fiqh-3es pdf-12 أحكام الحبس وهبة الثواب (pp.93-99) + registre + worklog
import json, re, sys

REPO = '/home/z/my-project/repo-417'
HTMLFR = '/home/z/my-project/download/f3-l12/htmlfr-pdf12-W35.html'
DOCID = 'pdf-12'

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
assert lessons[0]['htmlFr'].strip() == '', 'slot pdf-12 non vide — pose concurrente ?'
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

entry_w35 = """
## W35 — 2026-11-21 — IA-3 — traduction fiqh-3es leçon 12 أحكام الحبس وهبة الثواب (pdf-12, pp.93-99, suite W34)

- ORDRE DU PROPRIÉTAIRE R777 APPLIQUÉ (traduction seule, zone IA-3 fiqh-3es, leçons dans l'ordre) ; fetch-avant-pose : origin d9fc2b6d (CI après W34 896089f1), slot pdf-12 vérifié vide, ff-only local.
- MATIÈRE : content/textbooks-src/fiqh-3-iadadi_text.pdf pp.93-99 par couche pdftotext pp.92-101 + 14 lectures VLM 150 dpi + 9 zooms 600-1200 dpi ; leçon délimitée : متن pp.93-94 (2 p.), glossaire ×4 (سائع, أفلس, انقرض, يكلب), استخلاص ×3, التحليل 2 axes (أولا : هبة المال الكثير/اليسير/ما تبطل به + الصدقة بكل المال + الحيازة في التبرعات ; ثانيا : تعريف/حكم/أركان ×4/شرط الحبس/انقراض عقب/وفاة بعض المحبسين/بيع الحبس ×2), التقويم ×4 (incl. صورة العمل), استثمار ابن رشد [بداية المجتهد 4/711], إعداد الرهن والعارية والوديعة ; L13 démarre p.100 (متن الرهن dès p.100).
- CANON : shamela 11373/141-142 fetché (142 par miroir ftp.shamela.ws — shamela.ws timeout ×2 consigné) — le canon CONFIRME le متن composé du tirage : «ومن أعمر رجلا حياته دارا رجعت بعد موت الساكن ملكا لربها وكذلك إن أعمر عقبه فانقضى بخلاف الحبس فإن مات المعمر يومئذ كانت لورثته يوم موته ملكا» (clause العمرى, ×3 letter concordantes) ; «ويؤثر في الحبس أهل الحاجة بالسكنى والغلة» (الغلة tranché ×3 contre couche العلة) ; «ومن سكن فلا يخرج لغيره إلا أن يكون في أصل الحبس شرط فيمضي» (fimmadhi tranché ×3+canon contre zoom نصب فيصير) ; «ولا يباع الحبس وإن خرّب» ✓ ; «ويباع الفرس [الم]حبس يكلب ويجعل ثمنه في مثله أو يعان به فيه» ✓ (canon «الفرس الحبس», tirage المحبس — variante consignée).
- ARBITRAGES : سائع imprimé (×2 : متن+glossaire letter) vs canon سائغ — N.d.T. ; فلم يحزها tranché ×3+canon contre فلم ياخذه/فلحزها ; الإشهاد tranché (couche+VLM bas) contre الإنهاء/الإنشاد — canon Bukhārī ✓ ; عُقوق الباقين tranché letter-major contre عوق/عرق corruptions ; التوادر والزيادات 12/210 tranché (bidi 012//21 + VLM ×2) ; vers ابن عاصم «والحوز شرط صحة التخبيس قبل حدوث موت أو إفلاس» + clause التسولي «سائر التبرعات من هبة أو صدقة أو نحلة» — ينعقد/يتعقد/ينفذ lectures divergentes, letter porté translittéré neutralisé en «sauf le contrat de mariage constitué sur elle» (sens canon) ; البهجة في شرح التحفة 2/379 tranché (bidi 973/2 + VLM ×2) ; لغة الحبس «حبيس والجمع حبس مثل بريد وبرد» tranché ×2 ; الصحابة «كعمر بن الخطاب وعثمان وعلي وطلحة والزبير» tranché zoom600+v150 contre couche corrompue ; أركان ×4 letter (الواقف أهل التبرع / الصيغة / الموقوف مملوكا ذاتا أو منفعة «دارا» / الموقوف عليه أهلا للتملك حكما كالمسجد أو حكما كالأدمي) ; شرط الحبس «إن حيزت قبل موته» + إذن الوقف على معين vs غير معين كالمسجد letter ✓ ; بيع الحبس «ولا يباع الحبس ولا أُنفاضه إذا شرط الوقف عدم بيعه» — letter ×2 (أنفاضه/أقفاصه divergents) porté «ni ce qui en est désaffecté» sens-consigne ; يكلب بفتح الياء واللام + الهرم والمرض + الموقوفة لتسليكها أو لعملها tranché ×2-3 ; الجهاد tranché (couche letter) contre VLM الجهاز ; موطأ ابن وهب «بيع داثر وبئر تعطل ويعوض به ربع» — letter couche maintenu avec sens neutralisé en français (citerne/puits dont l'usage s'est arrêté) ; ابن رشد citation conforme canon بداية المجتهد (letter-renvoi 4/711 maintenu contre VLM corrompues بدائع الصنائع/إرادة الصحيح — N.d.T.) ; التقويم item 2 «أعرف بالوقف» letter couche+zoom contre أعرض VLM ; أهداف أتعرف ×3 letter couche+convention série contre أعرف VLM150/zoom.
- POSE : hand-set w35-pose-f3l12.py — QA PASS (balises équilibrées, guillemets appariés, 0 apostrophe droite, 0 arabe, 9 h2, 1 dl, 2 ul, 1 ol) ; registre IA-3 → pdf-12 ; worklog W35.
- SUIVANT : pdf-13 أحكام الرهن والعارية والوديعة (leçon 13, pp.100-107 — متن الرهن dès p.100 déjà aperçu couche pp.92-101 ; canon shamela 11373/142-144).
"""
open(f'{REPO}/worklog-ia3.md', 'a', encoding='utf-8').write(entry_w35)

print('POSE OK —', json.dumps(checks, ensure_ascii=False))
print('registre:', reg['hand'][-2:])
print('worklog: W35 appendu,', len(entry_w35), 'car')
