"use client";

import { createElement } from "react";
import {
  AudioLines,
  BookOpenText,
  Brain,
  Compass,
  Feather,
  Landmark,
  Languages,
  Library,
  MessagesSquare,
  Scale,
  ScrollText,
  Sparkles,
  type LucideIcon,
} from "lucide-react";
import { cn } from "@/lib/utils";

const SUBJECT_ICONS: Record<string, LucideIcon> = {
  tawhid: Sparkles,
  fiqh: Scale,
  sira: ScrollText,
  tajwid: AudioLines,
  tafsir: BookOpenText,
  nahu: Languages,
  hadith: MessagesSquare,
  mantiq: Brain,
  faraid: Landmark,
  balagha: Feather,
  "usul-fiqh": Compass,
  adab: Library,
};

export function subjectIcon(subjectId: string): LucideIcon {
  return SUBJECT_ICONS[subjectId] ?? BookOpenText;
}

/** Tuile d'icône « automne » avec dégradé chaud par matière. */
const TILE_GRADIENTS: Record<string, string> = {
  tawhid: "from-amber-500/90 to-orange-700/90",
  fiqh: "from-orange-600/90 to-red-800/80",
  sira: "from-yellow-600/85 to-amber-800/90",
  tajwid: "from-rose-500/80 to-orange-700/90",
  tafsir: "from-amber-600/90 to-yellow-800/85",
  nahu: "from-lime-600/70 to-amber-700/90",
  hadith: "from-orange-500/85 to-amber-800/90",
  mantiq: "from-teal-600/60 to-amber-700/90",
  faraid: "from-amber-700/90 to-stone-700/90",
  balagha: "from-orange-400/90 to-amber-700/90",
  "usul-fiqh": "from-amber-500/85 to-orange-800/85",
  adab: "from-yellow-500/85 to-orange-700/90",
};

export function SubjectTile({
  subjectId,
  className,
  iconClassName,
}: {
  subjectId: string;
  className?: string;
  iconClassName?: string;
}) {
  return (
    <span
      aria-hidden="true"
      className={cn(
        "inline-flex items-center justify-center rounded-xl bg-gradient-to-br text-amber-50 shadow-sm ring-1 ring-amber-900/10",
        TILE_GRADIENTS[subjectId] ?? "from-amber-600/90 to-orange-800/90",
        className
      )}
    >
      {createElement(subjectIcon(subjectId), {
        className: cn("size-5", iconClassName),
        strokeWidth: 1.9,
      })}
    </span>
  );
}
