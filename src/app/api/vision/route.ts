import { NextRequest, NextResponse } from "next/server";
import ZAI from "z-ai-web-dev-sdk";

export const runtime = "nodejs";
export const maxDuration = 120;

export async function POST(req: NextRequest) {
  try {
    const { image, prompt } = (await req.json()) as { image?: string; prompt?: string };

    if (!image) {
      return NextResponse.json({ error: "An image is required" }, { status: 400 });
    }

    const question =
      prompt?.trim() ||
      "Describe this image in detail: the scene, objects, people, colors, mood, and any notable text.";

    const zai = await ZAI.create();
    const response = await zai.chat.completions.createVision({
      model: "glm-4.6v",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: question },
            { type: "image_url", image_url: { url: image } },
          ],
        },
      ],
      thinking: { type: "disabled" },
    });

    const analysis: string | undefined = response?.choices?.[0]?.message?.content;
    if (!analysis) {
      return NextResponse.json(
        { error: "Vision analysis returned no content. Please retry." },
        { status: 502 }
      );
    }

    return NextResponse.json({ analysis });
  } catch (err) {
    console.error("[vision] error:", err);
    return NextResponse.json(
      { error: "Vision analysis failed. Please retry with a smaller image." },
      { status: 500 }
    );
  }
}
