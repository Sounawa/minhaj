#!/bin/bash
# R592 — chaîne machine atomique (install + build + start) — piège recyclage actif
cd /home/z/my-project
bun install >> tr-logs/build-r592.log 2>&1 || exit 1
echo "INSTALL_OK $(date -u +%H:%M:%SZ)" >> tr-logs/build-r592.log
node_modules/.bin/next build >> tr-logs/build-r592.log 2>&1 || exit 2
cp -r .next/static .next/standalone/.next/ >> tr-logs/build-r592.log 2>&1
cp -r public .next/standalone/ >> tr-logs/build-r592.log 2>&1
echo "BUILD_OK $(date -u +%H:%M:%SZ)" >> tr-logs/build-r592.log
NODE_ENV=production bun .next/standalone/server.js > server.log 2>&1 &
echo "START_OK $(date -u +%H:%M:%SZ)" >> tr-logs/build-r592.log
