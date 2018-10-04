from gi.repository import Gtk

# Interface helper classes
from src.gtk_interface.uiwidgets import UiButtons
from src.gtk_interface.uiwidgets import WidgetHelpers


class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        Gtk.ListBoxRow.__init__(self)
        self.data = data
        self.add(Gtk.Label(data))


class UiBoxes():
    def __init__(self):
        self.ui_buttons = UiButtons()
        self.ui_widget = WidgetHelpers()

    def home_box(self):
        # Main "Box" to build over window
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_end(vbox, True, True, 10)

        color_list_box = self.color_list_box('current')

        vbox.pack_start(color_list_box, False, False, 10)

        # Creates 'Box' to handle button widgets
        btn_box = Gtk.Box(spacing=6)
        vbox.pack_end(btn_box, False, True, 0)  # Packs box to end of 'vbox'

        btn_close = self.ui_buttons.create_btn_close_apply()
        btn_box.pack_end(btn_close, False, False, 0)

        return hbox

    def fake_box(self):
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        return hbox

    def color_list_box(self, profile):
        main_options = ['primary', 'secondary', ]
        led_options = ['right_primary', 'left_primary',
                       'right_secondary', 'left_secondary']
        box_fill = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        listbox = Gtk.ListBox()
        box_fill.pack_start(listbox, True, False, 0)

        for option in led_options:
            button = self.ui_buttons.create_btn_color_select(option, profile)

            if '_' in option:
                option = option.replace('_', ' ')

            row = self.ui_widget.create_list_row(
                f"{option.title()} LED", button)

            listbox.add(row)

        def sort_func(row_1, row_2, data, notify_destroy):
            return row_1.data.lower() > row_2.data.lower()

        def filter_func(row, data, notify_destroy):
            return False if row.data == 'Fail' else True

        def on_row_activated(listbox_widget, row):
            print(row.data)

        return box_fill
