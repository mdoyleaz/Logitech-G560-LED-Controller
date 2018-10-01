import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

import json
from time import sleep

# Local Imports
from src.ledcontrols import LedControls


class AlertControls(LedControls):
    """
    Class is ran each time
    Profiles are loaded on ever pass of 'Glib.MainLoop' to keep the json file dynamic

    """
    def __init__(self):
        LedControls.__init__(self)

    def __call__(self, bus, message):
        # Retreives JSON
        self.get_profiles()
        # Sets LEDs to default profile
        self.default_profile()

        keys = ["app_name", "replaces_id", "app_icon", "summary",
                "body", "actions", "hints", "expire_timeout"]
        args = message.get_args_list()

        if len(args) >= 8:
            notification = dict([(keys[i], args[i]) for i in range(8)])

            app = notification['app_name'].lower()
            app_profile = self.profile_data['alerts'][app]

            if app is not "google-chrome":
                func = self.profile_data['alerts'][app]['function']

                exec(f"self.{func}({app_profile})")

                ### Non function needs to be fixed
            elif 'www.facebook.com' in notification['body']:
                exec(f"self.{func}({'facebook'})")
            else:
                pass

    def get_profiles(self):
        try:
            with open('profiles/alertprofiles.json') as profiles:
                self.profile_data = json.load(profiles)
        except Exception as e:
            print(e)

    def default_profile(self):
        [self.set_color(option, color) for option,
         color in self.profile_data['default']['ledoption'].items()]

    def flash(self, profile):
        led_options = profile['ledoption']

        for i in range(profile['length']):
            for option, colors in led_options.items():
                if len(colors) > 1:
                    [self.set_color(option, color) for color in colors]
                else:
                    self.set_color(option, '000000')
                    self.set_color(option, colors[0])

            sleep(float(profile['speed']))

        self.default_profile()


# Runs at runtime
if __name__ == '__main__':
    loop = DBusGMainLoop(set_as_default=True)

    session_bus = dbus.SessionBus()
    session_bus.add_match_string(
        "type='method_call',interface='org.freedesktop.Notifications',member='Notify',eavesdrop=true")
    session_bus.add_message_filter(AlertControls())


    GLib.MainLoop().run()
