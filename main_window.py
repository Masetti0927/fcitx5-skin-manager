import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
from gi.repository import Gtk, Pango,Gdk
from theme_selector import ThemeSelector
from button_panel import ButtonPanel
from theme_utils import get_themes,get_default_theme

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Fcitx5主题管理器")
        self.default_theme = get_default_theme()
        self.theme_list = get_themes()
        self.picked_theme = self.default_theme
        # self.picked_path =
        self.set_default_size(800, 500)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(20)
        self.grid.set_row_spacing(10)
        self.grid.set_margin_top(20)
        self.grid.set_margin_bottom(20)
        self.grid.set_margin_start(20)
        self.grid.set_margin_end(20)

        # 左侧：主题选择器区域
        self.theme_frame = ThemeSelector(self)
        self.theme_frame.set_hexpand(True)
        self.theme_frame.set_vexpand(True)
        self.theme_frame.set_size_request(500, -1)  # 限制最大宽度
        self.grid.attach(self.theme_frame, 0, 0, 1, 1)

        # 右侧：交互按钮区域
        self.panel_frame = ButtonPanel(self)
        self.grid.attach(self.panel_frame, 1, 0, 1, 1)

        self.add(self.grid)


