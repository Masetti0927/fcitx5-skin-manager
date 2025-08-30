# theme_utils.py
import locale
import os
from config import THEME_DIRS

def read_metadata(path):
    metadata = {}
    lang = locale.getlocale()
    if not os.path.isfile(path):
        return metadata
    with open(path, encoding="utf-8") as f:
        in_meta = False
        for line in f:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                in_meta = (line == "[Metadata]")
                continue
            if in_meta and "=" in line:
                key, value = line.split("=", 1)
                metadata[key.strip()] = value.strip()
    localized_key = f"Name[{lang[0]}]"
    display_name = metadata.get(localized_key) or metadata.get("Name")
    metadata["Author"] = metadata.get("Author", "unknown")
    metadata["DisplayName"] = display_name
    metadata["Description"] = metadata.get("Description", "")
    return metadata

def get_themes():
    themes = []
    for theme_dir in THEME_DIRS:
        if not os.path.isdir(theme_dir):
            continue
        for folder in os.listdir(theme_dir):
            conf_path = os.path.join(theme_dir, folder, "theme.conf")
            meta = read_metadata(conf_path)
            if meta:
                themes.append((meta["DisplayName"],meta["Author"],meta["Description"],os.path.join(theme_dir, folder)))
    return themes
