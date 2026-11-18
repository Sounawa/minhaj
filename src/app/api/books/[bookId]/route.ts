import { NextResponse } from "next/server";
import { getBookDetail } from "@/lib/minhaj";

export const dynamic = "force-dynamic";

export async function GET(
  _req: Request,
  { params }: { params: Promise<{ bookId: string }> }
) {
  const { bookId } = await params;
  try {
    const detail = await getBookDetail(bookId);
    if (!detail) {
      return NextResponse.json(
        { error: "not_found", message: `Manuel ${bookId} introuvable.` },
        { status: 404 }
      );
    }
    return NextResponse.json(detail, { headers: { "Cache-Control": "no-store" } });
  } catch (e) {
    return NextResponse.json(
      { error: "book_unavailable", message: e instanceof Error ? e.message : String(e) },
      { status: 503 }
    );
  }
}
