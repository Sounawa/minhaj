import { NextResponse } from "next/server";
import { db } from "@/lib/db";

export const runtime = "nodejs";

export async function GET() {
  try {
    const [conversations, messages, images, ttsCount, asrCount, searches, recentImages, recentSearches] =
      await Promise.all([
        db.conversation.count(),
        db.message.count(),
        db.imageGen.count(),
        db.speechRecord.count({ where: { kind: "tts" } }),
        db.speechRecord.count({ where: { kind: "asr" } }),
        db.searchRecord.count(),
        db.imageGen.findMany({ orderBy: { createdAt: "desc" }, take: 6 }),
        db.searchRecord.findMany({ orderBy: { createdAt: "desc" }, take: 5 }),
      ]);

    return NextResponse.json({
      stats: {
        conversations,
        messages,
        images,
        tts: ttsCount,
        asr: asrCount,
        searches,
      },
      recentImages,
      recentSearches,
    });
  } catch (err) {
    console.error("[stats] error:", err);
    return NextResponse.json({
      stats: { conversations: 0, messages: 0, images: 0, tts: 0, asr: 0, searches: 0 },
      recentImages: [],
      recentSearches: [],
    });
  }
}
