import { NextRequest, NextResponse } from "next/server";
import ZAI from "z-ai-web-dev-sdk";
import crypto from "crypto";
import fs from "fs/promises";
import path from "path";
import { db } from "@/lib/db";

export const runtime = "nodejs";
export const maxDuration = 120;

const AUDIO_DIR = path.join(process.cwd(), "generated-audio");
const MAX_CHARS = 800;

export async function POST(req: NextRequest) {
  try {
    const { text, voice, speed } = (await req.json()) as {
      text?: string;
      voice?: string;
      speed?: number;
    };

    if (!text?.trim()) {
      return NextResponse.json({ error: "Text is required" }, { status: 400 });
    }
    if (text.length > MAX_CHARS) {
      return NextResponse.json(
        { error: `Text too long (${text.length} chars). Max ${MAX_CHARS} characters.` },
        { status: 400 }
      );
    }

    const useVoice = voice || "tongtong";
    const useSpeed = Math.min(2, Math.max(0.5, Number(speed) || 1));

    const zai = await ZAI.create();
    const response = await zai.audio.tts.create({
      input: text.trim(),
      voice: useVoice,
      speed: useSpeed,
      response_format: "wav",
      stream: false,
    });

    const arrayBuffer = await response.arrayBuffer();
    const buffer = Buffer.from(new Uint8Array(arrayBuffer));
    if (buffer.length < 100) {
      return NextResponse.json({ error: "TTS returned empty audio. Please retry." }, { status: 502 });
    }

    await fs.mkdir(AUDIO_DIR, { recursive: true });
    const fileName = `tts-${Date.now()}-${crypto.randomBytes(3).toString("hex")}.wav`;
    await fs.writeFile(path.join(AUDIO_DIR, fileName), buffer);

    // Estimate duration: 16kHz mono 16-bit ≈ 32KB/s; be conservative
    const durationSec = Math.max(1, Math.round(buffer.length / 32000));

    await db.speechRecord.create({
      data: {
        kind: "tts",
        input: text.trim().slice(0, 500),
        voice: useVoice,
        speed: useSpeed,
        fileName,
        duration: durationSec,
      },
    });

    const audioDataUrl = `data:audio/wav;base64,${buffer.toString("base64")}`;
    return NextResponse.json({ audio: audioDataUrl, duration: durationSec, fileName });
  } catch (err) {
    console.error("[tts] error:", err);
    return NextResponse.json(
      { error: "Text-to-speech failed. Please retry." },
      { status: 500 }
    );
  }
}
