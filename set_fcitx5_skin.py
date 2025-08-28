#!/usr/bin/env python3
import os
from pathlib import Path
import dbus

# 主题搜索路径
THEME_DIRS = [
    Path.home() / ".local/share/fcitx5/themes",
    Path("/usr/share/fcitx5/themes")
]

def list_themes():
    themes = []
    for directory in THEME_DIRS:
        if directory.exists():
            for item in directory.iterdir():
                if item.is_dir() and (item / "theme.conf").exists():
                    themes.append(item.name)
    return sorted(set(themes))

def change_theme(theme_name):
    session_bus = dbus.SessionBus()
    fcitx_obj = session_bus.get_object('org.fcitx.Fcitx5', '/controller')
    iface = dbus.Interface(fcitx_obj, dbus_interface='org.fcitx.Fcitx.Controller1')

    # 获取当前配置
    config_variant, *_ = iface.GetConfig('fcitx://config/addon/classicui')
    config_dict = dict(config_variant)

    # 修改 Theme 项
    config_dict['Theme'] = dbus.String(theme_name)
    config_dict['DarkTheme'] = dbus.String(theme_name)

    # 写回配置
    iface.SetConfig('fcitx://config/addon/classicui', dbus.Dictionary(config_dict, signature='sv'))
    iface.ReloadConfig()
    print(f"已切换到主题: {theme_name}")

def main():
    themes = list_themes()
    if not themes:
        print("未找到可用主题，请检查主题目录。")
        return

    print("可用主题列表：")
    for idx, name in enumerate(themes, start=1):
        print(f"{idx}. {name}")

    try:
        choice = int(input("\n输入要切换的主题编号: "))
        if 1 <= choice <= len(themes):
            change_theme(themes[choice - 1])
        else:
            print("无效的编号")
    except ValueError:
        print("请输入数字编号")


if __name__ == "__main__":
    main()
