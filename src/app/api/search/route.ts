import { NextRequest, NextResponse } from "next/server";
import { searchCorpus } from "@/lib/minhaj";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  const q = req.nextUrl.searchParams.get("q") ?? "";
  const limitRaw = Number(req.nextUrl.searchParams.get("limit") ?? "25");
  const limit = Number.isFinite(limitRaw) ? Math.min(Math.max(Math.trunc(limitRaw), 5), 50) : 25;
  if (q.trim().length < 2) {
    return NextResponse.json(
      { query: q, total: 0, truncated: false, hits: [] },
      { headers: { "Cache-Control": "no-store" } }
    );
  }
  try {
    const payload = await searchCorpus(q, limit);
    return NextResponse.json(payload, { headers: { "Cache-Control": "no-store" } });
  } catch (e) {
    return NextResponse.json(
      { error: "search_failed", message: e instanceof Error ? e.message : String(e) },
      { status: 500 }
    );
  }
}
