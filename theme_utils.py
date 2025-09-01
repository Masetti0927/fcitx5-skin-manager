# theme_utils.py
import locale
import os
import re
from config import THEME_DIRS,THEME_CONF
import dbus

def read_metadata(path):
    metadata = {}
    lang = locale.getlocale()[0]
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
    localized_key = f"Name[{lang}]"
    display_name = metadata.get(localized_key) or metadata.get("Name")
    metadata["Author"] = metadata.get("Author", "unknown")
    metadata["Description"] = metadata.get("Description", "")
    metadata["DisplayName"] = display_name
    return metadata

def get_default_theme():
    conf_path = os.path.expanduser(THEME_CONF)

    # 读取文件内容
    with open(conf_path, encoding='utf-8') as f:
        content = f.read()

    # 用正则提取主题信息
    theme_match = re.search(r'^Theme=(.+)', content, re.MULTILINE)
    # dark_theme_match = re.search(r'^DarkTheme=(.+)', content, re.MULTILINE)

    # 获取值
    theme = theme_match.group(1).strip() if theme_match else None
    # dark_theme = dark_theme_match.group(1).strip() if dark_theme_match else None

    # 输出结果
    print("当前主题:", theme)
    # print("深色主题:", dark_theme)
    return theme

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

def change_theme(theme_folder_name):
    session_bus = dbus.SessionBus()
    fcitx_obj = session_bus.get_object('org.fcitx.Fcitx5', '/controller')
    iface = dbus.Interface(fcitx_obj, dbus_interface='org.fcitx.Fcitx.Controller1')

    # 获取当前配置
    config_variant, *_ = iface.GetConfig('fcitx://config/addon/classicui')
    config_dict = dict(config_variant)

    # 修改 Theme 项
    config_dict['Theme'] = dbus.String(theme_folder_name)
    config_dict['DarkTheme'] = dbus.String(theme_folder_name)

    # 写回配置
    iface.SetConfig('fcitx://config/addon/classicui', dbus.Dictionary(config_dict, signature='sv'))
    iface.ReloadConfig()
    print(f"已切换到主题: {theme_folder_name}")

# debug
if __name__ == "__main__":
    change_theme("plasma")