# theme_selector.py
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
from gi.repository import Gtk, Pango

from theme_utils import get_themes

class ThemeSelector(Gtk.Window):
    def __init__(self):
        super().__init__(title="Fcitx5 皮肤选择器")
        self.set_border_width(10)
        self.set_default_size(600, 300)

        self.liststore = Gtk.ListStore(str, str, str)
        self.treeview = Gtk.TreeView(model=self.liststore)

        self._setup_columns()
        self._setup_scroll()
        self.load_themes()

    def _setup_columns(self):
        renderer = Gtk.CellRendererText()
        renderer.set_property("wrap-mode", Pango.WrapMode.WORD_CHAR)
        renderer.set_property("wrap-width", 300)

        self.treeview.append_column(Gtk.TreeViewColumn("皮肤", renderer, text=0))
        self.treeview.append_column(Gtk.TreeViewColumn("描述", renderer, text=1))
        self.treeview.append_column(Gtk.TreeViewColumn("路径", renderer, text=2))

        self.treeview.connect("row-activated", self.on_row_activated)

    def _setup_scroll(self):
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll.add(self.treeview)
        self.add(scroll)

    def load_themes(self):
        for display_name, path, desc in get_themes():
            self.liststore.append([display_name, desc, path])

    def on_row_activated(self, treeview, path, column):
        model = treeview.get_model()
        tree_iter = model.get_iter(path)
        name = model.get_value(tree_iter, 0)
        folder_path = model.get_value(tree_iter, 2)
        description = model.get_value(tree_iter, 1)
        print(f"你选择了皮肤：{name}\n路径：{folder_path}\n描述：{description}")
