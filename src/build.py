#!/usr/bin/env python3
"""Build index.html from template.html by substituting {{PLACEHOLDER}} tokens
with base64 data URIs from logo_b64.py and img_b64.py. Pure mechanical
string substitution -- no manual retyping of any binary data."""
import logo_b64
import img_b64

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

def png_uri(raw_b64):
    if raw_b64.startswith('data:'):
        return raw_b64
    return 'data:image/png;base64,' + raw_b64

replacements = {
    '{{LOGO_WORDMARK_WHITE}}': png_uri(logo_b64.logo_wordmark_white),
    '{{LOGO_WORDMARK_NAVY}}': png_uri(logo_b64.logo_wordmark_navy),
    '{{LOGO_ICON_WHITE}}': png_uri(logo_b64.logo_icon_white),
    '{{LOGO_ICON_NAVY}}': png_uri(logo_b64.logo_icon_navy),

    '{{IMG_CASA_LINGUE}}': img_b64.casa_lingue,
    '{{IMG_CASA_HUINGAN}}': img_b64.casa_huingan,
    '{{IMG_CASA_PEUMO}}': img_b64.casa_peumo,
    '{{IMG_CASA_BOLDO}}': img_b64.casa_boldo,
    '{{IMG_CASA_HUINGAN_FAMILIAR}}': img_b64.casa_huingan_familiar,
    '{{IMG_CASA_ROBLE}}': img_b64.casa_roble,
    '{{IMG_CASA_MAITEN}}': img_b64.casa_maiten,
    '{{IMG_CASA_COIHUE}}': img_b64.casa_coihue,

    '{{IMG_CUSTOM_1}}': img_b64.custom_1,
    '{{IMG_CUSTOM_2}}': img_b64.custom_2,
    '{{IMG_CUSTOM_3}}': img_b64.custom_3,

    '{{IMG_GALERIA_1}}': img_b64.galeria_1,
    '{{IMG_GALERIA_2}}': img_b64.galeria_2,
    '{{IMG_GALERIA_3}}': img_b64.galeria_3,
    '{{IMG_GALERIA_4}}': img_b64.galeria_4,

    '{{IMG_SITE_GALLERY_1}}': img_b64.site_gallery_1,
    '{{IMG_SITE_GALLERY_2}}': img_b64.site_gallery_2,
    '{{IMG_SITE_GALLERY_3}}': img_b64.site_gallery_3,
    '{{IMG_SITE_GALLERY_4}}': img_b64.site_gallery_4,

    '{{IMG_KIT_VENTANA}}': img_b64.kit_ventana,
    '{{IMG_KIT_ALBAYALDE}}': img_b64.kit_albayalde,
    '{{IMG_KIT_COCINA}}': img_b64.kit_cocina,
    '{{IMG_KIT_ESTUFA}}': img_b64.kit_estufa,
    '{{IMG_KIT_DUCHA}}': img_b64.kit_ducha,
    '{{IMG_KIT_TERRAZA}}': img_b64.kit_terraza,
    '{{IMG_KIT_PISO}}': img_b64.kit_piso,
    '{{IMG_KIT_METAL}}': img_b64.kit_metal,

    '{{IMG_PLANO_LINGUE}}': img_b64.plano_lingue,
    '{{IMG_PLANO_HUINGAN}}': img_b64.plano_huingan,
    '{{IMG_PLANO_PEUMO}}': img_b64.plano_peumo,
    '{{IMG_PLANO_BOLDO}}': img_b64.plano_boldo,
    '{{IMG_PLANO_HUINGAN_FAMILIAR}}': img_b64.plano_huingan_familiar,
    '{{IMG_PLANO_ROBLE}}': img_b64.plano_roble,
    '{{IMG_PLANO_MAITEN}}': img_b64.plano_maiten,
    '{{IMG_PLANO_COIHUE}}': img_b64.plano_coihue,
}

counts = {}
for placeholder, value in replacements.items():
    counts[placeholder] = html.count(placeholder)
    html = html.replace(placeholder, value)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Substitution counts:")
for k, v in counts.items():
    print(f"  {k}: {v}")

remaining = [p for p in replacements if p in html]
print("Remaining unsubstituted placeholders:", remaining)

import re
leftover = re.findall(r'\{\{[A-Z_0-9]+\}\}', html)
print("Any other {{...}} tokens left:", set(leftover))

print("Final size (bytes):", len(html.encode('utf-8')))
