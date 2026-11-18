import { NextResponse } from "next/server";
import { db } from "@/lib/db";

export const runtime = "nodejs";

export async function GET() {
  try {
    const records = await db.speechRecord.findMany({
      orderBy: { createdAt: "desc" },
      take: 30,
    });
    return NextResponse.json({ records });
  } catch (err) {
    console.error("[speech] list error:", err);
    return NextResponse.json({ records: [] });
  }
}
