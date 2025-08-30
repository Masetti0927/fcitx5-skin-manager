# main.py
from theme_gui import ThemeSelector
from gi.repository import Gtk

def main():
    win = ThemeSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
