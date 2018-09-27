import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from src.gtk_interface.main_window import BaseWin


win = BaseWin()
# Main "Box" to build over window
hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)

label_text = "Please select a color and press apply"
main_label = win.create_main_label(label_text)
hbox.pack_start(main_label, True, False, 0)

# Creates 'Box' to handle button widgets
btn_box = Gtk.Box(spacing=6)
hbox.pack_end(btn_box, True, True, 0) ## Packs box to end of 'hbox'

btn_color_select = win.create_btn_color_select()
btn_close = win.create_btn_close()

btn_box.pack_start(btn_color_select, False, False, 0)
btn_box.pack_end(btn_close, False, False, 0)

win.add(hbox)

## Runs window afer being built
win.show_all()
Gtk.main()
