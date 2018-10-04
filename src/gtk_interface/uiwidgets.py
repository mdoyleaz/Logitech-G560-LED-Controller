import json
from gi.repository import Gtk, Gdk

# Core classes
from src.ledcontrols import LedControls


class UiButtons():
    def __init__(self):
        self.led_control = LedControls()
        self.led_options = {}

    def create_btn_color_select(self, option, profile='default'):
        led_color = WidgetHelpers.get_led_profile(profile)

        self.led_options[option] = led_color[option]
        hbox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

        # Color Selection Button
        self.btn_color_sel = Gtk.ColorButton()
        # Converts HEX color to RGB
        rgb = tuple(float(int(self.led_options[option][i:i + 6 // 3], 16) / 255)
                    for i in range(0, 6, 6 // 3))

        color = Gdk.RGBA(rgb[0], rgb[1], rgb[2])

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
        color = widget.get_rgba()

        red = int(color.red * 255)
        green = int(color.green * 255)
        blue = int(color.blue * 255)

        self.led_options[option] = "{:02x}{:02x}{:02x}".format(
            red, green, blue)

    def on_apply_click(self, widget):
        if len(self.led_options) > 0:
            for option, color in self.led_options.items():
                self.led_control.set_color(option, color)
            WidgetHelpers.put_led_profile('current', self.led_options)


class WidgetHelpers:
    @staticmethod
    def get_led_profile(profile):
        try:
            with open('profiles/profilesettings.json') as profiles:
                loaded_profile = json.load(profiles)
                loaded_profile = loaded_profile['profiles'][profile]

                return loaded_profile

        except Exception as e:
            print("Error loading JSON: ", e)

    def put_led_profile(profile, data):
        try:
            with open('profiles/profilesettings.json', 'r+') as profiles:
                loaded_profile = json.load(profiles)
                loaded_profile['profiles'][profile] = data

                profiles.seek(0)
                json.dump(loaded_profile, profiles, indent=4)

        except Exception as e:
            print("Error loading JSON: ", e)

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
