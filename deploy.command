#!/bin/bash
cd "$(dirname "$0")"
echo "Subiendo cambios de Neorigen a GitHub (NEORIGEN)..."
echo ""

# Si Claude dejo un titulo preparado para este cambio, se usa ese. Se lee y
# se borra ANTES de "git add -A" para que el archivo nunca quede rastreado
# por git (no aparece como archivo en el commit).
MSG_FILE=".next_commit_message.txt"
MSG=""
if [ -f "$MSG_FILE" ]; then
  MSG=$(cat "$MSG_FILE")
  rm -f "$MSG_FILE"
fi

git add -A
if git diff --cached --quiet; then
  echo "No hay cambios nuevos para subir."
else
  if [ -n "$MSG" ]; then
    git commit -m "$MSG"
  else
    echo "Escribe una frase corta describiendo el cambio (o deja vacio para usar solo la fecha):"
    read -p "> " MSG
    if [ -z "$MSG" ]; then
      git commit -m "Actualizacion $(date '+%Y-%m-%d %H:%M')"
    else
      git commit -m "$MSG ($(date '+%Y-%m-%d %H:%M'))"
    fi
  fi
  echo ""
  git push
fi
echo ""
echo "Listo. Revisa arriba si dice algun error."
echo "Puedes cerrar esta ventana."
read -p "Presiona Enter para salir..."
