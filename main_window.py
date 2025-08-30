import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
from gi.repository import Gtk, Pango,Gdk
from theme_selector import ThemeSelector

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Fcitx5皮肤管理器")
        self.set_default_size(800, 500)

        grid = Gtk.Grid()
        grid.set_column_spacing(20)
        grid.set_row_spacing(10)
        grid.set_margin_top(10)
        grid.set_margin_bottom(10)
        grid.set_margin_start(10)
        grid.set_margin_end(10)

        # 左侧：主题选择器区域
        # theme_frame = Gtk.Frame()
        theme_frame = ThemeSelector()
        theme_frame.set_hexpand(True)
        theme_frame.set_vexpand(True)
        theme_frame.set_size_request(500, -1)  # 限制最大宽度
        theme_frame.add(Gtk.Label(label="这里是主题预览或选择器"))
        grid.attach(theme_frame, 0, 0, 1, 1)

        # 右侧：按钮区域
        button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)  # 增加按钮间距
        button_box.set_valign(Gtk.Align.START)
        button_box.set_margin_top(10)  # 顶部对齐左侧内容

        for label in ["设置", "导入", "删除", "应用"]:
            btn = Gtk.Button(label=label)
            btn.set_size_request(100, 40)  # 设置按钮尺寸
            button_box.pack_start(btn, False, False, 0)

        grid.attach(button_box, 1, 0, 1, 1)

        self.add(grid)


