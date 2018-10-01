import rpyc

# Local Imports
from .valuecheck import ValueCheck


class LedControls(object):
    """
    Controls for G560 LEDs
    """

    def __init__(self):
        # UsbOperations.__init__(self)
        self.led_id = {'left_secondary': '00', 'right_secondary': '01',
                       'left_primary': '02', 'right_primary': '03'}
        self.conn = rpyc.connect("localhost", port=17657)

    def build_option_list(self, led_option):
        """
        Builds list of leds based on value of of 'led_option'
        Options:
        'all': Selects all LEDs
        'primary': Selects both primary LEDs
        'secondary': Selects both secondary LEDs
        'left': Selects both left speaker LEDs
        'right': Selects both right speaker LEDs
        """

        if led_option == 'all':
            led_list = self.led_id
        else:
            led_list = [key for key in self.led_id.keys()
                        if led_option.lower() in key]

        if len(led_list) is 0:
            ValueCheck.led_option(led_option)

        return led_list

    def set_color(self, led_option, color):
        control_data = '11ff043a{}01{}02'

        ValueCheck.check_color(color)

        if led_option not in self.led_id:
            led_list = self.build_option_list(led_option)

            data = [control_data.format(
                self.led_id[led], color) for led in led_list]
        else:
            data = [control_data.format(self.led_id[led_option], color)]

        self.conn.root.data_transfer(data)

    def set_off(self, led_option):
        self.set_color(led_option, '000000')

    def set_color_cycle(self, led_option, speed=8, brightness=75):
        control_data = '11ff043e{}020000000000{}f8{}'

        speed = ValueCheck.cycle_speed(speed)
        brightness = ValueCheck.brightness(brightness)

        if led_option not in self.led_id:
            led_list = self.build_option_list(led_option)

            data = [control_data.format(
                self.led_id[led], speed, brightness) for led in led_list]
        else:
            data = [control_data.format(
                self.led_id[led_option], speed, brightness)]

        self.conn.root.data_transfer(data)

    def set_breathe(self, led_option, color, speed=5, brightness=100):
        control_data = '11ff043e{}04{}{}f000{}'

        color = ValueCheck.check_color(color)
        speed = ValueCheck.breathe_speed(speed)
        brightness = ValueCheck.brightness(brightness)

        if led_option not in self.led_id:
            led_list = self.build_option_list(led_option)
            data = [control_data.format(
                self.led_id[led], color, speed, brightness) for led in led_list]
        else:
            data = [control_data.format(
                self.led_id[led_option], color, speed, brightness)]
            print(data)


        self.conn.root.data_transfer(data)
