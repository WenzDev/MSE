import sys
import usb.core
import usb.util

VENDOR_ID = 0x0801
PRODUCT_ID = 0x0001
DATA_SIZE = 337

# find the MagTek reader

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None:
    sys.exit("Could not find MagTek USB HID Swipe Reader.")

endpoint = device[0][(0, 0)][0]
data = []
swiped = False
print("Please swipe your card")
