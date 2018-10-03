from gi.repository import Gtk

## Interface helper classes
from src.gtk_interface.uiboxes import UiBoxes


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        # Inherits Gtk.Window
        Gtk.Window.__init__(self, title="Logitech LED Controls")
        self.set_default_size(640, 380)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(2)
        self.connect("destroy", Gtk.main_quit)

        # Helper classes
        self.uiboxes = UiBoxes()

        # Builds sidebar stack for main window
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
        sidebar = self.create_sidebar()
        hbox.pack_end(sidebar, True, True, 1)

        self.add(hbox)

    def create_sidebar(self):
        vbox = Gtk.Box(homogeneous=False,
                       orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

        stack = Gtk.Stack()
        stack.set_hhomogeneous(True)

        stack.add_titled(self.uiboxes.home_box(), "Home", "Home")
        # stack.add_titled(self.uiboxes.fake_box(),
        #                  "Color Profiles", "Color Profiles")
        # stack.add_titled(self.uiboxes.fake_box(),
        #                  "Alert Profiles", "Alert Profiles")
        # stack.add_titled(self.uiboxes.fake_box(), "label", "A label")

        stack_sidebar = Gtk.StackSidebar()
        stack_sidebar.set_stack(stack)
        stack_sidebar.set_size_request((640/5), 300)

        vbox.pack_start(stack_sidebar, False, True, 0)
        vbox.pack_start(stack, True, True, 0)

        return vbox
