import stripe
import usb.core
import usb.util
import sys

VENDOR_ID = 0x0801
PRODUCT_ID = 0x001
DATA_SIZE = 337

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

buses = usb.busses()
for bus in buses:
    for device in bus.devices:
        if device.idVendor == VENDOR_ID and device.idProduct == PRODUCT_ID:
            print("Card Reader Initialized")
try:
    device.reset()
    device.set_configuration()
except usb.core.USBError as e:
    sys.exit("Could not set configuration: %s" % str(e))

endpoint = device[0][(0, 0)][0]

# wait for swipe

data = []
swiped = False
print("Please swipe your card...")
# while fault
while 1:
    try:
        data += device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        if not swiped:
            print("Reading...")
        swiped = True
    # debug error
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',) and swiped:
            if len(data) < DATA_SIZE:
                print("Bad swipe, try again. (%d bytes)" % len(data))
                print("Data: %s" % ''.join(map(chr, data)))
                data = []
                swiped = False
                continue
            else:
                break
