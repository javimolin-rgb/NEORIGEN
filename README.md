# Sitio web Neorigen (2026)

Rediseño del sitio web de Neorigen — casas prefabricadas sustentables — entregado como un artefacto HTML autocontenido con enrutamiento por hash (sin dependencias externas ni build step para verlo).

## Estructura

- `index.html` — el sitio final, listo para publicar tal cual (por ejemplo con GitHub Pages). Todas las imágenes van incrustadas como base64 dentro del archivo.
- `src/template.html` — plantilla fuente con placeholders `{{PLACEHOLDER}}` en vez de las imágenes.
- `src/build.py` — script que reemplaza los placeholders de `template.html` con las imágenes en base64 de `img_b64.py` / `logo_b64.py` y genera `index.html`. Se ejecuta con `python3 src/build.py` desde esta carpeta.
- `src/img_b64.py` / `src/logo_b64.py` — imágenes del sitio codificadas en base64.
- `assets/planos/` — planos oficiales de cada modelo (fuente: fichas técnicas ya publicadas en neorigen.cl), en la resolución final usada en el sitio.
- `assets/terminaciones/` — fotos de terminaciones/materiales usadas en la sección "Todo lo necesario para vivir bien, desde el primer día." (fuente: ficha oficial de terminaciones de Neorigen).

## Publicar en GitHub Pages

1. Settings → Pages → Deploy from a branch → rama `main`, carpeta `/ (root)`.
2. El sitio queda disponible en `https://<usuario>.github.io/<repo>/`.

## Notas

Este export no incluye los archivos de trabajo (PDFs originales, recortes intermedios, capturas de pantalla de QA) — solo el sitio final y los archivos fuente necesarios para reconstruirlo o editarlo.
