# theme_selector.py
import gi
import os
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
from gi.repository import Gtk, Pango,Gdk

from theme_utils import get_themes,get_default_theme

class ThemeSelector(Gtk.Frame):
    def __init__(self):
        super().__init__(label="主题选择器")

        # 是否为默认（图标名）、皮肤名、作者、描述、路径
        self.liststore = Gtk.ListStore(str, str, str, str, str)
        self.treeview = Gtk.TreeView(model=self.liststore)
        self.default_theme_name = get_default_theme()

        self._setup_columns()
        self._setup_scroll()
        self.load_themes()

    def _setup_columns(self):
        renderer = Gtk.CellRendererText()
        icon_renderer = Gtk.CellRendererPixbuf()
        renderer.set_property("wrap-mode", Pango.WrapMode.WORD_CHAR)
        renderer.set_property("wrap-width", 300)

        self.treeview.append_column(Gtk.TreeViewColumn("当前", icon_renderer, icon_name=0))
        self.treeview.append_column(Gtk.TreeViewColumn("主题", renderer, text=1))
        self.treeview.append_column(Gtk.TreeViewColumn("作者", renderer, text=2))
        self.treeview.append_column(Gtk.TreeViewColumn("描述", renderer, text=3))
        self.treeview.append_column(Gtk.TreeViewColumn("路径", renderer, text=4))

        self.treeview.connect("button-press-event", self.on_row_clicked)


    def _setup_scroll(self):
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll.add(self.treeview)
        self.add(scroll)

    def load_themes(self):
        default_name = self.default_theme_name  # 比如 "default"
        for name, author, desc, path in get_themes():
            icon = "emblem-ok-symbolic" if os.path.basename(path) == default_name else None
            self.liststore.append([icon,name, author, desc, path])

    def on_row_activated(self, treeview, path, column):
        model = treeview.get_model()
        tree_iter = model.get_iter(path)
        name = model.get_value(tree_iter, 1)
        author = model.get_value(tree_iter, 2)
        description = model.get_value(tree_iter, 3)
        folder_path = model.get_value(tree_iter, 4)
        print(f"你选择了皮肤：{name}\n作者：{author}\n描述：{description}\n路径：{folder_path}")

    def on_row_clicked(self, treeview, event):
        if event.button == 1 and event.type == Gdk.EventType.BUTTON_PRESS:  # 左键单击
            path_info = treeview.get_path_at_pos(int(event.x), int(event.y))
            if path_info is not None:
                path, column, cell_x, cell_y = path_info
                self.on_row_activated(treeview, path, column)

