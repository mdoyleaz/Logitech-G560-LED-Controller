import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

## Local
from src.ledcontrols import LedControls

HEX_COLOR = 000000

class BaseWin(Gtk.ApplicationWindow):
    def __init__(self):
        # Inherits Gtk.Window
        Gtk.Window.__init__(self, title="Logitech LED Controls")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(1)
        self.connect("destroy", Gtk.main_quit)

        self.hex_color = 0

        self.led_control = LedControls()

    def create_btn_color_select(self):
        # https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html

        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)

        btn_color_sel = Gtk.Button(label="Select Color")
        btn_color_sel.connect("clicked", self.on_color_selector_click)
        hbox.pack_start(btn_color_sel, False, False, 2)

        btn_apply = Gtk.Button(label="Apply")
        btn_apply.connect("clicked", self.on_apply_click)
        hbox.pack_end(btn_apply, False, False, 2)

        return hbox

    def create_btn_close(self):
        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)

        btn_close = Gtk.Button(label="Goodbye")
        btn_close.connect("clicked", Gtk.main_quit)
        hbox.pack_end(btn_close, False, False, 0)

        return hbox

    def create_main_label(self, text):
        hbox_text = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        label = Gtk.Label()
        label.set_text(text)
        hbox_text.pack_start(label, False, False, 0)

        return hbox_text


    def on_color_selector_click(self, widget):
        dialog = Gtk.ColorSelectionDialog("Please choose a file", self,
                                          (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                           Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Color Selection Opened")
            color = dialog.get_color_selection().get_current_color()

            red = int(color.red / 256)
            green = int(color.green / 256)
            blue = int(color.blue / 256)

            hex_color = "{:02x}{:02x}{:02x}".format(red, green, blue)

            self.hex_color = hex_color

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_apply_click(self, widget):
        print(self.hex_color)
        if self.hex_color is not 0:
            self.led_control.set_color('all', self.hex_color)
