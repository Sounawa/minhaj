// vlm-qa-19295.ts — lecture VLM des captures QA (règle ai)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function read(path: string, label: string) {
  const zai = await ZAI.create();
  const b64 = fs.readFileSync(path).toString('base64');
  const res = await zai.chat.completions.create({
    messages: [
      { role: 'system', content: 'Tu es contrôleur QA d’une page de lecture bilingue FR/AR (cours scolaire). Réponds en 4 lignes maximum au format: VERDICT: OK ou PROBLEME; puis raison courte.' },
      { role: 'user', content: [
        { type: 'text', text: `Capture ${label} de la leçon 19295 « Le tawqīt : le processus d’extraction de la manzila du Soleil pour toute date ». Vérifie: (1) le contenu FR de leçon est lisible et structuré (h1, sections, tableaux de vers); (2) pas de texte cassé/superposé; (3) le rendu bilingue FR/AR est standard (deux colonnes desktop, empilées mobile); (4) pas de débordement visible.` },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } }
      ] as any }
    ],
    thinking: { type: 'disabled' }
  } as any);
  console.log(`=== ${label} ===`);
  console.log(res.choices[0]?.message?.content);
}

async function main() {
  await read('/home/z/my-project/tr-tmp/qa-19295-desktop.png', 'DESKTOP 1280×900 (full)');
  await read('/home/z/my-project/tr-tmp/qa-19295-mobile.png', 'MOBILE 390×844 (full)');
}
main().catch(e => { console.error(e); process.exit(1); });
