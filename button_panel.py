import gi
gi.require_version("Gtk", "3.0")  # 如果你用的是 GTK 4，请改成 "4.0"
from gi.repository import Gtk

class ButtonPanel(Gtk.Frame):
    def __init__(self):
        super().__init__(label=None)

        self.set_shadow_type(Gtk.ShadowType.NONE)

        # 创建垂直按钮容器
        button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        button_box.set_valign(Gtk.Align.START)
        # button_box.set_margin_top(10)

        # 添加按钮
        for label in ["打开主题文件夹", "导入", "删除", "应用"]:
            btn = Gtk.Button(label=label)
            btn.set_size_request(100, 40)
            button_box.pack_start(btn, False, False, 0)

            # 可选：绑定事件（你可以在主程序中 connect）
            # btn.connect("clicked", self.on_button_clicked)

        # 将按钮容器添加到 Frame 中
        self.add(button_box)

    # 示例事件处理（可选）
    def on_button_clicked(self, button):
        print(f"点击了按钮：{button.get_label()}")
