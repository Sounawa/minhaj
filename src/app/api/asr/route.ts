import { NextRequest, NextResponse } from "next/server";
import ZAI from "z-ai-web-dev-sdk";
import { db } from "@/lib/db";

export const runtime = "nodejs";
export const maxDuration = 120;

export async function POST(req: NextRequest) {
  try {
    const { audioBase64, fileName } = (await req.json()) as {
      audioBase64?: string;
      fileName?: string;
    };

    if (!audioBase64) {
      return NextResponse.json({ error: "Audio file is required" }, { status: 400 });
    }

    // Strip data-URL prefix if present
    const b64 = audioBase64.includes(",") ? audioBase64.split(",")[1] : audioBase64;

    const zai = await ZAI.create();
    const response = await zai.audio.asr.create({
      file_base64: b64,
    });

    const text: string | undefined = response?.text;
    if (!text?.trim()) {
      return NextResponse.json(
        { error: "No speech detected in the audio. Try a clearer recording." },
        { status: 422 }
      );
    }

    await db.speechRecord.create({
      data: {
        kind: "asr",
        input: text.trim().slice(0, 1000),
      },
    });

    return NextResponse.json({ text, sourceName: fileName || "recording" });
  } catch (err) {
    console.error("[asr] error:", err);
    return NextResponse.json(
      { error: "Transcription failed. Check the audio format (wav/mp3/m4a) and retry." },
      { status: 500 }
    );
  }
}
