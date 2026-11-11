import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const fs = await import('fs');
  const b64 = fs.readFileSync('tr-tmp/al-aaraf-29-x8.png').toString('base64');
  // Pass 1: free transcription
  const r1 = await zai.chat.completions.create({
    messages: [
      { role: 'system', content: 'Tu es un expert en lecture de manuscrits coraniques en écriture maghrébine (Warsh). Transcris EXACTEMENT le texte de l\'image, lettre par lettre, avec les diacritiques. Indique aussi les ornements de fin de verset (rosettes ۝) s\'il y en a.' },
      { role: 'user', content: [
        { type: 'text', text: 'Transcris ce fragment coranique (image agrandie 8x d\'un bloc coranique d\'un manuel marocain). Donne la transcription exacte en graphie standard.' },
        { type: 'image_url', image_url: { url: 'data:image/png;base64,' + b64 } }
      ]}
    ],
    temperature: 0.1, max_tokens: 400
  });
  console.log('PASS1:', r1.choices[0].message.content);
}
main().catch(e => console.error('ERR', e.message));
