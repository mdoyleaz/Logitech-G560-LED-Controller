class ValueCheck:
    def led_option(led_option):
        raise ValueError(f"Invalid Option: ['{led_option}']")

    # Needs to raise error if index not met
    def check_color(color):
        color_int = int(color, 16)
        color_max = 16777215

        if color_int < 0 or color_int > color_max:
            raise ValueError(f"Invalid Color Option: #{color}")

        return color

    def cycle_speed(speed):
        if speed >= 0 and speed <= 10:
            hex_speed = "0x{:02x}".format(255 - int(speed * 25.5))[2:]
        else:
            raise ValueError(
                "Error: Speed value does not meet requirements '0 - 10'")

        return str(hex_speed)

    def breathe_speed(speed):
        if speed >= 5 and speed <= 10:
            hex_speed = "0x{:02x}".format(16 - int(speed))[2:]
        elif speed >= 0 and speed < 5:
            hex_speed = "0x{:02x}".format(24 - int(speed))[2:]
        else:
            raise ValueError(
                "Error: Speed value does not meet requirements '0 - 10'")

        return str(hex_speed)

    def brightness(brightness):
        if brightness >= 0 and brightness <= 100:
            hex_brightness = "0x{:02x}".format(int(brightness*2.559))[2:]
        else:
            raise ValueError(
                "ERROR: Brightness value does not meet rquirements 0 - 100")

        return str(hex_brightness)
