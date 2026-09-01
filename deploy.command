#!/bin/bash
cd "$(dirname "$0")"
echo "Subiendo cambios de Neorigen a GitHub (NEORIGEN)..."
echo ""
git add -A
if git diff --cached --quiet; then
  echo "No hay cambios nuevos para subir."
else
  git commit -m "Actualizacion $(date '+%Y-%m-%d %H:%M')"
  echo ""
  git push
fi
echo ""
echo "Listo. Revisa arriba si dice algun error."
echo "Puedes cerrar esta ventana."
read -p "Presiona Enter para salir..."
