const b = require('/home/z/my-project/content/books/tajwid-5ep.json');
const m = (b.lessons || []).find(l => String(l.docId) === '19056');
const html = m.html || '';

// Normalisation : retirer diacritiques (U+064B-U+065F, U+0670), tatweel (U+0640), espaces fins
function norm(s) {
  return s
    .replace(/&nbsp;/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

const rows = [...html.matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(r => r[1]);
console.log('rangées:', rows.length);
const kw = ['مدي', 'جائز', 'منفص', 'متصل', 'لازم', 'المد', 'بدل', 'احكم', 'احكم'];
for (let idx = 0; idx < rows.length; idx++) {
  const cells = [...rows[idx].matchAll(/<td[^>]*>([\s\S]*?)<\/td>/g)]
    .map(c => norm(c[1]))
    .filter(Boolean);
  const joined = cells.join(' ');
  if (kw.some(k => joined.includes(k))) {
    console.log('ROW', idx, '=>', cells.join('  ||  '));
  }
}
