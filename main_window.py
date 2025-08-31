import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
from gi.repository import Gtk, Pango,Gdk
from theme_selector import ThemeSelector
from button_panel import ButtonPanel

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Fcitx5主题管理器")
        self.set_default_size(800, 500)

        grid = Gtk.Grid()
        grid.set_column_spacing(20)
        grid.set_row_spacing(10)
        grid.set_margin_top(20)
        grid.set_margin_bottom(20)
        grid.set_margin_start(20)
        grid.set_margin_end(20)

        # 左侧：主题选择器区域
        theme_frame = ThemeSelector()
        theme_frame.set_hexpand(True)
        theme_frame.set_vexpand(True)
        theme_frame.set_size_request(500, -1)  # 限制最大宽度
        grid.attach(theme_frame, 0, 0, 1, 1)

        # 右侧：交互按钮区域
        panel = ButtonPanel()
        grid.attach(panel, 1, 0, 1, 1)

        self.add(grid)


