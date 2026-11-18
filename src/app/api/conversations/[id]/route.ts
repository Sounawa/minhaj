import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";

export const runtime = "nodejs";

type Ctx = { params: Promise<{ id: string }> };

export async function GET(_req: NextRequest, ctx: Ctx) {
  try {
    const { id } = await ctx.params;
    const conversation = await db.conversation.findUnique({
      where: { id },
      include: { messages: { orderBy: { createdAt: "asc" } } },
    });
    if (!conversation) {
      return NextResponse.json({ error: "Not found" }, { status: 404 });
    }
    return NextResponse.json({ conversation });
  } catch (err) {
    console.error("[conversation] get error:", err);
    return NextResponse.json({ error: "Failed to load conversation" }, { status: 500 });
  }
}

export async function DELETE(_req: NextRequest, ctx: Ctx) {
  try {
    const { id } = await ctx.params;
    await db.conversation.delete({ where: { id } });
    return NextResponse.json({ ok: true });
  } catch (err) {
    console.error("[conversation] delete error:", err);
    return NextResponse.json({ error: "Failed to delete conversation" }, { status: 500 });
  }
}

export async function PATCH(req: NextRequest, ctx: Ctx) {
  try {
    const { id } = await ctx.params;
    const { title } = (await req.json()) as { title?: string };
    if (!title?.trim()) {
      return NextResponse.json({ error: "Title required" }, { status: 400 });
    }
    const updated = await db.conversation.update({
      where: { id },
      data: { title: title.trim().slice(0, 80) },
    });
    return NextResponse.json({ conversation: updated });
  } catch (err) {
    console.error("[conversation] rename error:", err);
    return NextResponse.json({ error: "Failed to rename" }, { status: 500 });
  }
}
