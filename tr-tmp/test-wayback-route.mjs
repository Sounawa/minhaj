import ZAI from 'z-ai-web-dev-sdk';

const PDF_URL = 'https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/التفسير-الثانية-ثانوي/1_._سورة_الإسراء_الآية_1.pdf';
const WAYBACK_PDF = 'https://web.archive.org/web/20261013031750/' + PDF_URL;
const WAYBACK_TREE = 'https://web.archive.org/web/2026/https://www.habous.gov.ma/pressefra/fr/~/التعليم-العتيق';

async function testPageReader(zai, label, url) {
  console.log(`\n===== page_reader: ${label} =====`);
  console.log('URL:', url.slice(0, 120));
  try {
    const t0 = Date.now();
    const r = await zai.functions.invoke('page_reader', { url });
    const ms = Date.now() - t0;
    const data = r?.data;
    const html = data?.html || '';
    console.log(`status=${r?.status} code=${r?.code} ms=${ms} htmlLen=${html.length} title=${data?.title || ''}`);
    if (html) {
      const sample = html.replace(/\s+/g, ' ').slice(0, 500);
      console.log('SAMPLE:', sample);
      // detect PDF binary garbage vs real html
      const arabic = (html.match(/[\u0600-\u06FF]/g) || []).length;
      console.log('arabic chars:', arabic);
    }
    return { ok: !!html, html };
  } catch (e) {
    console.log('ERR:', e.message);
    return { ok: false };
  }
}

async function main() {
  const zai = await ZAI.create();

  // TEST 1: wayback PDF via page_reader (le contournement clé)
  const pdfTest = await testPageReader(zai, 'WAYBACK-PDF (Isra v1)', WAYBACK_PDF);

  // TEST 2: wayback tree page
  await testPageReader(zai, 'WAYBACK-TREE (portail)', WAYBACK_TREE);

  // TEST 3: web_search pour miroirs du manuel
  console.log('\n===== web_search: miroirs Tafsir 2e année secondaire =====');
  try {
    const r = await zai.functions.invoke('web_search', {
      query: 'التفسير الثانية ثانوي التعليم العتيق دروس PDF habous OR archive OR تحميل',
      num: 8,
    });
    const items = r?.result || r?.results || r || [];
    for (const it of (Array.isArray(items) ? items : [items])) {
      console.log('•', it?.name || it?.title || '');
      console.log('  url:', (it?.url || it?.link || '').slice(0, 110));
      console.log('  ', (it?.snippet || '').replace(/\s+/g, ' ').slice(0, 220));
    }
  } catch (e) {
    console.log('ERR search:', e.message);
  }

  console.log('\nVERDICT page_reader-PDF:', pdfTest.ok ? '=== CONTOURNEMENT POSSIBLE ===' : '=== PDF non lisible par page_reader ===');
}

main().catch(e => { console.log('FATAL', e.message); process.exit(1); });
