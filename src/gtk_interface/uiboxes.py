from gi.repository import Gtk

## Interface helper classes
from src.gtk_interface.uiwidgets import UiButtons
from src.gtk_interface.uiwidgets import UiLabels


class UiBoxes():
    def __init__(self):
        self.ui_buttons = UiButtons()
        self.ui_labels = UiLabels()

    def home_box(self):
        # Main "Box" to build over window
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        hbox.pack_end(vbox, True, True, 0)

        label_text = "Please select a color and press apply"
        main_label = self.ui_labels.create_label(label_text)
        vbox.pack_start(main_label, True, False, 0)

        # Creates 'Box' to handle button widgets
        btn_box = Gtk.Box(spacing=6)
        vbox.pack_end(btn_box, False, True, 0) ## Packs box to end of 'vbox'

        btn_color_select = self.ui_buttons.create_btn_color_select()
        btn_close = self.ui_buttons.create_btn_close_apply()

        btn_box.pack_start(btn_color_select, False, False, 0)
        btn_box.pack_end(btn_close, False, False, 0)

        return hbox

    def fake_box(self):
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        return hbox
