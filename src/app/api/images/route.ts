import { NextRequest, NextResponse } from "next/server";
import ZAI from "z-ai-web-dev-sdk";
import fs from "fs/promises";
import path from "path";
import crypto from "crypto";
import { db } from "@/lib/db";

export const runtime = "nodejs";
export const maxDuration = 300;

const IMAGES_DIR = path.join(process.cwd(), "generated-images");
const VALID_SIZES = ["1024x1024", "768x1344", "864x1152", "1344x768", "1152x864", "1440x720", "720x1440"];

export async function GET() {
  try {
    const images = await db.imageGen.findMany({
      orderBy: { createdAt: "desc" },
      take: 60,
    });
    return NextResponse.json({ images });
  } catch (err) {
    console.error("[images] list error:", err);
    return NextResponse.json({ images: [] });
  }
}

export async function POST(req: NextRequest) {
  try {
    const { prompt, size } = (await req.json()) as { prompt?: string; size?: string };

    if (!prompt?.trim()) {
      return NextResponse.json({ error: "Prompt is required" }, { status: 400 });
    }

    const imgSize = VALID_SIZES.includes(size || "") ? size! : "1024x1024";

    const zai = await ZAI.create();
    const response = await zai.images.generations.create({
      prompt: prompt.trim(),
      size: imgSize as "1024x1024",
    });

    const base64 = response?.data?.[0]?.base64;
    if (!base64) {
      return NextResponse.json(
        { error: "Image generation returned no data. Try rephrasing your prompt." },
        { status: 502 }
      );
    }

    await fs.mkdir(IMAGES_DIR, { recursive: true });
    const fileName = `img-${Date.now()}-${crypto.randomBytes(4).toString("hex")}.png`;
    const filePath = path.join(IMAGES_DIR, fileName);
    await fs.writeFile(filePath, Buffer.from(base64, "base64"));

    const record = await db.imageGen.create({
      data: {
        prompt: prompt.trim(),
        size: imgSize,
        filePath: fileName,
      },
    });

    return NextResponse.json({ image: record });
  } catch (err) {
    console.error("[images] generate error:", err);
    return NextResponse.json(
      { error: "Image generation failed. The service may be busy — please retry." },
      { status: 500 }
    );
  }
}
