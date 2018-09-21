from time import sleep
# Local Import
from src.ledcontrols import LedControls

class AlertProfiles(LedControls):
    def __init__(self):
        LedControls.__init__(self)

    def my_profile_static(self):
        color = {'lav': '784da5', 'teal': '3a698e'}  # Lavender, teal
        self.set_color('primary', color['lav'])
        self.set_color('secondary', color['teal'])

    def slack(self):
        self.set_breathe('all', 'ff0000', 10, 100)
        sleep(3)
        self.my_profile_static()

    def spotify(self):
        self.set_breathe('primary', '67d600', 10, 100)
        sleep(3.2)
        self.my_profile_static()

    def facebook(self):
        self.set_breathe('primary', '0061ff', 10, 100)
        sleep(3.2)
        self.my_profile_static()
