import os
import glob
import fileinput
import re

def update_group_name(xmp_file):
    # Nastavte nový název skupiny
    new_group_name = "@film.presets"

    # Přečíst obsah XMP souboru
    with open(xmp_file, 'r') as file:
        xmp_content = file.read()

    # Nahradit starý název skupiny novým názvem
    updated_xmp_content = re.sub(r'<crs:Group>\s+<rdf:Alt>\s+<rdf:li xml:lang="x-default">.*?</rdf:li>\s+</rdf:Alt>\s+</crs:Group>', '<crs:Group>\n    <rdf:Alt>\n      <rdf:li xml:lang="x-default">{}</rdf:li>\n    </rdf:Alt>\n  </crs:Group>'.format(new_group_name), xmp_content, flags=re.DOTALL)

    # Zapsat aktualizovaný obsah zpět do XMP souboru
    with open(xmp_file, 'w') as file:
        file.write(updated_xmp_content)

# Cesta ke složce s presety
preset_directory = r'C:\Users\Kuba\AppData\Roaming\Adobe\CameraRaw\Settings\@film.presets'

# Vyhledat všechny XMP soubory v dané složce
xmp_files = glob.glob(os.path.join(preset_directory, '*.xmp'))

# Hromadně aktualizovat názvy skupin v XMP souborech
for xmp_file in xmp_files:
    update_group_name(xmp_file)
