import locale
import os
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
from gi.repository import Pango
from gi.repository import Gtk

from config import THEME_DIRS


def read_metadata(path):
    '''
    获取theme.conf的数据
    :param path: 某个theme文件夹的路径
    :return: 该皮肤theme.conf当中的metadata信息，用于显示皮肤名字和描述
    '''
    metadata = {}
    lang = locale.getlocale()  # 获取系统语言，如 'zh_CN'
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
                key, value = key.strip(), value.strip()
                metadata[key] = value
    # 语言优先级：Name[本地语言] → Name
    localized_key = f"Name[{lang[0]}]"
    display_name = metadata.get(localized_key) or metadata.get("Name")
    metadata["DisplayName"] = display_name
    metadata["Description"] = metadata.get("Description", "")
    return metadata

def get_themes():
    '''
    :return: 返回系统当中的theme字典
    '''
    themes = []
    for theme_dir in THEME_DIRS:
        if not os.path.isdir(theme_dir):
            continue
        for folder in os.listdir(theme_dir):
            conf_path = os.path.join(theme_dir, folder, "theme.conf")
            meta = read_metadata(conf_path)
            if meta:
                themes.append((meta["DisplayName"], conf_path.rsplit("/", 2)[0] + "/" + folder, meta["Description"]))
    return themes

class ThemeSelector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fcitx5 皮肤选择器")
        self.set_border_width(10)
        self.set_default_size(600, 300)

        # 展示名, 文件夹路径, 描述
        self.liststore = Gtk.ListStore(str, str, str)
        self.treeview = Gtk.TreeView(model=self.liststore)

        renderer = Gtk.CellRendererText()
        # 为过长的描述末尾添加省略
        # renderer.set_property("ellipsize", Pango.EllipsizeMode.END)
        renderer.set_property("wrap-mode", Pango.WrapMode.WORD_CHAR) #为过长的描述自动换行
        renderer.set_property("wrap-width", 300)
        self.treeview.append_column(Gtk.TreeViewColumn("皮肤", renderer, text=0))
        self.treeview.append_column(Gtk.TreeViewColumn("描述", renderer, text=1))
        self.treeview.append_column(Gtk.TreeViewColumn("路径", renderer, text=2))

        self.treeview.connect("row-activated", self.on_row_activated)

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll.add(self.treeview)
        self.add(scroll)

        self.load_themes()

    def load_themes(self):
        for display_name, path, desc in get_themes():
            self.liststore.append([display_name, desc,path])

    def on_row_activated(self, treeview, path, column):
        model = treeview.get_model()
        tree_iter = model.get_iter(path)
        name = model.get_value(tree_iter, 0)
        folder_path = model.get_value(tree_iter, 1)
        description = model.get_value(tree_iter, 2)
        print(f"你选择了皮肤：{name}\n路径：{folder_path}\n描述：{description}")

if __name__ == "__main__":
    win = ThemeSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()