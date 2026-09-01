#!/usr/bin/env python3
"""Build a fully standalone HTML document (with <!DOCTYPE>, <html>, <head>,
<body>) from the already-built index.html fragment, for hosting on a real
static host (GitHub Pages) where nothing wraps the file for us the way the
Artifact tool does. Without a doctype the browser renders in Quirks Mode and
without a <meta name="viewport"> tag mobile browsers fall back to a virtual
~980px layout viewport and scale the whole page down -- which is exactly the
"broken margins on mobile" bug this fixes.

Run after build.py (needs index.html to already exist)."""
import logo_b64

with open('index.html', 'r', encoding='utf-8') as f:
    fragment = f.read()

MARKER = '</style>'
idx = fragment.find(MARKER)
if idx == -1:
    raise SystemExit("Couldn't find </style> marker in index.html fragment")
idx += len(MARKER)

head_extra = fragment[:idx]   # <title>...</title> + <link preconnect...> + <style>...</style>
body_content = fragment[idx:]  # rest: body markup + <script>...</script>

favicon_uri = 'data:image/png;base64,' + logo_b64.favicon_64
apple_touch_uri = 'data:image/png;base64,' + logo_b64.favicon_180

doc = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Neorigen — casas prediseñadas sustentables. Modelos, terminaciones y proceso de construcción llave en mano.">
<link rel="icon" type="image/png" href="{favicon_uri}">
<link rel="apple-touch-icon" href="{apple_touch_uri}">
{head_extra}
</head>
<body>
{body_content}
</body>
</html>
'''

with open('github_export/index.html', 'w', encoding='utf-8') as f:
    f.write(doc)

print('Standalone doc written to github_export/index.html')
print('Final size (bytes):', len(doc.encode('utf-8')))
