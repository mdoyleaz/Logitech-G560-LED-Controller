import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

from time import sleep

## Local Imports
from profiles.alertsprofile import AlertProfiles


class LedAlerts():
    def alerts(bus, message):
        profile = AlertProfiles()

        keys = ["app_name", "replaces_id", "app_icon", "summary",
                "body", "actions", "hints", "expire_timeout"]
        args = message.get_args_list()

        if len(args) == 8:
            notification = dict([(keys[i], args[i]) for i in range(8)])
            print(notification["app_name"])

            if notification['app_name'] == 'Slack':
                profile.slack()
            elif notification['app_name'] == 'Spotify':
                profile.spotify()
            elif 'facebook' in notification['app_name']:
                profile.facebook()

### Runs at runtime
if __name__ == '__main__':
    loop = DBusGMainLoop(set_as_default=True)

    session_bus = dbus.SessionBus()
    session_bus.add_match_string(
        "type='method_call',interface='org.freedesktop.Notifications',member='Notify',eavesdrop=true")
    session_bus.add_message_filter(LedAlerts.alerts)

    GLib.MainLoop().run()
