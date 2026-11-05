import type { NextConfig } from "next";
import path from "path";

// R603 — parade recyclage sandbox : node_modules du projet vit à /home/z/node_modules
// (racine stable hors-arbre ; l'arbre my-project est balayé par le nettoyeur du driver).
// Turbopack refusant de résoudre hors de sa racine détectée, on fixe root=/home/z.
const nextConfig: NextConfig = {
  output: "standalone",
  turbopack: {
    root: path.join(__dirname, ".."),
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
};

export default nextConfig;
