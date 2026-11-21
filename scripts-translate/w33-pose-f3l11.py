#!/usr/bin/env python3
# W33 — pose fiqh-3es pdf-11 أحكام الشفعة والتبرعات (pp.84-92)
# Re-pose après recyclage : le commit initial 810749e (jamais poussé) a été perdu ;
# htmlFr reconstruit à l'identique depuis la conversation (QA : 0 arabe, guillemets
# appariés, 0 apostrophe droite). Injecte le htmlFr prêt + registre + worklog.
import json, re, sys

REPO = '/home/z/my-project/repo-417'
HTMLFR = '/home/z/my-project/download/minhaj-f3-l11/htmlfr-pdf11-W33.html'
DOCID = 'pdf-11'

html = open(HTMLFR, encoding='utf-8').read().strip()
assert len(html) > 15000, f'htmlFr trop court: {len(html)}'

body = re.sub(r'<[^>]+>', '', html)
checks = {
    'car': len(body),
    'arabe': len(re.findall(r'[\u0600-\u06FF]', body)),
    'guillemets_écart': body.count('«') - body.count('»'),
    'apostrophe_droite': body.count("'"),
    'h1': html.count('<h1>'), 'h2': html.count('<h2>'), 'h3': html.count('<h3>'),
    'dl': html.count('<dl>'), 'ol': html.count('<ol>'), 'ul': html.count('<ul>'),
    'em_ouvert': html.count('<em>'), 'em_fermé': html.count('</em>'),
    'strong_o': html.count('<strong>'), 'strong_f': html.count('</strong>'),
    'p_o': html.count('<p>'), 'p_f': html.count('</p>'),
}
for tag in ('em', 'strong', 'p', 'h1', 'h2', 'h3'):
    o = html.count(f'<{tag}>'); c = html.count(f'</{tag}>')
    assert o == c, f'balises {tag} déséquilibrées: {o} vs {c}'
assert checks['arabe'] == 0, 'arabe résiduel dans htmlFr'
assert checks['guillemets_écart'] == 0, 'guillemets non appariés'
assert checks['apostrophe_droite'] == 0, 'apostrophes droites'
assert checks['h2'] == 9, f'h2 attendus 9: {checks["h2"]}'

path = f'{REPO}/content/books/fiqh-3es.json'
raw = open(path, encoding='utf-8').read()
d = json.loads(raw)
lessons = [x for x in d['lessons'] if x.get('docId') == DOCID]
assert len(lessons) == 1, f'{DOCID}: {len(lessons)} correspondances'
assert lessons[0]['htmlFr'].strip() == '', 'slot pdf-11 non vide — pose concurrente ?'
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

worklog = f'''{REPO}/worklog-ia3.md'''
entry_w33 = """
## W33 — 2026-11-21 — IA-3 — traduction fiqh-3es leçon 11 أحكام الشفعة والتبرعات (pdf-11, pp.84-92, suite W32)

- POSE puis RE-POSE : le commit initial 810749e (W33, jamais poussé — push bloqué avant passation) a été perdu au recyclage du sandbox (clone vidé, eb6e12b) ; htmlFr reconstruit à l'identique depuis la conversation, QA rejouée (17365 car, 0 arabe, guillemets appariés, 0 apostrophe droite, balises équilibrées, 9 h2, 1 dl), slot pdf-11 vérifié vide au fetch-avant-pose (origin 3c3c858).
- متن الرسالة traduit (letter pp.84-85) : «وإنما الشفعة في المشاع ولا شفعة في المذكور ولا للجار ولا في الطريق ولا في عرصة دار وقسمت ديارها ولا في عهل النخل ولا في البئر إذا قُسم النخل أو الأرض ولا شفعة إلا في الأرض وما لاحقها من العمران والشجر ولا شفعة للحاضر بعد السائل وللغائب شفعته وإن طالت غيبته والضمان على المشتري والشفيع ينتظر فيما أخذ أو ترك ولا توهب الشفعة ولا تبيع وتُقسم بين الشركاء على قدر الأنساب ولا تتم هبة ولا صدقة ولا حبس إلا بالحيازة فإن مات قبل أن يحيزها كان من التركة إلا أن تكون في المرض فيكون في الثلث إن كانت لغير وارث والموهوب للقريب أو للفقير كالصدقة لا رجعة فيه ومن تصدق على ولده فلا رجعة له ولحق له أن يرجع فيما وهبه لولده صغيرا أو كبيرا ما لم يتزوج عليه أو يترتب عليه دين أو يطرأ على الهبة تغيير وأم ترد ما دام الأب حيا إذا مات لم ترد ولا يُرَدُّ على اليتيم ويتيمه يكون في حياة أبيه وما وهبه لولده الصغير حيزته حلّة له إن لم يسكنه أو ألبسه إن كان ثوبا ولا حلّ له إلا ما عرفته بالعين فالأكبير لا تحل له حيزته ولا يرجع الرجل من صدقته ولا ترد عليه إلا بالميراث ولا بأس أن يشرب من لبن ما تصدق عليه ولا أن يشتري ما تصدق عليه والموهوب للعوض إما أثاب القيمة أو رد الهبة وذلك إذا كان يرى أنه أراد الثواب من الموهوب له».
- Écarts canon : «السائل» (2 lectures 400 dpi concordantes) vs canon shamela 11373/140 «السنة» — N.d.T. consigné ; queue «الثواب من الموهوب له» imprimée, absente du canon shamela (11373 s'arrête à «القيمة أو رد الهبة») — consignée.
- Canon fetché : shamela 11373/140-141 (4 passages WebFetch) + الثمر الداني shamela 7441/572 (dérivation الشفع/الوتر + définition Ibn al-Ḥājib «أخذ الشريك نصيبا من نصيب شريكه بيعا» corrobore).
- Renvois letter confirmés : [جامع الأمهات ١/٤١٦] / [البخاري كتاب الشفعة باب الشفعة فيما لم يقسم إذا أُقيمت العلامات وأنفرجت الطرق فلا شفعة] / [الفواكه الدواني ٢/١٥٣] / [البخاري كتاب الزكاة باب الصدقة من كسب طيب] / [المصباح المنير مادة عصر] / [شرح حدود ابن عرفة ص٤٢٧ — lexie douteuse consignée] / [الموطأ كتاب الشفعة باب ما لا تقع فيه الشفعة].
- Registre IA-3 → pdf-11. SUIVANT pdf-12 الحبس وهبة الثواب pp.93+ (متن aperçu p.93 : «ويكره أن يهب لبعض ولده ماله كله… ومن وهب هبة فلم يحزها الموهوب له حتى مرض الواهب أو أفلس…» + الحبس «ومن حبس دارا فهي على ما جعلها عليه إن حيزت قبل موته…») — canon shamela 11373/141-142 pré-fetchable.
"""
open(worklog, 'a', encoding='utf-8').write(entry_w33)

print('POSE OK —', json.dumps(checks, ensure_ascii=False))
print('registre:', reg['hand'][-2:])
print('worklog: W33 appendu,', len(entry_w33), 'car')
