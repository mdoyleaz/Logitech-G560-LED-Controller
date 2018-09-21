from src.ledcontrols import LedControls
from src.valuecheck import ValueCheck

if __name__ == '__main__':
    def my_profile_breathe():
        color={'lav': 'c159f9', 'teal': '3a698e'}  # Lavender, teal
        g.set_breathe('primary', color['lav'])
        g.set_breathe('secondary', color['teal'])

    g=LedControls()

    def my_profile_static():
        color={'lav': '784da5', 'teal': '3a698e'}  # Lavender, teal
        g.set_color('primary', color['lav'])
        g.set_color('secondary', color['teal'])

    g=LedControls()

    if not g.detach_driver():
        exit()

    my_profile_static()

    while True:
        color = input("Enter hex color code(ex 'ff3344'): ")

        print("\nLED Options:\n\
        'all': Selects all LEDs \n\
        'primary': Selects both primary LEDs\n\
        'secondary': Selects both secondary LEDs \n\
        'left': Selects both left speaker LEDs \n\
        'right': Selects both right speaker LEDs\n\
        ['left_secondary', 'right_secondary', 'left_primary', 'right_primary']\n")

        led_option = input("Enter led/led set to change: ")

        print(int(color, 16))
        g.set_color(led_option, color)
