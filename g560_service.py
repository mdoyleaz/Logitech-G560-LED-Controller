import usb.core
import usb.util

import rpyc
from rpyc.utils.server import ThreadedServer

from binascii import unhexlify
from time import sleep


class G560NotFound(BaseException):
    """
    Custom Exception for missing device
    """

    pass


class UsbOperations(rpyc.Service):
    """
    USB Object for driver management and data transfer
    """

    def __init__(self):
        id_vendor = 0x046d  # Logitech USB Vendor ID
        id_product = 0x0a78  # G560 USB Product ID

        # Initializes the USB device to be called throughout the script
        self.dev = usb.core.find(idVendor=id_vendor, idProduct=id_product)

        # Check to see if device was initialized properly
        if self.dev is None:
            raise G560NotFound("Please verify device is connected")

        self.bm_req_type = 0x21  # bm request type
        self.b_req = 0x09  # Request field for setup packet
        self.wvalue = 0x0211  # Value field for setup packet
        self.windex = 0x0002  # Index field for setup packet

    def detach_driver(self):
        try:
            if self.dev.is_kernel_driver_active(self.windex):
                self.dev.detach_kernel_driver(self.windex)
        except usb.core.USBError as e:
            print("Error detaching driver: ", e)
            return False

        return True

    def attach_driver(self):
        try:
            usb.util.release_interface(self.dev, 2)
            self.dev.attach_kernel_driver(2)
        except Exception as e:
            print("Could not renable driver: ", e)

    def data_transfer(self, data_list):
        self.detach_driver()

        if len(data_list) > 0:
            for data in data_list:
                data = unhexlify(data)

                self.dev.ctrl_transfer(
                    self.bm_req_type, self.b_req, self.wvalue, self.windex, data)

                sleep(.006)
        else:
            data = unhexlify(data[0])

            self.dev.ctrl_transfer(
                self.bm_req_type, self.b_req, self.wvalue, self.windex, data)

        self.attach_driver()


if __name__ == '__main__':
    server = ThreadedServer(UsbOperations, port=18812, protocol_config={
                            "allow_public_attrs": True})
    server.start()
