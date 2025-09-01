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

        self.buttons = {}

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
            # btn.set_sensitive(False)
            self.buttons[label] = btn  # 保存按钮引用进字典
            btn.connect("clicked", handlers[label])

        # 将按钮容器添加到 Frame 中
        self.add(button_box)

        self.refresh() # 初始化完成后立刻刷新一次控件状态，获取最新数据

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
        change_theme(self.parent.picked_theme)
        self.parent.default_theme = self.parent.picked_theme
        self.parent.theme_frame.refresh()
        self.parent.panel_frame.refresh()

    def refresh(self):
        """根据父窗口状态刷新按钮状态"""

        # 防止删除系统级默认皮肤，另：目前只打算使用名称辨别，但是会使同样命名的文件夹无法删除
        # 一般来说不会出现这种情况，后面如果出问题了，可能会考虑添加新的控制变量，检测系统路径而不是文件夹名称
        if self.parent.picked_theme == "default" or self.parent.picked_theme == "default-dark":
            self.buttons["删除"].set_sensitive(False)
        else:
            self.buttons["删除"].set_sensitive(True)

        # 选择当前主题时禁用“应用”
        if self.parent.picked_theme == self.parent.default_theme:
            self.buttons["应用"].set_sensitive(False)
        else:
            self.buttons["应用"].set_sensitive(True)