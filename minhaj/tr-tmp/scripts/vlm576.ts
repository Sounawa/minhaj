import ZAI, { VisionMessage } from 'z-ai-web-dev-sdk';
import { readFileSync } from 'fs';

// Usage: bun tr-tmp/scripts/vlm576.ts <image.png> "<prompt>"
async function main(path: string, prompt: string) {
	try {
		const b64 = readFileSync(path).toString('base64');
		const zai = await ZAI.create();
		const messages: VisionMessage[] = [
			{
				role: 'user',
				content: [
					{ type: 'text', text: prompt },
					{ type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } }
				]
			}
		];
		const response = await zai.chat.completions.createVision({
			model: 'glm-4.6v',
			messages,
			thinking: { type: 'disabled' }
		});
		const reply = response.choices?.[0]?.message?.content;
		console.log(reply ?? JSON.stringify(response, null, 2));
	} catch (err: any) {
		console.error('Vision chat failed:', err?.message || err);
	}
}
main(process.argv[2], process.argv[3] ?? 'Transcribe exactly what is written.');
