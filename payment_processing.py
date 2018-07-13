import sys
from libusb1 import *
import usb.core


class magtek():
    def __init__(self):
        self.VENDOR_ID = 0x0801
        self.PRODUCT_ID = 0x0001
        self.DATA_SIZE = 337
        self.device = usb.core.find(idVendor=self.VENDOR_ID, idProduct=self.PRODUCT_ID)


if magtek().device is None:
    sys.exit("Could not find MagTek USB HID Swipe Reader")

endpoint = magtek().device[0][0, 0][0]

data = []