"use client";

import { useState } from "react";
import {
  Sparkles,
  MessageSquare,
  ImageIcon,
  ScanEye,
  AudioLines,
  Globe,
  Sun,
  Moon,
  Zap,
} from "lucide-react";
import { useTheme } from "next-themes";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import DashboardPanel from "./dashboard-panel";
import ChatPanel from "./chat-panel";
import ImagePanel from "./image-panel";
import VisionPanel from "./vision-panel";
import SpeechPanel from "./speech-panel";
import SearchPanel from "./search-panel";

export type PanelKey = "dashboard" | "chat" | "images" | "vision" | "speech" | "search";

const NAV_ITEMS: {
  key: PanelKey;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  hint: string;
}[] = [
  { key: "dashboard", label: "Dashboard", icon: Sparkles, hint: "Overview & activity" },
  { key: "chat", label: "AI Chat", icon: MessageSquare, hint: "LLM conversations" },
  { key: "images", label: "Image Gen", icon: ImageIcon, hint: "Text to image" },
  { key: "vision", label: "Vision", icon: ScanEye, hint: "Image understanding" },
  { key: "speech", label: "Speech", icon: AudioLines, hint: "TTS & transcription" },
  { key: "search", label: "Web Search", icon: Globe, hint: "Search & page reader" },
];

export default function StudioShell() {
  const [panel, setPanel] = useState<PanelKey>("dashboard");
  const { theme, setTheme } = useTheme();

  const activeItem = NAV_ITEMS.find((n) => n.key === panel)!;

  return (
    <div className="min-h-screen flex flex-col bg-background">
      {/* ── Header ─────────────────────────────────────────── */}
      <header className="sticky top-0 z-40 border-b bg-background/85 backdrop-blur supports-[backdrop-filter]:bg-background/70">
        <div className="mx-auto flex h-14 max-w-[1400px] items-center gap-3 px-4 sm:px-6">
          <div className="flex items-center gap-2.5">
            <div className="flex size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground shadow-sm">
              <Zap className="size-4.5" />
            </div>
            <div className="leading-tight">
              <p className="text-sm font-bold tracking-tight">Nexus AI Studio</p>
              <p className="hidden text-[11px] text-muted-foreground sm:block">
                One workbench · every AI skill
              </p>
            </div>
          </div>

          <div className="ml-auto flex items-center gap-2">
            <Badge variant="accent" className="hidden md:inline-flex">
              <Sparkles className="size-3" />
              Z.ai Skills Inside
            </Badge>
            <Tooltip>
              <TooltipTrigger asChild>
                <Button
                  variant="ghost"
                  size="icon"
                  aria-label="Toggle theme"
                  onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
                >
                  <Sun className="size-4.5 dark:hidden" />
                  <Moon className="hidden size-4.5 dark:block" />
                </Button>
              </TooltipTrigger>
              <TooltipContent>Toggle light / dark</TooltipContent>
            </Tooltip>
          </div>
        </div>

        {/* Mobile nav */}
        <nav
          aria-label="Studio sections"
          className="flex gap-1 overflow-x-auto border-t px-3 py-2 lg:hidden"
        >
          {NAV_ITEMS.map((item) => (
            <button
              key={item.key}
              onClick={() => setPanel(item.key)}
              className={cn(
                "flex shrink-0 items-center gap-1.5 rounded-full px-3.5 py-1.5 text-sm font-medium transition-colors",
                panel === item.key
                  ? "bg-primary text-primary-foreground shadow-sm"
                  : "bg-muted text-muted-foreground hover:bg-accent hover:text-accent-foreground"
              )}
            >
              <item.icon className="size-4" />
              {item.label}
            </button>
          ))}
        </nav>
      </header>

      {/* ── Body ───────────────────────────────────────────── */}
      <div className="mx-auto flex w-full max-w-[1400px] flex-1 gap-0">
        {/* Desktop sidebar */}
        <aside className="sticky top-14 hidden h-[calc(100vh-3.5rem)] w-56 shrink-0 flex-col justify-between border-r py-4 pr-0 lg:flex">
          <nav aria-label="Studio sections" className="flex flex-col gap-1 px-3">
            <p className="mb-1 px-2 text-[11px] font-semibold uppercase tracking-wider text-muted-foreground">
              Workbench
            </p>
            {NAV_ITEMS.map((item) => (
              <button
                key={item.key}
                onClick={() => setPanel(item.key)}
                className={cn(
                  "group flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-all",
                  panel === item.key
                    ? "bg-primary/10 text-primary shadow-[inset_0_0_0_1px_var(--color-primary)/20]"
                    : "text-muted-foreground hover:bg-accent/60 hover:text-accent-foreground"
                )}
              >
                <span
                  className={cn(
                    "flex size-7 items-center justify-center rounded-md transition-colors",
                    panel === item.key
                      ? "bg-primary text-primary-foreground"
                      : "bg-muted group-hover:bg-card"
                  )}
                >
                  <item.icon className="size-4" />
                </span>
                <span className="flex flex-col items-start leading-tight">
                  {item.label}
                  <span className="text-[11px] font-normal text-muted-foreground/80">
                    {item.hint}
                  </span>
                </span>
              </button>
            ))}
          </nav>

          <div className="px-4">
            <div className="rounded-xl border bg-gradient-to-br from-primary/10 via-accent/20 to-transparent p-3.5">
              <p className="text-xs font-semibold">Powered by Skills</p>
              <p className="mt-1 text-[11px] leading-relaxed text-muted-foreground">
                Every panel calls a real AI skill through the Z.ai backend SDK — LLM,
                vision, TTS, ASR, image generation & web tools.
              </p>
            </div>
          </div>
        </aside>

        {/* Main content */}
        <main className="min-w-0 flex-1 pb-10">
          <div key={panel} className="animate-fade-up px-4 pt-5 sm:px-6 lg:pt-6">
            <div className="mb-4 flex items-center gap-2.5">
              <span className="flex size-8 items-center justify-center rounded-lg bg-accent text-accent-foreground">
                <activeItem.icon className="size-4.5" />
              </span>
              <div>
                <h1 className="text-lg font-bold tracking-tight">{activeItem.label}</h1>
                <p className="text-xs text-muted-foreground">{activeItem.hint}</p>
              </div>
            </div>

            {panel === "dashboard" && <DashboardPanel onNavigate={setPanel} />}
            {panel === "chat" && <ChatPanel />}
            {panel === "images" && <ImagePanel />}
            {panel === "vision" && <VisionPanel />}
            {panel === "speech" && <SpeechPanel />}
            {panel === "search" && <SearchPanel />}
          </div>
        </main>
      </div>

      {/* ── Sticky footer ──────────────────────────────────── */}
      <footer className="mt-auto border-t bg-card/60 backdrop-blur">
        <div className="mx-auto flex max-w-[1400px] flex-col items-center justify-between gap-2 px-4 py-4 pb-[calc(1rem+env(safe-area-inset-bottom))] text-xs text-muted-foreground sm:flex-row sm:px-6">
          <p className="flex items-center gap-1.5">
            <Zap className="size-3.5 text-primary" />
            <span className="font-medium text-foreground">Nexus AI Studio</span>
            <span>· © {new Date().getFullYear()} · Built on Next.js & Z.ai Skills</span>
          </p>
          <p className="flex items-center gap-1.5">
            LLM · Vision · TTS · ASR · ImageGen · WebSearch
          </p>
        </div>
      </footer>
    </div>
  );
}
