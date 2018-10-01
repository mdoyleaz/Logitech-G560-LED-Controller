from gi.repository import Gtk, Gdk

## Core classes
from src.ledcontrols import LedControls


class UiButtons():
    def __init__(self):
        self.led_control = LedControls()

    def create_btn_color_select(self):
        # https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html
        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

        ## Color Selection Button
        self.btn_color_sel = Gtk.ColorButton()
        color = Gdk.RGBA()
        self.btn_color_sel.set_rgba(color)
        self.btn_color_sel.connect("color-set", self.on_color_selector_click)
        hbox.pack_start(self.btn_color_sel, False, False, 2)

        return hbox

    def create_btn_close_apply(self):
        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)

        ## Apply selected color
        btn_apply = Gtk.Button(label="Apply")
        btn_apply.connect("clicked", self.on_apply_click)
        hbox.pack_end(btn_apply, False, False, 0)

        ## Closes application
        btn_close = Gtk.Button(label="Goodbye")
        btn_close.connect("clicked", Gtk.main_quit)
        hbox.pack_end(btn_close, False, False, 0)

        return hbox

    def on_color_selector_click(self, widget):
        color = self.btn_color_sel.get_rgba()

        red = int(color.red * 256)
        green = int(color.green * 256)
        blue = int(color.blue * 256)

        self.hex_color = "{:02x}{:02x}{:02x}".format(red, green, blue)

    def on_apply_click(self, widget):
        if self.hex_color is not 0:
            self.led_control.set_color('all', self.hex_color)


class UiLabels:
    @staticmethod
    def create_label(text):
        hbox_text = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        label = Gtk.Label()
        label.set_text(text)
        hbox_text.pack_start(label, False, False, 0)

        return hbox_text
