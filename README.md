# Logitech-G560-LED

Library for managing LEDs of the Logitech G560 speakers in Linux

* * *

## Requirements:

-   Python 3.6
-   pyusb
-   RPyC
-   GTK 3

* * *

## Instructions:

##### Do to libusb, this library requires root access.

-   RPC service needs to be run to handle libusb, this needs to be started as root this will be added as a system service eventually
    ```bash
    $ sudo python3 'g560_service.py'
    ```


-   I am working on building LED alerts, this can be accessed with:
    ```bash
    $ python3 'g560_alerts.py'
    ```


-   A GUI implementation can be accessed by running
    ```bash
    $ python3 'g560_gtk.py'
    ```

* * *

## Project Goal:

> The goal of this project is to build out an interface for handling Logitech devices, including:/
>
> -   Alerts
> -   GTK interface
> -   Integrate in Gnome with shell extensions
> -   Support for other Logitech devices, such as: Mice, Keyboards, or other LED controlled devices.

* * *
