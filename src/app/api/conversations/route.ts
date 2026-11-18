import { NextResponse } from "next/server";
import { db } from "@/lib/db";

export const runtime = "nodejs";

export async function GET() {
  try {
    const conversations = await db.conversation.findMany({
      orderBy: { updatedAt: "desc" },
      take: 50,
      include: { _count: { select: { messages: true } } },
    });
    return NextResponse.json({ conversations });
  } catch (err) {
    console.error("[conversations] list error:", err);
    return NextResponse.json({ conversations: [] });
  }
}
