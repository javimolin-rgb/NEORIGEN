#!/bin/bash
cd "$(dirname "$0")"
echo "Este script reescribe los titulos de los commits antiguos (los que dicen"
echo "'Actualizacion <fecha> <hora>') por titulos que describen el cambio real,"
echo "y despues fuerza el push a GitHub. Los hash de los commits van a cambiar."
echo ""
read -p "Presiona Enter para continuar, o cierra esta ventana para cancelar..."
echo ""

export FILTER_BRANCH_SQUELCH_WARNING=1

git filter-branch -f --msg-filter '
sha="$GIT_COMMIT"
case "$sha" in
  89c1a76ace604ed43dbab803a99c9c4ce075703f)
    echo "Agregar script de despliegue (deploy.command)" ;;
  ccf0c2c237a23e23172e0ab50d2a19ac77d03515)
    echo "Espaciados y lineas consistentes en el menu movil (drawer)" ;;
  10d0f6d383fe598fdae7b2ed6a1714e65f3e6cd1)
    echo "Cambiar \"prefabricada\" por \"prediseñada\" en todo el sitio" ;;
  c8e0497def5785dff40d316ce74d9a568cbb8ec9)
    echo "Transicion mas suave entre paginas + fondo navy menos oscuro" ;;
  c6be216fd3776f3e25b5e783028b4f667beda7e9)
    echo "Foto circular del hero mas grande + banners internos mas cortos" ;;
  a66f2149d99c3593234a52b634ceb94abb140cf8)
    echo "Rediseno del hero: foto a pantalla completa en todos los tamaños" ;;
  ed5468545d24674cc0d90fd809d262d32de7c78c)
    echo "Foto del hero en alta resolucion (Casa Roble) + logo del footer mas grande" ;;
  6a994258044daa2e7346a28802a121d380a9cff8)
    echo "Quitar sello flotante del hero + reforzar degrade en mobile" ;;
  *)
    cat ;;
esac
' -- --all

echo ""
echo "Historial reescrito localmente. Subiendo a GitHub con push forzado..."
git push --force-with-lease

echo ""
echo "Listo. Revisa arriba si dice algun error."
echo "Puedes cerrar esta ventana."
read -p "Presiona Enter para salir..."
