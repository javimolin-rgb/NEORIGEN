#!/bin/bash
cd "$(dirname "$0")"
echo "======================================"
echo " Diagnóstico de deploy — Neorigen"
echo "======================================"
echo ""
echo "--- git status ---"
git status
echo ""
echo "--- ultimos 8 commits (local) ---"
git log --oneline -8
echo ""
echo "--- commits locales que le faltan al remoto (origin/main) ---"
git log origin/main..HEAD --oneline
echo ""
echo "--- remoto configurado ---"
git remote -v
echo ""
echo "--- probando git push ---"
git push
echo ""
echo "======================================"
echo "Listo. Selecciona TODO el texto de esta ventana (Cmd+A),"
echo "cópialo (Cmd+C) y pégamelo en el chat."
echo "======================================"
read -p "Presiona Enter para salir..."
