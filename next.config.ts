import type { NextConfig } from "next";

// R603 — parade recyclage sandbox : node_modules du projet vit à /home/z/node_modules
// (racine stable hors-arbre ; l'arbre my-project est balayé par le nettoyeur du driver).
// Turbopack refusant de résoudre hors de sa racine détectée, on fixe root=/home/z.
// R606 (ouvrier A) : la cause réelle des vidages = NoSpaceLeft (disque 100 % plein :
// bundles de sûreté 3,1 Go + caches) — purgée, node_modules local survit ;
// turbopack.root retiré (il casse l'hydration client quand node_modules est local).
const nextConfig: NextConfig = {
  output: "standalone",
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
};

export default nextConfig;
