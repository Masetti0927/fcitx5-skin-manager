import subprocess
import os


import gi
gi.require_version("Gtk", "3.0")  # 如果你用的是 GTK 4，请改成 "4.0"
from gi.repository import Gtk
from config import  THEME_DIRS
from theme_utils import change_theme

class ButtonPanel(Gtk.Frame):
    def __init__(self,parent_window):
        super().__init__(label=None)
        self.set_shadow_type(Gtk.ShadowType.NONE)
        self.parent = parent_window

        # 创建垂直按钮容器
        button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        button_box.set_valign(Gtk.Align.START)

        # 设置按钮回调
        handlers = {
            "打开主题文件夹": self.on_open_folder,
            "导入": self.on_import,
            "删除": self.on_delete,
            "应用": self.on_apply,
        }
        # 添加按钮
        for label in ["打开主题文件夹", "导入", "删除", "应用"]:
            btn = Gtk.Button(label=label)
            btn.set_size_request(100, 40)
            button_box.pack_start(btn, False, False, 0)

            # 绑定事件
            btn.connect("clicked", handlers[label])

        # 将按钮容器添加到 Frame 中
        self.add(button_box)

    def on_open_folder(self,button):
        path = os.path.expanduser(THEME_DIRS[0])
        if os.path.exists(path):
            subprocess.Popen(["xdg-open", path])
        else:
            print("路径不存在：", path)

    def on_import(self):
        pass

    def on_delete(self):
        pass

    def on_apply(self,button):
        change_theme(self.parent.default_theme)
        self.parent.theme_frame.refresh()