# Sitio web Neorigen (2026)

Rediseño del sitio web de Neorigen — casas prediseñadas sustentables — entregado como un artefacto HTML autocontenido con enrutamiento por hash (sin dependencias externas ni build step para verlo).

## Estructura

- `index.html` — el sitio final, **documento HTML completo y autocontenido** (con `<!DOCTYPE html>`, `<head>` con `meta charset` + `meta viewport` + favicon, y `<body>`), listo para publicar tal cual en un hosting estático como GitHub Pages. Todas las imágenes van incrustadas como base64 dentro del archivo.
- `src/template.html` — plantilla fuente (fragmento, sin doctype/html/head/body) con placeholders `{{PLACEHOLDER}}` en vez de las imágenes. Es la fuente de verdad para todo el contenido/CSS/JS del sitio.
- `src/build.py` — reemplaza los placeholders de `template.html` con las imágenes en base64 de `img_b64.py` / `logo_b64.py` y genera un `index.html` **fragmento** (pensado para plataformas que envuelven el HTML por su cuenta, como el Artifact de Claude). Se ejecuta con `python3 src/build.py`.
- `src/build_standalone.py` — toma el fragmento generado por `build.py` y lo envuelve en un documento HTML completo (doctype, `<html>`, `<head>` con meta viewport/charset/favicon, `<body>`) — este es el paso que genera el `index.html` de la raíz del repo, el que de verdad se debe publicar. Se ejecuta después de `build.py`, con `python3 src/build_standalone.py` (asume que ya corriste `build.py` y que existe un `index.html` fragmento en el mismo directorio desde el que lo ejecutas).
- `src/img_b64.py` / `src/logo_b64.py` — imágenes y favicon del sitio codificados en base64.
- `assets/planos/` — planos oficiales de cada modelo (fuente: fichas técnicas ya publicadas en neorigen.cl), en la resolución final usada en el sitio.
- `assets/terminaciones/` — fotos de terminaciones/materiales usadas en la sección "Todo lo necesario para vivir bien, desde el primer día." (fuente: ficha oficial de terminaciones de Neorigen).

## Publicar en GitHub Pages

1. Settings → Pages → Deploy from a branch → rama `main`, carpeta `/ (root)`.
2. El sitio queda disponible en `https://<usuario>.github.io/<repo>/`.

## Hero mobile/tablet

En pantallas de hasta 900px de ancho, el hero de portada no usa la foto circular flotante con anillos decorativos que se ve en desktop — esa foto y el tag de "Casa Lingüe · 57 m²" estaban calibrados con offsets porcentuales pensados para una columna angosta de escritorio, y al apilarse a ancho completo terminaban saliéndose de la pantalla (el tag cortaba el texto). En su lugar, en ese rango se usa la misma foto como fondo suave detrás del texto, con un degradado oscuro para mantener la legibilidad — sin elementos flotantes que puedan desbordar.

## Favicon

El ícono de la pestaña es solo el isotipo (el techo/casa) en azul marino (`--navy`, `#011E2F`) sobre fondo transparente — sin tile ni fondo de color detrás.

## Por qué hay dos builds (fragmento vs. documento completo)

El HTML del sitio nació como un **fragmento** (sin `<!DOCTYPE>`/`<html>`/`<head>`/`<body>`) porque así lo requiere el Artifact de Claude, que envuelve el contenido con su propio `<head>` (incluye `meta viewport` automáticamente). Ese mismo fragmento, servido tal cual en GitHub Pages (un hosting estático real que no envuelve nada), hacía que el navegador cayera en **quirks mode** y, en mobile, usara un viewport virtual de ~980px en vez del ancho real de pantalla — eso es lo que causaba los márgenes/proporciones rotas al ver el sitio en el celular. `build_standalone.py` arregla esto agregando el doctype y el `meta viewport` explícitamente para la versión que se publica en este repo.

## Notas

Este export no incluye los archivos de trabajo (PDFs originales, recortes intermedios, capturas de pantalla de QA) — solo el sitio final y los archivos fuente necesarios para reconstruirlo o editarlo.
