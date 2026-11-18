"use client";

import { useEffect, useState } from "react";
import {
  MessageSquare,
  ImageIcon,
  AudioLines,
  Globe,
  ScanEye,
  MessagesSquare,
  ArrowRight,
  Loader2,
  RefreshCcw,
} from "lucide-react";
import { toast } from "sonner";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { cn, timeAgo } from "@/lib/utils";
import type { PanelKey } from "./studio-shell";

interface Stats {
  conversations: number;
  messages: number;
  images: number;
  tts: number;
  asr: number;
  searches: number;
}

interface RecentImage {
  id: string;
  prompt: string;
  filePath: string;
  createdAt: string;
}

interface RecentSearch {
  id: string;
  query: string;
  resultCount: number;
  createdAt: string;
}

export default function DashboardPanel({ onNavigate }: { onNavigate: (p: PanelKey) => void }) {
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [stats, setStats] = useState<Stats | null>(null);
  const [recentImages, setRecentImages] = useState<RecentImage[]>([]);
  const [recentSearches, setRecentSearches] = useState<RecentSearch[]>([]);

  const load = async (isRefresh = false) => {
    if (isRefresh) setRefreshing(true);
    try {
      const res = await fetch("/api/stats");
      const data = await res.json();
      setStats(data.stats);
      setRecentImages(data.recentImages || []);
      setRecentSearches(data.recentSearches || []);
      if (isRefresh) toast.success("Dashboard refreshed");
    } catch {
      toast.error("Failed to load stats");
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/stats");
        if (!res.ok || cancelled) return;
        const data = await res.json();
        if (cancelled) return;
        setStats(data.stats);
        setRecentImages(data.recentImages || []);
        setRecentSearches(data.recentSearches || []);
      } catch {
        /* dashboard shows zeros on failure */
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  const cards: {
    key: PanelKey;
    label: string;
    value: number;
    icon: React.ComponentType<{ className?: string }>;
    desc: string;
  }[] = [
    { key: "chat", label: "Conversations", value: stats?.conversations ?? 0, icon: MessageSquare, desc: "Chat threads" },
    { key: "chat", label: "Messages", value: stats?.messages ?? 0, icon: MessagesSquare, desc: "User + AI turns" },
    { key: "images", label: "Images", value: stats?.images ?? 0, icon: ImageIcon, desc: "Generated artwork" },
    { key: "speech", label: "Voice Clips", value: stats?.tts ?? 0, icon: AudioLines, desc: "Text-to-speech" },
    { key: "speech", label: "Transcripts", value: stats?.asr ?? 0, icon: ScanEye, desc: "Speech-to-text" },
    { key: "search", label: "Web Searches", value: stats?.searches ?? 0, icon: Globe, desc: "Queries run" },
  ];

  return (
    <div className="space-y-6">
      {/* Hero */}
      <Card className="studio-grid overflow-hidden">
        <CardContent className="relative flex flex-col gap-4 p-6 sm:flex-row sm:items-center sm:justify-between">
          <div className="max-w-xl">
            <h2 className="text-xl font-bold tracking-tight sm:text-2xl">
              Welcome to your AI workbench ⚡
            </h2>
            <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">
              Chat with an LLM, generate images, analyze pictures, synthesize & transcribe
              speech, and search the live web — all backed by real AI skills and saved
              automatically to your studio history.
            </p>
            <div className="mt-4 flex flex-wrap gap-2">
              <Button size="sm" onClick={() => onNavigate("chat")}>
                <MessageSquare className="size-4" /> Start chatting
              </Button>
              <Button size="sm" variant="outline" onClick={() => onNavigate("images")}>
                <ImageIcon className="size-4" /> Generate an image
              </Button>
            </div>
          </div>
          <div className="hidden shrink-0 lg:block">
            <div className="relative size-36 rounded-2xl border bg-gradient-to-br from-primary/25 via-accent/40 to-chart-3/20 p-1 shadow-inner">
              <div className="flex h-full flex-col items-center justify-center gap-2 rounded-xl bg-card/70">
                <ZapMark />
                <p className="text-[11px] font-medium text-muted-foreground">6 skills · 1 studio</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Stats grid */}
      <div>
        <div className="mb-3 flex items-center justify-between">
          <h3 className="text-sm font-semibold text-muted-foreground">Activity overview</h3>
          <Button
            variant="ghost"
            size="sm"
            onClick={() => load(true)}
            disabled={refreshing}
          >
            {refreshing ? <Loader2 className="size-4 animate-spin" /> : <RefreshCcw className="size-4" />}
            Refresh
          </Button>
        </div>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-6">
          {cards.map((c) => (
            <Card
              key={c.label}
              className="group cursor-pointer transition-all hover:-translate-y-0.5 hover:shadow-md"
              onClick={() => onNavigate(c.key)}
            >
              <CardContent className="flex flex-col gap-2 p-4">
                <span className="flex size-8 items-center justify-center rounded-lg bg-primary/10 text-primary">
                  <c.icon className="size-4" />
                </span>
                {loading ? (
                  <Skeleton className="h-7 w-14" />
                ) : (
                  <p className="text-2xl font-bold tabular-nums tracking-tight">{c.value}</p>
                )}
                <div>
                  <p className="text-xs font-medium">{c.label}</p>
                  <p className="text-[11px] text-muted-foreground">{c.desc}</p>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Recent activity */}
      <div className="grid gap-4 lg:grid-cols-2">
        {/* Recent images */}
        <Card>
          <CardContent className="p-5">
            <div className="mb-3 flex items-center justify-between">
              <h3 className="text-sm font-semibold">Latest generations</h3>
              <Button variant="ghost" size="sm" onClick={() => onNavigate("images")}>
                View all <ArrowRight className="size-3.5" />
              </Button>
            </div>
            {loading ? (
              <div className="grid grid-cols-3 gap-2">
                {Array.from({ length: 3 }).map((_, i) => (
                  <Skeleton key={i} className="aspect-square rounded-lg" />
                ))}
              </div>
            ) : recentImages.length === 0 ? (
              <EmptyHint
                text="No images yet — generate your first artwork from the Image Gen panel."
                onClick={() => onNavigate("images")}
              />
            ) : (
              <div className="grid grid-cols-3 gap-2">
                {recentImages.slice(0, 6).map((img) => (
                  <button
                    key={img.id}
                    onClick={() => onNavigate("images")}
                    className="group relative aspect-square overflow-hidden rounded-lg border"
                  >
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={`/api/images/file/${img.filePath}`}
                      alt={img.prompt.slice(0, 60)}
                      className="h-full w-full object-cover transition-transform group-hover:scale-105"
                      loading="lazy"
                    />
                  </button>
                ))}
              </div>
            )}
          </CardContent>
        </Card>

        {/* Recent searches */}
        <Card>
          <CardContent className="p-5">
            <div className="mb-3 flex items-center justify-between">
              <h3 className="text-sm font-semibold">Recent searches</h3>
              <Button variant="ghost" size="sm" onClick={() => onNavigate("search")}>
                New search <ArrowRight className="size-3.5" />
              </Button>
            </div>
            {loading ? (
              <div className="space-y-2">
                {Array.from({ length: 3 }).map((_, i) => (
                  <Skeleton key={i} className="h-10 w-full" />
                ))}
              </div>
            ) : recentSearches.length === 0 ? (
              <EmptyHint
                text="No searches yet — ask the live web anything from the Web Search panel."
                onClick={() => onNavigate("search")}
              />
            ) : (
              <ul className="space-y-1.5">
                {recentSearches.map((s) => (
                  <li
                    key={s.id}
                    className="flex items-center justify-between gap-3 rounded-lg border bg-muted/40 px-3 py-2"
                  >
                    <span className="truncate text-sm">{s.query}</span>
                    <span className="flex shrink-0 items-center gap-2">
                      <Badge variant="secondary" className="tabular-nums">
                        {s.resultCount} hits
                      </Badge>
                      <span className="text-[11px] text-muted-foreground">
                        {timeAgo(s.createdAt)}
                      </span>
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

function EmptyHint({ text, onClick }: { text: string; onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "flex w-full flex-col items-center justify-center gap-2 rounded-lg border border-dashed px-4 py-8 text-center transition-colors hover:border-primary/50 hover:bg-accent/30"
      )}
    >
      <p className="max-w-xs text-xs text-muted-foreground">{text}</p>
      <span className="text-xs font-medium text-primary">Go →</span>
    </button>
  );
}

function ZapMark() {
  return (
    <svg width="44" height="44" viewBox="0 0 44 44" fill="none" aria-hidden>
      <circle cx="22" cy="22" r="20" className="fill-primary/10" />
      <path
        d="M24 6 12 26h8l-2 12 12-20h-8l2-12Z"
        className="fill-primary"
      />
    </svg>
  );
}
