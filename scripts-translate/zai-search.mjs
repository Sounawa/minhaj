// Recherche web via z-ai-web-dev-sdk — usage: node zai-search.mjs "requête" [num]
import ZAI from 'z-ai-web-dev-sdk';
const [,, query, num] = process.argv;
if (!query) { console.error('usage: node zai-search.mjs "query" [num]'); process.exit(1); }
const zai = await ZAI.create();
const res = await zai.functions.invoke('search', { query, num: num ? Number(num) : 8 });
const items = Array.isArray(res) ? res : (res?.results || []);
for (const it of items) {
  console.log(`[${it.rank}] ${it.name}\n    ${it.url}\n    ${it.host_name} | ${it.date || ''}\n    ${(it.snippet || '').replace(/\s+/g, ' ').slice(0, 400)}\n`);
}
