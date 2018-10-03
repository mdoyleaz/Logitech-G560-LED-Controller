import json
from gi.repository import Gtk, Gdk

# Core classes
from src.ledcontrols import LedControls


class UiButtons():
    def __init__(self):
        self.led_control = LedControls()
        self.led_options = {}

    def get_led_profile(self, option):

        try:
            with open('profiles/ledprofiles.json') as profiles:
                profile_data = json.load(profiles)

                return profile_data['profiles']['default']['ledoption'][option]
        except Exception as e:
            print("Error loading JSON: ", e)


    def create_btn_color_select(self, option):
        led_color = self.get_led_profile(option)
        self.led_options[option] = led_color

        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

        # Color Selection Button
        self.btn_color_sel = Gtk.ColorButton()
        color = Gdk.RGBA()

        print(color)
        self.btn_color_sel.set_rgba(color)
        self.btn_color_sel.connect(
            "color-set", self.on_color_selector_click, option)
        hbox.pack_start(self.btn_color_sel, False, False, 2)

        return hbox

    def create_btn_close_apply(self):
        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)

        # Apply selected color
        btn_apply = Gtk.Button(label="Apply")
        btn_apply.connect("clicked", self.on_apply_click)
        hbox.pack_start(btn_apply, False, False, 0)

        # Closes application
        btn_close = Gtk.Button(label="Goodbye")
        btn_close.connect("clicked", Gtk.main_quit)
        hbox.pack_end(btn_close, False, False, 0)

        return hbox

    def on_color_selector_click(self, widget, option):
        color = widget.get_color()

        red = int(color.red / 256)
        green = int(color.green / 256)
        blue = int(color.blue / 256)

        self.led_options[option] = "{:02x}{:02x}{:02x}".format(
            red, green, blue)

    def on_apply_click(self, widget):
        if len(self.led_options) > 0:
            for option, color in self.led_options.items():
                self.led_control.set_color(option, color)

            self.led_options = {}


class UiHelperWidgets:
    @staticmethod
    def create_list_row(text, button):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        label = Gtk.Label(text, xalign=0)
        hbox.pack_start(label, True, True, 0)

        hbox.pack_start(button, False, True, 0)

        return row

    @staticmethod
    def create_label(text):
        hbox_text = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        label = Gtk.Label()
        label.set_text(text)
        hbox_text.pack_start(label, False, False, 0)

        return hbox_text
